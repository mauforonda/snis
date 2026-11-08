# Datos del SNIS de Bolivia

601 datasets con las estadísticas del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes, de 2001 a 2025, por municipio. Cada dataset es una carpeta con tres archivos:

- `datos.parquet`: los datos;
- `readme.md`: qué contiene, cómo usarlo y de dónde viene;
- `datapackage.json`: los mismos metadatos en formato [Data Package](https://datapackage.org).

Las carpetas siguen el orden `datos/<dominio>/<clasificación>/<dataset>/`. Hay dos dominios: vigilancia epidemiológica (formularios 302, 302a y 302b: casos, defunciones y otros eventos) y producción de servicios (formularios 301, 301a y 301b: consultas, vacunas, partos y otras prestaciones). La clasificación dice qué cuenta el dataset.

Índice:

- [Vigilancia epidemiológica](#vigilancia-epidemiológica)
- [Producción de servicios](#producción-de-servicios)
- [Referencias](#referencias)
- [Cómo leer los datos](#cómo-leer-los-datos)

## Vigilancia epidemiológica

241 datasets de los formularios 302, 302a y 302b.

### Casos

Personas atendidas con un diagnóstico. 182 datasets.

#### Accidentes

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Accidentes laborales](vigilancia/casos/accidentes_laborales/readme.md) | 2024-2025 | 302a | semanal | sexo, edad |  |  |
| [Hechos de tránsito](vigilancia/casos/hechos_transito/readme.md) | 2010-2025 | 302, 302a | semanal | sexo, edad |  |  |
| [Otros accidentes](vigilancia/casos/otros_accidentes/readme.md) | 2010-2025 | 302, 302a | semanal | sexo, edad |  |  |

#### Animal

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Rabia canina (casos en perros)](vigilancia/casos/rabia_canina/readme.md) | 2001-2004, 2010-2025 | 302, 302a | semanal | sexo, edad | Cuenta perros, no personas. El formulario usa para los perros la misma plantilla de sexo y bandas de edad que para las personas; las bandas de 20 años o más no son posibles en perros. |  |

#### Cáncer

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Cáncer de colon y recto](vigilancia/casos/cancer_colon_recto/readme.md) | 2024-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Cáncer de cuello uterino (2015-2023)](vigilancia/casos/cancer_cuello_uterino_2015_2023/readme.md) | 2015-2018, 2020-2023 | 302b | mensual | sexo, edad, nuevo o repetido | Desde 2024 la definición de SOAPS incluye cáncer del cuerpo del útero (C54, C55) y carcinoma in situ (D06). El dataset tiene registros implausibles. | Otros periodos: [2024-2025](vigilancia/casos/cancer_cuello_uterino_2024_2025/readme.md). |
| [Cáncer de cuello uterino (2024-2025)](vigilancia/casos/cancer_cuello_uterino_2024_2025/readme.md) | 2024-2025 | 302b | mensual | sexo, edad, nuevo o repetido | Desde 2024 la definición de SOAPS incluye cáncer del cuerpo del útero (C54, C55) y carcinoma in situ (D06). | Otros periodos: [2015-2023](vigilancia/casos/cancer_cuello_uterino_2015_2023/readme.md). |
| [Cáncer de estómago](vigilancia/casos/cancer_estomago/readme.md) | 2024-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Cáncer de mama](vigilancia/casos/cancer_mama/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Cáncer de otras localizaciones (2015-2023)](vigilancia/casos/cancer_otros_2015_2023/readme.md) | 2015-2018, 2020-2023 | 302b | mensual | sexo, edad, nuevo o repetido | En 2024 el formulario notifica aparte tiroides, pulmón, estómago, colon y recto, piel y linfomas: desde entonces esta variable excluye esas localizaciones. Excluye las localizaciones que el formulario notifica aparte. | Otros periodos: [2024-2025](vigilancia/casos/cancer_otros_2024_2025/readme.md). |
| [Cáncer de otras localizaciones (2024-2025)](vigilancia/casos/cancer_otros_2024_2025/readme.md) | 2024-2025 | 302b | mensual | sexo, edad, nuevo o repetido | En 2024 el formulario notifica aparte tiroides, pulmón, estómago, colon y recto, piel y linfomas: desde entonces esta variable excluye esas localizaciones. Excluye las localizaciones que el formulario notifica aparte. | Otros periodos: [2015-2023](vigilancia/casos/cancer_otros_2015_2023/readme.md). |
| [Cáncer de piel](vigilancia/casos/cancer_piel/readme.md) | 2024-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Cáncer de próstata](vigilancia/casos/cancer_prostata/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad, nuevo o repetido | El dataset tiene registros implausibles. |  |
| [Cáncer de pulmón](vigilancia/casos/cancer_pulmon/readme.md) | 2024-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Cáncer de tiroides](vigilancia/casos/cancer_tiroides/readme.md) | 2024-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Leucemias](vigilancia/casos/leucemias/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Linfomas](vigilancia/casos/linfomas/readme.md) | 2024-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |

#### Diarreica

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Cólera](vigilancia/casos/colera/readme.md) | 2001-2008, 2010-2013, 2016, 2018-2024 | 302, 302a | semanal | sexo, edad |  |  |
| [Enfermedad diarreica aguda](vigilancia/casos/eda/readme.md) | 2001-2025 | 302, 302a | semanal | sexo, edad |  |  |

#### Enfermedad no transmisible

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Accidente cerebrovascular](vigilancia/casos/accidente_cerebrovascular/readme.md) | 2024-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Artritis reumatoide](vigilancia/casos/artritis_reumatoide/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Asma](vigilancia/casos/asma/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Diabetes gestacional](vigilancia/casos/diabetes_gestacional/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad, nuevo o repetido | Una sola fila tiene 810 casos en mujeres de 60 años y más (Santa Rosa, septiembre de 2015): es un tercio de esa categoría. El código de la variable es O24.9 (diabetes en el embarazo, no especificada); también hay muchos casos en mujeres de 50 a 59 años. El dataset tiene registros implausibles. |  |
| [Diabetes tipo 1](vigilancia/casos/diabetes_tipo_1/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Diabetes tipo 2](vigilancia/casos/diabetes_tipo_2/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Dislipidemia](vigilancia/casos/dislipidemia/readme.md) | 2024-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Enfermedad pulmonar obstructiva crónica (EPOC)](vigilancia/casos/epoc/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Enfermedad renal](vigilancia/casos/enfermedad_renal/readme.md) | 2015-2018, 2020-2023 | 302b | mensual | sexo, edad, nuevo o repetido | Cuenta todas las enfermedades renales (CIE-10 N00 a N29), no sólo la enfermedad renal crónica. Los estadios 3, 4 y 5 tienen su propio dataset; no sabemos si sus casos están también aquí. |  |
| [Enfermedad renal crónica por estadio (2015-2023)](vigilancia/casos/enfermedad_renal_cronica_2015_2023/readme.md) | 2015-2018, 2020-2023 | 302b | mensual | estadio, sexo, edad, nuevo o repetido | Este dataset cuenta por separado 3 categorías de estadio: "3", "4" y "5". | Otros periodos: [2024-2025](vigilancia/casos/enfermedad_renal_cronica_2024_2025/readme.md). |
| [Enfermedad renal crónica por estadio (2024-2025)](vigilancia/casos/enfermedad_renal_cronica_2024_2025/readme.md) | 2024-2025 | 302b | mensual | estadio, sexo, edad, nuevo o repetido | Este dataset cuenta por separado 4 categorías de estadio: "3a", "3b", "4" y "5". El tablero la llama "Enfermedad Renal Crónica"; su código CIE-10 es N18.31 (estadio 3a). | Otros periodos: [2015-2023](vigilancia/casos/enfermedad_renal_cronica_2015_2023/readme.md). |
| [Hipertensión arterial](vigilancia/casos/hipertension_arterial/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Hipotiroidismo congénito](vigilancia/casos/hipotiroidismo_congenito/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Infarto agudo de miocardio](vigilancia/casos/infarto_agudo_miocardio/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Insuficiencia cardiaca](vigilancia/casos/insuficiencia_cardiaca/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Obesidad](vigilancia/casos/obesidad/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |

#### Grupo de enfermedades

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Morbilidad por capítulo de la CIE-10](vigilancia/casos/morbilidad_por_capitulo/readme.md) | 2001-2003 | 302 | semanal | capítulo, edad | Este dataset cuenta por separado 17 categorías de capítulo; el readme las lista. Clasificación general por sistema del formulario 2001-2003; puede incluir casos que también se notifican como enfermedades específicas. |  |

#### Inmunoprevenible

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Difteria](vigilancia/casos/difteria/readme.md) | 2001-2007, 2010-2019, 2021-2025 | 302, 302a | semanal | sexo, edad |  | No sumar: [Difteria (sección inmunoprevenibles, 2001-2003)](vigilancia/casos/difteria_seccion_inmunoprevenibles/readme.md). |
| [Difteria (sección inmunoprevenibles, 2001-2003)](vigilancia/casos/difteria_seccion_inmunoprevenibles/readme.md) | 2001-2003 | 302 | semanal | edad |  | No sumar: [Difteria](vigilancia/casos/difteria/readme.md). |
| [Enfermedades eruptivas](vigilancia/casos/eruptivas/readme.md) | 2001-2003 | 302 | semanal | edad |  |  |
| [Eventos supuestamente atribuidos a la vacunación (ESAVI)](vigilancia/casos/esavi/readme.md) | 2021-2025 | 302a | semanal | sexo, edad |  |  |
| [Fiebre amarilla (sección inmunoprevenibles, 2001-2003)](vigilancia/casos/fiebre_amarilla_seccion_inmunoprevenibles/readme.md) | 2001-2003 | 302 | semanal | edad |  | No sumar: [Fiebre amarilla](vigilancia/casos/fiebre_amarilla/readme.md). |
| [Hepatitis viral (2001-2014)](vigilancia/casos/hepatitis_viral_2001_2014/readme.md) | 2001-2014 | 302 | semanal | sexo, edad | Este dataset no separa por tipo. | Otros periodos: [2015-2020](vigilancia/casos/hepatitis_viral_2015_2020/readme.md), [2021-2023](vigilancia/casos/hepatitis_viral_2021_2023/readme.md), [2024-2025](vigilancia/casos/hepatitis_viral_2024_2025/readme.md). |
| [Hepatitis viral (2015-2020)](vigilancia/casos/hepatitis_viral_2015_2020/readme.md) | 2015-2020 | 302a | semanal | tipo, sexo, edad | Este dataset cuenta por separado 2 categorías de tipo: "A" y "B o C". | Otros periodos: [2001-2014](vigilancia/casos/hepatitis_viral_2001_2014/readme.md), [2021-2023](vigilancia/casos/hepatitis_viral_2021_2023/readme.md), [2024-2025](vigilancia/casos/hepatitis_viral_2024_2025/readme.md). |
| [Hepatitis viral (2021-2023)](vigilancia/casos/hepatitis_viral_2021_2023/readme.md) | 2021-2023 | 302a | semanal | tipo, sexo, edad | Este dataset cuenta por separado 3 categorías de tipo: "A", "B o C" y "otras". "B o C" y "otras" comparten los códigos B17.8 y B18.8: un caso puede estar en las dos. | Otros periodos: [2001-2014](vigilancia/casos/hepatitis_viral_2001_2014/readme.md), [2015-2020](vigilancia/casos/hepatitis_viral_2015_2020/readme.md), [2024-2025](vigilancia/casos/hepatitis_viral_2024_2025/readme.md). |
| [Hepatitis viral (2024-2025)](vigilancia/casos/hepatitis_viral_2024_2025/readme.md) | 2024-2025 | 302a | semanal | tipo, sexo, edad | Este dataset cuenta por separado 4 categorías de tipo: "A", "B", "C" y "otras". | Otros periodos: [2001-2014](vigilancia/casos/hepatitis_viral_2001_2014/readme.md), [2015-2020](vigilancia/casos/hepatitis_viral_2015_2020/readme.md), [2021-2023](vigilancia/casos/hepatitis_viral_2021_2023/readme.md). |
| [Parotiditis](vigilancia/casos/parotiditis/readme.md) | 2004-2025 | 302, 302a | semanal | sexo, edad |  |  |
| [Parálisis flácida aguda](vigilancia/casos/paralisis_flacida_aguda/readme.md) | 2001-2025 | 302, 302a | semanal | sexo, edad |  |  |
| [Poliomielitis](vigilancia/casos/poliomielitis/readme.md) | 2001-2003 | 302 | semanal | edad |  |  |
| [Sarampión o rubéola (2005-2025)](vigilancia/casos/sarampion_rubeola_2005_2025/readme.md) | 2005-2025 | 302, 302a | semanal | enfermedad, sexo, edad | Este dataset cuenta una sola categoría de enfermedad: "sarampión o rubéola". | Otros periodos: [2001-2003](vigilancia/casos/sarampion_rubeola_2001_2003/readme.md), [2004](vigilancia/casos/sarampion_rubeola_2004/readme.md). |
| [Sarampión y rubéola (2001-2003)](vigilancia/casos/sarampion_rubeola_2001_2003/readme.md) | 2001-2003 | 302 | semanal | enfermedad, edad | Este dataset cuenta por separado 2 categorías de enfermedad: "rubéola" y "sarampión". | Otros periodos: [2004](vigilancia/casos/sarampion_rubeola_2004/readme.md), [2005-2025](vigilancia/casos/sarampion_rubeola_2005_2025/readme.md). |
| [Sarampión y rubéola (2004)](vigilancia/casos/sarampion_rubeola_2004/readme.md) | 2004 | 302 | semanal | enfermedad, edad | Este dataset cuenta por separado 2 categorías de enfermedad: "rubéola" y "sarampión o rubéola". En 2004 el formulario tiene a la vez "Rubéola" y "Sarampión / Rubéola"; no sabemos si se superponen. | Otros periodos: [2001-2003](vigilancia/casos/sarampion_rubeola_2001_2003/readme.md), [2005-2025](vigilancia/casos/sarampion_rubeola_2005_2025/readme.md). |
| [Síndrome de rubéola congénita](vigilancia/casos/rubeola_congenita/readme.md) | 2015-2025 | 302a | semanal | sexo, edad |  |  |
| [Tos ferina](vigilancia/casos/tos_ferina/readme.md) | 2001-2025 | 302, 302a | semanal | sexo, edad |  | No sumar: [Tos ferina (sección inmunoprevenibles, 2001-2003)](vigilancia/casos/tos_ferina_seccion_inmunoprevenibles/readme.md). |
| [Tos ferina (sección inmunoprevenibles, 2001-2003)](vigilancia/casos/tos_ferina_seccion_inmunoprevenibles/readme.md) | 2001-2003 | 302 | semanal | edad |  | No sumar: [Tos ferina](vigilancia/casos/tos_ferina/readme.md). |
| [Tétanos (2001-2009)](vigilancia/casos/tetanos_2001_2009/readme.md) | 2001-2009 | 302 | semanal | tipo, sexo, edad | Este dataset cuenta por separado 2 categorías de tipo: "adulto" y "neonatal". | Otros periodos: [2010-2025](vigilancia/casos/tetanos_2010_2025/readme.md). |
| [Tétanos (neonatal y del adulto) (2010-2025)](vigilancia/casos/tetanos_2010_2025/readme.md) | 2010-2025 | 302, 302a | semanal | sexo, edad | Este dataset no separa por tipo. | Otros periodos: [2001-2009](vigilancia/casos/tetanos_2001_2009/readme.md). |
| [Varicela](vigilancia/casos/varicela/readme.md) | 2015-2025 | 302a | semanal | sexo, edad |  |  |

#### Intoxicación

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Enfermedades transmitidas por alimentos](vigilancia/casos/eta/readme.md) | 2010-2025 | 302, 302a | semanal | sexo, edad |  |  |
| [Intoxicación por alimentos (brotes)](vigilancia/casos/intoxicacion_alimentos_brotes/readme.md) | 2001-2003 | 302 | semanal |  |  |  |
| [Intoxicación por organofosforados y carbamatos (2001-2003)](vigilancia/casos/intoxicacion_plaguicidas_2001_2003/readme.md) | 2001-2003 | 302 | semanal | agente | Este dataset cuenta una sola categoría de agente: "organofosforados y carbamatos". | Otros periodos: [2004-2020](vigilancia/casos/intoxicacion_plaguicidas_2004_2020/readme.md), [2021-2025](vigilancia/casos/intoxicacion_plaguicidas_2021_2025/readme.md). |
| [Intoxicación por plaguicidas (2004-2020)](vigilancia/casos/intoxicacion_plaguicidas_2004_2020/readme.md) | 2004-2020 | 302, 302a | semanal | agente, sexo, edad | Este dataset cuenta una sola categoría de agente: "no especificado". | Otros periodos: [2001-2003](vigilancia/casos/intoxicacion_plaguicidas_2001_2003/readme.md), [2021-2025](vigilancia/casos/intoxicacion_plaguicidas_2021_2025/readme.md). |
| [Intoxicación por plaguicidas (2021-2025)](vigilancia/casos/intoxicacion_plaguicidas_2021_2025/readme.md) | 2021-2025 | 302a | semanal | agente, sexo, edad | Este dataset cuenta por separado 4 categorías de agente: "halogenados", "herbicidas y fungicidas", "organofosforados y carbamatos" y "otros plaguicidas e insecticidas". | Otros periodos: [2001-2003](vigilancia/casos/intoxicacion_plaguicidas_2001_2003/readme.md), [2004-2020](vigilancia/casos/intoxicacion_plaguicidas_2004_2020/readme.md). |
| [Otras intoxicaciones (2001-2003)](vigilancia/casos/intoxicacion_otras_2001_2003/readme.md) | 2001-2003 | 302 | semanal | agente | Este dataset cuenta por separado 2 categorías de agente: "alcohol" y "drogas". | Otros periodos: [2007-2025](vigilancia/casos/intoxicacion_otras_2007_2025/readme.md). |
| [Otras intoxicaciones (drogas, fármacos, alcohol) (2007-2025)](vigilancia/casos/intoxicacion_otras_2007_2025/readme.md) | 2007-2025 | 302, 302a | semanal | agente, sexo, edad | Este dataset cuenta una sola categoría de agente: "drogas, fármacos, alcohol y otras". | Otros periodos: [2001-2003](vigilancia/casos/intoxicacion_otras_2001_2003/readme.md). |

#### Lesiones por animales

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Envenenamiento por arácnidos y otros animales ponzoñosos](vigilancia/casos/envenenamiento_aracnidos/readme.md) | 2015-2025 | 302a | semanal | sexo, edad |  |  |
| [Mordedura o envenenamiento por serpiente](vigilancia/casos/mordedura_serpiente/readme.md) | 2010-2025 | 302, 302a | semanal | sexo, edad |  |  |
| [Personas expuestas al virus rábico (mordeduras)](vigilancia/casos/exposicion_rabica/readme.md) | 2004-2025 | 302, 302a | semanal | sexo, edad |  |  |

#### Metabólica congénita

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Fenilcetonuria](vigilancia/casos/fenilcetonuria/readme.md) | 2024-2025 | 302a | semanal | sexo, edad |  |  |
| [Fibrosis quística](vigilancia/casos/fibrosis_quistica/readme.md) | 2024 | 302a | semanal | sexo, edad |  |  |
| [Hiperplasia suprarrenal congénita](vigilancia/casos/hiperplasia_suprarrenal/readme.md) | 2024-2025 | 302a | semanal | sexo, edad |  |  |
| [Hipotiroidismo (tamizaje neonatal)](vigilancia/casos/hipotiroidismo_tamizaje/readme.md) | 2024-2025 | 302a | semanal | sexo, edad |  |  |

#### Neurológica

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Alzheimer](vigilancia/casos/alzheimer/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Epilepsia](vigilancia/casos/epilepsia/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Otras demencias](vigilancia/casos/demencias_otras/readme.md) | 2024-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Parkinson](vigilancia/casos/parkinson/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |

#### Otra transmisible

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Enfermedad meningocócica](vigilancia/casos/enfermedad_meningococica/readme.md) | 2015-2025 | 302a | semanal | sexo, edad |  | [Meningitis meningocócica](vigilancia/casos/meningitis_meningococica/readme.md). |
| [Meningitis (sección otras infecciones, 2001-2003)](vigilancia/casos/meningitis_seccion_otras_infecciones/readme.md) | 2001-2003 | 302 | semanal | edad |  | No sumar: [Meningitis por Haemophilus influenzae](vigilancia/casos/meningitis_haemophilus/readme.md), [Meningitis meningocócica](vigilancia/casos/meningitis_meningococica/readme.md), [Meningitis tuberculosa](vigilancia/casos/meningitis_tuberculosa/readme.md). |
| [Meningitis meningocócica](vigilancia/casos/meningitis_meningococica/readme.md) | 2001-2014 | 302 | semanal | edad |  | No sumar: [Meningitis por Haemophilus influenzae](vigilancia/casos/meningitis_haemophilus/readme.md), [Meningitis (sección otras infecciones, 2001-2003)](vigilancia/casos/meningitis_seccion_otras_infecciones/readme.md), [Meningitis tuberculosa](vigilancia/casos/meningitis_tuberculosa/readme.md). [Enfermedad meningocócica](vigilancia/casos/enfermedad_meningococica/readme.md). |
| [Meningitis por Haemophilus influenzae](vigilancia/casos/meningitis_haemophilus/readme.md) | 2001-2003 | 302 | semanal | edad |  | No sumar: [Meningitis meningocócica](vigilancia/casos/meningitis_meningococica/readme.md), [Meningitis (sección otras infecciones, 2001-2003)](vigilancia/casos/meningitis_seccion_otras_infecciones/readme.md), [Meningitis tuberculosa](vigilancia/casos/meningitis_tuberculosa/readme.md). |
| [Mpox (viruela símica)](vigilancia/casos/mpox/readme.md) | 2022-2025 | 302a | semanal | sexo, edad |  |  |
| [Otras meningitis](vigilancia/casos/meningitis_otras/readme.md) | 2020-2025 | 302a | semanal | sexo, edad |  |  |
| [Síndrome hemolítico urémico](vigilancia/casos/sindrome_hemolitico_uremico/readme.md) | 2020-2025 | 302a | semanal | sexo, edad |  |  |
| [Tifus exantemático](vigilancia/casos/tifus_exantematico/readme.md) | 2003 | 302 | semanal | edad |  | No sumar: [Tifus exantemático (sección otras infecciones, 2001-2003)](vigilancia/casos/tifus_exantematico_seccion_otras_infecciones/readme.md). |
| [Tifus exantemático (sección otras infecciones, 2001-2003)](vigilancia/casos/tifus_exantematico_seccion_otras_infecciones/readme.md) | 2001-2003 | 302 | semanal | edad |  | No sumar: [Tifus exantemático](vigilancia/casos/tifus_exantematico/readme.md). |

