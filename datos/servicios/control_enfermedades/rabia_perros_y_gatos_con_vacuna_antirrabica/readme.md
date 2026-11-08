# Rabia: perros y gatos con vacuna antirrábica

Registros en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2025. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2025 |
| Periodicidad | mensual |
| Municipios con registros | 343 |
| Desagregación |  |
| Filas | 14.814 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2015 | 2.757.871 |
| 2016 | 3.340.692 |
| 2017 | 3.830.488 |
| 2018 | 25.898.644 |
| 2019 | 3.340.613 |
| 2020 | 2.583.794 |
| 2021 | 3.292.104 |
| 2022 | 37.114.069 |
| 2023 | 3.369.444 |
| 2024 | 3.482.443 |
| 2025 | 3.104.919 |

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
from 'datos/servicios/control_enfermedades/rabia_perros_y_gatos_con_vacuna_antirrabica/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/rabia_perros_y_gatos_con_vacuna_antirrabica/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015 | 301a | Total N° de perros y gatos con vacuna antirrábica | 3.0.1 (2016) |
| 2016 | 301a | N° de perros y gatos con vacuna antirrábica | 3.0.2 (2016) |
| 2017 | 301a | N° de perros y gatos con vacuna antirrábica | 4.0.0 (2018) |
| 2018 | 301a | N° de perros y gatos con vacuna antirrábica | 4.0.1 (2018) |
| 2019-2020 | 301a | N° de perros y gatos con vacuna antirrábica | 5.0.1 (2020) |
| 2021 | 301a | N° de perros y gatos con vacuna antirrábica | 6.0.0 (2021) |
| 2022-2023 | 301a | N° de perros y gatos con vacuna antirrábica | 6.0.1 (2022) |
| 2024-2025 | 301a | 5. N° de perros y gatos con vacuna antirrábica | 7.0.1 (2026) |
