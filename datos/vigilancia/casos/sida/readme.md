# SIDA

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2014. Fuente: SNIS, formularios 302.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2014 |
| Periodicidad | semanal |
| Municipios con registros | 85 |
| Desagregación | sexo, edad |
| Filas | 2.082 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001 | <1, 5-14, 15-59, 60+ |
| 2002 | 15-59 |
| 2003 | 5-14, 15-59 |
| 2004 | <1, 1-4, 5-14, 15-59, 60+ |
| 2005 | 1-4, 5-14, 15-59, 60+ |
| 2006 | <1, 1-4, 15-59, 60+ |
| 2007 | <1, 1-4, 5-14, 15-59, 60+ |
| 2008 | <1, 1-4, 10-20, 21-59, 60+ |
| 2009-2010 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |
| 2011 | <1, 1-4, 10-20, 21-59, 60+ |
| 2012 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |
| 2013 | 1-4, 10-20, 21-59, 60+ |
| 2014 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2001 | 49 |
| 2002 | 7 |
| 2003 | 27 |
| 2004 | 115 |
| 2005 | 105 |
| 2006 | 117 |
| 2007 | 213 |
| 2008 | 264 |
| 2009 | 227 |
| 2010 | 228 |
| 2011 | 395 |
| 2012 | 586 |
| 2013 | 387 |
| 2014 | 232 |

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
from 'datos/vigilancia/casos/sida/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/sida/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/sida/datos.parquet'
where gestion = 2014 group by all order by casos desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2001-2003 | 302 | 32.- SIDA Mujeres; 33.- SIDA Hombres |  |  |
| 2004-2006 | 302 | 22 SIDA | 1.0.4 (2013) | B20 B24 |
| 2007 | 302 | 21 SIDA * | 1.0.4 (2013) | B20 B24 |
| 2008-2009 | 302 | 22 SIDA * | 1.0.4 (2013) | B20 B24 |
| 2010-2013 | 302 | SIDA * | 1.0.4 (2013) | B20 B24 |
| 2014 | 302 | SIDA * | 2.0.0 (2014) | B20 B24 |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302, 2001-2007: en las variables cuyas columnas "-M" siempre valen 0, "TOTAL-H" es igual a "TOTAL": "-H" contiene a ambos sexos. Esas variables no tienen sexo. En 2004 el grupo 09 (mortalidad) tampoco tiene sexo: hay 79 muertes maternas en "-H" y 94 en "-M".
