# Muerte neonatal tardía confirmada (7 a 27 días)

Muertes por esta causa en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2015-2025. Fuente: SNIS, formularios 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2025 |
| Periodicidad | semanal |
| Municipios con registros | 222 |
| Desagregación | sexo, lugar |
| Filas | 3.383 |

Valores de `lugar` (lugar):

- dentro (2015-2025)
- fuera (2015-2025)

Total por gestión:

| Gestión | Defunciones |
| ---: | ---: |
| 2015 | 320 |
| 2016 | 297 |
| 2017 | 329 |
| 2018 | 371 |
| 2019 | 330 |
| 2020 | 434 |
| 2021 | 339 |
| 2022 | 407 |
| 2023 | 434 |
| 2024 | 340 |
| 2025 | 294 |

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
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `defunciones` | integer | Número de defunciones en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_neonatal_tardia/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_neonatal_tardia/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_neonatal_tardia/datos.parquet'
where gestion = 2025 group by all order by defunciones desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015 | 302a | Muerte neonatal tardia (7-27 días) confirmada | 3.0.1 (2016) |
| 2016 | 302a | Muerte neonatal tardia (7-27 días) confirmada | 3.0.2 (2016) |
| 2017 | 302a | Muerte neonatal tardia (7-27 días) confirmada | 4.0.0 (2018) |
| 2018 | 302a | Muerte neonatal tardia (7-27 días) confirmada | 4.0.1 (2018) |
| 2019-2020 | 302a | Muerte neonatal tardia (7-27 días) confirmada | 5.0.1 (2020) |
| 2021 | 302a | Muerte neonatal tardia (7-27 días) confirmada | 6.0.0 (2021) |
| 2022-2023 | 302a | Muerte neonatal tardia (7-27 días) confirmada | 6.0.1 (2022) |
| 2024-2025 | 302a | 3. Muerte neonatal tardia (7-27 días) confirmada | 7.0.1 (2026) |
