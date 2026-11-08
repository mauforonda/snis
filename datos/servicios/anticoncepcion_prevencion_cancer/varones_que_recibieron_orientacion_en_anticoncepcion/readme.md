# Varones que recibieron orientación en anticoncepción

Atenciones registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2021-2025. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2021-2025 |
| Periodicidad | mensual |
| Municipios con registros | 337 |
| Desagregación | edad |
| Filas | 22.894 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2021-2023 | <15, 15-19, 20-34, 35-49, 50+ |
| 2024-2025 | <10, 10-14, 15-19, 20-34, 35-49, 50+ |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2021 | 42.694 |
| 2022 | 71.928 |
| 2023 | 71.491 |
| 2024 | 72.810 |
| 2025 | 78.664 |

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
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/anticoncepcion_prevencion_cancer/varones_que_recibieron_orientacion_en_anticoncepcion/datos.parquet'
group by gestion order by gestion;

-- Por gestión y edad_grupo
select gestion, edad_grupo, sum(cantidad) as cantidad
from 'datos/servicios/anticoncepcion_prevencion_cancer/varones_que_recibieron_orientacion_en_anticoncepcion/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/anticoncepcion_prevencion_cancer/varones_que_recibieron_orientacion_en_anticoncepcion/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Personas que recibieron orientación en anticoncepción](../../../servicios/anticoncepcion_prevencion_cancer/personas_que_recibieron_orientacion_en_anticoncepcion/readme.md): 2001-2020, formulario 301, 301a.
- [Mujeres que recibieron orientación en anticoncepción](../../../servicios/anticoncepcion_prevencion_cancer/mujeres_que_recibieron_orientacion_en_anticoncepcion/readme.md): 2021-2025, formulario 301a.
- Varones que recibieron orientación en anticoncepción (este dataset): 2021-2025, formulario 301a.

Hasta 2020 el formulario cuenta personas que recibieron orientación en anticoncepción; desde 2021, mujeres y varones por separado. Consultarlos juntos como una serie supone que mujeres y varones suman lo mismo que "personas".

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/anticoncepcion_prevencion_cancer/personas_que_recibieron_orientacion_en_anticoncepcion/datos.parquet',
    'datos/servicios/anticoncepcion_prevencion_cancer/mujeres_que_recibieron_orientacion_en_anticoncepcion/datos.parquet',
    'datos/servicios/anticoncepcion_prevencion_cancer/varones_que_recibieron_orientacion_en_anticoncepcion/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2021 | 301a | Número de varones que recibieron orientación en Anticoncepción | 6.0.0 (2021) |
| 2022-2023 | 301a | Número de varones que recibieron orientación en Anticoncepción | 6.0.1 (2022) |
| 2024-2025 | 301a | Número de varones que recibieron orientación en Anticoncepción | 7.0.1 (2026) |
