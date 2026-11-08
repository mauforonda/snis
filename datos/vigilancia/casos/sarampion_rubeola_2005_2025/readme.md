# Sarampión o rubéola (2005-2025)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2005-2025. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2005-2025 |
| Periodicidad | semanal |
| Municipios con registros | 190 |
| Desagregación | enfermedad, sexo, edad |
| Filas | 4.609 |

Valores de `enfermedad` (enfermedad):

- sarampión o rubéola (2005-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2005-2007 | <1, 1-4, 5-14, 15-59 |
| 2008-2009 | <1, 1-4, 5-9, 10-20, 21-59 |
| 2010-2014 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |
| 2015 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49 |
| 2016 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59 |
| 2017 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 60+ |
| 2018-2020 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2021 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49 |
| 2022-2025 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2005 | 163 |
| 2006 | 134 |
| 2007 | 77 |
| 2008 | 328 |
| 2009 | 97 |
| 2010 | 114 |
| 2011 | 188 |
| 2012 | 177 |
| 2013 | 152 |
| 2014 | 288 |
| 2015 | 81 |
| 2016 | 109 |
| 2017 | 51 |
| 2018 | 238 |
| 2019 | 138 |
| 2020 | 151 |
| 2021 | 97 |
| 2022 | 249 |
| 2023 | 250 |
| 2024 | 460 |
| 2025 | 2.666 |

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
| `enfermedad` | string | Enfermedad. |
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/sarampion_rubeola_2005_2025/datos.parquet'
group by gestion order by gestion;

-- Por gestión y enfermedad
select gestion, enfermedad, sum(casos) as casos
from 'datos/vigilancia/casos/sarampion_rubeola_2005_2025/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/sarampion_rubeola_2005_2025/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Sarampión y rubéola (2001-2003)](../../../vigilancia/casos/sarampion_rubeola_2001_2003/readme.md): 2001-2003, formulario 302.
- [Sarampión y rubéola (2004)](../../../vigilancia/casos/sarampion_rubeola_2004/readme.md): 2004, formulario 302.
- Sarampión o rubéola (2005-2025) (este dataset): 2005-2025, formulario 302, 302a.

Las categorías de `enfermedad` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/sarampion_rubeola_2001_2003/datos.parquet',
    'datos/vigilancia/casos/sarampion_rubeola_2004/datos.parquet',
    'datos/vigilancia/casos/sarampion_rubeola_2005_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2005-2009 | 302 | 1 Sarampión / Rubéola | 1.0.4 (2013) | B05 B06 |
| 2010-2013 | 302 | Sarampión / Rubéola | 1.0.4 (2013) | B05 B06 |
| 2014 | 302 | Sarampión / Rubéola | 2.0.0 (2014) | B05 B06 |
| 2015 | 302a | Sarampión / Rubéola | 3.0.1 (2016) | B05 B06 |
| 2016 | 302a | Sarampión / Rubéola | 3.0.2 (2016) | B05 B06 |
| 2017 | 302a | Sarampión / Rubéola | 4.0.0 (2018) | B05 B06 |
| 2018 | 302a | Sarampión / Rubéola | 4.0.1 (2018) | B05 B06 |
| 2019-2020 | 302a | Sarampión / Rubéola | 5.0.1 (2020) | B05 B06 |
| 2021 | 302a | Sarampión / Rubéola | 6.0.0 (2021) | B05 B06 |
| 2022-2023 | 302a | Sarampión / Rubéola | 6.0.1 (2022) | B05 B06 |
| 2024 | 302a | Sarampión / Rubéola | 7.0.1 (2026) | B05 B06 |
| 2025 | 302a | 01. Sarampión / Rubéola | 7.0.1 (2026) | B05 B06 |
