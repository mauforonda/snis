# Días camas disponibles maternidad

Registros de internación en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | mensual |
| Municipios con registros | 341 |
| Desagregación | sexo |
| Filas | 80.206 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 875.697 |
| 2002 | 1.009.233 |
| 2003 | 1.030.672 |
| 2004 | 1.109.757 |
| 2005 | 1.236.266 |
| 2006 | 1.345.744 |
| 2007 | 1.285.893 |
| 2008 | 1.321.663 |
| 2009 | 1.366.225 |
| 2010 | 1.403.409 |
| 2011 | 1.447.512 |
| 2012 | 1.462.372 |
| 2013 | 1.543.076 |
| 2014 | 1.523.101 |
| 2015 | 1.459.572 |
| 2016 | 1.537.595 |
| 2017 | 1.528.956 |
| 2018 | 1.548.332 |
| 2019 | 1.728.468 |
| 2020 | 1.622.361 |
| 2021 | 1.646.597 |
| 2022 | 1.700.436 |
| 2023 | 1.776.112 |
| 2024 | 1.859.048 |
| 2025 | 1.830.732 |

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
from 'datos/servicios/internacion/dias_camas_disponibles_maternidad/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/internacion/dias_camas_disponibles_maternidad/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/internacion/dias_camas_disponibles_maternidad/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2009 | 301 | Días camas disponibles maternidad |  |
| 2010-2011 | 301 | Días camas disponibles maternidad | 1.0.4 (2013) |
| 2012 | 301 | l 13.9 Días camas disponibles maternidad | 1.0.4 (2013) |
| 2013 | 301 | Días camas disponibles maternidad | 1.0.4 (2013) |
| 2014 | 301 | 13.9 Días camas disponibles maternidad | 2.0.0 (2014) |
| 2015 | 301a | Total Días camas disponibles maternidad | 3.0.1 (2016) |
| 2016 | 301a | Días camas disponibles maternidad | 3.0.2 (2016) |
| 2017 | 301a | Días camas disponibles maternidad | 4.0.0 (2018) |
| 2018 | 301a | Días camas disponibles maternidad | 4.0.1 (2018) |
| 2019-2020 | 301a | Días camas disponibles maternidad | 5.0.1 (2020) |
| 2021 | 301a | Días camas disponibles maternidad | 6.0.0 (2021) |
| 2022-2023 | 301a | Días camas disponibles maternidad | 6.0.1 (2022) |
| 2024-2025 | 301a | 9. Días camas disponibles maternidad | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
