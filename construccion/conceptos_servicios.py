"""Series de producción de servicios (formularios 301, 301a y 301b).

Cada variable-gestión del tablero se asigna a un dataset. El grupo del tablero da la
clasificación (la carpeta) y, a veces, atributos de población: la edad en las vacunas, el lugar
en los partos. El nombre de la variable da el resto: la dosis de una vacuna, el método y el tipo
de usuaria en anticoncepción, la edad y el caso en las consultas.

Sin una regla, una variable forma su propio dataset con su nombre normalizado; las variables con
el mismo nombre en distintas gestiones o formularios forman una serie. RELACIONES (al final)
enlaza datasets que cuentan algo parecido con otro nombre o con otras categorías.
"""

from __future__ import annotations

import re
import unicodedata

from comun import Relacion
from poblacion import banda

def normalizar(texto: str) -> str:
    t = unicodedata.normalize("NFKD", texto)
    t = "".join(c for c in t if not unicodedata.combining(c)).lower().replace("°", "o").replace("º", "o")
    t = " ".join(t.replace("\xa0", " ").split())
    t = re.sub(r"^l\s*\d+(\.\d+)*\s*", "", t)                      # «l 21.7», código de línea (2012)
    t = re.sub(r"^\d+(\.\d+)+\s*|^\d+\s*(\.-|-|\.)\s*", "", t)      # «7.2», «1.», «18.-»
    t = re.sub(r"^\d{3,}\s+|^\d+ (?=[a-z]{3})(?!anos|meses|dias|a |y )", "", t)  # «1310 dias», «1 ingresos»
    t = re.sub(r"^total\s+(de\s+)?", "", t)
    t = re.sub(r"^(no\.?|nro\.?|na|n?umero)\s*de\s*", "", t)                # «úmero de» (2015-2020)
    t = re.sub(r"(\d)(ra|da|ta)\.", r"\1\2", t)                     # «1ra.» -> «1ra»
    t = re.sub(r"(\d) g\b\.?", r"\1g", t)                            # «2500 g» -> «2500g»
    return t.strip(" .*:")


def limpiar(nombre: str) -> str:
    """Nombre para mostrar: sin numeración, «Total» ni «N° de», con tildes y en minúscula salvo las siglas."""
    t = " ".join(nombre.replace("\xa0", " ").split())
    t = re.sub(r"^l\s*\d+(\.\d+)*\s*|^\d+(\.\d+)+\.?\s*|^\d+\s*(\.-|-|\.)\s*", "", t, flags=re.I)  # «10.2.», «1.-»
    t = re.sub(r"^\d{3,}\s+|^\d+ (?=[a-záéíóú]{3})(?!años|meses|días)", "", t, flags=re.I)        # «1310 días», «3 egresos»
    t = re.sub(r"^total\s+(de\s+)?", "", t, flags=re.I)
    t = re.sub(r"^(n\s*[°ºª˚o]\.?|nro\.?|n?[úu]mero|na)\s*de\s*", "", t, flags=re.I)
    siglas = set() if t.isupper() else {w for w in re.findall(r"\b[A-ZÁÉÍÓÚÑ]{2,5}\b|\b[IVX]{1,4}\b", t)}
    t = t[:1].upper() + t[1:].lower()
    for sigla in siglas:
        t = re.sub(rf"\b{sigla.lower()}\b", sigla, t, flags=re.I)
    return t.strip(" .*:")


