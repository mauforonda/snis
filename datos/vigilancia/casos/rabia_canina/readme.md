# Rabia canina (casos en perros)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2004, 2010-2025. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2004, 2010-2025 |
| Periodicidad | semanal |
| Municipios con registros | 162 |
| Desagregación | sexo, edad |
| Filas | 4.601 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001-2003 | <1 |
| 2010-2014 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |
| 2015 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59 |
| 2016 | <6m, 6-11m, 1-4, 5-9, 10-14, 20-39, 40-49, 60+ |
| 2017 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 60+ |
| 2018 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59 |
| 2019-2025 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2001 | 116 |
| 2002 | 53 |
| 2003 | 52 |
| 2004 | 385 |
| 2010 | 173 |
| 2011 | 395 |
| 2012 | 325 |
| 2013 | 407 |
| 2014 | 495 |
| 2015 | 532 |
| 2016 | 389 |
| 2017 | 882 |
| 2018 | 743 |
| 2019 | 182 |
| 2020 | 110 |
| 2021 | 104 |
| 2022 | 259 |
| 2023 | 458 |
| 2024 | 375 |
| 2025 | 374 |

### Advertencias

- Cuenta perros, no personas. El formulario usa para los perros la misma plantilla de sexo y bandas de edad que para las personas; las bandas de 20 años o más no son posibles en perros.

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
from 'datos/vigilancia/casos/rabia_canina/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/rabia_canina/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/rabia_canina/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2003 | 302 | 42.- Rabia canina |  |
| 2004 | 302 | 1.15 Rabia en canes |  |
| 2010-2013 | 302 | Rabia canina | 1.0.4 (2013) |
| 2014 | 302 | Rabia canina | 2.0.0 (2014) |
| 2015 | 302a | Rabia en perros | 3.0.1 (2016) |
| 2016 | 302a | Rabia en perros | 3.0.2 (2016) |
| 2017 | 302a | Rabia en perros | 4.0.0 (2018) |
| 2018 | 302a | Rabia en perros | 4.0.1 (2018) |
| 2019 | 302a | Rabia en perros | 5.0.1 (2020) |
| 2020-2023 | 302a | Rabia canina | 7.0.1 (2026) |
| 2024 | 302a | Rabia Canina | 7.0.1 (2026) |
| 2025 | 302a | 13. Rabia Canina | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302, 2001-2007: en las variables cuyas columnas "-M" siempre valen 0, "TOTAL-H" es igual a "TOTAL": "-H" contiene a ambos sexos. Esas variables no tienen sexo. En 2004 el grupo 09 (mortalidad) tampoco tiene sexo: hay 79 muertes maternas en "-H" y 94 en "-M".
