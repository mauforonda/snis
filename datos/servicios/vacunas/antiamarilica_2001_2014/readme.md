# Vacuna Antiamarílica (2001-2014)

Dosis aplicadas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2014. Fuente: SNIS, formularios 301.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2014 |
| Periodicidad | mensual |
| Municipios con registros | 340 |
| Desagregación | edad, lugar |
| Filas | 82.632 |

Valores de `lugar` (lugar):

- dentro (2004, 2008-2013)
- fuera (2004, 2008-2013)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2004-2009 | 1 |
| 2010-2014 | 1, 2-4 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 1.171.168 |
| 2002 | 851.868 |
| 2003 | 545.918 |
| 2004 | 934.007 |
| 2005 | 1.033.328 |
| 2006 | 906.367 |
| 2007 | 5.181.856 |
| 2008 | 202.789 |
| 2009 | 160.173 |
| 2010 | 179.388 |
| 2011 | 240.480 |
| 2012 | 252.910 |
| 2013 | 241.693 |
| 2014 | 225.035 |

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
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/antiamarilica_2001_2014/datos.parquet'
group by gestion order by gestion;

-- Por gestión y edad_grupo
select gestion, edad_grupo, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/antiamarilica_2001_2014/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/antiamarilica_2001_2014/datos.parquet'
where gestion = 2014 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Vacuna Antiamarílica (2001-2014) (este dataset): 2001-2014, formulario 301.
- [Vacuna Antiamarílica (2015-2025)](../../../servicios/vacunas/antiamarilica_2015_2025/readme.md): 2015-2025, formulario 301a.

Las categorías de `dosis` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/vacunas/antiamarilica_2001_2014/datos.parquet',
    'datos/servicios/vacunas/antiamarilica_2015_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2003 | 301 | Vacunaciones antiamarílica |  |
| 2004 | 301 | Vacunaciones antiamarílica en personas a partir d; Vacunaciones fiebre amarilla dentro de servicio; Vacunaciones fiebre amarilla fuera de servicio |  |
| 2005-2007 | 301 | Vacunaciones antiamarílica en personas a part; Vacunaciones fiebre amarilla dentro de servic; Vacunaciones fiebre amarilla fuera de servici |  |
| 2008-2009 | 301 | Vacunaciones fiebre amarilla |  |
| 2010-2011 | 301 | Anti Amarílica | 1.0.4 (2013) |
| 2012 | 301 | l 18.2 Anti Amarílica; l 1910 Anti Amarílica | 1.0.4 (2013) |
| 2013 | 301 | Anti Amarílica | 1.0.4 (2013) |
| 2014 | 301 | 18.2 Anti Amarílica; 1910 Anti Amarílica | 2.0.0 (2014) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
