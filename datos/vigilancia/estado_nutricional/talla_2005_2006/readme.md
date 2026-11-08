# Talla para la edad (2005-2006)

Personas evaluadas, por resultado en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2005-2006. Fuente: SNIS, formularios 302.

## Qué es

| | |
| --- | --- |
| Gestiones | 2005-2006 |
| Periodicidad | semanal |
| Municipios con registros | 120 |
| Desagregación | clasificación, sexo, edad |
| Filas | 9.305 |

Valores de `clasificacion` (clasificación):

- baja grave (2005-2006)
- baja leve (2005-2006)
- baja moderada (2005-2006)
- normal (2005-2006)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2005-2006 | <2, 2-4 |

Total por gestión:

| Gestión | Personas |
| ---: | ---: |
| 2005 | 18.411 |
| 2006 | 59.277 |

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
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `personas` | integer | Número de personas en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(personas) as personas
from 'datos/vigilancia/estado_nutricional/talla_2005_2006/datos.parquet'
group by gestion order by gestion;

-- Por gestión y clasificacion
select gestion, clasificacion, sum(personas) as personas
from 'datos/vigilancia/estado_nutricional/talla_2005_2006/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(personas) as personas
from 'datos/vigilancia/estado_nutricional/talla_2005_2006/datos.parquet'
where gestion = 2006 group by all order by personas desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Talla para la edad (2005-2006) (este dataset): 2005-2006, formulario 302.
- [Talla baja (moderada y grave) (2007)](../../../vigilancia/estado_nutricional/talla_2007/readme.md): 2007, formulario 302.
- [Talla para la edad (2008-2025)](../../../vigilancia/estado_nutricional/talla_2008_2025/readme.md): 2008-2025, formulario 302, 302b.

Las categorías de `clasificacion` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(personas) as personas
from read_parquet([
    'datos/vigilancia/estado_nutricional/talla_2005_2006/datos.parquet',
    'datos/vigilancia/estado_nutricional/talla_2007/datos.parquet',
    'datos/vigilancia/estado_nutricional/talla_2008_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2005-2006 | 302 | 54 Talla normal (N); 55 Talla baja leve (L); 56 Talla baja moderada (M); 57 Talla baja grave (G) |  |
