#!/usr/bin/env python3
"""Descarga datos municipales del SNIS y los guarda directamente como Parquet."""

from __future__ import annotations

import argparse
import os
import unicodedata
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from functools import cache
from io import StringIO
from pathlib import Path
from threading import Event

import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import requests
from bs4 import BeautifulSoup, Tag
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


DIRECTORY = Path(__file__).resolve().parent
SOURCES_FILE = DIRECTORY / "fuentes.csv"
VARIABLES_DIRECTORY = DIRECTORY / "dimensiones" / "variables"
MUNICIPALITIES_DIRECTORY = DIRECTORY / "dimensiones" / "establecimientos"
DATA_DIRECTORY = DIRECTORY / "datos"
INDEX_FILE = DIRECTORY / "indice.csv"

# Los formularios de producción y vigilancia usan controles distintos para
# seleccionar una variable. El resto de la navegación es común.
VARIABLE_CONTROLS = {
    "301": "ctl00$MainContent$WebPanel2$list_subvariable",
    "301a": "ctl00$MainContent$WebPanel2$list_subvariable",
    "301b": "ctl00$MainContent$WebPanel2$list_subvariable",
    "302": "ctl00$MainContent$WebPanel2$Lista_subvar",
    "302a": "ctl00$MainContent$WebPanel2$Lista_subvar",
    "302b": "ctl00$MainContent$WebPanel2$Lista_subvar",
}

CONTROLS = {
    "gestion": "ctl00$MainContent$WebPanel2$List_gestion",
    "grupo": "ctl00$MainContent$WebPanel2$List_grvar",
    "agregacion": "ctl00$MainContent$WebPanel2$Grupo",
    "departamento": "ctl00$MainContent$WebPanel2$list_Depto",
    "mes": "ctl00$MainContent$WebPanel2$List_mes",
    "semana": "ctl00$MainContent$WebPanel2$Listbox1",
    "procesar": "ctl00$MainContent$WebPanel2$Button1",
}

SELECTORS = {
    "gestion": "#MainContent_WebPanel2_List_gestion option",
    "departamento": "#MainContent_WebPanel2_list_Depto option",
    "mes": "#MainContent_WebPanel2_List_mes option",
    "semana": "#MainContent_WebPanel2_Listbox1 option",
    "tabla": "#G_MainContentxWebPanel3xmydatagrid",
}

OUTPUT_COLUMNS = (
    "gestion",
    "periodo",
    "municipio_codigo",
    "poblacion",
    "valor",
)

INDEX_COLUMNS = (
    "formulario",
    "gestion",
    "grupo_codigo",
    "grupo",
    "variable_codigo",
    "variable",
    "archivo",
    "descargado",
    "filas",
    "error",
)

# No hay estructura de establecimientos para 2001--2004. La de 2005 es la
# referencia histórica más próxima y permite conservar el código municipal.
MUNICIPALITY_FALLBACKS = {year: 2005 for year in range(2001, 2005)}

TIMEOUT = (10, 120)
MAX_WORKERS = 6
VARIABLE_ATTEMPTS = 3
MAX_FAILURES = 10
STOP_EVENT = Event()


@dataclass(frozen=True)
class Source:
    formulario: str
    gestion: int
    url: str
    periodo: str


@dataclass(frozen=True)
class Variable:
    grupo_codigo: str
    variable_codigo: str


@dataclass(frozen=True)
class Task:
    source: Source
    variable: Variable


@dataclass(frozen=True)
class Municipality:
    codigo: str
    departamento: str


def task_label(task: Task) -> str:
    source, variable = task.source, task.variable
    return (
        f"{source.formulario} {source.gestion} "
        f"{variable.grupo_codigo}/{variable.variable_codigo}"
    )


def load_sources() -> tuple[Source, ...]:
    """Lee la definición declarativa y comprueba su clave primaria."""
    frame = pd.read_csv(SOURCES_FILE, dtype="string", keep_default_na=False)
    if frame.duplicated(["formulario", "gestion"]).any():
        raise ValueError("Hay fuentes duplicadas por formulario y gestión")
    if not set(frame["formulario"]).issubset(VARIABLE_CONTROLS):
        raise ValueError("fuentes.csv contiene formularios desconocidos")
    if not set(frame["periodo"]).issubset({"mes", "semana"}):
        raise ValueError("fuentes.csv contiene periodos desconocidos")
    return tuple(
        Source(row.formulario, int(row.gestion), row.url, row.periodo)
        for row in frame.itertuples(index=False)
    )


