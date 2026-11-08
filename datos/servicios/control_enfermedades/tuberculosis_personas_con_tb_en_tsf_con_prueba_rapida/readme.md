# Tuberculosis: personas con TB en TSF con prueba rápida

Registros en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2023. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2023 |
| Periodicidad | mensual |
| Municipios con registros | 293 |
| Desagregación | sexo |
| Filas | 12.664 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2015 | 4.988 |
| 2016 | 5.452 |
| 2017 | 5.699 |
| 2018 | 6.108 |
| 2019 | 6.180 |
| 2020 | 4.476 |
| 2021 | 5.900 |
| 2022 | 6.898 |
| 2023 | 8.305 |

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
from 'datos/servicios/control_enfermedades/tuberculosis_personas_con_tb_en_tsf_con_prueba_rapida/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tuberculosis_personas_con_tb_en_tsf_con_prueba_rapida/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tuberculosis_personas_con_tb_en_tsf_con_prueba_rapida/datos.parquet'
where gestion = 2023 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015 | 301a | Total Nº de Personas con TB en TSF con prueba rápida | 3.0.1 (2016) |
| 2016 | 301a | Nº de Personas con TB en TSF con prueba rápida | 3.0.2 (2016) |
| 2017 | 301a | Nº de Personas con TB en TSF con prueba rápida | 4.0.0 (2018) |
| 2018 | 301a | Nº de Personas con TB en TSF con prueba rápida | 4.0.1 (2018) |
| 2019-2020 | 301a | Nº de Personas con TB en TSF con prueba rápida | 5.0.1 (2020) |
| 2021 | 301a | Nº de Personas con TB en TSF con prueba rápida | 6.0.0 (2021) |
| 2022-2023 | 301a | Nº de Personas con TB en TSF con prueba rápida | 6.0.1 (2022) |
