# Vacuna Antipoliomielítica (2010-2025)

Dosis aplicadas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2010-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2010-2025 |
| Periodicidad | mensual |
| Municipios con registros | 344 |
| Desagregación | dosis, sexo, edad, lugar |
| Filas | 912.969 |

Valores de `dosis` (dosis):

- 1 (2010-2025)
- 2 (2010-2025)
- 3 (2010-2025)
- 4 (2010-2025)
- 5 (2010-2025)

Valores de `lugar` (lugar):

- dentro (2010-2013, 2015-2025)
- fuera (2010-2013, 2015-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2010-2014 | <1, 1, 2-4, 4 |
| 2015-2023 | <1, 1, 2-3, 4 |
| 2024-2025 | <1, 1, 2, 3, 4 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2010 | 768.355 |
| 2011 | 841.086 |
| 2012 | 834.627 |
| 2013 | 915.092 |
| 2014 | 959.017 |
| 2015 | 947.000 |
| 2016 | 910.756 |
| 2017 | 870.705 |
| 2018 | 890.722 |
| 2019 | 854.505 |
| 2020 | 771.224 |
| 2021 | 754.824 |
| 2022 | 758.207 |
| 2023 | 749.326 |
| 2024 | 762.875 |
| 2025 | 736.903 |

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
| `dosis` | string | Dosis: número (1 a 5), inicial, única, anual o refuerzo. |
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/antipoliomielitica_2010_2025/datos.parquet'
group by gestion order by gestion;

-- Por gestión y dosis
select gestion, dosis, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/antipoliomielitica_2010_2025/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/antipoliomielitica_2010_2025/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Vacuna Antipoliomielítica (2001-2003)](../../../servicios/vacunas/antipoliomielitica_2001_2003/readme.md): 2001-2003, formulario 301.
- [Vacuna Antipoliomielítica (2004-2009)](../../../servicios/vacunas/antipoliomielitica_2004_2009/readme.md): 2004-2009, formulario 301.
- Vacuna Antipoliomielítica (2010-2025) (este dataset): 2010-2025, formulario 301, 301a.

Las categorías de `dosis` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/vacunas/antipoliomielitica_2001_2003/datos.parquet',
    'datos/servicios/vacunas/antipoliomielitica_2004_2009/datos.parquet',
    'datos/servicios/vacunas/antipoliomielitica_2010_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2010-2011 | 301 | (O.P.V.) Antipoliomielítica 1ra dosis; (O.P.V.) Antipoliomielítica 2da dosis; (O.P.V.) Antipoliomielítica 3ra dosis; Antipoliomielitica 5ta dosis; Antipoliomielítica 1ra dosis; Antipoliomielítica 2da dosis; Antipoliomielítica 3ra dosis; Antipoliomielítica 4ta dosis | 1.0.4 (2013) |
