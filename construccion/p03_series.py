"""Paso 3. Asigna cada variable-gestión del tablero a una serie y a un dataset.

Entrada: intermedios/inventario.parquet (paso 1).
Salida: intermedios/series.parquet, una fila por variable-gestión con su dataset y lo que la
variable implica sobre la población:
- at_<columna>: valor de una columna propia del dataset (la clasificación del dengue, la dosis
  de una vacuna, el método anticonceptivo);
- fijo_<atributo>: sexo, edad, caso, lugar o condición que el nombre o el grupo implican y la
  etiqueta no dice;
- base: el dataset antes de dividirlo por formulario o por periodo; los datasets con la misma
  base se enlazan en la documentación;
- sexo_permitido, edad_desde_min, edad_hasta_max: población posible (sólo vigilancia).
Un dataset no une los formularios 301a y 301b, y tiene un solo conjunto de categorías (valores
de sus columnas propias) en todas sus gestiones. Falla si una variable-gestión con valores no
tiene serie.
"""

from __future__ import annotations

import sys

import pandas as pd

from comun import FORMULARIOS, INTERMEDIOS
import conceptos
import conceptos_servicios as servicios


def vigilancia(e) -> dict:
    r = conceptos.asignar(e.formulario, e.gestion, e.grupo_codigo, e.variable_codigo, e.variable)
    if r is None:
        return {}
    familia = conceptos.DATASET.get(r.id)
    lugar = r.fijo.get("lugar")
    # 302, 2001-2003: el grupo 09 es mortalidad en el establecimiento y el 15, fuera de él.
    if e.formulario == "302" and e.gestion <= 2003 and r.clasificacion == "defunciones":
        lugar = {"09": "dentro", "15": "fuera"}.get(e.grupo_codigo, lugar)
    fila = {"dominio": "vigilancia", "clasificacion": r.clasificacion, "serie_id": r.id, "serie": r.nombre,
            "tema": r.tema, "dataset": familia or r.id,
            "dataset_nombre": conceptos.FAMILIAS[familia].nombre if familia else r.nombre,
            "asignacion": "nombre" if r.patron else "codigo", "fijo_sexo": r.fijo.get("sexo"), "fijo_lugar": lugar,
            "sexo_permitido": (r.permitido.get("sexo") or (None,))[0],
            "edad_desde_min": r.permitido.get("edad_desde_min"), "edad_hasta_max": r.permitido.get("edad_hasta_max")}
    if familia:
        f = conceptos.FAMILIAS[familia]
        fila["at_" + f.columna] = f.miembros[r.id]
    return fila


def servicio(e) -> dict:
    r = servicios.asignar(e.formulario, e.gestion, e.grupo, e.variable)
    edad = servicios.edad(r["fijo"].get("edad"))
    fila = {"dominio": "servicios", "clasificacion": r["clasificacion"], "dataset": r["dataset"],
            "dataset_nombre": r["nombre"], "base": r["base"], "asignacion": "nombre",
            **{f"fijo_{k}": v for k, v in r["fijo"].items() if k != "edad"},
            **{f"at_{k}": v for k, v in r["atributos"].items()}}
    if edad:
        fila["fijo_edad_desde"], fila["fijo_edad_hasta"], fila["fijo_edad_grupo"] = edad
    return fila


def truncados(series: pd.DataFrame) -> pd.DataFrame:
    """Une las variables cuyo nombre está truncado en el índice del tablero con la serie de nombre
    completo que empieza igual, en la misma clasificación. Un nombre está truncado si termina en
    medio de una palabra del otro, o si es de 2001-2009 y tiene 44 caracteres o más: esos índices
    cortan los nombres en 45 a 49 caracteres («Partos atendidos por partera capacitada u otr»). Si
    hay varias candidatas, elige la más cercana en el tiempo."""
    auto = series[series.base.notna()]
    rangos = auto.groupby(["clasificacion", "base"]).agg(desde=("gestion", "min"), hasta=("gestion", "max"),
                                                          largo=("variable", lambda v: v.str.len().max()), dataset=("dataset", "first"))
    destino = {}
    for (clasificacion, base), r in rangos.iterrows():
        candidatas = [(b, c) for (cl, b), c in rangos.iterrows() if cl == clasificacion and b != base
                      and b.startswith(base) and (b[len(base)].isalnum() or (r.hasta <= 2009 and r.largo >= 44))]
        if candidatas:
            destino[(clasificacion, base)] = (clasificacion, min(
                candidatas, key=lambda x: max(x[1].desde - r.hasta, r.desde - x[1].hasta, 0))[0])
    for origen in destino:
        final = destino[origen]
        while final in destino:
            final = destino[final]
        filas = (series.clasificacion == origen[0]) & (series.base == origen[1])
        series.loc[filas, "dataset"] = rangos.loc[final, "dataset"]
    return series


