# Nacidos muertos

Atenciones y nacimientos registrados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | mensual |
| Municipios con registros | 317 |
| Desagregación | lugar |
| Filas | 14.280 |

Valores de `lugar` (lugar):

- servicio (2001-2025)
- domicilio (2024-2025)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 2.223 |
| 2002 | 2.510 |
| 2003 | 2.394 |
| 2004 | 2.285 |
| 2005 | 2.256 |
| 2006 | 2.209 |
| 2007 | 2.234 |
| 2008 | 2.547 |
| 2009 | 2.351 |
| 2010 | 2.464 |
| 2011 | 2.404 |
| 2012 | 2.491 |
| 2013 | 2.332 |
| 2014 | 2.264 |
| 2015 | 2.148 |
| 2016 | 2.105 |
| 2017 | 1.909 |
| 2018 | 1.970 |
| 2019 | 1.978 |
| 2020 | 1.955 |
| 2021 | 1.997 |
| 2022 | 1.814 |
| 2023 | 1.750 |
| 2024 | 1.564 |
| 2025 | 1.370 |

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
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/nacidos_muertos/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/nacidos_muertos/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2007 | 301 | Nacidos muertos |  |
| 2008-2013 | 301 | Nacidos muertos | 1.0.4 (2013) |
| 2014 | 301 | 11.4 Nacidos muertos | 2.0.0 (2014) |
| 2015 | 301a | Nacidos muertos | 3.0.1 (2016) |
| 2016 | 301a | Nacidos muertos | 3.0.2 (2016) |
| 2017 | 301a | Nacidos muertos | 4.0.0 (2018) |
| 2018 | 301a | Nacidos muertos | 4.0.1 (2018) |
| 2019-2020 | 301a | Nacidos muertos | 5.0.1 (2020) |
| 2021 | 301a | Nacidos muertos | 6.0.0 (2021) |
| 2022-2023 | 301a | Nacidos muertos | 6.0.1 (2022) |
| 2024-2025 | 301a | 9. Nacidos muertos | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
