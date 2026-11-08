# Enfermedades transmitidas por alimentos

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2010-2025. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2010-2025 |
| Periodicidad | semanal |
| Municipios con registros | 301 |
| Desagregación | sexo, edad |
| Filas | 76.835 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2010-2014 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |
| 2016-2025 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2010 | 4.984 |
| 2011 | 6.612 |
| 2012 | 7.580 |
| 2013 | 6.830 |
| 2014 | 7.299 |
| 2015 | 8.686 |
| 2016 | 8.893 |
| 2017 | 9.128 |
| 2018 | 9.667 |
| 2019 | 11.015 |
| 2020 | 7.375 |
| 2021 | 8.794 |
| 2022 | 10.119 |
| 2023 | 11.888 |
| 2024 | 11.870 |
| 2025 | 10.725 |

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
from 'datos/vigilancia/casos/eta/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/eta/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/eta/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2010-2013 | 302 | Enf. Transmitidas por Alimentos (E.T.A.) | 1.0.4 (2013) | A05 |
| 2014 | 302 | Enf. Transmitidas por Alimentos (E.T.A.) | 2.0.0 (2014) | A05 |
| 2015 | 302a | Enf. Transmitidas por Alimentos (E.T.A.) | 3.0.1 (2016) | A05 |
| 2016 | 302a | Enf. Transmitidas por Alimentos (E.T.A.) | 3.0.2 (2016) | A05 |
| 2017 | 302a | Enf. Transmitidas por Alimentos (E.T.A.) | 4.0.0 (2018) | A05 |
| 2018 | 302a | Enf. Transmitidas por Alimentos (E.T.A.) | 4.0.1 (2018) | A05 |
| 2019-2020 | 302a | Enf. Transmitidas por Alimentos (E.T.A.) | 5.0.1 (2020) | A05 |
| 2021 | 302a | Enf. Transmitidas por Alimentos (E.T.A.) | 6.0.0 (2021) | A05 |
| 2022-2023 | 302a | Enf. Transmitidas por Alimentos (E.T.A.) | 6.0.1 (2022) | A05 |
| 2024-2025 | 302a | 5. Enf. Transmitidas por Alimentos (E.T.A.) | 7.0.1 (2026) | A02 A03 A04 A05 A32 T61 T62 T64 |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
