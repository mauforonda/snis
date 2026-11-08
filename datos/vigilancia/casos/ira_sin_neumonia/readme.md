# Infección respiratoria aguda sin neumonía

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2004-2025. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2004-2025 |
| Periodicidad | semanal |
| Municipios con registros | 344 |
| Desagregación | sexo, edad |
| Filas | 4.675.482 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2004-2007 | <1, 1-4, 5-14, 15-59, 60+ |
| 2008-2014 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |
| 2015-2025 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2004 | 2.063.789 |
| 2005 | 2.219.463 |
| 2006 | 2.393.448 |
| 2007 | 2.615.960 |
| 2008 | 2.717.382 |
| 2009 | 3.141.499 |
| 2010 | 3.181.723 |
| 2011 | 3.232.775 |
| 2012 | 3.417.120 |
| 2013 | 3.654.049 |
| 2014 | 3.769.955 |
| 2015 | 3.923.885 |
| 2016 | 4.139.378 |
| 2017 | 4.075.321 |
| 2018 | 4.241.647 |
| 2019 | 4.051.999 |
| 2020 | 2.262.189 |
| 2021 | 2.689.624 |
| 2022 | 4.091.458 |
| 2023 | 4.830.981 |
| 2024 | 4.635.592 |
| 2025 | 4.789.903 |

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
from 'datos/vigilancia/casos/ira_sin_neumonia/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/ira_sin_neumonia/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/ira_sin_neumonia/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2004 | 302 | 27 IRA sin neumonía | 1.0.4 (2013) | J00 J01 J02 J03 J04 J05 J06 J10 J11 J20 |
| 2005-2006 | 302 | 24 IRA sin neumonía | 1.0.4 (2013) | J00 J01 J02 J03 J04 J05 J06 J10 J11 J20 |
| 2007 | 302 | 23 IRA sin neumonía | 1.0.4 (2013) | J00 J01 J02 J03 J04 J05 J06 J10 J11 J20 |
| 2008-2009 | 302 | 24 IRA sin neumonía | 1.0.4 (2013) | J00 J01 J02 J03 J04 J05 J06 J10 J11 J20 |
| 2010-2013 | 302 | IRA sin neumonía | 1.0.4 (2013) | J00 J01 J02 J03 J04 J05 J06 J10 J11 J20 |
| 2014 | 302 | IRA sin neumonía | 2.0.0 (2014) | J00 J01 J02 J03 J04 J05 J06 J10 J11 J20 |
| 2015 | 302a | IRA sin neumonía | 3.0.1 (2016) | J00 J01 J02 J03 J04 J05 J06 J20 |
| 2016 | 302a | IRA sin neumonía | 3.0.2 (2016) | J00 J01 J02 J03 J04 J05 J06 J20 |
| 2017 | 302a | IRA sin neumonía | 4.0.0 (2018) | H67 J00 J01 J02 J03 J04 J05 J06 J20 |
| 2018 | 302a | IRA sin neumonía | 4.0.1 (2018) | H67 J00 J01 J02 J03 J04 J05 J06 J20 |
| 2019-2020 | 302a | IRA sin neumonía | 5.0.1 (2020) | H67 J00 J01 J02 J03 J04 J05 J06 J20 |
| 2021 | 302a | IRA sin neumonía | 6.0.0 (2021) | H67 J00 J01 J02 J03 J04 J05 J06 J20 |
| 2022-2023 | 302a | IRA sin neumonía | 6.0.1 (2022) | H67 J00 J01 J02 J03 J04 J05 J06 J20 |
| 2024-2025 | 302a | 2. IRA sin neumonía | 7.0.1 (2026) | H67 J00 J01 J02 J03 J04 J05 J06 J20 |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302, 2001-2007: en las variables cuyas columnas "-M" siempre valen 0, "TOTAL-H" es igual a "TOTAL": "-H" contiene a ambos sexos. Esas variables no tienen sexo. En 2004 el grupo 09 (mortalidad) tampoco tiene sexo: hay 79 muertes maternas en "-H" y 94 en "-M".
