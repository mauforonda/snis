"""Series de vigilancia epidemiológica (formularios 302, 302a y 302b).

Una serie es lo que se cuenta con un mismo nombre a lo largo de las gestiones, por ejemplo
los casos de tos ferina. Cada regla asigna variables del tablero a una serie. Una regla se
aplica a un formulario, a grupos y a gestiones opcionales, y a un patrón sobre el nombre
normalizado de la variable (minúsculas, sin tildes, sin la numeración del formulario).

Campos de una regla:
- clasificacion: qué cuenta la serie (casos, defunciones, ...); es la carpeta del dataset.
- id, nombre, tema (agrupa series en el catálogo).
- fijo: atributos que la variable implica y la etiqueta no dice (sexo «mujer» en «SIDA
  Mujeres»). Sólo completan valores vacíos.
- permitido: población posible según la definición. Una fila fuera de ella es implausible:
  se publica y el readme la señala.
- nota: advertencia sobre lo que cuenta la serie, para el readme. Lo que cambia entre datasets
  no es una nota: es una relación (RELACIONES).

Un dataset publica una serie o una familia de series (FAMILIAS). CORTES divide una serie en las
gestiones en que cambia su definición. RELACIONES enlaza series que cuentan algo parecido. Las
tres listas están al final.
"""

from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass, field

from comun import Relacion

TODOS = None


@dataclass
class Regla:
    patron: str
    clasificacion: str
    id: str
    nombre: str
    tema: str
    formularios: tuple[str, ...] = ("302", "302a", "302b")
    grupos: tuple[str, ...] | None = TODOS
    gestiones: tuple[int, int] | None = None
    fijo: dict = field(default_factory=dict)
    permitido: dict = field(default_factory=dict)
    nota: str | None = None

    def aplica(self, formulario: str, grupo: str, gestion: int, nombre: str) -> bool:
        if formulario not in self.formularios:
            return False
        if self.grupos is not None and grupo not in self.grupos:
            return False
        if self.gestiones and not (self.gestiones[0] <= gestion <= self.gestiones[1]):
            return False
        return re.search(self.patron, nombre) is not None


def normalizar_nombre(texto: str) -> str:
    t = unicodedata.normalize("NFKD", texto)
    t = "".join(c for c in t if not unicodedata.combining(c)).lower()
    t = " ".join(t.split())
    # Numeración del formulario: «18.- », «1 », «01. », «1.15 », «11.1 », «51Embarazo».
    t = re.sub(r"^\d+(\.\d+)?\s*(\.-|-|\.)?\s*", "", t)
    return t.strip(" *")


MUJER = {"sexo": "mujer"}
HOMBRE = {"sexo": "hombre"}
SOLO_MUJER = {"sexo": ("mujer",)}
SOLO_HOMBRE = {"sexo": ("hombre",)}
MENOR_5 = {"edad_hasta_max": 5}
MATERNA = {"sexo": ("mujer",), "edad_desde_min": 10, "edad_hasta_max": 60}

C, D, N, F, E, R = "casos", "defunciones", "estado_nutricional", "factores_riesgo", "emergencias", "desarrollo_infantil"

# 302, 2001-2003: enfermedades que se registran también en otra sección del formulario (ver REGLAS).
# (patrón, id, nombre, tema, series de la sección «Sospecha diagnóstica» que cuentan lo mismo)
SECCIONES = [
    ("tosferina", "tos_ferina_seccion_inmunoprevenibles", "Tos ferina (sección inmunoprevenibles, 2001-2003)", "inmunoprevenible", ("tos_ferina",)),
    ("difteria", "difteria_seccion_inmunoprevenibles", "Difteria (sección inmunoprevenibles, 2001-2003)", "inmunoprevenible", ("difteria",)),
    ("fiebre amarilla", "fiebre_amarilla_seccion_inmunoprevenibles", "Fiebre amarilla (sección inmunoprevenibles, 2001-2003)", "inmunoprevenible", ("fiebre_amarilla",)),
    ("rabia humana", "rabia_humana_seccion_inmunoprevenibles", "Rabia humana (sección inmunoprevenibles, 2001-2003)", "zoonosis", ("rabia_humana_canina",)),
    ("fiebre hemorragica", "fiebre_hemorragica_seccion_otras_infecciones", "Fiebre hemorrágica (sección otras infecciones, 2001-2003)", "zoonosis", ("fiebre_hemorragica",)),
    ("enfermedad respiratoria hanta", "hantavirus_seccion_otras_infecciones", "Hantavirus (sección otras infecciones, 2001-2003)", "zoonosis", ("hantavirus",)),
    ("tifus exantematico", "tifus_exantematico_seccion_otras_infecciones", "Tifus exantemático (sección otras infecciones, 2001-2003)", "otra transmisible", ("tifus_exantematico",)),
    ("meningitis", "meningitis_seccion_otras_infecciones", "Meningitis (sección otras infecciones, 2001-2003)", "otra transmisible",
     ("meningitis_meningococica", "meningitis_haemophilus", "meningitis_tuberculosa")),
]

