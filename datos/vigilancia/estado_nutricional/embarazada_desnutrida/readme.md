# Embarazada desnutrida

Personas evaluadas, por resultado en los establecimientos de salud de Bolivia, por semana o mes y municipio, en las gestiones 2007-2018, 2020-2025. Fuente: SNIS, formularios 302, 302b.

## Qué es

| | |
| --- | --- |
| Gestiones | 2007-2018, 2020-2025 |
| Periodicidad | semanal y mensual |
| Municipios con registros | 340 |
| Desagregación | sexo, edad, embarazo o puerperio |
| Filas | 54.264 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015-2018 | 10-19, 20-59 |
| 2020-2025 | 10-19, 20-59 |

Total por gestión:

| Gestión | Personas |
| ---: | ---: |
| 2007 | 3.317 |
| 2008 | 6.783 |
| 2009 | 9.534 |
| 2010 | 11.434 |
| 2011 | 11.746 |
| 2012 | 10.449 |
| 2013 | 11.420 |
| 2014 | 12.377 |
| 2015 | 19.762 |
| 2016 | 20.069 |
| 2017 | 19.003 |
| 2018 | 20.264 |
| 2020 | 15.184 |
| 2021 | 17.114 |
| 2022 | 16.748 |
| 2023 | 16.350 |
| 2024 | 14.862 |
| 2025 | 14.330 |

## Cómo utilizar

Cada fila da el número de personas de un periodo, un municipio y una población. Para obtener un total, sume las filas: el dataset no tiene filas de total. Una combinación sin fila significa que no hubo registros. Las convenciones de tiempo, territorio y población están en el [catálogo](../../../README.md#cómo-leer-los-datos).

| Columna | Tipo | Descripción |
| --- | --- | --- |
| `gestion` | integer | Año calendario (gestión) del registro. |
| `semana` | integer | Semana epidemiológica, de 1 a 53. Va de domingo a sábado. |
| `mes` | integer | Mes, de 1 a 12. |
| `fecha_inicio` | date | Primer día de la semana o del mes. |
| `departamento` | string | Nombre del departamento. |
| `municipio` | string | Nombre del municipio. |
| `municipio_codigo` | string | Código del municipio, 6 dígitos: departamento (2), provincia (2) y municipio (2). |
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `condicion` | string | embarazada o puerpera. |
| `personas` | integer | Número de personas en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(personas) as personas
from 'datos/vigilancia/estado_nutricional/embarazada_desnutrida/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(personas) as personas
from 'datos/vigilancia/estado_nutricional/embarazada_desnutrida/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(personas) as personas
from 'datos/vigilancia/estado_nutricional/embarazada_desnutrida/datos.parquet'
where gestion = 2025 group by all order by personas desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2007 | 302 | 48 Nro. de embarazadas enflaquecidas (desnutridas) |  |
| 2008-2009 | 302 | 53 Desnutrida |  |
| 2010-2013 | 302 | Embarazada Desnutrida | 1.0.4 (2013) |
| 2014 | 302 | Embarazada Desnutrida | 2.0.0 (2014) |
| 2015 | 302b | Embarazada Desnutrida | 3.0.1 (2016) |
| 2016 | 302b | Embarazada Desnutrida | 3.0.2 (2016) |
| 2017 | 302b | Embarazada Desnutrida | 4.0.0 (2018) |
| 2018 | 302b | Embarazada Desnutrida | 4.0.1 (2018) |
| 2020 | 302b | Embarazada Desnutrida | 5.0.1 (2020) |
| 2021 | 302b | Embarazada Desnutrida | 6.0.0 (2021) |
| 2022-2023 | 302b | Embarazada Desnutrida | 6.0.1 (2022) |
| 2024-2025 | 302b | Embarazada Desnutrida | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302b, grupo 06: la columna Embarazada se divide en 10-19 y 20-59 años (reglas de SOAPS para el código 3050604). La columna menor es 10-19: NUEVO o MASCULINO es 10-19; REPETIDO o FEMENINO es 20-59.
