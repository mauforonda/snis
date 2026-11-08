# Partos atendidos por partera en servicio

Atenciones y nacimientos registrados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2023. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2023 |
| Periodicidad | mensual |
| Municipios con registros | 81 |
| Desagregación | lugar |
| Filas | 185 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2015 | 105 |
| 2016 | 305 |
| 2017 | 259 |
| 2018 | 147 |
| 2019 | 7 |
| 2020 | 8 |
| 2021 | 190 |
| 2022 | 118 |
| 2023 | 129 |

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
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/partos_atendidos_por_partera_en_servicio/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/partos_atendidos_por_partera_en_servicio/datos.parquet'
where gestion = 2023 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015 | 301a | Partos atendidos por partera en servicio | 3.0.1 (2016) |
| 2016 | 301a | Partos atendidos por partera en servicio | 3.0.2 (2016) |
| 2017 | 301a | Partos atendidos por partera en servicio | 4.0.0 (2018) |
| 2018 | 301a | Partos atendidos por partera en servicio | 4.0.1 (2018) |
| 2019-2020 | 301a | Partos atendidos por partera en servicio | 5.0.1 (2020) |
| 2021 | 301a | Partos atendidos por partera en servicio | 6.0.0 (2021) |
| 2022-2023 | 301a | Partos atendidos por partera en servicio | 6.0.1 (2022) |
