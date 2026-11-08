# Parálisis flácida aguda

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | semanal |
| Municipios con registros | 93 |
| Desagregación | sexo, edad |
| Filas | 805 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001 | 1-4, 5-14, 15-59, 60+ |
| 2002 | <1, 1-4, 5-14, 15-59 |
| 2003 | 1-4, 5-14 |
| 2004-2005 | <1, 1-4, 5-14, 15-59, 60+ |
| 2006-2007 | <1, 1-4, 5-14, 15-59 |
| 2008-2009 | <1, 1-4, 5-9, 10-20, 21-59 |
| 2010 | 1-4, 5-9, 10-20 |
| 2011 | <1, 1-4, 5-9, 10-20, 21-59 |
| 2012 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |
| 2013-2014 | <1, 1-4, 5-9, 10-20, 21-59 |
| 2015 | 1-4, 5-9, 10-14, 20-39 |
| 2016 | <6m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2017 | 1-4, 5-9, 10-14, 20-39, 40-49, 60+ |
| 2018 | 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2019 | 1-4, 5-9, 10-14, 20-39, 40-49, 50-59, 60+ |
| 2020 | <6m, 6-11m, 1-4, 5-9, 10-14 |
| 2021 | 6-11m, 1-4, 5-9, 10-14, 20-39, 40-49 |
| 2022 | 6-11m, 1-4, 5-9, 10-14, 20-39, 40-49, 50-59, 60+ |
| 2023 | 1-4, 5-9, 10-14, 20-39, 40-49, 50-59, 60+ |
| 2024 | 1-4, 5-9, 10-14, 20-39, 40-49 |
| 2025 | 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2001 | 143 |
| 2002 | 42 |
| 2003 | 37 |
| 2004 | 35 |
| 2005 | 40 |
| 2006 | 27 |
| 2007 | 15 |
| 2008 | 20 |
| 2009 | 23 |
| 2010 | 24 |
| 2011 | 30 |
| 2012 | 34 |
| 2013 | 44 |
| 2014 | 42 |
| 2015 | 27 |
| 2016 | 26 |
| 2017 | 20 |
| 2018 | 43 |
| 2019 | 23 |
| 2020 | 14 |
| 2021 | 16 |
| 2022 | 45 |
| 2023 | 39 |
| 2024 | 54 |
| 2025 | 41 |

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
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/paralisis_flacida_aguda/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/paralisis_flacida_aguda/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/paralisis_flacida_aguda/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2001-2003 | 302 | 40.- Parálisis Flácida |  |  |
| 2004 | 302 | 5 Parálisis flácida aguda | 1.0.4 (2013) | A80 |
| 2005-2009 | 302 | 4 Parálisis flácida aguda | 1.0.4 (2013) | A80 |
| 2010-2013 | 302 | Parálisis flácida aguda (Polio) | 1.0.4 (2013) | A80 |
| 2014 | 302 | Parálisis flácida aguda (Polio) | 2.0.0 (2014) | A80 |
| 2015 | 302a | Parálisis flácida aguda (Polio) | 3.0.1 (2016) | A80 |
| 2016 | 302a | Parálisis flácida aguda (Polio) | 3.0.2 (2016) | A80 |
| 2017 | 302a | Parálisis flácida aguda (Polio) | 4.0.0 (2018) | A80 |
| 2018 | 302a | Parálisis flácida aguda (Polio) | 4.0.1 (2018) | A80 |
| 2019-2020 | 302a | Parálisis flácida aguda (Polio) | 5.0.1 (2020) | A80 |
| 2021 | 302a | Parálisis flácida aguda (Polio) | 6.0.0 (2021) | A80 |
| 2022-2023 | 302a | Parálisis flácida aguda (Polio) | 6.0.1 (2022) | A80 |
| 2024 | 302a | Parálisis flácida aguda (Polio) | 7.0.1 (2026) | A80 |
| 2025 | 302a | 05. Parálisis flácida aguda (Polio) | 7.0.1 (2026) | A80 |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302, 2001-2007: en las variables cuyas columnas "-M" siempre valen 0, "TOTAL-H" es igual a "TOTAL": "-H" contiene a ambos sexos. Esas variables no tienen sexo. En 2004 el grupo 09 (mortalidad) tampoco tiene sexo: hay 79 muertes maternas en "-H" y 94 en "-M".
