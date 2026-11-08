"""Paso 5. Documenta los datasets: datapackage.json y readme.md de cada uno, el catálogo
datos/README.md y la documentación de referencias/municipios.

Cada hecho se calcula una vez, desde los datos publicados y los pasos anteriores, y se escribe en
el datapackage, el readme y el catálogo. Nada se escribe a mano: ejecutar este paso otra vez
después de reconstruir los datos actualiza toda la documentación.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from collections import defaultdict

import pandas as pd

from comun import CLASIFICACIONES, DATOS, DESCARGA, INTERMEDIOS, REFERENCIAS, SOAPS, conectar
import conceptos
import conceptos_servicios
from poblacion import CORRECCIONES

# --- Diccionario de columnas: tipo, descripción y nombre corto para el catálogo -------------------
COLUMNAS = {
    "gestion": ("integer", "Año calendario (gestión) del registro.", None),
    "semana": ("integer", "Semana epidemiológica, de 1 a 53. Va de domingo a sábado.", None),
    "mes": ("integer", "Mes, de 1 a 12.", None),
    "fecha_inicio": ("date", "Primer día de la semana o del mes.", None),
    "departamento": ("string", "Nombre del departamento.", None),
    "municipio": ("string", "Nombre del municipio.", None),
    "municipio_codigo": ("string", "Código del municipio, 6 dígitos: departamento (2), provincia (2) y municipio (2).", None),
    "sexo": ("string", "mujer u hombre.", "sexo"),
    "edad_desde": ("number", "Edad mínima de la banda, en años (6 meses = 0,5).", "edad"),
    "edad_hasta": ("number", "Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite.", "edad"),
    "edad_grupo": ("string", "Banda de edad en texto corto: «<6m» (menos de 6 meses), «1-4», «60+».", "edad"),
    "caso": ("string", "nuevo, repetido, seguimiento o primera, como lo registra el formulario.", "nuevo o repetido"),
    "lugar": ("string", "Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio.", "lugar"),
    "condicion": ("string", "embarazada o puerpera.", "embarazo o puerperio"),
    "medida": ("string", "Qué se cuenta: eventos, personas afectadas, fallecidas, damnificadas o pacientes atendidos.", "medida"),
    "especialidad": ("string", "Especialidad del hospital que atiende.", "especialidad"),
    "servicio": ("string", "Servicio que atiende o pide el estudio.", "servicio"),
    "especie": ("string", "Especie de Plasmodium.", "especie"),
    "tratamiento": ("string", "Estado del tratamiento: iniciado o concluido.", "tratamiento iniciado o concluido"),
    "participante": ("string", "Perfil de quien participa.", "participante"),
}
# Columnas propias de algunos datasets: distinguen las variables del tablero que el dataset une.
PROPIAS = {
    "dosis": "Dosis: número (1 a 5), inicial, única, anual o refuerzo.", "grupo": "Grupo de población al que se dirige la vacuna.",
    "metodo": "Método anticonceptivo.", "usuaria": "Usuaria nueva o continua.", "momento": "Momento de la consulta prenatal.",
    "via": "Vía del parto.", "diagnostico": "Diagnóstico de egreso.", "esquema": "Esquema de tratamiento.",
    "tipo": "Tipo.", "forma_clinica": "Forma clínica.", "clasificacion": "Clasificación.", "causal": "Causal legal.",
    "trimestre": "Trimestre del embarazo.", "movimiento": "Ingreso o egreso y su tipo.", "capitulo": "Capítulo de la CIE-10.",
    "enfermedad": "Enfermedad.", "forma": "Forma de la tuberculosis.", "desenlace": "Desenlace.", "agente": "Agente de la intoxicación.",
    "transmision": "Mecanismo de transmisión.", "resultado": "Resultado.", "gravedad": "Gravedad.", "evento": "Tipo de evento.",
    "ambito": "Ámbito de la violencia.", "estadio": "Estadio.", "sustancia": "Sustancia.",
    "dispositivo": "Tipo de teledispositivo.",
}
NOMBRE_PROPIA = {"metodo": "método", "via": "vía del parto", "diagnostico": "diagnóstico", "forma_clinica": "forma clínica",
                 "clasificacion": "clasificación", "capitulo": "capítulo", "transmision": "transmisión", "ambito": "ámbito",
                 "trimestre": "trimestre", "usuaria": "usuaria nueva o continua", "grupo": "grupo de población"}
TITULOS = {
    "casos": "Casos", "defunciones": "Defunciones", "estado_nutricional": "Estado nutricional",
    "factores_riesgo": "Factores de riesgo", "desarrollo_infantil": "Desarrollo infantil", "emergencias": "Emergencias y desastres",
    "consultas": "Consultas", "odontologia": "Odontología", "salud_materna_neonatal": "Salud materna y neonatal",
    "anticoncepcion_prevencion_cancer": "Anticoncepción y prevención del cáncer", "nutricion": "Nutrición",
    "vacunas": "Vacunas", "internacion": "Internación", "cirugia": "Cirugía", "diagnostico_tratamiento": "Diagnóstico y tratamiento",
    "control_enfermedades": "Control de enfermedades", "enfermedades_cronicas": "Enfermedades crónicas",
    "referencias": "Referencias de pacientes", "gestion_comunidad": "Gestión y comunidad",
}
DOMINIOS = {"vigilancia": ("Vigilancia epidemiológica", "formularios 302, 302a y 302b"),
            "servicios": ("Producción de servicios", "formularios 301, 301a y 301b")}
SEMANALES = ("302", "302a")


def comillas(texto: str) -> str:
    """La documentación usa comillas rectas: «Sueros» -> "Sueros"."""
    return texto.replace("«", '"').replace("»", '"')


def miles(n) -> str:
    return f"{int(n):,}".replace(",", ".")


def rangos(gestiones) -> str:
    """[2001, 2002, 2003, 2005] -> «2001-2003, 2005»."""
    g = sorted(set(int(x) for x in gestiones))
    partes, ini = [], g[0]
    for a, b in zip(g, g[1:] + [None]):
        if b != a + 1:
            partes.append(f"{ini}" if ini == a else f"{ini}-{a}")
            ini = b
    return ", ".join(partes)


def bloques(por_gestion: dict) -> list[tuple[str, object]]:
    """Agrupa gestiones consecutivas con el mismo valor: {2001: x, 2002: x, 2003: y} -> [("2001-2002", x), ...]."""
    salida, actual, gs = [], None, []
    for g in sorted(por_gestion):
        if gs and (por_gestion[g] != actual or g != gs[-1] + 1):
            salida.append((rangos(gs), actual))
            gs = []
        actual = por_gestion[g]
        gs.append(g)
    if gs:
        salida.append((rangos(gs), actual))
    return salida


def fechas_soaps() -> dict:
    spec = importlib.util.spec_from_file_location("paquetes", SOAPS.parent / "paquetes.py")
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return {p["version"]: p["fecha"] for p in modulo.PAQUETES}


def notas_vigilancia() -> dict:
    """Notas de cada serie de vigilancia, desde las reglas."""
    notas = defaultdict(list)
    for r in [*conceptos.REGLAS, *conceptos.POR_CODIGO.values()]:
        if r.nota and r.nota not in notas[r.id]:
            notas[r.id].append(r.nota)
    return notas


def relaciones(series: pd.DataFrame, datasets: pd.DataFrame) -> list[tuple]:
    """Grupos de datasets relacionados (claves, supuesto, unir, propias): los que vienen de un mismo
    dataset dividido por formulario o por periodo (paso 3), con las columnas propias del grupo, y
    los declarados en conceptos.RELACIONES y conceptos_servicios.RELACIONES (propias = None)."""
    por_base = defaultdict(list)
    for k, d in datasets.iterrows():
        por_base[(k[0], d.base)].append(k)
    orden = lambda claves: sorted(claves, key=lambda c: (datasets.loc[c].desde, c))
    grupos = []
    for (dominio, base), claves in por_base.items():
        if len(claves) < 2:
            continue
        s = series[(series.dominio == dominio) & (series.base == base)]
        partes, niveles = [], {c[2].endswith("_301b") for c in claves}
        if len(niveles) > 1:
            partes.append("El formulario 301a registra los servicios de primer nivel y el 301b, los de segundo y tercer "
                          "nivel: son registros complementarios, no partes de un total. Sumarlos supone que ninguna "
                          "atención se registra en los dos.")
        corte = conceptos.CORTES.get(base) if dominio == "vigilancia" else None
        if corte:
            partes.append(corte[1] + " Consultarlos juntos como una serie supone que las definiciones cuentan lo mismo.")
        propias = [c for c in s.columns if c.startswith("at_") and s[c].notna().any()]
        if len(claves) > len(niveles) and propias:
            columnas = " y ".join(f"`{c[3:]}`" for c in propias)
            partes.append(f"Las categorías de {columnas} cambian entre estos periodos; el readme de cada uno las lista. "
                          "Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo "
                          "cuentan, en total, lo mismo.")
        grupos.append((orden(claves), " ".join(partes), True, [c[3:] for c in propias]))
    for dominio, lista in (("vigilancia", conceptos.RELACIONES), ("servicios", conceptos_servicios.RELACIONES)):
        for r in lista:
            faltan = [b for b in r.bases if not por_base[(dominio, b)]]
            if faltan:
                sys.exit(f"Relación con datasets que no existen: {faltan}")
            claves = orden([k for b in r.bases for k in por_base[(dominio, b)]])
            mismo = next((g for g in grupos if g[0] == claves), None)
            if mismo:                                      # precisa el texto de un dataset dividido
                grupos[grupos.index(mismo)] = (claves, f"{mismo[1]} {r.supuesto}", mismo[2], mismo[3])
            else:
                grupos.append((claves, r.supuesto, r.unir, None))
    return grupos


class Documentador:
    def __init__(self):
        self.con = conectar(memoria="2GB", hilos=2)
        self.series = pd.read_parquet(INTERMEDIOS / "series.parquet")
        pob = pd.read_parquet(INTERMEDIOS / "poblaciones.parquet", columns=[
            "formulario", "gestion", "grupo_codigo", "variable_codigo", "regla", "usar", "suma"])
        pob = pob[pob.usar & (pob.suma > 0)]
        pob = pob.assign(regla=pob.regla.str.split("+")).explode("regla")
        self.reglas = pob.groupby(["formulario", "gestion", "grupo_codigo", "variable_codigo"]).regla.agg(set)
        self.implausibles = pd.concat([pd.read_parquet(p) for p in INTERMEDIOS.glob("implausibles_*.parquet")])
        self.fuentes = pd.read_csv(DESCARGA / "fuentes.csv", dtype=str).set_index(["formulario", "gestion"]).url
        self.soaps = fechas_soaps()
        self.notas = notas_vigilancia()
        clave = ["dominio", "clasificacion", "dataset"]
        self.datasets = self.series.sort_values("gestion").groupby(clave).agg(
            base=("base", "last"), nombre=("dataset_nombre", "last"), desde=("gestion", "min"), hasta=("gestion", "max"),
            formularios=("formulario", lambda f: ", ".join(sorted(set(f)))))
        self.relaciones = relaciones(self.series, self.datasets)
        self.catalogo = []

    # --- Hechos de un dataset ---
    def hechos(self, dominio: str, clasificacion: str, dataset: str) -> dict:
        ruta = DATOS / dominio / clasificacion / dataset
        archivo = f"'{ruta}/datos.parquet'"
        valor = CLASIFICACIONES[clasificacion][0]
        esquema = self.con.sql(f"describe select * from {archivo}").fetchall()
        columnas = [c[0] for c in esquema]
        tipos = {c[0]: c[1] for c in esquema}
        totales = self.con.sql(f"select gestion, sum({valor}) from {archivo} group by 1 order by 1").fetchall()
        filas, municipios = self.con.sql(f"select count(*), count(distinct municipio_codigo) from {archivo}").fetchone()
        propias = [c for c in columnas if c in PROPIAS]
        categorias = {}
        for c in propias + [c for c in ("especialidad", "servicio", "especie", "tratamiento", "participante",
                                        "condicion", "lugar", "caso", "medida") if c in columnas]:
            valores = self.con.sql(f"""select {c}, list(distinct gestion order by gestion) from {archivo}
                                       where {c} is not null group by 1 order by min(gestion), 1""").fetchall()
            categorias[c] = [(v, rangos(g)) for v, g in valores]
        edades = {}
        if "edad_grupo" in columnas:
            for g, bandas in self.con.sql(f"""select gestion, list(edad_grupo order by edad_desde, edad_grupo)
                                              from (select distinct gestion, edad_grupo, min(edad_desde) as edad_desde
                                                    from {archivo} where edad_grupo is not null group by all)
                                              group by 1""").fetchall():
                edades[g] = ", ".join(bandas)
        s = self.series[(self.series.dominio == dominio) & (self.series.clasificacion == clasificacion)
                        & (self.series.dataset == dataset)].sort_values(["gestion", "formulario"])
        return dict(dominio=dominio, clasificacion=clasificacion, dataset=dataset, valor=valor, columnas=columnas,
                    tipos=tipos, totales=totales, filas=filas, municipios=municipios, propias=propias,
                    categorias=categorias, edades=edades, series=s, nombre=s.dataset_nombre.iloc[-1],
                    gestiones=[g for g, _ in totales], tema=s.tema.dropna().iloc[-1] if s.tema.notna().any() else None,
                    periodicidad=self.periodicidad(s))

    @staticmethod
    def periodicidad(s: pd.DataFrame) -> str:
        semanal, mensual = s.formulario.isin(SEMANALES).any(), (~s.formulario.isin(SEMANALES)).any()
        if semanal and mensual:
            return "semanal y mensual"
        return "semanal" if semanal else "mensual"

    def desagregacion(self, h: dict) -> str:
        etiquetas = []
        for c in h["columnas"]:
            e = COLUMNAS.get(c, (None, None, None))[2] if c in COLUMNAS else (
                NOMBRE_PROPIA.get(c, c.replace("_", " ")) if c in PROPIAS else None)
            if e and e not in etiquetas:
                etiquetas.append(e)
        return ", ".join(etiquetas)

    def procedencia(self, h: dict) -> list[tuple[str, str, str, str, str]]:
        """Bloques de gestiones con la misma fuente: formulario, variables, versión SOAPS y CIE-10."""
        por_gestion = {}
        for g, x in h["series"].groupby("gestion"):
            formularios = ", ".join(sorted(x.formulario.unique()))
            variables = "; ".join(sorted({f"{v.strip()}" for v in x.variable}))
            versiones = sorted({v for v in x.version.dropna()})
            version = ", ".join(f"{v} ({self.soaps.get(v.split()[0], '')[:4]})" for v in versiones)
            completos = sorted({c for lista in x.cie10.dropna() for c in lista})
            categorias = " ".join(sorted({c[:3] for c in completos}))
            por_gestion[g] = (formularios, variables, version, categorias, " ".join(completos))
        return [(rango, *valores) for rango, valores in bloques(por_gestion)]

    def correcciones(self, h: dict) -> list[str]:
        claves = list(zip(h["series"].formulario, h["series"].gestion, h["series"].grupo_codigo, h["series"].variable_codigo))
        usadas = set().union(*(self.reglas.get(k, set()) for k in claves))
        nombres = {r.split(":")[0] for r in usadas}
        return [CORRECCIONES[n] for n in CORRECCIONES if n in nombres]

    def advertencias(self, h: dict) -> list[str]:
        """Notas sobre lo que cuenta el dataset, desde las reglas, y registros implausibles."""
        salida, bases = [], h["series"].base.unique()
        if h["dominio"] == "vigilancia":
            for base in bases:
                f = conceptos.FAMILIAS.get(base)
                if f and f.nota and (not f.nota_gestiones or (f.nota_gestiones[0] <= h["gestiones"][-1]
                                                            and h["gestiones"][0] <= f.nota_gestiones[1])):
                    salida.append(f.nota)
            for serie in h["series"].serie_id.unique():
                salida += [n for n in self.notas.get(serie, []) if n not in salida]
        else:
            salida += [conceptos_servicios.NOTAS[b] for b in bases if b in conceptos_servicios.NOTAS]
        imp = self.implausibles[(self.implausibles.dataset == h["dataset"]) & (self.implausibles.clasificacion == h["clasificacion"])]
        if len(imp):
            salida.append("Registros implausibles: hay filas con una población que la definición excluye. Se publican "
                          "tal como se registraron; pueden ser errores de registro o de codificación. Están en la tabla "
                          "«Registros implausibles».")
        return salida

    def enlace(self, k: tuple, desde: str = "../../../") -> str:
        d = self.datasets.loc[k]
        return f"[{d.nombre}]({desde}{k[0]}/{k[1]}/{k[2]}/readme.md)"

    def relacionados(self, h: dict) -> list[tuple]:
        k = (h["dominio"], h["clasificacion"], h["dataset"])
        return [g for g in self.relaciones if k in g[0]]

    def comentario(self, h: dict, advertencias: list[str]) -> tuple[str, str]:
        """Columnas "Comentario" (categorías, definición y advertencias) y "Relacionados" del catálogo."""
        partes, enlaces = [], []
        for c in h["propias"]:
            valores = [f'"{v}"' for v, _ in h["categorias"][c]]
            nombre = NOMBRE_PROPIA.get(c, c.replace("_", " "))
            if len(valores) == 1:
                partes.append(f"Este dataset cuenta una sola categoría de {nombre}: {valores[0]}.")
            elif len(valores) <= 8:
                partes.append(f"Este dataset cuenta por separado {len(valores)} categorías de {nombre}: "
                              f"{', '.join(valores[:-1])} y {valores[-1]}.")
            else:
                partes.append(f"Este dataset cuenta por separado {len(valores)} categorías de {nombre}; el readme las lista.")
        propio = (h["dominio"], h["clasificacion"], h["dataset"])
        grupos = self.relacionados(h)
        anios = lambda d: f"{d.desde}" if d.desde == d.hasta else f"{d.desde}-{d.hasta}"
        vistos = {propio}
        for claves, _, _, propias in [g for g in grupos if g[3] is not None]:      # mismo dataset, dividido
            faltan = [NOMBRE_PROPIA.get(c, c.replace("_", " ")) for c in propias if c not in h["propias"]]
            if faltan:
                partes.insert(0, f"Este dataset no separa por {' ni '.join(faltan)}.")
            corte = conceptos.CORTES.get(self.datasets.loc[propio].base) if h["dominio"] == "vigilancia" else None
            if corte:
                partes.append(corte[1])
            otros = [c for c in claves if c not in vistos]
            vistos |= set(otros)
            for c in otros:
                if c[2].endswith("_301b") != propio[2].endswith("_301b"):
                    enlaces.append(f"Formulario {'301b' if c[2].endswith('_301b') else '301a'}: {self.enlace(c, '')}")
            periodos = [c for c in otros if c[2].endswith("_301b") == propio[2].endswith("_301b")]
            if periodos:
                enlaces.append("Otros periodos: " + ", ".join(
                    f"[{anios(self.datasets.loc[c])}]({c[0]}/{c[1]}/{c[2]}/readme.md)" for c in periodos))
        for claves, _, unir, _ in [g for g in grupos if g[3] is None]:            # declarados
            otros = [c for c in claves if c not in vistos]
            vistos |= set(otros)
            if otros:
                enlaces.append(("" if unir else "No sumar: ") + ", ".join(self.enlace(c, "") for c in otros))
        partes += [a for a in advertencias if not a.startswith("Registros implausibles")]
        if any(a.startswith("Registros implausibles") for a in advertencias):
            partes.append("El dataset tiene registros implausibles.")
        return comillas(" ".join(partes)).replace("|", "/"), "".join(f"{e}. " for e in enlaces).strip().replace("|", "/")

    def seccion_relacionados(self, h: dict) -> list[str]:
        grupos = self.relacionados(h)
        if not grupos:
            return []
        v, propio = h["valor"], (h["dominio"], h["clasificacion"], h["dataset"])
        lineas = ["## Datasets relacionados", "", "Estos datasets cuentan algo parecido con otras categorías, otra "
                  "definición, otro nombre u otro formulario. El repositorio no los une.", ""]
        for claves, supuesto, unir, _ in grupos:
            for c in claves:
                d = self.datasets.loc[c]
                gestiones = f"{d.desde}" if d.desde == d.hasta else f"{d.desde}-{d.hasta}"
                nombre = f"{d.nombre} (este dataset)" if c == propio else self.enlace(c)
                lineas.append(f"- {nombre}: {gestiones}, formulario {d.formularios}.")
            lineas += ["", supuesto, ""]
            if unir:
                rutas = ",\n".join(f"    'datos/{c[0]}/{c[1]}/{c[2]}/datos.parquet'" for c in claves)
                lineas += ["Para consultarlos juntos, con ese supuesto:", "", "```sql",
                           f"select gestion, sum({v}) as {v}", f"from read_parquet([\n{rutas}\n], union_by_name = true)",
                           "group by gestion order by gestion;", "```", ""]
        return lineas

    def tabla_implausibles(self, h: dict) -> list[str]:
        imp = self.implausibles[(self.implausibles.dataset == h["dataset"]) & (self.implausibles.clasificacion == h["clasificacion"])]
        if imp.empty:
            return []
        total, v = sum(t for _, t in h["totales"]), h["valor"]
        lineas = ["### Registros implausibles", "", f"| Sexo | Edad | {v.capitalize()} | % del total | Gestiones | Municipios |",
                  "| --- | --- | ---: | ---: | --- | ---: |"]
        condiciones = []
        for r in imp.itertuples():
            lineas.append(f"| {r.sexo or ''} | {r.edad_grupo or ''} | {miles(r.valor)} | "
                          f"{f'{r.valor / total:.2%}'.replace('.', ',')} | {rangos(r.gestiones)} | {r.municipios} |")
            partes = [f"sexo = '{r.sexo}'" if r.sexo else "sexo is null",
                      f"edad_grupo = '{r.edad_grupo}'" if r.edad_grupo else "edad_grupo is null"]
            condiciones.append(f"({' and '.join(partes)})")
        ruta = f"datos/{h['dominio']}/{h['clasificacion']}/{h['dataset']}/datos.parquet"
        lineas += ["", "Para excluirlos:", "", "```sql", f"select gestion, sum({v}) as {v}", f"from '{ruta}'",
                   "where not coalesce(" + "\n    or ".join(condiciones) + ", false)", "group by gestion order by gestion;", "```", ""]
        return lineas

    # --- Escritura ---
    def resumen(self, h: dict) -> str:
        cuenta = CLASIFICACIONES[h["clasificacion"]][2]
        periodo = {"semanal": "semana", "mensual": "mes", "semanal y mensual": "semana o mes"}[h["periodicidad"]]
        formularios = ", ".join(sorted(h["series"].formulario.unique()))
        return (f"{cuenta.capitalize()} en los establecimientos de salud de Bolivia, por {periodo} y municipio, en las "
                f"gestiones {rangos(h['gestiones'])}. Fuente: SNIS, formularios {formularios}.")

    def datapackage(self, h: dict, advertencias, procedencia, correcciones) -> dict:
        campos = []
        for c in h["columnas"]:
            if c in COLUMNAS:
                tipo, descripcion, _ = COLUMNAS[c]
            elif c in PROPIAS:
                tipo, descripcion = "string", PROPIAS[c]
            else:
                tipo, descripcion = "integer", f"Número de {h['valor']} en la fila."
            campo = {"name": c, "type": tipo, "description": descripcion}
            if c in h["categorias"]:
                campo["categories"] = [v for v, _ in h["categorias"][c]]
            campos.append(campo)
        formularios = sorted(h["series"].formulario.unique())
        return {
            "$schema": "https://datapackage.org/profiles/2.0/datapackage.json",
            "name": h["dataset"],
            "title": h["nombre"],
            "description": self.resumen(h),
            "keywords": [k for k in (h["dominio"], h["clasificacion"], h["tema"]) if k],
            "sources": [{"title": f"SNIS, Ministerio de Salud y Deportes de Bolivia, formulario {f}",
                         "path": self.fuentes.get((f, str(h["series"][h["series"].formulario == f].gestion.max())), "")}
                        for f in formularios],
            "temporal": {"gestiones": h["gestiones"], "periodicidad": h["periodicidad"]},
            "spatial": {"unidad": "municipio", "municipios": h["municipios"]},
            "resources": [{"name": "datos", "path": "datos.parquet", "format": "parquet",
                           "mediatype": "application/vnd.apache.parquet", "schema": {"fields": campos}}],
            "snis": {
                "dominio": h["dominio"], "clasificacion": h["clasificacion"], "tema": h["tema"],
                "filas": h["filas"], "totales": {str(g): int(t) for g, t in h["totales"]},
                "edades": [{"gestiones": r, "bandas": b} for r, b in bloques(h["edades"])],
                "advertencias": advertencias, "correcciones": correcciones,
                "relacionados": [{"datasets": [f"{c[0]}/{c[1]}/{c[2]}" for c in claves], "supuesto": supuesto, "unir": unir}
                                 for claves, supuesto, unir, _ in self.relacionados(h)],
                "procedencia": [dict(zip(["gestiones", "formulario", "variable", "soaps", "cie10", "cie10_codigos"], p))
                                for p in procedencia],
            },
        }

    def readme(self, h: dict, advertencias, procedencia, correcciones) -> str:
        v, ruta = h["valor"], f"datos/{h['dominio']}/{h['clasificacion']}/{h['dataset']}/datos.parquet"
        lineas = [f"# {h['nombre']}", "", self.resumen(h), "", "## Qué es", ""]
        lineas += ["| | |", "| --- | --- |", f"| Gestiones | {rangos(h['gestiones'])} |",
                   f"| Periodicidad | {h['periodicidad']} |", f"| Municipios con registros | {h['municipios']} |",
                   f"| Desagregación | {self.desagregacion(h)} |", f"| Filas | {miles(h['filas'])} |", ""]
        for c, valores in h["categorias"].items():
            if len(valores) > 1 or c in h["propias"]:
                nombre = NOMBRE_PROPIA.get(c, COLUMNAS.get(c, (0, 0, c.replace("_", " ")))[2] or c.replace("_", " "))
                lineas += [f"Valores de `{c}` ({nombre}):", ""]
                lineas += [f"- {valor} ({gestiones})" for valor, gestiones in valores[:60]]
                if len(valores) > 60:
                    lineas.append(f"- y {len(valores) - 60} valores más (ver `datapackage.json`)")
                lineas.append("")
        if h["edades"]:
            lineas += ["Bandas de edad (`edad_grupo`) por gestión:", "", "| Gestiones | Bandas |", "| --- | --- |"]
            lineas += [f"| {r} | {b} |" for r, b in bloques(h["edades"])] + [""]
        lineas += ["Total por gestión:", "", f"| Gestión | {v.capitalize()} |", "| ---: | ---: |"]
        lineas += [f"| {g} | {miles(t)} |" for g, t in h["totales"]] + [""]
        if advertencias:
            lineas += ["### Advertencias", ""] + [f"- {a}" for a in advertencias] + [""]
        lineas += self.tabla_implausibles(h)

        lineas += ["## Cómo utilizar", "", f"Cada fila da el número de {v} de un periodo, un municipio y una población. "
                   "Para obtener un total, sume las filas: el dataset no tiene filas de total. Una combinación sin fila "
                   "significa que no hubo registros. Las convenciones de tiempo, territorio y población están en el "
                   "[catálogo](../../../README.md#cómo-leer-los-datos).", "",
                   "| Columna | Tipo | Descripción |", "| --- | --- | --- |"]
        for c in h["columnas"]:
            tipo, descripcion = (COLUMNAS[c][:2] if c in COLUMNAS else ("string", PROPIAS[c]) if c in PROPIAS
                                 else ("integer", f"Número de {v} en la fila."))
            lineas.append(f"| `{c}` | {tipo} | {descripcion} |")
        detalle = next((c for c in h["propias"]), None) or next((c for c in ("sexo", "edad_grupo") if c in h["columnas"]), None)
        lineas += ["", "Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:", "", "```sql",
                   "-- Total por gestión", f"select gestion, sum({v}) as {v}", f"from '{ruta}'",
                   "group by gestion order by gestion;"]
        if detalle:
            lineas += ["", f"-- Por gestión y {detalle}", f"select gestion, {detalle}, sum({v}) as {v}", f"from '{ruta}'",
                       "group by all order by all;"]
        lineas += ["", "-- Por departamento en la última gestión", f"select departamento, sum({v}) as {v}", f"from '{ruta}'",
                   f"where gestion = {h['gestiones'][-1]} group by all order by {v} desc;", "```", ""]
        lineas += self.seccion_relacionados(h)

        con_cie = any(c for *_, c, _ in procedencia)
        lineas += ["## De dónde viene", "", "Los datos vienen de los tableros del Sistema Nacional de Información en "
                   "Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) "
                   "y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del "
                   "software del SNIS cuyas reglas describen la variable, con el año de su instalador."
                   + (" Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; "
                      "los códigos completos están en `datapackage.json` (`snis.procedencia`)." if con_cie else ""), ""]
        if con_cie:
            lineas += ["| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |", "| --- | --- | --- | --- | --- |"]
            lineas += [f"| {r} | {f} | {var} | {s} | {c} |" for r, f, var, s, c, _ in procedencia] + [""]
        else:
            lineas += ["| Gestiones | Formulario | Variable del tablero | SOAPS |", "| --- | --- | --- | --- |"]
            lineas += [f"| {r} | {f} | {var} | {s} |" for r, f, var, s, *_ in procedencia] + [""]
        if correcciones:
            lineas += ["Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):", ""]
            lineas += [f"- {c}" for c in correcciones] + [""]
        return "\n".join(lineas)

    def documentar(self, dominio: str, clasificacion: str, dataset: str) -> None:
        h = self.hechos(dominio, clasificacion, dataset)
        advertencias, procedencia, correcciones = self.advertencias(h), self.procedencia(h), self.correcciones(h)
        ruta = DATOS / dominio / clasificacion / dataset
        paquete = self.datapackage(h, advertencias, procedencia, correcciones)
        texto = json.dumps(paquete, ensure_ascii=False, indent=2)
        (ruta / "datapackage.json").write_text(texto.replace("«", '\\"').replace("»", '\\"') + "\n")
        (ruta / "readme.md").write_text(comillas(self.readme(h, advertencias, procedencia, correcciones)))
        self.catalogo.append({**{k: h[k] for k in ("dominio", "clasificacion", "dataset", "nombre", "tema", "periodicidad")},
                              "gestiones": rangos(h["gestiones"]), "desagregacion": self.desagregacion(h),
                              "formularios": ", ".join(sorted(h["series"].formulario.unique())),
                              **dict(zip(["comentario", "relacionados"], self.comentario(h, advertencias)))})


def main() -> None:
    doc = Documentador()
    for dominio in DOMINIOS:
        for ruta in sorted((DATOS / dominio).glob("*/*/datos.parquet")):
            doc.documentar(dominio, ruta.parent.parent.name, ruta.parent.name)
    catalogo = pd.DataFrame(doc.catalogo)
    catalogo.to_parquet(INTERMEDIOS / "catalogo.parquet", index=False)
    escribir_catalogo(catalogo)
    escribir_municipios(doc.con)
    print(f"{len(catalogo)} datasets documentados")


def escribir_municipios(con) -> None:
    ruta = REFERENCIAS / "municipios"
    n, departamentos = con.sql(f"select count(*), count(distinct departamento) from '{ruta}/datos.parquet'").fetchone()
    campos = [("municipio_codigo", "Código del municipio, 6 dígitos: departamento (2), provincia (2) y municipio (2)."),
              ("municipio", "Nombre más reciente del municipio."), ("provincia_codigo", "Código de la provincia, 4 dígitos."),
              ("departamento_codigo", "Código del departamento, 2 dígitos."), ("departamento", "Nombre del departamento.")]
    paquete = {"$schema": "https://datapackage.org/profiles/2.0/datapackage.json", "name": "municipios",
               "title": "Municipios", "description": f"Código y nombre de los {n} municipios del SNIS.",
               "sources": [{"title": "SNIS, padrón de establecimientos de salud", "path": "../../descarga/dimensiones/establecimientos/"}],
               "resources": [{"name": "datos", "path": "datos.parquet", "format": "parquet",
                              "mediatype": "application/vnd.apache.parquet",
                              "schema": {"fields": [{"name": c, "type": "string", "description": d} for c, d in campos],
                                         "primaryKey": ["municipio_codigo"]}}]}
    (ruta / "datapackage.json").write_text(json.dumps(paquete, ensure_ascii=False, indent=2) + "\n")
    l = ["# Municipios", "", f"Código y nombre de los {n} municipios de los {departamentos} departamentos, según el padrón de "
         "establecimientos de salud del SNIS. Sirve para unir los datasets con otras fuentes por municipio o para "
         "completar municipios sin registros.", "", "## Cómo utilizar", "", "| Columna | Descripción |", "| --- | --- |"]
    l += [f"| `{c}` | {d} |" for c, d in campos]
    l += ["", "```sql", "-- Casos de tos ferina de 2024 por provincia", "select m.provincia_codigo, sum(c.casos) as casos",
          "from 'datos/vigilancia/casos/tos_ferina/datos.parquet' c",
          "join 'referencias/municipios/datos.parquet' m using (municipio_codigo)",
          "where c.gestion = 2024 group by all order by casos desc;", "```", "", "## De dónde viene", "",
          "Del padrón de establecimientos que acompaña a los tableros del SNIS ([`descarga/dimensiones/establecimientos`]"
          "(../../descarga/dimensiones/establecimientos/)). Cuando un municipio cambia de nombre entre gestiones, se usa el "
          "más reciente.", ""]
    (ruta / "readme.md").write_text("\n".join(l))


def escribir_catalogo(catalogo: pd.DataFrame) -> None:
    n = len(catalogo)
    l = ["# Datos del SNIS de Bolivia", "",
         f"{n} datasets con las estadísticas del Sistema Nacional de Información en Salud (SNIS) del Ministerio de "
         "Salud y Deportes, de 2001 a 2025, por municipio. Cada dataset es una carpeta con tres archivos:", "",
         "- `datos.parquet`: los datos;", "- `readme.md`: qué contiene, cómo usarlo y de dónde viene;",
         "- `datapackage.json`: los mismos metadatos en formato [Data Package](https://datapackage.org).", "",
         "Las carpetas siguen el orden `datos/<dominio>/<clasificación>/<dataset>/`. Hay dos dominios: vigilancia "
         "epidemiológica (formularios 302, 302a y 302b: casos, defunciones y otros eventos) y producción de servicios "
         "(formularios 301, 301a y 301b: consultas, vacunas, partos y otras prestaciones). La clasificación dice qué "
         "cuenta el dataset.", "", "Índice:", ""]
    for dominio, (titulo, _) in DOMINIOS.items():
        l.append(f"- [{titulo}](#{titulo.lower().replace(' ', '-')})")
    l += ["- [Referencias](#referencias)", "- [Cómo leer los datos](#cómo-leer-los-datos)", ""]
    for dominio, (titulo, formularios) in DOMINIOS.items():
        d = catalogo[catalogo.dominio == dominio]
        l += [f"## {titulo}", "", f"{len(d)} datasets de los {formularios}.", ""]
        for clasificacion, c in d.groupby("clasificacion", sort=False):
            cuenta = CLASIFICACIONES[clasificacion][1]
            l += [f"### {TITULOS[clasificacion]}", "", f"{cuenta.capitalize()}. {len(c)} datasets.", ""]
            grupos = c.groupby("tema", dropna=False, sort=True) if c.tema.notna().any() else [(None, c)]
            for tema, t in grupos:
                if tema is not None and isinstance(tema, str):
                    l += [f"#### {tema.capitalize()}", ""]
                l += ["| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |",
                      "| --- | --- | --- | --- | --- | --- | --- |"]
                for r in t.sort_values(["nombre", "gestiones"]).itertuples():
                    l.append(f"| [{r.nombre}]({r.dominio}/{r.clasificacion}/{r.dataset}/readme.md) | {r.gestiones} | "
                             f"{r.formularios} | {r.periodicidad} | {r.desagregacion} | {r.comentario} | {r.relacionados} |")
                l.append("")
    l += ["## Referencias", "", "- [Municipios](../referencias/municipios/readme.md): código, nombre, provincia y "
          "departamento de cada municipio.", ""]
    l += CONVENCIONES.splitlines() + ["", "### Correcciones de rótulos", "",
          "Cada columna del tablero tiene un encabezado de hasta tres niveles, separados por « | »: en «e. 10 a 14 "
          "años - F | NUEVO», el primer nivel da la edad y el sexo, y el segundo, si el caso es nuevo. El tablero "
          "arma estos encabezados con plantillas, y en algunos grupos de variables la plantilla no describe las "
          "columnas: por ejemplo, rotula «nuevo» y «repetido» columnas que en realidad son el sexo. "
          "Cada corrección se apoya en evidencia de los datos, de SOAPS o de los instructivos, y el readme de cada "
          "dataset dice cuáles se aplicaron. Lista completa:", ""]
    l += [f"- {texto}" for texto in CORRECCIONES.values()] + [""]
    (DATOS / "README.md").write_text(comillas("\n".join(l)))


CONVENCIONES = """## Cómo leer los datos

