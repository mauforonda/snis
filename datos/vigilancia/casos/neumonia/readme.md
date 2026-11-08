# Neumonía

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | semanal |
| Municipios con registros | 344 |
| Desagregación | sexo, edad |
| Filas | 980.030 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001-2007 | <1, 1-4, 5-14, 15-59, 60+ |
| 2008-2014 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |
| 2015-2025 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2001 | 153.608 |
| 2002 | 158.418 |
| 2003 | 183.057 |
| 2004 | 209.877 |
| 2005 | 200.476 |
| 2006 | 195.542 |
| 2007 | 194.613 |
| 2008 | 188.092 |
| 2009 | 194.329 |
| 2010 | 153.210 |
| 2011 | 137.006 |
| 2012 | 138.898 |
| 2013 | 151.110 |
| 2014 | 137.892 |
| 2015 | 127.665 |
| 2016 | 122.113 |
| 2017 | 117.006 |
| 2018 | 123.362 |
| 2019 | 115.910 |
| 2020 | 61.796 |
| 2021 | 99.556 |
| 2022 | 108.088 |
| 2023 | 145.664 |
| 2024 | 119.702 |
| 2025 | 132.370 |

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
from 'datos/vigilancia/casos/neumonia/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/neumonia/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/neumonia/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2001-2003 | 302 | 54.- Neumonia | 1.0.4 (2013) | J12 J13 J14 J15 J16 J17 J18 |
| 2004 | 302 | 28 Neumonía | 1.0.4 (2013) | J12 J13 J14 J15 J16 J17 J18 |
| 2005-2006 | 302 | 25 Neumonía | 1.0.4 (2013) | J12 J13 J14 J15 J16 J17 J18 |
| 2007 | 302 | 24 Neumonía | 1.0.4 (2013) | J12 J13 J14 J15 J16 J17 J18 |
| 2008-2009 | 302 | 25 Neumonía | 1.0.4 (2013) | J12 J13 J14 J15 J16 J17 J18 |
| 2010-2013 | 302 | Neumonía | 1.0.4 (2013) | J12 J13 J14 J15 J16 J17 J18 |
| 2014 | 302 | Neumonía | 2.0.0 (2014) | J12 J13 J14 J15 J16 J17 J18 |
| 2015 | 302a | Neumonía | 3.0.1 (2016) | J12 J13 J14 J15 J16 J17 J18 |
| 2016 | 302a | Neumonía | 3.0.2 (2016) | J12 J13 J14 J15 J16 J17 J18 |
| 2017 | 302a | Neumonía | 4.0.0 (2018) | J12 J13 J14 J15 J16 J17 J18 |
| 2018 | 302a | Neumonía | 4.0.1 (2018) | J12 J13 J14 J15 J16 J17 J18 |
| 2019-2020 | 302a | Neumonía | 5.0.1 (2020) | J12 J13 J14 J15 J16 J17 J18 |
| 2021 | 302a | Neumonía | 6.0.0 (2021) | J12 J13 J14 J15 J16 J17 J18 |
| 2022-2023 | 302a | Neumonía | 6.0.1 (2022) | J12 J13 J14 J15 J16 J17 J18 |
| 2024-2025 | 302a | 3. Neumonía | 7.0.1 (2026) | J12 J13 J14 J15 J16 J17 J18 |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302, 2001-2007: en las variables cuyas columnas "-M" siempre valen 0, "TOTAL-H" es igual a "TOTAL": "-H" contiene a ambos sexos. Esas variables no tienen sexo. En 2004 el grupo 09 (mortalidad) tampoco tiene sexo: hay 79 muertes maternas en "-H" y 94 en "-M".
