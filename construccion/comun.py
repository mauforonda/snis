"""Rutas, clasificaciones y conexión duckdb compartidas por los pasos de construcción."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import duckdb

RAIZ = Path(__file__).resolve().parents[1]
DESCARGA = RAIZ / "descarga"
DATOS_FUENTE = DESCARGA / "datos"
INDICE = DESCARGA / "indice.csv"
SOAPS = RAIZ / "contexto" / "sistemas" / "soaps" / "tablas"
INTERMEDIOS = RAIZ / "construccion" / "intermedios"
DATOS = RAIZ / "datos"
REFERENCIAS = RAIZ / "referencias"

FORMULARIOS = {"vigilancia": ("302", "302a", "302b"), "servicios": ("301", "301a", "301b")}
VIGILANCIA, SERVICIOS = FORMULARIOS["vigilancia"], FORMULARIOS["servicios"]

# Prefijo de casilla SOAPS por formulario de los tableros.
PREFIJO_CASILLA = {"301": "301", "301a": "301", "301b": "304", "302": "302", "302a": "302", "302b": "305"}

# Clasificación (carpeta) -> columna del valor, qué cuenta (catálogo) y qué cuenta un dataset (readme).
CLASIFICACIONES = {
    "casos": ("casos", "personas atendidas con un diagnóstico", "personas atendidas con este diagnóstico"),
    "defunciones": ("defunciones", "muertes", "muertes por esta causa"),
    "estado_nutricional": ("personas", "personas evaluadas, por resultado", "personas evaluadas, por resultado"),
    "factores_riesgo": ("personas", "personas con un factor de riesgo", "personas con este factor de riesgo"),
    "desarrollo_infantil": ("personas", "niñas y niños evaluados, por resultado", "niñas y niños evaluados, por resultado"),
    "emergencias": ("cantidad", "eventos y personas afectadas", "eventos y personas afectadas"),
    "consultas": ("cantidad", "consultas externas, de emergencia, interconsultas y telesalud", "atenciones registradas"),
    "odontologia": ("cantidad", "consultas y tratamientos odontológicos", "atenciones registradas"),
    "salud_materna_neonatal": ("cantidad", "control prenatal, partos, recién nacidos e interrupción legal del embarazo",
                               "atenciones y nacimientos registrados"),
    "anticoncepcion_prevencion_cancer": ("cantidad", "anticoncepción y detección de cáncer de cuello uterino y de mama",
                                         "atenciones registradas"),
    "nutricion": ("cantidad", "control de crecimiento, micronutrientes y alimentación complementaria", "atenciones registradas"),
    "vacunas": ("cantidad", "dosis de vacuna aplicadas", "dosis aplicadas"),
    "internacion": ("cantidad", "ingresos, egresos y días cama", "registros de internación"),
    "cirugia": ("cantidad", "cirugías, anestesias y quirófanos", "registros"),
    "diagnostico_tratamiento": ("cantidad", "laboratorio, imagen, tratamientos y enfermería", "estudios y procedimientos realizados"),
    "control_enfermedades": ("cantidad", "tuberculosis, malaria, chagas, leishmaniasis, VIH, rabia y otras", "registros"),
    "enfermedades_cronicas": ("cantidad", "atenciones de enfermedades crónicas y salud mental", "atenciones registradas"),
    "referencias": ("cantidad", "referencias y contrarreferencias de pacientes", "pacientes o referencias registrados"),
    "gestion_comunidad": ("cantidad", "actividades con la comunidad y de gestión de calidad", "actividades registradas"),
}



@dataclass
class Relacion:
    """Datasets que cuentan algo parecido con otras categorías o con otro nombre. Un dataset nunca
    los une: la documentación los enlaza y da una consulta para unirlos, con el supuesto que hace.

    bases: datasets antes de dividirlos por formulario o por periodo (columna base del paso 3).
    supuesto: qué cambia entre ellos y qué supone consultarlos juntos como una serie.
    unir: False si no deben sumarse (dos secciones del formulario que cuentan lo mismo); la
    documentación no da entonces la consulta para unirlos.
    """
    bases: tuple[str, ...]
    supuesto: str
    unir: bool = True


def conectar(memoria: str = "4GB", hilos: int = 2) -> duckdb.DuckDBPyConnection:
    """Conexión con límites de memoria: los datos completos no caben en RAM."""
    temporal = INTERMEDIOS / "duckdb_tmp"
    temporal.mkdir(parents=True, exist_ok=True)
    con = duckdb.connect()
    con.execute(f"set memory_limit='{memoria}'")
    con.execute(f"set threads={hilos}")
    con.execute(f"set temp_directory='{temporal}'")
    con.execute("set preserve_insertion_order=false")
    return con
