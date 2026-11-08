# Enfermedad por hantavirus

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | semanal |
| Municipios con registros | 57 |
| Desagregación | sexo, edad |
| Filas | 2.179 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001 | 15-59 |
| 2002 | 15-59, 60+ |
| 2003 | 5-14, 15-59, 60+ |
| 2004 | 5-14, 15-59 |
| 2005-2007 | 1-4, 5-14, 15-59, 60+ |
| 2008 | 1-4, 5-9, 10-20, 21-59, 60+ |
| 2009 | <1, 5-9, 10-20, 21-59 |
| 2010 | 1-4, 5-9, 10-20, 21-59, 60+ |
| 2011-2012 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |
| 2013 | 10-20, 21-59, 60+ |
| 2014 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |
| 2015 | 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2016-2019 | 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2020 | 5-9, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2021 | 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2022 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2023 | 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2024 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2025 | 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2001 | 5 |
| 2002 | 13 |
| 2003 | 26 |
| 2004 | 13 |
| 2005 | 60 |
| 2006 | 82 |
| 2007 | 58 |
| 2008 | 62 |
| 2009 | 78 |
| 2010 | 51 |
| 2011 | 91 |
| 2012 | 50 |
| 2013 | 38 |
| 2014 | 99 |
| 2015 | 91 |
| 2016 | 181 |
| 2017 | 82 |
| 2018 | 98 |
| 2019 | 231 |
| 2020 | 33 |
| 2021 | 115 |
| 2022 | 385 |
| 2023 | 340 |
| 2024 | 238 |
| 2025 | 333 |

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
from 'datos/vigilancia/casos/hantavirus/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/hantavirus/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/hantavirus/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Enfermedad por hantavirus (este dataset): 2001-2025, formulario 302, 302a.
- [Hantavirus (sección otras infecciones, 2001-2003)](../../../vigilancia/casos/hantavirus_seccion_otras_infecciones/readme.md): 2001-2003, formulario 302.

En 2001-2003 el formulario registra esta enfermedad en dos secciones, con cifras distintas: "Sospecha diagnóstica" y otra sección. No sabemos qué cuenta cada una. La de sospecha continúa desde 2004: para una serie larga, use esa. No las sume: un caso puede estar en ambas.

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2001-2003 | 302 | 25.- Hantavirus |  |  |
| 2004 | 302 | 8 Enfer. por Hanta Virus | 1.0.4 (2013) | A98 |
| 2005-2009 | 302 | 12 Enfer. Por Hanta virus | 1.0.4 (2013) | A98 |
| 2010-2013 | 302 | Enfermedad por Hanta virus | 1.0.4 (2013) | A98 |
| 2014 | 302 | Enfermedad por Hanta virus | 2.0.0 (2014) | A98 |
| 2015 | 302a | Enfermedad por Hanta virus | 3.0.1 (2016) | A98 |
| 2016 | 302a | Enfermedad por Hanta virus | 3.0.2 (2016) | A98 |
| 2017 | 302a | Enfermedad por Hanta virus | 4.0.0 (2018) | A98 |
| 2018 | 302a | Enfermedad por Hanta virus | 4.0.1 (2018) | A98 |
| 2019-2020 | 302a | Enfermedad por Hanta virus | 5.0.1 (2020) | A98 |
| 2021 | 302a | Enfermedad por Hanta virus | 6.0.0 (2021) | A98 |
| 2022-2023 | 302a | Enfermedad por Hanta virus | 6.0.1 (2022) | A98 |
| 2024 | 302a | Enfermedad por Hanta virus | 7.0.1 (2026) | A98 |
| 2025 | 302a | 12. Enfermedad por Hanta virus | 7.0.1 (2026) | A98 |
