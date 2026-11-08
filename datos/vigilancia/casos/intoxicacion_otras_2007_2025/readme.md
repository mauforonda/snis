# Otras intoxicaciones (drogas, fármacos, alcohol) (2007-2025)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2007-2025. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2007-2025 |
| Periodicidad | semanal |
| Municipios con registros | 331 |
| Desagregación | agente, sexo, edad |
| Filas | 65.845 |

Valores de `agente` (agente):

- drogas, fármacos, alcohol y otras (2007-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2008-2014 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |
| 2016-2025 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2007 | 2.507 |
| 2008 | 6.559 |
| 2009 | 7.458 |
| 2010 | 8.028 |
| 2011 | 8.742 |
| 2012 | 8.385 |
| 2013 | 10.110 |
| 2014 | 9.564 |
| 2015 | 8.042 |
| 2016 | 9.365 |
| 2017 | 19.393 |
| 2018 | 21.621 |
| 2019 | 9.687 |
| 2020 | 4.991 |
| 2021 | 5.771 |
| 2022 | 6.083 |
| 2023 | 7.509 |
| 2024 | 8.374 |
| 2025 | 9.101 |

## Cómo utilizar

Cada fila da el número de casos de un periodo, un municipio y una población. Para obtener un total, sume las filas: el dataset no tiene filas de total. Una combinación sin fila significa que no hubo registros. Las convenciones de tiempo, territorio y población están en el [catálogo](../../../README.md#cómo-leer-los-datos).

| Columna | Tipo | Descripción |
| --- | --- | --- |
| `gestion` | integer | Año calendario (gestión) del registro. |
| `semana` | integer | Semana epidemiológica, de 1 a 53. Va de domingo a sábado. |
| `fecha_inicio` | date | Primer día de la semana o del mes. |
| `departamento` | string | Nombre del departamento. |
| `municipio` | string | Nombre del municipio. |
| `municipio_codigo` | string | Código del municipio, 6 dígitos: departamento (2), provincia (2) y municipio (2). |
| `agente` | string | Agente de la intoxicación. |
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/intoxicacion_otras_2007_2025/datos.parquet'
group by gestion order by gestion;

-- Por gestión y agente
select gestion, agente, sum(casos) as casos
from 'datos/vigilancia/casos/intoxicacion_otras_2007_2025/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/intoxicacion_otras_2007_2025/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Otras intoxicaciones (2001-2003)](../../../vigilancia/casos/intoxicacion_otras_2001_2003/readme.md): 2001-2003, formulario 302.
- Otras intoxicaciones (drogas, fármacos, alcohol) (2007-2025) (este dataset): 2007-2025, formulario 302, 302a.

Las categorías de `agente` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/intoxicacion_otras_2001_2003/datos.parquet',
    'datos/vigilancia/casos/intoxicacion_otras_2007_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2007 | 302 | 57 Otras intoxicaciones |  |  |
| 2008-2009 | 302 | 36 Otras intoxicaciones (drogas, farmacos, alcohol, leer instructivo) | 1.0.4 (2013) | T36 T37 T38 T39 T40 T41 T42 T43 T44 T45 T46 T47 T48 T49 T50 T51 T52 T53 T54 T55 T56 T57 T58 T59 T60 T61 T62 T63 T64 T65 |
| 2010-2013 | 302 | Otras intoxicaciones (drogas, farmacos, etc.) | 1.0.4 (2013) | T36 T37 T38 T39 T40 T41 T42 T43 T44 T45 T46 T47 T48 T49 T50 T51 T52 T53 T54 T55 T56 T57 T58 T59 T60 T61 T62 T63 T64 T65 |
| 2014 | 302 | Otras intoxicaciones (drogas, farmacos, etc.) | 2.0.0 (2014) | T36 T37 T38 T39 T40 T41 T42 T43 T44 T45 T46 T47 T48 T49 T50 T51 T52 T53 T54 T55 T56 T57 T58 T59 T60 T61 T62 T63 T64 T65 |
| 2015 | 302a | Otras intoxicaciones (drogas, fármacos, alcohol etc.) | 3.0.1 (2016) | T36 T37 T38 T39 T40 T41 T42 T43 T44 T45 T46 T47 T48 T49 T50 T51 T52 T53 T54 T55 T56 T57 T58 T59 T61 T62 T63 T65 |
| 2016 | 302a | Otras intoxicaciones (drogas, fármacos, alcohol etc.) | 3.0.2 (2016) | T36 T37 T38 T39 T40 T41 T42 T43 T44 T45 T46 T47 T48 T49 T50 T51 T52 T53 T54 T55 T56 T57 T58 T59 T61 T62 T63 T65 |
| 2017 | 302a | Otras intoxicaciones (drogas, fármacos, alcohol etc.) | 4.0.0 (2018) | T36 T37 T38 T39 T40 T41 T42 T43 T44 T45 T46 T47 T48 T49 T50 T51 T52 T53 T54 T55 T56 T57 T58 T59 T61 T62 T63 T65 |
| 2018 | 302a | Otras intoxicaciones (drogas, fármacos, alcohol etc.) | 4.0.1 (2018) | T36 T37 T38 T39 T40 T41 T42 T43 T44 T45 T46 T47 T48 T49 T50 T51 T52 T53 T54 T55 T56 T57 T58 T59 T61 T62 T63 T65 |
| 2019-2020 | 302a | Otras intoxicaciones (drogas, fármacos, alcohol etc.) | 5.0.1 (2020) | T36 T37 T38 T39 T40 T41 T42 T43 T44 T45 T46 T47 T48 T49 T50 T51 T52 T53 T54 T55 T56 T57 T58 T59 T61 T62 T63 T65 |
| 2021 | 302a | Otras intoxicaciones (drogas, fármacos, alcohol etc.) | 6.0.0 (2021) | T36 T37 T38 T39 T40 T41 T42 T43 T44 T45 T46 T47 T48 T49 T50 T51 T52 T53 T54 T55 T56 T57 T58 T59 T61 T62 T63 T65 |
| 2022-2023 | 302a | Otras intoxicaciones (drogas, fármacos, alcohol etc.) | 6.0.1 (2022) | T36 T37 T38 T39 T40 T41 T42 T43 T44 T45 T46 T47 T48 T49 T50 T51 T52 T53 T54 T55 T56 T57 T58 T59 T61 T62 T63 T65 |
| 2024-2025 | 302a | 6. Otras intoxicaciones (drogas, fármacos, alcohol etc.) | 7.0.1 (2026) | T36 T37 T38 T39 T40 T41 T42 T43 T44 T45 T46 T47 T48 T49 T50 T51 T52 T53 T54 T55 T56 T57 T58 T59 T65 X40 X41 X42 X43 X44 X45 X46 X47 X49 |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