| 2012 | 301 | l 17.5 (O.P.V.) Antipoliomielítica 1ra dosis; l 17.6 (O.P.V.) Antipoliomielítica 2da dosis; l 17.7 (O.P.V.) Antipoliomielítica 3ra dosis; l 18.7 Antipoliomielítica 1ra dosis; l 18.8 Antipoliomielítica 2da dosis; l 18.9 Antipoliomielítica 3ra dosis; l 1810 Antipoliomielítica 4ta dosis; l 19.5 Antipoliomielítica 1ra dosis; l 19.6 Antipoliomielítica 2da dosis; l 19.7 Antipoliomielítica 3ra dosis; l 19.8 Antipoliomielítica 4ta dosis; l 20.2 Antipoliomielitica 5ta dosis | 1.0.4 (2013) |
| 2013 | 301 | (O.P.V.) Antipoliomielítica 1ra dosis; (O.P.V.) Antipoliomielítica 2da dosis; (O.P.V.) Antipoliomielítica 3ra dosis; Antipoliomielitica 5ta dosis; Antipoliomielítica 1ra dosis; Antipoliomielítica 2da dosis; Antipoliomielítica 3ra dosis; Antipoliomielítica 4ta dosis | 1.0.4 (2013) |
| 2014 | 301 | 17.5 (O.P.V.) Antipoliomielítica 1ra dosis; 17.6 (O.P.V.) Antipoliomielítica 2da dosis; 17.7 (O.P.V.) Antipoliomielítica 3ra dosis; 18.7 Antipoliomielítica 1ra dosis; 18.8 Antipoliomielítica 2da dosis; 18.9 Antipoliomielítica 3ra dosis; 1810 Antipoliomielítica 4ta dosis; 19.5 Antipoliomielítica 1ra dosis; 19.6 Antipoliomielítica 2da dosis; 19.7 Antipoliomielítica 3ra dosis; 19.8 Antipoliomielítica 4ta dosis; 20.2 Antipoliomielitica 5ta dosis | 2.0.0 (2014) |
| 2015 | 301a | Total Antipoliomielítica 1ra dosis; Total Antipoliomielítica 2da dosis; Total Antipoliomielítica 3ra dosis; Total Antipoliomielítica 4ta. dosis (1er. refuerzo); Total Antipoliomielítica 5ta. dosis (2do. refuerzo) | 3.0.1 (2016) |
| 2016 | 301a | Antipoliomielítica 1ra dosis; Antipoliomielítica 2da dosis; Antipoliomielítica 3ra dosis; Antipoliomielítica 4ta. dosis (1er. refuerzo); Antipoliomielítica 5ta. dosis (2do. refuerzo) | 3.0.2 (2016) |
| 2017 | 301a | Antipoliomielítica 1ra dosis; Antipoliomielítica 2da dosis; Antipoliomielítica 3ra dosis; Antipoliomielítica 4ta. dosis (1er. refuerzo); Antipoliomielítica 5ta. dosis (2do. refuerzo) | 4.0.0 (2018) |
| 2018 | 301a | Antipoliomielítica 1ra dosis; Antipoliomielítica 2da dosis; Antipoliomielítica 3ra dosis; Antipoliomielítica 4ta. Dosis; Antipoliomielítica 4ta. dosis; Antipoliomielítica 5ta. dosis | 4.0.1 (2018) |
| 2019-2020 | 301a | Antipoliomielítica 1ra dosis; Antipoliomielítica 2da dosis; Antipoliomielítica 3ra dosis; Antipoliomielítica 4ta. Dosis; Antipoliomielítica 4ta. dosis; Antipoliomielítica 5ta. dosis | 5.0.1 (2020) |
| 2021 | 301a | Antipoliomielítica 1ra dosis; Antipoliomielítica 2da dosis; Antipoliomielítica 3ra dosis; Antipoliomielítica 4ta. Dosis; Antipoliomielítica 4ta. dosis; Antipoliomielítica 5ta. dosis | 6.0.0 (2021) |
| 2022-2023 | 301a | Antipoliomielítica 1ra dosis; Antipoliomielítica 2da dosis; Antipoliomielítica 3ra dosis; Antipoliomielítica 4ta. Dosis; Antipoliomielítica 4ta. dosis; Antipoliomielítica 5ta. dosis | 6.0.1 (2022) |
| 2024-2025 | 301a | Antipoliomelitica 1ra Dosis; Antipoliomelitica 2da Dosis; Antipoliomelitica 3ra Dosis; Antipoliomelitica 4ta Dosis; Antipoliomelitica 5ta Dosis | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 301a, vacunas de 12 a 23 meses, de 2 a 3 años y de 4 años, 2015-2023: el segundo nivel dice DENTRO/FUERA otra vez, pero las reglas de SOAPS 6.0.1 dividen estas variables por sexo y lugar (código 3012805). El segundo nivel "DENTRO" suma 50,6 % y la proporción de varones en las vacunas rotuladas por sexo es 50,9 %: DENTRO es hombre y FUERA es mujer.
- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
