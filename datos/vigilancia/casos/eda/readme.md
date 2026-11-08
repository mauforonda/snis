# Enfermedad diarreica aguda

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | semanal |
| Municipios con registros | 344 |
| Desagregación | sexo, edad |
| Filas | 2.813.590 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001-2007 | <1, 1-4, 5-14, 15-59, 60+ |
| 2008-2014 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |
| 2015-2025 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2001 | 541.669 |
| 2002 | 611.980 |
| 2003 | 701.182 |
| 2004 | 755.390 |
| 2005 | 772.282 |
| 2006 | 825.341 |
| 2007 | 838.849 |
| 2008 | 880.786 |
| 2009 | 865.477 |
| 2010 | 834.008 |
| 2011 | 836.601 |
| 2012 | 871.688 |
| 2013 | 887.533 |
| 2014 | 940.670 |
| 2015 | 939.807 |
| 2016 | 894.929 |
| 2017 | 831.768 |
| 2018 | 813.010 |
| 2019 | 729.154 |
| 2020 | 509.176 |
| 2021 | 605.392 |
| 2022 | 612.070 |
| 2023 | 878.364 |
| 2024 | 897.591 |
| 2025 | 827.269 |

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
from 'datos/vigilancia/casos/eda/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/eda/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/eda/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2001-2003 | 302 | 53.- Diarrea |  |  |
| 2004 | 302 | 26 Enfermedad diarreica Aguda | 1.0.4 (2013) | A09 K59 P78 |
| 2005-2006 | 302 | 23 Enfermedad diarreica aguda | 1.0.4 (2013) | A09 K59 P78 |
| 2007 | 302 | 22 Enfermedad diarreica aguda | 1.0.4 (2013) | A09 K59 P78 |
| 2008-2009 | 302 | 23 Enfermedad diarreica aguda | 1.0.4 (2013) | A09 K59 P78 |
| 2010-2013 | 302 | Enfermedad diarreica aguda | 1.0.4 (2013) | A09 K59 P78 |
| 2014 | 302 | Enfermedad diarreica aguda | 2.0.0 (2014) | A09 K59 P78 |
| 2015 | 302a | Enfermedad Diarreica Aguda | 3.0.1 (2016) | A09 K59 P78 |
| 2016 | 302a | Enfermedad Diarreica Aguda | 3.0.2 (2016) | A09 K59 P78 |
| 2017 | 302a | Enfermedad Diarreica Aguda | 4.0.0 (2018) | A09 K59 P78 |
| 2018 | 302a | Enfermedad Diarreica Aguda | 4.0.1 (2018) | A09 K59 P78 |
| 2019-2020 | 302a | Enfermedad Diarreica Aguda | 5.0.1 (2020) | A09 K59 P78 |
| 2021 | 302a | Enfermedad Diarreica Aguda | 6.0.0 (2021) | A09 K59 P78 |
| 2022-2023 | 302a | Enfermedad Diarreica Aguda | 6.0.1 (2022) | A09 K59 P78 |
| 2024-2025 | 302a | 1. Enfermedad Diarreica Aguda | 7.0.1 (2026) | A09 K59 P78 |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302, 2001-2007: en las variables cuyas columnas "-M" siempre valen 0, "TOTAL-H" es igual a "TOTAL": "-H" contiene a ambos sexos. Esas variables no tienen sexo. En 2004 el grupo 09 (mortalidad) tampoco tiene sexo: hay 79 muertes maternas en "-H" y 94 en "-M".
