# Días camas ocupadas maternidad

Registros de internación en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | mensual |
| Municipios con registros | 341 |
| Desagregación | sexo |
| Filas | 75.947 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 312.454 |
| 2002 | 382.029 |
| 2003 | 392.146 |
| 2004 | 414.216 |
| 2005 | 430.198 |
| 2006 | 439.660 |
| 2007 | 444.981 |
| 2008 | 470.995 |
| 2009 | 500.486 |
| 2010 | 534.698 |
| 2011 | 563.365 |
| 2012 | 582.136 |
| 2013 | 586.211 |
| 2014 | 609.111 |
| 2015 | 642.314 |
| 2016 | 634.312 |
| 2017 | 613.237 |
| 2018 | 610.710 |
| 2019 | 665.901 |
| 2020 | 494.221 |
| 2021 | 499.052 |
| 2022 | 535.892 |
| 2023 | 534.639 |
| 2024 | 517.430 |
| 2025 | 525.942 |

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
from 'datos/servicios/internacion/dias_camas_ocupadas_maternidad/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/internacion/dias_camas_ocupadas_maternidad/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/internacion/dias_camas_ocupadas_maternidad/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2009 | 301 | Días camas ocupadas maternidad |  |
| 2010-2011 | 301 | Días camas ocupadas maternidad | 1.0.4 (2013) |
| 2012 | 301 | l 13.7 Días camas ocupadas maternidad | 1.0.4 (2013) |
| 2013 | 301 | Días camas ocupadas maternidad | 1.0.4 (2013) |
| 2014 | 301 | 13.7 Días camas ocupadas maternidad | 2.0.0 (2014) |
| 2015 | 301a | Total Días camas ocupadas maternidad | 3.0.1 (2016) |
| 2016 | 301a | Días camas ocupadas maternidad | 3.0.2 (2016) |
| 2017 | 301a | Días camas ocupadas maternidad | 4.0.0 (2018) |
| 2018 | 301a | Días camas ocupadas maternidad | 4.0.1 (2018) |
| 2019-2020 | 301a | Días camas ocupadas maternidad | 5.0.1 (2020) |
| 2021 | 301a | Días camas ocupadas maternidad | 6.0.0 (2021) |
| 2022-2023 | 301a | Días camas ocupadas maternidad | 6.0.1 (2022) |
| 2024-2025 | 301a | 7. Días camas ocupadas maternidad | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
