# Vacuna SRP (sarampión, rubéola y parotiditis) (2001-2009)

Dosis aplicadas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2009. Fuente: SNIS, formularios 301.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2009 |
| Periodicidad | mensual |
| Municipios con registros | 325 |
| Desagregación | edad, lugar |
| Filas | 57.795 |

Valores de `lugar` (lugar):

- dentro (2001-2009)
- fuera (2001-2009)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001-2009 | 1 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 262.306 |
| 2002 | 238.267 |
| 2003 | 262.507 |
| 2004 | 230.942 |
| 2005 | 230.125 |
| 2006 | 228.828 |
| 2007 | 216.064 |
| 2008 | 226.318 |
| 2009 | 225.037 |

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
from 'datos/servicios/vacunas/srp_2001_2009/datos.parquet'
group by gestion order by gestion;

-- Por gestión y edad_grupo
select gestion, edad_grupo, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/srp_2001_2009/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/srp_2001_2009/datos.parquet'
where gestion = 2009 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Vacuna SRP (sarampión, rubéola y parotiditis) (2001-2009) (este dataset): 2001-2009, formulario 301.
- [Vacuna SRP (sarampión, rubéola y parotiditis) (2010-2017)](../../../servicios/vacunas/srp_2010_2017/readme.md): 2010-2017, formulario 301, 301a.
- [Vacuna SRP (sarampión, rubéola y parotiditis) (2018-2025)](../../../servicios/vacunas/srp_2018_2025/readme.md): 2018-2025, formulario 301a.

Las categorías de `dosis` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/vacunas/srp_2001_2009/datos.parquet',
    'datos/servicios/vacunas/srp_2010_2017/datos.parquet',
    'datos/servicios/vacunas/srp_2018_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2007 | 301 | Vacunaciones SRP dentro de servicio; Vacunaciones SRP fuera de servicio |  |
| 2008-2009 | 301 | Vacunaciones SRP |  |
