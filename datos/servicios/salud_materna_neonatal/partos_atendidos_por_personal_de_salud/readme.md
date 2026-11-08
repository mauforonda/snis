# Partos atendidos por personal de salud

Atenciones y nacimientos registrados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2014. Fuente: SNIS, formularios 301.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2014 |
| Periodicidad | mensual |
| Municipios con registros | 340 |
| Desagregación | lugar |
| Filas | 39.543 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 12.380 |
| 2002 | 14.101 |
| 2003 | 14.922 |
| 2004 | 14.242 |
| 2005 | 14.529 |
| 2006 | 15.074 |
| 2007 | 15.060 |
| 2008 | 15.185 |
| 2009 | 14.172 |
| 2010 | 14.934 |
| 2011 | 15.596 |
| 2012 | 15.235 |
| 2013 | 14.491 |
| 2014 | 13.687 |

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
from 'datos/servicios/salud_materna_neonatal/partos_atendidos_por_personal_de_salud/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/partos_atendidos_por_personal_de_salud/datos.parquet'
where gestion = 2014 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Partos atendidos por personal de salud (este dataset): 2001-2014, formulario 301.
- [Partos atendidos por personal de salud calificado](../../../servicios/salud_materna_neonatal/partos_atendidos_por_personal_de_salud_calificado/readme.md): 2015-2025, formulario 301a.
- [Partos atendidos por proveedor calificado](../../../servicios/salud_materna_neonatal/partos_atendidos_por_proveedor_calificado/readme.md): 2015-2025, formulario 301a.

Hasta 2014 el formulario 301 cuenta los partos atendidos por personal de salud; desde 2015 el 301a separa proveedor calificado (médicos) y personal de salud calificado (enfermería), según su instructivo. Consultarlos juntos como una serie supone que los dos grupos de 2015 suman lo mismo que "personal de salud".

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/salud_materna_neonatal/partos_atendidos_por_personal_de_salud/datos.parquet',
    'datos/servicios/salud_materna_neonatal/partos_atendidos_por_personal_de_salud_calificado/datos.parquet',
    'datos/servicios/salud_materna_neonatal/partos_atendidos_por_proveedor_calificado/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2007 | 301 | Partos atendidos por personal de salud |  |
| 2008-2013 | 301 | Partos atendidos por personal de salud | 1.0.4 (2013) |
| 2014 | 301 | 12.1 Partos atendidos por personal de salud | 2.0.0 (2014) |
