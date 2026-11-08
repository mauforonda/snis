# Rabia humana

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2005-2015, 2017-2025. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2005-2015, 2017-2025 |
| Periodicidad | semanal |
| Municipios con registros | 49 |
| Desagregación | sexo, edad |
| Filas | 177 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2005-2006 | 1-4, 5-14, 15-59, 60+ |
| 2007 | <1, 1-4, 5-14, 15-59, 60+ |
| 2008 | 1-4, 5-9, 10-20, 21-59, 60+ |
| 2009 | 1-4, 5-9, 10-20, 21-59 |
| 2010 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |
| 2011 | 1-4, 5-9, 21-59, 60+ |
| 2012 | <1, 10-20, 21-59 |
| 2013 | 1-4, 5-9 |
| 2014 | 1-4, 5-9, 10-20, 21-59 |
| 2015 | 1-4, 5-9, 10-14, 15-19, 20-39, 50-59 |
| 2017 | 1-4, 5-9, 10-14, 15-19, 20-39, 40-49 |
| 2018 | 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59 |
| 2019 | 50-59, 60+ |
| 2020 | 1-4 |
| 2021 | 1-4, 5-9, 20-39 |
| 2022 | 5-9, 20-39, 50-59 |
| 2023 | 1-4, 15-19 |
| 2024 | 1-4, 5-9, 10-14, 15-19, 20-39, 50-59 |
| 2025 | 5-9, 15-19, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2005 | 19 |
| 2006 | 13 |
| 2007 | 32 |
| 2008 | 13 |
| 2009 | 8 |
| 2010 | 20 |
| 2011 | 7 |
| 2012 | 4 |
| 2013 | 2 |
| 2014 | 4 |
| 2015 | 12 |
| 2017 | 11 |
| 2018 | 9 |
| 2019 | 3 |
| 2020 | 1 |
| 2021 | 7 |
| 2022 | 4 |
| 2023 | 2 |
| 2024 | 8 |
| 2025 | 5 |

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
from 'datos/vigilancia/casos/rabia_humana/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/rabia_humana/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/rabia_humana/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2005-2009 | 302 | 13 Rabia Humana | 1.0.4 (2013) | A82 |
| 2010-2013 | 302 | Rabia Humana | 1.0.4 (2013) | A82 |
| 2014 | 302 | Rabia Humana | 2.0.0 (2014) | A82 |
| 2015 | 302a | Rabia humana | 3.0.1 (2016) | A82 |
| 2017 | 302a | Rabia humana | 4.0.0 (2018) | A82 |
| 2018 | 302a | Rabia humana | 4.0.1 (2018) | A82 |
| 2019-2020 | 302a | Rabia humana | 5.0.1 (2020) | A82 |
| 2021 | 302a | Rabia humana | 6.0.0 (2021) | A82 |
| 2022-2023 | 302a | Rabia humana | 6.0.1 (2022) | A82 |
| 2024 | 302a | Rabia Humana | 7.0.1 (2026) | A82 |
| 2025 | 302a | 14. Rabia Humana | 7.0.1 (2026) | A82 |