REGLAS: list[Regla] = [
    # --- Grupos de enfermedades por sistema (302, 2001-2003) -------------------------------
    *[Regla(rf"^{p}", C, i, n, "grupo de enfermedades", ("302",), ("00",), nota=(
        "Clasificación general por sistema del formulario 2001-2003; puede incluir casos que "
        "también se notifican como enfermedades específicas."))
      for p, i, n in [
          ("enfermedades del sistema nervioso", "grupo_sistema_nervioso", "Enfermedades del sistema nervioso"),
          ("enfermedades del ojo", "grupo_ojo", "Enfermedades del ojo y sus anexos"),
          ("enfermedades del oido", "grupo_oido", "Enfermedades del oído y de la apófisis mastoides"),
          ("enfermedades del sistema cardio", "grupo_circulatorio", "Enfermedades del sistema circulatorio"),
          ("enfermedades del sistema respiratorio", "grupo_respiratorio", "Enfermedades del sistema respiratorio"),
          ("enfermedades del sistema digestivo", "grupo_digestivo", "Enfermedades del sistema digestivo"),
          ("enfermedades del sistema genitourinario", "grupo_genitourinario", "Enfermedades del sistema genitourinario"),
          ("enfermedades de piel", "grupo_piel", "Enfermedades de la piel y del tejido subcutáneo"),
          ("enfermedades endocrinas", "grupo_endocrino", "Enfermedades endocrinas, nutricionales y metabólicas"),
          ("enfermedades sistema osteomuscular", "grupo_osteomuscular", "Enfermedades del sistema osteomuscular y del tejido conjuntivo"),
          ("enfermedades de la sangre", "grupo_sangre", "Enfermedades de la sangre y trastornos inmunitarios"),
          ("enfermedades tumorales", "grupo_tumores", "Tumores"),
          ("complicaciones embarazo", "grupo_embarazo", "Complicaciones del embarazo, parto y puerperio"),
          ("malformaciones congenitas", "grupo_malformaciones", "Malformaciones congénitas"),
          ("traumatismos y envenenamiento", "grupo_traumatismos", "Traumatismos y envenenamientos"),
          ("transtornos mentales", "grupo_mentales", "Trastornos mentales y del comportamiento"),
          ("otras causas", "grupo_otras_causas", "Otras causas"),
      ]],

    # --- 302, 2001-2003: la misma enfermedad en dos secciones del formulario ------------------
    # Las secciones «Inmunoprevenibles» (grupo 04) y «Otras infecciones» (grupo 06) repiten
    # enfermedades de la sección «Sospecha diagnóstica» (grupos 01 y 02). El número con
    # asterisco, como «Tosferina (3*)», remite al ítem de sospecha. Las cifras de las dos
    # secciones son distintas y ninguna contiene a la otra; no sabemos qué cuenta cada una.
    *[Regla(rf"^{p}.*\(\d", C, i, n, cat, ("302",), ("04", "06"), (2001, 2003)) for p, i, n, cat, _ in SECCIONES],


    # --- Inmunoprevenibles -------------------------------------------------------------------
    Regla(r"^sarampion$", C, "sarampion", "Sarampión", "inmunoprevenible", gestiones=(2001, 2003)),
    Regla(r"^rubeola$", C, "rubeola", "Rubéola", "inmunoprevenible"),
    Regla(r"^sarampion ?/ ?rubeola", C, "sarampion_rubeola", "Sarampión o rubéola", "inmunoprevenible"),
    Regla(r"^sindrome de rubeola congenita", C, "rubeola_congenita", "Síndrome de rubéola congénita", "inmunoprevenible",
          permitido={"edad_hasta_max": 1}),
    Regla(r"^tos ?ferina", C, "tos_ferina", "Tos ferina", "inmunoprevenible"),
    Regla(r"^difteria$", C, "difteria", "Difteria", "inmunoprevenible"),
    Regla(r"^paralisis flacida", C, "paralisis_flacida_aguda", "Parálisis flácida aguda", "inmunoprevenible"),
    Regla(r"^poliomielitis", C, "poliomielitis", "Poliomielitis", "inmunoprevenible"),
    Regla(r"^tetanos neonatal ?/ ?adulto", C, "tetanos", "Tétanos (neonatal y del adulto)", "inmunoprevenible"),
    Regla(r"^tetanos neonatal$", C, "tetanos_neonatal", "Tétanos neonatal", "inmunoprevenible"),
    Regla(r"^tetanos( del adulto| de adulto)?$", C, "tetanos_adulto", "Tétanos del adulto", "inmunoprevenible"),
    Regla(r"^hepatitis( viral)?$", C, "hepatitis_viral", "Hepatitis viral", "inmunoprevenible"),
    Regla(r"^hepatitis viral a\b", C, "hepatitis_a", "Hepatitis A", "inmunoprevenible"),
    Regla(r"^hepatitis viral b o c", C, "hepatitis_b_c", "Hepatitis B o C", "inmunoprevenible"),
    Regla(r"^hepatitis viral b\b", C, "hepatitis_b", "Hepatitis B", "inmunoprevenible"),
    Regla(r"^hepatitis viral c\b", C, "hepatitis_c", "Hepatitis C", "inmunoprevenible"),
    Regla(r"^otras hepatitis virales", C, "hepatitis_otras", "Otras hepatitis virales", "inmunoprevenible"),
    Regla(r"^parotiditis", C, "parotiditis", "Parotiditis", "inmunoprevenible"),
    Regla(r"^varicela", C, "varicela", "Varicela", "inmunoprevenible"),
    Regla(r"^eruptivas", C, "eruptivas", "Enfermedades eruptivas", "inmunoprevenible"),
    Regla(r"^esavi", C, "esavi", "Eventos supuestamente atribuidos a la vacunación (ESAVI)", "inmunoprevenible"),

    # --- Transmitidas por vectores --------------------------------------------------------------
    Regla(r"^fiebre amarilla$", C, "fiebre_amarilla", "Fiebre amarilla", "vectorial"),
    Regla(r"^dengue hemorragico", C, "dengue_hemorragico", "Dengue hemorrágico", "vectorial"),
    Regla(r"^dengue clasico", C, "dengue_clasico", "Dengue clásico", "vectorial"),
    Regla(r"^dengue grave", C, "dengue_grave", "Dengue grave", "vectorial"),
    Regla(r"^dengue con signos de alarma", C, "dengue_con_signos", "Dengue con signos de alarma", "vectorial"),
    Regla(r"^dengue sin signos de alarma", C, "dengue_sin_signos", "Dengue sin signos de alarma", "vectorial"),
    Regla(r"^dengue$", C, "dengue_seccion_metaxenicas", "Dengue (sección enfermedades metaxénicas)", "vectorial"),
    Regla(r"^chikungunya", C, "chikungunya", "Chikungunya", "vectorial"),
    Regla(r"^zika", C, "zika", "Zika", "vectorial"),
    Regla(r"^oropouche", C, "oropouche", "Oropouche", "vectorial"),
    Regla(r"^malaria sospechosos", C, "malaria_sospecha", "Malaria (sospecha)", "vectorial"),
    Regla(r"^malaria( confirmados)?$", C, "malaria", "Malaria", "vectorial", grupos=("06", "14", "17")),
    Regla(r"^leishmaniasis sospechosos", C, "leishmaniasis_sospecha", "Leishmaniasis (sospecha)", "vectorial"),
    Regla(r"^leishmaniasis( confirmados)?$", C, "leishmaniasis", "Leishmaniasis", "vectorial"),
    Regla(r"^leishmaniasis cutanea", C, "leishmaniasis_cutanea", "Leishmaniasis cutánea", "vectorial"),
    Regla(r"^leishmaniasis mucocutanea", C, "leishmaniasis_mucocutanea", "Leishmaniasis mucocutánea", "vectorial"),
    Regla(r"^leishmaniasis visceral", C, "leishmaniasis_visceral", "Leishmaniasis visceral", "vectorial"),
    Regla(r"^(enfermedades de )?chagas agud[oa]$", C, "chagas_agudo", "Chagas agudo", "vectorial"),
    Regla(r"^chagas agudo congenito", C, "chagas_agudo_congenito", "Chagas agudo congénito", "vectorial"),
    Regla(r"^chagas agudo por otros", C, "chagas_agudo_otros", "Chagas agudo por otros mecanismos de transmisión", "vectorial"),

    # --- Zoonosis y lesiones por animales ---------------------------------------------------------
    Regla(r"^fiebre hemorrag", C, "fiebre_hemorragica", "Fiebre hemorrágica", "zoonosis",
          nota="2004-2019 el nombre es «fiebre hemorrágica boliviana»."),
    Regla(r"hanta", C, "hantavirus", "Enfermedad por hantavirus", "zoonosis"),
    Regla(r"^peste", C, "peste", "Peste", "zoonosis"),
    Regla(r"^leptospirosis", C, "leptospirosis", "Leptospirosis", "zoonosis"),
    Regla(r"^rabia \(humana/canina\)", C, "rabia_humana_canina", "Rabia (humana o canina)", "zoonosis"),
    Regla(r"^rabia humana", C, "rabia_humana", "Rabia humana", "zoonosis"),
    Regla(r"^rabia (canina|en perros|en canes)", C, "rabia_canina", "Rabia canina (casos en perros)", "animal",
          nota="Cuenta perros, no personas. El formulario usa para los perros la misma plantilla de sexo y bandas de edad que para las personas; las bandas de 20 años o más no son posibles en perros."),
    Regla(r"(mordidas por (can|animal)|expuestas al virus rabico)", C, "exposicion_rabica",
          "Personas expuestas al virus rábico (mordeduras)", "lesiones por animales"),
    Regla(r"serpiente", C, "mordedura_serpiente", "Mordedura o envenenamiento por serpiente", "lesiones por animales"),
    Regla(r"(ponzonosos|aracnidos)", C, "envenenamiento_aracnidos", "Envenenamiento por arácnidos y otros animales ponzoñosos",
          "lesiones por animales"),
    Regla(r"^tifus exantematico$", C, "tifus_exantematico", "Tifus exantemático", "otra transmisible"),
    Regla(r"^colera", C, "colera", "Cólera", "diarreica"),

    # --- Meningitis y otras transmisibles ---------------------------------------------------------
    Regla(r"^(meningitis meningococ|menin\. meningococ)", C, "meningitis_meningococica", "Meningitis meningocócica", "otra transmisible"),
    Regla(r"^enfermedad meningococica", C, "enfermedad_meningococica", "Enfermedad meningocócica", "otra transmisible"),
    Regla(r"^meningitis por hemophilus", C, "meningitis_haemophilus", "Meningitis por Haemophilus influenzae", "otra transmisible"),
    Regla(r"^otras meningitis", C, "meningitis_otras", "Otras meningitis", "otra transmisible"),
    Regla(r"^influenza aviar|^influenza ?/ ?pandemica", C, "influenza_pandemica", "Influenza pandémica", "respiratoria"),
    Regla(r"^influenza \(irag", C, "influenza_irag_eti", "Influenza (IRAG, IRAGI y ETI)", "respiratoria"),
    Regla(r"^covid-19", C, "covid19", "COVID-19", "respiratoria"),
    Regla(r"^sindrome inflamatorio multisistemico", C, "sim_covid19", "Síndrome inflamatorio multisistémico asociado a COVID-19", "respiratoria"),
    Regla(r"^(viruela simica|mpox)", C, "mpox", "Mpox (viruela símica)", "otra transmisible"),
    Regla(r"^anomalia congenita", C, "anomalia_congenita_zika", "Anomalía congénita (vigilancia de zika)", "vectorial"),
    Regla(r"^microcefalia", C, "microcefalia_zika", "Microcefalia (vigilancia de zika)", "vectorial"),
    Regla(r"^(trastorno neurologico|trastorno nuerologico)", C, "trastorno_neurologico_zika", "Trastorno neurológico (vigilancia de zika)", "vectorial"),
    Regla(r"^sind\. guillain barre", C, "guillain_barre_zika", "Síndrome de Guillain-Barré (vigilancia de zika)", "vectorial"),
    Regla(r"^sindrome hemolitico uremico", C, "sindrome_hemolitico_uremico", "Síndrome hemolítico urémico", "otra transmisible"),

    # --- Respiratorias y diarreicas ---------------------------------------------------------------
    Regla(r"^(diarrea|enfermedad diarreica aguda)$", C, "eda", "Enfermedad diarreica aguda", "diarreica"),
    Regla(r"^ira sin neumonia", C, "ira_sin_neumonia", "Infección respiratoria aguda sin neumonía", "respiratoria"),
    Regla(r"^neumonia$", C, "neumonia", "Neumonía", "respiratoria"),
    Regla(r"^sintomatico respiratorio", C, "sintomatico_respiratorio", "Sintomáticos respiratorios", "tuberculosis y lepra"),

    # --- Tuberculosis y lepra --------------------------------------------------------------------
    Regla(r"^meningitis (tuberculosa|tb) en menores de 5", C, "meningitis_tb_menor_5", "Meningitis tuberculosa en menores de 5 años",
          "tuberculosis y lepra", permitido=MENOR_5),
    Regla(r"^meningitis tuberculosa$", C, "meningitis_tuberculosa", "Meningitis tuberculosa", "tuberculosis y lepra"),
    Regla(r"^tuberculosis meningea", C, "tuberculosis_meningea", "Tuberculosis meníngea", "tuberculosis y lepra"),
    Regla(r"^tuberculosis pulmonar baar (\(\+\)|\+) nuevos", C, "tb_pulmonar_baar_positivo", "Tuberculosis pulmonar BAAR positivo, casos nuevos", "tuberculosis y lepra"),
    Regla(r"^tuberculosis pulmonar baar (\(-\)|-)", C, "tb_pulmonar_baar_negativo", "Tuberculosis pulmonar BAAR negativo, casos nuevos", "tuberculosis y lepra"),
    Regla(r"^tuberculosis extrapulmonar", C, "tb_extrapulmonar", "Tuberculosis extrapulmonar", "tuberculosis y lepra"),
    Regla(r"^tuberculosis pulmonar baar \(\+\) prevamente", C, "tb_previamente_tratados", "Tuberculosis pulmonar BAAR positivo, previamente tratados", "tuberculosis y lepra"),
    Regla(r"^enfermos curados", C, "tb_curados", "Tuberculosis: enfermos curados", "tuberculosis y lepra"),
    Regla(r"^fracaso terapeutico", C, "tb_fracaso", "Tuberculosis: fracaso terapéutico", "tuberculosis y lepra"),
    Regla(r"(graves\)?$|rafa \(graves)", C, "rafa_grave", "Reacciones adversas graves a fármacos antituberculosos", "tuberculosis y lepra",
          grupos=("07",)),
    Regla(r"^(rafa (reacciones adversas )?\(leves|reaccion adversa a farmacos antituberculosos \(rafa\)$)", C, "rafa_leve",
          "Reacciones adversas leves o moderadas a fármacos antituberculosos", "tuberculosis y lepra", grupos=("07",),
          nota="En 2015-2023 la variable se llama «RAFA», sin calificar; se publica como leve o moderada porque el "
               "formulario notifica las graves aparte."),
    Regla(r"^lepra paucibacilar", C, "lepra_paucibacilar", "Lepra paucibacilar", "tuberculosis y lepra"),
    Regla(r"^lepra multibacilar", C, "lepra_multibacilar", "Lepra multibacilar", "tuberculosis y lepra"),
    Regla(r"^(lepra|enfermedad de hansen)$", C, "lepra", "Lepra", "tuberculosis y lepra"),

    # --- Transmisión sexual -----------------------------------------------------------------------
    Regla(r"^sida mujeres", C, "sida", "SIDA", "transmisión sexual", fijo=MUJER),
    Regla(r"^sida hombres", C, "sida", "SIDA", "transmisión sexual", fijo=HOMBRE),
    Regla(r"^sida o vih", C, "vih_sida", "VIH o SIDA", "transmisión sexual"),
    Regla(r"^sida$", C, "sida", "SIDA", "transmisión sexual"),
    Regla(r"^sifilis$", C, "sifilis", "Sífilis", "transmisión sexual"),
    Regla(r"^sifilis congenita( - nacido vivo)?$", C, "sifilis_congenita", "Sífilis congénita", "transmisión sexual"),
    Regla(r"^sifilis congenita - mortinato", C, "sifilis_congenita_mortinato", "Sífilis congénita en mortinatos", "transmisión sexual"),
    Regla(r"^sifilis en la mujer embarazada", C, "sifilis_embarazada", "Sífilis en la mujer embarazada", "transmisión sexual",
          fijo=MUJER, permitido=MATERNA),
    Regla(r"^(vih mujer embarazada|prueba rapida reactiva de vih en mujer embarazada)", C, "vih_embarazada",
          "VIH reactivo en la mujer embarazada", "transmisión sexual", fijo=MUJER, permitido=MATERNA),
    Regla(r"^(vih poblacion en general|prueba rapida reactiva de vih en poblacion)", C, "vih_poblacion_general",
          "VIH reactivo en la población general", "transmisión sexual"),
    Regla(r"^(its )?mujer con ulcera genital", C, "ulcera_genital", "Úlcera genital", "transmisión sexual", fijo=MUJER),
    Regla(r"^(its )?hombre con ulcera genital", C, "ulcera_genital", "Úlcera genital", "transmisión sexual", fijo=HOMBRE),
    Regla(r"^ulcera genital", C, "ulcera_genital", "Úlcera genital", "transmisión sexual"),
    Regla(r"^(its home|hombre) con flujo uretral", C, "flujo_uretral_vaginal", "Flujo uretral o vaginal", "transmisión sexual", fijo=HOMBRE),
    Regla(r"^flujo uretral", C, "flujo_uretral_vaginal", "Flujo uretral o vaginal", "transmisión sexual"),
    Regla(r"^gonorrea", C, "gonorrea", "Gonorrea", "transmisión sexual"),
    Regla(r"^verruga genital", C, "verruga_genital", "Verruga genital", "transmisión sexual"),
    Regla(r"^dolor abdominal/ edema de escroto", C, "dolor_abdominal_edema_escroto", "Dolor abdominal o edema de escroto", "transmisión sexual"),

    # --- Violencia, hechos de tránsito y accidentes -------------------------------------------------
    Regla(r"^violencia contra el hombre$|^hombres$", C, "violencia_intrafamiliar", "Violencia intrafamiliar", "violencia",
          ("302",), ("08",), fijo=HOMBRE),
    Regla(r"^violencia contra la mujer$|^mujeres$", C, "violencia_intrafamiliar", "Violencia intrafamiliar", "violencia",
          ("302",), ("08",), fijo=MUJER),
    Regla(r"^violencia contra el nino$", C, "violencia_intrafamiliar_ninez", "Violencia intrafamiliar contra niñas y niños", "violencia",
          ("302",), ("08",), fijo=HOMBRE),
    Regla(r"^violencia contra la nina$", C, "violencia_intrafamiliar_ninez", "Violencia intrafamiliar contra niñas y niños", "violencia",
          ("302",), ("08",), fijo=MUJER),
    Regla(r"^(intrafamiliar|violencia en la familia)", C, "violencia_intrafamiliar", "Violencia intrafamiliar", "violencia"),
    Regla(r"^violencia fisica familiar", C, "violencia_fisica_familiar", "Violencia física familiar", "violencia"),
    Regla(r"^violencia sexual familiar", C, "violencia_sexual_familiar", "Violencia sexual familiar", "violencia"),
    Regla(r"^violencia sexual \(familiar", C, "violencia_sexual", "Violencia sexual (familiar y en otros ámbitos)", "violencia"),
    Regla(r"^violencia fisica en otros contextos", C, "violencia_fisica_otros", "Violencia física en otros contextos", "violencia"),
    Regla(r"^violencia sexual en otros contextos", C, "violencia_sexual_otros", "Violencia sexual en otros contextos", "violencia"),
    Regla(r"^violencia por negligencia", C, "violencia_negligencia", "Violencia por negligencia o abandono", "violencia"),
    Regla(r"^violencia en la mujer embarazada", C, "violencia_embarazada", "Violencia en la mujer embarazada", "violencia",
          fijo=MUJER, permitido=MATERNA),
    Regla(r"^violencia en la persona con discapacidad", C, "violencia_discapacidad", "Violencia en la persona con discapacidad", "violencia"),
    Regla(r"^otras violencias por lesiones autoinflingidas y colectivas", C, "violencia_autoinfligida_colectiva",
          "Lesiones autoinfligidas y violencia colectiva", "violencia"),
    Regla(r"^otras violencias por lesiones autoinflingidas$", C, "lesiones_autoinfligidas", "Lesiones autoinfligidas", "violencia"),
    Regla(r"^otras violencias por lesiones colectivas", C, "violencia_colectiva", "Violencia colectiva", "violencia"),
    Regla(r"^otras violencias", C, "otras_violencias", "Otras violencias (causas externas)", "violencia"),
    Regla(r"hechos de transito", C, "hechos_transito", "Hechos de tránsito", "accidentes"),
    Regla(r"^(accidentes|n. de casos presentados por otros accidentes)$", C, "otros_accidentes", "Otros accidentes", "accidentes"),
    Regla(r"accidentes laborales", C, "accidentes_laborales", "Accidentes laborales", "accidentes"),

    # --- Intoxicaciones ---------------------------------------------------------------------------
    Regla(r"^plaguicidas", C, "plaguicidas", "Intoxicación por plaguicidas", "intoxicación"),
    Regla(r"^(organofosforados|organosfosforados)", C, "organofosforados", "Intoxicación por organofosforados y carbamatos", "intoxicación"),
    Regla(r"^halogenados", C, "halogenados", "Intoxicación por halogenados", "intoxicación"),
    Regla(r"^herbicida", C, "herbicidas", "Intoxicación por herbicidas y fungicidas", "intoxicación"),
    Regla(r"^otros plaguicidas", C, "otros_plaguicidas", "Intoxicación por otros plaguicidas e insecticidas", "intoxicación"),
    Regla(r"^alimentos \(brotes\)", C, "intoxicacion_alimentos_brotes", "Intoxicación por alimentos (brotes)", "intoxicación"),
    Regla(r"^enf\. transmitidas por alimentos", C, "eta", "Enfermedades transmitidas por alimentos", "intoxicación"),
    Regla(r"^alcohol$", C, "intoxicacion_alcohol", "Intoxicación por alcohol", "intoxicación"),
    Regla(r"^drogas$", C, "intoxicacion_drogas", "Intoxicación por drogas", "intoxicación"),
    Regla(r"^otras intoxicaciones", C, "otras_intoxicaciones", "Otras intoxicaciones (drogas, fármacos, alcohol)", "intoxicación"),

    # --- Salud materna (casos) ---------------------------------------------------------------------
    Regla(r"^aborto$", C, "aborto", "Aborto", "salud materna", fijo=MUJER, permitido=MATERNA),
    Regla(r"^hemorragia de la primera mitad.*(acabaron|termino) en aborto", C, "hemorragia_primera_mitad_aborto",
          "Hemorragia de la primera mitad del embarazo que terminó en aborto", "salud materna", fijo=MUJER, permitido=MATERNA),
    Regla(r"^hemorragia de la primera mitad", C, "hemorragia_primera_mitad", "Hemorragia de la primera mitad del embarazo",
          "salud materna", fijo=MUJER, permitido=MATERNA),
    Regla(r"^hemorragia del parto", C, "hemorragia_parto_puerperio", "Hemorragia del parto o puerperio", "salud materna",
          fijo=MUJER, permitido=MATERNA),
    Regla(r"^embarazo en adol", C, "embarazo_adolescente", "Embarazo en adolescentes (menores de 20 años)", "salud materna",
          fijo=MUJER, permitido={"sexo": ("mujer",), "edad_hasta_max": 20}),
    Regla(r"^parto de adolecente", C, "parto_adolescente", "Parto en adolescentes (menores de 20 años)", "salud materna", fijo=MUJER),
    Regla(r"^parto de mujer anosa", C, "parto_mayor_35", "Parto en mujeres mayores de 35 años", "salud materna", fijo=MUJER),
    Regla(r"^parturienta con hijo anterior vivo", C, "parturienta_hijo_vivo", "Parturienta con hijo anterior vivo", "salud materna", fijo=MUJER),
    Regla(r"^parturienta con hijo anterior muerto", C, "parturienta_hijo_muerto", "Parturienta con hijo anterior muerto", "salud materna", fijo=MUJER),
    Regla(r"^preeclampsia severa/eclampsia", C, "preeclampsia_eclampsia", "Preeclampsia severa o eclampsia", "salud materna",
          fijo=MUJER, permitido=MATERNA),
    Regla(r"^preeclampsia severa$", C, "preeclampsia_severa", "Preeclampsia severa", "salud materna", fijo=MUJER, permitido=MATERNA),
    Regla(r"^eclampsia", C, "eclampsia", "Eclampsia", "salud materna", fijo=MUJER, permitido=MATERNA),
    Regla(r"(sepsis obstetrica|gestantes y puerperas con sepsis)", C, "sepsis_obstetrica", "Sepsis obstétrica", "salud materna",
          fijo=MUJER, permitido=MATERNA),

    # --- Tamizaje metabólico neonatal (302a, 2024-2025) ---------------------------------------------
    Regla(r"^hipotiroidismo$", C, "hipotiroidismo_tamizaje", "Hipotiroidismo (tamizaje neonatal)", "metabólica congénita", ("302a",)),
    Regla(r"^hiperplasia suprarrenal", C, "hiperplasia_suprarrenal", "Hiperplasia suprarrenal congénita", "metabólica congénita"),
    Regla(r"^fibrosis quistica", C, "fibrosis_quistica", "Fibrosis quística", "metabólica congénita"),
    Regla(r"^fenilcetonuria", C, "fenilcetonuria", "Fenilcetonuria", "metabólica congénita"),

    # --- Enfermedades no transmisibles (302b) --------------------------------------------------------
    *[Regla(p, C, i, n, cat, ("302b",), ("02", "03", "04", "08", "09"), permitido=perm, nota=nota)
      for p, i, n, cat, perm, nota in [
          (r"^diabetes tipo 1", "diabetes_tipo_1", "Diabetes tipo 1", "enfermedad no transmisible", {}, None),
          (r"^diabetes tipo 2", "diabetes_tipo_2", "Diabetes tipo 2", "enfermedad no transmisible", {}, None),
          (r"^diabetes gestacional", "diabetes_gestacional", "Diabetes gestacional", "enfermedad no transmisible", MATERNA,
           "Una sola fila tiene 810 casos en mujeres de 60 años y más (Santa Rosa, septiembre de 2015): es un tercio "
           "de esa categoría. El código de la variable es O24.9 (diabetes en el embarazo, no especificada); "
           "también hay muchos casos en mujeres de 50 a 59 años."),
          (r"^obesidad", "obesidad", "Obesidad", "enfermedad no transmisible", {}, None),
          (r"^artritis", "artritis_reumatoide", "Artritis reumatoide", "enfermedad no transmisible", {}, None),
          (r"^hipertension arterial", "hipertension_arterial", "Hipertensión arterial", "enfermedad no transmisible", {}, None),
          (r"^infarto agudo", "infarto_agudo_miocardio", "Infarto agudo de miocardio", "enfermedad no transmisible", {}, None),
          (r"^insuficiencia cardiaca", "insuficiencia_cardiaca", "Insuficiencia cardiaca", "enfermedad no transmisible", {}, None),
          (r"^asma", "asma", "Asma", "enfermedad no transmisible", {}, None),
          (r"^enfermedad pulmonar obstructiva", "epoc", "Enfermedad pulmonar obstructiva crónica (EPOC)", "enfermedad no transmisible", {}, None),
          (r"^hipotiriodismo congenito", "hipotiroidismo_congenito", "Hipotiroidismo congénito", "enfermedad no transmisible", {}, None),
          (r"^dislipidemia", "dislipidemia", "Dislipidemia", "enfermedad no transmisible", {}, None),
          (r"^accidente cr?ebro ?vascular", "accidente_cerebrovascular", "Accidente cerebrovascular", "enfermedad no transmisible", {}, None),
          (r"^enfermedad renal$", "enfermedad_renal", "Enfermedad renal", "enfermedad no transmisible", {},
           "Cuenta todas las enfermedades renales (CIE-10 N00 a N29), no sólo la enfermedad renal crónica. "
           "Los estadios 3, 4 y 5 tienen su propio dataset; no sabemos si sus casos están también aquí."),
          (r"^enfermedad renal estadio 3", "enfermedad_renal_estadio_3", "Enfermedad renal, estadio 3", "enfermedad no transmisible", {},
           None),
          (r"^enfermedad renal grado 3a", "enfermedad_renal_estadio_3a", "Enfermedad renal, estadio 3a", "enfermedad no transmisible", {}, None),
          (r"^enfermedad renal grado 3b", "enfermedad_renal_estadio_3b", "Enfermedad renal, estadio 3b", "enfermedad no transmisible", {}, None),
          (r"^enfermedad renal (estadio|grado) 4", "enfermedad_renal_estadio_4", "Enfermedad renal, estadio 4", "enfermedad no transmisible", {}, None),
          (r"^enfermedad renal (estadio|grado) 5", "enfermedad_renal_estadio_5", "Enfermedad renal, estadio 5", "enfermedad no transmisible", {}, None),
          (r"^cancer (de )?cervico uterino", "cancer_cuello_uterino", "Cáncer de cuello uterino", "cáncer", SOLO_MUJER, None),
          (r"^cancer de mama", "cancer_mama", "Cáncer de mama", "cáncer", {}, None),
          (r"^cancer de prostata", "cancer_prostata", "Cáncer de próstata", "cáncer", SOLO_HOMBRE, None),
          (r"^cancer de tiroides", "cancer_tiroides", "Cáncer de tiroides", "cáncer", {}, None),
          (r"^cancer pulmonar", "cancer_pulmon", "Cáncer de pulmón", "cáncer", {}, None),
          (r"^cancer de estomago", "cancer_estomago", "Cáncer de estómago", "cáncer", {}, None),
          (r"^cancer de colon", "cancer_colon_recto", "Cáncer de colon y recto", "cáncer", {}, None),
          (r"^cancer de piel", "cancer_piel", "Cáncer de piel", "cáncer", {}, None),
          (r"^leucemias", "leucemias", "Leucemias", "cáncer", {}, None),
          (r"^linfomas", "linfomas", "Linfomas", "cáncer", {}, None),
          (r"^cancer en sus distintas formas", "cancer_otros", "Cáncer de otras localizaciones", "cáncer", {},
           "Excluye las localizaciones que el formulario notifica aparte."),
          (r"^episodios depresivos", "depresion", "Episodios depresivos", "salud mental", {}, None),
          (r"^episodios de ansiedad", "ansiedad", "Episodios de ansiedad", "salud mental", {}, None),
          (r"^episodios psicoticos", "psicosis_esquizofrenia", "Episodios psicóticos o esquizofrenia", "salud mental", {}, None),
          (r"^epilepsia", "epilepsia", "Epilepsia", "neurológica", {}, None),
          (r"^transtornos de comportamiento por consumo", "trastornos_consumo_sustancias", "Trastornos del comportamiento por consumo de sustancias",
           "salud mental", {}, None),
          (r"^transtornos alimenticios", "trastornos_alimentarios", "Trastornos alimentarios (anorexia, bulimia)", "salud mental", {}, None),
          (r"^transtornos de conducta", "trastornos_conducta", "Trastornos de conducta", "salud mental", {}, None),
          (r"^trastorno de bipolaridad", "trastorno_bipolar", "Trastorno bipolar", "salud mental", {}, None),
          (r"^autismo", "autismo", "Autismo", "salud mental", {}, None),
          (r"^trastornos mental asociado al embarazo", "trastorno_mental_perinatal", "Trastornos mentales del embarazo, parto y puerperio",
           "salud mental", MATERNA,
           "SOAPS cuenta esta variable cuando uno de los campos de diagnóstico tiene un código F53 (trastornos "
           "del puerperio), sin filtro de sexo. Los hombres de este dataset son pacientes registrados como "
           "hombres con ese código: pueden ser errores de sexo o de código. El instructivo de 2024 define el "
           "trastorno sólo en la madre."),
          (r"^alzheimer", "alzheimer", "Alzheimer", "neurológica", {}, None),
          (r"^parkinson", "parkinson", "Parkinson", "neurológica", {}, None),
          (r"^otras demencias", "demencias_otras", "Otras demencias", "neurológica", {}, None),
      ] if i],

    # --- Defunciones ------------------------------------------------------------------------------
    Regla(r"^muerte materna( notificada)?$|^sospecha de muerte materna", D, "muerte_materna", "Muerte materna", "salud materna",
          fijo=MUJER, permitido=MATERNA,
          nota="Desde 2015 cuenta las muertes maternas notificadas; las confirmadas son otro dataset."),
    Regla(r"^muerte materna confirmada", D, "muerte_materna_confirmada", "Muerte materna confirmada", "salud materna",
          fijo=MUJER, permitido=MATERNA),
    Regla(r"^muerte de mujer 10-59", D, "muerte_mujer_edad_fertil", "Muerte de mujer de 10 a 59 años", "salud materna",
          fijo=MUJER, permitido=MATERNA),
    Regla(r"^muerte rn menor de 7 dias", D, "muerte_neonatal_temprana", "Muerte neonatal temprana (menos de 7 días)", "perinatal e infantil",
          permitido={"edad_hasta_max": 1}),
    Regla(r"^muerte neonatal temprana", D, "muerte_neonatal_temprana_confirmada", "Muerte neonatal temprana confirmada (0 a 6 días)",
          "perinatal e infantil", permitido={"edad_hasta_max": 1}),
    Regla(r"^muerte neonatal tardia", D, "muerte_neonatal_tardia", "Muerte neonatal tardía confirmada (7 a 27 días)", "perinatal e infantil",
          permitido={"edad_hasta_max": 1}),
    Regla(r"^muerte fetal", D, "muerte_fetal", "Muerte fetal (óbito) confirmada", "perinatal e infantil"),
    Regla(r"^muerte menor de 28 dias por sepsis", D, "muerte_neonatal_sepsis", "Muerte en menores de 28 días por sepsis", "perinatal e infantil",
          permitido={"edad_hasta_max": 1}),
    Regla(r"^muerte menor de 28 dias por asfixia", D, "muerte_neonatal_asfixia", "Muerte en menores de 28 días por asfixia perinatal",
          "perinatal e infantil", permitido={"edad_hasta_max": 1}),
    Regla(r"^muerte menos de 28 dias por prematurez", D, "muerte_neonatal_prematurez", "Muerte en menores de 28 días por prematurez extrema",
          "perinatal e infantil", permitido={"edad_hasta_max": 1}),
    Regla(r"^muerte de 28 dias a menor de 1 ano", D, "muerte_posneonatal", "Muerte de 28 días a menos de 1 año", "perinatal e infantil",
          permitido={"edad_hasta_max": 1}),
    Regla(r"^muerte menor de 1 ano$", D, "muerte_menor_1", "Muerte en menores de 1 año", "perinatal e infantil",
          permitido={"edad_hasta_max": 1}),
    Regla(r"^muerte menor de 5 anos por diarrea", D, "muerte_menor_5_diarrea", "Muerte en menores de 5 años por diarrea", "perinatal e infantil",
          permitido=MENOR_5),
    Regla(r"^muerte menor de 5 anos por neumonia", D, "muerte_menor_5_neumonia", "Muerte en menores de 5 años por neumonía", "perinatal e infantil",
          permitido=MENOR_5),
    Regla(r"^muerte menor de 5 anos por desnutricion", D, "muerte_menor_5_desnutricion", "Muerte en menores de 5 años por desnutrición aguda grave",
          "perinatal e infantil", permitido=MENOR_5),
    Regla(r"^muerte menor de 5 anos por otras causas", D, "muerte_menor_5_otras", "Muerte en menores de 5 años por otras causas",
          "perinatal e infantil", permitido=MENOR_5),
    Regla(r"^otras muertes en (personas )?mayores de 5", D, "muerte_mayor_5_otras", "Otras muertes en mayores de 5 años", "otras causas",
          permitido={"edad_desde_min": 5}),
    Regla(r"^muerte por malaria", D, "muerte_malaria", "Muerte por malaria (P. falciparum)", "vectorial"),
    Regla(r"^muerte por otras causas", D, "muerte_otras_causas", "Muertes por otras causas", "otras causas"),
    Regla(r"^sospecha de muerte por dengue", D, "muerte_dengue_sospecha", "Sospecha de muerte por dengue", "vectorial"),
    Regla(r"^sospecha de muerte por covid", D, "muerte_covid19_sospecha", "Sospecha de muerte por COVID-19", "respiratoria"),
    *[Regla(p, D, i, n, cat, ("302b",), ("05",), permitido=perm, nota=nota[0] if nota else None)
      for p, i, n, cat, perm, *nota in [
          (r"^diabetes$", "muerte_diabetes", "Muerte por diabetes", "enfermedad no transmisible", {}),
          (r"^infarto agudo", "muerte_infarto", "Muerte por infarto agudo de miocardio", "enfermedad no transmisible", {}),
          (r"^otras enfermedades cardiovasculares", "muerte_cardiovascular_otras", "Muerte por otras enfermedades cardiovasculares", "enfermedad no transmisible", {}),
          (r"^enfermedad respiratoria cronica", "muerte_respiratoria_cronica", "Muerte por enfermedad respiratoria crónica", "enfermedad no transmisible", {}),
          (r"^c?ancer (de )?cervico uterino", "muerte_cancer_cuello_uterino", "Muerte por cáncer de cuello uterino", "cáncer", SOLO_MUJER),
          (r"^cancer de mama", "muerte_cancer_mama", "Muerte por cáncer de mama", "cáncer", {}),
          (r"^cancer de prostata", "muerte_cancer_prostata", "Muerte por cáncer de próstata", "cáncer", SOLO_HOMBRE),
          (r"^leucemias", "muerte_leucemias", "Muerte por leucemias", "cáncer", {}),
          (r"^cancer en sus distintas formas", "muerte_cancer_otros", "Muerte por cáncer de otras localizaciones", "cáncer", {}),
          (r"^accidente cerebrovascular", "muerte_acv", "Muerte por accidente cerebrovascular", "enfermedad no transmisible", {}),
          (r"^enfermedad pulmonar obstructiva", "muerte_epoc", "Muerte por EPOC", "enfermedad no transmisible", {},
           "SOAPS 7.0.1 asigna a esta variable el código interno DX16, «Mortalidad por Accidente "
           "Cerebrovascular», el mismo de la muerte por accidente cerebrovascular. Las cifras de los dos "
           "datasets son distintas (2024: 118 muertes por EPOC y 436 por accidente cerebrovascular): uno no "
           "copia al otro, pero no sabemos cómo se cuenta esta variable."),
          (r"^insuficiencia renal", "muerte_insuficiencia_renal", "Muerte por insuficiencia renal", "enfermedad no transmisible", {}),
      ]],

    # --- Estado nutricional -------------------------------------------------------------------------
    *[Regla(p, N, i, n, ind, ("302", "302b"), g, gs, fijo=fijo)
      for p, i, n, ind, g, gs, fijo in [
          (r"^clasificacion a y b", "nutricion_clasificacion_ab", "Clasificación A y B", "Clasificación nutricional (A a F)", ("11",), (2001, 2004), {}),
          (r"^clasificacion c$", "nutricion_clasificacion_c", "Clasificación C", "Clasificación nutricional (A a F)", ("11",), (2001, 2004), {}),
          (r"^clasificacion d$", "nutricion_clasificacion_d", "Clasificación D", "Clasificación nutricional (A a F)", ("11",), (2001, 2004), {}),
          (r"^clasificacion e$", "nutricion_clasificacion_e", "Clasificación E", "Clasificación nutricional (A a F)", ("11",), (2001, 2004), {}),
          (r"^clasificacion f$", "nutricion_clasificacion_f", "Clasificación F", "Clasificación nutricional (A a F)", ("11",), (2001, 2004), {}),
          (r"^sobrepeso", "peso_sobrepeso", "Sobrepeso", "Peso", ("11", "06"), None, {}),
          (r"^obesidad", "peso_obesidad", "Obesidad", "Peso", ("11", "06"), None, {}),
          (r"^nutricion superior", "peso_superior", "Nutrición superior", "Peso", ("11",), None, {}),
          (r"^nutricion normal", "peso_normal", "Normal", "Peso", ("11", "06"), None, {}),
          (r"^desnutricion leve", "peso_desnutricion_leve", "Desnutrición leve", "Peso", ("11",), None, {}),
          (r"^desnutricion moderada", "peso_desnutricion_moderada", "Desnutrición moderada", "Peso", ("11", "06"), None, {}),
          (r"^desnutricion grave", "peso_desnutricion_grave", "Desnutrición grave", "Peso", ("11", "06"), None, {}),
          (r"^(embarazada )?desnutrida$", "embarazada_desnutrida", "Embarazada desnutrida", "Estado nutricional de la embarazada", ("11", "06"), None, MUJER),
          (r"^talla normal", "talla_normal", "Talla normal", "Talla para la edad", ("12", "14", "07"), None, {}),
          (r"^talla baja leve", "talla_baja_leve", "Talla baja leve", "Talla para la edad", ("12",), None, {}),
          (r"^talla baja moderada", "talla_baja_moderada", "Talla baja moderada", "Talla para la edad", ("12",), None, {}),
          (r"^talla baja grave", "talla_baja_grave", "Talla baja grave", "Talla para la edad", ("12",), None, {}),
          (r"^talla baja( \(tb\))?$", "talla_baja", "Talla baja", "Talla para la edad", ("14", "07"), None, {}),
          (r"^global peso bajo", "peso_bajo_global", "Peso bajo (moderado y grave)", "Peso para la edad", ("12",), None, {}),
          (r"^cronica talla baja", "talla_baja_moderada_grave", "Talla baja (moderada y grave)", "Talla para la edad", ("12",), None, {}),
      ]],
    Regla(r"^desastres y emergencias", E, "emergencia_2004", "Desastres y emergencias", "emergencia", ("302",), ("03",), (2004, 2004)),
    Regla(r"^nro\. de embarazadas enflaquecidas", N, "embarazada_desnutrida", "Embarazada desnutrida",
          "Estado nutricional de la embarazada", ("302",), ("10",), fijo=MUJER),

    # --- Desarrollo infantil temprano (302b, 2024-2025) ----------------------------------------------
    *[Regla(p, R, i, n, "Desarrollo infantil temprano", ("302b",), ("10",))
      for p, i, n in [
          (r"^desarrollo adecuado", "desarrollo_adecuado", "Desarrollo adecuado"),
          (r"^rezago leve", "rezago_leve", "Rezago leve"),
          (r"^rezago moderado", "rezago_moderado", "Rezago moderado"),
          (r"^rezago grave", "rezago_grave", "Rezago grave"),
      ]],

    # --- Factores de riesgo de enfermedades no transmisibles (302b) -----------------------------------
    *[Regla(p, F, i, n, "factor de riesgo", ("302b",), ("01",))
      for p, i, n in [
          (r"^sedentarismo", "sedentarismo", "Sedentarismo"),
          (r"^sobrepeso", "sobrepeso", "Sobrepeso"),
          (r"^habito de fumar", "tabaquismo", "Hábito de fumar"),
          (r"^abuso de alcohol", "abuso_alcohol", "Abuso de alcohol"),
      ]],

    # --- Emergencias y desastres ----------------------------------------------------------------------
    *[Regla(p, E, i, n, "emergencia", ("302", "302a"), ("15", "16"), (2010, 2025), nota=nota)
      for p, i, n, nota in [
          (r"^riada", "riada", "Riada", None),
          (r"^helada/granizo/nevada", "helada_granizo_nevada", "Helada, granizo o nevada", None),
          (r"^granizo", "granizo", "Granizo", None),
          (r"^nevada", "nevada", "Nevada", None),
          (r"^heladas", "heladas", "Heladas", None),
          (r"^incendio", "incendio", "Incendio", None),
          (r"^deslizamiento/sismo", "deslizamiento_sismo", "Deslizamiento, sismo o terremoto", None),
          (r"^deslizamiento$", "deslizamiento", "Deslizamiento", None),
          (r"^sismo/terremoto", "sismo", "Sismo o terremoto", None),
          (r"^inundacion", "inundacion", "Inundación", None),
          (r"^sequias", "sequia", "Sequía", None),
          (r"^otros de excepcion", "emergencia_otra", "Otros eventos de excepción", None),
      ]],
]

