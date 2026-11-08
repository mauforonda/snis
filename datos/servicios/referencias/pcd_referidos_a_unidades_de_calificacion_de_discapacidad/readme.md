# PCD referidos a unidades de calificación de discapacidad

Pacientes o referencias registrados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2010-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2010-2025 |
| Periodicidad | mensual |
| Municipios con registros | 272 |
| Desagregación |  |
| Filas | 3.487 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2010 | 2.554 |
| 2011 | 863 |
| 2012 | 808 |
| 2013 | 1.273 |
| 2014 | 32.790 |
| 2015 | 2.338 |
| 2016 | 5.497 |
| 2017 | 6.313 |
| 2018 | 6.158 |
| 2019 | 2.526 |
| 2020 | 1.572 |
| 2021 | 1.920 |
| 2022 | 1.290 |
| 2023 | 2.801 |
| 2024 | 2.945 |
| 2025 | 3.308 |

## Cómo utilizar

Cada fila da el número de cantidad de un periodo, un municipio y una población. Para obtener un total, sume las filas: el dataset no tiene filas de total. Una combinación sin fila significa que no hubo registros. Las convenciones de tiempo, territorio y población están en el [catálogo](../../../README.md#cómo-leer-los-datos).

| Columna | Tipo | Descripción |
| --- | --- | --- |
| `gestion` | integer | Año calendario (gestión) del registro. |
| `mes` | integer | Mes, de 1 a 12. |
| `fecha_inicio` | date | Primer día de la semana o del mes. |
| `departamento` | string | Nombre del departamento. |
| `municipio` | string | Nombre del municipio. |
| `municipio_codigo` | string | Código del municipio, 6 dígitos: departamento (2), provincia (2) y municipio (2). |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/referencias/pcd_referidos_a_unidades_de_calificacion_de_discapacidad/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/referencias/pcd_referidos_a_unidades_de_calificacion_de_discapacidad/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2010-2013 | 301 | PCD referidas a Unidades de Calificación de Discapacidad. | 1.0.4 (2013) |
| 2014 | 301 | 2.4 PCD referidas a Unidades de Calificación de Discapacidad. | 2.0.0 (2014) |
| 2015 | 301a | PCD referidas a Unidades de Calificación de Discapacidad. | 3.0.1 (2016) |
| 2016 | 301a | PCD referidas a Unidades de Calificación de Discapacidad. | 3.0.2 (2016) |
| 2017 | 301a | PCD referidas a Unidades de Calificación de Discapacidad. | 4.0.0 (2018) |
| 2018 | 301a | PCD referidas a Unidades de Calificación de Discapacidad. | 4.0.1 (2018) |
| 2019-2020 | 301a | PCD referidas a Unidades de Calificación de Discapacidad. | 5.0.1 (2020) |
| 2021 | 301a | PCD referidas a Unidades de Calificación de Discapacidad. | 6.0.0 (2021) |
| 2022-2023 | 301a | PCD referidas a Unidades de Calificación de Discapacidad. | 6.0.1 (2022) |
| 2024-2025 | 301a | PCD referidos a Unidades de Calificación de Discapacidad | 7.0.1 (2026) |