def niveles(series: pd.DataFrame) -> pd.Series:
    """El 301a (servicios de primer nivel) y el 301b (segundo y tercer nivel) son registros
    complementarios. Si una variable tiene el mismo nombre en los dos (los sueros de enfermería),
    la del 301b forma otro dataset, con «301b» en el nombre. El 301 (2001-2014, un solo formulario)
    continúa en el 301a; si el nombre sólo está en el 301b, en el 301b."""
    con_301a = set(series[series.formulario == "301a"].groupby(["clasificacion", "dataset"]).groups)
    return (series.formulario == "301b") & pd.Series(
        [k in con_301a for k in zip(series.clasificacion, series.dataset)], index=series.index)


def periodos(series: pd.DataFrame) -> pd.DataFrame:
    """Divide un dataset en periodos de gestiones seguidas con el mismo conjunto de categorías, y en
    las gestiones en que cambia su definición (conceptos.CORTES). Así un dataset nunca supone que
    dos conjuntos de categorías o dos definiciones distintas cuentan lo mismo."""
    propias = [c for c in series.columns if c.startswith("at_")]
    categoria = series[propias].astype(str).agg("|".join, axis=1)
    for (clasificacion, dataset), g in series.groupby(["clasificacion", "dataset"]):
        conjuntos = categoria[g.index].groupby(g.gestion).agg(frozenset)
        corte = conceptos.CORTES.get(dataset, ((),))[0] if g.dominio.iloc[0] == "vigilancia" else ()
        cortes = ((conjuntos != conjuntos.shift()) | conjuntos.index.isin(corte)).cumsum()
        if cortes.iloc[-1] == 1:
            continue
        for _, gestiones in conjuntos.index.to_series().groupby(cortes.values):
            desde, hasta = gestiones.min(), gestiones.max()
            filas = g.index[g.gestion.between(desde, hasta)]
            sufijo = f"{desde}" if desde == hasta else f"{desde}_{hasta}"
            series.loc[filas, "dataset"] = f"{dataset}_{sufijo}"
            series.loc[filas, "periodo"] = f"{desde}" if desde == hasta else f"{desde}-{hasta}"
    return series


def main() -> None:
    inv = pd.read_parquet(INTERMEDIOS / "inventario.parquet")
    inv = inv[inv.suma > 0].reset_index(drop=True)
    filas = [vigilancia(e) if e.formulario in FORMULARIOS["vigilancia"] else servicio(e)
             for e in inv.itertuples(index=False)]
    series = pd.concat([inv.drop(columns=["etiquetas"]), pd.DataFrame(filas)], axis=1)
    sin = series[series.dataset.isna()]
    if len(sin):
        sys.exit(f"Variables-gestión sin serie:\n{sin[['formulario', 'gestion', 'grupo_codigo', 'variable_codigo', 'variable']].to_string()}")
    series = truncados(series)
    series["base"] = series.dataset
    b = niveles(series)
    series.loc[b, "dataset"] += "_301b"
    # Servicios: el nombre del dataset es el más largo de sus variables (el índice del tablero
    # abrevia o corta algunos: «Dias cama disp»); entre iguales, el más reciente.
    s = series.dominio == "servicios"
    orden = series[s].assign(largo=series.dataset_nombre.str.len()).sort_values(["largo", "gestion"])
    series.loc[s, "dataset_nombre"] = orden.groupby(["clasificacion", "dataset"]).dataset_nombre.transform("last")
    series.loc[b, "dataset_nombre"] += " (formulario 301b)"
    series["periodo"] = None
    series = periodos(series)
    p = series.periodo.notna()
    # Un periodo de una familia con una sola serie lleva el nombre de la serie («Dengue hemorrágico»).
    una = p & (series.dominio == "vigilancia") & (series.groupby("dataset").serie_id.transform("nunique") == 1)
    series.loc[una, "dataset_nombre"] = series.loc[una, "serie"]
    series.loc[p, "dataset_nombre"] += " (" + series.loc[p, "periodo"] + ")"
    series.loc[s, "serie_id"] = series.loc[s, "dataset"]
    series.loc[s, "serie"] = series.loc[s, "dataset_nombre"]
    series.drop(columns=["periodo"]).to_parquet(INTERMEDIOS / "series.parquet", index=False)
    print(series.groupby(["dominio", "clasificacion"]).dataset.nunique().to_string())


if __name__ == "__main__":
    main()
