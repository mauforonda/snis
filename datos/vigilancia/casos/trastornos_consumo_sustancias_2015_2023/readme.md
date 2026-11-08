# Trastornos del comportamiento por consumo de sustancias (2015-2023)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2018, 2020-2023. Fuente: SNIS, formularios 302b.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2018, 2020-2023 |
| Periodicidad | mensual |
| Municipios con registros | 231 |
| Desagregación | sexo, edad, nuevo o repetido |
| Filas | 12.845 |

Valores de `caso` (nuevo o repetido):

- nuevo (2015-2018, 2020-2023)
- repetido (2015-2018, 2020-2023)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015-2016 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2017-2018 | 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2020 | 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2021 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2022 | <6m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2023 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2015 | 4.421 |
| 2016 | 4.916 |
| 2017 | 9.202 |
| 2018 | 6.747 |
| 2020 | 4.264 |
| 2021 | 8.122 |
| 2022 | 10.477 |
| 2023 | 11.672 |

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
from 'datos/vigilancia/casos/trastornos_consumo_sustancias_2015_2023/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/trastornos_consumo_sustancias_2015_2023/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/trastornos_consumo_sustancias_2015_2023/datos.parquet'
where gestion = 2023 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Trastornos del comportamiento por consumo de sustancias (2015-2023) (este dataset): 2015-2023, formulario 302b.
- [Trastornos por consumo de sustancias (2024-2025)](../../../vigilancia/casos/trastornos_consumo_sustancias_2024_2025/readme.md): 2024-2025, formulario 302b.

Las categorías de `sustancia` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/trastornos_consumo_sustancias_2015_2023/datos.parquet',
    'datos/vigilancia/casos/trastornos_consumo_sustancias_2024_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2015 | 302b | Transtornos de comportamiento por consumo de susta | 3.0.1 (2016) | F10 F11 F12 F13 F14 F15 F16 F17 F18 F19 |
| 2016 | 302b | Transtornos de comportamiento por consumo de susta | 3.0.2 (2016) | F10 F11 F12 F13 F14 F15 F16 F17 F18 F19 |
| 2017 | 302b | Transtornos de comportamiento por consumo de susta | 4.0.0 (2018) | F10 F11 F12 F13 F14 F15 F16 F17 F18 F19 |
| 2018 | 302b | Transtornos de comportamiento por consumo de susta | 4.0.1 (2018) | F10 F11 F12 F13 F14 F15 F16 F17 F18 F19 |
| 2020 | 302b | Transtornos de comportamiento por consumo de susta | 5.0.1 (2020) | F10 F11 F12 F13 F14 F15 F16 F17 F18 F19 |
| 2021 | 302b | Transtornos de comportamiento por consumo de susta | 6.0.0 (2021) | F10 F11 F12 F13 F14 F15 F16 F17 F18 F19 |
| 2022-2023 | 302b | Transtornos de comportamiento por consumo de susta | 6.0.1 (2022) | F10 F11 F12 F13 F14 F15 F16 F17 F18 F19 |
