# Mordedura o envenenamiento por serpiente

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2010-2025. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2010-2025 |
| Periodicidad | semanal |
| Municipios con registros | 242 |
| Desagregación | sexo, edad |
| Filas | 17.106 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2010-2012 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |
| 2013 | 1-4, 5-9, 10-20, 21-59, 60+ |
| 2014 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |
| 2015-2016 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2017 | <6m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2018-2025 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2010 | 700 |
| 2011 | 846 |
| 2012 | 704 |
| 2013 | 760 |
| 2014 | 1.032 |
| 2015 | 1.427 |
| 2016 | 1.068 |
| 2017 | 1.178 |
| 2018 | 1.344 |
| 2019 | 1.525 |
| 2020 | 1.632 |
| 2021 | 1.360 |
| 2022 | 1.513 |
| 2023 | 1.754 |
| 2024 | 1.914 |
| 2025 | 1.959 |

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
from 'datos/vigilancia/casos/mordedura_serpiente/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/mordedura_serpiente/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/mordedura_serpiente/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2010-2013 | 302 | Mordedura de serpiente | 1.0.4 (2013) | T63 |
| 2014 | 302 | Mordedura de serpiente | 2.0.0 (2014) | T63 W59 |
| 2015 | 302a | N° de personas con Mordedura de Serpientes | 3.0.1 (2016) | T63 |
| 2016 | 302a | N° de personas con Mordedura de Serpientes | 3.0.2 (2016) | T63 |
| 2017 | 302a | N° de personas con Mordedura de Serpientes | 4.0.0 (2018) | T63 |
| 2018 | 302a | N° de personas con Mordedura de Serpientes | 4.0.1 (2018) | T63 |
| 2019 | 302a | N° de personas con Mordedura de Serpientes | 5.0.1 (2020) | T63 |
| 2020 | 302a | N° de personas con evenenamiento por mordedura de serpientes venenosas | 5.0.1 (2020) | T63 |
| 2021 | 302a | N° de personas con evenenamiento por mordedura de serpientes venenosas | 6.0.0 (2021) | T63 |
| 2022-2023 | 302a | N° de personas con evenenamiento por mordedura de serpientes venenosas | 6.0.1 (2022) | T63 |
| 2024-2025 | 302a | 5. N° de personas con envenenamiento por mordedura de serpientes venenosas | 7.0.1 (2026) | T63 |
