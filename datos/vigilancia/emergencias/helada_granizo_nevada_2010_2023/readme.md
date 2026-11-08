# Helada, granizo o nevada (2010-2023)

Eventos y personas afectadas en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2010-2023. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2010-2023 |
| Periodicidad | semanal |
| Municipios con registros | 143 |
| Desagregación | medida |
| Filas | 1.170 |

Valores de `medida` (medida):

- eventos (2010-2015)
- personas_afectadas (2010-2015)
- personas_fallecidas (2010-2013)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2010 | 6.661 |
| 2011 | 5.515 |
| 2012 | 3.723 |
| 2013 | 32.004 |
| 2014 | 9.944 |
| 2015 | 4.849 |
| 2016 | 11.851 |
| 2017 | 6.798 |
| 2018 | 12.466 |
| 2019 | 13.626 |
| 2020 | 13.101 |
| 2021 | 11.663 |
| 2022 | 16.455 |
| 2023 | 10.251 |

## Cómo utilizar

Cada fila da el número de cantidad de un periodo, un municipio y una población. Para obtener un total, sume las filas: el dataset no tiene filas de total. Una combinación sin fila significa que no hubo registros. Las convenciones de tiempo, territorio y población están en el [catálogo](../../../README.md#cómo-leer-los-datos).

| Columna | Tipo | Descripción |
| --- | --- | --- |
| `gestion` | integer | Año calendario (gestión) del registro. |
| `semana` | integer | Semana epidemiológica, de 1 a 53. Va de domingo a sábado. |
| `fecha_inicio` | date | Primer día de la semana o del mes. |
| `departamento` | string | Nombre del departamento. |
| `municipio` | string | Nombre del municipio. |
| `municipio_codigo` | string | Código del municipio, 6 dígitos: departamento (2), provincia (2) y municipio (2). |
| `medida` | string | Qué se cuenta: eventos, personas afectadas, fallecidas, damnificadas o pacientes atendidos. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/vigilancia/emergencias/helada_granizo_nevada_2010_2023/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/vigilancia/emergencias/helada_granizo_nevada_2010_2023/datos.parquet'
where gestion = 2023 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Helada, granizo o nevada (2010-2023) (este dataset): 2010-2023, formulario 302, 302a.
- [Helada, granizo y nevada (2024)](../../../vigilancia/emergencias/helada_granizo_nevada_2024/readme.md): 2024, formulario 302a.
- [Helada, granizo y nevada (2025)](../../../vigilancia/emergencias/helada_granizo_nevada_2025/readme.md): 2025, formulario 302a.

Las categorías de `evento` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/vigilancia/emergencias/helada_granizo_nevada_2010_2023/datos.parquet',
    'datos/vigilancia/emergencias/helada_granizo_nevada_2024/datos.parquet',
    'datos/vigilancia/emergencias/helada_granizo_nevada_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2010-2013 | 302 | Helada/Granizo/nevada | 1.0.4 (2013) |
| 2014 | 302 | Helada/Granizo/nevada | 2.0.0 (2014) |
| 2015 | 302a | Helada/granizo/nevada |  |
| 2016 | 302a | Helada/granizo/nevada | 3.0.2 (2016) |
| 2017 | 302a | Helada/granizo/nevada | 4.0.0 (2018) |
| 2018 | 302a | Helada/granizo/nevada | 4.0.1 (2018) |
| 2019-2020 | 302a | Helada/granizo/nevada | 5.0.1 (2020) |
| 2021 | 302a | Helada/granizo/nevada | 6.0.0 (2021) |
| 2022-2023 | 302a | Helada/granizo/nevada | 6.0.1 (2022) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
