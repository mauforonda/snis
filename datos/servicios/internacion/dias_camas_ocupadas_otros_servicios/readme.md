# Días camas ocupadas otros servicios

Registros de internación en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | mensual |
| Municipios con registros | 335 |
| Desagregación | sexo |
| Filas | 57.489 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 1.293.557 |
| 2002 | 1.632.460 |
| 2003 | 1.842.519 |
| 2004 | 1.938.072 |
| 2005 | 1.956.773 |
| 2006 | 2.047.679 |
| 2007 | 2.159.934 |
| 2008 | 2.230.433 |
| 2009 | 2.350.468 |
| 2010 | 2.228.290 |
| 2011 | 2.401.183 |
| 2012 | 2.479.420 |
| 2013 | 2.561.394 |
| 2014 | 2.490.761 |
| 2015 | 2.598.349 |
| 2016 | 2.687.284 |
| 2017 | 2.743.346 |
| 2018 | 2.821.298 |
| 2019 | 2.944.892 |
| 2020 | 2.190.918 |
| 2021 | 2.554.716 |
| 2022 | 2.807.398 |
| 2023 | 3.272.695 |
| 2024 | 3.195.777 |
| 2025 | 3.114.547 |

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
from 'datos/servicios/internacion/dias_camas_ocupadas_otros_servicios/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/internacion/dias_camas_ocupadas_otros_servicios/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/internacion/dias_camas_ocupadas_otros_servicios/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2009 | 301 | Días camas ocupadas otros servicios |  |
| 2010-2011 | 301 | Días camas ocupadas otros servicios | 1.0.4 (2013) |
| 2012 | 301 | l 13.8 Días camas ocupadas otros servicios | 1.0.4 (2013) |
| 2013 | 301 | Días camas ocupadas otros servicios | 1.0.4 (2013) |
| 2014 | 301 | 13.8 Días camas ocupadas otros servicios | 2.0.0 (2014) |
| 2015 | 301a | Total Días camas ocupadas otros servicios | 3.0.1 (2016) |
| 2016 | 301a | Días camas ocupadas otros servicios | 3.0.2 (2016) |
| 2017 | 301a | Días camas ocupadas otros servicios | 4.0.0 (2018) |
| 2018 | 301a | Días camas ocupadas otros servicios | 4.0.1 (2018) |
| 2019-2020 | 301a | Días camas ocupadas otros servicios | 5.0.1 (2020) |
| 2021 | 301a | Días camas ocupadas otros servicios | 6.0.0 (2021) |
| 2022-2023 | 301a | Días camas ocupadas otros servicios | 6.0.1 (2022) |
| 2024-2025 | 301a | 8. Días camas ocupadas otros servicios | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
