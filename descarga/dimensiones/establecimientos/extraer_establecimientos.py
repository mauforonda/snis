#!/usr/bin/env python3
"""Genera un Parquet por gestión a partir de las estructuras de establecimientos."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

import pandas as pd


DIRECTORY = Path(__file__).resolve().parent
RESOURCES = DIRECTORY / "recursos"

COLUMNS = [
    "gestion",
    "departamento",
    "municipio",
    "municipio_codigo",
    "red_salud",
    "establecimiento",
    "establecimiento_codigo",
    "establecimiento_tipo",
    "establecimiento_subsector",
    "establecimiento_nivel",
    "establecimiento_camas",
]

COLUMN_ALIASES = {
    "departamento": ("DEPARTAMENTO", "DPTO", "SEDES"),
    "municipio": ("MUNICIPIO", "MUN"),
    "municipio_codigo": ("COD_MUNICIPIO", "COD_MUN"),
    "red_salud": ("RED DE SALUD", "RED_SALUD", "RED_ESTABL"),
    "establecimiento": (
        "NOMBRE DE ESTABLECIMIENTO",
        "ESTABLECIMIENTO DE SALUD",
        "ESTABLECIMIENTO",
    ),
    "establecimiento_codigo": ("COD_ESTABLECIMIENTO", "COD_EST", "COD_ESTABL"),
    "establecimiento_tipo": ("TIPO",),
    "establecimiento_subsector": ("SUBSECTOR",),
    "establecimiento_nivel": ("NIVEL",),
    "establecimiento_camas": ("Nº DE CAMAS", "CAMAS"),
}

DYNAMIC_TYPE_COLUMNS = (
    "BANCO DE SANGRE",
    "C. CARACTERISTICAS PART.",
    "C.S. AMBULATORIO",
    "C.S. CON INTERNACION",
    "C.S. INTEGRAL",
    "CCESD",
    "CENTRO DE AISLAMIENTO",
    "CENTRO SALUD",
    "CLINICA",
    "CONSULTORIO VECINAL",
    "HOSPITAL CUARTO NIVEL",
    "HOSPITAL GENERAL",
    "HOSPITAL SEGUNDO NIVEL",
    "IDE",
    "IDIF",
    "INSTITUTO ESPECIALIZADO",
    "MEDICINA NUCLEAR",
    "POLICLINICO",
    "POLICONSULTORIO",
    "PUESTO DE SALUD",
    "VACUNATORIO",
)


@dataclass(frozen=True)
class Source:
    years: tuple[int, ...]
    resource: str
    sheet: str | int
    header: int
    layout: Literal["table", "dynamic"] = "table"
    year_prefix_in_code: bool = False


# Para agregar 2026, copie la fuente a recursos/ y añada aquí otro Source.
SOURCES = (
    Source(
        years=tuple(range(2005, 2018)),
        resource="estructura_establecimientos_2005_2017.xlsx",
        sheet="{year}",
        header=2,
    ),
    Source(
        years=(2018,),
        resource="estructura_establecimientos_2018.xlsx",
        sheet="estructura EESS 2018",
        header=5,
    ),
    Source(
        years=(2019,),
        resource="estructura_establecimientos_2019.xlsx",
        sheet="BASE DE DATOS",
        header=3,
    ),
    Source(
        years=(2020,),
        resource="estructura_establecimientos_2020.xlsx",
        sheet="BASE DE DATOS",
        header=3,
    ),
    Source(
        years=(2021,),
        resource="estructura_establecimientos_2021.xlsx",
        sheet="BASE DE DATOS",
        header=3,
    ),
    Source(
        years=(2022,),
        resource="estructura_establecimientos_2022.xlsx",
        sheet="BASE DE DATOS",
        header=3,
    ),
    Source(
        years=(2023,),
        resource="reporte_dinamico_establecimientos_2023.xls",
        sheet=0,
        header=3,
        layout="dynamic",
        year_prefix_in_code=True,
    ),
    Source(
        years=(2024,),
        resource="reporte_dinamico_establecimientos_2024.xls",
        sheet=0,
        header=3,
        layout="dynamic",
        year_prefix_in_code=True,
    ),
    Source(
        years=(2025,),
        resource="reporte_dinamico_establecimientos_2025.xls",
        sheet=0,
        header=3,
        layout="dynamic",
        year_prefix_in_code=True,
    ),
)

SOURCE_BY_YEAR = {year: source for source in SOURCES for year in source.years}

DYNAMIC_FILL_DOWN = (
    "departamento",
    "municipio",
    "municipio_codigo",
    "red_salud",
    "establecimiento_subsector",
    "establecimiento_nivel",
)


def normalized_name(value: object) -> str:
    return " ".join(str(value).replace("\xa0", " ").split()).strip().upper()


def source_column(frame: pd.DataFrame, field: str, required: bool = True) -> str | None:
    available = {normalized_name(column): column for column in frame.columns}
    for alias in COLUMN_ALIASES[field]:
        if normalized_name(alias) in available:
            return available[normalized_name(alias)]
    if required:
        raise ValueError(f"Falta {field!r}; columnas disponibles: {list(frame.columns)}")
    return None


def load_source(year: int) -> tuple[pd.DataFrame, Source]:
    source = SOURCE_BY_YEAR[year]
    sheet = source.sheet.format(year=year) if isinstance(source.sheet, str) else source.sheet
    frame = pd.read_excel(RESOURCES / source.resource, sheet_name=sheet, header=source.header)
    frame.columns = [" ".join(str(column).replace("\xa0", " ").split()).strip() for column in frame.columns]
    return frame, source


def direct_fields(frame: pd.DataFrame, source: Source) -> dict[str, pd.Series]:
    fields: dict[str, pd.Series] = {}
    for field in COLUMNS[1:]:
        optional = field == "establecimiento_camas" or (
            field == "establecimiento_tipo" and source.layout == "dynamic"
        )
        column = source_column(frame, field, required=not optional)
        if column is not None:
            fields[field] = frame[column]
    return fields


def dynamic_types(frame: pd.DataFrame) -> pd.Series:
    available = {normalized_name(column): column for column in frame.columns}
    columns = [available[name] for name in DYNAMIC_TYPE_COLUMNS if name in available]
    flags = frame[columns].apply(pd.to_numeric, errors="coerce").fillna(0).gt(0)
    result = pd.Series(pd.NA, index=frame.index, dtype="string")
    exactly_one = flags.sum(axis=1).eq(1)
    result.loc[exactly_one] = flags.loc[exactly_one].idxmax(axis=1).map(normalized_name)
    return result


def extract_fields(frame: pd.DataFrame, source: Source) -> pd.DataFrame:
    fields = direct_fields(frame, source)
    if source.layout == "dynamic":
        for field in DYNAMIC_FILL_DOWN:
            fields[field] = fields[field].ffill()
        fields["establecimiento_tipo"] = dynamic_types(frame)
    return pd.DataFrame(fields)


def clean_text(series: pd.Series) -> pd.Series:
    return (
        series.astype("string")
        .str.replace("\xa0", " ", regex=False)
        .str.replace(r"\s+", " ", regex=True)
        .str.strip()
        .replace("", pd.NA)
    )


def clean_code(series: pd.Series) -> pd.Series:
    return clean_text(series).str.replace(r"\.0$", "", regex=True)


def normalize(frame: pd.DataFrame, year: int, source: Source) -> pd.DataFrame:
    frame = frame[
        frame["establecimiento_codigo"].notna() & frame["establecimiento"].notna()
    ].copy()

    text_columns = [
        "departamento",
        "municipio",
        "red_salud",
        "establecimiento",
        "establecimiento_tipo",
        "establecimiento_subsector",
        "establecimiento_nivel",
    ]
    frame[text_columns] = frame[text_columns].apply(clean_text)
    frame["municipio_codigo"] = clean_code(frame["municipio_codigo"])
    frame["establecimiento_codigo"] = clean_code(frame["establecimiento_codigo"])

    if source.year_prefix_in_code:
        prefix = str(year)[-2:]
        valid = frame["establecimiento_codigo"].str.fullmatch(prefix + r"\d{6}")
        if not valid.all():
            raise ValueError(f"Hay códigos sin el prefijo {prefix} en {year}")
        frame["establecimiento_codigo"] = frame["establecimiento_codigo"].str[2:]

    if "establecimiento_camas" in frame:
        frame["establecimiento_camas"] = pd.to_numeric(
            frame["establecimiento_camas"], errors="coerce"
        ).astype("Int64")
    else:
        frame["establecimiento_camas"] = pd.Series(pd.NA, index=frame.index, dtype="Int64")

    frame.insert(0, "gestion", year)
    return frame[COLUMNS].sort_values("establecimiento_codigo").reset_index(drop=True)


def validate(frame: pd.DataFrame, year: int) -> None:
    required = [column for column in COLUMNS if column != "establecimiento_camas"]
    missing = frame[required].isna().sum()
    if missing.any():
        raise ValueError(f"Campos vacíos en {year}: {missing[missing > 0].to_dict()}")
    if frame["establecimiento_codigo"].duplicated().any():
        raise ValueError(f"Hay códigos de establecimiento duplicados en {year}")
    if not frame["municipio_codigo"].str.fullmatch(r"\d{5}").all():
        raise ValueError(f"Hay códigos municipales inválidos en {year}")
    if not frame["establecimiento_codigo"].str.fullmatch(r"\d{6}").all():
        raise ValueError(f"Hay códigos de establecimiento inválidos en {year}")


def extract(year: int) -> pd.DataFrame:
    source_frame, source = load_source(year)
    result = normalize(extract_fields(source_frame, source), year, source)
    validate(result, year)
    return result


def save(frame: pd.DataFrame, year: int) -> None:
    frame.to_parquet(
        DIRECTORY / f"{year}.parquet",
        index=False,
        compression="zstd",
        use_dictionary=True,
    )


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("years", nargs="*", type=int, choices=sorted(SOURCE_BY_YEAR))
    return parser.parse_args()


def main() -> None:
    selected = arguments().years or sorted(SOURCE_BY_YEAR)
    for year in selected:
        frame = extract(year)
        save(frame, year)
        print(f"{year}: {len(frame):,} establecimientos")


if __name__ == "__main__":
    main()
