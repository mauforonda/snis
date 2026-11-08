# Consultas prenatales (2001-2023)

Atenciones y nacimientos registrados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2023. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2023 |
| Periodicidad | mensual |
| Municipios con registros | 343 |
| Desagregación | momento, edad, lugar |
| Filas | 534.361 |

Valores de `momento` (momento):

- nueva antes del 5.º mes (2001-2023)
- nueva desde el 5.º mes (2001-2023)
- repetida (2001-2023)

Valores de `lugar` (lugar):

- dentro (2010-2013, 2015-2023)
- fuera (2010-2013, 2015-2023)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015-2023 | <15, 15-19, 20-34, 35-49, 50+ |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 785.547 |
| 2002 | 850.348 |
| 2003 | 904.948 |
| 2004 | 945.130 |
| 2005 | 996.419 |
| 2006 | 1.072.984 |
| 2007 | 1.070.755 |
| 2008 | 1.091.458 |
| 2009 | 1.222.455 |
| 2010 | 1.266.809 |
| 2011 | 1.260.008 |
| 2012 | 1.176.389 |
| 2013 | 1.271.159 |
| 2014 | 1.286.632 |
| 2015 | 1.332.575 |
| 2016 | 1.323.305 |
| 2017 | 1.262.716 |
| 2018 | 1.254.508 |
| 2019 | 1.168.294 |
| 2020 | 899.899 |
| 2021 | 1.017.396 |
| 2022 | 1.021.344 |
| 2023 | 998.242 |

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
| `momento` | string | Momento de la consulta prenatal. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/consulta_prenatal_2001_2023/datos.parquet'
group by gestion order by gestion;

-- Por gestión y momento
select gestion, momento, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/consulta_prenatal_2001_2023/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/consulta_prenatal_2001_2023/datos.parquet'
where gestion = 2023 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Consultas prenatales (2001-2023) (este dataset): 2001-2023, formulario 301, 301a.
- [Consultas prenatales (2024-2025)](../../../servicios/salud_materna_neonatal/consulta_prenatal_2024_2025/readme.md): 2024-2025, formulario 301a.

Las categorías de `momento` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/salud_materna_neonatal/consulta_prenatal_2001_2023/datos.parquet',
    'datos/servicios/salud_materna_neonatal/consulta_prenatal_2024_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2007 | 301 | Nuevas a partir del 5to mes de embarazo; Nuevas antes del 5to mes de embarazo; Repetidas |  |
| 2008-2013 | 301 | Nuevas a partir del 5to mes de embarazo; Nuevas antes del 5to mes de embarazo; Repetidas | 1.0.4 (2013) |
| 2014 | 301 | 4.1 Nuevas antes del 5to mes de embarazo; 4.2 Nuevas a partir del 5to mes de embarazo; 4.3 Repetidas | 2.0.0 (2014) |
| 2015-2023 | 301a | Nuevas a partir del 5to mes de embarazo; Nuevas antes del 5to mes de embarazo; Repetidas |  |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
