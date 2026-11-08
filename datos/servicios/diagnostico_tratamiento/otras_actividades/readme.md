# Otras actividades

Estudios y procedimientos realizados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2025. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2025 |
| Periodicidad | mensual |
| Municipios con registros | 343 |
| Desagregación |  |
| Filas | 40.319 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2015 | 25.067.516 |
| 2016 | 25.591.558 |
| 2017 | 29.964.384 |
| 2018 | 35.522.268 |
| 2019 | 38.526.232 |
| 2020 | 36.901.094 |
| 2021 | 50.111.388 |
| 2022 | 75.099.327 |
| 2023 | 82.097.460 |
| 2024 | 92.704.262 |
| 2025 | 61.398.121 |

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
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/diagnostico_tratamiento/otras_actividades/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/diagnostico_tratamiento/otras_actividades/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Otras actividades (este dataset): 2015-2025, formulario 301a.
- [Otras actividades (formulario 301b)](../../../servicios/diagnostico_tratamiento/otras_actividades_301b/readme.md): 2024-2025, formulario 301b.

El formulario 301a registra los servicios de primer nivel y el 301b, los de segundo y tercer nivel: son registros complementarios, no partes de un total. Sumarlos supone que ninguna atención se registra en los dos.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/diagnostico_tratamiento/otras_actividades/datos.parquet',
    'datos/servicios/diagnostico_tratamiento/otras_actividades_301b/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015 | 301a | Otras actividades | 3.0.1 (2016) |
| 2016 | 301a | Otras actividades | 3.0.2 (2016) |
| 2017 | 301a | Otras actividades | 4.0.0 (2018) |
| 2018 | 301a | Otras actividades | 4.0.1 (2018) |
| 2019-2020 | 301a | Otras actividades | 5.0.1 (2020) |
| 2021 | 301a | Otras actividades | 6.0.0 (2021) |
| 2022-2023 | 301a | Otras actividades | 6.0.1 (2022) |
| 2024-2025 | 301a | Otras actividades | 7.0.1 (2026) |
