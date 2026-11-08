# Beneficiarias (madres) del bono juana azurduy atendidas

Actividades registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2025. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2025 |
| Periodicidad | mensual |
| Municipios con registros | 343 |
| Desagregación |  |
| Filas | 33.314 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2015 | 147.537 |
| 2016 | 167.276 |
| 2017 | 165.120 |
| 2018 | 165.582 |
| 2019 | 159.653 |
| 2020 | 124.376 |
| 2021 | 144.838 |
| 2022 | 174.211 |
| 2023 | 212.839 |
| 2024 | 195.432 |
| 2025 | 175.464 |

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
from 'datos/servicios/gestion_comunidad/beneficiarias_madres_del_bono_juana_azurduy_atendidas/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/gestion_comunidad/beneficiarias_madres_del_bono_juana_azurduy_atendidas/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015 | 301a | N° de beneficiarias (madres) del bono Juana Azurduy atendidas | 3.0.1 (2016) |
| 2016 | 301a | N° de beneficiarias (madres) del bono Juana Azurduy atendidas | 3.0.2 (2016) |
| 2017 | 301a | N° de beneficiarias (madres) del bono Juana Azurduy atendidas | 4.0.0 (2018) |
| 2018 | 301a | N° de beneficiarias (madres) del bono Juana Azurduy atendidas | 4.0.1 (2018) |
| 2019-2020 | 301a | N° de beneficiarias (madres) del bono Juana Azurduy atendidas | 5.0.1 (2020) |
| 2021 | 301a | N° de beneficiarias (madres) del bono Juana Azurduy atendidas | 6.0.0 (2021) |
| 2022-2023 | 301a | N° de beneficiarias (madres) del bono Juana Azurduy atendidas | 6.0.1 (2022) |
| 2024-2025 | 301a | N° de beneficiarias (madres) del bono Juana Azurduy atendidas | 7.0.1 (2026) |
