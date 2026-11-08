# Anestesias generales, locales o regionales

Registros en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2007. Fuente: SNIS, formularios 301.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2007 |
| Periodicidad | mensual |
| Municipios con registros | 233 |
| Desagregación |  |
| Filas | 9.088 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 84.935 |
| 2002 | 123.982 |
| 2003 | 135.126 |
| 2004 | 154.493 |
| 2005 | 169.219 |
| 2006 | 186.477 |
| 2007 | 205.102 |

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
from 'datos/servicios/cirugia/anestesias_generales_locales_o_regionales/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/cirugia/anestesias_generales_locales_o_regionales/datos.parquet'
where gestion = 2007 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Anestesias generales, locales o regionales (este dataset): 2001-2007, formulario 301.
- [Anestesias generales y regionales](../../../servicios/cirugia/anestesias_generales_y_regionales/readme.md): 2008-2014, formulario 301.
- [Anestesias generales](../../../servicios/cirugia/anestesias_generales/readme.md): 2015-2025, formulario 301b.
- [Anestesias regionales](../../../servicios/cirugia/anestesias_regionales/readme.md): 2015-2025, formulario 301b.

El formulario 301 cuenta juntas las anestesias generales, locales o regionales (2001-2007) y después las generales y regionales (2008-2014); desde 2015 el 301b cuenta por separado las generales y las regionales, y las locales están en otro dataset. Consultarlos juntos como una serie supone que las categorías de cada periodo cuentan lo mismo; antes de 2008 incluyen las locales.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/cirugia/anestesias_generales_locales_o_regionales/datos.parquet',
    'datos/servicios/cirugia/anestesias_generales_y_regionales/datos.parquet',
    'datos/servicios/cirugia/anestesias_generales/datos.parquet',
    'datos/servicios/cirugia/anestesias_regionales/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2007 | 301 | Anestesias generales, locales o regionales |  |
