# Meningitis tuberculosa en menores de 5 años

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2009. Fuente: SNIS, formularios 302.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2009 |
| Periodicidad | semanal |
| Municipios con registros | 60 |
| Desagregación | sexo, edad |
| Filas | 216 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2004-2009 | <1, 1-4 |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2001 | 36 |
| 2002 | 26 |
| 2003 | 16 |
| 2004 | 22 |
| 2005 | 60 |
| 2006 | 58 |
| 2007 | 71 |
| 2008 | 49 |
| 2009 | 93 |

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
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/meningitis_tb_menor_5/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/meningitis_tb_menor_5/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/meningitis_tb_menor_5/datos.parquet'
where gestion = 2009 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Meningitis tuberculosa en menores de 5 años (este dataset): 2001-2009, formulario 302.
- [Meningitis tuberculosa](../../../vigilancia/casos/meningitis_tuberculosa/readme.md): 2001-2003, formulario 302.
- [Tuberculosis meníngea](../../../vigilancia/casos/tuberculosis_meningea/readme.md): 2010-2025, formulario 302, 302a.

El formulario notifica la meningitis tuberculosa en todas las edades (2001-2003) y en menores de 5 años (2001-2009); desde 2010, la tuberculosis meníngea en todas las edades. Consultarlos juntos como una serie supone que las tres variables cuentan lo mismo en las edades que comparten; filtre por edad antes de unirlas.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/meningitis_tb_menor_5/datos.parquet',
    'datos/vigilancia/casos/meningitis_tuberculosa/datos.parquet',
    'datos/vigilancia/casos/tuberculosis_meningea/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2003 | 302 | 61.- Meningitis tuberculosa en menores de 5 años |  |
| 2004 | 302 | 31 Meningitis TB en menores de 5 años |  |
| 2005-2006 | 302 | 29 Meningitis TB en menores de 5 años |  |
| 2007-2009 | 302 | 28 Meningitis TB en menores de 5 años |  |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302, 2001-2007: en las variables cuyas columnas "-M" siempre valen 0, "TOTAL-H" es igual a "TOTAL": "-H" contiene a ambos sexos. Esas variables no tienen sexo. En 2004 el grupo 09 (mortalidad) tampoco tiene sexo: hay 79 muertes maternas en "-H" y 94 en "-M".
- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
