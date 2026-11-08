# Peso para la edad (2008-2014)

Personas evaluadas, por resultado en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2008-2014. Fuente: SNIS, formularios 302.

## Qué es

| | |
| --- | --- |
| Gestiones | 2008-2014 |
| Periodicidad | semanal |
| Municipios con registros | 340 |
| Desagregación | clasificación, sexo, edad, embarazo o puerperio |
| Filas | 1.259.724 |

Valores de `clasificacion` (clasificación):

- desnutrición grave (2008-2014)
- desnutrición leve (2008-2014)
- desnutrición moderada (2008-2014)
- normal (2008-2014)
- obesidad (2008-2014)
- sobrepeso (2008-2014)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2008-2014 | 2-11m, 1, 2-4 |

Total por gestión:

| Gestión | Personas |
| ---: | ---: |
| 2008 | 2.523.669 |
| 2009 | 2.558.893 |
| 2010 | 2.291.515 |
| 2011 | 2.111.206 |
| 2012 | 1.820.798 |
| 2013 | 1.836.080 |
| 2014 | 1.792.347 |

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
| `condicion` | string | embarazada o puerpera. |
| `personas` | integer | Número de personas en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(personas) as personas
from 'datos/vigilancia/estado_nutricional/peso_2008_2014/datos.parquet'
group by gestion order by gestion;

-- Por gestión y clasificacion
select gestion, clasificacion, sum(personas) as personas
from 'datos/vigilancia/estado_nutricional/peso_2008_2014/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(personas) as personas
from 'datos/vigilancia/estado_nutricional/peso_2008_2014/datos.parquet'
where gestion = 2014 group by all order by personas desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Peso para la edad (2005-2006)](../../../vigilancia/estado_nutricional/peso_2005_2006/readme.md): 2005-2006, formulario 302.
- [Peso para la edad (2007)](../../../vigilancia/estado_nutricional/peso_2007/readme.md): 2007, formulario 302.
- Peso para la edad (2008-2014) (este dataset): 2008-2014, formulario 302.
- [Peso para la edad (2015-2025)](../../../vigilancia/estado_nutricional/peso_2015_2025/readme.md): 2015-2025, formulario 302b.

Las categorías de `clasificacion` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(personas) as personas
from read_parquet([
    'datos/vigilancia/estado_nutricional/peso_2005_2006/datos.parquet',
    'datos/vigilancia/estado_nutricional/peso_2007/datos.parquet',
    'datos/vigilancia/estado_nutricional/peso_2008_2014/datos.parquet',
    'datos/vigilancia/estado_nutricional/peso_2015_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2008-2009 | 302 | 47 Obesidad (O); 48 Sobrepeso (S); 49 Nutrición Normal (N); 50 Desnutrición leve (L); 51 Desnutrición moderada (M); 52 Desnutrición grave (G) | 1.0.4 (2013) |
| 2010-2013 | 302 | Desnutrición grave (G); Desnutrición leve (L); Desnutrición moderada (M); Nutrición Normal (N); Obesidad (O); Sobrepeso (S) | 1.0.4 (2013) |
| 2014 | 302 | Desnutrición grave (G); Desnutrición leve (L); Desnutrición moderada (M); Nutrición Normal (N); Obesidad (O); Sobrepeso (S) | 2.0.0 (2014) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302 (grupos 11 y 14, 2008-2014) y 302b (grupos 06 y 07): SOAPS cuenta la columna "Menor de 1 año" desde los 2 meses (reglas de 2 a 11 meses).
