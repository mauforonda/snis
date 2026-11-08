# Enfermedad renal crónica por estadio (2015-2023)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2018, 2020-2023. Fuente: SNIS, formularios 302b.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2018, 2020-2023 |
| Periodicidad | mensual |
| Municipios con registros | 153 |
| Desagregación | estadio, sexo, edad, nuevo o repetido |
| Filas | 18.852 |

Valores de `estadio` (estadio):

- 3 (2015-2018, 2020-2023)
- 4 (2015-2018, 2020-2023)
- 5 (2015-2018, 2020-2023)

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
| 2015 | 5.607 |
| 2016 | 7.220 |
| 2017 | 8.802 |
| 2018 | 15.314 |
| 2020 | 14.174 |
| 2021 | 28.910 |
| 2022 | 67.397 |
| 2023 | 68.836 |

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
| `estadio` | string | Estadio. |
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
from 'datos/vigilancia/casos/enfermedad_renal_cronica_2015_2023/datos.parquet'
group by gestion order by gestion;

-- Por gestión y estadio
select gestion, estadio, sum(casos) as casos
from 'datos/vigilancia/casos/enfermedad_renal_cronica_2015_2023/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/enfermedad_renal_cronica_2015_2023/datos.parquet'
where gestion = 2023 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Enfermedad renal crónica por estadio (2015-2023) (este dataset): 2015-2023, formulario 302b.
- [Enfermedad renal crónica por estadio (2024-2025)](../../../vigilancia/casos/enfermedad_renal_cronica_2024_2025/readme.md): 2024-2025, formulario 302b.

Las categorías de `estadio` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/enfermedad_renal_cronica_2015_2023/datos.parquet',
    'datos/vigilancia/casos/enfermedad_renal_cronica_2024_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015 | 302b | Enfermedad Renal Estadio 3; Enfermedad Renal Estadio 4; Enfermedad Renal Estadio 5 | 3.0.1 (2016) |
| 2016 | 302b | Enfermedad Renal Estadio 3; Enfermedad Renal Estadio 4; Enfermedad Renal Estadio 5 | 3.0.2 (2016) |
| 2017 | 302b | Enfermedad Renal Estadio 3; Enfermedad Renal Estadio 4; Enfermedad Renal Estadio 5 | 4.0.0 (2018) |
| 2018 | 302b | Enfermedad Renal Estadio 3; Enfermedad Renal Estadio 4; Enfermedad Renal Estadio 5 | 4.0.1 (2018) |
| 2020 | 302b | Enfermedad Renal Estadio 3; Enfermedad Renal Estadio 4; Enfermedad Renal Estadio 5 | 5.0.1 (2020) |
| 2021 | 302b | Enfermedad Renal Estadio 3; Enfermedad Renal Estadio 4; Enfermedad Renal Estadio 5 | 6.0.0 (2021) |
| 2022-2023 | 302b | Enfermedad Renal Estadio 3; Enfermedad Renal Estadio 4; Enfermedad Renal Estadio 5 | 6.0.1 (2022) |