# Reglas por código de variable, para variables cuyo nombre no basta.
POR_CODIGO = {
    # 302b 2024-2025: el nombre está truncado en el tablero; SOAPS 7.0.1 da el nombre completo.
    ("302b", "03", "11"): Regla("", C, "trastornos_drogas_estimulantes", "Trastornos por consumo de drogas estimulantes",
                                "salud mental", gestiones=(2024, 9999)),
    ("302b", "03", "12"): Regla("", C, "trastornos_drogas_depresoras", "Trastornos por consumo de drogas depresoras",
                                "salud mental", gestiones=(2024, 9999)),
    ("302b", "03", "13"): Regla("", C, "trastornos_drogas_alucinogenas", "Trastornos por consumo de drogas alucinógenas",
                                "salud mental", gestiones=(2024, 9999)),
    # 302b 2024-2025: el tablero llama «Enfermedad Renal Cronica» a la variable 09/02, pero su
    # código CIE-10 en SOAPS es N18.31 (estadio 3a), como el nombre de la casilla 3050902.
    ("302b", "09", "02"): Regla("", C, "enfermedad_renal_estadio_3a", "Enfermedad renal, estadio 3a",
                                "enfermedad no transmisible", gestiones=(2024, 9999),
                                nota="El tablero la llama «Enfermedad Renal Crónica»; su código CIE-10 es N18.31 (estadio 3a)."),
    # 302 2010-2014: dos variables tienen el mismo nombre truncado; SOAPS 1.0.4 y 2.0.0 las distinguen.
    ("302", "10", "01"): Regla("", C, "hemorragia_primera_mitad_aborto",
                               "Hemorragia de la primera mitad del embarazo que terminó en aborto", "salud materna",
                               gestiones=(2010, 2014), fijo=MUJER, permitido=MATERNA),
    ("302", "10", "03"): Regla("", C, "hemorragia_primera_mitad", "Hemorragia de la primera mitad del embarazo",
                               "salud materna", gestiones=(2010, 2014), fijo=MUJER, permitido=MATERNA),
}


