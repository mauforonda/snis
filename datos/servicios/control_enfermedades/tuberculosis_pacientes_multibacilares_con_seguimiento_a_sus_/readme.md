# Tuberculosis: pacientes multibacilares con seguimiento a sus contactos

Registros en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2021-2023. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2021-2023 |
| Periodicidad | mensual |
| Municipios con registros | 16 |
| Desagregación | sexo |
| Filas | 99 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2021 | 65 |
| 2022 | 159 |
| 2023 | 67 |

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
from 'datos/servicios/control_enfermedades/tuberculosis_pacientes_multibacilares_con_seguimiento_a_sus_/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tuberculosis_pacientes_multibacilares_con_seguimiento_a_sus_/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tuberculosis_pacientes_multibacilares_con_seguimiento_a_sus_/datos.parquet'
where gestion = 2023 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2021 | 301a | Nº de pacientes multibacilares con seguimiento a sus contactos | 6.0.0 (2021) |
| 2022-2023 | 301a | Nº de pacientes multibacilares con seguimiento a sus contactos | 6.0.1 (2022) |
