# Pacientes referidos a otros establecimientos

Pacientes o referencias registrados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | mensual |
| Municipios con registros | 344 |
| Desagregación |  |
| Filas | 83.735 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 127.990 |
| 2002 | 156.804 |
| 2003 | 150.097 |
| 2004 | 153.493 |
| 2005 | 165.713 |
| 2006 | 188.777 |
| 2007 | 196.847 |
| 2008 | 195.646 |
| 2009 | 209.041 |
| 2010 | 228.267 |
| 2011 | 241.861 |
| 2012 | 236.468 |
| 2013 | 279.847 |
| 2014 | 342.232 |
| 2015 | 397.122 |
| 2016 | 438.963 |
| 2017 | 463.271 |
| 2018 | 592.631 |
| 2019 | 713.316 |
| 2020 | 506.760 |
| 2021 | 687.776 |
| 2022 | 883.725 |
| 2023 | 1.024.162 |
| 2024 | 1.035.501 |
| 2025 | 1.019.238 |

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
from 'datos/servicios/referencias/pacientes_referidos_a_otros_establecimientos/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/referencias/pacientes_referidos_a_otros_establecimientos/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2007 | 301 | Pacientes referidos a otros establecimientos |  |
| 2008-2013 | 301 | Pacientes referidos a otros establecimientos | 1.0.4 (2013) |
| 2014 | 301 | 2.1 Pacientes referidos a otros establecimientos | 2.0.0 (2014) |
| 2015 | 301a | Pacientes referidos a otros establecimientos | 3.0.1 (2016) |
| 2016 | 301a | Pacientes referidos a otros establecimientos | 3.0.2 (2016) |
| 2017 | 301a | Pacientes referidos a otros establecimientos | 4.0.0 (2018) |
| 2018 | 301a | Pacientes referidos a otros establecimientos | 4.0.1 (2018) |
| 2019-2020 | 301a | Pacientes referidos a otros establecimientos | 5.0.1 (2020) |
| 2021 | 301a | Pacientes referidos a otros establecimientos | 6.0.0 (2021) |
| 2022-2023 | 301a | Pacientes referidos a otros establecimientos | 6.0.1 (2022) |
| 2024-2025 | 301a | Pacientes referidos a otros establecimientos | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
