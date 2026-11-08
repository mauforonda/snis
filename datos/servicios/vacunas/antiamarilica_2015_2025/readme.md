# Vacuna Antiamarílica (2015-2025)

Dosis aplicadas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2025. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2025 |
| Periodicidad | mensual |
| Municipios con registros | 343 |
| Desagregación | dosis, sexo, edad, lugar |
| Filas | 204.037 |

Valores de `dosis` (dosis):

- única (2015-2025)

Valores de `lugar` (lugar):

- dentro (2015-2025)
- fuera (2015-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015-2017 | 1, 2-3 |
| 2018-2023 | 1, 2-3, 4 |
| 2024-2025 | 1, 2, 3, 4, 5-9, 10, 11, 12-20, 21-59 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2015 | 222.589 |
| 2016 | 225.362 |
| 2017 | 205.304 |
| 2018 | 216.507 |
| 2019 | 204.317 |
| 2020 | 182.859 |
| 2021 | 219.276 |
| 2022 | 307.046 |
| 2023 | 360.458 |
| 2024 | 318.275 |
| 2025 | 297.595 |

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
from 'datos/servicios/vacunas/antiamarilica_2015_2025/datos.parquet'
group by gestion order by gestion;

-- Por gestión y dosis
select gestion, dosis, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/antiamarilica_2015_2025/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/antiamarilica_2015_2025/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Vacuna Antiamarílica (2001-2014)](../../../servicios/vacunas/antiamarilica_2001_2014/readme.md): 2001-2014, formulario 301.
- Vacuna Antiamarílica (2015-2025) (este dataset): 2015-2025, formulario 301a.

Las categorías de `dosis` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/vacunas/antiamarilica_2001_2014/datos.parquet',
    'datos/servicios/vacunas/antiamarilica_2015_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015 | 301a | Total Antiamarílica dosis única | 3.0.1 (2016) |
| 2016 | 301a | Antiamarílica dosis única | 3.0.2 (2016) |
| 2017 | 301a | Antiamarílica dosis única | 4.0.0 (2018) |
| 2018 | 301a | Antiamarilica dosis unica; Antiamarílica dosis única | 4.0.1 (2018) |
| 2019-2020 | 301a | Antiamarilica dosis unica; Antiamarílica dosis única | 5.0.1 (2020) |
| 2021 | 301a | 17.22 Antiamarílica ( dosis única); Antiamarilica dosis unica; Antiamarílica dosis única | 6.0.0 (2021) |
| 2022-2023 | 301a | 17.22 Antiamarílica ( dosis única); Antiamarilica dosis unica; Antiamarílica dosis única | 6.0.1 (2022) |
| 2024-2025 | 301a | Antiamarilica Dosis Unica; Antiamarilica Dosis unica | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 301a, vacunas de 12 a 23 meses, de 2 a 3 años y de 4 años, 2015-2023: el segundo nivel dice DENTRO/FUERA otra vez, pero las reglas de SOAPS 6.0.1 dividen estas variables por sexo y lugar (código 3012805). El segundo nivel "DENTRO" suma 50,6 % y la proporción de varones en las vacunas rotuladas por sexo es 50,9 %: DENTRO es hombre y FUERA es mujer.
