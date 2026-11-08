# Intoxicación por plaguicidas (2004-2020)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2004-2020. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2004-2020 |
| Periodicidad | semanal |
| Municipios con registros | 297 |
| Desagregación | agente, sexo, edad |
| Filas | 17.974 |

Valores de `agente` (agente):

- no especificado (2004-2020)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2008-2014 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |
| 2016-2020 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2004 | 2.170 |
| 2005 | 2.077 |
| 2006 | 1.540 |
| 2007 | 1.532 |
| 2008 | 1.803 |
| 2009 | 1.999 |
| 2010 | 2.080 |
| 2011 | 1.947 |
| 2012 | 1.648 |
| 2013 | 1.549 |
| 2014 | 1.349 |
| 2015 | 1.144 |
| 2016 | 1.066 |
| 2017 | 976 |
| 2018 | 1.084 |
| 2019 | 1.222 |
| 2020 | 1.148 |

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
| `agente` | string | Agente de la intoxicación. |
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/intoxicacion_plaguicidas_2004_2020/datos.parquet'
group by gestion order by gestion;

-- Por gestión y agente
select gestion, agente, sum(casos) as casos
from 'datos/vigilancia/casos/intoxicacion_plaguicidas_2004_2020/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/intoxicacion_plaguicidas_2004_2020/datos.parquet'
where gestion = 2020 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Intoxicación por organofosforados y carbamatos (2001-2003)](../../../vigilancia/casos/intoxicacion_plaguicidas_2001_2003/readme.md): 2001-2003, formulario 302.
- Intoxicación por plaguicidas (2004-2020) (este dataset): 2004-2020, formulario 302, 302a.
- [Intoxicación por plaguicidas (2021-2025)](../../../vigilancia/casos/intoxicacion_plaguicidas_2021_2025/readme.md): 2021-2025, formulario 302a.

Las categorías de `agente` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/intoxicacion_plaguicidas_2001_2003/datos.parquet',
    'datos/vigilancia/casos/intoxicacion_plaguicidas_2004_2020/datos.parquet',
    'datos/vigilancia/casos/intoxicacion_plaguicidas_2021_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2004 | 302 | 53 Plaguicidas |  |  |
| 2005-2006 | 302 | 11.1 Plaguicidas |  |  |
| 2007 | 302 | 56 Plaguicidas |  |  |
| 2008-2009 | 302 | 35 Plaguicidas | 1.0.4 (2013) | T60 |
| 2010-2013 | 302 | Plaguicidas | 1.0.4 (2013) | T60 |
| 2014 | 302 | Plaguicidas | 2.0.0 (2014) | T60 |
| 2015 | 302a | Plaguicidas | 3.0.1 (2016) | T60 |
| 2016 | 302a | Plaguicidas | 3.0.2 (2016) | T60 |
| 2017 | 302a | Plaguicidas | 4.0.0 (2018) | T60 |
| 2018 | 302a | Plaguicidas | 4.0.1 (2018) | T60 |
| 2019-2020 | 302a | Plaguicidas | 5.0.1 (2020) | T60 |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
