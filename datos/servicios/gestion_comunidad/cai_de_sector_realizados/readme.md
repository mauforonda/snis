# CAI de sector realizados

Actividades registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2004-2009. Fuente: SNIS, formularios 301.

## Qué es

| | |
| --- | --- |
| Gestiones | 2004-2009 |
| Periodicidad | mensual |
| Municipios con registros | 325 |
| Desagregación |  |
| Filas | 11.500 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2004 | 6.085 |
| 2005 | 5.968 |
| 2006 | 6.390 |
| 2007 | 6.112 |
| 2008 | 6.388 |
| 2009 | 6.063 |

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
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/gestion_comunidad/cai_de_sector_realizados/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/gestion_comunidad/cai_de_sector_realizados/datos.parquet'
where gestion = 2009 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- CAI de sector realizados (este dataset): 2004-2009, formulario 301.
- [CAI de establecimiento](../../../servicios/gestion_comunidad/cai_de_establecimiento/readme.md): 2010-2025, formulario 301, 301a.

Hasta 2009 la variable es "CAI de sector realizados"; desde 2010, "CAI de establecimiento". Consultarlos juntos como una serie supone que las dos cuentan lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/gestion_comunidad/cai_de_sector_realizados/datos.parquet',
    'datos/servicios/gestion_comunidad/cai_de_establecimiento/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2004-2007 | 301 | Nº de CAI de sector realizados |  |
| 2008-2009 | 301 | Nº de CAI de sector realizados | 1.0.4 (2013) |
