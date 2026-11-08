# Parotiditis

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2004-2025. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2004-2025 |
| Periodicidad | semanal |
| Municipios con registros | 333 |
| Desagregación | sexo, edad |
| Filas | 43.752 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2004-2007 | <1, 1-4, 5-14, 15-59, 60+ |
| 2008-2014 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |
| 2015-2025 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2004 | 2.384 |
| 2005 | 2.005 |
| 2006 | 4.373 |
| 2007 | 9.501 |
| 2008 | 10.873 |
| 2009 | 3.740 |
| 2010 | 1.781 |
| 2011 | 1.096 |
| 2012 | 855 |
| 2013 | 766 |
| 2014 | 832 |
| 2015 | 1.081 |
| 2016 | 1.268 |
| 2017 | 8.879 |
| 2018 | 12.853 |
| 2019 | 5.703 |
| 2020 | 1.344 |
| 2021 | 1.180 |
| 2022 | 1.210 |
| 2023 | 1.458 |
| 2024 | 1.652 |
| 2025 | 1.392 |

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
from 'datos/vigilancia/casos/parotiditis/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/parotiditis/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/parotiditis/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2004-2007 | 302 | 18 Parotiditis | 1.0.4 (2013) | B26 |
| 2008-2009 | 302 | 19 Parotiditis | 1.0.4 (2013) | B26 |
| 2010-2013 | 302 | Parotiditis | 1.0.4 (2013) | B26 |
| 2014 | 302 | Parotiditis | 2.0.0 (2014) | B26 |
| 2015 | 302a | Parotiditis | 3.0.1 (2016) | B26 |
| 2016 | 302a | Parotiditis | 3.0.2 (2016) | B26 |
| 2017 | 302a | Parotiditis | 4.0.0 (2018) | B26 |
| 2018 | 302a | Parotiditis | 4.0.1 (2018) | B26 |
| 2019-2020 | 302a | Parotiditis | 5.0.1 (2020) | B26 |
| 2021 | 302a | Parotiditis | 6.0.0 (2021) | B26 |
| 2022-2023 | 302a | Parotiditis | 6.0.1 (2022) | B26 |
| 2024-2025 | 302a | 6. Parotiditis | 7.0.1 (2026) | B26 |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302, 2001-2007: en las variables cuyas columnas "-M" siempre valen 0, "TOTAL-H" es igual a "TOTAL": "-H" contiene a ambos sexos. Esas variables no tienen sexo. En 2004 el grupo 09 (mortalidad) tampoco tiene sexo: hay 79 muertes maternas en "-H" y 94 en "-M".