def load_catalog(sources: tuple[Source, ...]) -> pd.DataFrame:
    """Construye una fila por Parquet esperado a partir de la dimensión de variables."""
    frames = []
    for source in sources:
        path = VARIABLES_DIRECTORY / f"{source.gestion}.parquet"
        frame = pd.read_parquet(
            path,
            filters=[("formulario", "=", source.formulario)],
            columns=["grupo_codigo", "grupo", "variable_codigo", "variable"],
        ).astype("string")
        frame = frame.drop_duplicates(["grupo_codigo", "variable_codigo"])
        frame.insert(0, "gestion", source.gestion)
        frame.insert(0, "formulario", source.formulario)
        frames.append(frame)
    return pd.concat(frames, ignore_index=True)


@cache
def available_municipality_years() -> frozenset[int]:
    return frozenset(
        int(path.stem)
        for path in MUNICIPALITIES_DIRECTORY.glob("*.parquet")
        if path.stem.isdigit()
    )


def municipality_reference_year(year: int) -> int:
    if year in available_municipality_years():
        return year
    if year in MUNICIPALITY_FALLBACKS:
        return MUNICIPALITY_FALLBACKS[year]
    raise ValueError(f"No existe una dimensión municipal aplicable a {year}")


def normalized_text(value: object) -> str:
    """Produce una clave tolerante a mayúsculas, tildes y espacios del portal."""
    text = " ".join(str(value).replace("\xa0", " ").split()).strip()
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode().upper()


def clean_text(value: object) -> str:
    return " ".join(str(value).replace("\xa0", " ").split()).strip()


@cache
def load_municipalities(year: int) -> dict[str, tuple[Municipality, ...]]:
    """Indexa municipios por nombre; conserva varios candidatos para homónimos."""
    reference = municipality_reference_year(year)
    frame = pd.read_parquet(
        MUNICIPALITIES_DIRECTORY / f"{reference}.parquet",
        columns=["departamento", "municipio", "municipio_codigo"],
    ).drop_duplicates()

    index: dict[str, list[Municipality]] = {}
    for row in frame.itertuples(index=False):
        municipality = Municipality(
            codigo=str(row.municipio_codigo),
            departamento=clean_text(row.departamento),
        )
        index.setdefault(normalized_text(row.municipio), []).append(municipality)
    return {name: tuple(values) for name, values in index.items()}


def new_session() -> requests.Session:
    """Crea una sesión con reintentos también para los POST de consulta."""
    retry = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=None,
    )
    session = requests.Session()
    session.headers["User-Agent"] = "snis-bolivia/datos"
    session.mount("https://", HTTPAdapter(max_retries=retry))
    return session


def parse(response: requests.Response) -> BeautifulSoup:
    response.raise_for_status()
    return BeautifulSoup(response.content, "html.parser")


def selected_value(select: Tag) -> str | None:
    option = select.select_one("option[selected]") or select.select_one("option")
    return option.get("value", "") if option else None


def form_values(page: BeautifulSoup) -> dict[str, str]:
    """Reconstruye el estado WebForms sin seleccionar filtros múltiples por defecto."""
    values = {
        field["name"]: field.get("value", "")
        for field in page.select("input[type=hidden][name]")
    }
    for select in page.select("select[name]:not([multiple])"):
        value = selected_value(select)
        if value is not None:
            values[select["name"]] = value
    return values


def options(page: BeautifulSoup, selector: str) -> tuple[tuple[str, str], ...]:
    return tuple(
        (str(option.get("value", "")).strip(), clean_text(option.get_text(" ")))
        for option in page.select(selector)
        if str(option.get("value", "")).strip()
    )


def postback(
    session: requests.Session,
    source: Source,
    page: BeautifulSoup,
    control: str,
    value: str,
) -> BeautifulSoup:
    """Ejecuta una transición dependiente del VIEWSTATE vigente."""
    data = form_values(page)
    data.update(
        {
            "__EVENTTARGET": CONTROLS[control],
            "__EVENTARGUMENT": "",
            CONTROLS["gestion"]: str(source.gestion),
            CONTROLS[control]: value,
        }
    )
    return parse(session.post(source.url, data=data, timeout=TIMEOUT))


