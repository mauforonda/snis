# Otras intoxicaciones (2001-2003)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2003. Fuente: SNIS, formularios 302.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2003 |
| Periodicidad | semanal |
| Municipios con registros | 237 |
| Desagregación | agente |
| Filas | 4.062 |

Valores de `agente` (agente):

- alcohol (2001-2003)
- drogas (2001-2003)

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2001 | 2.603 |
| 2002 | 3.972 |
| 2003 | 4.063 |

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
| `agente` | string | Agente de la intoxicación. |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/intoxicacion_otras_2001_2003/datos.parquet'
group by gestion order by gestion;

-- Por gestión y agente
select gestion, agente, sum(casos) as casos
from 'datos/vigilancia/casos/intoxicacion_otras_2001_2003/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/intoxicacion_otras_2001_2003/datos.parquet'
where gestion = 2003 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Otras intoxicaciones (2001-2003) (este dataset): 2001-2003, formulario 302.
- [Otras intoxicaciones (drogas, fármacos, alcohol) (2007-2025)](../../../vigilancia/casos/intoxicacion_otras_2007_2025/readme.md): 2007-2025, formulario 302, 302a.

Las categorías de `agente` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/intoxicacion_otras_2001_2003/datos.parquet',
    'datos/vigilancia/casos/intoxicacion_otras_2007_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2003 | 302 | 88.- Alcohol; 89.- Drogas |  |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302, grupo 13 (intoxicaciones), 2001-2003: la variable tiene una sola columna, "TOTAL-M". Se publica sin sexo, como total. Evidencia: la magnitud es la de un total de ambos sexos. Organofosforados suma de 1.700 a 2.208 por gestión en 2001-2003, y plaguicidas, sin sexo, suma 2.170 en 2004 y 2.077 en 2005.
