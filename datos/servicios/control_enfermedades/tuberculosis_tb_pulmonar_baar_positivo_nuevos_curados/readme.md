# Tuberculosis: TBP BAAR (+) nuevos curados

Registros en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2010-2023. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2010-2023 |
| Periodicidad | mensual |
| Municipios con registros | 305 |
| Desagregación | sexo |
| Filas | 14.940 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2010 | 2.991 |
| 2011 | 3.268 |
| 2012 | 3.709 |
| 2013 | 3.538 |
| 2014 | 3.457 |
| 2015 | 3.316 |
| 2016 | 3.405 |
| 2017 | 3.295 |
| 2018 | 3.108 |
| 2019 | 3.355 |
| 2020 | 3.203 |
| 2021 | 3.341 |
| 2022 | 3.995 |
| 2023 | 4.562 |

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
from 'datos/servicios/control_enfermedades/tuberculosis_tb_pulmonar_baar_positivo_nuevos_curados/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tuberculosis_tb_pulmonar_baar_positivo_nuevos_curados/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tuberculosis_tb_pulmonar_baar_positivo_nuevos_curados/datos.parquet'
where gestion = 2023 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2010-2011 | 301 | Nº de TBP BAAR (+) nuevos curados | 1.0.4 (2013) |
| 2012 | 301 | l 23.9 Nº de TBP BAAR (+) nuevos curados | 1.0.4 (2013) |
| 2013 | 301 | Nº de TBP BAAR (+) nuevos curados | 1.0.4 (2013) |
| 2014 | 301 | 23.9 Nº de TBP BAAR (+) nuevos curados | 2.0.0 (2014) |
| 2015 | 301a | Total Nº de TBP BAAR (+) nuevos curados | 3.0.1 (2016) |
| 2016 | 301a | Nº de TBP BAAR (+) nuevos curados | 3.0.2 (2016) |
| 2017 | 301a | Nº de TBP BAAR (+) nuevos curados | 4.0.0 (2018) |
| 2018 | 301a | Nº de TBP BAAR (+) nuevos curados | 4.0.1 (2018) |
| 2019-2020 | 301a | Nº de TBP BAAR (+) nuevos curados | 5.0.1 (2020) |
| 2021 | 301a | Nº de TBP BAAR (+) nuevos curados | 6.0.0 (2021) |
| 2022-2023 | 301a | Nº de TBP BAAR (+) nuevos curados | 6.0.1 (2022) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
