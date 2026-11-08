# Sospecha de muerte por dengue

Muertes por esta causa en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2021-2025. Fuente: SNIS, formularios 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2021-2025 |
| Periodicidad | semanal |
| Municipios con registros | 58 |
| Desagregación | sexo, edad, lugar |
| Filas | 318 |

Valores de `lugar` (lugar):

- dentro (2021-2025)
- fuera (2021-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2021 | <6m, 1-4, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2022 | <6m, 6-11m, 1-4, 20-39, 40-49, 50-59, 60+ |
| 2023 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2024 | <6m, 6-11m, 1-4, 5-9, 10-14, 20-39, 40-49, 50-59, 60+ |
| 2025 | 6-11m, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Defunciones |
| ---: | ---: |
| 2021 | 117 |
| 2022 | 29 |
| 2023 | 149 |
| 2024 | 63 |
| 2025 | 57 |

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
from 'datos/vigilancia/defunciones/muerte_dengue_sospecha/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_dengue_sospecha/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_dengue_sospecha/datos.parquet'
where gestion = 2025 group by all order by defunciones desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2021 | 302a | Sospecha de muerte por Dengue | 6.0.0 (2021) |
| 2022-2023 | 302a | Sospecha de muerte por Dengue | 6.0.1 (2022) |
| 2024-2025 | 302a | 6. Sospecha de muerte por Dengue | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302a, grupo 09, 2021-2025: el encabezado repite "f. 15 - 19 años - F" (pandas lo marca con ".1") y desplaza una posición a todas las columnas siguientes. La columna repetida es "g. 20 - 39 años - D" y cada etiqueta siguiente corresponde a la posición que le sigue. La última etiqueta ("j. 60 años y más - F") no tiene columna propia: en los 15 archivos del grupo 09 de 2021-2025 repite, fila por fila, la primera columna ("a. Menor de 6 meses - D").
