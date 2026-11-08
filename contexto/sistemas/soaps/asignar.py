"""Asigna una versión de SOAPS a cada entrada de producción de servicios (301, 301a, 301b) y de vigilancia
epidemiológica (302, 302a, 302b) del índice.

Uso: python asignar.py ../../../descarga/indice.csv ../../../descarga/datos/ tablas/

Para cada entrada, las versiones candidatas son las que tienen la misma variable (formulario y clave de
7 dígitos). Cada candidata se compara con la entrada en tres criterios, en este orden:

1. Nombre: similitud entre el nombre de la variable en el índice y en la versión.
2. Poblaciones: proporción de subvariables de la versión que están entre las poblaciones de los datos.
   Se compara el rango de edad, sin el sufijo final de una letra («- M», «- F», «- D»): en las versiones
   anteriores a 7.0.1, la etiqueta del grupo agrega el sexo aunque la casilla del formulario no lo tenga.
   Los datos tienen todas las casillas del formulario, también las que una versión no calcula; por eso una
   versión con menos casillas no pierde puntos, pero una con casillas que los datos no tienen sí.
   En el 301, la etiqueta de los datos empieza con el nombre de la variable, «Pentavalente 1ra dosis Dentro»;
   ese nombre se quita antes de comparar. Si la etiqueta sólo tiene el nombre de la variable, la variable no
   tiene desagregación, y se compara como «Cantidad», el nombre que le da SOAPS.
3. Fecha: años entre la publicación del paquete y la mitad de la gestión. Si el paquete declara gestiones,
   la distancia es cero para esas gestiones y se mide a la más cercana para las demás.

Los puntajes de nombre y poblaciones se redondean a un decimal, para que una diferencia mínima de escritura
no pese más que la fecha.

La entrada recibe la mejor candidata si su nombre y sus poblaciones superan los umbrales. Si no, queda sin
versión. Escribe tablas/indice_versiones.parquet.
"""

import difflib
import re
import sys
import unicodedata
from pathlib import Path

import duckdb
import pandas as pd

from paquetes import PAQUETES

UMBRAL_NOMBRE = 0.6
UMBRAL_POBLACIONES = 0.5
PREFIJOS = {"301": "301", "301a": "301", "301b": "304", "302": "302", "302a": "302", "302b": "305"}
PALABRAS_VACIAS = {"a", "al", "con", "de", "del", "el", "en", "la", "las", "los", "o", "otras", "otros", "por", "y"}


def normalizar(texto):
    """Minúsculas, sin tildes ni signos, sin numeración inicial («3.», «a.») y con intervalos «10 a 14» = «10-14»."""
    t = unicodedata.normalize("NFKD", str(texto)).encode("ascii", "ignore").decode().lower().strip()
    t = re.sub(r"^\s*(?:[0-9]+|[a-z])\s*[.)]\s*", "", t)
    t = re.sub(r"(\d+)\s*(?:a|-)\s*(\d+)", r"\1-\2", t)
    return re.sub(r"[^a-z0-9<>-]+", " ", t).strip()


def edad(etiqueta):
    """Etiqueta de población normalizada sin el sufijo final de una letra: «1-4 anos - m» → «1-4 anos»."""
    return re.sub(r"\s*-\s*[a-z]$", "", normalizar(etiqueta))


def similitud_nombre(a, b):
    """La mayor entre la similitud de caracteres y la proporción de palabras del nombre corto que están en el largo."""
    a, b = normalizar(a), normalizar(b)
    pa, pb = set(a.split()) - PALABRAS_VACIAS, set(b.split()) - PALABRAS_VACIAS
    contenido = len(pa & pb) / min(len(pa), len(pb)) if pa and pb else 0.0
    return max(difflib.SequenceMatcher(None, a, b).ratio(), contenido)


