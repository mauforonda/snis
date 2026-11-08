# Vacuna VPH (virus del papiloma humano) (2018-2023)

Dosis aplicadas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2018-2023. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2018-2023 |
| Periodicidad | mensual |
| Municipios con registros | 342 |
| Desagregación | dosis, grupo de población, sexo, lugar |
| Filas | 27.962 |

Valores de `dosis` (dosis):

- 1 (2018-2023)
- 2 (2018-2023)

Valores de `grupo` (grupo de población):

- niñas de 10 años (2018-2023)

Valores de `lugar` (lugar):

- dentro (2018-2023)
- fuera (2018-2023)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2018 | 152.530 |
| 2019 | 171.042 |
| 2020 | 96.470 |
| 2021 | 110.290 |
| 2022 | 143.780 |
| 2023 | 92.073 |

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
| `grupo` | string | Grupo de población al que se dirige la vacuna. |
| `sexo` | string | mujer u hombre. |
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/vph_2018_2023/datos.parquet'
group by gestion order by gestion;

-- Por gestión y dosis
select gestion, dosis, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/vph_2018_2023/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/vph_2018_2023/datos.parquet'
where gestion = 2023 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Vacuna VPH (virus del papiloma humano) (2018-2023) (este dataset): 2018-2023, formulario 301a.
- [Vacuna VPH (virus del papiloma humano) (2024-2025)](../../../servicios/vacunas/vph_2024_2025/readme.md): 2024-2025, formulario 301a.

Las categorías de `dosis` y `grupo` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/vacunas/vph_2018_2023/datos.parquet',
    'datos/servicios/vacunas/vph_2024_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2018 | 301a | VPH (niñas que cumpliran 10 años) 1ra. Dosis; VPH (niñas que cumpliran 10 años) 2da. Dosis | 4.0.1 (2018) |
| 2019-2020 | 301a | VPH (niñas que cumpliran 10 años) 1ra. Dosis; VPH (niñas que cumpliran 10 años) 2da. Dosis | 5.0.1 (2020) |
| 2021 | 301a | VPH (niñas que cumpliran 10 años) 1ra. Dosis; VPH (niñas que cumpliran 10 años) 2da. Dosis | 6.0.0 (2021) |
| 2022-2023 | 301a | VPH (niñas que cumpliran 10 años) 1ra. Dosis; VPH (niñas que cumpliran 10 años) 2da. Dosis | 6.0.1 (2022) |
