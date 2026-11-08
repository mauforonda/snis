# Mujeres con primer control post parto

Atenciones y nacimientos registrados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2014, 2021-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2014, 2021-2025 |
| Periodicidad | mensual |
| Municipios con registros | 344 |
| Desagregación | edad, lugar |
| Filas | 84.113 |

Valores de `lugar` (lugar):

- servicio (2001-2014, 2021-2025)
- domicilio (2021-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2024-2025 | <10, 10-14, 15-19, 20-34, 35-49, 50+ |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 94.329 |
| 2002 | 103.916 |
| 2003 | 115.750 |
| 2004 | 124.478 |
| 2005 | 132.010 |
| 2006 | 133.539 |
| 2007 | 126.334 |
| 2008 | 125.781 |
| 2009 | 125.245 |
| 2010 | 120.099 |
| 2011 | 124.530 |
| 2012 | 123.032 |
| 2013 | 121.820 |
| 2014 | 108.412 |
| 2021 | 59.412 |
| 2022 | 76.908 |
| 2023 | 87.239 |
| 2024 | 96.105 |
| 2025 | 103.949 |

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
from 'datos/servicios/salud_materna_neonatal/primer_control_post_parto/datos.parquet'
group by gestion order by gestion;

-- Por gestión y edad_grupo
select gestion, edad_grupo, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/primer_control_post_parto/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/primer_control_post_parto/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2007 | 301 | Mujeres con primer control post parto |  |
| 2008-2013 | 301 | Mujeres con primer control post parto | 1.0.4 (2013) |
| 2014 | 301 | 11.7 Mujeres con primer control post parto | 2.0.0 (2014) |
| 2021 | 301a | Primer Control Post Parto | 6.0.0 (2021) |
| 2022-2023 | 301a | Primer Control Post Parto | 6.0.1 (2022) |
| 2024-2025 | 301a | Primer control Post Parto | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
