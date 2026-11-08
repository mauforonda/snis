# Auditorias del programa en aplicación de la norma técnica

Actividades registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2023. Fuente: SNIS, formularios 301b.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2023 |
| Periodicidad | mensual |
| Municipios con registros | 31 |
| Desagregación |  |
| Filas | 450 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2015 | 361 |
| 2016 | 196 |
| 2017 | 128 |
| 2018 | 115 |
| 2019 | 124 |
| 2020 | 37 |
| 2021 | 357 |
| 2022 | 519 |
| 2023 | 584 |

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
from 'datos/servicios/gestion_comunidad/auditorias_del_programa_en_aplicacion_de_la_norma_tecnica/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/gestion_comunidad/auditorias_del_programa_en_aplicacion_de_la_norma_tecnica/datos.parquet'
where gestion = 2023 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015-2023 | 301b | Nº de auditorias del Programa en aplicación de la norma técnica |  |
