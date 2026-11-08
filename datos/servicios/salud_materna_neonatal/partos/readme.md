# Partos vaginales y cesáreas

Atenciones y nacimientos registrados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | mensual |
| Municipios con registros | 344 |
| Desagregación | vía del parto, edad, lugar |
| Filas | 126.058 |

Valores de `via` (vía del parto):

- cesárea (2001-2025)
- vaginal (2001-2025)

Valores de `lugar` (lugar):

- servicio (2001-2025)
- domicilio (2024-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2024-2025 | <10, 10-14, 15-19, 20-34, 35-49, 50+ |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 125.662 |
| 2002 | 144.382 |
| 2003 | 145.960 |
| 2004 | 149.600 |
| 2005 | 156.160 |
| 2006 | 163.557 |
| 2007 | 162.082 |
| 2008 | 165.510 |
| 2009 | 172.731 |
| 2010 | 181.746 |
| 2011 | 191.695 |
| 2012 | 190.179 |
| 2013 | 195.841 |
| 2014 | 195.685 |
| 2015 | 207.228 |
| 2016 | 201.135 |
| 2017 | 199.203 |
| 2018 | 194.503 |
| 2019 | 188.473 |
| 2020 | 168.622 |
| 2021 | 163.750 |
| 2022 | 162.777 |
| 2023 | 159.052 |
| 2024 | 152.470 |
| 2025 | 147.754 |

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
| `via` | string | Vía del parto. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/partos/datos.parquet'
group by gestion order by gestion;

-- Por gestión y via
select gestion, via, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/partos/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/partos/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2007 | 301 | Cesáreas; Vaginales |  |
| 2008-2013 | 301 | Cesáreas; Vaginales | 1.0.4 (2013) |
| 2014 | 301 | 11.1 Vaginales; 11.2 Cesáreas | 2.0.0 (2014) |
| 2015 | 301a | Cesáreas; Vaginales | 3.0.1 (2016) |
| 2016 | 301a | Cesáreas; Vaginales | 3.0.2 (2016) |
| 2017 | 301a | Cesáreas; Vaginales | 4.0.0 (2018) |
| 2018 | 301a | Cesáreas; Vaginales | 4.0.1 (2018) |
| 2019-2020 | 301a | Cesáreas; Vaginales | 5.0.1 (2020) |
| 2021 | 301a | Cesáreas; Vaginales | 6.0.0 (2021) |
| 2022-2023 | 301a | Cesáreas; Vaginales | 6.0.1 (2022) |
| 2024-2025 | 301a | Cesareas; Vaginales | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
