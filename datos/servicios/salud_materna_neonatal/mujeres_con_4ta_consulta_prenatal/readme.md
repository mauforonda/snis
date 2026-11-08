# Mujeres con 4ta consulta prenatal

Atenciones y nacimientos registrados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | mensual |
| Municipios con registros | 344 |
| Desagregación | edad, lugar |
| Filas | 180.424 |

Valores de `lugar` (lugar):

- dentro (2015-2025)
- fuera (2015-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015-2023 | <15, 15-19, 20-34, 35-49, 50+ |
| 2024-2025 | <10, 10-14, 15-19, 20-34, 35-49, 50+ |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 117.931 |
| 2002 | 116.535 |
| 2003 | 127.597 |
| 2004 | 139.391 |
| 2005 | 140.309 |
| 2006 | 155.149 |
| 2007 | 148.120 |
| 2008 | 148.585 |
| 2009 | 164.911 |
| 2010 | 163.281 |
| 2011 | 167.364 |
| 2012 | 153.458 |
| 2013 | 170.980 |
| 2014 | 174.115 |
| 2015 | 189.059 |
| 2016 | 191.815 |
| 2017 | 179.460 |
| 2018 | 175.379 |
| 2019 | 163.442 |
| 2020 | 121.721 |
| 2021 | 144.068 |
| 2022 | 141.653 |
| 2023 | 138.770 |
| 2024 | 122.890 |
| 2025 | 119.157 |

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
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/mujeres_con_4ta_consulta_prenatal/datos.parquet'
group by gestion order by gestion;

-- Por gestión y edad_grupo
select gestion, edad_grupo, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/mujeres_con_4ta_consulta_prenatal/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/mujeres_con_4ta_consulta_prenatal/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2009 | 301 | Mujeres con 4ta consulta prenatal |  |
| 2010-2013 | 301 | Mujeres con 4ta consulta prenatal | 1.0.4 (2013) |
| 2014 | 301 | 4.4 Mujeres con 4ta consulta prenatal | 2.0.0 (2014) |
| 2015-2023 | 301a | Mujeres con 4ta consulta prenatal |  |
| 2024-2025 | 301a | Mujeres con 4ta consulta prenatal | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