def asignar(formulario: str, gestion: int, grupo: str, variable: str, nombre: str) -> Regla | None:
    """Devuelve la regla por código si aplica; si no, la primera regla por nombre."""
    r = POR_CODIGO.get((formulario, grupo, variable))
    if r and r.gestiones[0] <= gestion <= r.gestiones[1]:
        return r
    n = normalizar_nombre(nombre)
    return next((r for r in REGLAS if r.aplica(formulario, grupo, gestion, n)), None)


# --- Familias -------------------------------------------------------------------------------
# Una familia publica varias series en un mismo dataset, con una columna que las distingue: las
# partes de una enfermedad (hepatitis A, B y C) o los grados de una condición (gravedad, forma
# clínica, estadio, clase nutricional). Un dataset tiene un solo conjunto de categorías: si el
# conjunto cambia entre gestiones, el paso 3 divide la familia en un dataset por periodo y la
# documentación los enlaza. Una serie sin parte propia (la hepatitis viral antes de dividirse)
# tiene el valor None; si convive con sus partes, «no especificado».

@dataclass
class Familia:
    nombre: str
    columna: str
    miembros: dict[str, str | None]   # serie_id -> valor en la columna
    nota: str | None = None
    nota_gestiones: tuple[int, int] | None = None   # la nota sólo vale para los datasets de esas gestiones


