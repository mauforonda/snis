# Vacuna COVID-19 (2021)

Dosis aplicadas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2021. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2021 |
| Periodicidad | mensual |
| Municipios con registros | 341 |
| Desagregación | dosis, sexo, lugar |
| Filas | 24.748 |

Valores de `dosis` (dosis):

- 1 (2021)
- 2 (2021)
- refuerzo (2021)
- única (2021)

Valores de `lugar` (lugar):

- dentro (2021)
- fuera (2021)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2021 | 8.639.202 |

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
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/covid_19_2021/datos.parquet'
group by gestion order by gestion;

-- Por gestión y dosis
select gestion, dosis, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/covid_19_2021/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/covid_19_2021/datos.parquet'
where gestion = 2021 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Vacuna COVID-19 (2021) (este dataset): 2021, formulario 301a.
- [Vacuna COVID-19 (2022)](../../../servicios/vacunas/covid_19_2022/readme.md): 2022, formulario 301a.
- [Vacuna COVID-19 (2023)](../../../servicios/vacunas/covid_19_2023/readme.md): 2023, formulario 301a.
- [Vacuna COVID-19 (2024-2025)](../../../servicios/vacunas/covid_19_2024_2025/readme.md): 2024-2025, formulario 301a.

Las categorías de `dosis` y `grupo` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/vacunas/covid_19_2021/datos.parquet',
    'datos/servicios/vacunas/covid_19_2022/datos.parquet',
    'datos/servicios/vacunas/covid_19_2023/datos.parquet',
    'datos/servicios/vacunas/covid_19_2024_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2021 | 301a | 17.23 COVID 1ra Dosis; 17.24 COVID 2da Dosis; 17.25 COVID Dosis Unica; 17.26 COVID Dosis de Refuerzo | 6.0.0 (2021), 6.0.1 (2022) |
