# Tuberculosis: quimioprofilaxis en menores de 5 años

Registros en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2008-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2008-2025 |
| Periodicidad | mensual |
| Municipios con registros | 293 |
| Desagregación | sexo, edad |
| Filas | 12.462 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2008-2025 | <5 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2008 | 1.679 |
| 2009 | 2.876 |
| 2010 | 1.707 |
| 2011 | 1.752 |
| 2012 | 1.949 |
| 2013 | 2.050 |
| 2014 | 2.018 |
| 2015 | 2.912 |
| 2016 | 1.891 |
| 2017 | 1.778 |
| 2018 | 1.853 |
| 2019 | 1.740 |
| 2020 | 1.186 |
| 2021 | 1.149 |
| 2022 | 1.377 |
| 2023 | 1.452 |
| 2024 | 1.401 |
| 2025 | 1.264 |

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
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tuberculosis_quimioprofilaxis/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tuberculosis_quimioprofilaxis/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tuberculosis_quimioprofilaxis/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2008 | 301 | N° de Quimioprofilaxis en menores de 5 | 1.0.4 (2013) |
| 2009-2011 | 301 | N° de Quimioprofilaxis en menores de 5 años | 1.0.4 (2013) |
| 2012 | 301 | l 23.8 N° de Quimioprofilaxis en menores de 5 años | 1.0.4 (2013) |
| 2013 | 301 | N° de Quimioprofilaxis en menores de 5 años | 1.0.4 (2013) |
| 2014 | 301 | 23.8 N° de Quimioprofilaxis en menores de 5 años | 2.0.0 (2014) |
| 2015 | 301a | Total Nº de Quimioprofilaxis en menores de 5 años | 3.0.1 (2016) |
| 2016 | 301a | Nº de Quimioprofilaxis en menores de 5 años | 3.0.2 (2016) |
| 2017 | 301a | Nº de Quimioprofilaxis en menores de 5 años | 4.0.0 (2018) |
| 2018 | 301a | Nº de Quimioprofilaxis en menores de 5 años | 4.0.1 (2018) |
| 2019-2020 | 301a | Nº de Quimioprofilaxis en menores de 5 años | 5.0.1 (2020) |
| 2021 | 301a | Nº de Quimioprofilaxis en menores de 5 años | 6.0.0 (2021) |
| 2022-2023 | 301a | Nº de Quimioprofilaxis en menores de 5 años | 6.0.1 (2022) |
| 2024-2025 | 301a | Nº de Quimioprofilaxis en menores de 5 años | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
