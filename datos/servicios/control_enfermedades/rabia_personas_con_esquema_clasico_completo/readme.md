# Rabia: personas con esquema clasico completo

Registros en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2025. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2025 |
| Periodicidad | mensual |
| Municipios con registros | 285 |
| Desagregación | sexo |
| Filas | 7.315 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2015 | 2.515 |
| 2016 | 2.256 |
| 2017 | 2.684 |
| 2018 | 3.483 |
| 2019 | 4.018 |
| 2020 | 4.546 |
| 2021 | 5.092 |
| 2022 | 9.206 |
| 2023 | 5.468 |
| 2024 | 5.813 |
| 2025 | 7.895 |

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
from 'datos/servicios/control_enfermedades/rabia_personas_con_esquema_clasico_completo/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/rabia_personas_con_esquema_clasico_completo/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/rabia_personas_con_esquema_clasico_completo/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015 | 301a | Total Nº de personas con esquema clasico completo | 3.0.1 (2016) |
| 2016 | 301a | Nº de personas con esquema clasico completo | 3.0.2 (2016) |
| 2017 | 301a | Nº de personas con esquema clasico completo | 4.0.0 (2018) |
| 2018 | 301a | Nº de personas con esquema clasico completo | 4.0.1 (2018) |
| 2019-2020 | 301a | Nº de personas con esquema clasico completo | 5.0.1 (2020) |
| 2021 | 301a | Nº de personas con esquema clasico completo | 6.0.0 (2021) |
| 2022-2023 | 301a | Nº de personas con esquema clasico completo | 6.0.1 (2022) |
| 2024-2025 | 301a | Nº de personas con esquema clasico completo | 7.0.1 (2026) |
