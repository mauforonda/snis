"""Construye las tablas de SOAPS a partir de las tablas intermedias de extraer.py.

Las tablas describen los formularios de producción de servicios (301, 301a, 301b) y de vigilancia
epidemiológica (302, 302a, 302b).

Uso: python construir.py [intermedios/] [tablas/]
"""

import re
import sys
from pathlib import Path

import duckdb
import pandas as pd

CARPETA = Path(__file__).resolve().parent

PATRON_IN = re.compile(r"IN\s*\(([0-9,\s]+)\)")
PATRON_ENTRE = re.compile(r"BETWEEN\s+([0-9]+)\s+AND\s+([0-9]+)")
PATRON_IGUAL = re.compile(r"=\s*([0-9]+)")
PATRON_FUNCION = re.compile(r"IN\s*\(\s*DBO\.([A-Z_]+)\s*\(\s*D\.DAT_DATA\s*\)\s*\)")


def leer_intervalos(texto):
    """Intervalos (desde, hasta) de un criterio SQL con IN(…), BETWEEN … AND … o = n. Falla si queda texto sin leer."""
    intervalos = [(int(v), int(v)) for lista in PATRON_IN.findall(texto) for v in lista.replace(" ", "").split(",") if v]
    intervalos += [(int(a), int(b)) for a, b in PATRON_ENTRE.findall(texto)]
    intervalos += [(int(v), int(v)) for v in PATRON_IGUAL.findall(texto)]
    resto = PATRON_IGUAL.sub(" ", PATRON_ENTRE.sub(" ", PATRON_IN.sub(" ", texto)))
    if re.sub(r"\bOR\b|\b(?:D\.)?DAT_DATA\b|@CODIGO|[()\s]", "", resto):
        raise ValueError(f"Criterio no reconocido: {texto[:120]}")
    return intervalos


def leer_criterio(criterio, funciones):
    """Intervalos de códigos que acepta un criterio de SOAPS; expande las funciones SQL del paquete."""
    texto = criterio.upper()
    intervalos = []
    for funcion in PATRON_FUNCION.findall(texto):
        cuerpo = funciones[funcion.lower()].upper().split("IF @CODIGO", 1)[1].split("BEGIN", 1)[0]
        intervalos += leer_intervalos(cuerpo)
    return intervalos + leer_intervalos(PATRON_FUNCION.sub(" ", texto))


# Cada paquete tiene un juego de tablas de reglas sin sufijo. SOAPS 7 agrega un juego con sufijo _n, que su
# configuración asigna a las gestiones 2025 y 2026; en ese paquete, las tablas sin sufijo son la versión
# «7.0.1 anterior».
TABLAS_REGLAS = ("SE_REPORTE_GRU", "SE_REPORTE_FIL", "SE_REPORTE_FILGRU", "SE_REPORTE_FILCOL")
TABLAS_REGLAS_N = ("SE_REPORTE_GRU_n", "SE_REPORTE_FIL_n", "SE_REPORTE_FILGRU_n", "SE_REPORTE_FILCOL_N")
# Formularios de SOAPS: el 301 y el 302 hasta 2014, y los formularios desde 2015, que SOAPS llama «-2014».
# El 301b es el formulario 304 de SOAPS y el 302b es el 305.
FORMULARIOS = {"301": "301", "301-2014": "301a", "304-2014": "301b", "302": "302", "302-2014": "302a", "305-2014": "302b"}
# Formularios hasta 2014: la descripción de sus reglas sólo tiene la casilla.
FORMULARIOS_ANTIGUOS = ("301", "302")


def leer_catalogo(carpeta):
    """Catálogo de enfermedades SE_CIE10 de un paquete: identificador, código y descripción."""
    return duckdb.execute("""
        SELECT CIE_CODIGO AS id, trim(CIE_ALFA) AS alfa, trim(CIE_DESCRIPCION) AS descripcion
        FROM read_json_auto(?, sample_size=-1)""", [str(carpeta / "BDEstadistica/SE_CIE10.jsonl")]).df()


