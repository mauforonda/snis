# Muerte por accidente cerebrovascular

Muertes por esta causa en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2018, 2020-2025. Fuente: SNIS, formularios 302b.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2018, 2020-2025 |
| Periodicidad | mensual |
| Municipios con registros | 221 |
| Desagregación | sexo, edad |
| Filas | 3.620 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015 | <6m, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2016 | <6m, 6-11m, 1-4, 5-9, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2017 | 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2018 | <6m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2020 | <6m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2021 | 6-11m, 1-4, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2022 | 1-4, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2023 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2024 | <6m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2025 | 6-11m, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Defunciones |
| ---: | ---: |
| 2015 | 501 |
| 2016 | 512 |
| 2017 | 473 |
| 2018 | 563 |
| 2020 | 472 |
| 2021 | 579 |
| 2022 | 578 |
| 2023 | 701 |
| 2024 | 436 |
| 2025 | 533 |

## Cómo utilizar

Cada fila da el número de defunciones de un periodo, un municipio y una población. Para obtener un total, sume las filas: el dataset no tiene filas de total. Una combinación sin fila significa que no hubo registros. Las convenciones de tiempo, territorio y población están en el [catálogo](../../../README.md#cómo-leer-los-datos).

| Columna | Tipo | Descripción |
| --- | --- | --- |
| `gestion` | integer | Año calendario (gestión) del registro. |
| `mes` | integer | Mes, de 1 a 12. |
| `fecha_inicio` | date | Primer día de la semana o del mes. |
| `departamento` | string | Nombre del departamento. |
| `municipio` | string | Nombre del municipio. |
| `municipio_codigo` | string | Código del municipio, 6 dígitos: departamento (2), provincia (2) y municipio (2). |
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `defunciones` | integer | Número de defunciones en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_acv/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_acv/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_acv/datos.parquet'
where gestion = 2025 group by all order by defunciones desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015 | 302b | Accidente Cerebrovascular | 3.0.1 (2016) |
| 2016 | 302b | Accidente Cerebrovascular | 3.0.2 (2016) |
| 2017 | 302b | Accidente Cerebrovascular | 4.0.0 (2018) |
| 2018 | 302b | Accidente Cerebrovascular | 4.0.1 (2018) |
| 2020 | 302b | Accidente Cerebrovascular | 5.0.1 (2020) |
| 2021 | 302b | Accidente Cerebrovascular | 6.0.0 (2021) |
| 2022-2023 | 302b | Accidente Cerebrovascular | 6.0.1 (2022) |
| 2024-2025 | 302b | Accidente Cerebrovascular | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302b, grupos 01, 05, 06, 07 y 10: el segundo nivel dice NUEVO/REPETIDO, pero las reglas de SOAPS dividen estas variables por sexo. Las muertes por cáncer de mama y de cuello uterino están en REPETIDO en todas las gestiones 2016-2025, y el tabaco y el alcohol (grupo 01, 2024-2025) están sobre todo en NUEVO: REPETIDO es mujer y NUEVO es hombre.
