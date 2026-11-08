# Dengue grave (2015-2018)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2015-2018. Fuente: SNIS, formularios 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2018 |
| Periodicidad | semanal |
| Municipios con registros | 29 |
| Desagregación | clasificación, sexo, edad |
| Filas | 229 |

Valores de `clasificacion` (clasificación):

- grave (2015-2018)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015 | 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2016-2018 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2015 | 86 |
| 2016 | 61 |
| 2017 | 68 |
| 2018 | 41 |

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
| `clasificacion` | string | Clasificación. |
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/dengue_2015_2018/datos.parquet'
group by gestion order by gestion;

-- Por gestión y clasificacion
select gestion, clasificacion, sum(casos) as casos
from 'datos/vigilancia/casos/dengue_2015_2018/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/dengue_2015_2018/datos.parquet'
where gestion = 2018 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Dengue hemorrágico (2002-2004)](../../../vigilancia/casos/dengue_2002_2004/readme.md): 2002-2004, formulario 302.
- [Dengue por clasificación clínica (2005-2014)](../../../vigilancia/casos/dengue_2005_2014/readme.md): 2005-2014, formulario 302.
- Dengue grave (2015-2018) (este dataset): 2015-2018, formulario 302a.
- [Dengue por clasificación clínica (2019-2025)](../../../vigilancia/casos/dengue_2019_2025/readme.md): 2019-2025, formulario 302a.

Las categorías de `clasificacion` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/dengue_2002_2004/datos.parquet',
    'datos/vigilancia/casos/dengue_2005_2014/datos.parquet',
    'datos/vigilancia/casos/dengue_2015_2018/datos.parquet',
    'datos/vigilancia/casos/dengue_2019_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

- [Dengue (sección enfermedades metaxénicas)](../../../vigilancia/casos/dengue_seccion_metaxenicas/readme.md): 2001-2020, formulario 302, 302a.
- [Dengue hemorrágico (2002-2004)](../../../vigilancia/casos/dengue_2002_2004/readme.md): 2002-2004, formulario 302.
- [Dengue por clasificación clínica (2005-2014)](../../../vigilancia/casos/dengue_2005_2014/readme.md): 2005-2014, formulario 302.
- Dengue grave (2015-2018) (este dataset): 2015-2018, formulario 302a.
- [Dengue por clasificación clínica (2019-2025)](../../../vigilancia/casos/dengue_2019_2025/readme.md): 2019-2025, formulario 302a.

El formulario registra el dengue en dos secciones, con cifras distintas: enfermedades metaxénicas (2001-2004 y 2015-2020), sin clasificación clínica, y dengue por clasificación clínica. En 2015-2018 la clasificación clínica sólo tiene dengue grave: la mayoría de los casos de esos años está en la sección de enfermedades metaxénicas. No las sume: un caso puede estar en ambas.

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2015 | 302a | Dengue grave | 3.0.1 (2016) | A91 |
| 2016 | 302a | Dengue grave | 3.0.2 (2016) | A91 |
| 2017 | 302a | Dengue grave | 4.0.0 (2018) | A91 |
| 2018 | 302a | Dengue grave | 4.0.1 (2018) | A91 |