FAMILIAS: dict[str, Familia] = {
    "morbilidad_por_capitulo": Familia("Morbilidad por capítulo de la CIE-10", "capitulo", {
        "grupo_sistema_nervioso": "Sistema nervioso", "grupo_ojo": "Ojo y anexos",
        "grupo_oido": "Oído y apófisis mastoides", "grupo_circulatorio": "Sistema circulatorio",
        "grupo_respiratorio": "Sistema respiratorio", "grupo_digestivo": "Sistema digestivo",
        "grupo_piel": "Piel y tejido subcutáneo", "grupo_osteomuscular": "Sistema osteomuscular",
        "grupo_genitourinario": "Sistema genitourinario", "grupo_embarazo": "Embarazo, parto y puerperio",
        "grupo_malformaciones": "Malformaciones congénitas", "grupo_traumatismos": "Traumatismos y envenenamientos",
        "grupo_mentales": "Trastornos mentales", "grupo_otras_causas": "Otras causas",
        "grupo_sangre": "Sangre y trastornos inmunitarios", "grupo_endocrino": "Endocrinas, nutricionales y metabólicas",
        "grupo_tumores": "Tumores"}),
    "dengue": Familia("Dengue por clasificación clínica", "clasificacion", {
        "dengue_clasico": "clásico", "dengue_hemorragico": "hemorrágico", "dengue_sin_signos": "sin signos de alarma",
        "dengue_con_signos": "con signos de alarma", "dengue_grave": "grave"}),
    "sarampion_rubeola": Familia("Sarampión y rubéola", "enfermedad", {
        "sarampion": "sarampión", "rubeola": "rubéola", "sarampion_rubeola": "sarampión o rubéola"},
        "En 2004 el formulario tiene a la vez «Rubéola» y «Sarampión / Rubéola»; no sabemos si se superponen.", (2004, 2004)),
    "tetanos": Familia("Tétanos", "tipo", {
        "tetanos_neonatal": "neonatal", "tetanos_adulto": "adulto", "tetanos": None}),
    "hepatitis_viral": Familia("Hepatitis viral", "tipo", {
        "hepatitis_viral": None, "hepatitis_a": "A", "hepatitis_b_c": "B o C",
        "hepatitis_b": "B", "hepatitis_c": "C", "hepatitis_otras": "otras"},
        "«B o C» y «otras» comparten los códigos B17.8 y B18.8: un caso puede estar en las dos.", (2021, 2023)),
    "leishmaniasis": Familia("Leishmaniasis", "forma_clinica", {
        "leishmaniasis": None, "leishmaniasis_cutanea": "cutánea",
        "leishmaniasis_mucocutanea": "mucocutánea", "leishmaniasis_visceral": "visceral"}),
    "chagas_agudo": Familia("Chagas agudo", "transmision", {
        "chagas_agudo": None, "chagas_agudo_congenito": "congénita", "chagas_agudo_otros": "otros mecanismos"},
        "SOAPS asigna el código B42.0 a la transmisión congénita y a otros mecanismos.", (2024, 2025)),
    "lepra": Familia("Lepra", "forma_clinica", {
        "lepra": None, "lepra_paucibacilar": "paucibacilar", "lepra_multibacilar": "multibacilar"}),
    "tuberculosis_por_forma": Familia("Tuberculosis por forma", "forma", {
        "tb_pulmonar_baar_positivo": "pulmonar BAAR positivo, nuevo", "tb_pulmonar_baar_negativo": "pulmonar BAAR negativo, nuevo",
        "tb_extrapulmonar": "extrapulmonar", "tb_previamente_tratados": "pulmonar BAAR positivo, previamente tratado"}),
    "tuberculosis_resultado_tratamiento": Familia("Tuberculosis: resultado del tratamiento", "resultado", {
        "tb_curados": "curado", "tb_fracaso": "fracaso terapéutico"}),
    "reacciones_adversas_antituberculosos": Familia("Reacciones adversas a fármacos antituberculosos", "gravedad", {
        "rafa_leve": "leve o moderada", "rafa_grave": "grave"}),
    "intoxicacion_plaguicidas": Familia("Intoxicación por plaguicidas", "agente", {
        "plaguicidas": "no especificado", "organofosforados": "organofosforados y carbamatos", "halogenados": "halogenados",
        "herbicidas": "herbicidas y fungicidas", "otros_plaguicidas": "otros plaguicidas e insecticidas"}),
    "intoxicacion_otras": Familia("Otras intoxicaciones", "agente", {
        "intoxicacion_alcohol": "alcohol", "intoxicacion_drogas": "drogas",
        "otras_intoxicaciones": "drogas, fármacos, alcohol y otras"}),
    "violencia_sexual": Familia("Violencia sexual", "ambito", {
        "violencia_sexual": None, "violencia_sexual_familiar": "familiar", "violencia_sexual_otros": "otros contextos"}),
    "violencia_fisica": Familia("Violencia física", "ambito", {
        "violencia_fisica_familiar": "familiar", "violencia_fisica_otros": "otros contextos"}),
    "lesiones_autoinfligidas_violencia_colectiva": Familia("Lesiones autoinfligidas y violencia colectiva", "tipo", {
        "violencia_autoinfligida_colectiva": None, "lesiones_autoinfligidas": "lesiones autoinfligidas",
        "violencia_colectiva": "violencia colectiva"}),
    "trastornos_consumo_sustancias": Familia("Trastornos por consumo de sustancias", "sustancia", {
        "trastornos_consumo_sustancias": None, "trastornos_drogas_estimulantes": "estimulantes",
        "trastornos_drogas_depresoras": "depresoras", "trastornos_drogas_alucinogenas": "alucinógenas"}),
    "enfermedad_renal_cronica": Familia("Enfermedad renal crónica por estadio", "estadio", {
        "enfermedad_renal_estadio_3": "3", "enfermedad_renal_estadio_3a": "3a", "enfermedad_renal_estadio_3b": "3b",
        "enfermedad_renal_estadio_4": "4", "enfermedad_renal_estadio_5": "5"}),
    "preeclampsia_eclampsia": Familia("Preeclampsia y eclampsia", "diagnostico", {
        "preeclampsia_eclampsia": None, "preeclampsia_severa": "preeclampsia severa", "eclampsia": "eclampsia"}),
    "hemorragia_primera_mitad_embarazo": Familia("Hemorragia de la primera mitad del embarazo", "desenlace", {
        "hemorragia_primera_mitad": "no especificado", "hemorragia_primera_mitad_aborto": "terminó en aborto"}),
    "clasificacion_nutricional_2001": Familia("Clasificación nutricional A a F", "clasificacion", {
        "nutricion_clasificacion_ab": "A y B", "nutricion_clasificacion_c": "C", "nutricion_clasificacion_d": "D",
        "nutricion_clasificacion_e": "E", "nutricion_clasificacion_f": "F"}),
    "peso": Familia("Peso para la edad", "clasificacion", {
        "peso_normal": "normal", "peso_desnutricion_leve": "desnutrición leve", "peso_desnutricion_moderada": "desnutrición moderada",
        "peso_desnutricion_grave": "desnutrición grave", "peso_bajo_global": "peso bajo (moderado y grave)",
        "peso_sobrepeso": "sobrepeso", "peso_obesidad": "obesidad", "peso_superior": "nutrición superior"},
        "«Peso bajo (moderado y grave)» está junto a «desnutrición moderada» y «desnutrición grave».", (2007, 2007)),
    "talla": Familia("Talla para la edad", "clasificacion", {
        "talla_normal": "normal", "talla_baja": "baja", "talla_baja_leve": "baja leve", "talla_baja_moderada": "baja moderada",
        "talla_baja_grave": "baja grave", "talla_baja_moderada_grave": "baja moderada y grave"}),
    "desarrollo_infantil": Familia("Desarrollo infantil temprano", "resultado", {
        "desarrollo_adecuado": "adecuado", "rezago_leve": "rezago leve", "rezago_moderado": "rezago moderado",
        "rezago_grave": "rezago grave"}),
    "helada_granizo_nevada": Familia("Helada, granizo y nevada", "evento", {
        "helada_granizo_nevada": None, "granizo": "granizo", "nevada": "nevada", "heladas": "heladas"}),
    "deslizamiento_sismo": Familia("Deslizamiento y sismo", "evento", {
        "deslizamiento": "deslizamiento", "deslizamiento_sismo": "deslizamiento o sismo", "sismo": "sismo o terremoto"}),
}

