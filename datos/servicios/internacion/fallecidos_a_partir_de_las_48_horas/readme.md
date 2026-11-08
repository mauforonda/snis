# Fallecidos a partir de las 48 horas

Registros de internación en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | mensual |
| Municipios con registros | 211 |
| Desagregación | sexo |
| Filas | 16.231 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 4.049 |
| 2002 | 5.035 |
| 2003 | 6.870 |
| 2004 | 9.977 |
| 2005 | 5.632 |
| 2006 | 6.430 |
| 2007 | 6.430 |
| 2008 | 6.627 |
| 2009 | 7.360 |
| 2010 | 6.513 |
| 2011 | 6.692 |
| 2012 | 6.487 |
| 2013 | 7.297 |
| 2014 | 7.300 |
| 2015 | 8.455 |
| 2016 | 7.810 |
| 2017 | 8.115 |
| 2018 | 8.803 |
| 2019 | 9.235 |
| 2020 | 10.865 |
| 2021 | 14.449 |
| 2022 | 10.270 |
| 2023 | 9.986 |
| 2024 | 10.059 |
| 2025 | 10.646 |

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
from 'datos/servicios/internacion/fallecidos_a_partir_de_las_48_horas/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/internacion/fallecidos_a_partir_de_las_48_horas/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/internacion/fallecidos_a_partir_de_las_48_horas/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2007 | 301 | Fallecidos a partir de las 48 horas |  |
| 2008-2013 | 301 | Fallecidos a partir de las 48 horas | 1.0.4 (2013) |
| 2014 | 301 | 13. 5 Fallecidos a partir de las 48 horas | 2.0.0 (2014) |
| 2015 | 301a | Fallecidos a partir de las 48 hrs. | 3.0.1 (2016) |
| 2016 | 301a | Fallecidos a partir de las 48 hrs. | 3.0.2 (2016) |
| 2017 | 301a | Fallecidos a partir de las 48 hrs. | 4.0.0 (2018) |
| 2018 | 301a | Fallecidos a partir de las 48 hrs. | 4.0.1 (2018) |
| 2019-2020 | 301a | Fallecidos a partir de las 48 hrs. | 5.0.1 (2020) |
| 2021 | 301a | Fallecidos a partir de las 48 hrs. | 6.0.0 (2021) |
| 2022-2023 | 301a | Fallecidos a partir de las 48 hrs. | 6.0.1 (2022) |
| 2024-2025 | 301a | Fallecidos a partir de las 48 hrs. | 7.0.1 (2026) |