def slug(texto: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", normalizar(texto)).strip("_")[:60]


# Grupo del tablero -> clasificación y atributos de población que implica. Primera coincidencia.
GRUPOS = [
    (r"vacunaciones en menores de 1|vacunaciones en menores de 1 ano dentro", "vacunas", {"edad": "menor de 1 ano"}),
    (r"12 a 23 meses", "vacunas", {"edad": "12 a 23 meses"}),
    (r"12 meses a menores de 5", "vacunas", {"edad": "12 meses a menor de 5 anos"}),
    (r"24 a menores de 5", "vacunas", {"edad": "24 meses a menor de 5 anos"}),
    (r"2 a 3 anos", "vacunas", {"edad": "2 a 3 anos"}),
    (r"2 a 4 anos", "vacunas", {"edad": "2 a 4 anos"}),
    (r"ninos de 4 anos", "vacunas", {"edad": "4 anos"}),
    (r"vacuna", "vacunas", {}),
    (r"perros y gatos|rabia|ofidios|tuberculosis|lepra|malaria|chagas|leishmaniasis|^vih|vectorial", "control_enfermedades", {}),
    (r"consulta externa|^emergencia|interconsultas|telesalud", "consultas", {}),
    (r"odontolog", "odontologia", {}),
    (r"partos? en servicio|parto y puerperio", "salud_materna_neonatal", {"lugar": "servicio"}),
    (r"partos? en domicilio", "salud_materna_neonatal", {"lugar": "domicilio"}),
    (r"prenatal|recien nacidos|interrupcion legal|metabolismo", "salud_materna_neonatal", {}),
    (r"anticoncepcion|planificacion familiar", "anticoncepcion_prevencion_cancer", {}),
    (r"crecimiento|nutricion|micronutrientes|lactancia|estado nutricional", "nutricion", {}),
    (r"diagnostico de egreso en menores de 5", "internacion", {"edad": "menores de 5 anos"}),
    (r"internacion|ingresos y egresos|egreso|dias camas", "internacion", {}),
    (r"cirugia|quirofano", "cirugia", {}),
    (r"enfermeria|complementarios", "diagnostico_tratamiento", {}),
    (r"referencia|refencias|contrareferencia|retornos", "referencias", {}),
    (r"no transmisibles", "enfermedades_cronicas", {}),
    (r".", "gestion_comunidad", {}),
]

# Nombres distintos de una misma serie (forma normalizada -> forma canónica).
ALIAS = {
    "ingresos-nuevos": "nuevos", "ingresos-existencia": "existencia", "ingresos-traslado interno": "traslado interno - ingresos",
    "egresos-traslado interno": "traslado interno - egresos", "egresos-alta medica": "alta",
    "egresos-defuncion antes de 48 hrs": "defuncion antes de 48 hrs", "defuncion despues de 48 hrs": "defuncion a partir de 48 hrs",
    "egresos-defuncion a partir de 48 hrs": "defuncion a partir de 48 hrs", "fallecidos antes de las 48 hrs": "fallecidos antes de las 48 horas",
    "fallecidos a partir de las 48 hrs": "fallecidos a partir de las 48 horas", "dias cama disp": "dias cama disponibles",
    "dias cama ocupada": "dias camas ocupadas", "contrarreferidos": "contrareferidos", "retornados": "contrareferidos",
    "pacientes contrarreferidos al establecimiento": "pacientes contrareferidos al establecimiento",
    "pacientes retornados al establecimiento de origen": "pacientes contrareferidos al establecimiento",
    "pacientes referidos de la comunidad o medicina tradicional": "pacientes derivados de la comunidad o medicina tradicional",
    "pcd referidas a unidades de calificacion de discapacidad": "pcd referidos a unidades de calificacion de discapacidad",
    "viviendas roceadas": "viviendas rociadas", "deanestesias locales": "anestesias locales",
    "seciones de fisioterapia realizadas": "sesiones de fisioterapia realizadas",
    "inyectable": "inyectables", "primeras consultas": "primera consulta",
    "mujeres con muestra de pap tomada": "mujeres con muestras de pap tomadas", "mujeres con muestra de pap": "mujeres con muestras de pap tomadas",
    "mujeres con muestra de citologia cervico vaginal": "mujeres con muestras de pap tomadas",
    "numero de mujeres con pildora anticonceptiva oral de emergencia": "mujeres con pildora anticonceptiva oral de emergencia",
    "tbp baar (+) nuevos": "tb pulmonar baar positivo nuevos", "tbp baar (-) nuevos": "tb pulmonar baar negativo nuevos",
    "tbp baar (+) nuevos curados": "tb pulmonar baar positivo nuevos curados",
    "trat. odontologico integral terminado (toit)": "trat. odontologico integral terminado",
    "actividades realizadas con participacion": "actividades realizadas con participacion de la comunidad",
    "anestesias locales realizadas": "anestesias locales", "cirugias menores realizadas": "cirugias menores",
    "mujeres con primer control post parto": "primer control post parto", "endodoncias": "endodoncia",
    "exodoncias": "exodoncia", "periodoncias": "periodoncia", "medidas preventivas": "acciones preventivas",
}

MOVIMIENTO = {
    "existencia": "ingreso: existencia al inicio", "nuevos": "ingreso: nuevo", "referidos": "ingreso: referido",
    "traslado interno - ingresos": "ingreso: traslado interno", "alta": "egreso: alta médica",
    "egresos-alta solicitada": "egreso: alta solicitada", "egresos-alta fuga": "egreso: fuga",
    "defuncion antes de 48 hrs": "egreso: defunción antes de 48 horas",
    "defuncion a partir de 48 hrs": "egreso: defunción a partir de 48 horas",
    "traslado interno - egresos": "egreso: traslado interno", "contrareferidos": "egreso: contrarreferido",
    "ingresos y egresos del mismo dia": "ingreso y egreso el mismo día",
}

# Nombres para mostrar de datasets cuyo nombre del tablero está abreviado.

PROGRAMAS = {"chagas": "Chagas", "malaria": "Malaria", "dengue": "Dengue", "tuberculosis": "Tuberculosis",
             "leishmaniasis": "Leishmaniasis", "vih": "VIH", "rabia": "Rabia", "ofidios": "Ofidios"}

# --- Vacunas -----------------------------------------------------------------------------------
VACUNAS = [
    (r"pentavalentes?|pentavelente", "pentavalente", "Pentavalente"),
    (r"antipoliomiel?itica|o\.p\.v|polio", "antipoliomielitica", "Antipoliomielítica"),
    (r"antirotavir", "antirrotavirica", "Antirrotavírica"),
    (r"neumococica", "antineumococica", "Antineumocócica"),
    (r"^bcg", "bcg", "BCG"),
    (r"srp", "srp", "SRP (sarampión, rubéola y parotiditis)"),
    (r"^(vacunaciones )?sr\b|vacunaciones (dentro|fuera) de servicio", "sr", "SR (sarampión y rubéola)"),
    (r"amarilica|fiebre amarilla", "antiamarilica", "Antiamarílica"),
    (r"\bdpt\b", "dpt", "DPT"),
    (r"\bdt\b", "dt", "dT (difteria y tétanos)"),
    (r"influenza", "influenza_estacional", "Influenza estacional"),
    (r"hepatitis b", "hepatitis_b", "Hepatitis B"),
    (r"covid", "covid_19", "COVID-19"),
    (r"vph", "vph", "VPH (virus del papiloma humano)"),
]
DOSIS = [(r"dosis inicial", "inicial"), (r"\b5ta\b", "5"), (r"\b4(ta|da)\b", "4"), (r"\b3(ra|da)\b", "3"),
         (r"\b2(da|ra)\b", "2"), (r"\b1r?a\b", "1"), (r"anual", "anual"), (r"unica", "única"), (r"refuerzo", "refuerzo")]
GRUPO_VACUNA = [
    (r"trabajador(es)? de salud|personal de salud", "personal de salud"), (r"vih", "personas con VIH"),
    (r"renales", "personas con enfermedad renal"), (r"inmunodeprimidos", "personas inmunodeprimidas"),
    (r"enfermedad(es)? cronicas?", "personas con enfermedad crónica"), (r"embarazadas", "embarazadas"),
    (r"mayores de 6[05]", "personas de 60 años y más"), (r"cumpliran 10", "niñas de 10 años"),
]


def _vacuna(n: str, fijo: dict) -> dict | None:
    for patron, ident, nombre in VACUNAS:
        if re.search(patron, n):
            atributos = {"dosis": next((v for p, v in DOSIS if re.search(p, n)), None)}
            atributos["grupo"] = next((v for p, v in GRUPO_VACUNA if re.search(p, n)), None)
            if re.search(r"dentro de servicio", n):
                fijo["lugar"] = "dentro"
            elif re.search(r"fuera de servicio", n):
                fijo["lugar"] = "fuera"
            m = re.search(r"(?:mujeres )?de (\d+ a \d+ anos)", n)
            if m:
                fijo["edad"] = m.group(1)
            if n.startswith("mujeres"):
                fijo["sexo"] = "mujer"
            m = re.search(r"\((\d+) ?m a (\d+) ?m\)|\((\d+) a (\d+) m\)", n)
            if m:
                a, b = [x for x in m.groups() if x]
                fijo["edad"] = f"{a} a {b} meses"
            return {"dataset": ident, "nombre": f"Vacuna {nombre}", "atributos": atributos}
    return None


# --- Reglas por nombre ---------------------------------------------------------------------------
VITAMINA_A = r"vitam|dosis unica d(e v?i?)?$|dosis v$|aceite v"
HIERRO = r"hier|90 tabletas|dosis comp?$"     # «con dosis com(pleta de hierro)», truncado
METODOS = [(r"ciclos", "píldora"), (r"^diu", "DIU"), (r"inyectable", "inyectable trimestral"), (r"condon femenino", "condón femenino"),
           (r"condon", "condón masculino"), (r"pildora", "píldora"), (r"implante", "implante subdérmico"),
           (r"metodos naturales", "métodos naturales")]
MOMENTO_PRENATAL = [(r"antes del 5to mes", "nueva antes del 5.º mes"), (r"a partir del 5to mes", "nueva desde el 5.º mes"),
                    (r"1er trimestre", "nueva en el 1.er trimestre"), (r"2do trimestre", "nueva en el 2.º trimestre"),
                    (r"3er trimestre", "nueva en el 3.er trimestre"), (r"^repetidas$", "repetida")]


def _edad_en(n: str) -> str | None:
    """Banda de edad dentro del nombre: «nuevas en menores de 5 años» -> «menores de 5 anos»."""
    n = re.sub(r"(del? )?recien nac\w*( a menor(es)? de 1 ano)?", "menor de 1 ano", n)
    n = re.sub(r"(a |de )?< ?(de )?(\d+)( a\w*)?$", r"a menor de \3 anos", n)          # «a < de 5 añ», «de < 5»
    n = re.sub(r"(a |de )?< ?(de )?(\d+)", r"a menor de \3", n)
    m = re.search(r"(menor(es)? de \d+ anos?|de \d+ anos? a menor(es)? de \d+ anos?|\d+ anos? a menor(es)? de \d+ anos?"
                  r"|de \d+ (a|-) \d+ (anos|meses)|\d+ a \d+ (anos|meses)|\d+ anos? (y|o) mas|rn a menor(es)? de 1 ano"
                  r"|de \d+ meses? a menor(es)? de \d+ anos?|\d+ meses? a menor de \d+ anos?|de \d+ anos? y mas)", n)
    return m and m.group(1).replace("rn a menor", "menor")


def edad(texto: str | None):
    """(edad_desde, edad_hasta, edad_grupo) de una banda escrita en un nombre, o None."""
    if not texto:
        return None
    t = re.sub(r"^de ", "", texto).replace("a menores de", "a menor de").replace("a menor 5", "a menor de 5")
    return banda(t)


def asignar(formulario: str, gestion: int, grupo: str, variable: str) -> dict:
    """Clasificación, dataset, atributos y población fija de una variable-gestión de servicios."""
    g, n = normalizar(grupo), normalizar(variable)
    n = ALIAS.get(n, n)
    clasificacion, fijo = next((c, dict(f)) for p, c, f in GRUPOS if re.search(p, g))
    r = None

    if clasificacion == "vacunas" or (clasificacion == "gestion_comunidad" and re.search(r"dosis|vacuna", n)):
        r = _vacuna(n, fijo)
        if r:
            clasificacion = "vacunas"
        elif re.search(r"antirrabica", n):
            clasificacion = "control_enfermedades"
    elif clasificacion == "consultas" and (re.search(r"^(nuevas|repetidas) en ", n) or _edad_en(n) or edad(n)):
        m = re.match(r"^(nuevas|repetidas) en ", n)
        if m:
            fijo["caso"] = "nuevo" if m.group(1) == "nuevas" else "repetido"
        fijo["edad"] = _edad_en(n) or n
        # La variable es una banda de edad: el nombre es el del grupo («Consulta externa por especialidad»).
        # El grupo «Emergencia» del 301b continúa en 2024 en la variable «Consulta por emergencia».
        r = ({"dataset": "consulta_por_emergencia", "nombre": "Consulta por emergencia"} if g == "emergencia"
             else {"dataset": slug(grupo), "nombre": limpiar(grupo)})
    elif clasificacion == "consultas" and re.match(r"^(teleconsultas|teleinterconsultas generadas) [ns]$", n):
        # Instructivo del 301a (2024), telesalud: «N» es nueva y «S», de seguimiento.
        fijo["caso"] = "nuevo" if n.endswith(" n") else "seguimiento"
        tele = n[:-2]
        r = {"dataset": slug(tele), "nombre": tele.capitalize()}
    elif clasificacion == "consultas" and n.startswith("teledispositivos "):
        dispositivo = n.split(" ", 1)[1]
        dispositivo = {"ecografo": "ecógrafo", "electrocardiografo": "electrocardiógrafo",
                       "espirometro": "espirómetro"}.get(dispositivo, dispositivo)
        r = {"dataset": "teledispositivos", "nombre": "Teledispositivos", "atributos": {"dispositivo": dispositivo}}
    elif clasificacion == "consultas" and n == "consulta por emergencia":
        r = {"dataset": "consulta_por_emergencia", "nombre": "Consulta por emergencia"}
    elif clasificacion == "anticoncepcion_prevencion_cancer":
        m = re.match(r"^(.*?)\s*: usuarias? ?\(?o?s?\)? (nuevas?|continuas?)", n)
        metodo = next((v for p, v in METODOS if re.search(p, n)), None)
        if m and metodo:
            r = {"dataset": "usuarias_anticoncepcion", "nombre": "Usuarias de anticoncepción",
                 "atributos": {"metodo": metodo, "usuaria": "nueva" if m.group(2).startswith("nueva") else "continua"}}
        elif metodo and re.search(r"(insertados|suministrad|entregados)$", n):
            r = {"dataset": "insumos_anticonceptivos", "nombre": "Insumos anticonceptivos entregados o insertados",
                 "atributos": {"metodo": metodo}}
        elif re.match(r"^aqv (femenino|masculino)$", n):
            fijo["sexo"] = "mujer" if n.endswith("femenino") else "hombre"
            r = {"dataset": "anticoncepcion_quirurgica", "nombre": "Anticoncepción quirúrgica voluntaria"}
    elif clasificacion == "nutricion" and re.search(r"control(es)? del? ni|controles (nuevos|repetidos)", n):
        m = re.search(r"controles (nuevos|repetidos)", n)
        if m:
            fijo["caso"] = "nuevo" if m.group(1) == "nuevos" else "repetido"
        fijo["edad"] = _edad_en(n)
        if "dentro del establecimiento" in n or "dentro del establecimie" in n:
            fijo["lugar"] = "dentro"
        elif "fuera del establecimien" in n:
            fijo["lugar"] = "fuera"
        r = {"dataset": "control_crecimiento", "nombre": "Control de crecimiento infantil"}
    elif clasificacion == "nutricion" and re.search(VITAMINA_A + "|" + HIERRO + r"|zinc|alimento compl|lactancia|complemento nutricional", n):
        for patron, ident, nombre in [(HIERRO, "hierro", "Hierro"), (VITAMINA_A, "vitamina_a", "Vitamina A"),
                                      (r"zinc", "zinc", "Zinc"), (r"alimento complement|complemento nutricional", "alimento_complementario", "Alimento complementario"),
                                      (r"lactancia", "lactancia_materna", "Lactancia materna")]:
            if re.search(patron, n):
                break
        if "embarazada" in n:
            fijo["condicion"], fijo["sexo"] = "embarazada", "mujer"
        elif re.search(r"puerperas|periodo de lactancia", n):
            fijo["condicion"], fijo["sexo"] = "puerpera", "mujer"
        else:
            fijo["edad"] = _edad_en(n.replace("6 m.", "6 meses").replace("6 mese ", "6 meses ")) or (
                "menores de 1 ano" if "menores de 1 ano" in n else "1 ano" if re.search(r"de 1 ano (con|que)", n) else
                "menores de 6 meses" if "menores de 6 meses" in n else "60 anos y mas" if "60 anos" in n else None)
        atributos = {"dosis": next((v for p, v in DOSIS if re.search(p, n)), None)}
        if ident == "lactancia_materna":
            atributos = {"tipo": "inmediata" if "inmediata" in n else "exclusiva"}
        r = {"dataset": ident, "nombre": f"Personas que recibieron {nombre[:1].lower()}{nombre[1:]}" if ident != "lactancia_materna" else "Lactancia materna",
             "atributos": atributos}
    elif clasificacion == "salud_materna_neonatal" and re.search(r"^(nuevas|repetidas)", n) and "odontolog" not in g:
        momento = next((v for p, v in MOMENTO_PRENATAL if re.search(p, n)), None)
        if momento:
            r = {"dataset": "consulta_prenatal", "nombre": "Consultas prenatales", "atributos": {"momento": momento}}
    elif clasificacion == "salud_materna_neonatal" and n in ("vaginales", "cesareas"):
        r = {"dataset": "partos", "nombre": "Partos vaginales y cesáreas", "atributos": {"via": "vaginal" if n == "vaginales" else "cesárea"}}
    elif clasificacion == "odontologia" and re.search(r"^(consultas? )?(nuevas?|repetidas?)( |$)", n):
        fijo["caso"] = "repetido" if "repetida" in n else "nuevo"
        if "embarazada o puerpera" in n:
            fijo["condicion"] = "embarazada o puerpera"
        else:
            fijo["edad"] = _edad_en(n)
        r = {"dataset": "consulta_odontologica", "nombre": "Consultas odontológicas"}
    elif clasificacion == "control_enfermedades" and re.search(r"tratamientos? (iniciados con )?esquema", n):
        m = re.search(r"esquema (.*)$", n)
        esquema = {"l": "I", "ll": "II", "lll": "III", "i": "I", "ii": "II", "iii": "III"}.get(m.group(1), m.group(1))
        r = {"dataset": "tratamiento_tuberculosis_lepra", "nombre": "Tratamientos iniciados de tuberculosis y lepra",
             "atributos": {"esquema": esquema.replace("pausibacilar", "paucibacilar").replace(" (p.q.t.)", "")}}
    elif clasificacion == "control_enfermedades" and re.search(r"tratamientos de leishmania", n):
        forma = re.search(r"leishmania (.*)$", n).group(1).replace(" (mucosa)", "")
        r = {"dataset": "tratamiento_leishmaniasis", "nombre": "Tratamientos de leishmaniasis", "atributos": {"forma_clinica": forma}}
    elif clasificacion == "control_enfermedades" and re.search(r"chagas", g) and re.search(r"^tratamientos", n):
        if "post parto" in n:
            fijo["condicion"], fijo["sexo"] = "puerpera", "mujer"
        else:
            fijo["edad"] = _edad_en(n.replace("de edad", "").replace(" ,", ""))
        estado = "concluido" if "terminados" in n else "iniciado" if "iniciados" in n else None
        r = {"dataset": "tratamiento_chagas", "nombre": "Tratamientos de chagas", "atributos": {"tratamiento": estado}}
    elif clasificacion == "control_enfermedades" and re.search(r"malaria", g) and (edad(n) or n == "mujer embarazada"):
        if n == "mujer embarazada":
            fijo["condicion"], fijo["sexo"] = "embarazada", "mujer"
        else:
            fijo["edad"] = n.replace("de 1 a menores", "1 a menor").replace("de 5", "5")
        # Variables por edad del grupo «Malaria» (301a). Según el instructivo del 301a (2024) cuentan los
        # tratamientos específicos entregados a pacientes confirmados.
        r = {"dataset": "malaria_tratamientos_especificos", "nombre": "Malaria: tratamientos específicos entregados"}

    elif re.search(r"interrupcion legal", g):
        causal = next(v for p, v in [(r"violencia", "violencia sexual"), (r"riesgo", "riesgo para la salud de la madre"),
                                     (r"malformacion", "malformación congénita incompatible con la vida")] if re.search(p, n))
        trimestre = re.search(r"(1er|2do|3er) trimestre", n)
        r = {"dataset": "interrupcion_legal_embarazo", "nombre": "Interrupciones legales del embarazo",
             "atributos": {"causal": causal, "trimestre": trimestre and {"1er": "1.º", "2do": "2.º", "3er": "3.º"}[trimestre.group(1)]}}
    elif re.search(r"diagnostico de egreso", g):
        n = re.sub(r"\s+en (menores|mayores) de 5 anos$", "", n)
        r = {"dataset": "egresos_por_diagnostico", "nombre": "Egresos por diagnóstico",
             "atributos": {"diagnostico": n}}
    elif re.search(r"^interconsultas", g):
        r = {"dataset": "interconsultas", "nombre": "Interconsultas", "atributos": {"servicio": n}}
    elif re.search(r"ingresos y egresos por servicio", g) and not re.search(r"^(camas|dias cama)", n):
        r = {"dataset": "ingresos_egresos_hospital", "nombre": "Ingresos y egresos por servicio de internación",
             "atributos": {"movimiento": MOVIMIENTO.get(n, n)}}
    elif re.search(r"estado nutricional", g) and re.search(r"normal|baja", n):
        r = {"dataset": "talla_para_la_edad", "nombre": "Talla para la edad",
             "atributos": {"clasificacion": "normal" if "normal" in n else "baja"}}

    if r is None:
        # Edad o lugar al final del nombre: «diarreas en menores de 5 años», «... dentro del establecimiento».
        m = re.search(r"\s+(en|de) ((menores|mayores) de \d+)( anos?)?$", n)      # «en menores de 5» (2008)
        if m and edad(m.group(2) + " anos"):
            fijo["edad"], n = m.group(2) + " anos", n[:m.start()]
        m = re.search(r"\s+(dentro|fuera) del establecimiento$", n)
        if m:
            fijo["lugar"], n = m.group(1), n[:m.start()]
        programa = clasificacion == "control_enfermedades" and next(
            (p for p in ("chagas", "malaria", "dengue", "tuberculosis", "leishmaniasis", "vih", "rabia", "ofidios")
             if p in g or (p == "rabia" and "perros" in g)), None)
        nombre = limpiar(variable)
        if programa and programa not in n:
            inicio = nombre[:1] if nombre[1:2].isupper() else nombre[:1].lower()       # «TBP» queda igual
            n, nombre = f"{programa} {n}", f"{PROGRAMAS[programa]}: {inicio}{nombre[1:]}"
        r = {"dataset": slug(n), "nombre": nombre, "base": n}
    return {"clasificacion": clasificacion, "dataset": r["dataset"], "nombre": r["nombre"], "base": r.get("base"),
            "atributos": {k: v for k, v in r.get("atributos", {}).items() if v}, "fijo": fijo}


# --- Notas para el readme, por dataset (base) ---------------------------------------------------
NOTAS = {
    "malaria_tratamientos_especificos": (
        "El tablero no nombra estas variables: son columnas por edad del grupo «Malaria» del 301a. Según el "
        "instructivo del 301a (2024), cuentan los tratamientos específicos entregados a pacientes confirmados."),
    "consulta_por_emergencia": (
        "Hasta 2023 el tablero registra estas consultas como variables por edad del grupo «Emergencia» del 301b; "
        "el instructivo del 301b (2024) dice que son las consultas del servicio de emergencia. Desde 2024 son la "
        "variable «Consulta por emergencia», con la edad en las columnas."),
    "dias_camas_disponibles_otros_servicios": (
        "Carapari registra 11.545.414 días cama en diciembre de 2015, casi tres veces el total nacional de otras "
        "gestiones (unos 4,3 millones). Se publica tal como se registró; probablemente es un error de registro."),
}


# --- Datasets relacionados -------------------------------------------------------------------------
# Variables que cambian de nombre o de categorías entre gestiones. Los datasets con la misma base (un
# dataset dividido por formulario o por periodo) se enlazan sin declararlos aquí.
_UNIRLOS = "Consultarlos juntos como una serie supone que "
RELACIONES = [
    Relacion(("personas_que_recibieron_orientacion_en_anticoncepcion", "mujeres_que_recibieron_orientacion_en_anticoncepcion",
              "varones_que_recibieron_orientacion_en_anticoncepcion"),
             "Hasta 2020 el formulario cuenta personas que recibieron orientación en anticoncepción; desde 2021, mujeres "
             "y varones por separado. " + _UNIRLOS + "mujeres y varones suman lo mismo que «personas»."),
    Relacion(("sesiones_de_fisioterapia_realizadas", "seciones_de_fisioterapia_realizadas_en_c_e",
              "sesiones_de_fisioterapia_realizadas_en_internacion"),
             "Hasta 2023 el formulario cuenta las sesiones de fisioterapia sin servicio; desde 2024, en consulta externa y "
             "en internación. " + _UNIRLOS + "los dos servicios suman lo mismo que el total anterior."),
    Relacion(("visitas_familiares_realizadas", "primeras_visitas_familares_realizadas",
              "segundas_visitas_familiares_realizadas", "terceras_visitas_familiares"),
             "Hasta 2023 el formulario cuenta las visitas familiares realizadas; desde 2024, la primera, la segunda y la "
             "tercera visita. " + _UNIRLOS + "las tres suman lo mismo que «visitas realizadas»; el formulario no lo dice."),
    Relacion(("vih_mujeres_embarazadas_con_prueba_rapida", "mujeres_embarazadas_con_prueba_rapida_vih_1ra_prueba",
              "mujeres_embarazadas_con_prueba_rapida_vih_2da_prueba"),
             "Hasta 2023 el formulario cuenta embarazadas con prueba rápida de VIH; desde 2024, embarazadas con primera y "
             "con segunda prueba. " + _UNIRLOS + "la primera y la segunda prueba suman lo mismo que el total anterior; "
             "una mujer con las dos pruebas se cuenta dos veces."),
    Relacion(("partos_atendidos_por_personal_de_salud", "partos_atendidos_por_proveedor_calificado",
              "partos_atendidos_por_personal_de_salud_calificado"),
             "Hasta 2014 el formulario 301 cuenta los partos atendidos por personal de salud; desde 2015 el 301a separa "
             "proveedor calificado (médicos) y personal de salud calificado (enfermería), según su instructivo. "
             + _UNIRLOS + "los dos grupos de 2015 suman lo mismo que «personal de salud»."),
    Relacion(("partos_atendidos_por_partera_capacitada_u_otra_pe", "partos_atendidos_por_partera_capacitada"),
             "Hasta 2007 la variable es «partos atendidos por partera capacitada u otra pe…» (el tablero corta el nombre); "
             "desde 2008, «por partera capacitada». " + _UNIRLOS + "la variable no cambió de contenido."),
    Relacion(("nacidos_vivos_atendidos_por_partera_capacitada_u", "nacidos_vivos_atendidos_por_partera_capacitada",
              "nacidos_vivos_atendidos_por_partera"),
             "La variable cambia de nombre: «por partera capacitada u…» (2001-2007, el tablero corta el nombre), «por "
             "partera capacitada» (2008-2014) y «por partera» (desde 2015). " + _UNIRLOS + "las tres cuentan lo mismo."),
    Relacion(("nacidos_muertos_atendidos_por_partera_capacitada", "nacidos_muertos_atendidos_por_partera"),
             "La variable cambia de nombre: «por partera capacitada» (2001-2014) y «por partera» (desde 2015). "
             + _UNIRLOS + "las dos cuentan lo mismo."),
    Relacion(("cai_de_sector_realizados", "cai_de_establecimiento"),
             "Hasta 2009 la variable es «CAI de sector realizados»; desde 2010, «CAI de establecimiento». "
             + _UNIRLOS + "las dos cuentan lo mismo."),
    Relacion(("reuniones_realizadas_con_comites_loc_de_salud_consejo_mun_de", "reuniones_realizadas_con_comites_loc_de_salud"),
             "Hasta 2014 la variable cuenta reuniones con comités locales de salud o con el consejo municipal de salud; "
             "desde 2015, sólo con comités locales de salud. " + _UNIRLOS + "las reuniones con el consejo municipal no "
             "cambian la serie."),
    Relacion(("cirugias_medianas_y_mayores", "cirugias_medianas", "cirugias_mayores"),
             "Hasta 2014 el formulario 301 cuenta juntas las cirugías medianas y mayores; desde 2015 el 301b las cuenta "
             "por separado. " + _UNIRLOS + "las dos suman lo mismo que el total anterior."),
    Relacion(("anestesias_generales_locales_o_regionales", "anestesias_generales_y_regionales", "anestesias_generales",
              "anestesias_regionales"),
             "El formulario 301 cuenta juntas las anestesias generales, locales o regionales (2001-2007) y después las "
             "generales y regionales (2008-2014); desde 2015 el 301b cuenta por separado las generales y las regionales, "
             "y las locales están en otro dataset. " + _UNIRLOS + "las categorías de cada periodo cuentan lo mismo; "
             "antes de 2008 incluyen las locales."),
    Relacion(("tuberculosis_tb_pulmonar_baar_positivo_nuevos", "tuberculosis_tb_pulmonar_bacteriologicamente_confirmados_nue"),
             "Hasta 2023 el formulario cuenta los casos nuevos de tuberculosis pulmonar con baciloscopía (BAAR) positiva; "
             "desde 2024, los casos nuevos y recaídas confirmados por cualquier prueba bacteriológica. La definición nueva "
             "es más amplia. " + _UNIRLOS + "las dos definiciones cuentan lo mismo."),
    Relacion(("tuberculosis_tb_pulmonar_baar_negativo_nuevos", "tuberculosis_tb_pulmonar_clinicamente_diagnosticados_nuevos_"),
             "Hasta 2023 el formulario cuenta los casos nuevos de tuberculosis pulmonar con baciloscopía (BAAR) negativa; "
             "desde 2024, los casos nuevos y recaídas diagnosticados clínicamente. La definición nueva es más amplia. "
             + _UNIRLOS + "las dos definiciones cuentan lo mismo."),
    Relacion(("tuberculosis_tb_extrapulmonar_nuevos", "tuberculosis_tb_extrapulmonar_nuevos_y_recaidas"),
             "Hasta 2023 el formulario cuenta los casos nuevos de tuberculosis extrapulmonar; desde 2024, los nuevos y las "
             "recaídas. " + _UNIRLOS + "las recaídas no cambian la serie."),
    Relacion(("malaria_tratamientos_especificos_dispensados", "malaria_tratamientos_especificos"),
             "Hasta 2014 el formulario 301 cuenta los tratamientos específicos de malaria dispensados; desde 2015 el "
             "301a cuenta, por edad, los tratamientos específicos entregados a pacientes confirmados. "
             + _UNIRLOS + "las dos variables cuentan lo mismo."),
    Relacion(("malaria_tratamientos_iniciados_en_el_mes", "malaria_tratamientos_iniciados_en_el_mes_para_p_vivax",
              "malaria_tratamientos_iniciados_en_el_mes_para_p_falciparu", "malaria_tratamientos_iniciados_en_el_mes_por_personal_de",
              "malaria_tratamientos_iniciados_en_el_mes_por_agente_comun", "malaria_tratamientos_iniciados_por_sospecha"),
             "Los tratamientos de malaria iniciados cambian de categorías casi cada gestión: en total (2001-2003), por "
             "especie (2004), por quién trata (2005-2006) y por sospecha (2007-2014). En 2001-2003 el formulario cuenta "
             "también los tratamientos iniciados por sospecha, en otro dataset. " + _UNIRLOS + "las categorías de cada "
             "gestión suman todos los tratamientos iniciados."),
    Relacion(("malaria_tratamientos_terminados_en_el_mes", "malaria_tratamientos_terminados_en_el_mes_para_p_vivax",
              "malaria_tratamientos_terminados_en_el_mes_para_p_falcipar"),
             "Los tratamientos de malaria terminados se cuentan en total (2001-2003) y por especie (2004). "
             + _UNIRLOS + "las dos especies suman todos los tratamientos terminados."),
    Relacion(("malaria_muestras_tomadas_por_personal_de_salud", "malaria_muestras_tomadas_por_agente_comunario",
              "malaria_muestras_hematicas_tomadas"),
             "Las muestras de malaria se cuentan por quién las toma (2005-2006) y después en total (2007-2014). "
             + _UNIRLOS + "las dos categorías de 2005-2006 suman todas las muestras."),
    Relacion(("malaria_viviendas_rociadas", "malaria_viviendas_rociadas_por_personal_de_salud",
              "malaria_viviendas_rociadas_por_agente_comunario"),
             "Las viviendas rociadas contra la malaria se cuentan en total (2001-2003) y por quién rocía "
             "(2005-2006). " + _UNIRLOS + "las dos categorías suman todas las viviendas rociadas."),
]
