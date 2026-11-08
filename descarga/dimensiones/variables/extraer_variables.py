#!/usr/bin/env python3
"""Extrae los grupos y variables publicados por cada formulario del SNIS."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from pathlib import Path

import pandas as pd
import requests
from bs4 import BeautifulSoup, Tag
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


DIRECTORY = Path(__file__).resolve().parent
SOURCES_FILE = DIRECTORY.parents[1] / "fuentes.csv"

COLUMNS = (
    "gestion",
    "formulario",
    "grupo_codigo",
    "grupo",
    "variable_codigo",
    "variable",
)

CONTROLS = {
    "gestion": "ctl00$MainContent$WebPanel2$List_gestion",
    "grupo": "ctl00$MainContent$WebPanel2$List_grvar",
}

SELECTORS = {
    "gestion": "#MainContent_WebPanel2_List_gestion option",
    "grupo": "#MainContent_WebPanel2_List_grvar option",
}

VARIABLE_SELECTORS = {
    "301": "#MainContent_WebPanel2_list_subvariable option",
    "301a": "#MainContent_WebPanel2_list_subvariable option",
    "301b": "#MainContent_WebPanel2_list_subvariable option",
    "302": "#MainContent_WebPanel2_Lista_subvar option",
    "302a": "#MainContent_WebPanel2_Lista_subvar option",
    "302b": "#MainContent_WebPanel2_Lista_subvar option",
}

TIMEOUT = (10, 90)
MAX_WORKERS = 6


@dataclass(frozen=True)
class Source:
    formulario: str
    gestion: int
    url: str


def load_sources() -> tuple[Source, ...]:
    frame = pd.read_csv(
        SOURCES_FILE,
        dtype={"formulario": "string", "gestion": "int64", "url": "string"},
    )
    unknown = set(frame["formulario"]) - set(VARIABLE_SELECTORS)
    if unknown:
        raise ValueError(f"Formularios sin selector de variables: {sorted(unknown)}")
    if frame.duplicated(["formulario", "gestion"]).any():
        raise ValueError("Hay fuentes duplicadas por formulario y gestión")
    return tuple(
        Source(row.formulario, row.gestion, row.url)
        for row in frame.itertuples(index=False)
    )


def new_session() -> requests.Session:
    retry = Retry(
        total=5,
        backoff_factor=1,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=None,
    )
    session = requests.Session()
    session.headers["User-Agent"] = "snis-bolivia/variables"
    session.mount("https://", HTTPAdapter(max_retries=retry))
    return session


def parse(response: requests.Response) -> BeautifulSoup:
    response.raise_for_status()
    return BeautifulSoup(response.content, "html.parser")


def selected_value(select: Tag) -> str | None:
    option = select.select_one("option[selected]") or select.select_one("option")
    return option.get("value", "") if option else None


def form_values(page: BeautifulSoup) -> dict[str, str]:
    values = {
        field["name"]: field.get("value", "")
        for field in page.select("input[type=hidden][name]")
    }
    for select in page.select("select[name]"):
        value = selected_value(select)
        if value is not None:
            values[select["name"]] = value
    return values


def postback(
    session: requests.Session,
    source: Source,
    page: BeautifulSoup,
    control: str,
    value: str,
) -> BeautifulSoup:
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


def clean_text(value: str) -> str:
    return " ".join(value.replace("\xa0", " ").split()).strip()


def options(page: BeautifulSoup, selector: str) -> tuple[tuple[str, str], ...]:
    return tuple(
        (str(option.get("value", "")).strip(), clean_text(option.get_text(" ")))
        for option in page.select(selector)
        if str(option.get("value", "")).strip() and clean_text(option.get_text(" "))
    )


def select_year(
    session: requests.Session, source: Source, page: BeautifulSoup
) -> BeautifulSoup:
    available = {value for value, _ in options(page, SELECTORS["gestion"])}
    if str(source.gestion) not in available:
        raise ValueError(f"La página no ofrece la gestión {source.gestion}")
    return postback(session, source, page, "gestion", str(source.gestion))


def extract_source(source: Source) -> pd.DataFrame:
    with new_session() as session:
        page = parse(session.get(source.url, timeout=TIMEOUT))
        page = select_year(session, source, page)
        groups = options(page, SELECTORS["grupo"])
        if not groups:
            raise ValueError("La página no contiene grupos")

        records = []
        for group_code, group in groups:
            page = postback(session, source, page, "grupo", group_code)
            variables = options(page, VARIABLE_SELECTORS[source.formulario])
            records.extend(
                {
                    "gestion": source.gestion,
                    "formulario": source.formulario,
                    "grupo_codigo": group_code,
                    "grupo": group,
                    "variable_codigo": variable_code,
                    "variable": variable,
                }
                for variable_code, variable in variables
            )

    result = pd.DataFrame.from_records(records, columns=COLUMNS).drop_duplicates()
    validate(result, source)
    return result


def validate(frame: pd.DataFrame, source: Source) -> None:
    if frame.empty:
        raise ValueError(f"No se extrajeron variables de {source.formulario} {source.gestion}")
    if frame.isna().any().any():
        raise ValueError(f"Hay campos vacíos en {source.formulario} {source.gestion}")
    if frame.duplicated(list(COLUMNS)).any():
        raise ValueError(f"Hay filas duplicadas en {source.formulario} {source.gestion}")


def save_year(frames: list[pd.DataFrame], year: int) -> None:
    result = pd.concat(frames, ignore_index=True)
    result = result.sort_values(
        ["formulario", "grupo_codigo", "variable_codigo"], kind="stable"
    ).reset_index(drop=True)
    result.to_parquet(
        DIRECTORY / f"{year}.parquet",
        index=False,
        compression="zstd",
        use_dictionary=True,
    )
    print(f"{year}: {len(result):,} variables")


def arguments(available_years: list[int]) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("years", nargs="*", type=int, choices=available_years)
    return parser.parse_args()


def main() -> None:
    sources = load_sources()
    available_years = sorted({source.gestion for source in sources})
    selected_years = arguments(available_years).years or available_years
    selected_sources = [source for source in sources if source.gestion in selected_years]

    by_year: dict[int, list[pd.DataFrame]] = {year: [] for year in selected_years}
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        pending = {executor.submit(extract_source, source): source for source in selected_sources}
        for future in as_completed(pending):
            source = pending[future]
            frame = future.result()
            by_year[source.gestion].append(frame)
            print(f"{source.formulario} {source.gestion}: {len(frame):,}", flush=True)

    for year in selected_years:
        save_year(by_year[year], year)


if __name__ == "__main__":
    main()
