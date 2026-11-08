# Vacuna Pentavalente (2001-2014)

Dosis aplicadas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2014. Fuente: SNIS, formularios 301.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2014 |
| Periodicidad | mensual |
| Municipios con registros | 340 |
| Desagregación | dosis, edad, lugar |
| Filas | 281.231 |

Valores de `dosis` (dosis):

- 1 (2001-2014)
- 2 (2001-2014)
- 3 (2001-2014)

Valores de `lugar` (lugar):

- dentro (2001-2013)
- fuera (2001-2013)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001-2014 | <1 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 692.751 |
| 2002 | 674.501 |
| 2003 | 639.636 |
| 2004 | 666.975 |
| 2005 | 678.190 |
| 2006 | 656.731 |
| 2007 | 647.061 |
| 2008 | 666.569 |
| 2009 | 669.507 |
| 2010 | 654.296 |
| 2011 | 686.438 |
| 2012 | 664.461 |
| 2013 | 680.459 |
| 2014 | 662.107 |

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
| `dosis` | string | Dosis: número (1 a 5), inicial, única, anual o refuerzo. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/pentavalente_2001_2014/datos.parquet'
group by gestion order by gestion;

-- Por gestión y dosis
select gestion, dosis, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/pentavalente_2001_2014/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/pentavalente_2001_2014/datos.parquet'
where gestion = 2014 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Vacuna Pentavalente (2001-2014) (este dataset): 2001-2014, formulario 301.
- [Vacuna Pentavalente (2015-2025)](../../../servicios/vacunas/pentavalente_2015_2025/readme.md): 2015-2025, formulario 301a.

Las categorías de `dosis` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/vacunas/pentavalente_2001_2014/datos.parquet',
    'datos/servicios/vacunas/pentavalente_2015_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2007 | 301 | Pentavalente 3ra dosis; Pentavalentes 1ra dosis; Pentavalentes 2da dosis |  |
| 2008-2009 | 301 | Pentavalente 1ra. dosis; Pentavalente 2da. dosis; Pentavalente 3ra. dosis | 1.0.4 (2013) |
| 2010-2011 | 301 | Pentavalente 1ra. Dosis; Pentavalente 2da. Dosis; Pentavalente 3ra. Dosis | 1.0.4 (2013) |
| 2012 | 301 | l 17.2 Pentavalente 1ra. Dosis; l 17.3 Pentavalente 2da. Dosis; l 17.4 Pentavalente 3ra. Dosis | 1.0.4 (2013) |
| 2013 | 301 | Pentavalente 1ra. Dosis; Pentavalente 2da. Dosis; Pentavalente 3ra. Dosis | 1.0.4 (2013) |
| 2014 | 301 | 17.2 Pentavalente 1ra. Dosis; 17.3 Pentavalente 2da. Dosis; 17.4 Pentavalente 3ra. Dosis | 2.0.0 (2014) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
