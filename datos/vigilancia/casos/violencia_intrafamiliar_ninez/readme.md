# Violencia intrafamiliar contra niñas y niños

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2003. Fuente: SNIS, formularios 302.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2003 |
| Periodicidad | semanal |
| Municipios con registros | 218 |
| Desagregación | sexo |
| Filas | 2.348 |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2001 | 1.113 |
| 2002 | 1.682 |
| 2003 | 1.237 |

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
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/violencia_intrafamiliar_ninez/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/violencia_intrafamiliar_ninez/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/violencia_intrafamiliar_ninez/datos.parquet'
where gestion = 2003 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Violencia intrafamiliar](../../../vigilancia/casos/violencia_intrafamiliar/readme.md): 2001-2023, formulario 302, 302a.
- Violencia intrafamiliar contra niñas y niños (este dataset): 2001-2003, formulario 302.

En 2001-2003 el formulario notifica aparte la violencia intrafamiliar contra niñas y niños. No sabemos si esos casos están también en la violencia intrafamiliar.

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2003 | 302 | 68.- Violencia contra el niño; 69.- Violencia contra la niña |  |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