### Formularios

Cada establecimiento informa al SNIS con formularios mensuales o semanales. En servicios, el formulario 301
(2001-2014) registra todos los servicios. Desde 2015 se divide en dos registros complementarios: el 301a, para
los servicios de primer nivel, y el 301b, para los de segundo y tercer nivel. El nivel es del servicio, no del
establecimiento: un hospital informa en los dos. Por eso un dataset nunca une el 301a con el 301b. Si una
variable tiene el mismo nombre en los dos (los sueros de enfermería), el dataset del 301b lleva «(formulario
301b)» en el nombre. Una variable del 301 continúa en el dataset del 301a con el mismo nombre o, si sólo está
en el 301b, en el del 301b. En
vigilancia, el 302 (2001-2014) es semanal; desde 2015 hay dos formularios: el 302a (semanal) y el 302b (mensual).

### Tiempo

`gestion` es el año calendario. Los formularios 302 y 302a registran por semana epidemiológica (`semana`); los
demás, por mes (`mes`). Un dataset que une formularios semanales y mensuales tiene las dos columnas, y cada fila
tiene sólo una. `fecha_inicio` es el primer día de la semana o del mes. La semana epidemiológica va de domingo a
sábado, y la semana 1 es la primera semana con al menos cuatro días del año nuevo. Por eso algunas gestiones
tienen 53 semanas (2003, 2008, 2014, 2020 y 2025).

