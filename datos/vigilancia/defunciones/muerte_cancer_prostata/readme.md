# Muerte por cáncer de próstata

Muertes por esta causa en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2018, 2020-2025. Fuente: SNIS, formularios 302b.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2018, 2020-2025 |
| Periodicidad | mensual |
| Municipios con registros | 115 |
| Desagregación | sexo, edad |
| Filas | 721 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015 | 15-19, 20-39, 40-49, 50-59, 60+ |
| 2016 | 20-39, 40-49, 50-59, 60+ |
| 2017 | 40-49, 50-59, 60+ |
| 2018 | 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2020 | 40-49, 50-59, 60+ |
| 2021 | 20-39, 50-59, 60+ |
| 2022 | 15-19, 40-49, 50-59, 60+ |
| 2023-2025 | 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Defunciones |
| ---: | ---: |
| 2015 | 81 |
| 2016 | 86 |
| 2017 | 100 |
| 2018 | 117 |
| 2020 | 62 |
| 2021 | 77 |
| 2022 | 201 |
| 2023 | 154 |
| 2024 | 94 |
| 2025 | 346 |

### Advertencias

- Registros implausibles: hay filas con una población que la definición excluye. Se publican tal como se registraron; pueden ser errores de registro o de codificación. Están en la tabla "Registros implausibles".

### Registros implausibles

| Sexo | Edad | Defunciones | % del total | Gestiones | Municipios |
| --- | --- | ---: | ---: | --- | ---: |
| mujer | 10-14 | 2 | 0,15% | 2018 | 2 |
| mujer | 15-19 | 1 | 0,08% | 2018 | 1 |
| mujer | 20-39 | 1 | 0,08% | 2021 | 1 |
| mujer | 50-59 | 11 | 0,83% | 2020-2021 | 3 |
| mujer | 60+ | 24 | 1,82% | 2020-2022 | 6 |

Para excluirlos:

```sql
select gestion, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_cancer_prostata/datos.parquet'
where not coalesce((sexo = 'mujer' and edad_grupo = '10-14')
    or (sexo = 'mujer' and edad_grupo = '15-19')
    or (sexo = 'mujer' and edad_grupo = '20-39')
    or (sexo = 'mujer' and edad_grupo = '50-59')
    or (sexo = 'mujer' and edad_grupo = '60+'), false)
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
from 'datos/vigilancia/defunciones/muerte_cancer_prostata/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_cancer_prostata/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_cancer_prostata/datos.parquet'
where gestion = 2025 group by all order by defunciones desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015 | 302b | Cancer de prostata | 3.0.1 (2016) |
| 2016 | 302b | Cancer de prostata | 3.0.2 (2016) |
| 2017 | 302b | Cancer de prostata | 4.0.0 (2018) |
| 2018 | 302b | Cancer de prostata | 4.0.1 (2018) |
| 2020 | 302b | Cancer de prostata | 5.0.1 (2020) |
| 2021 | 302b | Cancer de prostata | 6.0.0 (2021) |
| 2022-2023 | 302b | Cancer de prostata | 6.0.1 (2022) |
| 2024-2025 | 302b | Cancer de prostata | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302b, grupos 01, 05, 06, 07 y 10: el segundo nivel dice NUEVO/REPETIDO, pero las reglas de SOAPS dividen estas variables por sexo. Las muertes por cáncer de mama y de cuello uterino están en REPETIDO en todas las gestiones 2016-2025, y el tabaco y el alcohol (grupo 01, 2024-2025) están sobre todo en NUEVO: REPETIDO es mujer y NUEVO es hombre.
