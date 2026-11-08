# Clasificación nutricional A a F

Personas evaluadas, por resultado en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2004. Fuente: SNIS, formularios 302.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2004 |
| Periodicidad | semanal |
| Municipios con registros | 312 |
| Desagregación | clasificación |
| Filas | 219.970 |

Valores de `clasificacion` (clasificación):

- A y B (2001-2004)
- C (2001-2004)
- D (2001-2004)
- E (2001-2004)
- F (2001-2004)

Total por gestión:

| Gestión | Personas |
| ---: | ---: |
| 2001 | 1.811.308 |
| 2002 | 1.983.721 |
| 2003 | 2.335.909 |
| 2004 | 2.556.696 |

## Cómo utilizar

Cada fila da el número de personas de un periodo, un municipio y una población. Para obtener un total, sume las filas: el dataset no tiene filas de total. Una combinación sin fila significa que no hubo registros. Las convenciones de tiempo, territorio y población están en el [catálogo](../../../README.md#cómo-leer-los-datos).

| Columna | Tipo | Descripción |
| --- | --- | --- |
| `gestion` | integer | Año calendario (gestión) del registro. |
| `semana` | integer | Semana epidemiológica, de 1 a 53. Va de domingo a sábado. |
| `fecha_inicio` | date | Primer día de la semana o del mes. |
| `departamento` | string | Nombre del departamento. |
| `municipio` | string | Nombre del municipio. |
| `municipio_codigo` | string | Código del municipio, 6 dígitos: departamento (2), provincia (2) y municipio (2). |
| `clasificacion` | string | Clasificación. |
| `personas` | integer | Número de personas en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(personas) as personas
from 'datos/vigilancia/estado_nutricional/clasificacion_nutricional_2001/datos.parquet'
group by gestion order by gestion;

-- Por gestión y clasificacion
select gestion, clasificacion, sum(personas) as personas
from 'datos/vigilancia/estado_nutricional/clasificacion_nutricional_2001/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(personas) as personas
from 'datos/vigilancia/estado_nutricional/clasificacion_nutricional_2001/datos.parquet'
where gestion = 2004 group by all order by personas desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2003 | 302 | 82.- Clasificación A y B; 83.- Clasificación C; 84.- Clasificación D; 85.- Clasificación E; 86.- Clasificación F |  |
| 2004 | 302 | 44 Clasificacion A y B; 45 Clasificacion C; 46 Clasificacion D; 47 Clasificacion E; 48 Clasificacion F |  |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