#### Respiratoria

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [COVID-19](vigilancia/casos/covid19/readme.md) | 2020-2025 | 302a | semanal | sexo, edad |  |  |
| [Infección respiratoria aguda sin neumonía](vigilancia/casos/ira_sin_neumonia/readme.md) | 2004-2025 | 302, 302a | semanal | sexo, edad |  |  |
| [Influenza (IRAG, IRAGI y ETI)](vigilancia/casos/influenza_irag_eti/readme.md) | 2015-2025 | 302a | semanal | sexo, edad |  |  |
| [Influenza pandémica](vigilancia/casos/influenza_pandemica/readme.md) | 2008-2014 | 302 | semanal | edad |  |  |
| [Neumonía](vigilancia/casos/neumonia/readme.md) | 2001-2025 | 302, 302a | semanal | sexo, edad |  |  |
| [Síndrome inflamatorio multisistémico asociado a COVID-19](vigilancia/casos/sim_covid19/readme.md) | 2021-2025 | 302a | semanal | sexo, edad |  |  |

#### Salud materna

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Aborto](vigilancia/casos/aborto/readme.md) | 2004 | 302 | semanal | sexo |  |  |
| [Embarazo en adolescentes (menores de 20 años)](vigilancia/casos/embarazo_adolescente/readme.md) | 2004-2014 | 302 | semanal | sexo |  |  |
| [Hemorragia de la primera mitad del embarazo (2001-2009)](vigilancia/casos/hemorragia_primera_mitad_embarazo_2001_2009/readme.md) | 2001-2003, 2005-2009 | 302 | semanal | desenlace, sexo | Este dataset cuenta una sola categoría de desenlace: "no especificado". | Otros periodos: [2010-2014](vigilancia/casos/hemorragia_primera_mitad_embarazo_2010_2014/readme.md), [2015-2023](vigilancia/casos/hemorragia_primera_mitad_embarazo_2015_2023/readme.md), [2024-2025](vigilancia/casos/hemorragia_primera_mitad_embarazo_2024_2025/readme.md). |
| [Hemorragia de la primera mitad del embarazo (2010-2014)](vigilancia/casos/hemorragia_primera_mitad_embarazo_2010_2014/readme.md) | 2010-2014 | 302 | semanal | desenlace, sexo | Este dataset cuenta por separado 2 categorías de desenlace: "no especificado" y "terminó en aborto". | Otros periodos: [2001-2009](vigilancia/casos/hemorragia_primera_mitad_embarazo_2001_2009/readme.md), [2015-2023](vigilancia/casos/hemorragia_primera_mitad_embarazo_2015_2023/readme.md), [2024-2025](vigilancia/casos/hemorragia_primera_mitad_embarazo_2024_2025/readme.md). |
| [Hemorragia de la primera mitad del embarazo (2015-2023)](vigilancia/casos/hemorragia_primera_mitad_embarazo_2015_2023/readme.md) | 2015-2023 | 302a | semanal | desenlace, sexo | Este dataset cuenta una sola categoría de desenlace: "no especificado". | Otros periodos: [2001-2009](vigilancia/casos/hemorragia_primera_mitad_embarazo_2001_2009/readme.md), [2010-2014](vigilancia/casos/hemorragia_primera_mitad_embarazo_2010_2014/readme.md), [2024-2025](vigilancia/casos/hemorragia_primera_mitad_embarazo_2024_2025/readme.md). |
| [Hemorragia de la primera mitad del embarazo (2024-2025)](vigilancia/casos/hemorragia_primera_mitad_embarazo_2024_2025/readme.md) | 2024-2025 | 302a | semanal | desenlace, sexo, edad, lugar | Este dataset cuenta por separado 2 categorías de desenlace: "no especificado" y "terminó en aborto". | Otros periodos: [2001-2009](vigilancia/casos/hemorragia_primera_mitad_embarazo_2001_2009/readme.md), [2010-2014](vigilancia/casos/hemorragia_primera_mitad_embarazo_2010_2014/readme.md), [2015-2023](vigilancia/casos/hemorragia_primera_mitad_embarazo_2015_2023/readme.md). |
| [Hemorragia del parto o puerperio](vigilancia/casos/hemorragia_parto_puerperio/readme.md) | 2004-2006 | 302 | semanal | sexo |  |  |
| [Parto en adolescentes (menores de 20 años)](vigilancia/casos/parto_adolescente/readme.md) | 2001-2003 | 302 | semanal | sexo |  |  |
| [Parto en mujeres mayores de 35 años](vigilancia/casos/parto_mayor_35/readme.md) | 2001-2003 | 302 | semanal | sexo |  |  |
| [Parturienta con hijo anterior muerto](vigilancia/casos/parturienta_hijo_muerto/readme.md) | 2001-2003 | 302 | semanal | sexo |  |  |
| [Parturienta con hijo anterior vivo](vigilancia/casos/parturienta_hijo_vivo/readme.md) | 2001-2003 | 302 | semanal | sexo |  |  |
| [Preeclampsia severa o eclampsia (2004-2014)](vigilancia/casos/preeclampsia_eclampsia_2004_2014/readme.md) | 2004-2014 | 302 | semanal | sexo | Este dataset no separa por diagnóstico. | Otros periodos: [2015-2025](vigilancia/casos/preeclampsia_eclampsia_2015_2025/readme.md). |
| [Preeclampsia y eclampsia (2015-2025)](vigilancia/casos/preeclampsia_eclampsia_2015_2025/readme.md) | 2015-2025 | 302a | semanal | diagnóstico, sexo, edad, lugar | Este dataset cuenta por separado 2 categorías de diagnóstico: "eclampsia" y "preeclampsia severa". | Otros periodos: [2004-2014](vigilancia/casos/preeclampsia_eclampsia_2004_2014/readme.md). |
| [Sepsis obstétrica](vigilancia/casos/sepsis_obstetrica/readme.md) | 2015-2025 | 302a | semanal | sexo, edad, lugar |  |  |

#### Salud mental

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Autismo](vigilancia/casos/autismo/readme.md) | 2024-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Episodios de ansiedad](vigilancia/casos/ansiedad/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Episodios depresivos](vigilancia/casos/depresion/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Episodios psicóticos o esquizofrenia](vigilancia/casos/psicosis_esquizofrenia/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Trastorno bipolar](vigilancia/casos/trastorno_bipolar/readme.md) | 2024-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Trastornos alimentarios (anorexia, bulimia)](vigilancia/casos/trastornos_alimentarios/readme.md) | 2024-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Trastornos de conducta](vigilancia/casos/trastornos_conducta/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad, nuevo o repetido |  |  |
| [Trastornos del comportamiento por consumo de sustancias (2015-2023)](vigilancia/casos/trastornos_consumo_sustancias_2015_2023/readme.md) | 2015-2018, 2020-2023 | 302b | mensual | sexo, edad, nuevo o repetido | Este dataset no separa por sustancia. | Otros periodos: [2024-2025](vigilancia/casos/trastornos_consumo_sustancias_2024_2025/readme.md). |
| [Trastornos mentales del embarazo, parto y puerperio](vigilancia/casos/trastorno_mental_perinatal/readme.md) | 2024-2025 | 302b | mensual | sexo, edad, nuevo o repetido | SOAPS cuenta esta variable cuando uno de los campos de diagnóstico tiene un código F53 (trastornos del puerperio), sin filtro de sexo. Los hombres de este dataset son pacientes registrados como hombres con ese código: pueden ser errores de sexo o de código. El instructivo de 2024 define el trastorno sólo en la madre. El dataset tiene registros implausibles. |  |
| [Trastornos por consumo de sustancias (2024-2025)](vigilancia/casos/trastornos_consumo_sustancias_2024_2025/readme.md) | 2024-2025 | 302b | mensual | sustancia, sexo, edad, nuevo o repetido | Este dataset cuenta por separado 3 categorías de sustancia: "alucinógenas", "depresoras" y "estimulantes". | Otros periodos: [2015-2023](vigilancia/casos/trastornos_consumo_sustancias_2015_2023/readme.md). |

#### Transmisión sexual

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Dolor abdominal o edema de escroto](vigilancia/casos/dolor_abdominal_edema_escroto/readme.md) | 2010 | 302 | semanal | sexo, edad |  |  |
| [Flujo uretral o vaginal (2001-2006)](vigilancia/casos/flujo_uretral_vaginal_2001_2006/readme.md) | 2001-2006 | 302 | semanal | sexo, edad | La variable cuenta hombres con flujo uretral (2001-2006), flujo uretral o uretritis sin restringir el sexo (2007-2010) y flujo uretral o vaginal (desde 2011). | Otros periodos: [2007-2010](vigilancia/casos/flujo_uretral_vaginal_2007_2010/readme.md), [2011-2025](vigilancia/casos/flujo_uretral_vaginal_2011_2025/readme.md). |
| [Flujo uretral o vaginal (2007-2010)](vigilancia/casos/flujo_uretral_vaginal_2007_2010/readme.md) | 2007-2010 | 302 | semanal | sexo, edad | La variable cuenta hombres con flujo uretral (2001-2006), flujo uretral o uretritis sin restringir el sexo (2007-2010) y flujo uretral o vaginal (desde 2011). | Otros periodos: [2001-2006](vigilancia/casos/flujo_uretral_vaginal_2001_2006/readme.md), [2011-2025](vigilancia/casos/flujo_uretral_vaginal_2011_2025/readme.md). |
| [Flujo uretral o vaginal (2011-2025)](vigilancia/casos/flujo_uretral_vaginal_2011_2025/readme.md) | 2011-2025 | 302, 302a | semanal | sexo, edad | La variable cuenta hombres con flujo uretral (2001-2006), flujo uretral o uretritis sin restringir el sexo (2007-2010) y flujo uretral o vaginal (desde 2011). | Otros periodos: [2001-2006](vigilancia/casos/flujo_uretral_vaginal_2001_2006/readme.md), [2007-2010](vigilancia/casos/flujo_uretral_vaginal_2007_2010/readme.md). |
| [Gonorrea](vigilancia/casos/gonorrea/readme.md) | 2015-2025 | 302a | semanal | sexo, edad |  |  |
| [SIDA](vigilancia/casos/sida/readme.md) | 2001-2014 | 302 | semanal | sexo, edad |  |  |
| [Sífilis](vigilancia/casos/sifilis/readme.md) | 2001-2003 | 302 | semanal | edad |  |  |
| [Sífilis congénita](vigilancia/casos/sifilis_congenita/readme.md) | 2001-2003, 2015-2025 | 302, 302a | semanal | sexo, edad |  |  |
| [Sífilis congénita en mortinatos](vigilancia/casos/sifilis_congenita_mortinato/readme.md) | 2001-2003 | 302 | semanal | edad |  |  |
| [Sífilis en la mujer embarazada](vigilancia/casos/sifilis_embarazada/readme.md) | 2011-2025 | 302, 302a | semanal | sexo, edad | El dataset tiene registros implausibles. |  |
| [VIH o SIDA](vigilancia/casos/vih_sida/readme.md) | 2001-2003 | 302 | semanal | edad |  |  |
| [VIH reactivo en la mujer embarazada](vigilancia/casos/vih_embarazada/readme.md) | 2010-2025 | 302, 302a | semanal | sexo, edad | El dataset tiene registros implausibles. |  |
| [VIH reactivo en la población general](vigilancia/casos/vih_poblacion_general/readme.md) | 2010-2025 | 302, 302a | semanal | sexo, edad |  |  |
| [Verruga genital](vigilancia/casos/verruga_genital/readme.md) | 2015-2025 | 302a | semanal | sexo, edad |  |  |
| [Úlcera genital](vigilancia/casos/ulcera_genital/readme.md) | 2001-2025 | 302, 302a | semanal | sexo, edad |  |  |

#### Tuberculosis y lepra

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Lepra (2001-2006)](vigilancia/casos/lepra_2001_2006/readme.md) | 2001-2006 | 302 | semanal | edad | Este dataset no separa por forma clínica. | Otros periodos: [2007-2025](vigilancia/casos/lepra_2007_2025/readme.md). |
| [Lepra (2007-2025)](vigilancia/casos/lepra_2007_2025/readme.md) | 2007-2025 | 302, 302a | semanal | forma clínica, sexo, edad | Este dataset cuenta por separado 2 categorías de forma clínica: "multibacilar" y "paucibacilar". | Otros periodos: [2001-2006](vigilancia/casos/lepra_2001_2006/readme.md). |
| [Meningitis tuberculosa](vigilancia/casos/meningitis_tuberculosa/readme.md) | 2001-2003 | 302 | semanal | edad |  | No sumar: [Meningitis por Haemophilus influenzae](vigilancia/casos/meningitis_haemophilus/readme.md), [Meningitis meningocócica](vigilancia/casos/meningitis_meningococica/readme.md), [Meningitis (sección otras infecciones, 2001-2003)](vigilancia/casos/meningitis_seccion_otras_infecciones/readme.md). [Meningitis tuberculosa en menores de 5 años](vigilancia/casos/meningitis_tb_menor_5/readme.md), [Tuberculosis meníngea](vigilancia/casos/tuberculosis_meningea/readme.md). |
| [Meningitis tuberculosa en menores de 5 años](vigilancia/casos/meningitis_tb_menor_5/readme.md) | 2001-2009 | 302 | semanal | sexo, edad |  | [Meningitis tuberculosa](vigilancia/casos/meningitis_tuberculosa/readme.md), [Tuberculosis meníngea](vigilancia/casos/tuberculosis_meningea/readme.md). |
| [Reacciones adversas a fármacos antituberculosos (2008-2023)](vigilancia/casos/reacciones_adversas_antituberculosos_2008_2023/readme.md) | 2008-2023 | 302, 302a | semanal | gravedad, sexo, edad | Este dataset cuenta por separado 2 categorías de gravedad: "grave" y "leve o moderada". En 2015-2023 la variable se llama "RAFA", sin calificar; se publica como leve o moderada porque el formulario notifica las graves aparte. | Otros periodos: [2024-2025](vigilancia/casos/reacciones_adversas_antituberculosos_2024_2025/readme.md). |
| [Reacciones adversas graves a fármacos antituberculosos (2024-2025)](vigilancia/casos/reacciones_adversas_antituberculosos_2024_2025/readme.md) | 2024-2025 | 302a | semanal | gravedad, sexo, edad | Este dataset cuenta una sola categoría de gravedad: "grave". | Otros periodos: [2008-2023](vigilancia/casos/reacciones_adversas_antituberculosos_2008_2023/readme.md). |
| [Sintomáticos respiratorios](vigilancia/casos/sintomatico_respiratorio/readme.md) | 2001-2007 | 302 | semanal | sexo, edad |  |  |
| [Tuberculosis meníngea](vigilancia/casos/tuberculosis_meningea/readme.md) | 2010-2016, 2018-2025 | 302, 302a | semanal | sexo, edad |  | [Meningitis tuberculosa en menores de 5 años](vigilancia/casos/meningitis_tb_menor_5/readme.md), [Meningitis tuberculosa](vigilancia/casos/meningitis_tuberculosa/readme.md). |
| [Tuberculosis por forma (2001-2003)](vigilancia/casos/tuberculosis_por_forma_2001_2003/readme.md) | 2001-2003 | 302 | semanal | forma | Este dataset cuenta por separado 4 categorías de forma: "extrapulmonar", "pulmonar BAAR negativo, nuevo", "pulmonar BAAR positivo, nuevo" y "pulmonar BAAR positivo, previamente tratado". | Otros periodos: [2004-2007](vigilancia/casos/tuberculosis_por_forma_2004_2007/readme.md). |
| [Tuberculosis por forma (2004-2007)](vigilancia/casos/tuberculosis_por_forma_2004_2007/readme.md) | 2004-2007 | 302 | semanal | forma, sexo, edad | Este dataset cuenta por separado 3 categorías de forma: "extrapulmonar", "pulmonar BAAR negativo, nuevo" y "pulmonar BAAR positivo, nuevo". | Otros periodos: [2001-2003](vigilancia/casos/tuberculosis_por_forma_2001_2003/readme.md). |
| [Tuberculosis: resultado del tratamiento](vigilancia/casos/tuberculosis_resultado_tratamiento/readme.md) | 2005-2007 | 302 | semanal | resultado, sexo, edad | Este dataset cuenta por separado 2 categorías de resultado: "curado" y "fracaso terapéutico". |  |

#### Vectorial

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Anomalía congénita (vigilancia de zika)](vigilancia/casos/anomalia_congenita_zika/readme.md) | 2017-2018 | 302a | semanal | sexo, edad |  |  |
| [Chagas agudo (2001-2023)](vigilancia/casos/chagas_agudo_2001_2023/readme.md) | 2001-2003, 2010-2023 | 302, 302a | semanal | sexo, edad | Este dataset no separa por transmisión. | Otros periodos: [2024-2025](vigilancia/casos/chagas_agudo_2024_2025/readme.md). |
| [Chagas agudo (2024-2025)](vigilancia/casos/chagas_agudo_2024_2025/readme.md) | 2024-2025 | 302a | semanal | transmisión, sexo, edad | Este dataset cuenta por separado 2 categorías de transmisión: "congénita" y "otros mecanismos". SOAPS asigna el código B42.0 a la transmisión congénita y a otros mecanismos. | Otros periodos: [2001-2023](vigilancia/casos/chagas_agudo_2001_2023/readme.md). |
| [Chikungunya](vigilancia/casos/chikungunya/readme.md) | 2016-2025 | 302a | semanal | sexo, edad |  |  |
| [Dengue (sección enfermedades metaxénicas)](vigilancia/casos/dengue_seccion_metaxenicas/readme.md) | 2001-2004, 2015-2020 | 302, 302a | semanal | sexo, edad |  | No sumar: [Dengue hemorrágico (2002-2004)](vigilancia/casos/dengue_2002_2004/readme.md), [Dengue por clasificación clínica (2005-2014)](vigilancia/casos/dengue_2005_2014/readme.md), [Dengue grave (2015-2018)](vigilancia/casos/dengue_2015_2018/readme.md), [Dengue por clasificación clínica (2019-2025)](vigilancia/casos/dengue_2019_2025/readme.md). |
| [Dengue grave (2015-2018)](vigilancia/casos/dengue_2015_2018/readme.md) | 2015-2018 | 302a | semanal | clasificación, sexo, edad | Este dataset cuenta una sola categoría de clasificación: "grave". | Otros periodos: [2002-2004](vigilancia/casos/dengue_2002_2004/readme.md), [2005-2014](vigilancia/casos/dengue_2005_2014/readme.md), [2019-2025](vigilancia/casos/dengue_2019_2025/readme.md). No sumar: [Dengue (sección enfermedades metaxénicas)](vigilancia/casos/dengue_seccion_metaxenicas/readme.md). |
| [Dengue hemorrágico (2002-2004)](vigilancia/casos/dengue_2002_2004/readme.md) | 2002-2004 | 302 | semanal | clasificación, edad | Este dataset cuenta una sola categoría de clasificación: "hemorrágico". | Otros periodos: [2005-2014](vigilancia/casos/dengue_2005_2014/readme.md), [2015-2018](vigilancia/casos/dengue_2015_2018/readme.md), [2019-2025](vigilancia/casos/dengue_2019_2025/readme.md). No sumar: [Dengue (sección enfermedades metaxénicas)](vigilancia/casos/dengue_seccion_metaxenicas/readme.md). |
| [Dengue por clasificación clínica (2005-2014)](vigilancia/casos/dengue_2005_2014/readme.md) | 2005-2014 | 302 | semanal | clasificación, edad | Este dataset cuenta por separado 2 categorías de clasificación: "clásico" y "hemorrágico". | Otros periodos: [2002-2004](vigilancia/casos/dengue_2002_2004/readme.md), [2015-2018](vigilancia/casos/dengue_2015_2018/readme.md), [2019-2025](vigilancia/casos/dengue_2019_2025/readme.md). No sumar: [Dengue (sección enfermedades metaxénicas)](vigilancia/casos/dengue_seccion_metaxenicas/readme.md). |
| [Dengue por clasificación clínica (2019-2025)](vigilancia/casos/dengue_2019_2025/readme.md) | 2019-2025 | 302a | semanal | clasificación, sexo, edad | Este dataset cuenta por separado 3 categorías de clasificación: "con signos de alarma", "grave" y "sin signos de alarma". | Otros periodos: [2002-2004](vigilancia/casos/dengue_2002_2004/readme.md), [2005-2014](vigilancia/casos/dengue_2005_2014/readme.md), [2015-2018](vigilancia/casos/dengue_2015_2018/readme.md). No sumar: [Dengue (sección enfermedades metaxénicas)](vigilancia/casos/dengue_seccion_metaxenicas/readme.md). |
| [Fiebre amarilla](vigilancia/casos/fiebre_amarilla/readme.md) | 2001-2025 | 302, 302a | semanal | sexo, edad |  | No sumar: [Fiebre amarilla (sección inmunoprevenibles, 2001-2003)](vigilancia/casos/fiebre_amarilla_seccion_inmunoprevenibles/readme.md). |
| [Leishmaniasis (2001-2023)](vigilancia/casos/leishmaniasis_2001_2023/readme.md) | 2001-2023 | 302, 302a | semanal | sexo, edad | Este dataset no separa por forma clínica. | Otros periodos: [2024-2025](vigilancia/casos/leishmaniasis_2024_2025/readme.md). |
| [Leishmaniasis (2024-2025)](vigilancia/casos/leishmaniasis_2024_2025/readme.md) | 2024-2025 | 302a | semanal | forma clínica, sexo, edad | Este dataset cuenta por separado 3 categorías de forma clínica: "cutánea", "mucocutánea" y "visceral". | Otros periodos: [2001-2023](vigilancia/casos/leishmaniasis_2001_2023/readme.md). |
| [Leishmaniasis (sospecha)](vigilancia/casos/leishmaniasis_sospecha/readme.md) | 2010-2014 | 302 | semanal | sexo, edad |  |  |
| [Malaria (2001-2009)](vigilancia/casos/malaria_2001_2009/readme.md) | 2001-2009 | 302 | semanal | sexo, edad | En 2010-2014 la variable es "Malaria confirmados" y el formulario notifica los casos sospechosos aparte; antes y después, "Malaria". | Otros periodos: [2010-2014](vigilancia/casos/malaria_2010_2014/readme.md), [2015-2025](vigilancia/casos/malaria_2015_2025/readme.md). [Malaria (sospecha)](vigilancia/casos/malaria_sospecha/readme.md). |
| [Malaria (2010-2014)](vigilancia/casos/malaria_2010_2014/readme.md) | 2010-2014 | 302 | semanal | sexo, edad | En 2010-2014 la variable es "Malaria confirmados" y el formulario notifica los casos sospechosos aparte; antes y después, "Malaria". | Otros periodos: [2001-2009](vigilancia/casos/malaria_2001_2009/readme.md), [2015-2025](vigilancia/casos/malaria_2015_2025/readme.md). [Malaria (sospecha)](vigilancia/casos/malaria_sospecha/readme.md). |
| [Malaria (2015-2025)](vigilancia/casos/malaria_2015_2025/readme.md) | 2015-2025 | 302a | semanal | sexo, edad | En 2010-2014 la variable es "Malaria confirmados" y el formulario notifica los casos sospechosos aparte; antes y después, "Malaria". | Otros periodos: [2001-2009](vigilancia/casos/malaria_2001_2009/readme.md), [2010-2014](vigilancia/casos/malaria_2010_2014/readme.md). [Malaria (sospecha)](vigilancia/casos/malaria_sospecha/readme.md). |
| [Malaria (sospecha)](vigilancia/casos/malaria_sospecha/readme.md) | 2010-2014 | 302 | semanal | sexo, edad |  | [Malaria (2001-2009)](vigilancia/casos/malaria_2001_2009/readme.md), [Malaria (2010-2014)](vigilancia/casos/malaria_2010_2014/readme.md), [Malaria (2015-2025)](vigilancia/casos/malaria_2015_2025/readme.md). |
| [Microcefalia (vigilancia de zika)](vigilancia/casos/microcefalia_zika/readme.md) | 2017-2018 | 302a | semanal | sexo, edad |  |  |
| [Oropouche](vigilancia/casos/oropouche/readme.md) | 2024-2025 | 302a | semanal | sexo, edad |  |  |
| [Síndrome de Guillain-Barré (vigilancia de zika)](vigilancia/casos/guillain_barre_zika/readme.md) | 2017-2018 | 302a | semanal | sexo, edad |  |  |
| [Trastorno neurológico (vigilancia de zika)](vigilancia/casos/trastorno_neurologico_zika/readme.md) | 2017-2018 | 302a | semanal | sexo, edad |  |  |
| [Zika](vigilancia/casos/zika/readme.md) | 2016-2025 | 302a | semanal | sexo, edad |  |  |