def open_group(
    session: requests.Session, source: Source, group_code: str
) -> BeautifulSoup:
    """Inicializa una sesión nueva en la gestión y grupo requeridos."""
    page = parse(session.get(source.url, timeout=TIMEOUT))
    years = {value for value, _ in options(page, SELECTORS["gestion"])}
    if str(source.gestion) not in years:
        raise ValueError(f"La página no ofrece la gestión {source.gestion}")
    page = postback(session, source, page, "gestion", str(source.gestion))
    return postback(session, source, page, "grupo", group_code)


def period_values(page: BeautifulSoup, source: Source) -> tuple[int, ...]:
    periods = tuple(int(value) for value, _ in options(page, SELECTORS[source.periodo]))
    if not periods:
        raise ValueError(f"La página no ofrece valores de {source.periodo}")
    return periods


def department_values(page: BeautifulSoup) -> dict[str, str]:
    return {
        normalized_text(label): value
        for value, label in options(page, SELECTORS["departamento"])
    }


def flatten_column(column: object) -> str:
    """Une encabezados jerárquicos sin repetir niveles ni marcadores de pandas."""
    levels = column if isinstance(column, tuple) else (column,)
    result = []
    for level in levels:
        text = clean_text(level)
        if not text or text.lower().startswith("unnamed:") or text in result:
            continue
        result.append(text)
    return " | ".join(result)


def parse_table(page: BeautifulSoup, period: int) -> pd.DataFrame:
    """Convierte la tabla cruzada del portal a observaciones largas y dispersas."""
    table = page.select_one(SELECTORS["tabla"])
    if table is None:
        raise ValueError("La respuesta no contiene la tabla esperada")

    frame = pd.read_html(StringIO(str(table)))[0]
    frame.columns = [flatten_column(column) for column in frame.columns]
    if frame.empty:
        return pd.DataFrame(columns=["periodo", "municipio", "poblacion", "valor"])
    if not frame.columns[0]:
        raise ValueError("La tabla no identifica su columna geográfica")

    frame = frame.rename(columns={frame.columns[0]: "municipio"})
    frame["municipio"] = frame["municipio"].map(clean_text)
    frame = frame[~frame["municipio"].map(normalized_text).str.startswith("TOTAL")]

    empty_tokens = {"", "-", "--", "NAN", "NONE"}
    descriptor_columns = []
    for column in frame.columns[1:]:
        values = frame[column].astype("string").str.strip()
        meaningful = values.notna() & ~values.str.upper().isin(empty_tokens)
        numeric = pd.to_numeric(values[meaningful], errors="coerce")
        if meaningful.any() and numeric.isna().any():
            descriptor_columns.append(column)

    # Algunos reportes, especialmente 301b, agregan una categoría intermedia
    # como ESPECIALIDAD. Se incorpora al nombre poblacional para conservar un
    # único esquema largo sin perder esa información.
    frame = frame.melt(
        id_vars=["municipio", *descriptor_columns],
        var_name="poblacion",
        value_name="valor",
    )
    frame["poblacion"] = frame["poblacion"].map(clean_text)
    for column in reversed(descriptor_columns):
        descriptor = frame[column].map(clean_text)
        frame["poblacion"] = column + ": " + descriptor + " | " + frame["poblacion"]
    frame = frame.drop(columns=descriptor_columns)

    raw_values = frame["valor"].astype("string").str.strip()
    numeric = pd.to_numeric(
        raw_values.mask(raw_values.str.upper().isin(empty_tokens)), errors="coerce"
    )
    invalid = (
        raw_values.notna()
        & numeric.isna()
        & ~raw_values.str.upper().isin(empty_tokens)
    )
    if invalid.any():
        examples = raw_values[invalid].drop_duplicates().head(5).tolist()
        raise ValueError(f"La tabla contiene valores no numéricos: {examples}")

    frame["valor"] = numeric
    frame = frame[frame["valor"].notna()].copy()
    if not frame["valor"].mod(1).eq(0).all():
        raise ValueError("La tabla contiene conteos no enteros")
    frame["valor"] = frame["valor"].astype("int64")
    frame.insert(0, "periodo", period)
    return frame.reset_index(drop=True)


