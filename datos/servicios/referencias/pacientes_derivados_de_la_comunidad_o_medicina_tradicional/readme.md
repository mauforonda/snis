# Pacientes referidos de la comunidad o medicina tradicional

Pacientes o referencias registrados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2010-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2010-2025 |
| Periodicidad | mensual |
| Municipios con registros | 257 |
| Desagregación |  |
| Filas | 5.440 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2010 | 1.816 |
| 2011 | 1.598 |
| 2012 | 2.171 |
| 2013 | 1.969 |
| 2014 | 2.052 |
| 2015 | 1.779 |
| 2016 | 8.211 |
| 2017 | 5.492 |
| 2018 | 11.185 |
| 2019 | 8.700 |
| 2020 | 2.933 |
| 2021 | 2.031 |
| 2022 | 1.767 |
| 2023 | 1.375 |
| 2024 | 1.263 |
| 2025 | 1.124 |

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
from 'datos/servicios/referencias/pacientes_derivados_de_la_comunidad_o_medicina_tradicional/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/referencias/pacientes_derivados_de_la_comunidad_o_medicina_tradicional/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2010-2013 | 301 | Pacientes derivados de la comunidad o medicina tradicional | 1.0.4 (2013) |
| 2014 | 301 | 2.2 Pacientes derivados de la comunidad o medicina tradicional | 2.0.0 (2014) |
| 2015 | 301a | Pacientes derivados de la comunidad o medicina tradicional | 3.0.1 (2016) |
| 2016 | 301a | Pacientes derivados de la comunidad o medicina tradicional | 3.0.2 (2016) |
| 2017 | 301a | Pacientes derivados de la comunidad o medicina tradicional | 4.0.0 (2018) |
| 2018 | 301a | Pacientes derivados de la comunidad o medicina tradicional | 4.0.1 (2018) |
| 2019-2020 | 301a | Pacientes derivados de la comunidad o medicina tradicional | 5.0.1 (2020) |
| 2021 | 301a | Pacientes derivados de la comunidad o medicina tradicional | 6.0.0 (2021) |
| 2022-2023 | 301a | Pacientes derivados de la comunidad o medicina tradicional | 6.0.1 (2022) |
| 2024-2025 | 301a | Pacientes referidos de la comunidad o medicina tradicional | 7.0.1 (2026) |
