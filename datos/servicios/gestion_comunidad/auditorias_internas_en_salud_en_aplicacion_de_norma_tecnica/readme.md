# Auditorias internas en salud en aplicación de norma técnica

Actividades registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2010-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2010-2025 |
| Periodicidad | mensual |
| Municipios con registros | 322 |
| Desagregación |  |
| Filas | 13.101 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2010 | 1.234 |
| 2011 | 1.185 |
| 2012 | 1.057 |
| 2013 | 958 |
| 2014 | 1.358 |
| 2015 | 2.535 |
| 2016 | 3.366 |
| 2017 | 4.346 |
| 2018 | 5.540 |
| 2019 | 6.734 |
| 2020 | 6.531 |
| 2021 | 8.020 |
| 2022 | 11.656 |
| 2023 | 13.086 |
| 2024 | 14.346 |
| 2025 | 13.330 |

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
from 'datos/servicios/gestion_comunidad/auditorias_internas_en_salud_en_aplicacion_de_norma_tecnica/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/gestion_comunidad/auditorias_internas_en_salud_en_aplicacion_de_norma_tecnica/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2010-2013 | 301 | N° de auditorias internas en salud en aplicación de norma técnica | 1.0.4 (2013) |
| 2014 | 301 | 10.7. N° de auditorias internas en salud en aplicación de norma técnica | 2.0.0 (2014) |
| 2015 | 301a | N° de auditorias internas en salud en aplicación de norma técnica | 3.0.1 (2016) |
| 2016 | 301a | N° de auditorias internas en salud en aplicación de norma técnica | 3.0.2 (2016) |
| 2017 | 301a | N° de auditorias internas en salud en aplicación de norma técnica | 4.0.0 (2018) |
| 2018 | 301a | N° de auditorias internas en salud en aplicación de norma técnica | 4.0.1 (2018) |
| 2019-2020 | 301a | N° de auditorias internas en salud en aplicación de norma técnica | 5.0.1 (2020) |
| 2021 | 301a | N° de auditorias internas en salud en aplicación de norma técnica | 6.0.0 (2021) |
| 2022-2023 | 301a | N° de auditorias internas en salud en aplicación de norma técnica | 6.0.1 (2022) |
| 2024-2025 | 301a | N° de auditorias internas en salud en aplicación de norma técnica | 7.0.1 (2026) |
