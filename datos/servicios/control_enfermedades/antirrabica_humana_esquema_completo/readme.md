# Antirrábica humana esquema completo

Registros en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2014. Fuente: SNIS, formularios 301.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2014 |
| Periodicidad | mensual |
| Municipios con registros | 299 |
| Desagregación | lugar |
| Filas | 6.690 |

Valores de `lugar` (lugar):

- dentro (2010-2013)
- fuera (2010-2013)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 4.520 |
| 2002 | 3.598 |
| 2003 | 3.845 |
| 2004 | 7.047 |
| 2005 | 10.617 |
| 2006 | 10.477 |
| 2007 | 6.163 |
| 2008 | 7.072 |
| 2009 | 4.878 |
| 2010 | 5.245 |
| 2011 | 7.095 |
| 2012 | 7.143 |
| 2013 | 8.237 |
| 2014 | 8.023 |

## Cómo utilizar

Cada fila da el número de cantidad de un periodo, un municipio y una población. Para obtener un total, sume las filas: el dataset no tiene filas de total. Una combinación sin fila significa que no hubo registros. Las convenciones de tiempo, territorio y población están en el [catálogo](../../../README.md#cómo-leer-los-datos).

| Columna | Tipo | Descripción |
| --- | --- | --- |
| `gestion` | integer | Año calendario (gestión) del registro. |
| `mes` | integer | Mes, de 1 a 12. |
| `fecha_inicio` | date | Primer día de la semana o del mes. |
| `departamento` | string | Nombre del departamento. |
| `municipio` | string | Nombre del municipio. |
| `municipio_codigo` | string | Código del municipio, 6 dígitos: departamento (2), provincia (2) y municipio (2). |
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/antirrabica_humana_esquema_completo/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/antirrabica_humana_esquema_completo/datos.parquet'
where gestion = 2014 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2009 | 301 | Antirrábica humana esquema completo |  |
| 2010-2011 | 301 | Antirrábica humana esquema completo | 1.0.4 (2013) |
| 2012 | 301 | l 2110 Antirrábica humana esquema completo | 1.0.4 (2013) |
| 2013 | 301 | Antirrábica humana esquema completo | 1.0.4 (2013) |
| 2014 | 301 | 2110 Antirrábica humana esquema completo | 2.0.0 (2014) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
