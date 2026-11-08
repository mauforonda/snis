"""Traducción de etiquetas de población del tablero a atributos estructurados.

Una etiqueta del tablero une hasta tres niveles de encabezado con « | ». Su significado
depende del formulario y de la gestión. Las reglas de este módulo son explícitas y
cada una corresponde a un patrón observado en los datos descargados.

Convención de edad: intervalo semiabierto [edad_desde, edad_hasta) en años.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import asdict, dataclass

DIAS = 1 / 365.25


@dataclass
class Atributos:
    es_total: bool = False
    sexo: str | None = None          # mujer | hombre
    edad_desde: float | None = None
    edad_hasta: float | None = None
    edad_grupo: str | None = None
    caso: str | None = None          # nuevo | repetido
    lugar: str | None = None         # dentro | fuera
    condicion: str | None = None     # embarazada | puerpera
    especialidad: str | None = None  # servicios de hospital (301b)
    servicio: str | None = None      # servicio que pide un estudio (301b): consulta externa, ...
    especie: str | None = None       # especie de Plasmodium (malaria)
    tratamiento: str | None = None   # iniciado | concluido
    participante: str | None = None  # perfil de quien participa en teleeducación
    medida: str | None = None        # eventos | personas_afectadas | ...
    posicion: int | None = None      # posición en la plantilla a..j × sufijo, desde 1
    sufijo: str | None = None        # letra tras « - » en el primer nivel (D, F, M, H)
    nivel2: str | None = None        # segundo nivel sin números finales
    duplicado: bool = False          # pandas añadió «.1» a un encabezado repetido
    regla: str | None = None         # nombre de la regla aplicada
    sin_traducir: bool = False
    conflicto: bool = False          # dos niveles dan valores distintos al mismo atributo

    def dict(self) -> dict:
        return asdict(self)


def normalizar(texto: str) -> str:
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    return " ".join(texto.lower().replace("\xa0", " ").split())


def _anios(numero: str, unidad: str) -> float:
    n = float(numero)
    if unidad.startswith("mes") or unidad == "m":
        return n / 12
    if unidad.startswith("dia"):
        return n * DIAS
    return n


def _grupo(desde: float | None, hasta: float | None, unidad: str = "a") -> str:
    def fmt(valor: float) -> str:
        if unidad == "d":
            return f"{round(valor / DIAS)}d"
        if valor < 1 and valor > 0:
            return f"{round(valor * 12)}m"
        return f"{valor:g}"

    if hasta is None:
        return f"{fmt(desde)}+"
    if not desde:
        return f"<{fmt(hasta)}"
    if unidad == "d":
        return f"{fmt(desde)}-{fmt(hasta - DIAS)}"
    if hasta <= 1:
        a, b = round(desde * 12), round(hasta * 12) - 1
        return f"{a}m" if a == b else f"{a}-{b}m"
    if desde < 1:
        return f"{fmt(desde)}-{hasta - 1:g}"
    if hasta - desde == 1:
        return f"{desde:g}"
    return f"{desde:g}-{hasta - 1:g}"


# Expresiones de banda de edad, ya normalizadas (minúsculas, sin tildes).
_U = r"(anos?|meses|mes|m|dias?)"
_BANDAS = [
    # «menor de 6 meses», «< de 1 año», «< 7 dias», «menores de 5 años», «< a 1 año»
    (re.compile(rf"^(?:menor(?:es)? de|< de|< a|<)\s*(\d+)\s*{_U}$"), "menor"),
    # «6 m a menor de 1 año», «1 a menor de 2 años»
    (re.compile(rf"^(\d+)\s*{_U}?\s*a menor de\s*(\d+)\s*{_U}$"), "a_menor"),
    # «60 y más», «60 años y más», «60 a más», «50 y +», «mayores de 60 años»
    (re.compile(rf"^(\d+)\s*{_U}?\s*(?:y mas|a mas|y \+|o mas)$"), "y_mas"),
    (re.compile(rf"^mayores de\s*(\d+)\s*{_U}?$"), "y_mas"),
    # «4 años», «6 meses»: un año o un mes cumplido
    (re.compile(rf"^(\d+)\s*{_U}$"), "exacta"),
    # «1 a 4 años», «1 - 4 años», «7 a 28 dias»
    (re.compile(rf"^(\d+)\s*(?:a|-)\s*(\d+)\s*{_U}$"), "rango"),
]


def banda(texto: str) -> tuple[float, float | None, str] | None:
    """Devuelve (edad_desde, edad_hasta, edad_grupo) o None si el texto no es una banda."""
    t = normalizar(texto)
    for patron, tipo in _BANDAS:
        m = patron.match(t)
        if not m:
            continue
        if tipo == "menor":
            n, u = m.groups()
            hasta = _anios(n, u)
            return 0.0, round(hasta, 4), _grupo(0.0, hasta, "d" if u.startswith("dia") else "a")
        if tipo == "a_menor":
            a, ua, b, ub = m.groups()
            desde = _anios(a, ua or ub)
            hasta = _anios(b, ub)
            return desde, hasta, _grupo(desde, hasta)
        if tipo == "y_mas":
            a, u = m.groups()
            desde = _anios(a, u or "anos")
            return desde, None, _grupo(desde, None)
        if tipo == "exacta":
            a, u = m.groups()
            desde = _anios(a, u)
            hasta = desde + (1 if u.startswith("ano") else 1 / 12)
            return round(desde, 4), round(hasta, 4), _grupo(desde, hasta)
        if tipo == "rango":
            a, b, u = m.groups()
            # «1 a 4 años» incluye a quien tiene 4 años: el límite superior excluido es 5.
            desde = _anios(a, u)
            if u.startswith("dia"):
                hasta = _anios(b, u) + DIAS
                return round(desde, 4), round(hasta, 4), _grupo(desde, hasta, "d")
            hasta = _anios(b, u) + (1 if u.startswith("ano") else 1 / 12)
            return desde, hasta, _grupo(desde, hasta)
    return None


_LETRA = re.compile(r"^([a-j])\.\s+(.*)$")
_SUFIJO = re.compile(r"^(.*?)\s*-\s*([DFMH])$")
_NUM_FINAL = re.compile(r"^(.*?)(\d+)$")

_MEDIDAS = {
    # 302a 2024, grupo 15: el tablero repite «Nevada» en lugar de los tres encabezados
    # de medida; el orden es el de 2023 y 2025 (eventos, afectados, fallecidos).
    "nevada": "eventos",
    "nevada1": "personas_afectadas",
    "nevada2": "personas_fallecidas",
    "nro. eventos": "eventos",
    "nro.": "eventos",
    "nro. personas afectadas": "personas_afectadas",
    "nro. de personas afectadas": "personas_afectadas",
    "nro. afectados": "personas_afectadas",
    "nro. personas fallecidas": "personas_fallecidas",
    "nro. de personas fallecidas": "personas_fallecidas",
    "nro. fallecidos": "personas_fallecidas",
    "nro. de personas damnificadas": "personas_damnificadas",
    "nro. de pacientes atendidos": "pacientes_atendidos",
}


def traducir(formulario: str, gestion: int, etiqueta: str) -> Atributos:
    """Interpreta una etiqueta según las convenciones de su formulario y gestión."""
    a = Atributos()
    niveles = [n.strip() for n in etiqueta.split("|")]

    if normalizar(niveles[0]).startswith("total"):
        a.es_total = True
        a.regla = "total"
        return a

    # Segundo nivel. pandas añade «.1» a encabezados repetidos; el 302b numera las columnas.
    if len(niveles) > 1:
        n2 = niveles[1]
        if n2.endswith(".1"):
            a.duplicado = True
            n2 = n2[:-2]
        m = _NUM_FINAL.match(n2)
        if m and m.group(1).upper() in ("NUEVO", "REPETIDO"):
            n2 = m.group(1)
        a.nivel2 = n2.upper()

    primero = niveles[0]
    m = _LETRA.match(primero)
    letra = None
    if m:
        letra, primero = m.groups()
    m = _SUFIJO.match(primero)
    if m:
        primero, a.sufijo = m.group(1), m.group(2)

    # Medidas de emergencias y desastres.
    medida = _MEDIDAS.get(normalizar(primero))
    if medida:
        a.medida, a.regla = medida, "medida"
        return a

    b = banda(primero)
    t = normalizar(primero)
    if b:
        a.edad_desde, a.edad_hasta, a.edad_grupo = b
    elif t in ("dentro", "fuera"):
        a.lugar = t
    elif t == "embarazada":
        a.condicion = "embarazada"
    elif t == "imc":
        pass
    elif t == "cantidad":
        pass
    else:
        a.sin_traducir = True
        a.regla = "sin_traducir"
        return a

    if letra:
        a.posicion = (ord(letra) - ord("a")) * (2 if a.sufijo else 1) + (2 if a.sufijo == "F" else 1)

    # Primer nivel: sufijo de sexo o de lugar.
    if a.sufijo:
        if formulario == "302":
            a.sexo = {"H": "hombre", "M": "mujer"}.get(a.sufijo)
        elif formulario == "302b":
            a.sexo = {"F": "mujer", "M": "hombre"}.get(a.sufijo)
        elif formulario == "302a":
            a.lugar = {"D": "dentro", "F": "fuera"}.get(a.sufijo)

    # Segundo nivel.
    n2 = a.nivel2
    if n2 in ("FEMENINO", "MASCULINO"):
        valor = "mujer" if n2 == "FEMENINO" else "hombre"
        if formulario == "302b" and a.sufijo:
            # 302b 2015: el sufijo es el sexo y el segundo nivel, mal rotulado, es el caso.
            # SOAPS 3.0.1 divide cada subvariable de sexo en reglas de caso nuevo y repetido;
            # la proporción primera/segunda columna coincide con nuevo/repetido de 2017.
            a.caso = "nuevo" if n2 == "FEMENINO" else "repetido"
            a.regla = "302b_2015_caso"
        else:
            a.sexo = valor
    elif n2 in ("NUEVO", "REPETIDO"):
        a.caso = n2.lower()
    elif n2 in ("DENTRO", "FUERA"):
        a.lugar = n2.lower()
    elif n2 == "MUJER EMBARAZADA":
        a.condicion = "embarazada"
        a.sexo = "mujer"
    elif n2 == "____":
        a.sin_traducir = True
        a.regla = "columna_vacia"
        return a
    elif n2 is not None:
        a.sin_traducir = True
        a.regla = "sin_traducir"
        return a

    a.regla = a.regla or "texto"
    return a


# ---------------------------------------------------------------------------
# Correcciones por familia de variables.
#
# El tablero arma los encabezados con plantillas por grupo. En algunas familias la
# plantilla no describe las columnas. Cada regla indica la evidencia que la sostiene.
# ---------------------------------------------------------------------------

CORRECCIONES = {
    "301a_sexo_en_lugar": (
        "301a, vacunas de 12 a 23 meses, de 2 a 3 años y de 4 años, 2015-2023: el segundo nivel dice "
        "DENTRO/FUERA otra vez, pero las reglas de SOAPS 6.0.1 dividen estas variables por sexo y lugar (código 3012805). "
        "El segundo nivel «DENTRO» suma 50,6 % y la proporción de varones en las vacunas rotuladas por "
        "sexo es 50,9 %: DENTRO es hombre y FUERA es mujer."
    ),
    "301_tratamiento_repetido": (
        "301 y 301a, tratamientos de chagas, leishmaniasis y en mujeres posparto: el tablero repite las "
        "columnas de sexo («FEMENINO» y «FEMENINO.1»). En 2020 los totales dicen «TOTAL Iniciado» y "
        "«TOTAL Concluido», y coinciden con la primera y la segunda columna: la primera es tratamiento "
        "iniciado y la repetida, concluido."
    ),
    "301b_columnas_sin_rotulo": (
        "301b, actividades de enfermería, 2024-2025: cada variable tiene tres columnas sin rótulo "
        "(«Sueros», «Sueros1», «Sueros2») que suman el total. El formulario 301b de 2024 tiene, en ese "
        "orden, las columnas emergencias, consulta externa e internación, y el instructivo de 2024 nombra "
        "los mismos servicios: se publican como esos servicios."
    ),
    "301a_columnas_edad": (
        "301a, anticoncepción y prevención del cáncer (2015-2016) e interrupción legal del embarazo (2021): "
        "las variables tienen cinco columnas sin rótulo («Número de condones entregados», «...1» a «...4»). "
        "Son las bandas de edad <15, 15-19, 20-34, 35-49 y 50+, en ese orden. En anticoncepción las "
        "proporciones coinciden con las de 2017 (muestras de PAP 2016: 0,3 %, 7,1 %, 48,5 %, 32,0 % y 12,2 %; "
        "2017: 0,3 %, 7,1 %, 48,4 %, 31,7 % y 12,5 %). En la interrupción legal del embarazo, el encabezado de "
        "2022 une cada columna numerada con su banda («A. < 15», «B. 15 A 19 ... 1»). En 2022 la segunda "
        "banda de las causales riesgo de salud de la madre y malformación dice «15 A 49»; es 15-19."
    ),
    "301_caso_segundo_nivel": (
        "301, control de crecimiento, 2008-2009: el primer nivel dice siempre NUEVO; el segundo dice "
        "NUEVO/REPETIDO y sus totales coinciden con «TOTAL NUEVO» y «TOTAL REPETIDO»: vale el segundo."
    ),
    "302b_sexo_en_caso": (
        "302b, grupos 01, 05, 06, 07 y 10: el segundo nivel dice NUEVO/REPETIDO, pero las reglas de "
        "SOAPS dividen estas variables por sexo. Las muertes por cáncer de mama y de cuello uterino "
        "están en REPETIDO en todas las gestiones 2016-2025, y el tabaco y el alcohol (grupo 01, "
        "2024-2025) están sobre todo en NUEVO: REPETIDO es mujer y NUEVO es hombre."
    ),
    "302b_embarazada": (
        "302b, grupo 06: la columna Embarazada se divide en 10-19 y 20-59 años (reglas de SOAPS "
        "para el código 3050604). La columna menor es 10-19: NUEVO o MASCULINO es 10-19; "
        "REPETIDO o FEMENINO es 20-59."
    ),
    "nutricion_menor_1": (
        "302 (grupos 11 y 14, 2008-2014) y 302b (grupos 06 y 07): SOAPS cuenta la columna "
        "«Menor de 1 año» desde los 2 meses (reglas de 2 a 11 meses)."
    ),
    "302a_materna_lugar": (
        "302a, grupo 10, 2024-2025: el segundo nivel dice FEMENINO/MASCULINO, pero SOAPS 7.0.1 "
        "divide por lugar. Las complicaciones atendidas dentro del establecimiento son muchas más "
        "que fuera (preeclampsia 2025: 2.513 frente a 137): MASCULINO es dentro y FEMENINO es fuera."
    ),
    "302_sin_sexo": (
        "302, 2001-2007: en las variables cuyas columnas «-M» siempre valen 0, «TOTAL-H» es igual "
        "a «TOTAL»: «-H» contiene a ambos sexos. Esas variables no tienen sexo. En 2004 el grupo 09 "
        "(mortalidad) tampoco tiene sexo: hay 79 muertes maternas en «-H» y 94 en «-M»."
    ),
    "total_unico": (
        "302, grupo 13 (intoxicaciones), 2001-2003: la variable tiene una sola columna, «TOTAL-M». "
        "Se publica sin sexo, como total. Evidencia: la magnitud es la de un total de ambos sexos. "
        "Organofosforados suma de 1.700 a 2.208 por gestión en 2001-2003, y plaguicidas, sin "
        "sexo, suma 2.170 en 2004 y 2.077 en 2005."
    ),
    "solo_total": (
        "Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, "
        "sin desagregación."
    ),
    "302a_mortalidad_desplazada": (
        "302a, grupo 09, 2021-2025: el encabezado repite «f. 15 - 19 años - F» (pandas lo marca "
        "con «.1») y desplaza una posición a todas las columnas siguientes. La columna repetida es "
        "«g. 20 - 39 años - D» y cada etiqueta siguiente corresponde a la posición que le sigue. La "
        "última etiqueta («j. 60 años y más - F») no tiene columna propia: en los 15 archivos del grupo "
        "09 de 2021-2025 repite, fila por fila, la primera columna («a. Menor de 6 meses - D»)."
    ),
}

# Plantilla de posiciones del grupo 09 del 302a: 10 bandas por dos lugares.
_BANDAS_09 = [
    ("a. Menor de 6 meses"), ("b. 6 m a menor de 1 año"), ("c. 1 - 4 años"), ("d. 5 - 9 años"),
    ("e. 10 a 14 años"), ("f. 15 - 19 años"), ("g. 20 - 39 años"), ("h. 40 - 49 años"),
    ("i. 50 - 59 años"), ("j. 60 años y más"),
]


def corregir(formulario: str, gestion: int, grupo: str, variable: str, etiqueta: str,
             a: Atributos, desplazar: bool) -> Atributos:
    """Aplica las correcciones de familia a los atributos traducidos de una etiqueta."""
    if a.es_total or a.sin_traducir or a.medida:
        return a

    if formulario == "302b" and grupo in ("01", "05", "06", "07", "10") and not a.sufijo:
        if a.condicion == "embarazada" and grupo == "06":
            menor = a.nivel2 in ("NUEVO", "MASCULINO")
            a.edad_desde, a.edad_hasta = (10.0, 20.0) if menor else (20.0, 60.0)
            a.edad_grupo = "10-19" if menor else "20-59"
            a.sexo, a.caso = "mujer", None
            a.regla = "302b_embarazada"
        elif a.nivel2 in ("NUEVO", "REPETIDO"):
            a.sexo = "hombre" if a.nivel2 == "NUEVO" else "mujer"
            a.caso = None
            a.regla = "302b_sexo_en_caso"

    nutricion = (formulario == "302b" and grupo in ("06", "07")) or (
        formulario == "302" and gestion >= 2008 and grupo in ("11", "14"))
    if nutricion and a.edad_desde == 0 and a.edad_hasta == 1:
        a.edad_desde, a.edad_grupo = round(2 / 12, 4), "2-11m"
        a.regla = (a.regla or "texto") + "+nutricion_menor_1"

    if formulario == "302a" and grupo == "10" and a.nivel2 in ("FEMENINO", "MASCULINO"):
        a.lugar = "dentro" if a.nivel2 == "MASCULINO" else "fuera"
        a.sexo = "mujer"
        a.regla = "302a_materna_lugar"

    if formulario == "302a" and grupo == "09" and desplazar and a.posicion:
        posicion = 13 if a.duplicado else (a.posicion + 1 if a.posicion >= 13 else a.posicion)
        if posicion != a.posicion:
            if posicion > 20:
                a.sin_traducir = True
                a.regla = "302a_mortalidad_desplazada:fuera_de_plantilla"
                return a
            texto = _BANDAS_09[(posicion - 1) // 2] + (" - D" if posicion % 2 else " - F")
            nuevo = traducir(formulario, gestion, texto + " | " + a.nivel2)
            nuevo.posicion, nuevo.regla = posicion, "302a_mortalidad_desplazada"
            return nuevo
    return a


# ---------------------------------------------------------------------------
# Producción de servicios (301, 301a, 301b).
#
# La etiqueta repite el nombre de la variable (completo, truncado o dos veces) y añade los
# atributos: «PENTAVALENTE 1RA DOSIS DENTRO | FEMENINO», «ESPECIALIDAD: PEDIATRIA | 1 A 4
# AÑOS NUEVO | MASCULINO». Se quita el nombre y se interpretan las palabras que quedan.
# ---------------------------------------------------------------------------

_NUMERACION = re.compile(r"^(l\s*)?\d+(\.\d+)+\s*|^(l\s*)?\d+\s*(\.-|-|\.)\s*")
_PALABRAS = {
    "sexo": {"femenino": "mujer", "masculino": "hombre", "maculino": "hombre", "mujer": "mujer", "hombre": "hombre"},
    "caso": {"nuevo": "nuevo", "nuevos": "nuevo", "nueva": "nuevo", "nuevas": "nuevo", "primera": "primera",
             "repetido": "repetido", "repetidos": "repetido", "repetida": "repetido", "repetidas": "repetido"},
    "lugar": {"dentro": "dentro", "fuera": "fuera", "d": "dentro", "f": "fuera",
              "servicio": "servicio", "domicilio": "domicilio"},
    "condicion": {"emb": "embarazada", "post": "puerpera"},
    "servicio": {"ce": "consulta externa", "c.e.": "consulta externa", "internacion": "internación",
                 "emergencia": "emergencia", "emergencias": "emergencia", "quirofano": "quirófano"},
    "especie": {"vivax": "P. vivax", "falciparum": "P. falciparum"},
    "tratamiento": {"iniciado": "iniciado", "inciado": "iniciado", "concluido": "concluido"},
    "participante": {"medicos": "médicos", "enfermera": "enfermería", "auxiliar": "auxiliares", "odonto": "odontología",
                     "otro_personal": "otro personal", "dirigente": "dirigentes", "promotores": "promotores",
                     "promotor": "promotores", "adultos": "adultos", "jovenes": "jóvenes", "escolar": "escolares",
                     "otros": "otros"},
}
_PALABRA = {p: (campo, valor) for campo, d in _PALABRAS.items() for p, valor in d.items()}
_IGNORAR = {"cantidad", "serv/dom"}


def _norm(texto: str) -> str:
    return " ".join(normalizar(texto).replace("°", "o").replace("º", "o").split())


def quitar_variable(texto: str, variable: str) -> str:
    """Quita de un nivel de la etiqueta el nombre de la variable: completo, repetido o truncado."""
    t, v = _NUMERACION.sub("", _norm(texto)), _NUMERACION.sub("", _norm(variable))
    if len(v) < 2:
        return t
    if t.startswith(v) and len(t) > len(v) and t[len(v)].isalnum():      # nombre truncado en el índice
        t = t[len(v):].split(" ", 1)[1] if " " in t[len(v):] else ""
    t = " ".join(t.replace(v, " ").split())
    for k in range(len(v) - 1, 2, -1):                                    # final del nombre repetido
        if t.startswith(v[-k:]) and (len(t) == k or t[k] == " "):
            t = t[k:].strip()
            break
    t = t.replace("grupo edad: (cantidad)", " ")
    palabras = [p for p in t.split() if not re.fullmatch(r"\d+\.\d*", p)]       # «25.5», numeración
    vp = v.split()
    if palabras and len(palabras[0]) >= 2 and vp[-1].endswith(palabras[0]) and palabras[0] != vp[-1]:
        palabras = palabras[1:]                                           # «os nuevo» de «años nuevo»
    if palabras and all(p in vp for p in palabras if p not in _PALABRA):  # el nombre otra vez, abreviado
        palabras = [p for p in palabras if p in _PALABRA or p not in vp]
    return " ".join(palabras)


def _banda_servicio(texto: str):
    t = re.sub(r"^[a-j]\.\s+", "", texto).replace("< a ", "< ").replace(" y +", " y mas")
    t = re.sub(r"^(\d+ \w+) < (\d+ \w+)$", r"\1 a menor de \2", t)
    return banda(t) or banda(t + " anos")


def traducir_servicio(formulario: str, gestion: int, variable: str, etiqueta: str) -> Atributos:
    """Interpreta una etiqueta de producción de servicios."""
    a = Atributos()
    # 301a 2022, interrupción legal del embarazo: la segunda banda dice «15 A 49» (CORRECCIONES).
    if "INTERRUPCIONES LEGALES" in etiqueta.upper():
        etiqueta = re.sub(r"(B\. 15 A) 49", r"\1 19", etiqueta)
    niveles = [n.strip() for n in etiqueta.split("|")]
    if _norm(niveles[0]).startswith("especialidad:"):
        a.especialidad = niveles.pop(0).split(":", 1)[1].strip().capitalize()
    textos = [quitar_variable(n, variable) for n in niveles]
    con_total = _norm(variable).startswith("total")
    if not niveles or any((_norm(n).startswith("total") and not con_total) or _norm(n) in ("total", "totales")
                          or t.startswith("total") or " total " in f" {t} " for n, t in zip(niveles, textos)):
        a.es_total, a.regla = True, "total"
        return a
    if len(niveles) == 1 and not textos[0] and a.especialidad is None:
        # Columna sin rótulo: «Sueros», «Sueros1», «Sueros2». Su significado depende de la
        # variable-gestión (corregir_servicio).
        a.posicion = int(re.search(r"(\d?)$", niveles[0]).group(1) or 0) + 1
    a.regla = "texto"
    pendiente = []
    for i, texto in enumerate(textos):
        if re.search(r"(femenino|masculino)(\.1|1)$", texto):
            a.duplicado = True                                   # columna repetida (CORRECCIONES)
        texto = re.sub(r"(?<=[a-z])(\.1|\d+)$", "", texto)    # «otras actividades2», «femenino.1»
        texto = re.sub(r"\s*-\s*([a-z]+)$", r" \1", texto)                         # «< a 1 año - d»
        palabras = texto.split()
        while palabras and palabras[-1] in _PALABRA:
            campo, valor = _PALABRA[palabras.pop()]
            previo = getattr(a, campo)
            if previo and previo != valor and i > 0:
                if campo == "lugar" and formulario == "301a":
                    # Vacunas de 12 meses a 4 años: el segundo nivel es el sexo (CORRECCIONES).
                    campo, valor, a.regla = "sexo", {"dentro": "hombre", "fuera": "mujer"}[valor], "301a_sexo_en_lugar"
                elif campo == "caso":
                    a.regla = "301_caso_segundo_nivel"                  # el primer nivel es plantilla
                else:
                    a.conflicto = True
            setattr(a, campo, valor)
        resto = " ".join(p for p in palabras if p not in _IGNORAR)
        if resto:
            pendiente.append(resto)
    for texto in pendiente:
        b = _banda_servicio(texto)
        if b and a.edad_desde is None:
            a.edad_desde, a.edad_hasta, a.edad_grupo = b
        else:
            a.sin_traducir, a.regla = True, "sin_traducir"
    return a


_BANDAS_ANTICONCEPCION = [(0.0, 15.0, "<15"), (15.0, 20.0, "15-19"), (20.0, 35.0, "20-34"), (35.0, 50.0, "35-49"),
                          (50.0, None, "50+")]


_SERVICIOS_ENFERMERIA = ["emergencia", "consulta externa", "internación"]


def corregir_servicio(formulario: str, columnas: int, repetidas: bool, a: Atributos) -> Atributos:
    """Correcciones que dependen de toda la variable-gestión.

    columnas: número de columnas sin rótulo; repetidas: la variable-gestión repite columnas de sexo.
    """
    if repetidas and a.sexo:
        a.tratamiento = "concluido" if a.duplicado else "iniciado"
        a.duplicado, a.regla = False, "301_tratamiento_repetido"
    if a.posicion and columnas > 1:
        if formulario == "301a" and columnas == 5:
            a.edad_desde, a.edad_hasta, a.edad_grupo = _BANDAS_ANTICONCEPCION[a.posicion - 1]
            a.regla = "301a_columnas_edad"
        elif formulario == "301b" and columnas == 3:
            a.servicio, a.regla = _SERVICIOS_ENFERMERIA[a.posicion - 1], "301b_columnas_sin_rotulo"
        else:
            a.sin_traducir, a.regla = True, "columna_sin_rotulo"
    return a
