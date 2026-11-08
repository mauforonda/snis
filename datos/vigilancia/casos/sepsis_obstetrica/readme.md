# Sepsis obstétrica

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2015-2025. Fuente: SNIS, formularios 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2025 |
| Periodicidad | semanal |
| Municipios con registros | 188 |
| Desagregación | sexo, edad, lugar |
| Filas | 2.121 |

Valores de `lugar` (lugar):

- dentro (2024-2025)
- fuera (2024-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2024 | 10-14, 15-19, 20-39, 40-49, 50-59 |
| 2025 | 10-14, 15-19, 20-39, 40-49 |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2015 | 1.400 |
| 2016 | 966 |
| 2017 | 530 |
| 2018 | 384 |
| 2019 | 280 |
| 2020 | 261 |
| 2021 | 366 |
| 2022 | 430 |
| 2023 | 226 |
| 2024 | 199 |
| 2025 | 134 |

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
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/sepsis_obstetrica/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/sepsis_obstetrica/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/sepsis_obstetrica/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015 | 302a | Gestantes y puerperas con sepsis | 3.0.1 (2016) |
| 2016 | 302a | Gestantes y puerperas con sepsis | 3.0.2 (2016) |
| 2017 | 302a | Gestantes y puerperas con sepsis | 4.0.0 (2018) |
| 2018 | 302a | Gestantes y puerperas con sepsis | 4.0.1 (2018) |
| 2019-2020 | 302a | Gestantes y puerperas con sepsis | 5.0.1 (2020) |
| 2021 | 302a | Gestantes y puerperas con sepsis | 6.0.0 (2021) |
| 2022-2023 | 302a | Gestantes y puerperas con sepsis | 6.0.1 (2022) |
| 2024-2025 | 302a | 3. Sepsis obstetrica | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302a, grupo 10, 2024-2025: el segundo nivel dice FEMENINO/MASCULINO, pero SOAPS 7.0.1 divide por lugar. Las complicaciones atendidas dentro del establecimiento son muchas más que fuera (preeclampsia 2025: 2.513 frente a 137): MASCULINO es dentro y FEMENINO es fuera.
- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
