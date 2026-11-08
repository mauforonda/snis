# Cólera

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2008, 2010-2013, 2016, 2018-2024. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2008, 2010-2013, 2016, 2018-2024 |
| Periodicidad | semanal |
| Municipios con registros | 45 |
| Desagregación | sexo, edad |
| Filas | 178 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001 | <1, 15-59 |
| 2002 | 1-4, 5-14, 15-59, 60+ |
| 2003 | <1, 5-14, 15-59, 60+ |
| 2004 | 15-59 |
| 2005 | 60+ |
| 2006 | 15-59, 60+ |
| 2007 | <1, 15-59 |
| 2008 | <1, 1-4, 21-59 |
| 2010 | <1, 1-4, 10-20, 21-59 |
| 2011 | <1, 1-4, 60+ |
| 2012 | <1, 1-4, 10-20, 21-59 |
| 2013 | 1-4, 21-59, 60+ |
| 2016 | 1-4 |
| 2018 | 1-4, 20-39 |
| 2019 | 1-4, 10-14, 15-19, 20-39 |
| 2020 | 1-4, 10-14, 20-39, 60+ |
| 2021 | 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2022 | 6-11m, 20-39, 40-49, 50-59 |
| 2023 | 40-49, 60+ |
| 2024 | 40-49 |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2001 | 11 |
| 2002 | 63 |
| 2003 | 29 |
| 2004 | 6 |
| 2005 | 5 |
| 2006 | 2 |
| 2007 | 13 |
| 2008 | 3 |
| 2010 | 14 |
| 2011 | 7 |
| 2012 | 5 |
| 2013 | 5 |
| 2016 | 1 |
| 2018 | 2 |
| 2019 | 9 |
| 2020 | 10 |
| 2021 | 23 |
| 2022 | 4 |
| 2023 | 2 |
| 2024 | 1 |

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
from 'datos/vigilancia/casos/colera/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/colera/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/colera/datos.parquet'
where gestion = 2024 group by all order by casos desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2001-2003 | 302 | 30.- Cólera | 1.0.4 (2013) | A00 |
| 2004 | 302 | 13 Cólera | 1.0.4 (2013) | A00 |
| 2005-2008 | 302 | 11 Cólera | 1.0.4 (2013) | A00 |
| 2010-2013 | 302 | Cólera | 1.0.4 (2013) | A00 |
| 2016 | 302a | Cólera | 3.0.2 (2016) | A00 |
| 2018 | 302a | Cólera | 4.0.1 (2018) | A00 |
| 2019-2020 | 302a | Cólera | 5.0.1 (2020) | A00 |
| 2021 | 302a | Cólera | 6.0.0 (2021) | A00 |
| 2022-2023 | 302a | Cólera | 6.0.1 (2022) | A00 |
| 2024 | 302a | Cólera | 7.0.1 (2026) | A00 |
