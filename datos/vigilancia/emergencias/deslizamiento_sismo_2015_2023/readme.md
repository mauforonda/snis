# Deslizamiento, sismo o terremoto (2015-2023)

Eventos y personas afectadas en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2015-2023. Fuente: SNIS, formularios 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2023 |
| Periodicidad | semanal |
| Municipios con registros | 50 |
| Desagregación | evento, medida |
| Filas | 137 |

Valores de `evento` (evento):

- deslizamiento o sismo (2015-2023)

Valores de `medida` (medida):

- eventos (2015)
- personas_afectadas (2015)
- personas_fallecidas (2015)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2015 | 200 |
| 2016 | 68 |
| 2017 | 953 |
| 2018 | 1.054 |
| 2019 | 1.000 |
| 2020 | 173 |
| 2021 | 132 |
| 2022 | 40 |
| 2023 | 152 |

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
| `evento` | string | Tipo de evento. |
| `medida` | string | Qué se cuenta: eventos, personas afectadas, fallecidas, damnificadas o pacientes atendidos. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/vigilancia/emergencias/deslizamiento_sismo_2015_2023/datos.parquet'
group by gestion order by gestion;

-- Por gestión y evento
select gestion, evento, sum(cantidad) as cantidad
from 'datos/vigilancia/emergencias/deslizamiento_sismo_2015_2023/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/vigilancia/emergencias/deslizamiento_sismo_2015_2023/datos.parquet'
where gestion = 2023 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Deslizamiento (2010-2014)](../../../vigilancia/emergencias/deslizamiento_sismo_2010_2014/readme.md): 2010-2014, formulario 302.
- Deslizamiento, sismo o terremoto (2015-2023) (este dataset): 2015-2023, formulario 302a.
- [Deslizamiento (2024)](../../../vigilancia/emergencias/deslizamiento_sismo_2024/readme.md): 2024, formulario 302a.
- [Deslizamiento y sismo (2025)](../../../vigilancia/emergencias/deslizamiento_sismo_2025/readme.md): 2025, formulario 302a.

Las categorías de `evento` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/vigilancia/emergencias/deslizamiento_sismo_2010_2014/datos.parquet',
    'datos/vigilancia/emergencias/deslizamiento_sismo_2015_2023/datos.parquet',
    'datos/vigilancia/emergencias/deslizamiento_sismo_2024/datos.parquet',
    'datos/vigilancia/emergencias/deslizamiento_sismo_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015 | 302a | Deslizamiento/Sismo/Terremoto |  |
| 2016 | 302a | Deslizamiento/Sismo/Terremoto | 3.0.2 (2016) |
| 2017 | 302a | Deslizamiento/Sismo/Terremoto | 4.0.0 (2018) |
| 2018 | 302a | Deslizamiento/Sismo/Terremoto | 4.0.1 (2018) |
| 2019-2020 | 302a | Deslizamiento/Sismo/Terremoto | 5.0.1 (2020) |
| 2021 | 302a | Deslizamiento/Sismo/Terremoto | 6.0.0 (2021) |
| 2022-2023 | 302a | Deslizamiento/Sismo/Terremoto | 6.0.1 (2022) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
