# Tuberculosis: TB extrapulmonar nuevos

Registros en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2008-2023. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2008-2023 |
| Periodicidad | mensual |
| Municipios con registros | 289 |
| Desagregación | sexo |
| Filas | 8.731 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2008 | 1.619 |
| 2009 | 1.961 |
| 2010 | 1.912 |
| 2011 | 2.249 |
| 2012 | 1.956 |
| 2013 | 2.019 |
| 2014 | 1.640 |
| 2015 | 1.892 |
| 2016 | 1.850 |
| 2017 | 1.879 |
| 2018 | 1.800 |
| 2019 | 1.805 |
| 2020 | 1.182 |
| 2021 | 1.423 |
| 2022 | 1.512 |
| 2023 | 1.705 |

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
from 'datos/servicios/control_enfermedades/tuberculosis_tb_extrapulmonar_nuevos/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tuberculosis_tb_extrapulmonar_nuevos/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tuberculosis_tb_extrapulmonar_nuevos/datos.parquet'
where gestion = 2023 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Tuberculosis: TB extrapulmonar nuevos (este dataset): 2008-2023, formulario 301, 301a.
- [Tuberculosis: TB extrapulmonar nuevos y recaidas](../../../servicios/control_enfermedades/tuberculosis_tb_extrapulmonar_nuevos_y_recaidas/readme.md): 2024-2025, formulario 301a.

Hasta 2023 el formulario cuenta los casos nuevos de tuberculosis extrapulmonar; desde 2024, los nuevos y las recaídas. Consultarlos juntos como una serie supone que las recaídas no cambian la serie.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/control_enfermedades/tuberculosis_tb_extrapulmonar_nuevos/datos.parquet',
    'datos/servicios/control_enfermedades/tuberculosis_tb_extrapulmonar_nuevos_y_recaidas/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2008-2011 | 301 | N° de TB extrapulmonar nuevos | 1.0.4 (2013) |
| 2012 | 301 | l 23.4 N° de TB extrapulmonar nuevos | 1.0.4 (2013) |
| 2013 | 301 | N° de TB extrapulmonar nuevos | 1.0.4 (2013) |
| 2014 | 301 | 23.4 N° de TB extrapulmonar nuevos | 2.0.0 (2014) |
| 2015 | 301a | Total N° de TB extrapulmonar nuevos | 3.0.1 (2016) |
| 2016 | 301a | N° de TB extrapulmonar nuevos | 3.0.2 (2016) |
| 2017 | 301a | N° de TB extrapulmonar nuevos | 4.0.0 (2018) |
| 2018 | 301a | N° de TB extrapulmonar nuevos | 4.0.1 (2018) |
| 2019-2020 | 301a | N° de TB extrapulmonar nuevos | 5.0.1 (2020) |
| 2021 | 301a | N° de TB extrapulmonar nuevos | 6.0.0 (2021) |
| 2022-2023 | 301a | N° de TB extrapulmonar nuevos | 6.0.1 (2022) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
