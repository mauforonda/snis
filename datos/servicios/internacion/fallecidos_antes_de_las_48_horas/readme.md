# Fallecidos antes de las 48 horas

Registros de internación en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | mensual |
| Municipios con registros | 278 |
| Desagregación | sexo |
| Filas | 20.161 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 3.281 |
| 2002 | 3.944 |
| 2003 | 3.761 |
| 2004 | 3.743 |
| 2005 | 3.994 |
| 2006 | 5.773 |
| 2007 | 4.871 |
| 2008 | 4.846 |
| 2009 | 4.820 |
| 2010 | 4.827 |
| 2011 | 5.241 |
| 2012 | 5.178 |
| 2013 | 5.582 |
| 2014 | 5.330 |
| 2015 | 7.382 |
| 2016 | 5.283 |
| 2017 | 5.265 |
| 2018 | 4.825 |
| 2019 | 5.976 |
| 2020 | 6.733 |
| 2021 | 7.259 |
| 2022 | 5.910 |
| 2023 | 5.255 |
| 2024 | 5.693 |
| 2025 | 5.947 |

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
from 'datos/servicios/internacion/fallecidos_antes_de_las_48_horas/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/internacion/fallecidos_antes_de_las_48_horas/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/internacion/fallecidos_antes_de_las_48_horas/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2007 | 301 | Fallecidos antes de las 48 horas |  |
| 2008-2013 | 301 | Fallecidos antes de las 48 horas | 1.0.4 (2013) |
| 2014 | 301 | 13. 4 Fallecidos antes de las 48 horas | 2.0.0 (2014) |
| 2015 | 301a | Fallecidos antes de las 48 hrs. | 3.0.1 (2016) |
| 2016 | 301a | Fallecidos antes de las 48 hrs. | 3.0.2 (2016) |
| 2017 | 301a | Fallecidos antes de las 48 hrs. | 4.0.0 (2018) |
| 2018 | 301a | Fallecidos antes de las 48 hrs. | 4.0.1 (2018) |
| 2019-2020 | 301a | Fallecidos antes de las 48 hrs. | 5.0.1 (2020) |
| 2021 | 301a | Fallecidos antes de las 48 hrs. | 6.0.0 (2021) |
| 2022-2023 | 301a | Fallecidos antes de las 48 hrs. | 6.0.1 (2022) |
| 2024-2025 | 301a | Fallecidos antes de las 48 hrs. | 7.0.1 (2026) |
