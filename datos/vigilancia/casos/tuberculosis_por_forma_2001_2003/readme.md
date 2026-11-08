# Tuberculosis por forma (2001-2003)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2003. Fuente: SNIS, formularios 302.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2003 |
| Periodicidad | semanal |
| Municipios con registros | 273 |
| Desagregación | forma |
| Filas | 7.703 |

Valores de `forma` (forma):

- extrapulmonar (2001-2003)
- pulmonar BAAR negativo, nuevo (2001-2003)
- pulmonar BAAR positivo, nuevo (2001-2003)
- pulmonar BAAR positivo, previamente tratado (2001-2003)

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2001 | 10.288 |
| 2002 | 5.401 |
| 2003 | 3.705 |

## Cómo utilizar

Cada fila da el número de casos de un periodo, un municipio y una población. Para obtener un total, sume las filas: el dataset no tiene filas de total. Una combinación sin fila significa que no hubo registros. Las convenciones de tiempo, territorio y población están en el [catálogo](../../../README.md#cómo-leer-los-datos).

| Columna | Tipo | Descripción |
| --- | --- | --- |
| `gestion` | integer | Año calendario (gestión) del registro. |
| `semana` | integer | Semana epidemiológica, de 1 a 53. Va de domingo a sábado. |
| `fecha_inicio` | date | Primer día de la semana o del mes. |
| `departamento` | string | Nombre del departamento. |
| `municipio` | string | Nombre del municipio. |
| `municipio_codigo` | string | Código del municipio, 6 dígitos: departamento (2), provincia (2) y municipio (2). |
| `forma` | string | Forma de la tuberculosis. |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/tuberculosis_por_forma_2001_2003/datos.parquet'
group by gestion order by gestion;

-- Por gestión y forma
select gestion, forma, sum(casos) as casos
from 'datos/vigilancia/casos/tuberculosis_por_forma_2001_2003/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/tuberculosis_por_forma_2001_2003/datos.parquet'
where gestion = 2003 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Tuberculosis por forma (2001-2003) (este dataset): 2001-2003, formulario 302.
- [Tuberculosis por forma (2004-2007)](../../../vigilancia/casos/tuberculosis_por_forma_2004_2007/readme.md): 2004-2007, formulario 302.

Las categorías de `forma` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/tuberculosis_por_forma_2001_2003/datos.parquet',
    'datos/vigilancia/casos/tuberculosis_por_forma_2004_2007/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2003 | 302 | 62.- Tuberculosis pulmonar BAAR (+) nuevos; 63.- Tuberculosis pulmonar BAAR (-); 64.- Tuberculosis extrapulmonar; 65.- Tuberculosis pulmonar BAAR (+) prevamente tratados |  |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
