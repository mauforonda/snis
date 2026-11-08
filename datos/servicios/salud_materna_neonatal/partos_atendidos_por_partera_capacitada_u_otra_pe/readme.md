# Partos atendidos por partera capacitada u otra pe

Atenciones y nacimientos registrados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2007. Fuente: SNIS, formularios 301.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2007 |
| Periodicidad | mensual |
| Municipios con registros | 318 |
| Desagregación | lugar |
| Filas | 12.230 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 8.758 |
| 2002 | 7.941 |
| 2003 | 6.633 |
| 2004 | 6.224 |
| 2005 | 6.419 |
| 2006 | 5.750 |
| 2007 | 4.986 |

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
from 'datos/servicios/salud_materna_neonatal/partos_atendidos_por_partera_capacitada_u_otra_pe/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/partos_atendidos_por_partera_capacitada_u_otra_pe/datos.parquet'
where gestion = 2007 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Partos atendidos por partera capacitada u otra pe (este dataset): 2001-2007, formulario 301.
- [Partos atendidos por partera capacitada](../../../servicios/salud_materna_neonatal/partos_atendidos_por_partera_capacitada/readme.md): 2008-2025, formulario 301, 301a.

Hasta 2007 la variable es "partos atendidos por partera capacitada u otra pe…" (el tablero corta el nombre); desde 2008, "por partera capacitada". Consultarlos juntos como una serie supone que la variable no cambió de contenido.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/salud_materna_neonatal/partos_atendidos_por_partera_capacitada_u_otra_pe/datos.parquet',
    'datos/servicios/salud_materna_neonatal/partos_atendidos_por_partera_capacitada/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2003 | 301 | Partos atendidos por partera capacitada u otr |  |
| 2004 | 301 | Partos atendidos por partera capacitada u otra pe |  |
| 2005-2007 | 301 | Partos atendidos por partera capacitada u otr |  |