def process_query(
    session: requests.Session,
    task: Task,
    page: BeautifulSoup,
    period: int,
    department: str | None = None,
) -> tuple[BeautifulSoup, pd.DataFrame]:
    """Solicita una variable y periodo, siempre agrupados por municipio."""
    source = task.source
    data = form_values(page)
    data.update(
        {
            "__EVENTTARGET": "",
            "__EVENTARGUMENT": "",
            CONTROLS["gestion"]: str(source.gestion),
            CONTROLS["grupo"]: task.variable.grupo_codigo,
            VARIABLE_CONTROLS[source.formulario]: task.variable.variable_codigo,
            CONTROLS["agregacion"]: "nomMunicip",
            CONTROLS[source.periodo]: str(period),
            CONTROLS["procesar"]: " Procesar",
        }
    )
    if department is not None:
        data[CONTROLS["departamento"]] = department

    result_page = parse(session.post(source.url, data=data, timeout=TIMEOUT))
    return result_page, parse_table(result_page, period)


def ambiguous_names(
    frame: pd.DataFrame, municipalities: dict[str, tuple[Municipality, ...]]
) -> set[str]:
    observed = {normalized_text(value) for value in frame["municipio"]}
    return {name for name in observed if len(municipalities.get(name, ())) > 1}


def resolve_ambiguous(
    session: requests.Session,
    task: Task,
    page: BeautifulSoup,
    period: int,
    frame: pd.DataFrame,
    municipalities: dict[str, tuple[Municipality, ...]],
    departments: dict[str, str],
) -> tuple[BeautifulSoup, pd.DataFrame]:
    """Reconsulta sólo municipios homónimos, filtrándolos por departamento."""
    ambiguous = ambiguous_names(frame, municipalities)
    if not ambiguous:
        return page, frame

    kept = frame[~frame["municipio"].map(normalized_text).isin(ambiguous)].copy()
    resolved = [kept]
    for name in sorted(ambiguous):
        for municipality in municipalities[name]:
            department = departments.get(normalized_text(municipality.departamento))
            if department is None:
                raise ValueError(
                    f"No se pudo filtrar el departamento {municipality.departamento!r}"
                )
            page, candidate = process_query(session, task, page, period, department)
            candidate = candidate[candidate["municipio"].map(normalized_text).eq(name)].copy()
            if not candidate.empty:
                candidate["municipio_codigo"] = municipality.codigo
                resolved.append(candidate)
    return page, pd.concat(resolved, ignore_index=True)


def attach_municipality_codes(
    frame: pd.DataFrame, municipalities: dict[str, tuple[Municipality, ...]]
) -> pd.DataFrame:
    """Asigna códigos a nombres únicos; los homónimos ya llegan resueltos."""
    if frame.empty:
        frame["municipio_codigo"] = pd.Series(dtype="string")
        return frame

    keys = frame["municipio"].map(normalized_text)
    unresolved = sorted({key for key in keys if key not in municipalities})
    if unresolved:
        raise ValueError(f"Municipios sin código: {unresolved[:10]}")

    needs_code = frame.get("municipio_codigo", pd.Series(pd.NA, index=frame.index)).isna()
    ambiguous = {key for key in keys[needs_code] if len(municipalities[key]) != 1}
    if ambiguous:
        raise ValueError(f"Municipios homónimos sin resolver: {sorted(ambiguous)}")
    frame.loc[needs_code, "municipio_codigo"] = keys[needs_code].map(
        lambda key: municipalities[key][0].codigo
    )
    return frame


def normalize_output(frame: pd.DataFrame, year: int) -> pd.DataFrame:
    """Fija tipos, orden y clave para que las actualizaciones sean deterministas."""
    frame.insert(0, "gestion", year)
    frame = frame[list(OUTPUT_COLUMNS)].copy()
    frame["gestion"] = frame["gestion"].astype("int16")
    frame["periodo"] = frame["periodo"].astype("int16")
    frame["municipio_codigo"] = frame["municipio_codigo"].astype("string")
    frame["poblacion"] = frame["poblacion"].astype("string")
    frame["valor"] = frame["valor"].astype("int64")

    key = ["periodo", "municipio_codigo", "poblacion"]
    if frame.duplicated(key).any():
        raise ValueError("La salida contiene observaciones duplicadas")
    return frame.sort_values(key, kind="stable").reset_index(drop=True)


def output_path(task: Task) -> Path:
    source, variable = task.source, task.variable
    return (
        DATA_DIRECTORY
        / source.formulario
        / str(source.gestion)
        / variable.grupo_codigo
        / f"{variable.variable_codigo}.parquet"
    )


def output_status(path: Path) -> tuple[bool, int | None]:
    """Comprueba el esquema y obtiene filas sin leer el contenido completo."""
    if not path.exists():
        return False, None
    try:
        parquet = pq.ParquetFile(path)
        complete = parquet.schema_arrow.names == list(OUTPUT_COLUMNS)
        return complete, parquet.metadata.num_rows if complete else None
    except (OSError, pa.ArrowException):
        return False, None


