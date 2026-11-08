# Fiebre amarilla

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | semanal |
| Municipios con registros | 63 |
| Desagregación | sexo, edad |
| Filas | 735 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001 | 5-14, 15-59 |
| 2002 | 1-4, 5-14, 15-59 |
| 2003 | 15-59 |
| 2004-2005 | 1-4, 5-14, 15-59 |
| 2006 | 5-14, 15-59, 60+ |
| 2007 | 1-4, 5-14, 15-59, 60+ |
| 2008 | 10-20, 21-59, 60+ |
| 2009-2010 | 5-9, 10-20, 21-59, 60+ |
| 2011 | 1-4, 10-20, 21-59 |
| 2012 | <1, 5-9, 10-20, 21-59 |
| 2013-2014 | 5-9, 10-20, 21-59, 60+ |
| 2015 | 5-9, 10-14, 20-39, 40-49, 50-59, 60+ |
| 2016 | 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2017 | 1-4, 5-9, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2018 | 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2019 | 1-4, 5-9, 10-14, 20-39, 40-49, 50-59, 60+ |
| 2020 | 10-14, 20-39, 40-49 |
| 2021 | 6-11m, 1-4, 10-14, 20-39, 50-59, 60+ |
| 2022 | <6m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2023 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2024-2025 | 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2001 | 5 |
| 2002 | 14 |
| 2003 | 6 |
| 2004 | 20 |
| 2005 | 47 |
| 2006 | 58 |
| 2007 | 63 |
| 2008 | 18 |
| 2009 | 6 |
| 2010 | 8 |
| 2011 | 9 |
| 2012 | 12 |
| 2013 | 43 |
| 2014 | 32 |
| 2015 | 19 |
| 2016 | 20 |
| 2017 | 44 |
| 2018 | 38 |
| 2019 | 30 |
| 2020 | 11 |
| 2021 | 16 |
| 2022 | 79 |
| 2023 | 44 |
| 2024 | 103 |
| 2025 | 119 |

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
from 'datos/vigilancia/casos/fiebre_amarilla/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/fiebre_amarilla/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/fiebre_amarilla/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Fiebre amarilla (este dataset): 2001-2025, formulario 302, 302a.
- [Fiebre amarilla (sección inmunoprevenibles, 2001-2003)](../../../vigilancia/casos/fiebre_amarilla_seccion_inmunoprevenibles/readme.md): 2001-2003, formulario 302.

En 2001-2003 el formulario registra esta enfermedad en dos secciones, con cifras distintas: "Sospecha diagnóstica" y otra sección. No sabemos qué cuenta cada una. La de sospecha continúa desde 2004: para una serie larga, use esa. No las sume: un caso puede estar en ambas.

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2001-2003 | 302 | 22.- Fiebre amarilla | 1.0.4 (2013) | A95 |
| 2004 | 302 | 6 Fiebre amarilla | 1.0.4 (2013) | A95 |
| 2005-2009 | 302 | 5 Fiebre amarilla | 1.0.4 (2013) | A95 |
| 2010-2013 | 302 | Fiebre amarilla | 1.0.4 (2013) | A95 |
| 2014 | 302 | Fiebre amarilla | 2.0.0 (2014) | A95 |
| 2015 | 302a | Fiebre amarilla | 3.0.1 (2016) | A95 |
| 2016 | 302a | Fiebre amarilla | 3.0.2 (2016) | A95 |
| 2017 | 302a | Fiebre amarilla | 4.0.0 (2018) | A95 |
| 2018 | 302a | Fiebre amarilla | 4.0.1 (2018) | A95 |
| 2019-2020 | 302a | Fiebre amarilla | 5.0.1 (2020) | A95 |
| 2021 | 302a | Fiebre amarilla | 6.0.0 (2021) | A95 |
| 2022-2023 | 302a | Fiebre amarilla | 6.0.1 (2022) | A95 |
| 2024 | 302a | Fiebre amarilla | 7.0.1 (2026) | A95 |
| 2025 | 302a | 06. Fiebre amarilla | 7.0.1 (2026) | A95 |
