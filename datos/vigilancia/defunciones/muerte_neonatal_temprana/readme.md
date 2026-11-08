# Muerte neonatal temprana (menos de 7 días)

Muertes por esta causa en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2014. Fuente: SNIS, formularios 302.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2014 |
| Periodicidad | semanal |
| Municipios con registros | 312 |
| Desagregación | sexo, lugar |
| Filas | 11.833 |

Valores de `lugar` (lugar):

- dentro (2001-2003, 2005-2014)
- fuera (2005-2014)

Total por gestión:

| Gestión | Defunciones |
| ---: | ---: |
| 2001 | 920 |
| 2002 | 893 |
| 2003 | 975 |
| 2004 | 1.481 |
| 2005 | 1.428 |
| 2006 | 1.330 |
| 2007 | 1.293 |
| 2008 | 1.299 |
| 2009 | 1.309 |
| 2010 | 1.300 |
| 2011 | 1.374 |
| 2012 | 1.374 |
| 2013 | 1.372 |
| 2014 | 1.143 |

## Cómo utilizar

Cada fila da el número de defunciones de un periodo, un municipio y una población. Para obtener un total, sume las filas: el dataset no tiene filas de total. Una combinación sin fila significa que no hubo registros. Las convenciones de tiempo, territorio y población están en el [catálogo](../../../README.md#cómo-leer-los-datos).

| Columna | Tipo | Descripción |
| --- | --- | --- |
| `gestion` | integer | Año calendario (gestión) del registro. |
| `semana` | integer | Semana epidemiológica, de 1 a 53. Va de domingo a sábado. |
| `fecha_inicio` | date | Primer día de la semana o del mes. |
| `departamento` | string | Nombre del departamento. |
| `municipio` | string | Nombre del municipio. |
| `municipio_codigo` | string | Código del municipio, 6 dígitos: departamento (2), provincia (2) y municipio (2). |
| `sexo` | string | mujer u hombre. |
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `defunciones` | integer | Número de defunciones en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_neonatal_temprana/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_neonatal_temprana/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_neonatal_temprana/datos.parquet'
where gestion = 2014 group by all order by defunciones desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2003 | 302 | 71.- Muerte RN menor de 7 días | 1.0.4 (2013) |
| 2004 | 302 | 38 Muerte RN menor de 7 días |  |
| 2005-2007 | 302 | 39 Muerte RN menor de 7 días | 1.0.4 (2013) |
| 2008-2009 | 302 | 38 Muerte RN menor de 7 días | 1.0.4 (2013) |
| 2010-2013 | 302 | Muerte RN menor de 7 días | 1.0.4 (2013) |
| 2014 | 302 | Muerte RN menor de 7 días | 2.0.0 (2014) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302, 2001-2007: en las variables cuyas columnas "-M" siempre valen 0, "TOTAL-H" es igual a "TOTAL": "-H" contiene a ambos sexos. Esas variables no tienen sexo. En 2004 el grupo 09 (mortalidad) tampoco tiene sexo: hay 79 muertes maternas en "-H" y 94 en "-M".
- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
