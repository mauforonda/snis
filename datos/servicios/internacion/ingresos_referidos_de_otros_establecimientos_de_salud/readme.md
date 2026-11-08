# Ingresos referidos de otros establecimientos de salud

Registros de internación en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | mensual |
| Municipios con registros | 315 |
| Desagregación | sexo |
| Filas | 41.278 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 35.815 |
| 2002 | 26.783 |
| 2003 | 26.300 |
| 2004 | 29.257 |
| 2005 | 38.473 |
| 2006 | 41.071 |
| 2007 | 41.562 |
| 2008 | 39.594 |
| 2009 | 57.426 |
| 2010 | 73.359 |
| 2011 | 92.754 |
| 2012 | 53.462 |
| 2013 | 48.196 |
| 2014 | 66.104 |
| 2015 | 68.678 |
| 2016 | 82.370 |
| 2017 | 81.217 |
| 2018 | 83.251 |
| 2019 | 124.496 |
| 2020 | 75.554 |
| 2021 | 102.561 |
| 2022 | 99.713 |
| 2023 | 112.586 |
| 2024 | 109.253 |
| 2025 | 107.925 |

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
from 'datos/servicios/internacion/ingresos_referidos_de_otros_establecimientos_de_salud/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/internacion/ingresos_referidos_de_otros_establecimientos_de_salud/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/internacion/ingresos_referidos_de_otros_establecimientos_de_salud/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2003 | 301 | Ingresos referidos de otros establecimientos |  |
| 2004 | 301 | Ingresos referidos de otros establecimientos de s |  |
| 2005-2007 | 301 | Ingresos referidos de otros establecimientos |  |
| 2008 | 301 | Ingresos referidos de otros establecim | 1.0.4 (2013) |
| 2009 | 301 | Ingresos referidos de otros establecimientos | 1.0.4 (2013) |
| 2010-2013 | 301 | Ingresos referidos de otros establecimientos de salud | 1.0.4 (2013) |
| 2014 | 301 | 13. 1 Ingresos referidos de otros establecimientos de salud | 2.0.0 (2014) |
| 2015 | 301a | Ingresos referidos de otros establecimientos de salud | 3.0.1 (2016) |
| 2016 | 301a | Ingresos referidos de otros establecimientos de salud | 3.0.2 (2016) |
| 2017 | 301a | Ingresos referidos de otros establecimientos de salud | 4.0.0 (2018) |
| 2018 | 301a | Ingresos referidos de otros establecimientos de salud | 4.0.1 (2018) |
| 2019-2020 | 301a | Ingresos referidos de otros establecimientos de salud | 5.0.1 (2020) |
| 2021 | 301a | Ingresos referidos de otros establecimientos de salud | 6.0.0 (2021) |
| 2022-2023 | 301a | Ingresos referidos de otros establecimientos de salud | 6.0.1 (2022) |
| 2024-2025 | 301a | Ingresos referidos de otros establecimientos de salud | 7.0.1 (2026) |
