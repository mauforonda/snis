# Actividades realizadas con participación de la comunidad

Actividades registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2004-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2004-2025 |
| Periodicidad | mensual |
| Municipios con registros | 344 |
| Desagregación |  |
| Filas | 75.754 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2004 | 144.900 |
| 2005 | 136.856 |
| 2006 | 145.577 |
| 2007 | 131.621 |
| 2008 | 137.575 |
| 2009 | 159.685 |
| 2010 | 112.547 |
| 2011 | 99.660 |
| 2012 | 99.768 |
| 2013 | 77.789 |
| 2014 | 75.245 |
| 2015 | 74.948 |
| 2016 | 80.774 |
| 2017 | 92.735 |
| 2018 | 108.858 |
| 2019 | 100.345 |
| 2020 | 108.526 |
| 2021 | 133.392 |
| 2022 | 152.472 |
| 2023 | 189.082 |
| 2024 | 190.905 |
| 2025 | 193.089 |

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
from 'datos/servicios/gestion_comunidad/actividades_realizadas_con_participacion_de_la_comunidad/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/gestion_comunidad/actividades_realizadas_con_participacion_de_la_comunidad/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2004 | 301 | Nº de actividades realizadas con participación de |  |
| 2005-2007 | 301 | Nº de actividades realizadas con participación |  |
| 2008-2009 | 301 | Nº de actividades realizadas con participación | 1.0.4 (2013) |
| 2010-2013 | 301 | Nº de actividades realizadas con participación de la comunidad | 1.0.4 (2013) |
| 2014 | 301 | 10.1. Nº de actividades realizadas con participación de la comunidad | 2.0.0 (2014) |
| 2015 | 301a | Nº de actividades realizadas con participación de la comunidad | 3.0.1 (2016) |
| 2016 | 301a | Nº de actividades realizadas con participación de la comunidad | 3.0.2 (2016) |
| 2017 | 301a | Nº de actividades realizadas con participación de la comunidad | 4.0.0 (2018) |
| 2018 | 301a | Nº de actividades realizadas con participación de la comunidad | 4.0.1 (2018) |
| 2019-2020 | 301a | Nº de actividades realizadas con participación de la comunidad | 5.0.1 (2020) |
| 2021 | 301a | Nº de actividades realizadas con participación de la comunidad | 6.0.0 (2021) |
| 2022-2023 | 301a | Nº de actividades realizadas con participación de la comunidad | 6.0.1 (2022) |
| 2024-2025 | 301a | Nº de actividades realizadas con participación de la comunidad | 7.0.1 (2026) |