### Territorio

`municipio_codigo` tiene 6 dígitos: departamento (2), provincia (2) y municipio (2). `departamento` y `municipio`
son los nombres más recientes. La tabla [municipios](../referencias/municipios/readme.md) da también el código
de provincia.

### Población

Cada dataset tiene sólo las columnas de población que la fuente registra. La edad es un intervalo en años:
`edad_desde` incluido y `edad_hasta` excluido (6 meses = 0,5; un `edad_hasta` vacío no tiene límite). Así, la
banda «1 a 4 años» es `edad_desde = 1` y `edad_hasta = 5`. `edad_grupo` repite la banda en texto corto. Las
bandas cambian entre gestiones: para comparar gestiones, agrupe en bandas compatibles. `caso` dice si la
atención es nueva o repetida, como la registra el formulario. `lugar` dice si ocurrió dentro o fuera del
establecimiento.

### Ceros y totales

El SNIS registra eventos, no ausencias, y no distingue «cero casos» de «no notificó». Por eso los datasets no
tienen filas con valor cero: una combinación sin fila significa que no hubo registros. Para un análisis que
necesita ceros (promedios, tasas, modelos de conteo), complételos con una consulta. Ejemplo, casos de tos
ferina por municipio y semana de 2024:

```sql
with semanas as (select distinct semana from 'datos/vigilancia/casos/tos_ferina/datos.parquet' where gestion = 2024),
municipios as (select municipio_codigo from 'referencias/municipios/datos.parquet'),
casos as (select municipio_codigo, semana, sum(casos) as casos from 'datos/vigilancia/casos/tos_ferina/datos.parquet'
          where gestion = 2024 group by all)
select m.municipio_codigo, s.semana, coalesce(c.casos, 0) as casos
from municipios m cross join semanas s left join casos c using (municipio_codigo, semana);
```

