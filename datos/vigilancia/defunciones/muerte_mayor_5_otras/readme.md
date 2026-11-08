# Otras muertes en mayores de 5 años

Muertes por esta causa en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | semanal |
| Municipios con registros | 342 |
| Desagregación | sexo, edad, lugar |
| Filas | 216.965 |

Valores de `lugar` (lugar):

- dentro (2001-2003, 2005-2025)
- fuera (2005-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015-2025 | 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Defunciones |
| ---: | ---: |
| 2001 | 1.828 |
| 2002 | 2.752 |
| 2003 | 3.849 |
| 2004 | 8.171 |
| 2005 | 8.391 |
| 2006 | 9.306 |
| 2007 | 9.971 |
| 2008 | 10.810 |
| 2009 | 12.532 |
| 2010 | 14.649 |
| 2011 | 15.129 |
| 2012 | 16.585 |
| 2013 | 18.302 |
| 2014 | 17.212 |
| 2015 | 18.400 |
| 2016 | 21.190 |
| 2017 | 23.080 |
| 2018 | 24.902 |
| 2019 | 25.276 |
| 2020 | 40.511 |
| 2021 | 40.493 |
| 2022 | 36.987 |
| 2023 | 36.181 |
| 2024 | 36.575 |
| 2025 | 40.136 |

## Cómo utilizar

Cada fila da el número de defunciones de un periodo, un municipio y una población. Para obtener un total, sume las filas: el dataset no tiene filas de total. Una combinación sin fila significa que no hubo registros. Las convenciones de tiempo, territorio y población están en el [catálogo](../../../README.md#cómo-leer-los-datos).

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
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `defunciones` | integer | Número de defunciones en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_mayor_5_otras/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_mayor_5_otras/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_mayor_5_otras/datos.parquet'
where gestion = 2025 group by all order by defunciones desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2003 | 302 | 76.- Otras muertes en personas mayores de 5 años | 1.0.4 (2013) |
| 2004 | 302 | 43 Otras muertes en personas mayores de 5 años |  |
| 2005-2007 | 302 | 44 Otras muertes en personas mayores de 5 años | 1.0.4 (2013) |
| 2008-2009 | 302 | 43 Otras muertes en mayores de 5 años | 1.0.4 (2013) |
| 2010-2013 | 302 | Otras muertes en mayores de 5 años | 1.0.4 (2013) |
| 2014 | 302 | Otras muertes en mayores de 5 años | 2.0.0 (2014) |
| 2015 | 302a | Otras muertes en mayores de 5 años | 3.0.1 (2016) |
| 2016 | 302a | Otras muertes en mayores de 5 años | 3.0.2 (2016) |
| 2017 | 302a | Otras muertes en mayores de 5 años | 4.0.0 (2018) |
| 2018 | 302a | Otras muertes en mayores de 5 años | 4.0.1 (2018) |
| 2019-2020 | 302a | Otras muertes en mayores de 5 años | 5.0.1 (2020) |
| 2021 | 302a | Otras muertes en mayores de 5 años | 6.0.0 (2021) |
| 2022-2023 | 302a | Otras muertes en mayores de 5 años | 6.0.1 (2022) |
| 2024 | 302a | 5. Otras muertes en mayores de 5 años | 6.0.1 (2022) |
| 2025 | 302a | 5. Otras muertes en mayores de 5 años | 7.0.1 anterior (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302, 2001-2007: en las variables cuyas columnas "-M" siempre valen 0, "TOTAL-H" es igual a "TOTAL": "-H" contiene a ambos sexos. Esas variables no tienen sexo. En 2004 el grupo 09 (mortalidad) tampoco tiene sexo: hay 79 muertes maternas en "-H" y 94 en "-M".
- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
- 302a, grupo 09, 2021-2025: el encabezado repite "f. 15 - 19 años - F" (pandas lo marca con ".1") y desplaza una posición a todas las columnas siguientes. La columna repetida es "g. 20 - 39 años - D" y cada etiqueta siguiente corresponde a la posición que le sigue. La última etiqueta ("j. 60 años y más - F") no tiene columna propia: en los 15 archivos del grupo 09 de 2021-2025 repite, fila por fila, la primera columna ("a. Menor de 6 meses - D").
