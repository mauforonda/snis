# Seciones de fisioterapia realizadas

Estudios y procedimientos realizados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2023. Fuente: SNIS, formularios 301b.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2023 |
| Periodicidad | mensual |
| Municipios con registros | 54 |
| Desagregación | sexo |
| Filas | 8.285 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2015 | 708.559 |
| 2016 | 941.309 |
| 2017 | 1.466.152 |
| 2018 | 1.383.999 |
| 2019 | 1.461.641 |
| 2020 | 769.106 |
| 2021 | 1.404.590 |
| 2022 | 1.770.044 |
| 2023 | 2.425.478 |

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
from 'datos/servicios/diagnostico_tratamiento/sesiones_de_fisioterapia_realizadas/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/diagnostico_tratamiento/sesiones_de_fisioterapia_realizadas/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/diagnostico_tratamiento/sesiones_de_fisioterapia_realizadas/datos.parquet'
where gestion = 2023 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Seciones de fisioterapia realizadas (este dataset): 2015-2023, formulario 301b.
- [Seciones de fisioterapia realizadas en c.e](../../../servicios/diagnostico_tratamiento/seciones_de_fisioterapia_realizadas_en_c_e/readme.md): 2024-2025, formulario 301b.
- [Sesiones de fisioterapia realizadas en internación](../../../servicios/diagnostico_tratamiento/sesiones_de_fisioterapia_realizadas_en_internacion/readme.md): 2024-2025, formulario 301b.

Hasta 2023 el formulario cuenta las sesiones de fisioterapia sin servicio; desde 2024, en consulta externa y en internación. Consultarlos juntos como una serie supone que los dos servicios suman lo mismo que el total anterior.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/diagnostico_tratamiento/sesiones_de_fisioterapia_realizadas/datos.parquet',
    'datos/servicios/diagnostico_tratamiento/seciones_de_fisioterapia_realizadas_en_c_e/datos.parquet',
    'datos/servicios/diagnostico_tratamiento/sesiones_de_fisioterapia_realizadas_en_internacion/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015-2023 | 301b | N° de Seciones de Fisioterapia realizadas |  |
