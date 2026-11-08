# Contrareferidos

Registros de internación en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2007-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2007-2025 |
| Periodicidad | mensual |
| Municipios con registros | 285 |
| Desagregación | sexo |
| Filas | 15.559 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2007 | 16.097 |
| 2008 | 12.406 |
| 2009 | 22.511 |
| 2010 | 9.296 |
| 2011 | 8.036 |
| 2012 | 6.425 |
| 2013 | 10.284 |
| 2014 | 20.184 |
| 2015 | 41.809 |
| 2016 | 49.339 |
| 2017 | 56.242 |
| 2018 | 49.637 |
| 2019 | 77.416 |
| 2020 | 74.455 |
| 2021 | 109.089 |
| 2022 | 136.359 |
| 2023 | 159.010 |
| 2024 | 171.855 |
| 2025 | 159.400 |

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
from 'datos/servicios/internacion/contrareferidos/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/internacion/contrareferidos/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/internacion/contrareferidos/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2007-2009 | 301 | 0 Contrareferidos |  |
| 2010-2013 | 301 | Retornados | 1.0.4 (2013) |
| 2014 | 301 | 13. 6 Retornados | 2.0.0 (2014) |
| 2015 | 301a | Contrareferidos | 3.0.1 (2016) |
| 2016 | 301a | Contrareferidos | 3.0.2 (2016) |
| 2017 | 301a | Contrareferidos | 4.0.0 (2018) |
| 2018 | 301a | Contrareferidos | 4.0.1 (2018) |
| 2019-2020 | 301a | Contrareferidos | 5.0.1 (2020) |
| 2021 | 301a | Contrareferidos | 6.0.0 (2021) |
| 2022-2023 | 301a | Contrareferidos | 6.0.1 (2022) |
| 2024-2025 | 301a | Contrareferidos | 7.0.1 (2026) |
