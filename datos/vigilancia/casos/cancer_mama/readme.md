# Cáncer de mama

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2018, 2020-2025. Fuente: SNIS, formularios 302b.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2018, 2020-2025 |
| Periodicidad | mensual |
| Municipios con registros | 180 |
| Desagregación | sexo, edad, nuevo o repetido |
| Filas | 9.696 |

Valores de `caso` (nuevo o repetido):

- nuevo (2015-2018, 2020-2025)
- repetido (2015-2018, 2020-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015-2018 | 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2020-2025 | 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2015 | 7.645 |
| 2016 | 6.122 |
| 2017 | 13.846 |
| 2018 | 17.634 |
| 2020 | 11.514 |
| 2021 | 20.228 |
| 2022 | 28.880 |
| 2023 | 37.434 |
| 2024 | 45.018 |
| 2025 | 51.949 |

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
from 'datos/vigilancia/casos/cancer_mama/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/cancer_mama/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/cancer_mama/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2015 | 302b | Cancer de mama | 3.0.1 (2016) | C50 |
| 2016 | 302b | Cancer de mama | 3.0.2 (2016) | C50 |
| 2017 | 302b | Cancer de mama | 4.0.0 (2018) | C50 |
| 2018 | 302b | Cancer de mama | 4.0.1 (2018) | C50 |
| 2020 | 302b | Cancer de mama | 5.0.1 (2020) | C50 |
| 2021 | 302b | Cancer de mama | 6.0.0 (2021) | C50 |
| 2022-2023 | 302b | Cancer de mama | 6.0.1 (2022) | C50 |
| 2024-2025 | 302b | Cáncer de Mama | 7.0.1 (2026) | C50 D05 |
