# Fiebre hemorrágica

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2003-2014, 2016-2025. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2003-2014, 2016-2025 |
| Periodicidad | semanal |
| Municipios con registros | 31 |
| Desagregación | sexo, edad |
| Filas | 653 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2003 | 1-4, 5-14, 15-59 |
| 2004 | 15-59 |
| 2005-2006 | 5-14, 15-59 |
| 2007 | 15-59 |
| 2008-2009 | 10-20 |
| 2010 | 5-9, 10-20, 21-59 |
| 2011-2012 | 10-20, 21-59 |
| 2013 | 1-4, 5-9, 10-20, 21-59 |
| 2014 | 5-9, 10-20, 21-59 |
| 2016-2017 | 20-39 |
| 2018 | 20-39, 40-49 |
| 2019 | 20-39, 40-49, 60+ |
| 2020 | 5-9, 10-14, 15-19, 20-39, 40-49, 50-59 |
| 2021-2022 | 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2023 | <6m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2024-2025 | 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2003 | 9 |
| 2004 | 12 |
| 2005 | 4 |
| 2006 | 4 |
| 2007 | 2 |
| 2008 | 1 |
| 2009 | 1 |
| 2010 | 6 |
| 2011 | 7 |
| 2012 | 10 |
| 2013 | 9 |
| 2014 | 21 |
| 2016 | 1 |
| 2017 | 1 |
| 2018 | 2 |
| 2019 | 17 |
| 2020 | 22 |
| 2021 | 69 |
| 2022 | 245 |
| 2023 | 194 |
| 2024 | 112 |
| 2025 | 210 |

### Advertencias

- 2004-2019 el nombre es "fiebre hemorrágica boliviana".

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
from 'datos/vigilancia/casos/fiebre_hemorragica/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/fiebre_hemorragica/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/fiebre_hemorragica/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Fiebre hemorrágica (sección otras infecciones, 2001-2003)](../../../vigilancia/casos/fiebre_hemorragica_seccion_otras_infecciones/readme.md): 2001-2003, formulario 302.
- Fiebre hemorrágica (este dataset): 2003-2025, formulario 302, 302a.

En 2001-2003 el formulario registra esta enfermedad en dos secciones, con cifras distintas: "Sospecha diagnóstica" y otra sección. No sabemos qué cuenta cada una. La de sospecha continúa desde 2004: para una serie larga, use esa. No las sume: un caso puede estar en ambas.

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2003 | 302 | 26.- Fiebre Hemorrágica |  |  |
| 2004 | 302 | 9 Fiebre Hemorrag. Bol |  |  |
| 2005-2009 | 302 | 8 Fiebre Hemorrag. Bol |  |  |
| 2010-2013 | 302 | Fiebre Hemorrágica Boliviana | 1.0.4 (2013) | A96 |
| 2014 | 302 | Fiebre Hemorrágica Boliviana | 2.0.0 (2014) | A96 |
| 2016 | 302a | Fiebre Hemorrágica Boliviana | 3.0.2 (2016) | A96 |
| 2017 | 302a | Fiebre Hemorrágica Boliviana | 4.0.0 (2018) | A96 |
| 2018 | 302a | Fiebre Hemorrágica Boliviana | 4.0.1 (2018) | A96 |
| 2019 | 302a | Fiebre Hemorrágica Boliviana | 5.0.1 (2020) | A96 |
| 2020 | 302a | Fiebre Hemorrágica | 5.0.1 (2020) | A96 |
| 2021 | 302a | Fiebre Hemorrágica | 6.0.0 (2021) | A96 |
| 2022-2023 | 302a | Fiebre Hemorrágica | 6.0.1 (2022) | A96 |
| 2024 | 302a | Fiebre Hemorrágica | 7.0.1 (2026) | A96 |
| 2025 | 302a | 07. Fiebre Hemorrágica | 7.0.1 (2026) | A96 |
