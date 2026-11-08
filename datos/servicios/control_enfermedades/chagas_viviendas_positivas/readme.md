# Chagas: viviendas positivas

Registros en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2007-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2007-2025 |
| Periodicidad | mensual |
| Municipios con registros | 170 |
| Desagregación |  |
| Filas | 10.289 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2007 | 5.079 |
| 2008 | 8.203 |
| 2009 | 7.067 |
| 2010 | 9.868 |
| 2011 | 7.464 |
| 2012 | 5.770 |
| 2013 | 7.397 |
| 2014 | 7.561 |
| 2015 | 4.894 |
| 2016 | 8.481 |
| 2017 | 5.524 |
| 2018 | 4.284 |
| 2019 | 3.345 |
| 2020 | 1.538 |
| 2021 | 5.198 |
| 2022 | 4.665 |
| 2023 | 4.629 |
| 2024 | 3.601 |
| 2025 | 3.068 |

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
from 'datos/servicios/control_enfermedades/chagas_viviendas_positivas/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/chagas_viviendas_positivas/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2007-2009 | 301 | Viviendas positivas |  |
| 2010-2011 | 301 | Viviendas Positivas |  |
| 2012 | 301 | l 25.7 Viviendas Positivas |  |
| 2013 | 301 | Viviendas Positivas |  |
| 2014 | 301 | 25.7 Viviendas Positivas | 2.0.0 (2014) |
| 2015 | 301a | Total Viviendas Positivas | 3.0.1 (2016) |
| 2016-2023 | 301a | Viviendas Positivas |  |
| 2024-2025 | 301a | 7. Viviendas Positivas |  |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
