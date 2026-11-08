# Lepra (2007-2025)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2007-2025. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2007-2025 |
| Periodicidad | semanal |
| Municipios con registros | 113 |
| Desagregación | forma clínica, sexo, edad |
| Filas | 1.983 |

Valores de `forma_clinica` (forma clínica):

- multibacilar (2007-2025)
- paucibacilar (2007-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2007 | <1, 1-4, 5-14, 15-59, 60+ |
| 2008 | 5-9, 10-20, 21-59, 60+ |
| 2009-2014 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |
| 2015 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2016 | <6m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2017-2018 | 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2019-2020 | 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2021 | 5-9, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2022 | 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2023 | 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2024 | 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2025 | 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2007 | 346 |
| 2008 | 48 |
| 2009 | 38 |
| 2010 | 112 |
| 2011 | 294 |
| 2012 | 241 |
| 2013 | 167 |
| 2014 | 168 |
| 2015 | 356 |
| 2016 | 287 |
| 2017 | 284 |
| 2018 | 190 |
| 2019 | 109 |
| 2020 | 61 |
| 2021 | 53 |
| 2022 | 65 |
| 2023 | 122 |
| 2024 | 153 |
| 2025 | 70 |

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
| `forma_clinica` | string | Forma clínica. |
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/lepra_2007_2025/datos.parquet'
group by gestion order by gestion;

-- Por gestión y forma_clinica
select gestion, forma_clinica, sum(casos) as casos
from 'datos/vigilancia/casos/lepra_2007_2025/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/lepra_2007_2025/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Lepra (2001-2006)](../../../vigilancia/casos/lepra_2001_2006/readme.md): 2001-2006, formulario 302.
- Lepra (2007-2025) (este dataset): 2007-2025, formulario 302, 302a.

Las categorías de `forma_clinica` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/lepra_2001_2006/datos.parquet',
    'datos/vigilancia/casos/lepra_2007_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2007 | 302 | 34 Lepra paucibacilar*; 35 Lepra multibacilar * | 1.0.4 (2013) | A30 |
| 2008-2009 | 302 | 31 Lepra paucibacilar*; 32 Lepra multibacilar * | 1.0.4 (2013) | A30 |
| 2010-2013 | 302 | Lepra multibacilar *; Lepra paucibacilar* | 1.0.4 (2013) | A30 |
| 2014 | 302 | Lepra multibacilar *; Lepra paucibacilar* | 2.0.0 (2014) | A30 |
| 2015 | 302a | Lepra Multibacilar; Lepra Paucibacilar | 3.0.1 (2016) | A30 |
| 2016 | 302a | Lepra Multibacilar; Lepra Paucibacilar | 3.0.2 (2016) | A30 |
| 2017 | 302a | Lepra Multibacilar; Lepra Paucibacilar | 4.0.0 (2018) | A30 |
| 2018 | 302a | Lepra Multibacilar; Lepra Paucibacilar | 4.0.1 (2018) | A30 |
| 2019-2020 | 302a | Lepra Multibacilar; Lepra Paucibacilar | 5.0.1 (2020) | A30 |
| 2021 | 302a | Lepra Multibacilar; Lepra Paucibacilar | 6.0.0 (2021) | A30 |
| 2022-2023 | 302a | Lepra Multibacilar; Lepra Paucibacilar | 6.0.1 (2022) | A30 |
| 2024-2025 | 302a | 3. Lepra Paucibacilar; 4. Lepra Multibacilar | 7.0.1 (2026) | A30 |
