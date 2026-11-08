# Días camas disponibles otros servicios

Registros de internación en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | mensual |
| Municipios con registros | 340 |
| Desagregación | sexo |
| Filas | 70.252 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 2.651.327 |
| 2002 | 3.204.596 |
| 2003 | 3.322.664 |
| 2004 | 3.494.798 |
| 2005 | 3.657.697 |
| 2006 | 3.829.940 |
| 2007 | 3.897.023 |
| 2008 | 3.936.788 |
| 2009 | 4.002.997 |
| 2010 | 4.149.019 |
| 2011 | 4.228.315 |
| 2012 | 4.251.533 |
| 2013 | 4.387.353 |
| 2014 | 4.248.992 |
| 2015 | 15.918.114 |
| 2016 | 4.326.718 |
| 2017 | 4.830.970 |
| 2018 | 4.882.653 |
| 2019 | 5.307.569 |
| 2020 | 5.368.439 |
| 2021 | 5.697.740 |
| 2022 | 5.978.269 |
| 2023 | 6.108.822 |
| 2024 | 6.168.126 |
| 2025 | 6.207.392 |

### Advertencias

- Carapari registra 11.545.414 días cama en diciembre de 2015, casi tres veces el total nacional de otras gestiones (unos 4,3 millones). Se publica tal como se registró; probablemente es un error de registro.

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
from 'datos/servicios/internacion/dias_camas_disponibles_otros_servicios/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/internacion/dias_camas_disponibles_otros_servicios/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/internacion/dias_camas_disponibles_otros_servicios/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2009 | 301 | Días camas disponibles otros servicios |  |
| 2010-2011 | 301 | Días camas disponibles otros servicios | 1.0.4 (2013) |
| 2012 | 301 | l 1310 Días camas disponibles otros servicios | 1.0.4 (2013) |
| 2013 | 301 | Días camas disponibles otros servicios | 1.0.4 (2013) |
| 2014 | 301 | 1310 Días camas disponibles otros servicios | 2.0.0 (2014) |
| 2015 | 301a | Total Días camas disponibles otros servicios | 3.0.1 (2016) |
| 2016 | 301a | Días camas disponibles otros servicios | 3.0.2 (2016) |
| 2017 | 301a | Días camas disponibles otros servicios | 4.0.0 (2018) |
| 2018 | 301a | Días camas disponibles otros servicios | 4.0.1 (2018) |
| 2019-2020 | 301a | Días camas disponibles otros servicios | 5.0.1 (2020) |
| 2021 | 301a | Días camas disponibles otros servicios | 6.0.0 (2021) |
| 2022-2023 | 301a | Días camas disponibles otros servicios | 6.0.1 (2022) |
| 2024-2025 | 301a | 10. Días camas disponibles otros servicios | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
