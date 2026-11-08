# Ingresos espontáneos

Registros de internación en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | mensual |
| Municipios con registros | 343 |
| Desagregación | sexo |
| Filas | 108.834 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 311.799 |
| 2002 | 408.856 |
| 2003 | 437.410 |
| 2004 | 475.836 |
| 2005 | 502.020 |
| 2006 | 533.776 |
| 2007 | 542.688 |
| 2008 | 583.366 |
| 2009 | 622.873 |
| 2010 | 626.292 |
| 2011 | 678.308 |
| 2012 | 672.855 |
| 2013 | 687.697 |
| 2014 | 706.849 |
| 2015 | 678.532 |
| 2016 | 669.840 |
| 2017 | 655.079 |
| 2018 | 653.176 |
| 2019 | 625.897 |
| 2020 | 483.868 |
| 2021 | 529.995 |
| 2022 | 579.298 |
| 2023 | 671.364 |
| 2024 | 678.348 |
| 2025 | 703.373 |

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
from 'datos/servicios/internacion/ingresos_espontaneos/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/internacion/ingresos_espontaneos/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/internacion/ingresos_espontaneos/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2007 | 301 | Ingresos espontáneos |  |
| 2008-2013 | 301 | Ingresos espontáneos | 1.0.4 (2013) |
| 2014 | 301 | 13. 2 Ingresos espontáneos | 2.0.0 (2014) |
| 2015 | 301a | Ingresos espontáneos | 3.0.1 (2016) |
| 2016 | 301a | Ingresos espontáneos | 3.0.2 (2016) |
| 2017 | 301a | Ingresos espontáneos | 4.0.0 (2018) |
| 2018 | 301a | Ingresos espontáneos | 4.0.1 (2018) |
| 2019-2020 | 301a | Ingresos espontáneos | 5.0.1 (2020) |
| 2021 | 301a | Ingresos espontáneos | 6.0.0 (2021) |
| 2022-2023 | 301a | Ingresos espontáneos | 6.0.1 (2022) |
| 2024-2025 | 301a | Ingresos espontáneos | 7.0.1 (2026) |