DATASET = {s: d for d, f in FAMILIAS.items() for s in f.miembros}   # serie_id -> dataset

_ids = {r.id for r in REGLAS} | {r.id for r in POR_CODIGO.values()}
assert set(DATASET) <= _ids, set(DATASET) - _ids
_choques = {d for d in FAMILIAS if d in _ids and DATASET.get(d) != d}
assert not _choques, f"familias con el id de otra serie: {_choques}"


# --- Cortes ------------------------------------------------------------------------------------
# Gestiones en que cambia la definición de una serie con el mismo nombre. El paso 3 divide el
# dataset en esas gestiones, y la documentación enlaza los periodos con este texto.
CORTES: dict[str, tuple[tuple[int, ...], str]] = {
    "flujo_uretral_vaginal": ((2007, 2011), "La variable cuenta hombres con flujo uretral (2001-2006), flujo uretral o "
                              "uretritis sin restringir el sexo (2007-2010) y flujo uretral o vaginal (desde 2011)."),
    "malaria": ((2010, 2015), "En 2010-2014 la variable es «Malaria confirmados» y el formulario notifica los casos "
                "sospechosos aparte; antes y después, «Malaria»."),
    "cancer_cuello_uterino": ((2024,), "Desde 2024 la definición de SOAPS incluye cáncer del cuerpo del útero (C54, "
                              "C55) y carcinoma in situ (D06)."),
    "cancer_otros": ((2024,), "En 2024 el formulario notifica aparte tiroides, pulmón, estómago, colon y recto, piel y "
                     "linfomas: desde entonces esta variable excluye esas localizaciones."),
}

