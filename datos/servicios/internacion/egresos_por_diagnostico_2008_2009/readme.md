# Egresos por diagnóstico (2008-2009)

Registros de internación en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2008-2009. Fuente: SNIS, formularios 301.

## Qué es

| | |
| --- | --- |
| Gestiones | 2008-2009 |
| Periodicidad | mensual |
| Municipios con registros | 212 |
| Desagregación | diagnóstico |
| Filas | 8.575 |

Valores de `diagnostico` (diagnóstico):

- diabetes (2008-2009)
- diarreas (2008-2009)
- discapacitados (2008-2009)
- hipertension arterial (2008-2009)
- neumonias (2008-2009)
- otros (2008-2009)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2008 | 89.999 |
| 2009 | 90.728 |

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
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/internacion/egresos_por_diagnostico_2008_2009/datos.parquet'
group by gestion order by gestion;

-- Por gestión y diagnostico
select gestion, diagnostico, sum(cantidad) as cantidad
from 'datos/servicios/internacion/egresos_por_diagnostico_2008_2009/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/internacion/egresos_por_diagnostico_2008_2009/datos.parquet'
where gestion = 2009 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Egresos por diagnóstico (2001-2007)](../../../servicios/internacion/egresos_por_diagnostico_2001_2007/readme.md): 2001-2007, formulario 301.
- Egresos por diagnóstico (2008-2009) (este dataset): 2008-2009, formulario 301.
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
| 2008-2009 | 301 | Diabetes en mayores de 5 años; Diarreas en menores de 5 años; Discapacitados; Hipertensión Arterial en mayores de 5 años; Neumonías en menores de 5 años; Otros en menores de 5 años | 1.0.4 (2013) |
