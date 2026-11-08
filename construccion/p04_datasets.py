"""Paso 4. Construye los datasets de un dominio (vigilancia o servicios).

Entradas: descarga/datos, intermedios/poblaciones.parquet (paso 2), intermedios/series.parquet
(paso 3).
Salidas:
- datos/<dominio>/<clasificacion>/<dataset>/datos.parquet, sólo con las columnas que tienen valores.
- referencias/municipios/datos.parquet.
- intermedios/implausibles_<dominio>.parquet: categorías fuera de la población posible de la
  serie. Se publican; el readme las señala.

Cada formulario se agrega por separado en una base duckdb en disco, para no exceder la memoria.
La construcción se detiene si la suma publicada no es igual a la suma de la fuente usada.
"""

from __future__ import annotations

import datetime as dt
import shutil
import sys

import pandas as pd

from comun import CLASIFICACIONES, DATOS, DATOS_FUENTE, DESCARGA, FORMULARIOS, INTERMEDIOS, REFERENCIAS, conectar

# Atributos de población de las etiquetas; los fijos de la serie completan los vacíos.
POBLACION = ["sexo", "edad_desde", "edad_hasta", "edad_grupo", "caso", "lugar", "condicion", "medida",
             "especialidad", "servicio", "especie", "tratamiento", "participante"]
SEMANALES = ("302", "302a")


