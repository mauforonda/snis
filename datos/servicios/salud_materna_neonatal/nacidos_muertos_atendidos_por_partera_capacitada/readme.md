# Nacidos muertos atendidos por partera capacitada

Atenciones y nacimientos registrados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2014. Fuente: SNIS, formularios 301.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2014 |
| Periodicidad | mensual |
| Municipios con registros | 278 |
| Desagregación | lugar |
| Filas | 2.065 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 345 |
| 2002 | 266 |
| 2003 | 233 |
| 2004 | 226 |
| 2005 | 282 |
| 2006 | 194 |
| 2007 | 174 |
| 2008 | 158 |
| 2009 | 136 |
| 2010 | 215 |
| 2011 | 142 |
| 2012 | 123 |
| 2013 | 169 |
| 2014 | 165 |

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
from 'datos/servicios/salud_materna_neonatal/nacidos_muertos_atendidos_por_partera_capacitada/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/nacidos_muertos_atendidos_por_partera_capacitada/datos.parquet'
where gestion = 2014 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Nacidos muertos atendidos por partera capacitada (este dataset): 2001-2014, formulario 301.
- [Nacidos muertos atendidos por partera](../../../servicios/salud_materna_neonatal/nacidos_muertos_atendidos_por_partera/readme.md): 2015-2025, formulario 301a.

La variable cambia de nombre: "por partera capacitada" (2001-2014) y "por partera" (desde 2015). Consultarlos juntos como una serie supone que las dos cuentan lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/salud_materna_neonatal/nacidos_muertos_atendidos_por_partera_capacitada/datos.parquet',
    'datos/servicios/salud_materna_neonatal/nacidos_muertos_atendidos_por_partera/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2003 | 301 | Nacidos muertos atendidos por partera capacit |  |
| 2004 | 301 | Nacidos muertos atendidos por partera capacitada |  |
| 2005-2007 | 301 | Nacidos muertos atendidos por partera capacit |  |
| 2008-2011 | 301 | Nacidos muertos atendidos por partera capacitada | 1.0.4 (2013) |
| 2012 | 301 | l 12.8 Nacidos muertos atendidos por partera capacitada | 1.0.4 (2013) |
| 2013 | 301 | Nacidos muertos atendidos por partera capacitada | 1.0.4 (2013) |
| 2014 | 301 | 12.8 Nacidos muertos atendidos por partera capacitada | 2.0.0 (2014) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
