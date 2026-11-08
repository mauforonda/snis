# Enfermedad meningocócica

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2015-2025. Fuente: SNIS, formularios 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2025 |
| Periodicidad | semanal |
| Municipios con registros | 49 |
| Desagregación | sexo, edad |
| Filas | 264 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015 | <6m, 1-4, 10-14, 20-39, 40-49 |
| 2016 | <6m, 5-9, 10-14, 15-19, 20-39, 40-49, 60+ |
| 2017 | <6m, 6-11m, 1-4, 15-19, 20-39, 40-49, 60+ |
| 2018 | 6-11m, 1-4, 15-19, 20-39, 40-49, 60+ |
| 2019 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2020 | 6-11m, 1-4, 15-19, 20-39 |
| 2021 | <6m, 1-4, 5-9, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2022 | <6m, 6-11m, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2023 | <6m, 6-11m, 1-4, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2024 | 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2025 | <6m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2015 | 16 |
| 2016 | 15 |
| 2017 | 15 |
| 2018 | 12 |
| 2019 | 45 |
| 2020 | 8 |
| 2021 | 25 |
| 2022 | 28 |
| 2023 | 31 |
| 2024 | 45 |
| 2025 | 35 |

## Cómo utilizar

Cada fila da el número de casos de un periodo, un municipio y una población. Para obtener un total, sume las filas: el dataset no tiene filas de total. Una combinación sin fila significa que no hubo registros. Las convenciones de tiempo, territorio y población están en el [catálogo](../../../README.md#cómo-leer-los-datos).

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
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/enfermedad_meningococica/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/enfermedad_meningococica/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/enfermedad_meningococica/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Meningitis meningocócica](../../../vigilancia/casos/meningitis_meningococica/readme.md): 2001-2014, formulario 302.
- Enfermedad meningocócica (este dataset): 2015-2025, formulario 302a.

Hasta 2014 el formulario notifica la meningitis meningocócica; desde 2015, la enfermedad meningocócica, una definición más amplia. Consultarlos juntos como una serie supone que la definición más amplia no cambia la serie.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/meningitis_meningococica/datos.parquet',
    'datos/vigilancia/casos/enfermedad_meningococica/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2015 | 302a | Enfermedad Meningocócica | 3.0.1 (2016) | A39 |
| 2016 | 302a | Enfermedad Meningocócica | 3.0.2 (2016) | A39 |
| 2017 | 302a | Enfermedad Meningocócica | 4.0.0 (2018) | A39 |
| 2018 | 302a | Enfermedad Meningocócica | 4.0.1 (2018) | A39 |
| 2019-2020 | 302a | Enfermedad Meningocócica | 5.0.1 (2020) | A39 G01 |
| 2021 | 302a | Enfermedad Meningocócica | 6.0.0 (2021) | A39 G01 |
| 2022-2023 | 302a | Enfermedad Meningocócica | 6.0.1 (2022) | A39 G01 |
| 2024 | 302a | Enfermedad Meningocócica | 7.0.1 (2026) | A39 G01 |
| 2025 | 302a | 09. Enfermedad Meningocócica | 7.0.1 (2026) | A39 G01 |