def index_key(task: Task) -> tuple[str, int, str, str]:
    source, variable = task.source, task.variable
    return (
        source.formulario,
        source.gestion,
        variable.grupo_codigo,
        variable.variable_codigo,
    )


def save_index(frame: pd.DataFrame) -> None:
    """Publica el índice de forma atómica, igual que los datos."""
    temporary = INDEX_FILE.with_name(f".{INDEX_FILE.name}.tmp")
    frame.to_csv(temporary, index=False)
    os.replace(temporary, INDEX_FILE)


def refresh_index(sources: tuple[Source, ...]) -> pd.DataFrame:
    """Reconcilia el índice con el catálogo y los Parquet presentes en disco."""
    previous_errors: dict[tuple[str, int, str, str], str] = {}
    if INDEX_FILE.exists():
        previous = pd.read_csv(INDEX_FILE, dtype="string", keep_default_na=False)
        for row in previous.itertuples(index=False):
            key = (
                row.formulario,
                int(row.gestion),
                row.grupo_codigo,
                row.variable_codigo,
            )
            previous_errors[key] = row.error

    source_by_key = {(source.formulario, source.gestion): source for source in sources}
    records = []
    for row in load_catalog(sources).itertuples(index=False):
        source = source_by_key[(row.formulario, row.gestion)]
        task = Task(source, Variable(row.grupo_codigo, row.variable_codigo))
        path = output_path(task)
        downloaded, rows = output_status(path)
        records.append(
            {
                "formulario": row.formulario,
                "gestion": row.gestion,
                "grupo_codigo": row.grupo_codigo,
                "grupo": row.grupo,
                "variable_codigo": row.variable_codigo,
                "variable": row.variable,
                "archivo": path.relative_to(DIRECTORY).as_posix(),
                "descargado": downloaded,
                "filas": rows,
                "error": "" if downloaded else previous_errors.get(index_key(task), ""),
            }
        )

    index = pd.DataFrame.from_records(records, columns=INDEX_COLUMNS)
    index["gestion"] = index["gestion"].astype("int64")
    index["descargado"] = index["descargado"].astype("bool")
    index["filas"] = pd.array(index["filas"], dtype="Int64")
    index["error"] = index["error"].astype("string")
    index = index.sort_values(
        ["gestion", "formulario", "grupo_codigo", "variable_codigo"], kind="stable"
    ).reset_index(drop=True)
    save_index(index)
    return index


def update_index(
    index: pd.DataFrame,
    task: Task,
    downloaded: bool,
    rows: int | None,
    error: str = "",
) -> None:
    """Registra inmediatamente el resultado de cada variable terminada."""
    source, variable = task.source, task.variable
    selected = (
        index["formulario"].eq(source.formulario)
        & index["gestion"].eq(source.gestion)
        & index["grupo_codigo"].eq(variable.grupo_codigo)
        & index["variable_codigo"].eq(variable.variable_codigo)
    )
    if selected.sum() != 1:
        raise ValueError(f"El índice no identifica unívocamente {task_label(task)}")
    index.loc[selected, "descargado"] = downloaded
    index.loc[selected, "filas"] = rows if rows is not None else pd.NA
    index.loc[selected, "error"] = error
    save_index(index)


def save_atomic(frame: pd.DataFrame, path: Path) -> None:
    """Evita que una interrupción deje un Parquet final parcial."""
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    frame.to_parquet(temporary, index=False, compression="zstd", use_dictionary=True)
    os.replace(temporary, path)


def extract_once(task: Task) -> pd.DataFrame:
    source = task.source
    municipalities = load_municipalities(source.gestion)
    frames = []

    with new_session() as session:
        page = open_group(session, source, task.variable.grupo_codigo)
        periods = period_values(page, source)
        departments = department_values(page)

        for period in periods:
            if STOP_EVENT.is_set():
                raise InterruptedError("Corrida interrumpida")
            page, frame = process_query(session, task, page, period)
            page, frame = resolve_ambiguous(
                session,
                task,
                page,
                period,
                frame,
                municipalities,
                departments,
            )
            frames.append(attach_municipality_codes(frame, municipalities))

    result = pd.concat(frames, ignore_index=True)
    return normalize_output(result, source.gestion)