#### Violencia

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Lesiones autoinfligidas y violencia colectiva (2015-2023)](vigilancia/casos/lesiones_autoinfligidas_violencia_colectiva_2015_2023/readme.md) | 2015-2023 | 302a | semanal | sexo, edad | Este dataset no separa por tipo. | Otros periodos: [2024-2025](vigilancia/casos/lesiones_autoinfligidas_violencia_colectiva_2024_2025/readme.md). |
| [Lesiones autoinfligidas y violencia colectiva (2024-2025)](vigilancia/casos/lesiones_autoinfligidas_violencia_colectiva_2024_2025/readme.md) | 2024-2025 | 302a | semanal | tipo, sexo, edad | Este dataset cuenta por separado 2 categorías de tipo: "lesiones autoinfligidas" y "violencia colectiva". | Otros periodos: [2015-2023](vigilancia/casos/lesiones_autoinfligidas_violencia_colectiva_2015_2023/readme.md). |
| [Otras violencias (causas externas)](vigilancia/casos/otras_violencias/readme.md) | 2007-2014 | 302 | semanal | sexo, edad |  |  |
| [Violencia en la mujer embarazada](vigilancia/casos/violencia_embarazada/readme.md) | 2024-2025 | 302a | semanal | sexo, edad |  |  |
| [Violencia en la persona con discapacidad](vigilancia/casos/violencia_discapacidad/readme.md) | 2024-2025 | 302a | semanal | sexo, edad |  |  |
| [Violencia física](vigilancia/casos/violencia_fisica/readme.md) | 2024-2025 | 302a | semanal | ámbito, sexo, edad | Este dataset cuenta por separado 2 categorías de ámbito: "familiar" y "otros contextos". | No sumar: [Violencia intrafamiliar](vigilancia/casos/violencia_intrafamiliar/readme.md), [Violencia sexual (familiar y en otros ámbitos) (2015-2023)](vigilancia/casos/violencia_sexual_2015_2023/readme.md), [Violencia por negligencia o abandono](vigilancia/casos/violencia_negligencia/readme.md), [Violencia sexual (2024-2025)](vigilancia/casos/violencia_sexual_2024_2025/readme.md). |
| [Violencia intrafamiliar](vigilancia/casos/violencia_intrafamiliar/readme.md) | 2001-2023 | 302, 302a | semanal | sexo, edad |  | No sumar: [Violencia sexual (familiar y en otros ámbitos) (2015-2023)](vigilancia/casos/violencia_sexual_2015_2023/readme.md), [Violencia física](vigilancia/casos/violencia_fisica/readme.md), [Violencia por negligencia o abandono](vigilancia/casos/violencia_negligencia/readme.md), [Violencia sexual (2024-2025)](vigilancia/casos/violencia_sexual_2024_2025/readme.md). No sumar: [Violencia intrafamiliar contra niñas y niños](vigilancia/casos/violencia_intrafamiliar_ninez/readme.md). |
| [Violencia intrafamiliar contra niñas y niños](vigilancia/casos/violencia_intrafamiliar_ninez/readme.md) | 2001-2003 | 302 | semanal | sexo |  | No sumar: [Violencia intrafamiliar](vigilancia/casos/violencia_intrafamiliar/readme.md). |
| [Violencia por negligencia o abandono](vigilancia/casos/violencia_negligencia/readme.md) | 2024-2025 | 302a | semanal | sexo, edad |  | No sumar: [Violencia intrafamiliar](vigilancia/casos/violencia_intrafamiliar/readme.md), [Violencia sexual (familiar y en otros ámbitos) (2015-2023)](vigilancia/casos/violencia_sexual_2015_2023/readme.md), [Violencia física](vigilancia/casos/violencia_fisica/readme.md), [Violencia sexual (2024-2025)](vigilancia/casos/violencia_sexual_2024_2025/readme.md). |
| [Violencia sexual (2024-2025)](vigilancia/casos/violencia_sexual_2024_2025/readme.md) | 2024-2025 | 302a | semanal | ámbito, sexo, edad | Este dataset cuenta por separado 2 categorías de ámbito: "familiar" y "otros contextos". | Otros periodos: [2015-2023](vigilancia/casos/violencia_sexual_2015_2023/readme.md). No sumar: [Violencia intrafamiliar](vigilancia/casos/violencia_intrafamiliar/readme.md), [Violencia física](vigilancia/casos/violencia_fisica/readme.md), [Violencia por negligencia o abandono](vigilancia/casos/violencia_negligencia/readme.md). |
| [Violencia sexual (familiar y en otros ámbitos) (2015-2023)](vigilancia/casos/violencia_sexual_2015_2023/readme.md) | 2015-2023 | 302a | semanal | sexo, edad | Este dataset no separa por ámbito. | Otros periodos: [2024-2025](vigilancia/casos/violencia_sexual_2024_2025/readme.md). No sumar: [Violencia intrafamiliar](vigilancia/casos/violencia_intrafamiliar/readme.md), [Violencia física](vigilancia/casos/violencia_fisica/readme.md), [Violencia por negligencia o abandono](vigilancia/casos/violencia_negligencia/readme.md). |

#### Zoonosis

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Enfermedad por hantavirus](vigilancia/casos/hantavirus/readme.md) | 2001-2025 | 302, 302a | semanal | sexo, edad |  | No sumar: [Hantavirus (sección otras infecciones, 2001-2003)](vigilancia/casos/hantavirus_seccion_otras_infecciones/readme.md). |
| [Fiebre hemorrágica](vigilancia/casos/fiebre_hemorragica/readme.md) | 2003-2014, 2016-2025 | 302, 302a | semanal | sexo, edad | 2004-2019 el nombre es "fiebre hemorrágica boliviana". | No sumar: [Fiebre hemorrágica (sección otras infecciones, 2001-2003)](vigilancia/casos/fiebre_hemorragica_seccion_otras_infecciones/readme.md). |
| [Fiebre hemorrágica (sección otras infecciones, 2001-2003)](vigilancia/casos/fiebre_hemorragica_seccion_otras_infecciones/readme.md) | 2001-2003 | 302 | semanal | edad |  | No sumar: [Fiebre hemorrágica](vigilancia/casos/fiebre_hemorragica/readme.md). |
| [Hantavirus (sección otras infecciones, 2001-2003)](vigilancia/casos/hantavirus_seccion_otras_infecciones/readme.md) | 2001-2003 | 302 | semanal | edad |  | No sumar: [Enfermedad por hantavirus](vigilancia/casos/hantavirus/readme.md). |
| [Leptospirosis](vigilancia/casos/leptospirosis/readme.md) | 2010-2025 | 302, 302a | semanal | sexo, edad |  |  |
| [Peste](vigilancia/casos/peste/readme.md) | 2008, 2010, 2012-2014, 2016, 2018-2019, 2024 | 302, 302a | semanal | sexo, edad |  |  |
| [Rabia (humana o canina)](vigilancia/casos/rabia_humana_canina/readme.md) | 2001-2003 | 302 | semanal | edad |  | No sumar: [Rabia humana (sección inmunoprevenibles, 2001-2003)](vigilancia/casos/rabia_humana_seccion_inmunoprevenibles/readme.md). |
| [Rabia humana](vigilancia/casos/rabia_humana/readme.md) | 2005-2015, 2017-2025 | 302, 302a | semanal | sexo, edad |  |  |
| [Rabia humana (sección inmunoprevenibles, 2001-2003)](vigilancia/casos/rabia_humana_seccion_inmunoprevenibles/readme.md) | 2001-2003 | 302 | semanal | edad |  | No sumar: [Rabia (humana o canina)](vigilancia/casos/rabia_humana_canina/readme.md). |

### Defunciones

Muertes. 33 datasets.

#### Cáncer

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Muerte por cáncer de cuello uterino](vigilancia/defunciones/muerte_cancer_cuello_uterino/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad | El dataset tiene registros implausibles. |  |
| [Muerte por cáncer de mama](vigilancia/defunciones/muerte_cancer_mama/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad |  |  |
| [Muerte por cáncer de otras localizaciones](vigilancia/defunciones/muerte_cancer_otros/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad |  |  |
| [Muerte por cáncer de próstata](vigilancia/defunciones/muerte_cancer_prostata/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad | El dataset tiene registros implausibles. |  |
| [Muerte por leucemias](vigilancia/defunciones/muerte_leucemias/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad |  |  |

#### Enfermedad no transmisible

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Muerte por EPOC](vigilancia/defunciones/muerte_epoc/readme.md) | 2024-2025 | 302b | mensual | sexo, edad | SOAPS 7.0.1 asigna a esta variable el código interno DX16, "Mortalidad por Accidente Cerebrovascular", el mismo de la muerte por accidente cerebrovascular. Las cifras de los dos datasets son distintas (2024: 118 muertes por EPOC y 436 por accidente cerebrovascular): uno no copia al otro, pero no sabemos cómo se cuenta esta variable. |  |
| [Muerte por accidente cerebrovascular](vigilancia/defunciones/muerte_acv/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad |  |  |
| [Muerte por diabetes](vigilancia/defunciones/muerte_diabetes/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad |  |  |
| [Muerte por enfermedad respiratoria crónica](vigilancia/defunciones/muerte_respiratoria_cronica/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad |  |  |
| [Muerte por infarto agudo de miocardio](vigilancia/defunciones/muerte_infarto/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad |  |  |
| [Muerte por insuficiencia renal](vigilancia/defunciones/muerte_insuficiencia_renal/readme.md) | 2024-2025 | 302b | mensual | sexo, edad |  |  |
| [Muerte por otras enfermedades cardiovasculares](vigilancia/defunciones/muerte_cardiovascular_otras/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad |  |  |

#### Otras causas

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Muertes por otras causas](vigilancia/defunciones/muerte_otras_causas/readme.md) | 2001-2003 | 302 | semanal | lugar |  |  |
| [Otras muertes en mayores de 5 años](vigilancia/defunciones/muerte_mayor_5_otras/readme.md) | 2001-2025 | 302, 302a | semanal | sexo, edad, lugar |  |  |

#### Perinatal e infantil

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Muerte de 28 días a menos de 1 año](vigilancia/defunciones/muerte_posneonatal/readme.md) | 2015-2025 | 302a | semanal | sexo, lugar |  |  |
| [Muerte en menores de 1 año](vigilancia/defunciones/muerte_menor_1/readme.md) | 2004-2014 | 302 | semanal | sexo, lugar |  |  |
| [Muerte en menores de 28 días por asfixia perinatal](vigilancia/defunciones/muerte_neonatal_asfixia/readme.md) | 2015-2025 | 302a | semanal | sexo, lugar |  |  |
| [Muerte en menores de 28 días por prematurez extrema](vigilancia/defunciones/muerte_neonatal_prematurez/readme.md) | 2024-2025 | 302a | semanal | sexo, lugar |  |  |
| [Muerte en menores de 28 días por sepsis](vigilancia/defunciones/muerte_neonatal_sepsis/readme.md) | 2015-2025 | 302a | semanal | sexo, lugar |  |  |
| [Muerte en menores de 5 años por desnutrición aguda grave](vigilancia/defunciones/muerte_menor_5_desnutricion/readme.md) | 2011-2025 | 302, 302a | semanal | sexo, edad, lugar |  |  |
| [Muerte en menores de 5 años por diarrea](vigilancia/defunciones/muerte_menor_5_diarrea/readme.md) | 2001-2025 | 302, 302a | semanal | sexo, edad, lugar |  |  |
| [Muerte en menores de 5 años por neumonía](vigilancia/defunciones/muerte_menor_5_neumonia/readme.md) | 2001-2025 | 302, 302a | semanal | sexo, edad, lugar |  |  |
| [Muerte en menores de 5 años por otras causas](vigilancia/defunciones/muerte_menor_5_otras/readme.md) | 2001-2025 | 302, 302a | semanal | sexo, edad, lugar |  |  |
| [Muerte fetal (óbito) confirmada](vigilancia/defunciones/muerte_fetal/readme.md) | 2015-2025 | 302a | semanal | sexo, lugar |  |  |
| [Muerte neonatal tardía confirmada (7 a 27 días)](vigilancia/defunciones/muerte_neonatal_tardia/readme.md) | 2015-2025 | 302a | semanal | sexo, lugar |  |  |
| [Muerte neonatal temprana (menos de 7 días)](vigilancia/defunciones/muerte_neonatal_temprana/readme.md) | 2001-2014 | 302 | semanal | sexo, lugar |  |  |
| [Muerte neonatal temprana confirmada (0 a 6 días)](vigilancia/defunciones/muerte_neonatal_temprana_confirmada/readme.md) | 2015-2025 | 302a | semanal | sexo, lugar |  |  |

#### Respiratoria

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Sospecha de muerte por COVID-19](vigilancia/defunciones/muerte_covid19_sospecha/readme.md) | 2021-2025 | 302a | semanal | sexo, edad, lugar |  |  |

#### Salud materna

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Muerte de mujer de 10 a 59 años](vigilancia/defunciones/muerte_mujer_edad_fertil/readme.md) | 2019 | 302a | semanal | sexo, edad | El dataset tiene registros implausibles. |  |
| [Muerte materna](vigilancia/defunciones/muerte_materna/readme.md) | 2001-2025 | 302, 302a | semanal | sexo, edad, lugar | Desde 2015 cuenta las muertes maternas notificadas; las confirmadas son otro dataset. |  |
| [Muerte materna confirmada](vigilancia/defunciones/muerte_materna_confirmada/readme.md) | 2015-2020, 2022-2025 | 302a | semanal | sexo, edad, lugar |  |  |

#### Vectorial

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Muerte por malaria (P. falciparum)](vigilancia/defunciones/muerte_malaria/readme.md) | 2001-2004 | 302 | semanal | lugar |  |  |
| [Sospecha de muerte por dengue](vigilancia/defunciones/muerte_dengue_sospecha/readme.md) | 2021-2025 | 302a | semanal | sexo, edad, lugar |  |  |

### Desarrollo infantil

Niñas y niños evaluados, por resultado. 1 datasets.

#### Desarrollo infantil temprano

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Desarrollo infantil temprano](vigilancia/desarrollo_infantil/desarrollo_infantil/readme.md) | 2024-2025 | 302b | mensual | resultado, sexo, edad | Este dataset cuenta por separado 4 categorías de resultado: "adecuado", "rezago grave", "rezago leve" y "rezago moderado". |  |

### Emergencias y desastres

Eventos y personas afectadas. 12 datasets.

#### Emergencia

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Desastres y emergencias](vigilancia/emergencias/emergencia_2004/readme.md) | 2004 | 302 | semanal |  |  |  |
| [Deslizamiento (2010-2014)](vigilancia/emergencias/deslizamiento_sismo_2010_2014/readme.md) | 2010-2014 | 302 | semanal | evento, medida | Este dataset cuenta una sola categoría de evento: "deslizamiento". | Otros periodos: [2015-2023](vigilancia/emergencias/deslizamiento_sismo_2015_2023/readme.md), [2024](vigilancia/emergencias/deslizamiento_sismo_2024/readme.md), [2025](vigilancia/emergencias/deslizamiento_sismo_2025/readme.md). |
| [Deslizamiento (2024)](vigilancia/emergencias/deslizamiento_sismo_2024/readme.md) | 2024 | 302a | semanal | evento, medida | Este dataset cuenta una sola categoría de evento: "deslizamiento". | Otros periodos: [2010-2014](vigilancia/emergencias/deslizamiento_sismo_2010_2014/readme.md), [2015-2023](vigilancia/emergencias/deslizamiento_sismo_2015_2023/readme.md), [2025](vigilancia/emergencias/deslizamiento_sismo_2025/readme.md). |
| [Deslizamiento y sismo (2025)](vigilancia/emergencias/deslizamiento_sismo_2025/readme.md) | 2025 | 302a | semanal | evento, medida | Este dataset cuenta por separado 2 categorías de evento: "deslizamiento" y "sismo o terremoto". | Otros periodos: [2010-2014](vigilancia/emergencias/deslizamiento_sismo_2010_2014/readme.md), [2015-2023](vigilancia/emergencias/deslizamiento_sismo_2015_2023/readme.md), [2024](vigilancia/emergencias/deslizamiento_sismo_2024/readme.md). |
| [Deslizamiento, sismo o terremoto (2015-2023)](vigilancia/emergencias/deslizamiento_sismo_2015_2023/readme.md) | 2015-2023 | 302a | semanal | evento, medida | Este dataset cuenta una sola categoría de evento: "deslizamiento o sismo". | Otros periodos: [2010-2014](vigilancia/emergencias/deslizamiento_sismo_2010_2014/readme.md), [2024](vigilancia/emergencias/deslizamiento_sismo_2024/readme.md), [2025](vigilancia/emergencias/deslizamiento_sismo_2025/readme.md). |
| [Helada, granizo o nevada (2010-2023)](vigilancia/emergencias/helada_granizo_nevada_2010_2023/readme.md) | 2010-2023 | 302, 302a | semanal | medida | Este dataset no separa por evento. | Otros periodos: [2024](vigilancia/emergencias/helada_granizo_nevada_2024/readme.md), [2025](vigilancia/emergencias/helada_granizo_nevada_2025/readme.md). |
| [Helada, granizo y nevada (2024)](vigilancia/emergencias/helada_granizo_nevada_2024/readme.md) | 2024 | 302a | semanal | evento, medida | Este dataset cuenta por separado 2 categorías de evento: "granizo" y "nevada". | Otros periodos: [2010-2023](vigilancia/emergencias/helada_granizo_nevada_2010_2023/readme.md), [2025](vigilancia/emergencias/helada_granizo_nevada_2025/readme.md). |
| [Helada, granizo y nevada (2025)](vigilancia/emergencias/helada_granizo_nevada_2025/readme.md) | 2025 | 302a | semanal | evento, medida | Este dataset cuenta por separado 3 categorías de evento: "granizo", "heladas" y "nevada". | Otros periodos: [2010-2023](vigilancia/emergencias/helada_granizo_nevada_2010_2023/readme.md), [2024](vigilancia/emergencias/helada_granizo_nevada_2024/readme.md). |
| [Incendio](vigilancia/emergencias/incendio/readme.md) | 2010-2025 | 302, 302a | semanal | medida |  |  |
| [Inundación](vigilancia/emergencias/inundacion/readme.md) | 2010-2025 | 302, 302a | semanal | medida |  |  |
| [Otros eventos de excepción](vigilancia/emergencias/emergencia_otra/readme.md) | 2010-2025 | 302, 302a | semanal | medida |  |  |
| [Riada](vigilancia/emergencias/riada/readme.md) | 2010-2025 | 302, 302a | semanal | medida |  |  |

### Estado nutricional

Personas evaluadas, por resultado. 9 datasets.

#### Clasificación nutricional (a a f)

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Clasificación nutricional A a F](vigilancia/estado_nutricional/clasificacion_nutricional_2001/readme.md) | 2001-2004 | 302 | semanal | clasificación | Este dataset cuenta por separado 5 categorías de clasificación: "A y B", "C", "D", "E" y "F". |  |

#### Estado nutricional de la embarazada

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Embarazada desnutrida](vigilancia/estado_nutricional/embarazada_desnutrida/readme.md) | 2007-2018, 2020-2025 | 302, 302b | semanal y mensual | sexo, edad, embarazo o puerperio |  |  |

#### Peso

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Peso para la edad (2005-2006)](vigilancia/estado_nutricional/peso_2005_2006/readme.md) | 2005-2006 | 302 | semanal | clasificación, sexo, edad | Este dataset cuenta por separado 5 categorías de clasificación: "desnutrición grave", "desnutrición leve", "desnutrición moderada", "normal" y "sobrepeso". | Otros periodos: [2007](vigilancia/estado_nutricional/peso_2007/readme.md), [2008-2014](vigilancia/estado_nutricional/peso_2008_2014/readme.md), [2015-2025](vigilancia/estado_nutricional/peso_2015_2025/readme.md). |
| [Peso para la edad (2008-2014)](vigilancia/estado_nutricional/peso_2008_2014/readme.md) | 2008-2014 | 302 | semanal | clasificación, sexo, edad, embarazo o puerperio | Este dataset cuenta por separado 6 categorías de clasificación: "desnutrición grave", "desnutrición leve", "desnutrición moderada", "normal", "obesidad" y "sobrepeso". | Otros periodos: [2005-2006](vigilancia/estado_nutricional/peso_2005_2006/readme.md), [2007](vigilancia/estado_nutricional/peso_2007/readme.md), [2015-2025](vigilancia/estado_nutricional/peso_2015_2025/readme.md). |
| [Peso para la edad (2015-2025)](vigilancia/estado_nutricional/peso_2015_2025/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | clasificación, sexo, edad, embarazo o puerperio | Este dataset cuenta por separado 5 categorías de clasificación: "desnutrición grave", "desnutrición moderada", "normal", "obesidad" y "sobrepeso". | Otros periodos: [2005-2006](vigilancia/estado_nutricional/peso_2005_2006/readme.md), [2007](vigilancia/estado_nutricional/peso_2007/readme.md), [2008-2014](vigilancia/estado_nutricional/peso_2008_2014/readme.md). |

#### Peso para la edad

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Peso para la edad (2007)](vigilancia/estado_nutricional/peso_2007/readme.md) | 2007 | 302 | semanal | clasificación, sexo, edad | Este dataset cuenta por separado 6 categorías de clasificación: "desnutrición grave", "desnutrición leve", "desnutrición moderada", "normal", "nutrición superior" y "peso bajo (moderado y grave)". "Peso bajo (moderado y grave)" está junto a "desnutrición moderada" y "desnutrición grave". | Otros periodos: [2005-2006](vigilancia/estado_nutricional/peso_2005_2006/readme.md), [2008-2014](vigilancia/estado_nutricional/peso_2008_2014/readme.md), [2015-2025](vigilancia/estado_nutricional/peso_2015_2025/readme.md). |

