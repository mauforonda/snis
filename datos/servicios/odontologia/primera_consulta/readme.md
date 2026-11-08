# Primeras consultas

Atenciones registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2005-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2005-2025 |
| Periodicidad | mensual |
| Municipios con registros | 343 |
| Desagregación | sexo, edad, embarazo o puerperio |
| Filas | 506.693 |

Valores de `condicion` (embarazo o puerperio):

- embarazada (2015-2025)
- puerpera (2015-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015-2025 | <5, 5-13, 14-19, 20-59, 60+ |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2005 | 220.668 |
| 2006 | 689.872 |
| 2007 | 944.297 |
| 2008 | 947.025 |
| 2009 | 962.384 |
| 2010 | 955.823 |
| 2011 | 1.067.828 |
| 2012 | 1.067.120 |
| 2013 | 1.114.046 |
| 2014 | 1.104.610 |
| 2015 | 1.117.410 |
| 2016 | 1.167.048 |
| 2017 | 1.183.280 |
| 2018 | 1.208.670 |
| 2019 | 1.164.561 |
| 2020 | 718.077 |
| 2021 | 882.589 |
| 2022 | 1.100.107 |
| 2023 | 1.231.766 |
| 2024 | 1.247.858 |
| 2025 | 1.196.496 |

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
| `condicion` | string | embarazada o puerpera. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/odontologia/primera_consulta/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/odontologia/primera_consulta/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/odontologia/primera_consulta/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2005-2007 | 301 | Primeras consultas |  |
| 2008-2009 | 301 | Primeras consultas | 1.0.4 (2013) |
| 2010-2013 | 301 | Primera consulta | 1.0.4 (2013) |
| 2014 | 301 | 3.1 Primera consulta | 2.0.0 (2014) |
| 2015-2025 | 301a | Primera consulta | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