def calendario() -> pd.DataFrame:
    """Semanas epidemiológicas de domingo a sábado. La semana 1 es la primera con al menos
    cuatro días del año nuevo. Las gestiones con semana 53 en los datos (2003, 2008, 2014,
    2020, 2025) coinciden con esta regla."""
    def inicio(anio: int) -> dt.date:
        d = dt.date(anio, 1, 1)
        domingo = d - dt.timedelta(days=(d.weekday() + 1) % 7)
        return domingo + dt.timedelta(days=7) if (d - domingo).days > 3 else domingo

    return pd.DataFrame([
        {"gestion": a, "semana": s + 1, "fecha_inicio": inicio(a) + dt.timedelta(days=7 * s)}
        for a in range(2001, 2027) for s in range((inicio(a + 1) - inicio(a)).days // 7)])


def municipios(con) -> None:
    con.execute(f"""
        create or replace table municipios as
        select lpad(municipio_codigo, 6, '0') as municipio_codigo,
               any_value(municipio order by gestion desc) as municipio,
               left(lpad(municipio_codigo, 6, '0'), 4) as provincia_codigo,
               left(lpad(municipio_codigo, 6, '0'), 2) as departamento_codigo,
               any_value(departamento order by gestion desc) as departamento
        from read_parquet('{DESCARGA}/dimensiones/establecimientos/*.parquet')
        group by all order by 1
    """)
    destino = REFERENCIAS / "municipios"
    destino.mkdir(parents=True, exist_ok=True)
    con.execute(f"copy municipios to '{destino}/datos.parquet' (format parquet, compression zstd)")


def agregar(con, formulario: str, atributos: list[str]) -> None:
    """Agrega los valores positivos de un formulario y los añade a la tabla salida."""
    fijos = {c: f"s.fijo_{c}" for c in ("sexo", "lugar", "caso", "condicion", "edad_desde", "edad_hasta", "edad_grupo")}
    poblacion = ", ".join(f"coalesce(p.{c}, {fijos[c]}) as {c}" if c in fijos else
                          (f"coalesce(p.{c}, s.at_{c}) as {c}" if f"at_{c}" in atributos else f"p.{c}")
                          for c in POBLACION)
    propios = ", ".join(f"s.{a}" for a in atributos if a[3:] not in POBLACION)
    con.execute(f"""
        create or replace temp table filas as
        with fuente as (
            select gestion::integer as gestion,
                   regexp_extract(filename, '/\\d{{4}}/([^/]+)/', 1) as grupo_codigo,
                   regexp_extract(filename, '/([^/]+)\\.parquet$', 1) as variable_codigo,
                   periodo, lpad(municipio_codigo, 6, '0') as municipio_codigo, poblacion, valor
            from read_parquet('{DATOS_FUENTE}/{formulario}/*/*/*.parquet', filename = true)
            where valor > 0
        )
        select f.gestion, f.periodo, f.municipio_codigo, f.valor, s.clasificacion, s.dataset, s.serie_id,
               {propios + "," if propios else ""} {poblacion},
               (s.sexo_permitido is not null and coalesce(p.sexo, s.fijo_sexo) <> s.sexo_permitido)
               or (s.edad_hasta_max is not null and p.edad_desde is not null and coalesce(p.edad_hasta, 999) > s.edad_hasta_max)
               or (s.edad_desde_min is not null and p.edad_desde < s.edad_desde_min) as implausible
        from fuente f
        join (select * from '{INTERMEDIOS}/poblaciones.parquet' where usar and formulario = '{formulario}') p
          using (gestion, grupo_codigo, variable_codigo, poblacion)
        join (select * from series where formulario = '{formulario}') s using (gestion, grupo_codigo, variable_codigo)
    """)
    usada = con.sql(f"""select coalesce(sum(suma), 0) from '{INTERMEDIOS}/poblaciones.parquet'
                        where usar and formulario = '{formulario}'""").fetchone()[0]
    leida = con.sql("select coalesce(sum(valor), 0) from filas").fetchone()[0]
    if usada != leida:
        sys.exit(f"{formulario}: la suma leída ({leida:,.0f}) no es igual a la suma usada ({usada:,.0f}).")
    con.execute("insert into implausibles by name select * exclude (implausible) from filas where implausible")
    semanal = formulario in SEMANALES
    claves = ", ".join(["f." + a for a in atributos if a[3:] not in POBLACION] + ["f." + c for c in POBLACION])
    con.execute(f"""
        insert into salida by name
        select f.clasificacion, f.dataset, f.gestion,
               {"f.periodo" if semanal else "null"}::smallint as semana,
               {"null" if semanal else "f.periodo"}::smallint as mes,
               {"c.fecha_inicio" if semanal else "make_date(f.gestion, f.periodo, 1)"} as fecha_inicio,
               m.departamento, m.municipio, f.municipio_codigo, {claves}, sum(f.valor)::bigint as valor
        from filas f
        {"left join calendario_df c on c.gestion = f.gestion and c.semana = f.periodo" if semanal else ""}
        left join municipios m using (municipio_codigo)
        group by all
    """)
    print(f"  {formulario}: {leida:,.0f}")


def main(dominio: str = "vigilancia") -> None:
    INTERMEDIOS.mkdir(parents=True, exist_ok=True)
    base = INTERMEDIOS / f"salida_{dominio}.duckdb"
    base.unlink(missing_ok=True)
    con = conectar(memoria="4GB", hilos=4)
    con.execute(f"attach '{base}' as disco")
    con.execute("use disco")
    con.register("calendario_df", calendario())
    municipios(con)
    con.execute(f"create table series as select * from '{INTERMEDIOS}/series.parquet' where dominio = '{dominio}'")
    atributos = [c for c in con.sql("select * from series limit 0").columns if c.startswith("at_")]
    # Atributos propios con valores en este dominio, más los de población.
    atributos = [a for a in atributos if con.sql(f"select count({a}) from series").fetchone()[0]]
    propios = [a for a in atributos if a[3:] not in POBLACION]
    tipos = ", ".join(f"{a} varchar" for a in propios)
    con.execute(f"""
        create table salida (clasificacion varchar, dataset varchar, gestion integer, semana smallint, mes smallint,
            fecha_inicio date, departamento varchar, municipio varchar, municipio_codigo varchar,
            {tipos + "," if tipos else ""} sexo varchar, edad_desde double, edad_hasta double, edad_grupo varchar,
            caso varchar, lugar varchar, condicion varchar, medida varchar, especialidad varchar, servicio varchar,
            especie varchar, tratamiento varchar, participante varchar, valor bigint)
    """)
    con.execute(f"""
        create table implausibles (gestion integer, periodo smallint, municipio_codigo varchar, valor bigint,
            clasificacion varchar, dataset varchar, serie_id varchar, {tipos + "," if tipos else ""}
            {", ".join(f"{c} {'double' if c.startswith('edad_') and c != 'edad_grupo' else 'varchar'}" for c in POBLACION)})
    """)
    for formulario in FORMULARIOS[dominio]:
        agregar(con, formulario, atributos)

    usada = con.sql(f"""select sum(suma) from '{INTERMEDIOS}/poblaciones.parquet'
                        where usar and formulario in ({", ".join(f"'{f}'" for f in FORMULARIOS[dominio])})""").fetchone()[0]
    publicada = con.sql("select sum(valor) from salida").fetchone()[0]
    if publicada != usada:
        sys.exit(f"La suma publicada ({publicada:,.0f}) no es igual a la suma usada ({usada:,.0f}).")
    con.execute(f"""
        copy (
            select i.clasificacion, i.dataset, i.serie_id, {", ".join(f"i.{a}" for a in propios) + "," if propios else ""}
                   i.sexo, i.edad_grupo, sum(i.valor)::bigint as valor,
                   list(distinct i.gestion order by i.gestion) as gestiones,
                   count(distinct i.municipio_codigo) as municipios
            from implausibles i group by all order by all
        ) to '{INTERMEDIOS}/implausibles_{dominio}.parquet' (format parquet)
    """)

    columnas = ["semana", "mes", "departamento", "municipio", *propios, *POBLACION]
    presentes = con.sql(f"""
        select clasificacion, dataset, {", ".join(f"count({c}) > 0 as {c}" for c in columnas)}
        from salida group by all order by all
    """).df()
    shutil.rmtree(DATOS / dominio, ignore_errors=True)
    for d in presentes.to_dict("records"):
        valor = CLASIFICACIONES[d["clasificacion"]][0]
        elegidas = ["gestion", *[c for c in ("semana", "mes") if d[c]], "fecha_inicio",
                    *[c for c in ("departamento", "municipio") if d[c]], "municipio_codigo",
                    *[c for c in columnas[4:] if d[c]]]
        select = ", ".join(f'"{c}" as "{c[3:] if c.startswith("at_") else c}"' for c in elegidas)
        destino = DATOS / dominio / d["clasificacion"] / d["dataset"]
        destino.mkdir(parents=True)
        con.execute(f"""
            copy (select {select}, valor as {valor} from salida
                  where clasificacion = '{d["clasificacion"]}' and dataset = '{d["dataset"]}'
                  order by gestion, fecha_inicio, municipio_codigo)
            to '{destino}/datos.parquet' (format parquet, compression zstd)
        """)
    filas, total = con.sql("select count(*), sum(valor) from salida").fetchone()
    print(f"{dominio}: {len(presentes)} datasets, {filas:,} filas, suma {total:,}")


if __name__ == "__main__":
    main(*sys.argv[1:])
