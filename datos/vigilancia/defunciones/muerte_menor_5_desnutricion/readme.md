# Muerte en menores de 5 años por desnutrición aguda grave

Muertes por esta causa en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2011-2025. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2011-2025 |
| Periodicidad | semanal |
| Municipios con registros | 124 |
| Desagregación | sexo, edad, lugar |
| Filas | 515 |

Valores de `lugar` (lugar):

- dentro (2011-2025)
- fuera (2011-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015-2025 | <6m, 6-11m, 1-4 |

Total por gestión:

| Gestión | Defunciones |
| ---: | ---: |
| 2011 | 51 |
| 2012 | 49 |
| 2013 | 50 |
| 2014 | 43 |
| 2015 | 53 |
| 2016 | 44 |
| 2017 | 35 |
| 2018 | 30 |
| 2019 | 21 |
| 2020 | 27 |
| 2021 | 30 |
| 2022 | 15 |
| 2023 | 34 |
| 2024 | 18 |
| 2025 | 29 |

## Cómo utilizar

Cada fila da el número de defunciones de un periodo, un municipio y una población. Para obtener un total, sume las filas: el dataset no tiene filas de total. Una combinación sin fila significa que no hubo registros. Las convenciones de tiempo, territorio y población están en el [catálogo](../../../README.md#cómo-leer-los-datos).

| Columna | Tipo | Descripción |
| --- | --- | --- |
| `gestion` | integer | Año calendario (gestión) del registro. |
| `semana` | integer | Semana epidemiológica, de 1 a 53. Va de domingo a sábado. |
| `fecha_inicio` | date | Primer día de la semana o del mes. |
| `departamento` | string | Nombre del departamento. |
| `municipio` | string | Nombre del municipio. |
| `municipio_codigo` | string | Código del municipio, 6 dígitos: departamento (2), provincia (2) y municipio (2). |
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `defunciones` | integer | Número de defunciones en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_menor_5_desnutricion/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_menor_5_desnutricion/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_menor_5_desnutricion/datos.parquet'
where gestion = 2025 group by all order by defunciones desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2011-2013 | 302 | Muerte menor de 5 años por desnutricion aguda gra | 1.0.4 (2013) |
| 2014 | 302 | Muerte menor de 5 años por desnutricion aguda gra | 2.0.0 (2014) |
| 2015 | 302a | Muerte menor de 5 años por desnutrición aguda grave | 3.0.1 (2016) |
| 2016 | 302a | Muerte menor de 5 años por desnutrición aguda grave | 3.0.2 (2016) |
| 2017 | 302a | Muerte menor de 5 años por desnutrición aguda grave | 4.0.0 (2018) |
| 2018 | 302a | Muerte menor de 5 años por desnutrición aguda grave | 4.0.1 (2018) |
| 2019-2020 | 302a | Muerte menor de 5 años por desnutrición aguda grave | 5.0.1 (2020) |
| 2021 | 302a | Muerte menor de 5 años por desnutrición aguda grave | 6.0.0 (2021) |
| 2022-2023 | 302a | Muerte menor de 5 años por desnutrición aguda grave | 6.0.1 (2022) |
| 2024-2025 | 302a | 3. Muerte menor de 5 años por desnutrición aguda grave | 7.0.1 (2026) |
