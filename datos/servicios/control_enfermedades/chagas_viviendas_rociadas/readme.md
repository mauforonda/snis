# Chagas: viviendas rociadas

Registros en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2006, 2010-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2006, 2010-2025 |
| Periodicidad | mensual |
| Municipios con registros | 199 |
| Desagregación |  |
| Filas | 12.231 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 81.542 |
| 2002 | 15.526 |
| 2003 | 247.101 |
| 2004 | 94.983 |
| 2005 | 180.991 |
| 2006 | 47.617 |
| 2010 | 22.433 |
| 2011 | 36.609 |
| 2012 | 36.287 |
| 2013 | 28.281 |
| 2014 | 34.655 |
| 2015 | 19.939 |
| 2016 | 27.473 |
| 2017 | 22.711 |
| 2018 | 19.910 |
| 2019 | 11.017 |
| 2020 | 7.042 |
| 2021 | 16.279 |
| 2022 | 16.212 |
| 2023 | 12.576 |
| 2024 | 13.800 |
| 2025 | 8.267 |

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
from 'datos/servicios/control_enfermedades/chagas_viviendas_rociadas/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/chagas_viviendas_rociadas/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2006 | 301 | Viviendas rociadas |  |
| 2010-2011 | 301 | Viviendas Roceadas |  |
| 2012 | 301 | l 25.8 Viviendas Roceadas |  |
| 2013 | 301 | Viviendas Roceadas |  |
| 2014 | 301 | 25.8 Viviendas Roceadas | 2.0.0 (2014) |
| 2015 | 301a | Total Viviendas Roceadas | 3.0.1 (2016) |
| 2016-2023 | 301a | Viviendas Roceadas |  |
| 2024-2025 | 301a | 8. Viviendas Rociadas |  |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
