# Muerte por cáncer de cuello uterino

Muertes por esta causa en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2018, 2020-2025. Fuente: SNIS, formularios 302b.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2018, 2020-2025 |
| Periodicidad | mensual |
| Municipios con registros | 212 |
| Desagregación | sexo, edad |
| Filas | 2.367 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015 | 20-39, 40-49, 50-59, 60+ |
| 2016 | 15-19, 20-39, 40-49, 50-59, 60+ |
| 2017-2018 | 20-39, 40-49, 50-59, 60+ |
| 2020 | 15-19, 20-39, 40-49, 50-59, 60+ |
| 2021 | 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2022-2023 | 15-19, 20-39, 40-49, 50-59, 60+ |
| 2024 | 20-39, 40-49, 50-59, 60+ |
| 2025 | 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Defunciones |
| ---: | ---: |
| 2015 | 220 |
| 2016 | 278 |
| 2017 | 276 |
| 2018 | 336 |
| 2020 | 309 |
| 2021 | 436 |
| 2022 | 637 |
| 2023 | 452 |
| 2024 | 213 |
| 2025 | 632 |

### Advertencias

- Registros implausibles: hay filas con una población que la definición excluye. Se publican tal como se registraron; pueden ser errores de registro o de codificación. Están en la tabla "Registros implausibles".

### Registros implausibles

| Sexo | Edad | Defunciones | % del total | Gestiones | Municipios |
| --- | --- | ---: | ---: | --- | ---: |
| hombre | 40-49 | 2 | 0,05% | 2021-2022 | 2 |
| hombre | 50-59 | 2 | 0,05% | 2020 | 2 |
| hombre | 60+ | 6 | 0,16% | 2015-2017, 2020-2021 | 4 |

Para excluirlos:

```sql
select gestion, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_cancer_cuello_uterino/datos.parquet'
where not coalesce((sexo = 'hombre' and edad_grupo = '40-49')
    or (sexo = 'hombre' and edad_grupo = '50-59')
    or (sexo = 'hombre' and edad_grupo = '60+'), false)
group by gestion order by gestion;
```

## Cómo utilizar

Cada fila da el número de defunciones de un periodo, un municipio y una población. Para obtener un total, sume las filas: el dataset no tiene filas de total. Una combinación sin fila significa que no hubo registros. Las convenciones de tiempo, territorio y población están en el [catálogo](../../../README.md#cómo-leer-los-datos).

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
| `defunciones` | integer | Número de defunciones en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_cancer_cuello_uterino/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_cancer_cuello_uterino/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_cancer_cuello_uterino/datos.parquet'
where gestion = 2025 group by all order by defunciones desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015 | 302b | ancer de cervico uterino | 3.0.1 (2016) |
| 2016 | 302b | ancer de cervico uterino | 3.0.2 (2016) |
| 2017 | 302b | ancer de cervico uterino | 4.0.0 (2018) |
| 2018 | 302b | ancer de cervico uterino | 4.0.1 (2018) |
| 2020 | 302b | ancer de cervico uterino | 5.0.1 (2020) |
| 2021 | 302b | ancer de cervico uterino | 6.0.0 (2021) |
| 2022-2023 | 302b | ancer de cervico uterino | 6.0.1 (2022) |
| 2024-2025 | 302b | Cancer de cervico uterino | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302b, grupos 01, 05, 06, 07 y 10: el segundo nivel dice NUEVO/REPETIDO, pero las reglas de SOAPS dividen estas variables por sexo. Las muertes por cáncer de mama y de cuello uterino están en REPETIDO en todas las gestiones 2016-2025, y el tabaco y el alcohol (grupo 01, 2024-2025) están sobre todo en NUEVO: REPETIDO es mujer y NUEVO es hombre.