def extract(task: Task) -> tuple[Path, int]:
    """Reinicia desde una sesión limpia si falla una variable completa."""
    error: Exception | None = None
    for _ in range(VARIABLE_ATTEMPTS):
        try:
            frame = extract_once(task)
            path = output_path(task)
            save_atomic(frame, path)
            return path, len(frame)
        except InterruptedError:
            raise
        except Exception as current_error:
            error = current_error
    source, variable = task.source, task.variable
    raise RuntimeError(
        f"Falló {source.formulario} {source.gestion} "
        f"{variable.grupo_codigo}/{variable.variable_codigo}: {error}"
    ) from error


def build_tasks(index: pd.DataFrame, sources: tuple[Source, ...]) -> list[Task]:
    """Convierte las filas seleccionadas del índice en unidades de trabajo."""
    source_by_key = {(source.formulario, source.gestion): source for source in sources}
    return [
        Task(
            source_by_key[(row.formulario, row.gestion)],
            Variable(row.grupo_codigo, row.variable_codigo),
        )
        for row in index.itertuples(index=False)
    ]


def arguments(available_years: list[int]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("years", nargs="*", type=int, choices=available_years)
    parser.add_argument("--forms", nargs="+", choices=sorted(VARIABLE_CONTROLS))
    parser.add_argument("--workers", type=int, default=MAX_WORKERS)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--replace", action="store_true")
    return parser.parse_args()


def main() -> None:
    STOP_EVENT.clear()
    sources = load_sources()
    available_years = sorted({source.gestion for source in sources})
    args = arguments(available_years)
    if args.workers < 1:
        raise ValueError("--workers debe ser mayor que cero")
    if args.limit is not None and args.limit < 0:
        raise ValueError("--limit no puede ser negativo")

    # Sin selección explícita se procesan todas las gestiones con diccionario
    # municipal disponible: actualmente 2001--2025.
    supported_years = available_municipality_years() | set(MUNICIPALITY_FALLBACKS)
    selected_years = args.years or sorted(set(available_years) & supported_years)
    unsupported = set(selected_years) - supported_years
    if unsupported:
        raise ValueError(f"Gestiones sin dimensión municipal: {sorted(unsupported)}")

    indexed_sources = tuple(
        source for source in sources if source.gestion in supported_years
    )
    print("[1/3] Reconciliando indice.csv con los Parquet locales", flush=True)
    index = refresh_index(indexed_sources)
    downloaded = int(index["descargado"].sum())
    print(f"      {downloaded:,}/{len(index):,} Parquet descargados", flush=True)

    selected_sources = tuple(
        source
        for source in indexed_sources
        if source.gestion in selected_years
        and (args.forms is None or source.formulario in args.forms)
    )
    selected_keys = {(source.formulario, source.gestion) for source in selected_sources}
    selected_index = index[
        index[["formulario", "gestion"]]
        .apply(tuple, axis=1)
        .isin(selected_keys)
    ]
    if not args.replace:
        selected_index = selected_index[~selected_index["descargado"]]
    tasks = build_tasks(selected_index, selected_sources)
    if args.limit is not None:
        tasks = tasks[: args.limit]

    print(f"[2/3] {len(tasks):,} variables seleccionadas para esta corrida", flush=True)
    failures = []
    completed = 0
    print(f"[3/3] Descargando con {args.workers} trabajadores", flush=True)
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        pending = {executor.submit(extract, task): task for task in tasks}
        try:
            for future in as_completed(pending):
                task = pending[future]
                try:
                    _, rows = future.result()
                    completed += 1
                    update_index(index, task, True, rows)
                    print(f"[{completed:,}/{len(tasks):,}]", flush=True)
                except Exception as error:
                    failures.append((task, error))
                    update_index(index, task, False, None, str(error))
                    print(f"[error] {task_label(task)}: {error}", flush=True)
                    if len(failures) >= MAX_FAILURES:
                        STOP_EVENT.set()
                        for remaining in pending:
                            remaining.cancel()
                        break
        except KeyboardInterrupt:
            # Las tareas activas terminan su solicitud vigente y se detienen
            # antes del siguiente periodo; las pendientes nunca comienzan.
            STOP_EVENT.set()
            for future in pending:
                future.cancel()
            raise

    print(
        f"Corrida terminada: {completed:,} variables completadas; "
        f"{len(failures):,} errores",
        flush=True,
    )
    if failures:
        raise RuntimeError("La corrida terminó con variables pendientes")


if __name__ == "__main__":
    main()
