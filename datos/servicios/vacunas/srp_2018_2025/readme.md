# Vacuna SRP (sarampión, rubéola y parotiditis) (2018-2025)

Dosis aplicadas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2018-2025. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2018-2025 |
| Periodicidad | mensual |
| Municipios con registros | 343 |
| Desagregación | dosis, sexo, edad, lugar |
| Filas | 271.232 |

Valores de `dosis` (dosis):

- 1 (2018-2025)
- 2 (2018-2025)

Valores de `lugar` (lugar):

- dentro (2018-2025)
- fuera (2018-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2018-2023 | 1, 2-3, 4 |
| 2024-2025 | 1, 2, 3, 4 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2018 | 401.027 |
| 2019 | 376.650 |
| 2020 | 348.074 |
| 2021 | 385.284 |
| 2022 | 332.422 |
| 2023 | 331.470 |
| 2024 | 374.512 |
| 2025 | 355.930 |

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
from 'datos/servicios/vacunas/srp_2018_2025/datos.parquet'
group by gestion order by gestion;

-- Por gestión y dosis
select gestion, dosis, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/srp_2018_2025/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/srp_2018_2025/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Vacuna SRP (sarampión, rubéola y parotiditis) (2001-2009)](../../../servicios/vacunas/srp_2001_2009/readme.md): 2001-2009, formulario 301.
- [Vacuna SRP (sarampión, rubéola y parotiditis) (2010-2017)](../../../servicios/vacunas/srp_2010_2017/readme.md): 2010-2017, formulario 301, 301a.
- Vacuna SRP (sarampión, rubéola y parotiditis) (2018-2025) (este dataset): 2018-2025, formulario 301a.

Las categorías de `dosis` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/vacunas/srp_2001_2009/datos.parquet',
    'datos/servicios/vacunas/srp_2010_2017/datos.parquet',
    'datos/servicios/vacunas/srp_2018_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2018 | 301a | SRP 1ra. Dosis; SRP 1ra. dosis; SRP 2da. Dosis | 4.0.1 (2018) |
| 2019-2020 | 301a | SRP 1ra. Dosis; SRP 1ra. dosis; SRP 2da. Dosis | 5.0.1 (2020) |
| 2021 | 301a | SRP 1ra. Dosis; SRP 1ra. dosis; SRP 2da. Dosis | 6.0.0 (2021) |
| 2022-2023 | 301a | SRP 1ra. Dosis; SRP 1ra. dosis; SRP 2da. Dosis | 6.0.1 (2022) |
| 2024-2025 | 301a | SRP 1ra Dosis; SRP 2da Dosis | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 301a, vacunas de 12 a 23 meses, de 2 a 3 años y de 4 años, 2015-2023: el segundo nivel dice DENTRO/FUERA otra vez, pero las reglas de SOAPS 6.0.1 dividen estas variables por sexo y lugar (código 3012805). El segundo nivel "DENTRO" suma 50,6 % y la proporción de varones en las vacunas rotuladas por sexo es 50,9 %: DENTRO es hombre y FUERA es mujer.
