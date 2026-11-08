# Diabetes tipo 2

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2018, 2020-2025. Fuente: SNIS, formularios 302b.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2018, 2020-2025 |
| Periodicidad | mensual |
| Municipios con registros | 341 |
| Desagregación | sexo, edad, nuevo o repetido |
| Filas | 257.419 |

Valores de `caso` (nuevo o repetido):

- nuevo (2015-2018, 2020-2025)
- repetido (2015-2018, 2020-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015-2018 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2020-2024 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2025 | 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2015 | 178.839 |
| 2016 | 255.705 |
| 2017 | 324.354 |
| 2018 | 402.038 |
| 2020 | 304.877 |
| 2021 | 449.005 |
| 2022 | 576.716 |
| 2023 | 709.612 |
| 2024 | 732.896 |
| 2025 | 774.528 |

## Cómo utilizar

Cada fila da el número de casos de un periodo, un municipio y una población. Para obtener un total, sume las filas: el dataset no tiene filas de total. Una combinación sin fila significa que no hubo registros. Las convenciones de tiempo, territorio y población están en el [catálogo](../../../README.md#cómo-leer-los-datos).

| Columna | Tipo | Descripción |
| --- | --- | --- |
| `gestion` | integer | Año calendario (gestión) del registro. |
| `mes` | integer | Mes, de 1 a 12. |
| `fecha_inicio` | date | Primer día de la semana o del mes. |
| `departamento` | string | Nombre del departamento. |
| `municipio` | string | Nombre del municipio. |
| `municipio_codigo` | string | Código del municipio, 6 dígitos: departamento (2), provincia (2) y municipio (2). |
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `caso` | string | nuevo, repetido, seguimiento o primera, como lo registra el formulario. |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/diabetes_tipo_2/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/diabetes_tipo_2/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/diabetes_tipo_2/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2015 | 302b | Diabetes Tipo 2 | 3.0.1 (2016) | E10 E11 E12 E13 E14 E15 |
| 2016 | 302b | Diabetes Tipo 2 | 3.0.2 (2016) | E10 E11 E12 E13 E14 E15 |
| 2017 | 302b | Diabetes Tipo 2 | 4.0.0 (2018) | E10 E11 E12 E13 E14 E15 |
| 2018 | 302b | Diabetes Tipo 2 | 4.0.1 (2018) | E10 E11 E12 E13 E14 E15 |
| 2020 | 302b | Diabetes Tipo 2 | 5.0.1 (2020) | E10 E11 E12 E13 E14 E15 |
| 2021 | 302b | Diabetes Tipo 2 | 6.0.0 (2021) | E10 E11 E12 E13 E14 E15 |
| 2022-2023 | 302b | Diabetes Tipo 2 | 6.0.1 (2022) | E10 E11 E12 E13 E14 E15 |
| 2024-2025 | 302b | Diabetes Tipo 2 | 7.0.1 (2026) | E11 E12 E13 E14 O24 |
