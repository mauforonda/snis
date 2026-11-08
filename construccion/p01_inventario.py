"""Paso 1. Inventario de variables-gestión y de etiquetas de población.

Salidas en intermedios/:
- etiquetas.parquet: una fila por variable-gestión y etiqueta de población, con filas y suma.
- inventario.parquet: una fila por variable-gestión con nombre, versión SOAPS, códigos CIE-10
  y resumen de etiquetas.
"""

from __future__ import annotations

from comun import DATOS_FUENTE, INDICE, INTERMEDIOS, PREFIJO_CASILLA, SOAPS, conectar


def main() -> None:
    con = conectar()
    prefijos = " ".join(f"when '{f}' then '{p}'" for f, p in PREFIJO_CASILLA.items())

    # La ruta del archivo identifica formulario, gestión, grupo y variable.
    con.execute(f"""
        copy (
            select
                regexp_extract(filename, '/datos/([^/]+)/(\\d{{4}})/([^/]+)/([^/]+)\\.parquet$', 1) as formulario,
                cast(regexp_extract(filename, '/datos/([^/]+)/(\\d{{4}})/', 2) as integer) as gestion,
                regexp_extract(filename, '/datos/[^/]+/\\d{{4}}/([^/]+)/', 1) as grupo_codigo,
                regexp_extract(filename, '/([^/]+)\\.parquet$', 1) as variable_codigo,
                poblacion,
                count(*) as filas,
                sum(valor) as suma,
                count(*) filter (where valor = 0) as filas_cero
            from read_parquet('{DATOS_FUENTE}/*/*/*/*.parquet', filename = true)
            group by all
        ) to '{INTERMEDIOS}/etiquetas.parquet' (format parquet)
    """)

    con.execute(f"""
        copy (
            with indice as (
                select formulario, gestion::integer as gestion, grupo_codigo, grupo, variable_codigo,
                       variable, archivo, descargado, filas
                from read_csv('{INDICE}', all_varchar = true, header = true)
            ),
            versiones as (
                select formulario, gestion::integer as gestion, grupo_codigo, variable_codigo, version
                from '{SOAPS}/indice_versiones.parquet'
            ),
            -- La casilla SOAPS de 9 dígitos repite grupo y variable en los dígitos 4 a 7,
            -- salvo en el 301 de 2001-2007, cuyo código de variable ya tiene 9 dígitos.
            claves as (
                select i.*, v.version,
                       case when length(i.variable_codigo) = 9 then left(i.variable_codigo, 7)
                            else (case i.formulario {prefijos} end) || i.grupo_codigo || i.variable_codigo
                       end as clave7
                from indice i left join versiones v using (formulario, gestion, grupo_codigo, variable_codigo)
            ),
            cie as (
                select version, formulario, left(casilla, 7) as clave7,
                       list(distinct cie_alfa order by cie_alfa)
                           filter (where regexp_matches(cie_alfa, '^[A-Z][0-9]')) as cie10,
                       list(distinct cie_alfa order by cie_alfa)
                           filter (where not regexp_matches(cie_alfa, '^[A-Z][0-9]')) as cie_internos
                from '{SOAPS}/enfermedades.parquet'
                group by all
            ),
            etiquetas as (
                select formulario, gestion, grupo_codigo, variable_codigo,
                       count(*) as n_etiquetas,
                       sum(suma) as suma,
                       list(poblacion order by poblacion) as etiquetas
                from '{INTERMEDIOS}/etiquetas.parquet'
                group by all
            )
            select c.formulario, c.gestion, c.grupo_codigo, c.grupo, c.variable_codigo, c.variable,
                   c.archivo, c.descargado = 'True' as descargado, c.filas::bigint as filas,
                   c.version, c.clave7, cie.cie10, cie.cie_internos,
                   e.n_etiquetas, e.suma, e.etiquetas
            from claves c
            left join cie on cie.version = c.version and cie.formulario = c.formulario and cie.clave7 = c.clave7
            left join etiquetas e
                on e.formulario = c.formulario and e.gestion = c.gestion
               and e.grupo_codigo = c.grupo_codigo and e.variable_codigo = c.variable_codigo
            order by formulario, gestion, grupo_codigo, variable_codigo
        ) to '{INTERMEDIOS}/inventario.parquet' (format parquet)
    """)
    print(con.sql(f"""
        select formulario, count(*) entradas, count(version) con_version,
               count(*) filter (where len(cie10) > 0) con_cie10, sum(suma) suma
        from '{INTERMEDIOS}/inventario.parquet' group by 1 order by 1
    """))


if __name__ == "__main__":
    main()
