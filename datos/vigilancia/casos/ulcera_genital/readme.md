# Úlcera genital

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | semanal |
| Municipios con registros | 339 |
| Desagregación | sexo, edad |
| Filas | 54.411 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001-2004 | <1, 1-4, 5-14, 15-59, 60+ |
| 2005-2007 | 5-14, 15-59, 60+ |
| 2008-2009 | 5-9, 10-20, 21-59, 60+ |
| 2010-2014 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |
| 2015-2025 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2001 | 5.585 |
| 2002 | 9.528 |
| 2003 | 12.023 |
| 2004 | 10.694 |
| 2005 | 9.156 |
| 2006 | 7.504 |
| 2007 | 4.568 |
| 2008 | 4.783 |
| 2009 | 4.468 |
| 2010 | 3.617 |
| 2011 | 3.852 |
| 2012 | 4.060 |
| 2013 | 4.718 |
| 2014 | 4.708 |
| 2015 | 4.562 |
| 2016 | 4.594 |
| 2017 | 4.853 |
| 2018 | 4.041 |
| 2019 | 4.172 |
| 2020 | 2.900 |
| 2021 | 3.901 |
| 2022 | 4.290 |
| 2023 | 4.061 |
| 2024 | 4.657 |
| 2025 | 4.493 |

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
from 'datos/vigilancia/casos/ulcera_genital/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/ulcera_genital/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/ulcera_genital/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2001-2003 | 302 | 47.- ITS Mujer con úlcera genital; 48.- ITS Hombre con úlcera genital | 1.0.4 (2013) | A51 A60 N48 N76 |
| 2004-2006 | 302 | 19 Mujer con úlcera genital; 20 Hombre con úlcera genital | 1.0.4 (2013) | A51 A60 N48 N76 |
| 2007 | 302 | 19 Ulcera genital | 1.0.4 (2013) | A51 A60 N48 N76 |
| 2008-2009 | 302 | 20 Ulcera genital | 1.0.4 (2013) | A51 A60 N48 N76 |
| 2010-2013 | 302 | Ulcera genital | 1.0.4 (2013) | A51 A60 N48 N76 |
| 2014 | 302 | Ulcera genital | 2.0.0 (2014) | A51 A60 N48 N76 |
| 2015 | 302a | Úlcera genital | 3.0.1 (2016) | A51 A57 A60 N48 N76 |
| 2016 | 302a | Úlcera genital | 3.0.2 (2016) | A51 A57 A60 N48 N76 |
| 2017 | 302a | Úlcera genital | 4.0.0 (2018) | A51 A57 A60 N48 N76 |
| 2018 | 302a | Úlcera genital | 4.0.1 (2018) | A51 A57 A60 N48 N76 |
| 2019-2020 | 302a | Úlcera genital | 5.0.1 (2020) | A51 A57 A60 N48 N76 |
| 2021 | 302a | Úlcera genital | 6.0.0 (2021) | A51 A57 A60 N48 N76 |
| 2022-2023 | 302a | Úlcera genital | 6.0.1 (2022) | A51 A57 A60 N48 N76 |
| 2024-2025 | 302a | 1. Úlcera genital | 7.0.1 (2026) | A51 A57 A60 N48 N76 |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302, 2001-2007: en las variables cuyas columnas "-M" siempre valen 0, "TOTAL-H" es igual a "TOTAL": "-H" contiene a ambos sexos. Esas variables no tienen sexo. En 2004 el grupo 09 (mortalidad) tampoco tiene sexo: hay 79 muertes maternas en "-H" y 94 en "-M".