# --- Relaciones --------------------------------------------------------------------------------
# Series con otro nombre, otra definición o en otra sección del formulario. Los datasets de una
# misma serie o familia divididos por periodo se enlazan sin declararlos aquí.
_UNIRLOS = "Consultarlos juntos como una serie supone que "
RELACIONES = [
    *[Relacion((i, *par),
               "En 2001-2003 el formulario registra esta enfermedad en dos secciones, con cifras distintas: «Sospecha "
               "diagnóstica» y otra sección. No sabemos qué cuenta cada una. La de sospecha continúa desde 2004: para "
               "una serie larga, use esa. No las sume: un caso puede estar en ambas.", unir=False)
      for _, i, _, _, par in SECCIONES],
    Relacion(("dengue_seccion_metaxenicas", "dengue"),
             "El formulario registra el dengue en dos secciones, con cifras distintas: enfermedades metaxénicas "
             "(2001-2004 y 2015-2020), sin clasificación clínica, y dengue por clasificación clínica. En 2015-2018 la "
             "clasificación clínica sólo tiene dengue grave: la mayoría de los casos de esos años está en la sección "
             "de enfermedades metaxénicas. No las sume: un caso puede estar en ambas.", unir=False),
    Relacion(("hemorragia_primera_mitad_embarazo",),
             "En 2024 las dos partes suman lo mismo que la variable única de 2023 (20.570 y 19.761). En 2010-2014 "
             "suman unos 32 mil, más que la variable única de 2009 (21.905) y de 2015 (20.426): pueden superponerse."),
    Relacion(("meningitis_meningococica", "enfermedad_meningococica"),
             "Hasta 2014 el formulario notifica la meningitis meningocócica; desde 2015, la enfermedad meningocócica, "
             "una definición más amplia. " + _UNIRLOS + "la definición más amplia no cambia la serie."),
    Relacion(("meningitis_tuberculosa", "meningitis_tb_menor_5", "tuberculosis_meningea"),
             "El formulario notifica la meningitis tuberculosa en todas las edades (2001-2003) y en menores de 5 años "
             "(2001-2009); desde 2010, la tuberculosis meníngea en todas las edades. " + _UNIRLOS + "las tres "
             "variables cuentan lo mismo en las edades que comparten; filtre por edad antes de unirlas."),
    Relacion(("malaria", "malaria_sospecha"),
             "En 2010-2014 el formulario notifica por separado los casos de malaria confirmados y los sospechosos; "
             "antes y después, una sola variable, «Malaria». " + _UNIRLOS + "«Malaria» equivale a los confirmados, "
             "o a confirmados más sospechosos; el formulario no dice cuál."),
    Relacion(("violencia_intrafamiliar", "violencia_fisica", "violencia_sexual", "violencia_negligencia"),
             "Hasta 2023 el formulario notifica la violencia intrafamiliar; desde 2024 separa la violencia física y la "
             "sexual, familiar y en otros contextos (columna `ambito`), y la negligencia o abandono. No sabemos qué "
             "partes de 2024 equivalen a la violencia intrafamiliar.", unir=False),
    Relacion(("violencia_intrafamiliar", "violencia_intrafamiliar_ninez"),
             "En 2001-2003 el formulario notifica aparte la violencia intrafamiliar contra niñas y niños. No sabemos si "
             "esos casos están también en la violencia intrafamiliar.", unir=False),
]