#### Talla para la edad

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Talla baja (moderada y grave) (2007)](vigilancia/estado_nutricional/talla_2007/readme.md) | 2007 | 302 | semanal | clasificación, sexo, edad | Este dataset cuenta una sola categoría de clasificación: "baja moderada y grave". | Otros periodos: [2005-2006](vigilancia/estado_nutricional/talla_2005_2006/readme.md), [2008-2025](vigilancia/estado_nutricional/talla_2008_2025/readme.md). |
| [Talla para la edad (2005-2006)](vigilancia/estado_nutricional/talla_2005_2006/readme.md) | 2005-2006 | 302 | semanal | clasificación, sexo, edad | Este dataset cuenta por separado 4 categorías de clasificación: "baja grave", "baja leve", "baja moderada" y "normal". | Otros periodos: [2007](vigilancia/estado_nutricional/talla_2007/readme.md), [2008-2025](vigilancia/estado_nutricional/talla_2008_2025/readme.md). |
| [Talla para la edad (2008-2025)](vigilancia/estado_nutricional/talla_2008_2025/readme.md) | 2008-2009, 2015-2018, 2020-2025 | 302, 302b | semanal y mensual | clasificación, sexo, edad | Este dataset cuenta por separado 2 categorías de clasificación: "baja" y "normal". | Otros periodos: [2005-2006](vigilancia/estado_nutricional/talla_2005_2006/readme.md), [2007](vigilancia/estado_nutricional/talla_2007/readme.md). |

### Factores de riesgo

Personas con un factor de riesgo. 4 datasets.

#### Factor de riesgo

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Abuso de alcohol](vigilancia/factores_riesgo/abuso_alcohol/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad |  |  |
| [Hábito de fumar](vigilancia/factores_riesgo/tabaquismo/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad |  |  |
| [Sedentarismo](vigilancia/factores_riesgo/sedentarismo/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad |  |  |
| [Sobrepeso](vigilancia/factores_riesgo/sobrepeso/readme.md) | 2015-2018, 2020-2025 | 302b | mensual | sexo, edad |  |  |

## Producción de servicios

360 datasets de los formularios 301, 301a y 301b.

### Anticoncepción y prevención del cáncer

Anticoncepción y detección de cáncer de cuello uterino y de mama. 23 datasets.

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Abandono de método anticonceptivo](servicios/anticoncepcion_prevencion_cancer/abandono_de_metodo_anticonceptivo/readme.md) | 2021-2025 | 301a | mensual | edad |  |  |
| [Anticoncepción quirúrgica voluntaria](servicios/anticoncepcion_prevencion_cancer/anticoncepcion_quirurgica/readme.md) | 2001-2025 | 301, 301a | mensual | sexo, edad |  |  |
| [DIU's retirados](servicios/anticoncepcion_prevencion_cancer/diu_s_retirados/readme.md) | 2021-2025 | 301a | mensual | edad |  |  |
| [Implantes retirados](servicios/anticoncepcion_prevencion_cancer/implantes_retirados/readme.md) | 2021-2025 | 301a | mensual | edad |  |  |
| [Insumos anticonceptivos entregados o insertados (2001-2014)](servicios/anticoncepcion_prevencion_cancer/insumos_anticonceptivos_2001_2014/readme.md) | 2001-2014 | 301 | mensual | método | Este dataset cuenta por separado 3 categorías de método: "DIU", "condón masculino" y "píldora". | Otros periodos: [2015-2025](servicios/anticoncepcion_prevencion_cancer/insumos_anticonceptivos_2015_2025/readme.md). |
| [Insumos anticonceptivos entregados o insertados (2015-2025)](servicios/anticoncepcion_prevencion_cancer/insumos_anticonceptivos_2015_2025/readme.md) | 2015-2025 | 301a | mensual | método, edad | Este dataset cuenta por separado 4 categorías de método: "DIU", "condón masculino", "implante subdérmico" y "píldora". | Otros periodos: [2001-2014](servicios/anticoncepcion_prevencion_cancer/insumos_anticonceptivos_2001_2014/readme.md). |
| [Inyectables trimestrales suministrados](servicios/anticoncepcion_prevencion_cancer/inyectables_trimestrales_suministrados/readme.md) | 2001-2025 | 301, 301a | mensual | edad |  |  |
| [Mujeres con IVAA](servicios/anticoncepcion_prevencion_cancer/mujeres_con_ivaa/readme.md) | 2015-2025 | 301a | mensual | edad |  |  |
| [Mujeres con IVAA positivos](servicios/anticoncepcion_prevencion_cancer/mujeres_con_ivaa_positivos/readme.md) | 2015-2025 | 301a | mensual | edad |  |  |
| [Mujeres con IVAA positivos tratadas](servicios/anticoncepcion_prevencion_cancer/mujeres_con_ivaa_positivos_tratadas/readme.md) | 2015-2025 | 301a | mensual | edad |  |  |
| [Mujeres con estudios mamaográficos positivos](servicios/anticoncepcion_prevencion_cancer/mujeres_con_estudios_mamaograficos_positivos/readme.md) | 2015-2025 | 301a | mensual | edad |  |  |
| [Mujeres con exámen clínico de mama positivos (sospechoso de nódulo neoplásico)](servicios/anticoncepcion_prevencion_cancer/mujeres_con_examen_clinico_de_mama_positivos_sospechoso_de_n/readme.md) | 2015-2025 | 301a | mensual | edad |  |  |
| [Mujeres con muestra de citologia cervico vaginal](servicios/anticoncepcion_prevencion_cancer/mujeres_con_muestras_de_pap_tomadas/readme.md) | 2001-2025 | 301, 301a | mensual | edad |  |  |
| [Mujeres con píldora anticonceptiva oral de emergencia](servicios/anticoncepcion_prevencion_cancer/mujeres_con_pildora_anticonceptiva_oral_de_emergencia/readme.md) | 2010-2025 | 301, 301a | mensual | edad |  |  |
| [Mujeres con resultados de PAP positivos](servicios/anticoncepcion_prevencion_cancer/mujeres_con_resultados_de_pap_positivos/readme.md) | 2015-2025 | 301a | mensual | edad |  |  |
| [Mujeres con resultados de PAP positivos tratadas](servicios/anticoncepcion_prevencion_cancer/mujeres_con_resultados_de_pap_positivos_tratadas/readme.md) | 2015-2025 | 301a | mensual | edad |  |  |
| [Mujeres después de aborto que egresaron con método moderno](servicios/anticoncepcion_prevencion_cancer/mujeres_despues_de_aborto_que_egresaron_con_metodo_moderno/readme.md) | 2021-2025 | 301a | mensual | edad |  |  |
| [Mujeres post parto que egresaron con método moderno](servicios/anticoncepcion_prevencion_cancer/mujeres_post_parto_que_egresaron_con_metodo_moderno/readme.md) | 2021-2025 | 301a | mensual | edad |  |  |
| [Mujeres que recibieron orientación en anticoncepción](servicios/anticoncepcion_prevencion_cancer/mujeres_que_recibieron_orientacion_en_anticoncepcion/readme.md) | 2021-2025 | 301a | mensual | edad |  | [Personas que recibieron orientación en anticoncepción](servicios/anticoncepcion_prevencion_cancer/personas_que_recibieron_orientacion_en_anticoncepcion/readme.md), [Varones que recibieron orientación en anticoncepción](servicios/anticoncepcion_prevencion_cancer/varones_que_recibieron_orientacion_en_anticoncepcion/readme.md). |
| [Personas que recibieron orientación en anticoncepción](servicios/anticoncepcion_prevencion_cancer/personas_que_recibieron_orientacion_en_anticoncepcion/readme.md) | 2001-2020 | 301, 301a | mensual | edad |  | [Mujeres que recibieron orientación en anticoncepción](servicios/anticoncepcion_prevencion_cancer/mujeres_que_recibieron_orientacion_en_anticoncepcion/readme.md), [Varones que recibieron orientación en anticoncepción](servicios/anticoncepcion_prevencion_cancer/varones_que_recibieron_orientacion_en_anticoncepcion/readme.md). |
| [Usuarias de anticoncepción (2001-2014)](servicios/anticoncepcion_prevencion_cancer/usuarias_anticoncepcion_2001_2014/readme.md) | 2001-2014 | 301 | mensual | método, usuaria nueva o continua | Este dataset cuenta por separado 5 categorías de método: "DIU", "condón masculino", "inyectable trimestral", "métodos naturales" y "píldora". Este dataset cuenta por separado 2 categorías de usuaria nueva o continua: "continua" y "nueva". | Otros periodos: [2015-2025](servicios/anticoncepcion_prevencion_cancer/usuarias_anticoncepcion_2015_2025/readme.md). |
| [Usuarias de anticoncepción (2015-2025)](servicios/anticoncepcion_prevencion_cancer/usuarias_anticoncepcion_2015_2025/readme.md) | 2015-2025 | 301a | mensual | método, usuaria nueva o continua, edad | Este dataset cuenta por separado 7 categorías de método: "DIU", "condón femenino", "condón masculino", "implante subdérmico", "inyectable trimestral", "métodos naturales" y "píldora". Este dataset cuenta por separado 2 categorías de usuaria nueva o continua: "continua" y "nueva". | Otros periodos: [2001-2014](servicios/anticoncepcion_prevencion_cancer/usuarias_anticoncepcion_2001_2014/readme.md). |
| [Varones que recibieron orientación en anticoncepción](servicios/anticoncepcion_prevencion_cancer/varones_que_recibieron_orientacion_en_anticoncepcion/readme.md) | 2021-2025 | 301a | mensual | edad |  | [Personas que recibieron orientación en anticoncepción](servicios/anticoncepcion_prevencion_cancer/personas_que_recibieron_orientacion_en_anticoncepcion/readme.md), [Mujeres que recibieron orientación en anticoncepción](servicios/anticoncepcion_prevencion_cancer/mujeres_que_recibieron_orientacion_en_anticoncepcion/readme.md). |

### Cirugía

Cirugías, anestesias y quirófanos. 20 datasets.

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Anestesias generales](servicios/cirugia/anestesias_generales/readme.md) | 2015-2025 | 301b | mensual | sexo |  | [Anestesias generales, locales o regionales](servicios/cirugia/anestesias_generales_locales_o_regionales/readme.md), [Anestesias generales y regionales](servicios/cirugia/anestesias_generales_y_regionales/readme.md), [Anestesias regionales](servicios/cirugia/anestesias_regionales/readme.md). |
| [Anestesias generales y regionales](servicios/cirugia/anestesias_generales_y_regionales/readme.md) | 2008-2014 | 301 | mensual | sexo |  | [Anestesias generales, locales o regionales](servicios/cirugia/anestesias_generales_locales_o_regionales/readme.md), [Anestesias generales](servicios/cirugia/anestesias_generales/readme.md), [Anestesias regionales](servicios/cirugia/anestesias_regionales/readme.md). |
| [Anestesias generales, locales o regionales](servicios/cirugia/anestesias_generales_locales_o_regionales/readme.md) | 2001-2007 | 301 | mensual |  |  | [Anestesias generales y regionales](servicios/cirugia/anestesias_generales_y_regionales/readme.md), [Anestesias generales](servicios/cirugia/anestesias_generales/readme.md), [Anestesias regionales](servicios/cirugia/anestesias_regionales/readme.md). |
| [Anestesias locales (formulario 301b)](servicios/cirugia/anestesias_locales_301b/readme.md) | 2015-2023 | 301b | mensual | sexo |  | Formulario 301a: [Anestesias locales realizadas](servicios/cirugia/anestesias_locales/readme.md). |
| [Anestesias locales realizadas](servicios/cirugia/anestesias_locales/readme.md) | 2024-2025 | 301a | mensual | sexo |  | Formulario 301b: [Anestesias locales (formulario 301b)](servicios/cirugia/anestesias_locales_301b/readme.md). |
| [Anestesias regionales](servicios/cirugia/anestesias_regionales/readme.md) | 2015-2025 | 301b | mensual | sexo |  | [Anestesias generales, locales o regionales](servicios/cirugia/anestesias_generales_locales_o_regionales/readme.md), [Anestesias generales y regionales](servicios/cirugia/anestesias_generales_y_regionales/readme.md), [Anestesias generales](servicios/cirugia/anestesias_generales/readme.md). |
| [Cirugias de emergencia realizadas en el periodo](servicios/cirugia/cirugias_de_emergencia_realizadas_en_el_periodo/readme.md) | 2024-2025 | 301b | mensual | sexo, servicio |  |  |
| [Cirugias mayores](servicios/cirugia/cirugias_mayores/readme.md) | 2015-2025 | 301b | mensual | sexo |  | [Cirugías medianas y mayores](servicios/cirugia/cirugias_medianas_y_mayores/readme.md), [Cirugias medianas](servicios/cirugia/cirugias_medianas/readme.md). |
| [Cirugias medianas](servicios/cirugia/cirugias_medianas/readme.md) | 2015-2025 | 301b | mensual | sexo |  | [Cirugías medianas y mayores](servicios/cirugia/cirugias_medianas_y_mayores/readme.md), [Cirugias mayores](servicios/cirugia/cirugias_mayores/readme.md). |
| [Cirugias menores (formulario 301b)](servicios/cirugia/cirugias_menores_301b/readme.md) | 2015-2023 | 301b | mensual | sexo |  | Formulario 301a: [Cirugias menores realizadas](servicios/cirugia/cirugias_menores/readme.md). |
| [Cirugias menores realizadas](servicios/cirugia/cirugias_menores/readme.md) | 2024-2025 | 301a | mensual | sexo |  | Formulario 301b: [Cirugias menores (formulario 301b)](servicios/cirugia/cirugias_menores_301b/readme.md). |
| [Cirugias programadas en el periodo](servicios/cirugia/cirugias_programadas_en_el_periodo/readme.md) | 2024-2025 | 301b | mensual | sexo |  |  |
| [Cirugias realizadas en el periodo](servicios/cirugia/cirugias_realizadas_en_el_periodo/readme.md) | 2024-2025 | 301b | mensual | sexo |  |  |
| [Cirugías medianas y mayores](servicios/cirugia/cirugias_medianas_y_mayores/readme.md) | 2001-2014 | 301 | mensual | sexo |  | [Cirugias mayores](servicios/cirugia/cirugias_mayores/readme.md), [Cirugias medianas](servicios/cirugia/cirugias_medianas/readme.md). |
| [Complicaciones anestesicas](servicios/cirugia/complicaciones_anestesicas/readme.md) | 2015-2025 | 301b | mensual | sexo |  |  |
| [Complicaciones postquirurgicas](servicios/cirugia/complicaciones_postquirurgicas/readme.md) | 2015-2025 | 301b | mensual | sexo |  |  |
| [Quirofanos funcionales en el periodo](servicios/cirugia/quirofanos_funcionales_en_el_periodo/readme.md) | 2024-2025 | 301b | mensual |  |  |  |
| [Quirofanos instalados](servicios/cirugia/quirofanos_instalados/readme.md) | 2024-2025 | 301b | mensual |  |  |  |
| [Quirofanos para cirugia de emergencia en el periodo](servicios/cirugia/quirofanos_para_cirugia_de_emergencia_en_el_periodo/readme.md) | 2024-2025 | 301b | mensual |  |  |  |
| [Quirófanos funcionales para cirugia en el periodo](servicios/cirugia/quirofanos_funcionales_para_cirugia_en_el_periodo/readme.md) | 2024-2025 | 301b | mensual |  |  |  |

### Consultas

Consultas externas, de emergencia, interconsultas y telesalud. 10 datasets.

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Consulta externa](servicios/consultas/consulta_externa/readme.md) | 2001-2025 | 301, 301a | mensual | sexo, edad, nuevo o repetido |  |  |
| [Consulta externa por especialidad](servicios/consultas/consulta_externa_por_especialidad/readme.md) | 2015-2025 | 301b | mensual | sexo, edad, nuevo o repetido, especialidad |  |  |
| [Consulta por emergencia](servicios/consultas/consulta_por_emergencia/readme.md) | 2015-2025 | 301b | mensual | sexo, edad, especialidad, servicio | Hasta 2023 el tablero registra estas consultas como variables por edad del grupo "Emergencia" del 301b; el instructivo del 301b (2024) dice que son las consultas del servicio de emergencia. Desde 2024 son la variable "Consulta por emergencia", con la edad en las columnas. |  |
| [Defunciones en emergencias a partir de las 48 hrs](servicios/consultas/defunciones_en_emergencias_a_partir_de_las_48_hrs/readme.md) | 2024-2025 | 301b | mensual | sexo, edad |  |  |
| [Defunciones en emergencias antes de las 48 hrs](servicios/consultas/defunciones_en_emergencias_antes_de_las_48_hrs/readme.md) | 2024-2025 | 301b | mensual | sexo, edad |  |  |
| [Interconsultas](servicios/consultas/interconsultas/readme.md) | 2024-2025 | 301b | mensual | sexo, edad, servicio |  |  |
| [Teleconsultas](servicios/consultas/teleconsultas/readme.md) | 2024-2025 | 301a | mensual | sexo, edad, nuevo o repetido |  |  |
| [Teledispositivos](servicios/consultas/teledispositivos/readme.md) | 2024-2025 | 301a | mensual | dispositivo, sexo, edad | Este dataset cuenta por separado 7 categorías de dispositivo: "colposcopio", "ecógrafo", "electrocardiógrafo", "espirómetro", "monitor de signos vitales", "oftalmoscopio" y "otoscopio". |  |
| [Teleinterconsultas de respuesta efectivizadas](servicios/consultas/teleinterconsultas_de_respuesta_efectivizadas/readme.md) | 2024-2025 | 301a | mensual | sexo, edad |  |  |
| [Teleinterconsultas generadas](servicios/consultas/teleinterconsultas_generadas/readme.md) | 2024-2025 | 301a | mensual | sexo, edad, nuevo o repetido |  |  |

### Control de enfermedades

Tuberculosis, malaria, chagas, leishmaniasis, vih, rabia y otras. 76 datasets.

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Antirrábica canina](servicios/control_enfermedades/antirrabica_canina/readme.md) | 2001-2009 | 301 | mensual |  |  |  |
| [Antirrábica en humano](servicios/control_enfermedades/antirrabica_en_humano/readme.md) | 2010-2014 | 301 | mensual | lugar |  |  |
| [Antirrábica en perros y gatos](servicios/control_enfermedades/antirrabica_en_perros_y_gatos/readme.md) | 2010-2014 | 301 | mensual | lugar |  |  |
| [Antirrábica humana esquema completo](servicios/control_enfermedades/antirrabica_humana_esquema_completo/readme.md) | 2001-2014 | 301 | mensual | lugar |  |  |
| [Chagas: positivos en el mes niños RN a nueve meses](servicios/control_enfermedades/chagas_positivos_en_el_mes_ninos_rn_a_nueve_meses/readme.md) | 2007 | 301 | mensual |  |  |  |
| [Chagas: positivos en el mes niños menores de 5 años](servicios/control_enfermedades/chagas_positivos_en_el_mes_ninos_menores_de_5_anos/readme.md) | 2007 | 301 | mensual |  |  |  |
| [Chagas: viviendas evaluadas](servicios/control_enfermedades/chagas_viviendas_evaluadas/readme.md) | 2007-2025 | 301, 301a | mensual |  |  |  |
| [Chagas: viviendas positivas](servicios/control_enfermedades/chagas_viviendas_positivas/readme.md) | 2007-2025 | 301, 301a | mensual |  |  |  |
| [Chagas: viviendas programadas para rociado](servicios/control_enfermedades/chagas_viviendas_programadas_para_rociado/readme.md) | 2001-2003 | 301 | mensual |  |  |  |
| [Chagas: viviendas rociadas](servicios/control_enfermedades/chagas_viviendas_rociadas/readme.md) | 2001-2006, 2010-2025 | 301, 301a | mensual |  |  |  |
| [Chagas: viviendas visitadas por agente comunitario](servicios/control_enfermedades/chagas_viviendas_visitadas_por_agente_comunitario/readme.md) | 2005-2006 | 301 | mensual |  |  |  |
| [Dengue: actividades realizadas con la comunidad](servicios/control_enfermedades/dengue_actividades_realizadas_con_la_comunidad/readme.md) | 2007-2009 | 301 | mensual |  |  |  |
| [Dengue: viviendas evaluadas entomológicamente](servicios/control_enfermedades/dengue_viviendas_evaluadas_entomologicamente/readme.md) | 2010-2014 | 301 | mensual |  |  |  |
| [Dengue: viviendas positivas](servicios/control_enfermedades/dengue_viviendas_positivas/readme.md) | 2010-2014 | 301 | mensual |  |  |  |
| [Malaria: casos confirmados](servicios/control_enfermedades/malaria_casos_confirmados/readme.md) | 2007-2014 | 301 | mensual | sexo, especie |  |  |
| [Malaria: muestras hemáticas tomadas](servicios/control_enfermedades/malaria_muestras_hematicas_tomadas/readme.md) | 2007-2014 | 301 | mensual | sexo, especie |  | [Malaria: muestras tomadas por agente comunario](servicios/control_enfermedades/malaria_muestras_tomadas_por_agente_comunario/readme.md), [Malaria: muestras tomadas por personal de salud](servicios/control_enfermedades/malaria_muestras_tomadas_por_personal_de_salud/readme.md). |
| [Malaria: muestras tomadas por agente comunario](servicios/control_enfermedades/malaria_muestras_tomadas_por_agente_comunario/readme.md) | 2005-2006 | 301 | mensual |  |  | [Malaria: muestras tomadas por personal de salud](servicios/control_enfermedades/malaria_muestras_tomadas_por_personal_de_salud/readme.md), [Malaria: muestras hemáticas tomadas](servicios/control_enfermedades/malaria_muestras_hematicas_tomadas/readme.md). |
| [Malaria: muestras tomadas por personal de salud](servicios/control_enfermedades/malaria_muestras_tomadas_por_personal_de_salud/readme.md) | 2005-2006 | 301 | mensual |  |  | [Malaria: muestras tomadas por agente comunario](servicios/control_enfermedades/malaria_muestras_tomadas_por_agente_comunario/readme.md), [Malaria: muestras hemáticas tomadas](servicios/control_enfermedades/malaria_muestras_hematicas_tomadas/readme.md). |
| [Malaria: tratamientos específicos dispensados](servicios/control_enfermedades/malaria_tratamientos_especificos_dispensados/readme.md) | 2010-2014 | 301 | mensual | sexo, especie |  | [Malaria: tratamientos específicos entregados](servicios/control_enfermedades/malaria_tratamientos_especificos/readme.md). |
| [Malaria: tratamientos específicos entregados](servicios/control_enfermedades/malaria_tratamientos_especificos/readme.md) | 2015-2025 | 301a | mensual | sexo, edad, embarazo o puerperio, especie | El tablero no nombra estas variables: son columnas por edad del grupo "Malaria" del 301a. Según el instructivo del 301a (2024), cuentan los tratamientos específicos entregados a pacientes confirmados. | [Malaria: tratamientos específicos dispensados](servicios/control_enfermedades/malaria_tratamientos_especificos_dispensados/readme.md). |
| [Malaria: tratamientos iniciados antes de las 48 horas](servicios/control_enfermedades/malaria_tratamientos_iniciados_antes_de_las_48_horas/readme.md) | 2010-2014 | 301 | mensual | sexo, especie |  |  |
| [Malaria: tratamientos iniciados en el mes](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes/readme.md) | 2001-2003 | 301 | mensual |  |  | [Malaria: tratamientos iniciados en el mes para p.falciparu](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_para_p_falciparu/readme.md), [Malaria: tratamientos iniciados en el mes para p.vivax](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_para_p_vivax/readme.md), [Malaria: tratamientos iniciados en el mes por agente comun](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_por_agente_comun/readme.md), [Malaria: tratamientos iniciados en el mes por personal de](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_por_personal_de/readme.md), [Malaria: tratamientos iniciados por sospecha](servicios/control_enfermedades/malaria_tratamientos_iniciados_por_sospecha/readme.md). |
| [Malaria: tratamientos iniciados en el mes para p.falciparu](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_para_p_falciparu/readme.md) | 2004 | 301 | mensual |  |  | [Malaria: tratamientos iniciados en el mes](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes/readme.md), [Malaria: tratamientos iniciados en el mes para p.vivax](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_para_p_vivax/readme.md), [Malaria: tratamientos iniciados en el mes por agente comun](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_por_agente_comun/readme.md), [Malaria: tratamientos iniciados en el mes por personal de](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_por_personal_de/readme.md), [Malaria: tratamientos iniciados por sospecha](servicios/control_enfermedades/malaria_tratamientos_iniciados_por_sospecha/readme.md). |
| [Malaria: tratamientos iniciados en el mes para p.vivax](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_para_p_vivax/readme.md) | 2004 | 301 | mensual |  |  | [Malaria: tratamientos iniciados en el mes](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes/readme.md), [Malaria: tratamientos iniciados en el mes para p.falciparu](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_para_p_falciparu/readme.md), [Malaria: tratamientos iniciados en el mes por agente comun](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_por_agente_comun/readme.md), [Malaria: tratamientos iniciados en el mes por personal de](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_por_personal_de/readme.md), [Malaria: tratamientos iniciados por sospecha](servicios/control_enfermedades/malaria_tratamientos_iniciados_por_sospecha/readme.md). |
| [Malaria: tratamientos iniciados en el mes por agente comun](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_por_agente_comun/readme.md) | 2005-2006 | 301 | mensual |  |  | [Malaria: tratamientos iniciados en el mes](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes/readme.md), [Malaria: tratamientos iniciados en el mes para p.falciparu](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_para_p_falciparu/readme.md), [Malaria: tratamientos iniciados en el mes para p.vivax](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_para_p_vivax/readme.md), [Malaria: tratamientos iniciados en el mes por personal de](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_por_personal_de/readme.md), [Malaria: tratamientos iniciados por sospecha](servicios/control_enfermedades/malaria_tratamientos_iniciados_por_sospecha/readme.md). |
| [Malaria: tratamientos iniciados en el mes por personal de](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_por_personal_de/readme.md) | 2005-2006 | 301 | mensual |  |  | [Malaria: tratamientos iniciados en el mes](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes/readme.md), [Malaria: tratamientos iniciados en el mes para p.falciparu](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_para_p_falciparu/readme.md), [Malaria: tratamientos iniciados en el mes para p.vivax](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_para_p_vivax/readme.md), [Malaria: tratamientos iniciados en el mes por agente comun](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_por_agente_comun/readme.md), [Malaria: tratamientos iniciados por sospecha](servicios/control_enfermedades/malaria_tratamientos_iniciados_por_sospecha/readme.md). |
| [Malaria: tratamientos iniciados por sospecha](servicios/control_enfermedades/malaria_tratamientos_iniciados_por_sospecha/readme.md) | 2007-2014 | 301 | mensual | sexo, especie |  | [Malaria: tratamientos iniciados en el mes](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes/readme.md), [Malaria: tratamientos iniciados en el mes para p.falciparu](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_para_p_falciparu/readme.md), [Malaria: tratamientos iniciados en el mes para p.vivax](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_para_p_vivax/readme.md), [Malaria: tratamientos iniciados en el mes por agente comun](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_por_agente_comun/readme.md), [Malaria: tratamientos iniciados en el mes por personal de](servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_por_personal_de/readme.md). |
| [Malaria: tratamientos terminados en el mes](servicios/control_enfermedades/malaria_tratamientos_terminados_en_el_mes/readme.md) | 2001-2003 | 301 | mensual |  |  | [Malaria: tratamientos terminados en el mes para p.falcipar](servicios/control_enfermedades/malaria_tratamientos_terminados_en_el_mes_para_p_falcipar/readme.md), [Malaria: tratamientos terminados en el mes para p.vivax](servicios/control_enfermedades/malaria_tratamientos_terminados_en_el_mes_para_p_vivax/readme.md). |
| [Malaria: tratamientos terminados en el mes para p.falcipar](servicios/control_enfermedades/malaria_tratamientos_terminados_en_el_mes_para_p_falcipar/readme.md) | 2004 | 301 | mensual |  |  | [Malaria: tratamientos terminados en el mes](servicios/control_enfermedades/malaria_tratamientos_terminados_en_el_mes/readme.md), [Malaria: tratamientos terminados en el mes para p.vivax](servicios/control_enfermedades/malaria_tratamientos_terminados_en_el_mes_para_p_vivax/readme.md). |
| [Malaria: tratamientos terminados en el mes para p.vivax](servicios/control_enfermedades/malaria_tratamientos_terminados_en_el_mes_para_p_vivax/readme.md) | 2004 | 301 | mensual |  |  | [Malaria: tratamientos terminados en el mes](servicios/control_enfermedades/malaria_tratamientos_terminados_en_el_mes/readme.md), [Malaria: tratamientos terminados en el mes para p.falcipar](servicios/control_enfermedades/malaria_tratamientos_terminados_en_el_mes_para_p_falcipar/readme.md). |
| [Malaria: tratatamientos iniciados por sospecha](servicios/control_enfermedades/malaria_tratatamientos_iniciados_por_sospecha/readme.md) | 2001-2003 | 301 | mensual |  |  |  |
| [Malaria: viviendas rociadas](servicios/control_enfermedades/malaria_viviendas_rociadas/readme.md) | 2001-2003 | 301 | mensual |  |  | [Malaria: viviendas rociadas por agente comunario](servicios/control_enfermedades/malaria_viviendas_rociadas_por_agente_comunario/readme.md), [Malaria: viviendas rociadas por personal de salud](servicios/control_enfermedades/malaria_viviendas_rociadas_por_personal_de_salud/readme.md). |
| [Malaria: viviendas rociadas por agente comunario](servicios/control_enfermedades/malaria_viviendas_rociadas_por_agente_comunario/readme.md) | 2005-2006 | 301 | mensual |  |  | [Malaria: viviendas rociadas](servicios/control_enfermedades/malaria_viviendas_rociadas/readme.md), [Malaria: viviendas rociadas por personal de salud](servicios/control_enfermedades/malaria_viviendas_rociadas_por_personal_de_salud/readme.md). |
| [Malaria: viviendas rociadas por personal de salud](servicios/control_enfermedades/malaria_viviendas_rociadas_por_personal_de_salud/readme.md) | 2005-2006 | 301 | mensual |  |  | [Malaria: viviendas rociadas](servicios/control_enfermedades/malaria_viviendas_rociadas/readme.md), [Malaria: viviendas rociadas por agente comunario](servicios/control_enfermedades/malaria_viviendas_rociadas_por_agente_comunario/readme.md). |
| [Mujeres con prueba rapida VIH en el parto o puertperio](servicios/control_enfermedades/mujeres_con_prueba_rapida_vih_en_el_parto_o_puertperio/readme.md) | 2024-2025 | 301a | mensual | sexo |  |  |
| [Mujeres embarazadas con prueba rápida VIH (1ra prueba)](servicios/control_enfermedades/mujeres_embarazadas_con_prueba_rapida_vih_1ra_prueba/readme.md) | 2024-2025 | 301a | mensual | sexo |  | [VIH: mujeres embarazadas con prueba rápida](servicios/control_enfermedades/vih_mujeres_embarazadas_con_prueba_rapida/readme.md), [Mujeres embarazadas con prueba rápida VIH (2da prueba)](servicios/control_enfermedades/mujeres_embarazadas_con_prueba_rapida_vih_2da_prueba/readme.md). |
| [Mujeres embarazadas con prueba rápida VIH (2da prueba)](servicios/control_enfermedades/mujeres_embarazadas_con_prueba_rapida_vih_2da_prueba/readme.md) | 2024-2025 | 301a | mensual | sexo |  | [VIH: mujeres embarazadas con prueba rápida](servicios/control_enfermedades/vih_mujeres_embarazadas_con_prueba_rapida/readme.md), [Mujeres embarazadas con prueba rápida VIH (1ra prueba)](servicios/control_enfermedades/mujeres_embarazadas_con_prueba_rapida_vih_1ra_prueba/readme.md). |
| [Ofidios: tratamientos inciados con suero antiofidico](servicios/control_enfermedades/ofidios_tratamientos_inciados_con_suero_antiofidico/readme.md) | 2024-2025 | 301a | mensual | sexo |  |  |
| [Ofidios: tratamientos iniciados con suero antiaracnido](servicios/control_enfermedades/ofidios_tratamientos_iniciados_con_suero_antiaracnido/readme.md) | 2024-2025 | 301a | mensual | sexo |  |  |
| [Ofidios: tratamientos iniciados con suero antiescorpionico](servicios/control_enfermedades/ofidios_tratamientos_iniciados_con_suero_antiescorpionico/readme.md) | 2024-2025 | 301a | mensual | sexo |  |  |
| [Personas con prueba rápida de VIH](servicios/control_enfermedades/personas_con_prueba_rapida_de_vih/readme.md) | 2024-2025 | 301a | mensual | sexo |  |  |
| [Rabia: perros y gatos con vacuna antirrábica](servicios/control_enfermedades/rabia_perros_y_gatos_con_vacuna_antirrabica/readme.md) | 2015-2025 | 301a | mensual |  |  |  |
| [Rabia: personas con esquema clasico completo](servicios/control_enfermedades/rabia_personas_con_esquema_clasico_completo/readme.md) | 2015-2025 | 301a | mensual | sexo |  |  |
| [Rabia: personas con esquema reducido completo](servicios/control_enfermedades/rabia_personas_con_esquema_reducido_completo/readme.md) | 2015-2025 | 301a | mensual | sexo |  |  |
| [Rabia: personas con vacuna antirrábica](servicios/control_enfermedades/rabia_personas_con_vacuna_antirrabica/readme.md) | 2015-2025 | 301a | mensual | sexo |  |  |
| [Rabia: personas que abandonaron esquema](servicios/control_enfermedades/rabia_personas_que_abandonaron_esquema/readme.md) | 2015-2025 | 301a | mensual | sexo |  |  |
| [Tratamientos de chagas (2001-2006)](servicios/control_enfermedades/tratamiento_chagas_2001_2006/readme.md) | 2001-2006 | 301 | mensual | edad, tratamiento iniciado o concluido | Este dataset no separa por tratamiento. | Otros periodos: [2008-2009](servicios/control_enfermedades/tratamiento_chagas_2008_2009/readme.md), [2010-2025](servicios/control_enfermedades/tratamiento_chagas_2010_2025/readme.md). |
| [Tratamientos de chagas (2008-2009)](servicios/control_enfermedades/tratamiento_chagas_2008_2009/readme.md) | 2008-2009 | 301 | mensual | edad, tratamiento iniciado o concluido | Este dataset no separa por tratamiento. | Otros periodos: [2001-2006](servicios/control_enfermedades/tratamiento_chagas_2001_2006/readme.md), [2010-2025](servicios/control_enfermedades/tratamiento_chagas_2010_2025/readme.md). |
| [Tratamientos de chagas (2010-2025)](servicios/control_enfermedades/tratamiento_chagas_2010_2025/readme.md) | 2010-2025 | 301, 301a | mensual | sexo, edad, embarazo o puerperio, tratamiento iniciado o concluido | Este dataset no separa por tratamiento. | Otros periodos: [2001-2006](servicios/control_enfermedades/tratamiento_chagas_2001_2006/readme.md), [2008-2009](servicios/control_enfermedades/tratamiento_chagas_2008_2009/readme.md). |
| [Tratamientos de leishmaniasis](servicios/control_enfermedades/tratamiento_leishmaniasis/readme.md) | 2010-2025 | 301, 301a | mensual | forma clínica, sexo, tratamiento iniciado o concluido | Este dataset cuenta por separado 4 categorías de forma clínica: "cutanea", "mucosa", "mucosa y cutanea" y "visceral". |  |
| [Tratamientos específicos para malaria grave](servicios/control_enfermedades/tratamientos_especificos_para_malaria_grave/readme.md) | 2015-2025 | 301a | mensual | sexo, especie |  |  |
| [Tratamientos iniciados de tuberculosis y lepra (2001-2009)](servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2001_2009/readme.md) | 2001-2009 | 301 | mensual | esquema | Este dataset cuenta por separado 3 categorías de esquema: "I", "II" y "III". | Otros periodos: [2010-2023](servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2010_2023/readme.md), [2024-2025](servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2024_2025/readme.md). |
| [Tratamientos iniciados de tuberculosis y lepra (2010-2023)](servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2010_2023/readme.md) | 2010-2023 | 301, 301a | mensual | esquema, sexo | Este dataset cuenta por separado 5 categorías de esquema: "I", "II", "III", "multibacilar" y "paucibacilar". | Otros periodos: [2001-2009](servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2001_2009/readme.md), [2024-2025](servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2024_2025/readme.md). |
| [Tratamientos iniciados de tuberculosis y lepra (2024-2025)](servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2024_2025/readme.md) | 2024-2025 | 301a | mensual | esquema, sexo | Este dataset cuenta por separado 4 categorías de esquema: "de tb sensible", "modificado para tb", "multibacilar" y "paucibacilar". | Otros periodos: [2001-2009](servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2001_2009/readme.md), [2010-2023](servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2010_2023/readme.md). |
| [Tuberculosis: TB extrapulmonar nuevos](servicios/control_enfermedades/tuberculosis_tb_extrapulmonar_nuevos/readme.md) | 2008-2023 | 301, 301a | mensual | sexo |  | [Tuberculosis: TB extrapulmonar nuevos y recaidas](servicios/control_enfermedades/tuberculosis_tb_extrapulmonar_nuevos_y_recaidas/readme.md). |
| [Tuberculosis: TB extrapulmonar nuevos y recaidas](servicios/control_enfermedades/tuberculosis_tb_extrapulmonar_nuevos_y_recaidas/readme.md) | 2024-2025 | 301a | mensual | sexo |  | [Tuberculosis: TB extrapulmonar nuevos](servicios/control_enfermedades/tuberculosis_tb_extrapulmonar_nuevos/readme.md). |
| [Tuberculosis: TB pulmonar bacteriologicamente confirmados (nuevos y recaidas)](servicios/control_enfermedades/tuberculosis_tb_pulmonar_bacteriologicamente_confirmados_nue/readme.md) | 2024-2025 | 301a | mensual | sexo |  | [Tuberculosis: TBP BAAR (+) nuevos](servicios/control_enfermedades/tuberculosis_tb_pulmonar_baar_positivo_nuevos/readme.md). |
| [Tuberculosis: TB pulmonar clinicamente diagnosticados (nuevos y recaidas)](servicios/control_enfermedades/tuberculosis_tb_pulmonar_clinicamente_diagnosticados_nuevos_/readme.md) | 2024-2025 | 301a | mensual | sexo |  | [Tuberculosis: TBP BAAR (-) nuevos](servicios/control_enfermedades/tuberculosis_tb_pulmonar_baar_negativo_nuevos/readme.md). |
| [Tuberculosis: TBP BAAR (+) nuevos](servicios/control_enfermedades/tuberculosis_tb_pulmonar_baar_positivo_nuevos/readme.md) | 2008-2023 | 301, 301a | mensual | sexo |  | [Tuberculosis: TB pulmonar bacteriologicamente confirmados (nuevos y recaidas)](servicios/control_enfermedades/tuberculosis_tb_pulmonar_bacteriologicamente_confirmados_nue/readme.md). |
| [Tuberculosis: TBP BAAR (+) nuevos curados](servicios/control_enfermedades/tuberculosis_tb_pulmonar_baar_positivo_nuevos_curados/readme.md) | 2010-2023 | 301, 301a | mensual | sexo |  |  |
| [Tuberculosis: TBP BAAR (-) nuevos](servicios/control_enfermedades/tuberculosis_tb_pulmonar_baar_negativo_nuevos/readme.md) | 2008-2023 | 301, 301a | mensual | sexo |  | [Tuberculosis: TB pulmonar clinicamente diagnosticados (nuevos y recaidas)](servicios/control_enfermedades/tuberculosis_tb_pulmonar_clinicamente_diagnosticados_nuevos_/readme.md). |
| [Tuberculosis: casos TB TSF (nuevos y recaidas) con éxito de tratamiento](servicios/control_enfermedades/tuberculosis_casos_tb_tsf_nuevos_y_recaidas_con_exito_de_tra/readme.md) | 2024-2025 | 301a | mensual | sexo |  |  |
| [Tuberculosis: pacientes con coinfección TB/VIH](servicios/control_enfermedades/tuberculosis_pacientes_con_coinfeccion_tb_vih/readme.md) | 2015-2025 | 301a | mensual | sexo |  |  |
| [Tuberculosis: pacientes con lepra con seguimiento a sus contactos](servicios/control_enfermedades/tuberculosis_pacientes_con_lepra_con_seguimiento_a_sus_conta/readme.md) | 2024-2025 | 301a | mensual | sexo |  |  |
| [Tuberculosis: pacientes multibacilares con seguimiento a sus contactos](servicios/control_enfermedades/tuberculosis_pacientes_multibacilares_con_seguimiento_a_sus_/readme.md) | 2021-2023 | 301a | mensual | sexo |  |  |
| [Tuberculosis: pacientes multidrogos resistentes mdrs](servicios/control_enfermedades/tuberculosis_pacientes_multidrogos_resistentes_mdrs/readme.md) | 2015-2025 | 301a | mensual | sexo |  |  |
| [Tuberculosis: pacientes paucibacilares con seguimiento a sus contactos](servicios/control_enfermedades/tuberculosis_pacientes_paucibacilares_con_seguimiento_a_sus_/readme.md) | 2021-2023 | 301a | mensual | sexo |  |  |
| [Tuberculosis: personas con TB en TSF con prueba rápida](servicios/control_enfermedades/tuberculosis_personas_con_tb_en_tsf_con_prueba_rapida/readme.md) | 2015-2023 | 301a | mensual | sexo |  |  |
| [Tuberculosis: quimioprofilaxis en menores de 5 años](servicios/control_enfermedades/tuberculosis_quimioprofilaxis/readme.md) | 2008-2025 | 301, 301a | mensual | sexo, edad |  |  |
| [Tuberculosis: sintomáticos respiratorios](servicios/control_enfermedades/tuberculosis_sintomaticos_respiratorios/readme.md) | 2008-2025 | 301, 301a | mensual | sexo |  |  |
| [VIH: mujeres con prueba para sifilis en el parto o puerperio](servicios/control_enfermedades/vih_mujeres_con_prueba_para_sifilis_en_el_parto_o_puerperio/readme.md) | 2024-2025 | 301a | mensual | sexo |  |  |
| [VIH: mujeres embarazadas con prueba para sifilis (1ra prueba)](servicios/control_enfermedades/vih_mujeres_embarazadas_con_prueba_para_sifilis_1ra_prueba/readme.md) | 2024-2025 | 301a | mensual | sexo |  |  |
| [VIH: mujeres embarazadas con prueba para sifilis (2da prueba)](servicios/control_enfermedades/vih_mujeres_embarazadas_con_prueba_para_sifilis_2da_prueba/readme.md) | 2024-2025 | 301a | mensual | sexo |  |  |
| [VIH: mujeres embarazadas con prueba rápida](servicios/control_enfermedades/vih_mujeres_embarazadas_con_prueba_rapida/readme.md) | 2010-2023 | 301, 301a | mensual | sexo |  | [Mujeres embarazadas con prueba rápida VIH (1ra prueba)](servicios/control_enfermedades/mujeres_embarazadas_con_prueba_rapida_vih_1ra_prueba/readme.md), [Mujeres embarazadas con prueba rápida VIH (2da prueba)](servicios/control_enfermedades/mujeres_embarazadas_con_prueba_rapida_vih_2da_prueba/readme.md). |
| [VIH: personas con pre-consejeria realizadas para acceso a la prueba rápida](servicios/control_enfermedades/vih_personas_con_pre_consejeria_realizadas_para_acceso_a_la_/readme.md) | 2010-2014 | 301 | mensual | sexo |  |  |
| [VIH: personas con prueba rápida](servicios/control_enfermedades/vih_personas_con_prueba_rapida/readme.md) | 2010-2023 | 301, 301a | mensual | sexo |  |  |

