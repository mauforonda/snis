# Comunidades que participaron en el CAI de establecimiento

Actividades registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2010-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2010-2025 |
| Periodicidad | mensual |
| Municipios con registros | 343 |
| Desagregación |  |
| Filas | 24.646 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2010 | 13.478 |
| 2011 | 13.151 |
| 2012 | 8.751 |
| 2013 | 13.130 |
| 2014 | 14.109 |
| 2015 | 13.401 |
| 2016 | 15.050 |
| 2017 | 14.800 |
| 2018 | 15.395 |
| 2019 | 16.113 |
| 2020 | 9.347 |
| 2021 | 13.458 |
| 2022 | 17.727 |
| 2023 | 18.719 |
| 2024 | 18.769 |
| 2025 | 17.156 |

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
from 'datos/servicios/gestion_comunidad/comunidades_que_participaron_en_el_cai_de_establecimiento/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/gestion_comunidad/comunidades_que_participaron_en_el_cai_de_establecimiento/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2010-2013 | 301 | Nº de comunidades que participaron en el CAI de establecimiento | 1.0.4 (2013) |
| 2014 | 301 | 10.3. Nº de comunidades que participaron en el CAI de establecimiento | 2.0.0 (2014) |
| 2015 | 301a | Nº de comunidades que participaron en el CAI de establecimiento | 3.0.1 (2016) |
| 2016 | 301a | Nº de comunidades que participaron en el CAI de establecimiento | 3.0.2 (2016) |
| 2017 | 301a | Nº de comunidades que participaron en el CAI de establecimiento | 4.0.0 (2018) |
| 2018 | 301a | Nº de comunidades que participaron en el CAI de establecimiento | 4.0.1 (2018) |
| 2019-2020 | 301a | Nº de comunidades que participaron en el CAI de establecimiento | 5.0.1 (2020) |
| 2021 | 301a | Nº de comunidades que participaron en el CAI de establecimiento | 6.0.0 (2021) |
| 2022-2023 | 301a | Nº de comunidades que participaron en el CAI de establecimiento | 6.0.1 (2022) |
| 2024-2025 | 301a | Nº de comunidades que participaron en el CAI de establecimiento | 7.0.1 (2026) |
