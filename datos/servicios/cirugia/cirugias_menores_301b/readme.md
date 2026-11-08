# Cirugias menores (formulario 301b)

Registros en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2023. Fuente: SNIS, formularios 301b.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2023 |
| Periodicidad | mensual |
| Municipios con registros | 69 |
| Desagregación | sexo |
| Filas | 8.644 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2015 | 47.744 |
| 2016 | 50.621 |
| 2017 | 54.794 |
| 2018 | 57.911 |
| 2019 | 52.282 |
| 2020 | 31.595 |
| 2021 | 38.118 |
| 2022 | 48.185 |
| 2023 | 59.507 |

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
| `sexo` | string | mujer u hombre. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/cirugia/cirugias_menores_301b/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/cirugia/cirugias_menores_301b/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/cirugia/cirugias_menores_301b/datos.parquet'
where gestion = 2023 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Cirugias menores (formulario 301b) (este dataset): 2015-2023, formulario 301b.
- [Cirugias menores realizadas](../../../servicios/cirugia/cirugias_menores/readme.md): 2024-2025, formulario 301a.

El formulario 301a registra los servicios de primer nivel y el 301b, los de segundo y tercer nivel: son registros complementarios, no partes de un total. Sumarlos supone que ninguna atención se registra en los dos.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/cirugia/cirugias_menores_301b/datos.parquet',
    'datos/servicios/cirugia/cirugias_menores/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015-2023 | 301b | N° de Cirugias menores |  |