### Diagnóstico y tratamiento

Laboratorio, imagen, tratamientos y enfermería. 24 datasets.

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Administracion de medicamentos](servicios/diagnostico_tratamiento/administracion_de_medicamentos/readme.md) | 2024-2025 | 301b | mensual | servicio |  |  |
| [Administracion de sondas](servicios/diagnostico_tratamiento/administracion_de_sondas/readme.md) | 2024-2025 | 301b | mensual | servicio |  |  |
| [Curaciones y/o suturas](servicios/diagnostico_tratamiento/curaciones_y_o_suturas/readme.md) | 2001-2025 | 301, 301a | mensual |  |  | Formulario 301b: [Curaciones y/o suturas (formulario 301b)](servicios/diagnostico_tratamiento/curaciones_y_o_suturas_301b/readme.md). |
| [Curaciones y/o suturas (formulario 301b)](servicios/diagnostico_tratamiento/curaciones_y_o_suturas_301b/readme.md) | 2024-2025 | 301b | mensual | servicio |  | Formulario 301a: [Curaciones y/o suturas](servicios/diagnostico_tratamiento/curaciones_y_o_suturas/readme.md). |
| [Ecografias realizados](servicios/diagnostico_tratamiento/ecografias_realizados/readme.md) | 2015-2025 | 301b | mensual | sexo, servicio |  |  |
| [Electrocardiogramas realizados](servicios/diagnostico_tratamiento/electrocardiogramas_realizados/readme.md) | 2015-2025 | 301b | mensual | sexo, servicio |  |  |
| [Estudios de anatomía patologico](servicios/diagnostico_tratamiento/estudios_de_anatomia_patologico/readme.md) | 2015-2025 | 301b | mensual | sexo, servicio |  |  |
| [Hemodialisis realizadas](servicios/diagnostico_tratamiento/hemodialisis_realizadas/readme.md) | 2015-2025 | 301b | mensual | sexo |  |  |
| [Inyectable (formulario 301b)](servicios/diagnostico_tratamiento/inyectables_301b/readme.md) | 2024-2025 | 301b | mensual | servicio |  | Formulario 301a: [Inyectables](servicios/diagnostico_tratamiento/inyectables/readme.md). |
| [Inyectables](servicios/diagnostico_tratamiento/inyectables/readme.md) | 2001-2025 | 301, 301a | mensual |  |  | Formulario 301b: [Inyectable (formulario 301b)](servicios/diagnostico_tratamiento/inyectables_301b/readme.md). |
| [Otras actividades](servicios/diagnostico_tratamiento/otras_actividades/readme.md) | 2015-2025 | 301a | mensual |  |  | Formulario 301b: [Otras actividades (formulario 301b)](servicios/diagnostico_tratamiento/otras_actividades_301b/readme.md). |
| [Otras actividades (formulario 301b)](servicios/diagnostico_tratamiento/otras_actividades_301b/readme.md) | 2024-2025 | 301b | mensual | servicio |  | Formulario 301a: [Otras actividades](servicios/diagnostico_tratamiento/otras_actividades/readme.md). |
| [Otros estudios complementarios](servicios/diagnostico_tratamiento/otros_estudios_complementarios/readme.md) | 2015-2025 | 301b | mensual | sexo, servicio |  |  |
| [Placas radiograficas realizadas](servicios/diagnostico_tratamiento/placas_radiograficas_realizadas/readme.md) | 2015-2025 | 301b | mensual | sexo, servicio |  |  |
| [Pruebas de laboratorio realizados](servicios/diagnostico_tratamiento/pruebas_de_laboratorio_realizados/readme.md) | 2015-2025 | 301b | mensual | sexo, servicio |  |  |
| [Quimioterapia realizadas](servicios/diagnostico_tratamiento/quimioterapia_realizadas/readme.md) | 2015-2025 | 301b | mensual | sexo |  |  |
| [Radioterapias realizadas](servicios/diagnostico_tratamiento/radioterapias_realizadas/readme.md) | 2015-2025 | 301b | mensual | sexo |  |  |
| [Seciones de fisioterapia realizadas](servicios/diagnostico_tratamiento/sesiones_de_fisioterapia_realizadas/readme.md) | 2015-2023 | 301b | mensual | sexo |  | [Seciones de fisioterapia realizadas en c.e](servicios/diagnostico_tratamiento/seciones_de_fisioterapia_realizadas_en_c_e/readme.md), [Sesiones de fisioterapia realizadas en internación](servicios/diagnostico_tratamiento/sesiones_de_fisioterapia_realizadas_en_internacion/readme.md). |
| [Seciones de fisioterapia realizadas en c.e](servicios/diagnostico_tratamiento/seciones_de_fisioterapia_realizadas_en_c_e/readme.md) | 2024-2025 | 301b | mensual | sexo |  | [Seciones de fisioterapia realizadas](servicios/diagnostico_tratamiento/sesiones_de_fisioterapia_realizadas/readme.md), [Sesiones de fisioterapia realizadas en internación](servicios/diagnostico_tratamiento/sesiones_de_fisioterapia_realizadas_en_internacion/readme.md). |
| [Sesiones de fisioterapia realizadas en internación](servicios/diagnostico_tratamiento/sesiones_de_fisioterapia_realizadas_en_internacion/readme.md) | 2024-2025 | 301b | mensual | sexo |  | [Seciones de fisioterapia realizadas](servicios/diagnostico_tratamiento/sesiones_de_fisioterapia_realizadas/readme.md), [Seciones de fisioterapia realizadas en c.e](servicios/diagnostico_tratamiento/seciones_de_fisioterapia_realizadas_en_c_e/readme.md). |
| [Sueros](servicios/diagnostico_tratamiento/sueros/readme.md) | 2001-2025 | 301, 301a | mensual |  |  | Formulario 301b: [Sueros (formulario 301b)](servicios/diagnostico_tratamiento/sueros_301b/readme.md). |
| [Sueros (formulario 301b)](servicios/diagnostico_tratamiento/sueros_301b/readme.md) | 2024-2025 | 301b | mensual | servicio |  | Formulario 301a: [Sueros](servicios/diagnostico_tratamiento/sueros/readme.md). |
| [Transfusiones de sangre realizadas](servicios/diagnostico_tratamiento/transfusiones_de_sangre_realizadas/readme.md) | 2015-2025 | 301b | mensual | sexo |  |  |
| [Usuarias (os) en dialisis peritoneal](servicios/diagnostico_tratamiento/usuarias_os_en_dialisis_peritoneal/readme.md) | 2015-2025 | 301b | mensual | sexo |  |  |

