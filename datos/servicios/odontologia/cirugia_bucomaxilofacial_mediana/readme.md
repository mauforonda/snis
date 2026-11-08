# Cirugia bucomaxilofacial mediana

Atenciones registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2025. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2025 |
| Periodicidad | mensual |
| Municipios con registros | 207 |
| Desagregación | sexo, edad |
| Filas | 5.995 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015-2025 | <5, 5-13, 14-19, 20-59, 60+ |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2015 | 1.564 |
| 2016 | 1.394 |
| 2017 | 1.032 |
| 2018 | 1.183 |
| 2019 | 1.751 |
| 2020 | 926 |
| 2021 | 4.916 |
| 2022 | 2.872 |
| 2023 | 3.931 |
| 2024 | 2.898 |
| 2025 | 2.846 |

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
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/odontologia/cirugia_bucomaxilofacial_mediana/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/odontologia/cirugia_bucomaxilofacial_mediana/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/odontologia/cirugia_bucomaxilofacial_mediana/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015 | 301a | Cirugia Bucomaxilofacial Mediana | 3.0.1 (2016) |
| 2016 | 301a | Cirugia Bucomaxilofacial Mediana | 3.0.2 (2016) |
| 2017 | 301a | Cirugia Bucomaxilofacial Mediana | 4.0.0 (2018) |
| 2018 | 301a | Cirugia Bucomaxilofacial Mediana | 4.0.1 (2018) |
| 2019-2020 | 301a | Cirugia Bucomaxilofacial Mediana | 5.0.1 (2020) |
| 2021 | 301a | Cirugia Bucomaxilofacial Mediana | 6.0.0 (2021) |
| 2022-2023 | 301a | Cirugia Bucomaxilofacial Mediana | 6.0.1 (2022) |
| 2024-2025 | 301a | Cirugia Bucomaxilofacial Mediana | 7.0.1 (2026) |
