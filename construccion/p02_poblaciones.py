"""Paso 2. Diccionario de poblaciones: qué significa cada etiqueta de población del tablero.

Entradas: intermedios/etiquetas.parquet e intermedios/inventario.parquet (paso 1), tablas SOAPS.
Salidas:
- intermedios/poblaciones.parquet: atributos por variable-gestión y etiqueta, y si la etiqueta
  se usa en los datos (el detalle; el total sólo si no hay detalle).
- intermedios/poblaciones_soaps_<dominio>.parquet: por variable-gestión, la parte de la suma
  cuyas etiquetas coinciden con una regla de SOAPS.

Se detiene si una variable-gestión con valores no aporta filas o si una etiqueta con valores
queda sin traducir.
"""

from __future__ import annotations

import sys

import pandas as pd

from comun import FORMULARIOS, INTERMEDIOS, SOAPS, conectar
from poblacion import DIAS, corregir, corregir_servicio, traducir, traducir_servicio

CLAVE = ["formulario", "gestion", "grupo_codigo", "variable_codigo"]
ATRIBUTOS = ["sexo", "edad_desde", "edad_hasta", "caso", "lugar", "condicion", "medida", "especialidad",
             "servicio", "especie", "tratamiento", "participante"]


def _clave(pob: pd.DataFrame) -> pd.Series:
    return pd.Series(list(zip(*(pob[c] for c in CLAVE))), index=pob.index)


def vigilancia(pob: pd.DataFrame) -> pd.DataFrame:
    # El desplazamiento de columnas depende de que la variable-gestión tenga un encabezado repetido.
    filas = [traducir(f.formulario, f.gestion, f.poblacion) for f in pob.itertuples(index=False)]
    desplazadas = {c for c, a in zip(_clave(pob), filas) if a.duplicado}
    filas = [corregir(*c, f.poblacion, a, c in desplazadas)
             for c, f, a in zip(_clave(pob), pob.itertuples(index=False), filas)]
    pob = pd.concat([pob.reset_index(drop=True), pd.DataFrame([a.dict() for a in filas])], axis=1)

    # 302 hasta 2007: si «-M» nunca tiene valores, «-H» contiene a ambos sexos (CORRECCIONES).
    temprano = (pob.formulario == "302") & (pob.gestion <= 2007) & pob.sufijo.isin(["H", "M"])
    suma_m = pob[temprano & (pob.sufijo == "M")].groupby(CLAVE).suma.sum()
    sin_sexo = set(suma_m[suma_m == 0].index) | set(_clave(pob[(pob.formulario == "302") & (pob.gestion == 2004)
                                                               & (pob.grupo_codigo == "09")]))
    marca = temprano & _clave(pob).isin(sin_sexo)
    pob.loc[marca, "sexo"] = None
    pob.loc[marca, "regla"] += "+302_sin_sexo"
    # Las columnas «-M» de esas variables están vacías y repetirían las claves de «-H».
    pob.loc[marca & (pob.sufijo == "M") & ~_clave(pob).isin(set(suma_m[suma_m > 0].index)), "sin_traducir"] = True
    return pob


def servicios(pob: pd.DataFrame) -> pd.DataFrame:
    filas = [traducir_servicio(f.formulario, f.gestion, f.variable, f.poblacion) for f in pob.itertuples(index=False)]
    con_posicion = pd.Series([a.posicion is not None for a in filas], index=pob.index)
    columnas = pob[con_posicion].groupby(CLAVE).size()
    repetidas = {c for c, a, s in zip(_clave(pob), filas, pob.suma) if a.duplicado and s > 0}
    filas = [corregir_servicio(f.formulario, int(columnas.get(c, 0)), c in repetidas, a)
             for c, f, a in zip(_clave(pob), pob.itertuples(index=False), filas)]
    return pd.concat([pob.reset_index(drop=True), pd.DataFrame([a.dict() for a in filas])], axis=1)


def marcar_agregados(pob: pd.DataFrame) -> pd.Series:
    """Una etiqueta es agregada si otra de la misma variable-gestión la desagrega.

    Ejemplo: «1 a 4 años» junto a «1 a 4 años | FEMENINO» y «1 a 4 años | MASCULINO».
    """
    agregado = pd.Series(False, index=pob.index)
    for _, grupo in pob[~pob.es_total & ~pob.sin_traducir].groupby(CLAVE):
        valores = [{d: v for d, v in zip(ATRIBUTOS, fila) if pd.notna(v)}
                   for fila in grupo[ATRIBUTOS].itertuples(index=False)]
        for i, vi in zip(grupo.index, valores):
            agregado[i] = any(len(vj) > len(vi) and vi.items() <= vj.items() for vj in valores)
    return agregado


def diccionario(con, dominio: str) -> pd.DataFrame:
    lista = ", ".join(f"'{f}'" for f in FORMULARIOS[dominio])
    pob = con.sql(f"""
        select e.*, i.variable
        from '{INTERMEDIOS}/etiquetas.parquet' e
        join '{INTERMEDIOS}/inventario.parquet' i using (formulario, gestion, grupo_codigo, variable_codigo)
        where e.formulario in ({lista})
    """).df()
    pob = vigilancia(pob) if dominio == "vigilancia" else servicios(pob)
    pob["es_agregado"] = marcar_agregados(pob)

    # Se usa el detalle; si una variable-gestión no tiene detalle con valores, su total.
    detalle = ~pob.es_total & ~pob.es_agregado & ~pob.sin_traducir
    tiene = _clave(pob).isin(set(_clave(pob[detalle & (pob.suma > 0)])))
    total = pob.es_total & ~tiene
    prioridad = pob.poblacion.str.upper().map({"TOTAL": 0, "TOTALES | TOTAL": 0}).fillna(1)
    unico = pob.groupby(CLAVE).poblacion.transform("nunique") == 1
    elegido = pob[total & ((prioridad == 0) | unico)].assign(p=prioridad).sort_values("p").drop_duplicates(CLAVE).index
    pob["usar"] = detalle | pob.index.isin(elegido)
    pob.loc[elegido, "regla"] = prioridad[elegido].map({0: "solo_total", 1: "total_unico"})
    # El total no tiene atributos: «TOTAL-M» en el 302 de 2001-2003 es el total de ambos sexos.
    pob.loc[elegido, ["sexo", "edad_desde", "edad_hasta", "edad_grupo", "caso", "lugar"]] = None
    return pob