### Enfermedades crónicas

Atenciones de enfermedades crónicas y salud mental. 13 datasets.

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Abuso de alcohol](servicios/enfermedades_cronicas/abuso_de_alcohol/readme.md) | 2010-2014 | 301 | mensual | sexo |  |  |
| [Cardiovasculares](servicios/enfermedades_cronicas/cardiovasculares/readme.md) | 2010-2014 | 301 | mensual | sexo |  |  |
| [Cáncer cervicouterino](servicios/enfermedades_cronicas/cancer_cervicouterino/readme.md) | 2010-2014 | 301 | mensual | sexo |  |  |
| [Cáncer otros](servicios/enfermedades_cronicas/cancer_otros/readme.md) | 2010-2014 | 301 | mensual | sexo |  |  |
| [Diabetes mellitus I - II](servicios/enfermedades_cronicas/diabetes_mellitus_i_ii/readme.md) | 2010-2014 | 301 | mensual | sexo |  |  |
| [Epilepsia / convulsiones / ataques](servicios/enfermedades_cronicas/epilepsia_convulsiones_ataques/readme.md) | 2010-2014 | 301 | mensual | sexo |  |  |
| [Episodios depresivos / ansiedad](servicios/enfermedades_cronicas/episodios_depresivos_ansiedad/readme.md) | 2010-2014 | 301 | mensual | sexo |  |  |
| [Habito de fumar](servicios/enfermedades_cronicas/habito_de_fumar/readme.md) | 2010-2014 | 301 | mensual | sexo |  |  |
| [Hipertensión arterial sistémica en mayores de 5 años](servicios/enfermedades_cronicas/hipertension_arterial_sistemica/readme.md) | 2010-2014 | 301 | mensual | sexo, edad |  |  |
| [Personas con discapacidad](servicios/enfermedades_cronicas/personas_con_discapacidad/readme.md) | 2010-2014 | 301 | mensual | sexo |  |  |
| [Reumáticas](servicios/enfermedades_cronicas/reumaticas/readme.md) | 2010-2014 | 301 | mensual | sexo |  |  |
| [Sobrepeso en mayores de 5 años](servicios/enfermedades_cronicas/sobrepeso/readme.md) | 2010-2014 | 301 | mensual | sexo, edad |  |  |
| [Trastornos de comportamiento y consumo de sustancias psicoactivas](servicios/enfermedades_cronicas/trastornos_de_comportamiento_y_consumo_de_sustancias_psicoac/readme.md) | 2010-2014 | 301 | mensual | sexo |  |  |

### Gestión y comunidad

Actividades con la comunidad y de gestión de calidad. 49 datasets.

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Actividades con la comunidad](servicios/gestion_comunidad/actividades_con_la_comunidad/readme.md) | 2001-2003 | 301 | mensual |  |  |  |
| [Actividades de educacion integral en sexualidad a adolescentes](servicios/gestion_comunidad/actividades_de_educacion_integral_en_sexualidad_a_adolescent/readme.md) | 2024-2025 | 301a | mensual |  |  |  |
| [Actividades de la comunidad con participación del establecimiento](servicios/gestion_comunidad/actividades_de_la_comunidad_con_participacion_del_establecim/readme.md) | 2015-2025 | 301a | mensual |  |  |  |
| [Actividades educativas en salud](servicios/gestion_comunidad/actividades_educativas_en_salud/readme.md) | 2010-2025 | 301, 301a | mensual |  |  |  |
| [Actividades realizadas con participación de la comunidad](servicios/gestion_comunidad/actividades_realizadas_con_participacion_de_la_comunidad/readme.md) | 2004-2025 | 301, 301a | mensual |  |  |  |
| [Auditorias del programa en aplicación de la norma técnica](servicios/gestion_comunidad/auditorias_del_programa_en_aplicacion_de_la_norma_tecnica/readme.md) | 2015-2023 | 301b | mensual |  |  |  |
| [Auditorias internas de servicio en aplicación de la norma técnica](servicios/gestion_comunidad/auditorias_internas_de_servicio_en_aplicacion_de_la_norma_te/readme.md) | 2015-2025 | 301b | mensual |  |  |  |
| [Auditorias internas en salud en aplicación de norma técnica](servicios/gestion_comunidad/auditorias_internas_en_salud_en_aplicacion_de_norma_tecnica/readme.md) | 2010-2025 | 301, 301a | mensual |  |  |  |
| [Auditorias programadas en aplicación de la norma técnica](servicios/gestion_comunidad/auditorias_programadas_en_aplicacion_de_la_norma_tecnica/readme.md) | 2024-2025 | 301b | mensual |  |  |  |
| [Autoevaluaciones para acreditación de los servicios](servicios/gestion_comunidad/autoevaluaciones_para_acreditacion_de_los_servicios/readme.md) | 2015-2025 | 301b | mensual |  |  |  |
| [Autoevaluciones para acreditación del establecimiento](servicios/gestion_comunidad/autoevaluciones_para_acreditacion_del_establecimiento/readme.md) | 2010-2025 | 301, 301a | mensual |  |  |  |
| [Beneficiarias (madres) del bono juana azurduy atendidas](servicios/gestion_comunidad/beneficiarias_madres_del_bono_juana_azurduy_atendidas/readme.md) | 2015-2025 | 301a | mensual |  |  |  |
| [Beneficiarias (madres) nuevas del bono juana azurduy](servicios/gestion_comunidad/beneficiarias_madres_nuevas_del_bono_juana_azurduy/readme.md) | 2010-2014 | 301 | mensual |  |  |  |
| [Beneficiarios(as) (niño/as) con educación en salud oral](servicios/gestion_comunidad/beneficiarios_as_nino_as_con_educacion_en_salud_oral/readme.md) | 2021-2023 | 301a | mensual |  |  |  |
| [Beneficiarios(as) (niño/as) con promoción en salud oral](servicios/gestion_comunidad/beneficiarios_as_nino_as_con_promocion_en_salud_oral/readme.md) | 2021-2023 | 301a | mensual |  |  |  |
| [Beneficiarios(as) (niño/as) del bono juana azurduy atendidos(as)](servicios/gestion_comunidad/beneficiarios_as_nino_as_del_bono_juana_azurduy_atendidos_as/readme.md) | 2015-2025 | 301a | mensual |  |  |  |
| [Beneficiarios(as) (niños/as) nuevos(as) del bono juana azurduy](servicios/gestion_comunidad/beneficiarios_as_ninos_as_nuevos_as_del_bono_juana_azurduy/readme.md) | 2010-2014 | 301 | mensual |  |  |  |
| [Beneficiarios(as) con educación en salud oral](servicios/gestion_comunidad/beneficiarios_as_con_educacion_en_salud_oral/readme.md) | 2024-2025 | 301a | mensual |  |  |  |
| [Beneficiarios(as) con promoción en salud oral](servicios/gestion_comunidad/beneficiarios_as_con_promocion_en_salud_oral/readme.md) | 2024-2025 | 301a | mensual |  |  |  |
| [CAI de establecimiento](servicios/gestion_comunidad/cai_de_establecimiento/readme.md) | 2010-2025 | 301, 301a | mensual |  |  | [CAI de sector realizados](servicios/gestion_comunidad/cai_de_sector_realizados/readme.md). |
| [CAI de sector realizados](servicios/gestion_comunidad/cai_de_sector_realizados/readme.md) | 2004-2009 | 301 | mensual |  |  | [CAI de establecimiento](servicios/gestion_comunidad/cai_de_establecimiento/readme.md). |
| [CAI hospitario](servicios/gestion_comunidad/cai_hospitario/readme.md) | 2015-2025 | 301b | mensual |  |  |  |
| [Cajas de evidencia utilizadas](servicios/gestion_comunidad/cajas_de_evidencia_utilizadas/readme.md) | 2024-2025 | 301a | mensual |  |  |  |
| [Capacitaciones recibidas](servicios/gestion_comunidad/capacitaciones_recibidas/readme.md) | 2001-2003 | 301 | mensual |  |  |  |
| [Certificados únicos para casos de violencia (ley 348)](servicios/gestion_comunidad/certificados_unicos_para_casos_de_violencia_ley_348/readme.md) | 2021-2025 | 301a | mensual |  |  |  |
| [Comunidades que participaron en el CAI de establecimiento](servicios/gestion_comunidad/comunidades_que_participaron_en_el_cai_de_establecimiento/readme.md) | 2010-2025 | 301, 301a | mensual |  |  |  |
| [Comunidades que participaron en el CAI de sector](servicios/gestion_comunidad/comunidades_que_participaron_en_el_cai_de_sector/readme.md) | 2004-2009 | 301 | mensual |  |  |  |
| [Familias carpetizadas con seguimiento durante el periódo](servicios/gestion_comunidad/familias_carpetizadas_con_seguimiento_durante_el_periodo/readme.md) | 2015-2025 | 301a | mensual |  |  |  |
| [Familias nuevas carpetizadas durante el periódo](servicios/gestion_comunidad/familias_nuevas_carpetizadas_durante_el_periodo/readme.md) | 2015-2025 | 301a | mensual |  |  |  |
| [Participantes de telecapacitacion](servicios/gestion_comunidad/participantes_de_telecapacitacion/readme.md) | 2024-2025 | 301a | mensual | sexo, participante |  |  |
| [Participantes de telepromociones](servicios/gestion_comunidad/participantes_de_telepromociones/readme.md) | 2024-2025 | 301a | mensual | sexo, participante |  |  |
| [Personas con discapacidad atendidas en el establecimiento](servicios/gestion_comunidad/personas_con_discapacidad_atendidas_en_el_establecimiento/readme.md) | 2021-2025 | 301a | mensual |  |  |  |
| [Personas con discapacidad atendidas en la comunidad](servicios/gestion_comunidad/personas_con_discapacidad_atendidas_en_la_comunidad/readme.md) | 2021-2025 | 301a | mensual |  |  |  |
| [Primeras visitas familares realizadas](servicios/gestion_comunidad/primeras_visitas_familares_realizadas/readme.md) | 2024-2025 | 301a | mensual |  |  | [Visitas familiares realizadas](servicios/gestion_comunidad/visitas_familiares_realizadas/readme.md), [Segundas visitas familiares realizadas](servicios/gestion_comunidad/segundas_visitas_familiares_realizadas/readme.md), [Terceras visitas familiares](servicios/gestion_comunidad/terceras_visitas_familiares/readme.md). |
| [Proyectos ejecutados en determinantes de salud](servicios/gestion_comunidad/proyectos_ejecutados_en_determinantes_de_salud/readme.md) | 2024-2025 | 301a | mensual |  |  |  |
| [Quejas y reclamos realizadas por los usuarios](servicios/gestion_comunidad/quejas_y_reclamos_realizadas_por_los_usuarios/readme.md) | 2015-2025 | 301a | mensual |  |  |  |
| [RPS, parteras y promotores activos](servicios/gestion_comunidad/rps_parteras_y_promotores_activos/readme.md) | 2001-2003 | 301 | mensual |  |  |  |
| [Reuniones del CAI de establecimientos (secto](servicios/gestion_comunidad/reuniones_del_cai_de_establecimientos_secto/readme.md) | 2001-2003 | 301 | mensual |  |  |  |
| [Reuniones del CAI del distrito](servicios/gestion_comunidad/reuniones_del_cai_del_distrito/readme.md) | 2001-2003 | 301 | mensual |  |  |  |
| [Reuniones realizadas con autoridades locales de salud](servicios/gestion_comunidad/reuniones_realizadas_con_autoridades_locales_de_salud/readme.md) | 2015-2025 | 301a | mensual |  |  |  |
| [Reuniones realizadas con comités loc. de salud](servicios/gestion_comunidad/reuniones_realizadas_con_comites_loc_de_salud/readme.md) | 2015-2025 | 301a | mensual |  |  | [Reuniones realizadas con comités loc. de salud/consejo mun. de salud](servicios/gestion_comunidad/reuniones_realizadas_con_comites_loc_de_salud_consejo_mun_de/readme.md). |
| [Reuniones realizadas con comités loc. de salud/consejo mun. de salud](servicios/gestion_comunidad/reuniones_realizadas_con_comites_loc_de_salud_consejo_mun_de/readme.md) | 2010-2014 | 301 | mensual |  |  | [Reuniones realizadas con comités loc. de salud](servicios/gestion_comunidad/reuniones_realizadas_con_comites_loc_de_salud/readme.md). |
| [Reunones del CAI de area y/o municipio](servicios/gestion_comunidad/reunones_del_cai_de_area_y_o_municipio/readme.md) | 2001-2003 | 301 | mensual |  |  |  |
| [Segundas visitas familiares realizadas](servicios/gestion_comunidad/segundas_visitas_familiares_realizadas/readme.md) | 2024-2025 | 301a | mensual |  |  | [Visitas familiares realizadas](servicios/gestion_comunidad/visitas_familiares_realizadas/readme.md), [Primeras visitas familares realizadas](servicios/gestion_comunidad/primeras_visitas_familares_realizadas/readme.md), [Terceras visitas familiares](servicios/gestion_comunidad/terceras_visitas_familiares/readme.md). |
| [Sugerencias y agradeciemientos realizados por los usuarios](servicios/gestion_comunidad/sugerencias_y_agradeciemientos_realizados_por_los_usuarios/readme.md) | 2015-2025 | 301a | mensual |  |  |  |
| [Supervisiones recibidas](servicios/gestion_comunidad/supervisiones_recibidas/readme.md) | 2001-2003 | 301 | mensual |  |  |  |
| [Terceras visitas familiares](servicios/gestion_comunidad/terceras_visitas_familiares/readme.md) | 2024-2025 | 301a | mensual |  |  | [Visitas familiares realizadas](servicios/gestion_comunidad/visitas_familiares_realizadas/readme.md), [Primeras visitas familares realizadas](servicios/gestion_comunidad/primeras_visitas_familares_realizadas/readme.md), [Segundas visitas familiares realizadas](servicios/gestion_comunidad/segundas_visitas_familiares_realizadas/readme.md). |
| [Visitas familiares planificadas](servicios/gestion_comunidad/visitas_familiares_planificadas/readme.md) | 2015-2023 | 301a | mensual |  |  |  |
| [Visitas familiares realizadas](servicios/gestion_comunidad/visitas_familiares_realizadas/readme.md) | 2015-2023 | 301a | mensual |  |  | [Primeras visitas familares realizadas](servicios/gestion_comunidad/primeras_visitas_familares_realizadas/readme.md), [Segundas visitas familiares realizadas](servicios/gestion_comunidad/segundas_visitas_familiares_realizadas/readme.md), [Terceras visitas familiares](servicios/gestion_comunidad/terceras_visitas_familiares/readme.md). |

### Internación

Ingresos, egresos y días cama. 19 datasets.

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Camas](servicios/internacion/camas/readme.md) | 2016-2025 | 301b | mensual | especialidad |  |  |
| [Contrareferidos](servicios/internacion/contrareferidos/readme.md) | 2007-2025 | 301, 301a | mensual | sexo |  |  |
| [Dias cama disp](servicios/internacion/dias_cama_disponibles/readme.md) | 2015-2025 | 301b | mensual | especialidad |  |  |
| [Dias cama ocupada](servicios/internacion/dias_camas_ocupadas/readme.md) | 2015-2025 | 301b | mensual | especialidad |  |  |
| [Días camas disponibles maternidad](servicios/internacion/dias_camas_disponibles_maternidad/readme.md) | 2001-2025 | 301, 301a | mensual | sexo |  |  |
| [Días camas disponibles otros servicios](servicios/internacion/dias_camas_disponibles_otros_servicios/readme.md) | 2001-2025 | 301, 301a | mensual | sexo | Carapari registra 11.545.414 días cama en diciembre de 2015, casi tres veces el total nacional de otras gestiones (unos 4,3 millones). Se publica tal como se registró; probablemente es un error de registro. |  |
| [Días camas ocupadas maternidad](servicios/internacion/dias_camas_ocupadas_maternidad/readme.md) | 2001-2025 | 301, 301a | mensual | sexo |  |  |
| [Días camas ocupadas otros servicios](servicios/internacion/dias_camas_ocupadas_otros_servicios/readme.md) | 2001-2025 | 301, 301a | mensual | sexo |  |  |
| [Egresos](servicios/internacion/egresos/readme.md) | 2001-2025 | 301, 301a | mensual | sexo |  |  |
| [Egresos por diagnóstico (2001-2007)](servicios/internacion/egresos_por_diagnostico_2001_2007/readme.md) | 2001-2007 | 301 | mensual | diagnóstico, edad | Este dataset cuenta por separado 3 categorías de diagnóstico: "diarreas", "neumonias" y "otros". | Otros periodos: [2008-2009](servicios/internacion/egresos_por_diagnostico_2008_2009/readme.md), [2010-2014](servicios/internacion/egresos_por_diagnostico_2010_2014/readme.md). |
| [Egresos por diagnóstico (2008-2009)](servicios/internacion/egresos_por_diagnostico_2008_2009/readme.md) | 2008-2009 | 301 | mensual | diagnóstico | Este dataset cuenta por separado 6 categorías de diagnóstico: "diabetes", "diarreas", "discapacitados", "hipertension arterial", "neumonias" y "otros". | Otros periodos: [2001-2007](servicios/internacion/egresos_por_diagnostico_2001_2007/readme.md), [2010-2014](servicios/internacion/egresos_por_diagnostico_2010_2014/readme.md). |
| [Egresos por diagnóstico (2010-2014)](servicios/internacion/egresos_por_diagnostico_2010_2014/readme.md) | 2010-2014 | 301 | mensual | diagnóstico, sexo | Este dataset cuenta por separado 3 categorías de diagnóstico: "diarreas", "neumonias" y "otros". | Otros periodos: [2001-2007](servicios/internacion/egresos_por_diagnostico_2001_2007/readme.md), [2008-2009](servicios/internacion/egresos_por_diagnostico_2008_2009/readme.md). |
| [Fallecidos a partir de las 48 horas](servicios/internacion/fallecidos_a_partir_de_las_48_horas/readme.md) | 2001-2025 | 301, 301a | mensual | sexo |  |  |
| [Fallecidos antes de las 48 horas](servicios/internacion/fallecidos_antes_de_las_48_horas/readme.md) | 2001-2025 | 301, 301a | mensual | sexo |  |  |
| [Ingresos espontáneos](servicios/internacion/ingresos_espontaneos/readme.md) | 2001-2025 | 301, 301a | mensual | sexo |  |  |
| [Ingresos referidos de otros establecimientos de salud](servicios/internacion/ingresos_referidos_de_otros_establecimientos_de_salud/readme.md) | 2001-2025 | 301, 301a | mensual | sexo |  |  |
| [Ingresos y egresos por servicio de internación (2015)](servicios/internacion/ingresos_egresos_hospital_2015/readme.md) | 2015 | 301b | mensual | movimiento, especialidad | Este dataset cuenta por separado 6 categorías de movimiento: "egreso: contrarreferido", "egreso: defunción a partir de 48 horas", "egreso: defunción antes de 48 horas", "egreso: traslado interno", "ingreso y egreso el mismo día" y "ingreso: traslado interno". | Otros periodos: [2016-2023](servicios/internacion/ingresos_egresos_hospital_2016_2023/readme.md), [2024-2025](servicios/internacion/ingresos_egresos_hospital_2024_2025/readme.md). |
| [Ingresos y egresos por servicio de internación (2016-2023)](servicios/internacion/ingresos_egresos_hospital_2016_2023/readme.md) | 2016-2023 | 301b | mensual | movimiento, especialidad | Este dataset cuenta por separado 10 categorías de movimiento; el readme las lista. | Otros periodos: [2015](servicios/internacion/ingresos_egresos_hospital_2015/readme.md), [2024-2025](servicios/internacion/ingresos_egresos_hospital_2024_2025/readme.md). |
| [Ingresos y egresos por servicio de internación (2024-2025)](servicios/internacion/ingresos_egresos_hospital_2024_2025/readme.md) | 2024-2025 | 301b | mensual | movimiento, especialidad | Este dataset cuenta por separado 12 categorías de movimiento; el readme las lista. | Otros periodos: [2015](servicios/internacion/ingresos_egresos_hospital_2015/readme.md), [2016-2023](servicios/internacion/ingresos_egresos_hospital_2016_2023/readme.md). |

