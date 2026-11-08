# Leishmaniasis (2001-2023)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2023. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2023 |
| Periodicidad | semanal |
| Municipios con registros | 274 |
| Desagregación | sexo, edad |
| Filas | 43.579 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001-2007 | <1, 1-4, 5-14, 15-59, 60+ |
| 2008-2014 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |
| 2015-2023 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2001 | 2.043 |
| 2002 | 2.518 |
| 2003 | 2.452 |
| 2004 | 2.819 |
| 2005 | 2.657 |
| 2006 | 3.152 |
| 2007 | 3.182 |
| 2008 | 2.907 |
| 2009 | 2.447 |
| 2010 | 1.748 |
| 2011 | 1.422 |
| 2012 | 2.179 |
| 2013 | 2.130 |
| 2014 | 1.387 |
| 2015 | 3.893 |
| 2016 | 3.642 |
| 2017 | 4.386 |
| 2018 | 4.963 |
| 2019 | 3.360 |
| 2020 | 2.649 |
| 2021 | 2.813 |
| 2022 | 2.984 |
| 2023 | 2.900 |

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
from 'datos/vigilancia/casos/leishmaniasis_2001_2023/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/leishmaniasis_2001_2023/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/leishmaniasis_2001_2023/datos.parquet'
where gestion = 2023 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Leishmaniasis (2001-2023) (este dataset): 2001-2023, formulario 302, 302a.
- [Leishmaniasis (2024-2025)](../../../vigilancia/casos/leishmaniasis_2024_2025/readme.md): 2024-2025, formulario 302a.

Las categorías de `forma_clinica` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/leishmaniasis_2001_2023/datos.parquet',
    'datos/vigilancia/casos/leishmaniasis_2024_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2001-2003 | 302 | 92.- Leishmaniasis |  |  |
| 2004 | 302 | 24 Leishmaniasis |  |  |
| 2005-2006 | 302 | 27 Leishmaniasis | 1.0.4 (2013) |  |
| 2007 | 302 | 26 Leishmaniasis | 1.0.4 (2013) |  |
| 2008-2009 | 302 | 27 Leishmaniasis | 1.0.4 (2013) |  |
| 2010-2013 | 302 | Leishmaniasis Confirmados | 1.0.4 (2013) | B55 |
| 2014 | 302 | Leishmaniasis Confirmados | 2.0.0 (2014) | B55 |
| 2015 | 302a | Leishmaniasis | 3.0.1 (2016) | B55 |
| 2016 | 302a | Leishmaniasis | 3.0.2 (2016) | B55 |
| 2017 | 302a | Leishmaniasis | 4.0.0 (2018) | B55 |
| 2018 | 302a | Leishmaniasis | 4.0.1 (2018) | B55 |
| 2019-2020 | 302a | Leishmaniasis | 5.0.1 (2020) | B55 |
| 2021 | 302a | Leishmaniasis | 6.0.0 (2021) | B55 |
| 2022-2023 | 302a | Leishmaniasis | 6.0.1 (2022) | B55 |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302, 2001-2007: en las variables cuyas columnas "-M" siempre valen 0, "TOTAL-H" es igual a "TOTAL": "-H" contiene a ambos sexos. Esas variables no tienen sexo. En 2004 el grupo 09 (mortalidad) tampoco tiene sexo: hay 79 muertes maternas en "-H" y 94 en "-M".
