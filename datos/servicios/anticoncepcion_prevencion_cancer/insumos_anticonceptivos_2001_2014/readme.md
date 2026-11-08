# Insumos anticonceptivos entregados o insertados (2001-2014)

Atenciones registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2014. Fuente: SNIS, formularios 301.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2014 |
| Periodicidad | mensual |
| Municipios con registros | 340 |
| Desagregación | método |
| Filas | 110.453 |

Valores de `metodo` (método):

- DIU (2001-2014)
- condón masculino (2001-2014)
- píldora (2001-2014)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 857.079 |
| 2002 | 1.001.397 |
| 2003 | 993.960 |
| 2004 | 1.011.640 |
| 2005 | 944.411 |
| 2006 | 766.099 |
| 2007 | 763.987 |
| 2008 | 927.129 |
| 2009 | 1.053.352 |
| 2010 | 1.184.517 |
| 2011 | 1.135.326 |
| 2012 | 1.277.704 |
| 2013 | 1.636.814 |
| 2014 | 1.540.622 |

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
| `metodo` | string | Método anticonceptivo. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/anticoncepcion_prevencion_cancer/insumos_anticonceptivos_2001_2014/datos.parquet'
group by gestion order by gestion;

-- Por gestión y metodo
select gestion, metodo, sum(cantidad) as cantidad
from 'datos/servicios/anticoncepcion_prevencion_cancer/insumos_anticonceptivos_2001_2014/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/anticoncepcion_prevencion_cancer/insumos_anticonceptivos_2001_2014/datos.parquet'
where gestion = 2014 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Insumos anticonceptivos entregados o insertados (2001-2014) (este dataset): 2001-2014, formulario 301.
- [Insumos anticonceptivos entregados o insertados (2015-2025)](../../../servicios/anticoncepcion_prevencion_cancer/insumos_anticonceptivos_2015_2025/readme.md): 2015-2025, formulario 301a.

Las categorías de `metodo` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/anticoncepcion_prevencion_cancer/insumos_anticonceptivos_2001_2014/datos.parquet',
    'datos/servicios/anticoncepcion_prevencion_cancer/insumos_anticonceptivos_2015_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2007 | 301 | Número de DIU insertados; Número de ciclos entregados; Número de condones entregados |  |
| 2008-2009 | 301 | Número de DIU insertados; Número de ciclos entregados; Número de condones entregados | 1.0.4 (2013) |
| 2010-2013 | 301 | Número de DIU Insertados; Número de ciclos entregados; Número de condones entregados | 1.0.4 (2013) |
| 2014 | 301 | 5.03 Número de DIU Insertados; 5.09 Número de condones entregados; 5.12 Número de ciclos entregados | 2.0.0 (2014) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
