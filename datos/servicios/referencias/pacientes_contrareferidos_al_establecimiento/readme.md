# Pacientes retornados al establecimiento de origen

Pacientes o referencias registrados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2010-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2010-2025 |
| Periodicidad | mensual |
| Municipios con registros | 341 |
| Desagregación |  |
| Filas | 19.320 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2010 | 13.621 |
| 2011 | 16.901 |
| 2012 | 18.414 |
| 2013 | 24.704 |
| 2014 | 28.164 |
| 2015 | 18.871 |
| 2016 | 17.174 |
| 2017 | 17.975 |
| 2018 | 28.522 |
| 2019 | 58.077 |
| 2020 | 34.415 |
| 2021 | 42.425 |
| 2022 | 77.483 |
| 2023 | 89.782 |
| 2024 | 106.338 |
| 2025 | 133.203 |

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
from 'datos/servicios/referencias/pacientes_contrareferidos_al_establecimiento/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/referencias/pacientes_contrareferidos_al_establecimiento/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2010-2013 | 301 | Pacientes retornados al establecimiento de origen | 1.0.4 (2013) |
| 2014 | 301 | 2.3 Pacientes retornados al establecimiento de origen | 2.0.0 (2014) |
| 2015 | 301a | Pacientes contrareferidos al establecimiento | 3.0.1 (2016) |
| 2016 | 301a | Pacientes contrareferidos al establecimiento | 3.0.2 (2016) |
| 2017 | 301a | Pacientes contrareferidos al establecimiento | 4.0.0 (2018) |
| 2018 | 301a | Pacientes contrareferidos al establecimiento | 4.0.1 (2018) |
| 2019-2020 | 301a | Pacientes contrareferidos al establecimiento | 5.0.1 (2020) |
| 2021 | 301a | Pacientes contrareferidos al establecimiento | 6.0.0 (2021) |
| 2022-2023 | 301a | Pacientes contrareferidos al establecimiento | 6.0.1 (2022) |
| 2024-2025 | 301a | Pacientes contrarreferidos al establecimiento | 7.0.1 (2026) |