def catalogo_referencia(carpetas):
    """Identificadores de enfermedades de los paquetes cuyo catálogo se lee completo.

    En los paquetes 3.0.1 a 6.0.1, el lector no recupera CIE_CODIGO en casi todas las filas. Los paquetes que se
    leen completos (2.0.0 y 7.0.1) dan el mismo código y descripción para cada identificador común: el catálogo
    sólo agrega enfermedades. Con esta referencia, construir_paquete recupera los identificadores que faltan.
    """
    completos = [c for c in (leer_catalogo(carpeta) for carpeta in carpetas) if c["id"].notna().all()]
    referencia = pd.concat(completos).drop_duplicates()
    if referencia["id"].duplicated().any():
        sys.exit("Los catálogos de enfermedades completos no coinciden entre paquetes")
    return referencia


def construir_paquete(carpeta, referencia):
    """Las cinco tablas de un paquete de intermedios/, con sus versiones de reglas."""
    paquete = carpeta.name
    con = duckdb.connect()
    for jsonl in sorted(carpeta.glob("*/*.jsonl")):
        con.execute(f'CREATE TABLE "{jsonl.stem}" AS SELECT * FROM read_json_auto(?, sample_size=-1)', [str(jsonl)])
    con.register("referencia", referencia)
    con.execute("""
        CREATE OR REPLACE TABLE SE_CIE10 AS
        SELECT coalesce(c.CIE_CODIGO, r.id) AS CIE_CODIGO, c.CIE_ALFA, c.CIE_DESCRIPCION
        FROM SE_CIE10 c
        LEFT JOIN referencia r ON c.CIE_CODIGO IS NULL AND r.alfa = trim(c.CIE_ALFA) AND r.descripcion = trim(c.CIE_DESCRIPCION)""")
    funciones = {sql.stem.lower(): sql.read_text(errors="replace") for sql in carpeta.glob("BDEstadistica/*.sql")}
    existentes = {t.lower() for (t,) in con.execute("SELECT table_name FROM duckdb_tables()").fetchall()}
    versiones = {paquete: TABLAS_REGLAS}
    if TABLAS_REGLAS_N[0].lower() in existentes:
        versiones = {paquete: TABLAS_REGLAS_N, f"{paquete} anterior": TABLAS_REGLAS}

    reportes = {trim: codigo for trim, codigo in con.execute("SELECT trim(rep_descripcion), rep_codigo FROM SE_REPORTE").fetchall()}
    formularios = {reportes[r]: f for r, f in FORMULARIOS.items() if r in reportes}
    casos = " ".join(f"WHEN {codigo} THEN '{formulario}'" for codigo, formulario in formularios.items())
    reglas = " UNION ALL BY NAME ".join(rf"""(
        SELECT DISTINCT ON (fg.filg_codigo) '{version}' AS version, CASE g.rep_codigo {casos} END AS formulario,
               regexp_extract(fg.filg_descripcion, '^\s*([0-9]{{9}})', 1) AS casilla, fg.filg_codigo AS regla_id,
               trim(g.gru_descripcion) AS gru_descripcion, fg.filg_codigo, fg.filg_descripcion,
               fg.fil_cuaderno::VARCHAR AS fil_cuaderno, fg.fil_sexo::VARCHAR AS fil_sexo,
               fg.fil_reconsulta::VARCHAR AS fil_reconsulta, fg.fil_fnanio::VARCHAR AS fil_fnanio,
               fg.fil_fnmes::VARCHAR AS fil_fnmes, fg.fil_fndia::VARCHAR AS fil_fndia
        FROM {gru} g JOIN {fil} f ON f.gru_codigo = g.gru_codigo JOIN {filgru} fg ON fg.fil_codigo = f.fil_codigo
        WHERE g.rep_codigo IN ({", ".join(map(str, formularios))})
        ORDER BY fg.filg_codigo)""" for version, (gru, fil, filgru, _) in versiones.items())
    con.execute(f"CREATE TABLE reglas AS {reglas}")
    condiciones = " UNION ALL BY NAME ".join(
        f"SELECT '{version}' AS version, * FROM {filcol}" for version, (*_, filcol) in versiones.items())
    con.execute(f"CREATE TABLE condiciones AS {condiciones}")

    # Nombres de variables y subvariables, según el formulario y la versión:
    # - Formularios desde 2015 con tablas _n: el catálogo t_Formsubvar de 2026 del mismo paquete.
    # - Formularios desde 2015 sin tablas _n: los textos de las reglas. Algunas casillas cambiaron de significado,
    #   así que no se usa el catálogo de 2026. El nombre de la variable está en la descripción de la regla,
    #   «302011101 - (1. Sarampión / Rubéola)» o «301032602 - (3.11 Trat. de Fracturas dentoalveolares)», sin la
    #   numeración, y el de la subvariable en la del grupo, «SOSPECHA DIAGNOSTICA-Menor de 6 meses».
    # - 301 y 302: la descripción de la regla sólo tiene la casilla. Los nombres vienen del catálogo t_Formsubvar
    #   de la gestión más reciente hasta 2014 del mismo paquete. Si el paquete no tiene esa gestión, quedan vacíos.
    # Si las reglas de una casilla dan nombres distintos, la tabla guarda una fila por nombre.
    version_n = next((v for v, t in versiones.items() if t == TABLAS_REGLAS_N), None)
    subvariables = con.execute(r"""
        WITH catalogo_antiguo AS (
            SELECT codform, codsubvar, trim(desvariabl) AS variable, trim(desabrev) AS subvariable
            FROM t_Formsubvar
            WHERE list_contains($antiguos, codform) AND idgestion = (SELECT max(idgestion) FROM t_Formsubvar WHERE idgestion <= 2014)
        )
        SELECT DISTINCT r.version, r.formulario, r.casilla,
               CASE WHEN list_contains($antiguos, r.formulario) THEN c.variable
                    WHEN r.version = $version_n THEN n.variable
                    ELSE nullif(trim(regexp_extract(r.filg_descripcion, '\((?:[0-9]+(?:\.[0-9]*)+\s*)?(.*)\)\s*$', 1)), '') END AS variable,
               CASE WHEN list_contains($antiguos, r.formulario) THEN c.subvariable
                    WHEN r.version = $version_n THEN n.subvariable
                    ELSE nullif(trim(regexp_extract(r.gru_descripcion, '^[^-]*-\s*(.*)$', 1)), '') END AS subvariable
        FROM reglas r
        LEFT JOIN catalogo_antiguo c ON c.codform = r.formulario AND c.codsubvar = r.casilla
        LEFT JOIN (SELECT codsubvar, trim(desvariabl) AS variable, trim(desabrev) AS subvariable FROM t_Formsubvar
                   WHERE idgestion = 2026) n ON r.version = $version_n AND n.codsubvar = r.casilla
        ORDER BY r.version, r.formulario, r.casilla""", {"version_n": version_n, "antiguos": list(FORMULARIOS_ANTIGUOS)}).df()

    cuadernos = con.execute("""
        SELECT r.version, r.formulario, r.casilla, r.regla_id, c.CUA_CODIGO AS cuaderno_codigo, trim(c.CUA_DESCRIPCION) AS cuaderno
        FROM reglas r, SE_CUADERNO c
        WHERE list_contains(string_split(replace(r.fil_cuaderno::VARCHAR, ' ', ''), ','), c.CUA_CODIGO::VARCHAR)
        ORDER BY r.version, r.formulario, r.casilla, r.regla_id, cuaderno_codigo""").df()

    unidades = con.execute("""
        SELECT r.version, r.formulario, r.casilla, r.regla_id, trim(s.COL_DESCRIPCION) AS campo, s.COL_TIPO AS tipo,
               trim(c.condicion) AS conector, trim(c.col_criterio) AS criterio, trim(t.lis_tabla) AS lista
        FROM reglas r
        JOIN condiciones c ON c.version = r.version AND c.filg_codigo = r.regla_id
        JOIN SE_COLUMNAS s ON s.COL_CODIGO = c.col_codigo
        LEFT JOIN ad_RelacionaTablas t ON t.rel_codigo = s.rel_codigo AND s.COL_TIPO <> 3
        ORDER BY r.version, r.formulario, r.casilla, r.regla_id, c.col_codigo""").df()
    # En los paquetes anteriores a 7.0.1, ad_listagenericaE tiene los códigos pero no las etiquetas.
    etiquetas = {
        lista: dict(zip(d["codigo"], d["etiqueta"]))
        for lista, d in con.execute("""
            SELECT DISTINCT trim(lis_tabla) AS lista, lis_codigo AS codigo, trim(lis_descripcion) AS etiqueta
            FROM ad_listagenericaE WHERE trim(lis_descripcion) <> ''""").df().groupby("lista")
    }
    # Valor registrado: etiquetas de los códigos que acepta el criterio, sólo en campos con lista de valores.
    # Un código que no está en la lista no recibe etiqueta.
    unidades["valor_registrado"] = [
        [etiquetas[lista][c] for a, b in leer_criterio(criterio, funciones) for c in range(a, b + 1) if c in etiquetas[lista]]
        if isinstance(lista, str) and lista in etiquetas else None
        for lista, criterio in zip(unidades["lista"], unidades["criterio"])
    ]

    # Enfermedades: códigos que aceptan los campos de diagnóstico (tipo 3), en el catálogo SE_CIE10.
    llave = ["version", "formulario", "casilla", "regla_id"]
    intervalos = pd.DataFrame(
        [(*k, a, b) for *k, t, cr in unidades[llave + ["tipo", "criterio"]].itertuples(index=False)
         if t == 3 for a, b in leer_criterio(cr, funciones)],
        columns=llave + ["desde", "hasta"],
    )
    con.register("intervalos_enfermedad", intervalos)
    enfermedades = con.execute("""
        SELECT DISTINCT i.version, i.formulario, i.casilla, i.regla_id, e.CIE_CODIGO AS cie_codigo,
               trim(e.CIE_ALFA) AS cie_alfa, trim(e.CIE_DESCRIPCION) AS cie_descripcion
        FROM intervalos_enfermedad i JOIN SE_CIE10 e ON e.CIE_CODIGO BETWEEN i.desde AND i.hasta
        ORDER BY i.version, i.formulario, i.casilla, i.regla_id, cie_codigo""").df()

    # Edad: la regla usa una sola columna de edad; su código es un intervalo de SE_INTERVALOS o una lista de
    # intervalos, «3,4». SOAPS cuenta la atención si la edad está en uno de los intervalos (función dbo.edades).
    # Una lista de intervalos contiguos se une en uno solo; una lista con huecos detiene la construcción.
    poblaciones = con.execute("""
        WITH edades AS (
            SELECT version, regla_id, trim(unnest(string_split(coalesce(fil_fnanio, fil_fnmes, fil_fndia::VARCHAR), ','))) AS codigo
            FROM reglas),
        intervalos AS (
            SELECT e.version, e.regla_id, min(i.INT_LIMINF) AS edad_min, max(i.INT_LIMSUP) AS edad_max,
                   sum(i.INT_LIMSUP - i.INT_LIMINF + 1) AS cubiertos, count(i.INT_CODIGO) AS encontrados, count(*) AS codigos
            FROM edades e LEFT JOIN SE_INTERVALOS i ON i.INT_CODIGO::VARCHAR = e.codigo
            GROUP BY e.version, e.regla_id)
        SELECT r.version, r.formulario, r.casilla, r.regla_id, r.fil_sexo::VARCHAR AS fil_sexo,
               r.fil_reconsulta::VARCHAR AS fil_reconsulta,
               CASE WHEN r.fil_fnanio IS NOT NULL THEN 'años' WHEN r.fil_fnmes IS NOT NULL THEN 'meses'
                    WHEN r.fil_fndia::VARCHAR IS NOT NULL THEN 'días' END AS edad_unidad,
               CASE WHEN i.encontrados = i.codigos THEN i.edad_min END AS edad_min,
               CASE WHEN i.encontrados = i.codigos THEN i.edad_max END AS edad_max,
               i.cubiertos = i.edad_max - i.edad_min + 1 AS edad_contigua
        FROM reglas r
        LEFT JOIN intervalos i ON i.version = r.version AND i.regla_id = r.regla_id
        ORDER BY r.version, r.formulario, r.casilla, r.regla_id""").df()
    if (poblaciones["edad_contigua"] == False).any():
        sys.exit(f"{paquete}: hay reglas con intervalos de edad no contiguos")
    sexos_bdsnis = dict(con.execute("SELECT id, trim(sexo) FROM t_sexo").fetchall()) if "t_sexo" in existentes else None
    codigos_sexo = {c for (c,) in con.execute("SELECT lis_codigo FROM ad_listagenericaE WHERE trim(lis_tabla) = 'se_sexo'").fetchall()}
    con.close()

    # Sexo: código del filtro de la regla en la lista se_sexo. Si la regla no filtra el sexo,
    # el valor registrado de la lista se_sexo_mueobit, por ejemplo «MASCULINO (DENTRO)».
    # Si la lista no tiene etiquetas pero tiene los mismos códigos, se usan las etiquetas de SOAPS 7.0.1. Las demás
    # listas cambian de códigos entre versiones, así que sus valores quedan sin etiqueta.
    se_sexo = etiquetas.get("se_sexo")
    if se_sexo is None and codigos_sexo == {1, 2}:
        se_sexo = {1: "MASCULINO", 2: "FEMENINO"}
    if se_sexo != {1: "MASCULINO", 2: "FEMENINO"} or sexos_bdsnis not in (None, {1: "V", 2: "M"}):
        sys.exit(f"{paquete}: los códigos de sexo cambiaron: t_sexo {sexos_bdsnis}, se_sexo {se_sexo}")
    valores = (unidades.dropna(subset=["valor_registrado"]).groupby(["version", "regla_id"])["valor_registrado"]
               .agg(lambda v: [x for l in v for x in l]))
    sexo_obito = valores.map(lambda v: sorted({m.group(1) for x in v if (m := re.fullmatch(r"(MASCULINO|FEMENINO) \((?:DENTRO|FUERA)\)", x))}))
    # Lugar: valor registrado DENTRO o FUERA, también dentro de un paréntesis, por ejemplo «FEMENINO (FUERA)».
    # En los campos de marca o de número, el lugar está al final del nombre del campo, por ejemplo
    # «PENTAVALENTE 1RA DOSIS - DENTRO».
    lugares = valores.map(lambda v: {m.group(1) for x in v if (m := re.fullmatch(r"(?:.*\()?(DENTRO|FUERA)\)?", x))})
    lugares_campo = (unidades[unidades["tipo"].isin([0, 1])].assign(lugar=lambda u: u["campo"].str.extract(r"[\s-](DENTRO|FUERA)$")[0])
                     .dropna(subset=["lugar"]).groupby(["version", "regla_id"])["lugar"].agg(set))
    lugares = lugares.combine(lugares_campo, lambda a, b: a | b, fill_value=set()).map(sorted)
    llaves = list(zip(poblaciones["version"], poblaciones["regla_id"]))
    poblaciones = poblaciones.assign(
        sexo=[se_sexo[int(s)] if pd.notna(s) else (o[0] if len(o := sexo_obito.get(k, [])) == 1 else None)
              for k, s in zip(llaves, poblaciones["fil_sexo"])],
        # Reconsulta: 0 = caso nuevo, 1 = caso repetido (comentarios del procedimiento sp_reporte_snis2007).
        reconsulta=poblaciones["fil_reconsulta"].map({"0": False, "1": True}).astype("boolean"),
        lugar=[l[0] if len(l := lugares.get(k, [])) == 1 else None for k in llaves],
    )[llave + ["sexo", "edad_unidad", "edad_min", "edad_max", "reconsulta", "lugar"]]

    if poblaciones.duplicated(["version", "regla_id"]).any():
        sys.exit(f"{paquete}: hay reglas repetidas")
    if not poblaciones["edad_unidad"].isna().eq(poblaciones["edad_min"].isna()).all():
        sys.exit(f"{paquete}: hay códigos de edad sin intervalo en SE_INTERVALOS")
    return {
        "subvariables": subvariables,
        "poblaciones": poblaciones,
        "cuadernos": cuadernos,
        "unidades_registro": unidades[llave + ["campo", "tipo", "conector", "valor_registrado"]],
        "enfermedades": enfermedades,
    }


def main(intermedios, salida):
    carpetas = sorted(c for c in intermedios.iterdir() if c.is_dir())
    referencia = catalogo_referencia(carpetas)
    por_paquete = [construir_paquete(carpeta, referencia) for carpeta in carpetas]
    salida.mkdir(parents=True, exist_ok=True)
    for nombre in por_paquete[0]:
        tabla = pd.concat([p[nombre] for p in por_paquete], ignore_index=True)
        tabla.to_parquet(salida / f"{nombre}.parquet", index=False)
        print(f"{nombre}: {len(tabla)} filas")


if __name__ == "__main__":
    if len(sys.argv) > 3:
        sys.exit(__doc__)
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else CARPETA / "intermedios",
         Path(sys.argv[2]) if len(sys.argv) > 2 else CARPETA / "tablas")
