# Usuarias de anticoncepción (2001-2014)

Atenciones registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2014. Fuente: SNIS, formularios 301.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2014 |
| Periodicidad | mensual |
| Municipios con registros | 340 |
| Desagregación | método, usuaria nueva o continua |
| Filas | 347.087 |

Valores de `metodo` (método):

- DIU (2001-2014)
- condón masculino (2001-2014)
- inyectable trimestral (2001-2014)
- métodos naturales (2001-2014)
- píldora (2001-2014)

Valores de `usuaria` (usuaria nueva o continua):

- continua (2001-2014)
- nueva (2001-2014)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 450.895 |
| 2002 | 524.404 |
| 2003 | 586.437 |
| 2004 | 597.904 |
| 2005 | 598.753 |
| 2006 | 574.760 |
| 2007 | 588.814 |
| 2008 | 658.918 |
| 2009 | 645.338 |
| 2010 | 552.103 |
| 2011 | 667.289 |
| 2012 | 570.607 |
| 2013 | 654.639 |
| 2014 | 637.821 |

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
| `usuaria` | string | Usuaria nueva o continua. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/anticoncepcion_prevencion_cancer/usuarias_anticoncepcion_2001_2014/datos.parquet'
group by gestion order by gestion;

-- Por gestión y metodo
select gestion, metodo, sum(cantidad) as cantidad
from 'datos/servicios/anticoncepcion_prevencion_cancer/usuarias_anticoncepcion_2001_2014/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/anticoncepcion_prevencion_cancer/usuarias_anticoncepcion_2001_2014/datos.parquet'
where gestion = 2014 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Usuarias de anticoncepción (2001-2014) (este dataset): 2001-2014, formulario 301.
- [Usuarias de anticoncepción (2015-2025)](../../../servicios/anticoncepcion_prevencion_cancer/usuarias_anticoncepcion_2015_2025/readme.md): 2015-2025, formulario 301a.

Las categorías de `metodo` y `usuaria` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/anticoncepcion_prevencion_cancer/usuarias_anticoncepcion_2001_2014/datos.parquet',
    'datos/servicios/anticoncepcion_prevencion_cancer/usuarias_anticoncepcion_2015_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2007 | 301 | Condón: Usuarias (os) Continuas(os); Condón: Usuarias(os) Nuevas (os); DIU: Usuarias continuas; DIU: Usuarias nuevas; Inyectables trimestral: Usuarias Continuas; Inyectables trimestral: Usuarias Nuevas; Métodos naturales: Usuarias Continuas; Métodos naturales: Usuarias Nuevas; Píldora: Usuarias Continuas; Píldora: Usuarias Nuevas |  |
| 2008-2009 | 301 | Condón: Usuarias (os) Continuas(os); Condón: Usuarias(os) Nuevas (os); DIU: Usuarias continuas; DIU: Usuarias nuevas; Inyectables trimestral: Usuarias Continuas; Inyectables trimestral: Usuarias Nuevas; Métodos naturales: Usuarias Continuas; Métodos naturales: Usuarias Nuevas; Píldora: Usuarias Continuas; Píldora: Usuarias Nuevas | 1.0.4 (2013) |
| 2010-2013 | 301 | Condón: Usuarias (os) Continuas(os); Condón: Usuarias(os) Nuevas (os); DIU: Usuarias continuas; DIU: Usuarias nuevas; Inyectable Trimestral: Usuarias Continuas; Inyectable Trimestral: Usuarias Nuevas; Métodos naturales: Usuarias Continuas; Métodos naturales: Usuarias Nuevas; Píldora: Usuarias Continuas; Píldora: Usuarias Nuevas | 1.0.4 (2013) |
| 2014 | 301 | 5.01 DIU: Usuarias nuevas; 5.02 DIU: Usuarias continuas; 5.04 Inyectable Trimestral: Usuarias Nuevas; 5.05 Inyectable Trimestral: Usuarias Continuas; 5.07 Condón: Usuarias(os) Nuevas (os); 5.08 Condón: Usuarias (os) Continuas(os); 5.10 Píldora: Usuarias Nuevas; 5.11 Píldora: Usuarias Continuas; 5.13 Métodos naturales: Usuarias Nuevas; 5.14 Métodos naturales: Usuarias Continuas | 2.0.0 (2014) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