### Nutrición

Control de crecimiento, micronutrientes y alimentación complementaria. 11 datasets.

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Control de crecimiento infantil](servicios/nutricion/control_crecimiento/readme.md) | 2001-2025 | 301, 301a | mensual | sexo, edad, nuevo o repetido, lugar |  |  |
| [Lactancia materna (2007-2008)](servicios/nutricion/lactancia_materna_2007_2008/readme.md) | 2007-2008 | 301 | mensual | tipo, edad | Este dataset cuenta una sola categoría de tipo: "exclusiva". | Otros periodos: [2015-2025](servicios/nutricion/lactancia_materna_2015_2025/readme.md). |
| [Lactancia materna (2015-2025)](servicios/nutricion/lactancia_materna_2015_2025/readme.md) | 2015-2025 | 301a | mensual | tipo | Este dataset cuenta por separado 2 categorías de tipo: "exclusiva" y "inmediata". | Otros periodos: [2007-2008](servicios/nutricion/lactancia_materna_2007_2008/readme.md). |
| [Personas que recibieron alimento complementario](servicios/nutricion/alimento_complementario/readme.md) | 2009-2025 | 301, 301a | mensual | sexo, edad, embarazo o puerperio |  |  |
| [Personas que recibieron hierro (2001-2006)](servicios/nutricion/hierro_2001_2006/readme.md) | 2001-2006 | 301 | mensual | dosis, sexo, edad, embarazo o puerperio | Este dataset cuenta por separado 2 categorías de dosis: "1" y "3". | Otros periodos: [2007-2025](servicios/nutricion/hierro_2007_2025/readme.md). |
| [Personas que recibieron hierro (2007-2025)](servicios/nutricion/hierro_2007_2025/readme.md) | 2007-2025 | 301, 301a | mensual | sexo, edad, embarazo o puerperio | Este dataset no separa por dosis. | Otros periodos: [2001-2006](servicios/nutricion/hierro_2001_2006/readme.md). |
| [Personas que recibieron vitamina A (2001-2003)](servicios/nutricion/vitamina_a_2001_2003/readme.md) | 2001-2003 | 301 | mensual | dosis, sexo, edad, embarazo o puerperio | Este dataset cuenta por separado 3 categorías de dosis: "1", "2" y "única". | Otros periodos: [2004](servicios/nutricion/vitamina_a_2004/readme.md), [2005-2025](servicios/nutricion/vitamina_a_2005_2025/readme.md). |
| [Personas que recibieron vitamina A (2004)](servicios/nutricion/vitamina_a_2004/readme.md) | 2004 | 301 | mensual | dosis, sexo, edad, embarazo o puerperio | Este dataset cuenta por separado 3 categorías de dosis: "1", "2" y "única". | Otros periodos: [2001-2003](servicios/nutricion/vitamina_a_2001_2003/readme.md), [2005-2025](servicios/nutricion/vitamina_a_2005_2025/readme.md). |
| [Personas que recibieron vitamina A (2005-2025)](servicios/nutricion/vitamina_a_2005_2025/readme.md) | 2005-2025 | 301, 301a | mensual | dosis, sexo, edad, embarazo o puerperio | Este dataset cuenta por separado 3 categorías de dosis: "1", "2" y "única". | Otros periodos: [2001-2003](servicios/nutricion/vitamina_a_2001_2003/readme.md), [2004](servicios/nutricion/vitamina_a_2004/readme.md). |
| [Personas que recibieron zinc](servicios/nutricion/zinc/readme.md) | 2015-2025 | 301a | mensual | edad |  |  |
| [Talla para la edad](servicios/nutricion/talla_para_la_edad/readme.md) | 2010-2014 | 301 | mensual | clasificación, sexo, edad | Este dataset cuenta por separado 2 categorías de clasificación: "baja" y "normal". |  |

### Odontología

Consultas y tratamientos odontológicos. 22 datasets.

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Acciones preventivas dentro del establecimiento](servicios/odontologia/acciones_preventivas/readme.md) | 2005-2025 | 301, 301a | mensual | sexo, edad, lugar |  |  |
| [Actividades de educación en salud oral](servicios/odontologia/actividades_de_educacion_en_salud_oral/readme.md) | 2010-2014 | 301 | mensual |  |  |  |
| [Actividades odontológicas en la comunidad](servicios/odontologia/actividades_odontologicas_en_la_comunidad/readme.md) | 2008-2009 | 301 | mensual |  |  |  |
| [Aplicación de fluor](servicios/odontologia/aplicacion_de_fluor/readme.md) | 2015-2020 | 301a | mensual | sexo, edad |  |  |
| [Cirugia bucal menor](servicios/odontologia/cirugia_bucal_menor/readme.md) | 2010-2025 | 301, 301a | mensual | sexo, edad |  |  |
| [Cirugia bucomaxilofacial mediana](servicios/odontologia/cirugia_bucomaxilofacial_mediana/readme.md) | 2015-2025 | 301a | mensual | sexo, edad |  |  |
| [Cirugia bucomaxilofacial menor](servicios/odontologia/cirugia_bucomaxilofacial_menor/readme.md) | 2015-2025 | 301a | mensual | sexo, edad |  |  |
| [Cirugia maxilo faciales](servicios/odontologia/cirugia_maxilo_faciales/readme.md) | 2005-2009 | 301 | mensual |  |  |  |
| [Consultas odontológicas](servicios/odontologia/consulta_odontologica/readme.md) | 2001-2025 | 301, 301a | mensual | sexo, edad, nuevo o repetido, embarazo o puerperio |  |  |
| [Endodoncias](servicios/odontologia/endodoncia/readme.md) | 2005-2025 | 301, 301a | mensual | sexo, edad |  |  |
| [Exodoncias](servicios/odontologia/exodoncia/readme.md) | 2001-2004, 2008-2009, 2015-2020 | 301, 301a | mensual | sexo, edad |  |  |
| [Fluorizaciones](servicios/odontologia/fluorizaciones/readme.md) | 2004 | 301 | mensual |  |  |  |
| [Obturaciones](servicios/odontologia/obturaciones/readme.md) | 2001-2004 | 301 | mensual |  |  |  |
| [Otras acciones](servicios/odontologia/otras_acciones/readme.md) | 2010-2014 | 301 | mensual | sexo |  |  |
| [Periodoncias](servicios/odontologia/periodoncia/readme.md) | 2005-2025 | 301, 301a | mensual | sexo, edad |  |  |
| [Primeras consultas](servicios/odontologia/primera_consulta/readme.md) | 2005-2025 | 301, 301a | mensual | sexo, edad, embarazo o puerperio |  |  |
| [Pulpotomías](servicios/odontologia/pulpotomias/readme.md) | 2004-2007 | 301 | mensual |  |  |  |
| [Rayos X dental](servicios/odontologia/rayos_x_dental/readme.md) | 2021-2025 | 301a | mensual | sexo, edad |  |  |
| [Restauraciones](servicios/odontologia/restauraciones/readme.md) | 2005-2025 | 301, 301a | mensual | sexo, edad |  |  |
| [Tartectomias](servicios/odontologia/tartectomias/readme.md) | 2004 | 301 | mensual |  |  |  |
| [Trat. de fracturas dentoalveolares](servicios/odontologia/trat_de_fracturas_dentoalveolares/readme.md) | 2015-2025 | 301a | mensual | sexo, edad |  |  |
| [Trat. odontológico integral terminado (TOIT)](servicios/odontologia/trat_odontologico_integral_terminado/readme.md) | 2021-2025 | 301a | mensual | sexo, edad |  |  |

### Referencias de pacientes

Referencias y contrarreferencias de pacientes. 17 datasets.

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Autoreferencias recibidas por el establecimiento](servicios/referencias/autoreferencias_recibidas_por_el_establecimiento/readme.md) | 2024-2025 | 301b | mensual | sexo, servicio |  |  |
| [Contrareferencias realizadas](servicios/referencias/contrareferencias_realizadas/readme.md) | 2024-2025 | 301b | mensual | sexo, servicio |  |  |
| [PCD referidos a servicios/centros de rehabilitación](servicios/referencias/pcd_referidos_a_servicios_centros_de_rehabilitacion/readme.md) | 2021-2025 | 301a | mensual |  |  |  |
| [PCD referidos a unidades de calificación de discapacidad](servicios/referencias/pcd_referidos_a_unidades_de_calificacion_de_discapacidad/readme.md) | 2010-2025 | 301, 301a | mensual |  |  |  |
| [Pacientes referidos a otros establecimientos](servicios/referencias/pacientes_referidos_a_otros_establecimientos/readme.md) | 2001-2025 | 301, 301a | mensual |  |  |  |
| [Pacientes referidos de la comunidad o medicina tradicional](servicios/referencias/pacientes_derivados_de_la_comunidad_o_medicina_tradicional/readme.md) | 2010-2025 | 301, 301a | mensual |  |  |  |
| [Pacientes referidos del establecimiento a la medicina tradicional](servicios/referencias/pacientes_referidos_del_establecimiento_a_la_medicina_tradic/readme.md) | 2015-2025 | 301a | mensual |  |  |  |
| [Pacientes referidos recibidos por el establecimiento](servicios/referencias/pacientes_referidos_recibidos_por_el_establecimiento/readme.md) | 2015-2025 | 301a | mensual |  |  |  |
| [Pacientes retornados al establecimiento de origen](servicios/referencias/pacientes_contrareferidos_al_establecimiento/readme.md) | 2010-2025 | 301, 301a | mensual |  |  |  |
| [Referencias adecuadas](servicios/referencias/referencias_adecuadas/readme.md) | 2015-2025 | 301b | mensual | sexo, servicio |  |  |
| [Referencias inadeuadas](servicios/referencias/referencias_inadeuadas/readme.md) | 2024-2025 | 301b | mensual | sexo, servicio |  |  |
| [Referencias injustificadas](servicios/referencias/referencias_injustificadas/readme.md) | 2024-2025 | 301b | mensual | sexo, servicio |  |  |
| [Referencias inoportunas](servicios/referencias/referencias_inoportunas/readme.md) | 2024-2025 | 301b | mensual | sexo, servicio |  |  |
| [Referencias justificadas](servicios/referencias/referencias_justificadas/readme.md) | 2015-2025 | 301b | mensual | sexo, servicio |  |  |
| [Referencias oportunas](servicios/referencias/referencias_oportunas/readme.md) | 2015-2025 | 301b | mensual | sexo, servicio |  |  |
| [Referencias recibidas por el establecimiento](servicios/referencias/referencias_recibidas_por_el_establecimiento/readme.md) | 2024-2025 | 301b | mensual | sexo, servicio |  |  |
| [Transferencias realizadas a otros establecimientos](servicios/referencias/transferencias_realizadas_a_otros_establecimientos/readme.md) | 2024-2025 | 301b | mensual | sexo, servicio |  |  |

### Salud materna y neonatal

Control prenatal, partos, recién nacidos e interrupción legal del embarazo. 44 datasets.

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [ARO detectados](servicios/salud_materna_neonatal/aro_detectados/readme.md) | 2001-2003 | 301 | mensual |  |  |  |
| [ARO referidos](servicios/salud_materna_neonatal/aro_referidos/readme.md) | 2001-2003 | 301 | mensual |  |  |  |
| [Consultas prenatales (2001-2023)](servicios/salud_materna_neonatal/consulta_prenatal_2001_2023/readme.md) | 2001-2023 | 301, 301a | mensual | momento, edad, lugar | Este dataset cuenta por separado 3 categorías de momento: "nueva antes del 5.º mes", "nueva desde el 5.º mes" y "repetida". | Otros periodos: [2024-2025](servicios/salud_materna_neonatal/consulta_prenatal_2024_2025/readme.md). |
| [Consultas prenatales (2024-2025)](servicios/salud_materna_neonatal/consulta_prenatal_2024_2025/readme.md) | 2024-2025 | 301a | mensual | momento, edad, lugar | Este dataset cuenta por separado 4 categorías de momento: "nueva en el 1.er trimestre", "nueva en el 2.º trimestre", "nueva en el 3.er trimestre" y "repetida". | Otros periodos: [2001-2023](servicios/salud_materna_neonatal/consulta_prenatal_2001_2023/readme.md). |
| [Interrupciones legales del embarazo (2021-2023)](servicios/salud_materna_neonatal/interrupcion_legal_embarazo_2021_2023/readme.md) | 2021-2023 | 301a | mensual | causal, edad | Este dataset no separa por trimestre. Este dataset cuenta por separado 3 categorías de causal: "malformación congénita incompatible con la vida", "riesgo para la salud de la madre" y "violencia sexual". | Otros periodos: [2024-2025](servicios/salud_materna_neonatal/interrupcion_legal_embarazo_2024_2025/readme.md). |
| [Interrupciones legales del embarazo (2024-2025)](servicios/salud_materna_neonatal/interrupcion_legal_embarazo_2024_2025/readme.md) | 2024-2025 | 301a | mensual | causal, trimestre, edad | Este dataset cuenta por separado 3 categorías de causal: "malformación congénita incompatible con la vida", "riesgo para la salud de la madre" y "violencia sexual". Este dataset cuenta por separado 3 categorías de trimestre: "1.º", "2.º" y "3.º". | Otros periodos: [2021-2023](servicios/salud_materna_neonatal/interrupcion_legal_embarazo_2021_2023/readme.md). |
| [Mujeres con 4ta consulta prenatal](servicios/salud_materna_neonatal/mujeres_con_4ta_consulta_prenatal/readme.md) | 2001-2025 | 301, 301a | mensual | edad, lugar |  |  |
| [Mujeres con primer control post parto](servicios/salud_materna_neonatal/primer_control_post_parto/readme.md) | 2001-2014, 2021-2025 | 301, 301a | mensual | edad, lugar |  |  |
| [Mujeres con visita de control en las 48 hrs siguientes al parto](servicios/salud_materna_neonatal/mujeres_con_visita_de_control_en_las_48_hrs_siguientes_al_pa/readme.md) | 2015-2025 | 301a | mensual | edad, lugar |  |  |
| [Nacidos muertos](servicios/salud_materna_neonatal/nacidos_muertos/readme.md) | 2001-2025 | 301, 301a | mensual | lugar |  |  |
| [Nacidos muertos atendidos por otros](servicios/salud_materna_neonatal/nacidos_muertos_atendidos_por_otros/readme.md) | 2021-2025 | 301a | mensual | lugar |  |  |
| [Nacidos muertos atendidos por partera](servicios/salud_materna_neonatal/nacidos_muertos_atendidos_por_partera/readme.md) | 2015-2025 | 301a | mensual | lugar |  | [Nacidos muertos atendidos por partera capacitada](servicios/salud_materna_neonatal/nacidos_muertos_atendidos_por_partera_capacitada/readme.md). |
| [Nacidos muertos atendidos por partera capacitada](servicios/salud_materna_neonatal/nacidos_muertos_atendidos_por_partera_capacitada/readme.md) | 2001-2014 | 301 | mensual | lugar |  | [Nacidos muertos atendidos por partera](servicios/salud_materna_neonatal/nacidos_muertos_atendidos_por_partera/readme.md). |
| [Nacidos muertos atendidos por personal de salud](servicios/salud_materna_neonatal/nacidos_muertos_atendidos_por_personal_de_salud/readme.md) | 2001-2025 | 301, 301a | mensual | lugar |  |  |
| [Nacidos muertos con peso menor a 2500 g](servicios/salud_materna_neonatal/nacidos_muertos_con_peso_menor_a_2500g/readme.md) | 2001-2025 | 301, 301a | mensual | lugar |  |  |
| [Nacidos muertos prematuros 28 a < 37 semanas](servicios/salud_materna_neonatal/nacidos_muertos_prematuros_28_a_37_semanas/readme.md) | 2024-2025 | 301a | mensual | lugar |  |  |
| [Nacidos muertos prematuros < 28 semanas](servicios/salud_materna_neonatal/nacidos_muertos_prematuros_28_semanas/readme.md) | 2024-2025 | 301a | mensual | lugar |  |  |
| [Nacidos vivos](servicios/salud_materna_neonatal/nacidos_vivos/readme.md) | 2001-2025 | 301, 301a | mensual | lugar |  |  |
| [Nacidos vivos atendidos por otros](servicios/salud_materna_neonatal/nacidos_vivos_atendidos_por_otros/readme.md) | 2021-2025 | 301a | mensual | lugar |  |  |
| [Nacidos vivos atendidos por partera](servicios/salud_materna_neonatal/nacidos_vivos_atendidos_por_partera/readme.md) | 2015-2025 | 301a | mensual | lugar |  | [Nacidos vivos atendidos por partera capacitada u](servicios/salud_materna_neonatal/nacidos_vivos_atendidos_por_partera_capacitada_u/readme.md), [Nacidos vivos atendidos por partera capacitada](servicios/salud_materna_neonatal/nacidos_vivos_atendidos_por_partera_capacitada/readme.md). |
| [Nacidos vivos atendidos por partera capacitada](servicios/salud_materna_neonatal/nacidos_vivos_atendidos_por_partera_capacitada/readme.md) | 2008-2014 | 301 | mensual | lugar |  | [Nacidos vivos atendidos por partera capacitada u](servicios/salud_materna_neonatal/nacidos_vivos_atendidos_por_partera_capacitada_u/readme.md), [Nacidos vivos atendidos por partera](servicios/salud_materna_neonatal/nacidos_vivos_atendidos_por_partera/readme.md). |
| [Nacidos vivos atendidos por partera capacitada u](servicios/salud_materna_neonatal/nacidos_vivos_atendidos_por_partera_capacitada_u/readme.md) | 2001-2007 | 301 | mensual | lugar |  | [Nacidos vivos atendidos por partera capacitada](servicios/salud_materna_neonatal/nacidos_vivos_atendidos_por_partera_capacitada/readme.md), [Nacidos vivos atendidos por partera](servicios/salud_materna_neonatal/nacidos_vivos_atendidos_por_partera/readme.md). |
| [Nacidos vivos atendidos por personal de salud](servicios/salud_materna_neonatal/nacidos_vivos_atendidos_por_personal_de_salud/readme.md) | 2001-2025 | 301, 301a | mensual | lugar |  |  |
| [Nacidos vivos con peso menor a 2500 g](servicios/salud_materna_neonatal/nacidos_vivos_con_peso_menor_a_2500g/readme.md) | 2001-2025 | 301, 301a | mensual | lugar |  |  |
| [Nacidos vivos en mujeres de 15 a 49 años con 4 CPN](servicios/salud_materna_neonatal/nacidos_vivos_en_mujeres_de_15_a_49_anos_con_4_cpn/readme.md) | 2015-2025 | 301a | mensual | lugar |  |  |
| [Nacidos vivos prematuros 28 a < 37 semanas](servicios/salud_materna_neonatal/nacidos_vivos_prematuros_28_a_37_semanas/readme.md) | 2024-2025 | 301a | mensual | lugar |  |  |
| [Nacidos vivos prematuros < 28 semanas](servicios/salud_materna_neonatal/nacidos_vivos_prematuros_28_semanas/readme.md) | 2024-2025 | 301a | mensual | lugar |  |  |
| [Neonatos (de 7 a 28 días) a los que se les ha realizado tamizaje neonatal temprano](servicios/salud_materna_neonatal/neonatos_de_7_a_28_dias_a_los_que_se_les_ha_realizado_tamiza/readme.md) | 2024-2025 | 301a | mensual | sexo |  |  |
| [Neonatos (menor de 7 dias) a los que se les ha realizado tamizaje neonatal temprano](servicios/salud_materna_neonatal/neonatos_menor_de_7_dias_a_los_que_se_les_ha_realizado_tamiz/readme.md) | 2024-2025 | 301a | mensual | sexo |  |  |
| [Partos atendidos por otros](servicios/salud_materna_neonatal/partos_atendidos_por_otros/readme.md) | 2015-2025 | 301a | mensual | edad, lugar |  |  |
| [Partos atendidos por partera capacitada](servicios/salud_materna_neonatal/partos_atendidos_por_partera_capacitada/readme.md) | 2008-2025 | 301, 301a | mensual | edad, lugar |  | [Partos atendidos por partera capacitada u otra pe](servicios/salud_materna_neonatal/partos_atendidos_por_partera_capacitada_u_otra_pe/readme.md). |
| [Partos atendidos por partera capacitada u otra pe](servicios/salud_materna_neonatal/partos_atendidos_por_partera_capacitada_u_otra_pe/readme.md) | 2001-2007 | 301 | mensual | lugar |  | [Partos atendidos por partera capacitada](servicios/salud_materna_neonatal/partos_atendidos_por_partera_capacitada/readme.md). |
| [Partos atendidos por partera empirica](servicios/salud_materna_neonatal/partos_atendidos_por_partera_empirica/readme.md) | 2015-2025 | 301a | mensual | edad, lugar |  |  |
| [Partos atendidos por partera en servicio](servicios/salud_materna_neonatal/partos_atendidos_por_partera_en_servicio/readme.md) | 2015-2023 | 301a | mensual | lugar |  |  |
| [Partos atendidos por personal de salud](servicios/salud_materna_neonatal/partos_atendidos_por_personal_de_salud/readme.md) | 2001-2014 | 301 | mensual | lugar |  | [Partos atendidos por personal de salud calificado](servicios/salud_materna_neonatal/partos_atendidos_por_personal_de_salud_calificado/readme.md), [Partos atendidos por proveedor calificado](servicios/salud_materna_neonatal/partos_atendidos_por_proveedor_calificado/readme.md). |
| [Partos atendidos por personal de salud calificado](servicios/salud_materna_neonatal/partos_atendidos_por_personal_de_salud_calificado/readme.md) | 2015-2025 | 301a | mensual | edad, lugar |  | [Partos atendidos por personal de salud](servicios/salud_materna_neonatal/partos_atendidos_por_personal_de_salud/readme.md), [Partos atendidos por proveedor calificado](servicios/salud_materna_neonatal/partos_atendidos_por_proveedor_calificado/readme.md). |
| [Partos atendidos por personal de salud calificado y partera (articulacion)](servicios/salud_materna_neonatal/partos_atendidos_por_personal_de_salud_calificado_y_partera_/readme.md) | 2024-2025 | 301a | mensual | edad, lugar |  |  |
| [Partos atendidos por proveedor calificado](servicios/salud_materna_neonatal/partos_atendidos_por_proveedor_calificado/readme.md) | 2015-2025 | 301a | mensual | edad, lugar |  | [Partos atendidos por personal de salud](servicios/salud_materna_neonatal/partos_atendidos_por_personal_de_salud/readme.md), [Partos atendidos por personal de salud calificado](servicios/salud_materna_neonatal/partos_atendidos_por_personal_de_salud_calificado/readme.md). |
| [Partos vaginales y cesáreas](servicios/salud_materna_neonatal/partos/readme.md) | 2001-2025 | 301, 301a | mensual | vía del parto, edad, lugar | Este dataset cuenta por separado 2 categorías de vía del parto: "cesárea" y "vaginal". |  |
| [RN con alojamiento conjunto](servicios/salud_materna_neonatal/rn_con_alojamiento_conjunto/readme.md) | 2015-2025 | 301a | mensual | lugar |  |  |
| [RN con apego precoz](servicios/salud_materna_neonatal/rn_con_apego_precoz/readme.md) | 2015-2025 | 301a | mensual | lugar |  |  |
| [RN con corte tardío de cordón umbilical](servicios/salud_materna_neonatal/rn_con_corte_tardio_de_cordon_umbilical/readme.md) | 2021-2025 | 301a | mensual | lugar |  |  |
| [RN con malformación congénita](servicios/salud_materna_neonatal/rn_con_malformacion_congenita/readme.md) | 2015-2025 | 301a | mensual | lugar |  |  |
| [RN con visita de control en las 48 hrs siguientes al nacimiento](servicios/salud_materna_neonatal/rn_con_visita_de_control_en_las_48_hrs_siguientes_al_nacimie/readme.md) | 2015-2025 | 301a | mensual | lugar |  |  |

