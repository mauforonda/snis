# Talla para la edad (2008-2025)

Personas evaluadas, por resultado en los establecimientos de salud de Bolivia, por semana o mes y municipio, en las gestiones 2008-2009, 2015-2018, 2020-2025. Fuente: SNIS, formularios 302, 302b.

## Qué es

| | |
| --- | --- |
| Gestiones | 2008-2009, 2015-2018, 2020-2025 |
| Periodicidad | semanal y mensual |
| Municipios con registros | 343 |
| Desagregación | clasificación, sexo, edad |
| Filas | 583.412 |

Valores de `clasificacion` (clasificación):

- baja (2008-2009, 2015-2018, 2020-2025)
- normal (2008-2009, 2015-2018, 2020-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2008-2009 | 2-11m, 1, 2-4 |
| 2015-2018 | 2-11m, 1, 2-4 |
| 2020-2025 | 2-11m, 1, 2-4 |

Total por gestión:

| Gestión | Personas |
| ---: | ---: |
| 2008 | 1.502.544 |
| 2009 | 3.015.509 |
| 2015 | 2.118.382 |
| 2016 | 1.483.079 |
| 2017 | 1.284.584 |
| 2018 | 1.086.412 |
| 2020 | 461.631 |
| 2021 | 599.697 |
| 2022 | 695.262 |
| 2023 | 725.263 |
| 2024 | 705.300 |
| 2025 | 686.444 |

## Cómo utilizar

Cada fila da el número de personas de un periodo, un municipio y una población. Para obtener un total, sume las filas: el dataset no tiene filas de total. Una combinación sin fila significa que no hubo registros. Las convenciones de tiempo, territorio y población están en el [catálogo](../../../README.md#cómo-leer-los-datos).

| Columna | Tipo | Descripción |
| --- | --- | --- |
| `gestion` | integer | Año calendario (gestión) del registro. |
| `semana` | integer | Semana epidemiológica, de 1 a 53. Va de domingo a sábado. |
| `mes` | integer | Mes, de 1 a 12. |
| `fecha_inicio` | date | Primer día de la semana o del mes. |
| `departamento` | string | Nombre del departamento. |
| `municipio` | string | Nombre del municipio. |
| `municipio_codigo` | string | Código del municipio, 6 dígitos: departamento (2), provincia (2) y municipio (2). |
| `clasificacion` | string | Clasificación. |
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `personas` | integer | Número de personas en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(personas) as personas
from 'datos/vigilancia/estado_nutricional/talla_2008_2025/datos.parquet'
group by gestion order by gestion;

-- Por gestión y clasificacion
select gestion, clasificacion, sum(personas) as personas
from 'datos/vigilancia/estado_nutricional/talla_2008_2025/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(personas) as personas
from 'datos/vigilancia/estado_nutricional/talla_2008_2025/datos.parquet'
where gestion = 2025 group by all order by personas desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Talla para la edad (2005-2006)](../../../vigilancia/estado_nutricional/talla_2005_2006/readme.md): 2005-2006, formulario 302.
- [Talla baja (moderada y grave) (2007)](../../../vigilancia/estado_nutricional/talla_2007/readme.md): 2007, formulario 302.
- Talla para la edad (2008-2025) (este dataset): 2008-2025, formulario 302, 302b.

Las categorías de `clasificacion` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(personas) as personas
from read_parquet([
    'datos/vigilancia/estado_nutricional/talla_2005_2006/datos.parquet',
    'datos/vigilancia/estado_nutricional/talla_2007/datos.parquet',
    'datos/vigilancia/estado_nutricional/talla_2008_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2008-2009 | 302 | 54 Talla normal (T N); 55 Talla baja (TB) |  |
| 2015 | 302b | Talla Normal; Talla baja | 3.0.1 (2016) |
| 2016 | 302b | Talla Normal; Talla baja | 3.0.2 (2016) |
| 2017 | 302b | Talla Normal; Talla baja | 4.0.0 (2018) |
| 2018 | 302b | Talla Normal; Talla baja | 4.0.1 (2018) |
| 2020 | 302b | Talla Normal; Talla baja | 5.0.1 (2020) |
| 2021 | 302b | Talla Normal; Talla baja | 6.0.0 (2021) |
| 2022-2023 | 302b | Talla Normal; Talla baja | 6.0.1 (2022) |
| 2024-2025 | 302b | Talla Normal; Talla baja | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302b, grupos 01, 05, 06, 07 y 10: el segundo nivel dice NUEVO/REPETIDO, pero las reglas de SOAPS dividen estas variables por sexo. Las muertes por cáncer de mama y de cuello uterino están en REPETIDO en todas las gestiones 2016-2025, y el tabaco y el alcohol (grupo 01, 2024-2025) están sobre todo en NUEVO: REPETIDO es mujer y NUEVO es hombre.
- 302 (grupos 11 y 14, 2008-2014) y 302b (grupos 06 y 07): SOAPS cuenta la columna "Menor de 1 año" desde los 2 meses (reglas de 2 a 11 meses).
