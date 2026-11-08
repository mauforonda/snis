# Egresos por diagnóstico (2001-2007)

Registros de internación en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2007. Fuente: SNIS, formularios 301.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2007 |
| Periodicidad | mensual |
| Municipios con registros | 283 |
| Desagregación | diagnóstico, edad |
| Filas | 24.314 |

Valores de `diagnostico` (diagnóstico):

- diarreas (2001-2007)
- neumonias (2001-2007)
- otros (2001-2007)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001-2007 | <5 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 54.506 |
| 2002 | 61.951 |
| 2003 | 68.734 |
| 2004 | 73.240 |
| 2005 | 73.078 |
| 2006 | 96.194 |
| 2007 | 87.914 |

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
| `diagnostico` | string | Diagnóstico de egreso. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/internacion/egresos_por_diagnostico_2001_2007/datos.parquet'
group by gestion order by gestion;

-- Por gestión y diagnostico
select gestion, diagnostico, sum(cantidad) as cantidad
from 'datos/servicios/internacion/egresos_por_diagnostico_2001_2007/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/internacion/egresos_por_diagnostico_2001_2007/datos.parquet'
where gestion = 2007 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Egresos por diagnóstico (2001-2007) (este dataset): 2001-2007, formulario 301.
- [Egresos por diagnóstico (2008-2009)](../../../servicios/internacion/egresos_por_diagnostico_2008_2009/readme.md): 2008-2009, formulario 301.
- [Egresos por diagnóstico (2010-2014)](../../../servicios/internacion/egresos_por_diagnostico_2010_2014/readme.md): 2010-2014, formulario 301.

Las categorías de `diagnostico` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/internacion/egresos_por_diagnostico_2001_2007/datos.parquet',
    'datos/servicios/internacion/egresos_por_diagnostico_2008_2009/datos.parquet',
    'datos/servicios/internacion/egresos_por_diagnostico_2010_2014/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2007 | 301 | Diarreas; Neumonías; Otros |  |