### Vacunas

Dosis de vacuna aplicadas. 32 datasets.

| Dataset | Gestiones | Formularios | Periodicidad | Desagregación | Comentario | Relacionados |
| --- | --- | --- | --- | --- | --- | --- |
| [Vacuna Antiamarílica (2001-2014)](servicios/vacunas/antiamarilica_2001_2014/readme.md) | 2001-2014 | 301 | mensual | edad, lugar | Este dataset no separa por dosis. | Otros periodos: [2015-2025](servicios/vacunas/antiamarilica_2015_2025/readme.md). |
| [Vacuna Antiamarílica (2015-2025)](servicios/vacunas/antiamarilica_2015_2025/readme.md) | 2015-2025 | 301a | mensual | dosis, sexo, edad, lugar | Este dataset cuenta una sola categoría de dosis: "única". | Otros periodos: [2001-2014](servicios/vacunas/antiamarilica_2001_2014/readme.md). |
| [Vacuna Antineumocócica (2010)](servicios/vacunas/antineumococica_2010/readme.md) | 2010 | 301 | mensual | dosis, edad, lugar | Este dataset cuenta por separado 2 categorías de dosis: "1" y "2". | Otros periodos: [2011-2025](servicios/vacunas/antineumococica_2011_2025/readme.md). |
| [Vacuna Antineumocócica (2011-2025)](servicios/vacunas/antineumococica_2011_2025/readme.md) | 2011-2025 | 301, 301a | mensual | dosis, sexo, edad, lugar | Este dataset cuenta por separado 3 categorías de dosis: "1", "2" y "3". | Otros periodos: [2010](servicios/vacunas/antineumococica_2010/readme.md). |
| [Vacuna Antipoliomielítica (2001-2003)](servicios/vacunas/antipoliomielitica_2001_2003/readme.md) | 2001-2003 | 301 | mensual | dosis, edad, lugar | Este dataset cuenta por separado 4 categorías de dosis: "1", "2", "3" y "inicial". | Otros periodos: [2004-2009](servicios/vacunas/antipoliomielitica_2004_2009/readme.md), [2010-2025](servicios/vacunas/antipoliomielitica_2010_2025/readme.md). |
| [Vacuna Antipoliomielítica (2004-2009)](servicios/vacunas/antipoliomielitica_2004_2009/readme.md) | 2004-2009 | 301 | mensual | dosis, edad, lugar | Este dataset cuenta por separado 3 categorías de dosis: "1", "2" y "3". | Otros periodos: [2001-2003](servicios/vacunas/antipoliomielitica_2001_2003/readme.md), [2010-2025](servicios/vacunas/antipoliomielitica_2010_2025/readme.md). |
| [Vacuna Antipoliomielítica (2010-2025)](servicios/vacunas/antipoliomielitica_2010_2025/readme.md) | 2010-2025 | 301, 301a | mensual | dosis, sexo, edad, lugar | Este dataset cuenta por separado 5 categorías de dosis: "1", "2", "3", "4" y "5". | Otros periodos: [2001-2003](servicios/vacunas/antipoliomielitica_2001_2003/readme.md), [2004-2009](servicios/vacunas/antipoliomielitica_2004_2009/readme.md). |
| [Vacuna Antirrotavírica (2008-2009)](servicios/vacunas/antirrotavirica_2008_2009/readme.md) | 2008-2009 | 301 | mensual | dosis, edad, lugar | Este dataset cuenta por separado 3 categorías de dosis: "1", "2" y "3". | Otros periodos: [2010-2025](servicios/vacunas/antirrotavirica_2010_2025/readme.md). |
| [Vacuna Antirrotavírica (2010-2025)](servicios/vacunas/antirrotavirica_2010_2025/readme.md) | 2010-2025 | 301, 301a | mensual | dosis, sexo, edad, lugar | Este dataset cuenta por separado 2 categorías de dosis: "1" y "2". | Otros periodos: [2008-2009](servicios/vacunas/antirrotavirica_2008_2009/readme.md). |
| [Vacuna BCG](servicios/vacunas/bcg/readme.md) | 2001-2025 | 301, 301a | mensual | sexo, edad, lugar |  |  |
| [Vacuna COVID-19 (2021)](servicios/vacunas/covid_19_2021/readme.md) | 2021 | 301a | mensual | dosis, sexo, lugar | Este dataset no separa por grupo de población. Este dataset cuenta por separado 4 categorías de dosis: "1", "2", "refuerzo" y "única". | Otros periodos: [2022](servicios/vacunas/covid_19_2022/readme.md), [2023](servicios/vacunas/covid_19_2023/readme.md), [2024-2025](servicios/vacunas/covid_19_2024_2025/readme.md). |
| [Vacuna COVID-19 (2022)](servicios/vacunas/covid_19_2022/readme.md) | 2022 | 301a | mensual | dosis, sexo, lugar | Este dataset no separa por grupo de población. Este dataset cuenta por separado 5 categorías de dosis: "1", "2", "3", "4" y "única". | Otros periodos: [2021](servicios/vacunas/covid_19_2021/readme.md), [2023](servicios/vacunas/covid_19_2023/readme.md), [2024-2025](servicios/vacunas/covid_19_2024_2025/readme.md). |
| [Vacuna COVID-19 (2023)](servicios/vacunas/covid_19_2023/readme.md) | 2023 | 301a | mensual | dosis, sexo, lugar | Este dataset no separa por grupo de población. Este dataset cuenta por separado 6 categorías de dosis: "1", "2", "3", "4", "refuerzo" y "única". | Otros periodos: [2021](servicios/vacunas/covid_19_2021/readme.md), [2022](servicios/vacunas/covid_19_2022/readme.md), [2024-2025](servicios/vacunas/covid_19_2024_2025/readme.md). |
| [Vacuna COVID-19 (2024-2025)](servicios/vacunas/covid_19_2024_2025/readme.md) | 2024-2025 | 301a | mensual | dosis, grupo de población, sexo, edad, lugar | Este dataset cuenta por separado 5 categorías de dosis: "1", "2", "3", "anual" y "única". Este dataset cuenta una sola categoría de grupo de población: "personas inmunodeprimidas". | Otros periodos: [2021](servicios/vacunas/covid_19_2021/readme.md), [2022](servicios/vacunas/covid_19_2022/readme.md), [2023](servicios/vacunas/covid_19_2023/readme.md). |
| [Vacuna DPT (2001-2007)](servicios/vacunas/dpt_2001_2007/readme.md) | 2001-2007 | 301 | mensual | dosis, edad | Este dataset cuenta una sola categoría de dosis: "3". | Otros periodos: [2010-2014](servicios/vacunas/dpt_2010_2014/readme.md). |
| [Vacuna DPT (2010-2014)](servicios/vacunas/dpt_2010_2014/readme.md) | 2010-2014 | 301 | mensual | dosis, edad, lugar | Este dataset cuenta por separado 5 categorías de dosis: "1", "2", "3", "4" y "5". | Otros periodos: [2001-2007](servicios/vacunas/dpt_2001_2007/readme.md). |
| [Vacuna Hepatitis B (2010-2014)](servicios/vacunas/hepatitis_b_2010_2014/readme.md) | 2010-2014 | 301 | mensual | dosis, grupo de población, lugar | Este dataset cuenta por separado 3 categorías de dosis: "1", "2" y "3". Este dataset cuenta una sola categoría de grupo de población: "personal de salud". | Otros periodos: [2015-2020](servicios/vacunas/hepatitis_b_2015_2020/readme.md), [2021-2025](servicios/vacunas/hepatitis_b_2021_2025/readme.md). |
| [Vacuna Hepatitis B (2015-2020)](servicios/vacunas/hepatitis_b_2015_2020/readme.md) | 2015-2020 | 301a | mensual | dosis, grupo de población, sexo, lugar | Este dataset cuenta por separado 3 categorías de dosis: "1", "2" y "3". Este dataset cuenta por separado 2 categorías de grupo de población: "personal de salud" y "personas con VIH". | Otros periodos: [2010-2014](servicios/vacunas/hepatitis_b_2010_2014/readme.md), [2021-2025](servicios/vacunas/hepatitis_b_2021_2025/readme.md). |
| [Vacuna Hepatitis B (2021-2025)](servicios/vacunas/hepatitis_b_2021_2025/readme.md) | 2021-2025 | 301a | mensual | dosis, grupo de población, sexo, edad, lugar | Este dataset cuenta por separado 3 categorías de dosis: "1", "2" y "3". Este dataset cuenta por separado 3 categorías de grupo de población: "personal de salud", "personas con VIH" y "personas con enfermedad renal". | Otros periodos: [2010-2014](servicios/vacunas/hepatitis_b_2010_2014/readme.md), [2015-2020](servicios/vacunas/hepatitis_b_2015_2020/readme.md). |
| [Vacuna Influenza estacional (2015-2023)](servicios/vacunas/influenza_estacional_2015_2023/readme.md) | 2015-2023 | 301a | mensual | dosis, grupo de población, sexo, edad, lugar | Este dataset cuenta por separado 3 categorías de dosis: "1", "2" y "única". Este dataset cuenta por separado 4 categorías de grupo de población: "embarazadas", "personal de salud", "personas con enfermedad crónica" y "personas de 60 años y más". | Otros periodos: [2024-2025](servicios/vacunas/influenza_estacional_2024_2025/readme.md). |
| [Vacuna Influenza estacional (2024-2025)](servicios/vacunas/influenza_estacional_2024_2025/readme.md) | 2024-2025 | 301a | mensual | dosis, grupo de población, sexo, edad, lugar | Este dataset cuenta por separado 3 categorías de dosis: "1", "2" y "única". Este dataset cuenta por separado 3 categorías de grupo de población: "embarazadas", "personal de salud" y "personas con enfermedad crónica". | Otros periodos: [2015-2023](servicios/vacunas/influenza_estacional_2015_2023/readme.md). |
| [Vacuna Pentavalente (2001-2014)](servicios/vacunas/pentavalente_2001_2014/readme.md) | 2001-2014 | 301 | mensual | dosis, edad, lugar | Este dataset cuenta por separado 3 categorías de dosis: "1", "2" y "3". | Otros periodos: [2015-2025](servicios/vacunas/pentavalente_2015_2025/readme.md). |
| [Vacuna Pentavalente (2015-2025)](servicios/vacunas/pentavalente_2015_2025/readme.md) | 2015-2025 | 301a | mensual | dosis, sexo, edad, lugar | Este dataset cuenta por separado 5 categorías de dosis: "1", "2", "3", "4" y "5". | Otros periodos: [2001-2014](servicios/vacunas/pentavalente_2001_2014/readme.md). |
| [Vacuna SR (sarampión y rubéola)](servicios/vacunas/sr/readme.md) | 2001-2007, 2021-2025 | 301, 301a | mensual | sexo, edad, lugar |  |  |
| [Vacuna SRP (sarampión, rubéola y parotiditis) (2001-2009)](servicios/vacunas/srp_2001_2009/readme.md) | 2001-2009 | 301 | mensual | edad, lugar | Este dataset no separa por dosis. | Otros periodos: [2010-2017](servicios/vacunas/srp_2010_2017/readme.md), [2018-2025](servicios/vacunas/srp_2018_2025/readme.md). |
| [Vacuna SRP (sarampión, rubéola y parotiditis) (2010-2017)](servicios/vacunas/srp_2010_2017/readme.md) | 2010-2017 | 301, 301a | mensual | dosis, sexo, edad, lugar | Este dataset cuenta una sola categoría de dosis: "única". | Otros periodos: [2001-2009](servicios/vacunas/srp_2001_2009/readme.md), [2018-2025](servicios/vacunas/srp_2018_2025/readme.md). |
| [Vacuna SRP (sarampión, rubéola y parotiditis) (2018-2025)](servicios/vacunas/srp_2018_2025/readme.md) | 2018-2025 | 301a | mensual | dosis, sexo, edad, lugar | Este dataset cuenta por separado 2 categorías de dosis: "1" y "2". | Otros periodos: [2001-2009](servicios/vacunas/srp_2001_2009/readme.md), [2010-2017](servicios/vacunas/srp_2010_2017/readme.md). |
| [Vacuna VPH (virus del papiloma humano) (2018-2023)](servicios/vacunas/vph_2018_2023/readme.md) | 2018-2023 | 301a | mensual | dosis, grupo de población, sexo, lugar | Este dataset cuenta por separado 2 categorías de dosis: "1" y "2". Este dataset cuenta una sola categoría de grupo de población: "niñas de 10 años". | Otros periodos: [2024-2025](servicios/vacunas/vph_2024_2025/readme.md). |
| [Vacuna VPH (virus del papiloma humano) (2024-2025)](servicios/vacunas/vph_2024_2025/readme.md) | 2024-2025 | 301a | mensual | dosis, sexo, edad, lugar | Este dataset no separa por grupo de población. Este dataset cuenta una sola categoría de dosis: "1". | Otros periodos: [2018-2023](servicios/vacunas/vph_2018_2023/readme.md). |
| [Vacuna dT (difteria y tétanos) (2001-2003)](servicios/vacunas/dt_2001_2003/readme.md) | 2001-2003 | 301 | mensual | dosis, sexo, edad | Este dataset cuenta por separado 5 categorías de dosis: "1", "2", "3", "4" y "5". | Otros periodos: [2004-2007](servicios/vacunas/dt_2004_2007/readme.md), [2008-2025](servicios/vacunas/dt_2008_2025/readme.md). |
| [Vacuna dT (difteria y tétanos) (2004-2007)](servicios/vacunas/dt_2004_2007/readme.md) | 2004-2007 | 301 | mensual | dosis, sexo, edad | Este dataset cuenta por separado 3 categorías de dosis: "1", "2" y "5". | Otros periodos: [2001-2003](servicios/vacunas/dt_2001_2003/readme.md), [2008-2025](servicios/vacunas/dt_2008_2025/readme.md). |
| [Vacuna dT (difteria y tétanos) (2008-2025)](servicios/vacunas/dt_2008_2025/readme.md) | 2008-2025 | 301, 301a | mensual | dosis, sexo, edad, lugar | Este dataset cuenta por separado 5 categorías de dosis: "1", "2", "3", "4" y "5". | Otros periodos: [2001-2003](servicios/vacunas/dt_2001_2003/readme.md), [2004-2007](servicios/vacunas/dt_2004_2007/readme.md). |

## Referencias

- [Municipios](../referencias/municipios/readme.md): código, nombre, provincia y departamento de cada municipio.

## Cómo leer los datos

### Formularios

Cada establecimiento informa al SNIS con formularios mensuales o semanales. En servicios, el formulario 301
(2001-2014) registra todos los servicios. Desde 2015 se divide en dos registros complementarios: el 301a, para
los servicios de primer nivel, y el 301b, para los de segundo y tercer nivel. El nivel es del servicio, no del
establecimiento: un hospital informa en los dos. Por eso un dataset nunca une el 301a con el 301b. Si una
variable tiene el mismo nombre en los dos (los sueros de enfermería), el dataset del 301b lleva "(formulario
301b)" en el nombre. Una variable del 301 continúa en el dataset del 301a con el mismo nombre o, si sólo está
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
banda "1 a 4 años" es `edad_desde = 1` y `edad_hasta = 5`. `edad_grupo` repite la banda en texto corto. Las
bandas cambian entre gestiones: para comparar gestiones, agrupe en bandas compatibles. `caso` dice si la
atención es nueva o repetida, como la registra el formulario. `lugar` dice si ocurrió dentro o fuera del
establecimiento.

### Ceros y totales

El SNIS registra eventos, no ausencias, y no distingue "cero casos" de "no notificó". Por eso los datasets no
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

El readme de cada dataset enlaza, en "Datasets relacionados", los datasets que cuentan algo parecido con otras
categorías, otra definición, otro nombre u otro formulario. Dice qué cambia y qué supone unirlos, y da la
consulta para hacerlo. En el catálogo, la columna "Comentario" resume lo que distingue a cada dataset (sus
categorías y sus datasets relacionados) y sus advertencias.

En el formulario 302 de 2001 a 2003, algunas enfermedades aparecen en dos secciones con cifras distintas. Son
datasets separados y el readme de cada uno enlaza al otro. No sume los dos: un caso puede estar en ambos.

### Registros implausibles

Algunas filas tienen una población que la definición excluye: por ejemplo, cáncer de próstata en mujeres. Se
publican tal como se registraron, porque no hay información para saber si son errores ni de qué tipo. El readme
de cada dataset las lista en "Advertencias", con su volumen, para que quien analiza decida si las excluye.

### Códigos CIE-10 y SOAPS

SOAPS es el software de atención primaria del SNIS. Sus reglas dicen qué diagnósticos (códigos CIE-10) y qué
poblaciones cuenta cada variable. El readme de cada dataset da, por gestión, la versión de SOAPS que describe la
variable y las categorías CIE-10. SOAPS existe desde 2013 (versión 1.0.4): para las gestiones anteriores, la
versión asignada es la más parecida por nombre y poblaciones, y sus códigos son una aproximación. Las
defunciones tienen códigos internos de SOAPS, no CIE-10.

### Correcciones de rótulos

Cada columna del tablero tiene un encabezado de hasta tres niveles, separados por " | ": en "e. 10 a 14 años - F | NUEVO", el primer nivel da la edad y el sexo, y el segundo, si el caso es nuevo. El tablero arma estos encabezados con plantillas, y en algunos grupos de variables la plantilla no describe las columnas: por ejemplo, rotula "nuevo" y "repetido" columnas que en realidad son el sexo. Cada corrección se apoya en evidencia de los datos, de SOAPS o de los instructivos, y el readme de cada dataset dice cuáles se aplicaron. Lista completa:

- 301a, vacunas de 12 a 23 meses, de 2 a 3 años y de 4 años, 2015-2023: el segundo nivel dice DENTRO/FUERA otra vez, pero las reglas de SOAPS 6.0.1 dividen estas variables por sexo y lugar (código 3012805). El segundo nivel "DENTRO" suma 50,6 % y la proporción de varones en las vacunas rotuladas por sexo es 50,9 %: DENTRO es hombre y FUERA es mujer.
- 301 y 301a, tratamientos de chagas, leishmaniasis y en mujeres posparto: el tablero repite las columnas de sexo ("FEMENINO" y "FEMENINO.1"). En 2020 los totales dicen "TOTAL Iniciado" y "TOTAL Concluido", y coinciden con la primera y la segunda columna: la primera es tratamiento iniciado y la repetida, concluido.
- 301b, actividades de enfermería, 2024-2025: cada variable tiene tres columnas sin rótulo ("Sueros", "Sueros1", "Sueros2") que suman el total. El formulario 301b de 2024 tiene, en ese orden, las columnas emergencias, consulta externa e internación, y el instructivo de 2024 nombra los mismos servicios: se publican como esos servicios.
- 301a, anticoncepción y prevención del cáncer (2015-2016) e interrupción legal del embarazo (2021): las variables tienen cinco columnas sin rótulo ("Número de condones entregados", "...1" a "...4"). Son las bandas de edad <15, 15-19, 20-34, 35-49 y 50+, en ese orden. En anticoncepción las proporciones coinciden con las de 2017 (muestras de PAP 2016: 0,3 %, 7,1 %, 48,5 %, 32,0 % y 12,2 %; 2017: 0,3 %, 7,1 %, 48,4 %, 31,7 % y 12,5 %). En la interrupción legal del embarazo, el encabezado de 2022 une cada columna numerada con su banda ("A. < 15", "B. 15 A 19 ... 1"). En 2022 la segunda banda de las causales riesgo de salud de la madre y malformación dice "15 A 49"; es 15-19.
- 301, control de crecimiento, 2008-2009: el primer nivel dice siempre NUEVO; el segundo dice NUEVO/REPETIDO y sus totales coinciden con "TOTAL NUEVO" y "TOTAL REPETIDO": vale el segundo.
- 302b, grupos 01, 05, 06, 07 y 10: el segundo nivel dice NUEVO/REPETIDO, pero las reglas de SOAPS dividen estas variables por sexo. Las muertes por cáncer de mama y de cuello uterino están en REPETIDO en todas las gestiones 2016-2025, y el tabaco y el alcohol (grupo 01, 2024-2025) están sobre todo en NUEVO: REPETIDO es mujer y NUEVO es hombre.
- 302b, grupo 06: la columna Embarazada se divide en 10-19 y 20-59 años (reglas de SOAPS para el código 3050604). La columna menor es 10-19: NUEVO o MASCULINO es 10-19; REPETIDO o FEMENINO es 20-59.
- 302 (grupos 11 y 14, 2008-2014) y 302b (grupos 06 y 07): SOAPS cuenta la columna "Menor de 1 año" desde los 2 meses (reglas de 2 a 11 meses).
- 302a, grupo 10, 2024-2025: el segundo nivel dice FEMENINO/MASCULINO, pero SOAPS 7.0.1 divide por lugar. Las complicaciones atendidas dentro del establecimiento son muchas más que fuera (preeclampsia 2025: 2.513 frente a 137): MASCULINO es dentro y FEMENINO es fuera.
- 302, 2001-2007: en las variables cuyas columnas "-M" siempre valen 0, "TOTAL-H" es igual a "TOTAL": "-H" contiene a ambos sexos. Esas variables no tienen sexo. En 2004 el grupo 09 (mortalidad) tampoco tiene sexo: hay 79 muertes maternas en "-H" y 94 en "-M".
- 302, grupo 13 (intoxicaciones), 2001-2003: la variable tiene una sola columna, "TOTAL-M". Se publica sin sexo, como total. Evidencia: la magnitud es la de un total de ambos sexos. Organofosforados suma de 1.700 a 2.208 por gestión en 2001-2003, y plaguicidas, sin sexo, suma 2.170 en 2004 y 2.077 en 2005.
- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
- 302a, grupo 09, 2021-2025: el encabezado repite "f. 15 - 19 años - F" (pandas lo marca con ".1") y desplaza una posición a todas las columnas siguientes. La columna repetida es "g. 20 - 39 años - D" y cada etiqueta siguiente corresponde a la posición que le sigue. La última etiqueta ("j. 60 años y más - F") no tiene columna propia: en los 15 archivos del grupo 09 de 2021-2025 repite, fila por fila, la primera columna ("a. Menor de 6 meses - D").
