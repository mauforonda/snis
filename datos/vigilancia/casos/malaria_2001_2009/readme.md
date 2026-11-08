# Malaria (2001-2009)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2009. Fuente: SNIS, formularios 302.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2009 |
| Periodicidad | semanal |
| Municipios con registros | 259 |
| Desagregación | sexo, edad |
| Filas | 54.510 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001-2007 | <1, 1-4, 5-14, 15-59, 60+ |
| 2008-2009 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2001 | 24.739 |
| 2002 | 25.296 |
| 2003 | 50.402 |
| 2004 | 49.912 |
| 2005 | 104.300 |
| 2006 | 108.147 |
| 2007 | 91.536 |
| 2008 | 63.755 |
| 2009 | 44.620 |

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
from 'datos/vigilancia/casos/malaria_2001_2009/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/malaria_2001_2009/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/malaria_2001_2009/datos.parquet'
where gestion = 2009 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Malaria (2001-2009) (este dataset): 2001-2009, formulario 302.
- [Malaria (2010-2014)](../../../vigilancia/casos/malaria_2010_2014/readme.md): 2010-2014, formulario 302.
- [Malaria (2015-2025)](../../../vigilancia/casos/malaria_2015_2025/readme.md): 2015-2025, formulario 302a.

En 2010-2014 la variable es "Malaria confirmados" y el formulario notifica los casos sospechosos aparte; antes y después, "Malaria". Consultarlos juntos como una serie supone que las definiciones cuentan lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/malaria_2001_2009/datos.parquet',
    'datos/vigilancia/casos/malaria_2010_2014/datos.parquet',
    'datos/vigilancia/casos/malaria_2015_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

- Malaria (2001-2009) (este dataset): 2001-2009, formulario 302.
- [Malaria (2010-2014)](../../../vigilancia/casos/malaria_2010_2014/readme.md): 2010-2014, formulario 302.
- [Malaria (sospecha)](../../../vigilancia/casos/malaria_sospecha/readme.md): 2010-2014, formulario 302.
- [Malaria (2015-2025)](../../../vigilancia/casos/malaria_2015_2025/readme.md): 2015-2025, formulario 302a.

En 2010-2014 el formulario notifica por separado los casos de malaria confirmados y los sospechosos; antes y después, una sola variable, "Malaria". Consultarlos juntos como una serie supone que "Malaria" equivale a los confirmados, o a confirmados más sospechosos; el formulario no dice cuál.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/malaria_2001_2009/datos.parquet',
    'datos/vigilancia/casos/malaria_2010_2014/datos.parquet',
    'datos/vigilancia/casos/malaria_sospecha/datos.parquet',
    'datos/vigilancia/casos/malaria_2015_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2003 | 302 | 91.- Malaria |  |
| 2004 | 302 | 23 Malaria |  |
| 2005-2006 | 302 | 26 Malaria |  |
| 2007 | 302 | 25 Malaria |  |
| 2008-2009 | 302 | 26 Malaria |  |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302, 2001-2007: en las variables cuyas columnas "-M" siempre valen 0, "TOTAL-H" es igual a "TOTAL": "-H" contiene a ambos sexos. Esas variables no tienen sexo. En 2004 el grupo 09 (mortalidad) tampoco tiene sexo: hay 79 muertes maternas en "-H" y 94 en "-M".
