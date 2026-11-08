# Vacuna BCG

Dosis aplicadas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | mensual |
| Municipios con registros | 344 |
| Desagregación | sexo, edad, lugar |
| Filas | 209.569 |

Valores de `lugar` (lugar):

- dentro (2001-2013, 2015-2025)
- fuera (2001-2013, 2015-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001-2023 | <1 |
| 2024-2025 | <1, 1, 2, 3, 4 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 227.319 |
| 2002 | 234.485 |
| 2003 | 224.986 |
| 2004 | 223.738 |
| 2005 | 228.137 |
| 2006 | 227.929 |
| 2007 | 224.948 |
| 2008 | 226.569 |
| 2009 | 229.260 |
| 2010 | 237.560 |
| 2011 | 247.236 |
| 2012 | 234.148 |
| 2013 | 237.503 |
| 2014 | 239.986 |
| 2015 | 241.055 |
| 2016 | 234.188 |
| 2017 | 226.605 |
| 2018 | 222.165 |
| 2019 | 213.261 |
| 2020 | 200.167 |
| 2021 | 187.722 |
| 2022 | 183.677 |
| 2023 | 176.936 |
| 2024 | 161.500 |
| 2025 | 151.712 |

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
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/bcg/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/bcg/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/bcg/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2007 | 301 | BCG |  |
| 2008-2011 | 301 | BCG | 1.0.4 (2013) |
| 2012 | 301 | l 17.1 BCG | 1.0.4 (2013) |
| 2013 | 301 | BCG | 1.0.4 (2013) |
| 2014 | 301 | 17.1 BCG | 2.0.0 (2014) |
| 2015 | 301a | Total BCG | 3.0.1 (2016) |
| 2016 | 301a | BCG | 3.0.2 (2016) |
| 2017 | 301a | BCG | 4.0.0 (2018) |
| 2018 | 301a | BCG | 4.0.1 (2018) |
| 2019-2020 | 301a | BCG | 5.0.1 (2020) |
| 2021 | 301a | BCG | 6.0.0 (2021) |
| 2022-2023 | 301a | BCG | 6.0.1 (2022) |
| 2024-2025 | 301a | BCG | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
