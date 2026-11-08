# Enfermedad renal

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2018, 2020-2023. Fuente: SNIS, formularios 302b.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2018, 2020-2023 |
| Periodicidad | mensual |
| Municipios con registros | 339 |
| Desagregación | sexo, edad, nuevo o repetido |
| Filas | 95.328 |

Valores de `caso` (nuevo o repetido):

- nuevo (2015-2018, 2020-2023)
- repetido (2015-2018, 2020-2023)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015-2018 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2020-2023 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2015 | 44.127 |
| 2016 | 61.577 |
| 2017 | 72.625 |
| 2018 | 93.268 |
| 2020 | 49.109 |
| 2021 | 80.789 |
| 2022 | 105.641 |
| 2023 | 131.818 |

### Advertencias

- Cuenta todas las enfermedades renales (CIE-10 N00 a N29), no sólo la enfermedad renal crónica. Los estadios 3, 4 y 5 tienen su propio dataset; no sabemos si sus casos están también aquí.

## Cómo utilizar

Cada fila da el número de casos de un periodo, un municipio y una población. Para obtener un total, sume las filas: el dataset no tiene filas de total. Una combinación sin fila significa que no hubo registros. Las convenciones de tiempo, territorio y población están en el [catálogo](../../../README.md#cómo-leer-los-datos).

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
| `caso` | string | nuevo, repetido, seguimiento o primera, como lo registra el formulario. |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/enfermedad_renal/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/enfermedad_renal/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/enfermedad_renal/datos.parquet'
where gestion = 2023 group by all order by casos desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2015 | 302b | Enfermedad Renal | 3.0.1 (2016) | N00 N01 N02 N03 N04 N05 N06 N07 N08 N10 N11 N12 N13 N14 N15 N16 N17 N18 N19 N20 N21 N22 N23 N25 N26 N27 N28 N29 |
| 2016 | 302b | Enfermedad Renal | 3.0.2 (2016) | N00 N01 N02 N03 N04 N05 N06 N07 N08 N10 N11 N12 N13 N14 N15 N16 N17 N18 N19 N20 N21 N22 N23 N25 N26 N27 N28 N29 |
| 2017 | 302b | Enfermedad Renal | 4.0.0 (2018) | N00 N01 N02 N03 N04 N05 N06 N07 N08 N10 N11 N12 N13 N14 N15 N16 N17 N18 N19 N20 N21 N22 N23 N25 N26 N27 N28 N29 |
| 2018 | 302b | Enfermedad Renal | 4.0.1 (2018) | N00 N01 N02 N03 N04 N05 N06 N07 N08 N10 N11 N12 N13 N14 N15 N16 N17 N18 N19 N20 N21 N22 N23 N25 N26 N27 N28 N29 |
| 2020 | 302b | Enfermedad Renal | 5.0.1 (2020) | N00 N01 N02 N03 N04 N05 N06 N07 N08 N10 N11 N12 N13 N14 N15 N16 N17 N18 N19 N20 N21 N22 N23 N25 N26 N27 N28 N29 |
| 2021 | 302b | Enfermedad Renal | 6.0.0 (2021) | N00 N01 N02 N03 N04 N05 N06 N07 N08 N10 N11 N12 N13 N14 N15 N16 N17 N18 N19 N20 N21 N22 N23 N25 N26 N27 N28 N29 |
| 2022-2023 | 302b | Enfermedad Renal | 6.0.1 (2022) | N00 N01 N02 N03 N04 N05 N06 N07 N08 N10 N11 N12 N13 N14 N15 N16 N17 N18 N19 N20 N21 N22 N23 N25 N26 N27 N28 N29 |
