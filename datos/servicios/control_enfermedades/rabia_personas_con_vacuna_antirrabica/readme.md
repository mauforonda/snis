# Rabia: personas con vacuna antirrábica

Registros en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2025. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2025 |
| Periodicidad | mensual |
| Municipios con registros | 318 |
| Desagregación | sexo |
| Filas | 20.689 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2015 | 32.171 |
| 2016 | 30.083 |
| 2017 | 32.346 |
| 2018 | 40.086 |
| 2019 | 37.322 |
| 2020 | 22.968 |
| 2021 | 24.115 |
| 2022 | 33.453 |
| 2023 | 34.336 |
| 2024 | 32.925 |
| 2025 | 38.102 |

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
| `sexo` | string | mujer u hombre. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/rabia_personas_con_vacuna_antirrabica/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/rabia_personas_con_vacuna_antirrabica/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/rabia_personas_con_vacuna_antirrabica/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015 | 301a | Total Nº de personas con vacuna Antirrábica | 3.0.1 (2016) |
| 2016 | 301a | Nº de personas con vacuna Antirrábica | 3.0.2 (2016) |
| 2017 | 301a | Nº de personas con vacuna Antirrábica | 4.0.0 (2018) |
| 2018 | 301a | Nº de personas con vacuna Antirrábica | 4.0.1 (2018) |
| 2019-2020 | 301a | Nº de personas con vacuna Antirrábica | 5.0.1 (2020) |
| 2021 | 301a | Nº de personas con vacuna Antirrábica | 6.0.0 (2021) |
| 2022-2023 | 301a | Nº de personas con vacuna Antirrábica | 6.0.1 (2022) |
| 2024-2025 | 301a | Nº de personas con vacuna Antirrábica | 7.0.1 (2026) |