def reglas_soaps(con) -> pd.DataFrame:
    """Atributos de cada regla SOAPS en la misma convención de edad que las etiquetas."""
    reglas = con.sql(f"select * from '{SOAPS}/poblaciones.parquet'").df()
    factor = reglas.edad_unidad.map({"años": 1, "meses": 1 / 12, "días": DIAS})
    reglas["edad_desde"] = (reglas.edad_min * factor).round(4)
    reglas["edad_hasta"] = ((reglas.edad_max + 1) * factor).round(4).where(reglas.edad_max < 130)
    reglas["sexo"] = reglas.sexo.map({"FEMENINO": "mujer", "MASCULINO": "hombre"})
    reglas["caso"] = reglas.reconsulta.map({True: "repetido", False: "nuevo"})
    reglas["lugar"] = reglas.lugar.str.lower()
    reglas["clave7"] = reglas.casilla.str[:7]
    return reglas


def acuerdo_soaps(pob: pd.DataFrame, inventario: pd.DataFrame, reglas: pd.DataFrame) -> pd.DataFrame:
    """Por variable-gestión con versión SOAPS: parte de la suma con atributos que SOAPS conoce."""
    dims_todas = ["sexo", "edad_desde", "edad_hasta", "caso", "lugar"]
    detalle = pob[pob.usar & pob.medida.isna()].merge(inventario[CLAVE + ["version", "clave7"]], on=CLAVE)
    grupos_reglas = dict(list(reglas.groupby(["version", "formulario", "clave7"])))
    resultados = []
    for (formulario, *resto, version, clave7), grupo in detalle[detalle.version.notna()].groupby(CLAVE + ["version", "clave7"]):
        r = grupos_reglas.get((version, formulario, clave7))
        if r is None:
            continue
        dims = [d for d in dims_todas if grupo[d].notna().any() and r[d].notna().any()]
        tuplas = set(r[dims].fillna(-1).itertuples(index=False, name=None))
        coincide = pd.Series([t in tuplas for t in grupo[dims].fillna(-1).itertuples(index=False, name=None)]
                             if dims else True, index=grupo.index)
        resultados.append(dict(zip(CLAVE, [formulario, *resto]), version=version, suma=grupo.suma.sum(),
                               suma_coincide=grupo.suma[coincide].sum()))
    return pd.DataFrame(resultados)


def main(dominio: str = "vigilancia") -> None:
    con = conectar()
    pob = diccionario(con, dominio)

    # Las columnas que copian otra (302a, grupo 09, 2021-2025) se excluyen a propósito.
    sin = pob[pob.sin_traducir & (pob.suma > 0) & ~pob.regla.str.endswith("fuera_de_plantilla")]
    if len(sin):
        sys.exit(f"Etiquetas con valores sin traducir:\n{sin[CLAVE + ['poblacion', 'suma']].to_string()}")
    suma = pob.groupby(CLAVE).suma.sum()
    usada = pob[pob.usar].groupby(CLAVE).suma.sum().reindex(suma.index, fill_value=0)
    perdidas = suma[(suma > 0) & (usada == 0)]
    if len(perdidas):
        sys.exit(f"Variables-gestión con valores y sin filas usadas:\n{perdidas.to_string()}")
    # Dos etiquetas con los mismos atributos se suman en los datos.
    usadas = pob[pob.usar & (pob.suma > 0)]
    repetidas = usadas[usadas.duplicated(CLAVE + ATRIBUTOS, keep=False)]
    print(f"{dominio}: {len(pob):,} etiquetas, {int(pob.usar.sum()):,} usadas; con atributos repetidos:",
          repetidas.groupby("formulario").size().to_dict())
    repetidas.to_parquet(INTERMEDIOS / f"repetidas_{dominio}.parquet", index=False)

    destino = INTERMEDIOS / "poblaciones.parquet"
    otras = pd.read_parquet(destino) if destino.exists() else pd.DataFrame(columns=["formulario"])
    otras = otras[~otras.formulario.isin(FORMULARIOS[dominio])]
    pd.concat([otras, pob], ignore_index=True).to_parquet(destino, index=False)

    inventario = con.sql(f"select * from '{INTERMEDIOS}/inventario.parquet'").df()
    acuerdo = acuerdo_soaps(pob, inventario, reglas_soaps(con))
    acuerdo.to_parquet(INTERMEDIOS / f"poblaciones_soaps_{dominio}.parquet", index=False)
    if len(acuerdo):
        completas = (acuerdo.suma_coincide >= 0.999 * acuerdo.suma).groupby(acuerdo.formulario).agg(["size", "sum"])
        print("Acuerdo con SOAPS (variables-gestión, completas):\n" + completas.to_string())


if __name__ == "__main__":
    main(*sys.argv[1:])