def sin_variable(etiqueta, variable):
    """Etiqueta de población sin el nombre de la variable al inicio: «pentavalente 1ra dosis dentro» → «dentro»,
    y «cantidad» si sólo queda el nombre."""
    variable = normalizar(variable)
    if not etiqueta.startswith(variable):
        return etiqueta
    return etiqueta[len(variable):].strip() or "cantidad"


def proporcion_en_datos(version, datos):
    return len(version & datos) / len(version) if version and datos else None


def main(indice_csv, datos, tablas):
    indice = pd.read_csv(indice_csv, dtype={"grupo_codigo": str, "variable_codigo": str})
    indice = indice[indice["formulario"].isin(PREFIJOS)].reset_index(drop=True)
    indice["clave7"] = indice["formulario"].map(PREFIJOS) + indice["grupo_codigo"] + indice["variable_codigo"]

    # Poblaciones de los datos: la primera parte de «a. Menor de 6 meses - F | NUEVO5», sin totales.
    archivos = duckdb.sql(f"""
        SELECT DISTINCT filename, split_part(poblacion, ' | ', 1) AS etiqueta
        FROM read_parquet('{datos}/30[12]*/*/*/*.parquet', filename = true)""").df()
    archivos = archivos[~archivos["etiqueta"].str.upper().str.startswith("TOTAL")]
    partes = archivos["filename"].str.extract(r"(30[12][ab]?)/(\d{4})/(\d+)/(\d+)\.parquet$")
    archivos["llave"] = list(zip(partes[0], partes[1].astype(int), partes[2], partes[3]))
    poblaciones_datos = archivos.groupby("llave")["etiqueta"].agg(lambda e: {edad(x) for x in e})

    subvariables = pd.read_parquet(tablas / "subvariables.parquet")
    subvariables["clave7"] = subvariables["casilla"].str[:7]
    nombres = subvariables.groupby(["formulario", "clave7", "version"])["variable"].agg(lambda v: [x for x in set(v) if pd.notna(x)])
    etiquetas = subvariables.groupby(["formulario", "clave7", "version"])["subvariable"].agg(
        lambda s: {edad(x) for x in s if pd.notna(x)})

    fechas = {p["version"]: pd.Timestamp(p["fecha"]) for p in PAQUETES}
    fechas = {v: f.year + (f.dayofyear - 1) / 365 for v, f in fechas.items()}
    declaradas = {p["version"]: p["gestiones"] for p in PAQUETES if "gestiones" in p}

    def distancia(version, gestion):
        if version in declaradas:
            return min(abs(g - gestion) for g in declaradas[version])
        return abs(fechas[version.split()[0]] - (gestion + 0.5))

    versiones = []
    for e in indice.itertuples(index=False):
        datos_entrada = {sin_variable(d, e.variable) for d in
                         poblaciones_datos.get((e.formulario, e.gestion, e.grupo_codigo, e.variable_codigo), set())}
        candidatas = []
        for (formulario, clave7, version), nombres_version in nombres.items():
            if formulario != e.formulario or clave7 != e.clave7:
                continue
            nombre = max((similitud_nombre(e.variable, n) for n in nombres_version), default=0.0)
            poblaciones = proporcion_en_datos(etiquetas[(formulario, clave7, version)], datos_entrada)
            candidatas.append((round(nombre, 1), round(poblaciones, 1) if poblaciones is not None else 0.0,
                               -distancia(version, e.gestion), version, nombre, poblaciones))
        elegida = None
        if candidatas:
            *_, version, nombre, poblaciones = max(candidatas)
            if nombre >= UMBRAL_NOMBRE and (poblaciones is None or poblaciones >= UMBRAL_POBLACIONES):
                elegida = version
        versiones.append(elegida)

    resultado = indice[["formulario", "gestion", "grupo_codigo", "variable_codigo"]].assign(version=versiones)
    resultado.to_parquet(tablas / "indice_versiones.parquet", index=False)
    resumen = resultado.assign(con_version=resultado["version"].notna()).groupby("formulario")["con_version"].agg(["sum", "size"])
    print(resumen.to_string())


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    main(Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]))
