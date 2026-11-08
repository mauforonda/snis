# Abuso de alcohol

Personas con este factor de riesgo en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2018, 2020-2025. Fuente: SNIS, formularios 302b.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2018, 2020-2025 |
| Periodicidad | mensual |
| Municipios con registros | 251 |
| Desagregación | sexo, edad |
| Filas | 8.003 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015-2018 | 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2020-2024 | 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2025 | 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Personas |
| ---: | ---: |
| 2015 | 4.995 |
| 2016 | 4.177 |
| 2017 | 5.815 |
| 2018 | 10.532 |
| 2020 | 3.511 |
| 2021 | 6.912 |
| 2022 | 6.138 |
| 2023 | 5.898 |
| 2024 | 7.954 |
| 2025 | 7.115 |

## Cómo utilizar

Cada fila da el número de personas de un periodo, un municipio y una población. Para obtener un total, sume las filas: el dataset no tiene filas de total. Una combinación sin fila significa que no hubo registros. Las convenciones de tiempo, territorio y población están en el [catálogo](../../../README.md#cómo-leer-los-datos).

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
| `personas` | integer | Número de personas en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(personas) as personas
from 'datos/vigilancia/factores_riesgo/abuso_alcohol/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(personas) as personas
from 'datos/vigilancia/factores_riesgo/abuso_alcohol/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(personas) as personas
from 'datos/vigilancia/factores_riesgo/abuso_alcohol/datos.parquet'
where gestion = 2025 group by all order by personas desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2015 | 302b | Abuso de Alcohol | 3.0.1 (2016) | Z72 |
| 2016 | 302b | Abuso de Alcohol | 3.0.2 (2016) | Z72 |
| 2017 | 302b | Abuso de Alcohol | 4.0.0 (2018) | Z72 |
| 2018 | 302b | Abuso de Alcohol | 4.0.1 (2018) | Z72 |
| 2020 | 302b | Abuso de Alcohol | 5.0.1 (2020) | Z72 |
| 2021 | 302b | Abuso de Alcohol | 6.0.0 (2021) | Z72 |
| 2022-2023 | 302b | Abuso de Alcohol | 6.0.1 (2022) | Z72 |
| 2024-2025 | 302b | Abuso de Alcohol | 7.0.1 (2026) | R78 Y15 Y90 Y91 Z71 Z72 |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302b, grupos 01, 05, 06, 07 y 10: el segundo nivel dice NUEVO/REPETIDO, pero las reglas de SOAPS dividen estas variables por sexo. Las muertes por cáncer de mama y de cuello uterino están en REPETIDO en todas las gestiones 2016-2025, y el tabaco y el alcohol (grupo 01, 2024-2025) están sobre todo en NUEVO: REPETIDO es mujer y NUEVO es hombre.
