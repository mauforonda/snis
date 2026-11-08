# Cirugías medianas y mayores

Registros en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2014. Fuente: SNIS, formularios 301.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2014 |
| Periodicidad | mensual |
| Municipios con registros | 174 |
| Desagregación | sexo |
| Filas | 17.581 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 78.582 |
| 2002 | 111.139 |
| 2003 | 124.007 |
| 2004 | 133.354 |
| 2005 | 141.692 |
| 2006 | 154.419 |
| 2007 | 165.609 |
| 2008 | 166.572 |
| 2009 | 176.203 |
| 2010 | 172.526 |
| 2011 | 190.762 |
| 2012 | 193.182 |
| 2013 | 221.273 |
| 2014 | 193.459 |

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
| `sexo` | string | mujer u hombre. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/cirugia/cirugias_medianas_y_mayores/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/cirugia/cirugias_medianas_y_mayores/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/cirugia/cirugias_medianas_y_mayores/datos.parquet'
where gestion = 2014 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Cirugías medianas y mayores (este dataset): 2001-2014, formulario 301.
- [Cirugias mayores](../../../servicios/cirugia/cirugias_mayores/readme.md): 2015-2025, formulario 301b.
- [Cirugias medianas](../../../servicios/cirugia/cirugias_medianas/readme.md): 2015-2025, formulario 301b.

Hasta 2014 el formulario 301 cuenta juntas las cirugías medianas y mayores; desde 2015 el 301b las cuenta por separado. Consultarlos juntos como una serie supone que las dos suman lo mismo que el total anterior.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/cirugia/cirugias_medianas_y_mayores/datos.parquet',
    'datos/servicios/cirugia/cirugias_mayores/datos.parquet',
    'datos/servicios/cirugia/cirugias_medianas/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2007 | 301 | Cirugías medianas y mayores |  |
| 2008-2013 | 301 | Cirugías medianas y mayores | 1.0.4 (2013) |
| 2014 | 301 | 15.1 Cirugías medianas y mayores | 2.0.0 (2014) |