Los datasets tampoco tienen filas de total: para un total, sume las filas.

### Categorías y datasets relacionados

Algunos datasets unen varias variables del tablero con una columna propia que las distingue: la dosis de una
vacuna, el método anticonceptivo, la forma clínica de la lepra. Un dataset tiene un solo conjunto de categorías
en todas sus gestiones. Cuando el formulario cambia las categorías (la hepatitis viral se divide en A, B y C en
2015), empieza otro dataset, con las gestiones en el nombre: `hepatitis_viral_2001_2014`,
`hepatitis_viral_2015_2020`. Lo mismo pasa cuando cambia la definición de una variable con el mismo nombre: el
flujo uretral incluye el flujo vaginal desde 2011. Así ningún dataset supone que dos conjuntos de categorías o
dos definiciones distintas cuentan lo mismo. Un cambio de rótulo que no cambia lo que se cuenta (ortografía,
numeración, abreviaturas) no divide un dataset; el readme lista las variables del tablero de cada gestión.

El readme de cada dataset enlaza, en «Datasets relacionados», los datasets que cuentan algo parecido con otras
categorías, otra definición, otro nombre u otro formulario. Dice qué cambia y qué supone unirlos, y da la
consulta para hacerlo. En el catálogo, la columna «Comentario» resume lo que distingue a cada dataset (sus
categorías y sus datasets relacionados) y sus advertencias.

En el formulario 302 de 2001 a 2003, algunas enfermedades aparecen en dos secciones con cifras distintas. Son
datasets separados y el readme de cada uno enlaza al otro. No sume los dos: un caso puede estar en ambos.

### Registros implausibles

Algunas filas tienen una población que la definición excluye: por ejemplo, cáncer de próstata en mujeres. Se
publican tal como se registraron, porque no hay información para saber si son errores ni de qué tipo. El readme
de cada dataset las lista en «Advertencias», con su volumen, para que quien analiza decida si las excluye.

### Códigos CIE-10 y SOAPS

SOAPS es el software de atención primaria del SNIS. Sus reglas dicen qué diagnósticos (códigos CIE-10) y qué
poblaciones cuenta cada variable. El readme de cada dataset da, por gestión, la versión de SOAPS que describe la
variable y las categorías CIE-10. SOAPS existe desde 2013 (versión 1.0.4): para las gestiones anteriores, la
versión asignada es la más parecida por nombre y poblaciones, y sus códigos son una aproximación. Las
defunciones tienen códigos internos de SOAPS, no CIE-10."""


if __name__ == "__main__":
    main()
