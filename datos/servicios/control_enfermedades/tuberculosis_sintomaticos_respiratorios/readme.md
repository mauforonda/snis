# Tuberculosis: sintomáticos respiratorios

Registros en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2008-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2008-2025 |
| Periodicidad | mensual |
| Municipios con registros | 344 |
| Desagregación | sexo |
| Filas | 96.724 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2008 | 80.566 |
| 2009 | 81.896 |
| 2010 | 78.138 |
| 2011 | 80.255 |
| 2012 | 85.158 |
| 2013 | 85.384 |
| 2014 | 85.644 |
| 2015 | 82.851 |
| 2016 | 84.985 |
| 2017 | 83.553 |
| 2018 | 92.801 |
| 2019 | 86.093 |
| 2020 | 43.883 |
| 2021 | 51.580 |
| 2022 | 67.912 |
| 2023 | 82.833 |
| 2024 | 85.973 |
| 2025 | 93.185 |

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
from 'datos/servicios/control_enfermedades/tuberculosis_sintomaticos_respiratorios/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tuberculosis_sintomaticos_respiratorios/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tuberculosis_sintomaticos_respiratorios/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2008-2011 | 301 | N° de Sintomáticos Respiratorios | 1.0.4 (2013) |
| 2012 | 301 | l 23.1 N° de Sintomáticos Respiratorios | 1.0.4 (2013) |
| 2013 | 301 | N° de Sintomáticos Respiratorios | 1.0.4 (2013) |
| 2014 | 301 | 23.1 N° de Sintomáticos Respiratorios | 2.0.0 (2014) |
| 2015 | 301a | Total N° de Sintomáticos Respiratorios | 3.0.1 (2016) |
| 2016 | 301a | N° de Sintomáticos Respiratorios | 3.0.2 (2016) |
| 2017 | 301a | N° de Sintomáticos Respiratorios | 4.0.0 (2018) |
| 2018 | 301a | N° de Sintomáticos Respiratorios | 4.0.1 (2018) |
| 2019-2020 | 301a | N° de Sintomáticos Respiratorios | 5.0.1 (2020) |
| 2021 | 301a | N° de Sintomáticos Respiratorios | 6.0.0 (2021) |
| 2022-2023 | 301a | N° de Sintomáticos Respiratorios | 6.0.1 (2022) |
| 2024-2025 | 301a | N° de Sintomáticos Respiratorios | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
