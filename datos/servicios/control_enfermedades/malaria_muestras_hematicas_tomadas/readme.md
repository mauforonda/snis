# Malaria: muestras hemáticas tomadas

Registros en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2007-2014. Fuente: SNIS, formularios 301.

## Qué es

| | |
| --- | --- |
| Gestiones | 2007-2014 |
| Periodicidad | mensual |
| Municipios con registros | 184 |
| Desagregación | sexo, especie |
| Filas | 11.258 |

Valores de `especie` (especie):

- P. falciparum (2010-2013)
- P. vivax (2010-2013)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2007 | 136.512 |
| 2008 | 122.261 |
| 2009 | 95.396 |
| 2010 | 95.615 |
| 2011 | 106.927 |
| 2012 | 90.655 |
| 2013 | 90.827 |
| 2014 | 68.454 |

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
| `especie` | string | Especie de Plasmodium. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/malaria_muestras_hematicas_tomadas/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/malaria_muestras_hematicas_tomadas/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/malaria_muestras_hematicas_tomadas/datos.parquet'
where gestion = 2014 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Malaria: muestras tomadas por agente comunario](../../../servicios/control_enfermedades/malaria_muestras_tomadas_por_agente_comunario/readme.md): 2005-2006, formulario 301.
- [Malaria: muestras tomadas por personal de salud](../../../servicios/control_enfermedades/malaria_muestras_tomadas_por_personal_de_salud/readme.md): 2005-2006, formulario 301.
- Malaria: muestras hemáticas tomadas (este dataset): 2007-2014, formulario 301.

Las muestras de malaria se cuentan por quién las toma (2005-2006) y después en total (2007-2014). Consultarlos juntos como una serie supone que las dos categorías de 2005-2006 suman todas las muestras.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/control_enfermedades/malaria_muestras_tomadas_por_agente_comunario/datos.parquet',
    'datos/servicios/control_enfermedades/malaria_muestras_tomadas_por_personal_de_salud/datos.parquet',
    'datos/servicios/control_enfermedades/malaria_muestras_hematicas_tomadas/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2007-2009 | 301 | Número de Muestras hemáticas tomadas |  |
| 2010-2011 | 301 | Número de Muestras hemáticas tomadas | 1.0.4 (2013) |
| 2012 | 301 | l 21.1 Número de Muestras hemáticas tomadas | 1.0.4 (2013) |
| 2013 | 301 | Número de Muestras hemáticas tomadas | 1.0.4 (2013) |
| 2014 | 301 | 21.1 Número de Muestras hemáticas tomadas | 2.0.0 (2014) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
