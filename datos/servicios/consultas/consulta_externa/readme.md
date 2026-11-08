# Consulta externa

Atenciones registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | mensual |
| Municipios con registros | 344 |
| Desagregación | sexo, edad, nuevo o repetido |
| Filas | 2.410.356 |

Valores de `caso` (nuevo o repetido):

- nuevo (2001-2013, 2015-2025)
- repetido (2001-2013, 2015-2025)
- primera (2024-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001-2007 | <5, 5-14, 15-59, 60+ |
| 2008-2014 | <5, 5-9, 10-20, 21-59, 60+ |
| 2015-2025 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 8.543.731 |
| 2002 | 10.050.834 |
| 2003 | 11.584.449 |
| 2004 | 12.720.992 |
| 2005 | 13.475.257 |
| 2006 | 14.791.759 |
| 2007 | 15.897.972 |
| 2008 | 15.953.168 |
| 2009 | 17.148.318 |
| 2010 | 17.751.964 |
| 2011 | 18.008.081 |
| 2012 | 17.766.317 |
| 2013 | 19.582.319 |
| 2014 | 20.559.091 |
| 2015 | 22.346.148 |
| 2016 | 23.944.647 |
| 2017 | 24.244.734 |
| 2018 | 25.763.962 |
| 2019 | 26.125.042 |
| 2020 | 18.653.938 |
| 2021 | 24.084.874 |
| 2022 | 28.023.146 |
| 2023 | 31.815.453 |
| 2024 | 33.737.086 |
| 2025 | 34.552.067 |

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
| `caso` | string | nuevo, repetido, seguimiento o primera, como lo registra el formulario. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/consultas/consulta_externa/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/consultas/consulta_externa/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/consultas/consulta_externa/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2007 | 301 | Nuevas en menores de 5 años; Nuevas en personas de 15 a 59 años; Nuevas en personas de 5 a 14 años; Nuevas en personas de 60 años o más; Repetidas en menores de 5 años; Repetidas en personas de 15 a 59 años; Repetidas en personas de 5 a 14 años; Repetidas en personas de 60 años o más |  |
| 2008-2009 | 301 | Menores de 5 años; Personas de 10 a 20 años; Personas de 21 a 59 años; Personas de 5 a 9 años; Personas de 60 años y más |  |
| 2010-2013 | 301 | Menores de 5 años; Personas de 10 a 20 años; Personas de 21 a 59 años; Personas de 5 a 9 años; Personas de 60 años y más | 1.0.4 (2013) |
| 2014 | 301 | 1.1 Menores de 5 años; 1.2 Personas de 5 a 9 años; 1.3 Personas de 10 a 20 años; 1.4 Personas de 21 a 59 años; 1.5 Personas de 60 años y más | 2.0.0 (2014) |
| 2015 | 301a | Menores de 6 meses; Ninos de 6 meses a < 1 año; Niños de 1 a 4 años; Personas de 10 a 14 años; Personas de 15 a 19 años; Personas de 20 a 39 años; Personas de 40 a 49 años; Personas de 5 a 9 años; Personas de 50 a 59 años; Personas de 60 años y más | 3.0.1 (2016) |
| 2016 | 301a | Menores de 6 meses; Ninos de 6 meses a < 1 año; Niños de 1 a 4 años; Personas de 10 a 14 años; Personas de 15 a 19 años; Personas de 20 a 39 años; Personas de 40 a 49 años; Personas de 5 a 9 años; Personas de 50 a 59 años; Personas de 60 años y más | 3.0.2 (2016) |
| 2017 | 301a | Menores de 6 meses; Ninos de 6 meses a < 1 año; Niños de 1 a 4 años; Personas de 10 a 14 años; Personas de 15 a 19 años; Personas de 20 a 39 años; Personas de 40 a 49 años; Personas de 5 a 9 años; Personas de 50 a 59 años; Personas de 60 años y más | 4.0.0 (2018) |
| 2018 | 301a | Menores de 6 meses; Ninos de 6 meses a < 1 año; Niños de 1 a 4 años; Personas de 10 a 14 años; Personas de 15 a 19 años; Personas de 20 a 39 años; Personas de 40 a 49 años; Personas de 5 a 9 años; Personas de 50 a 59 años; Personas de 60 años y más | 4.0.1 (2018) |
| 2019-2020 | 301a | Menores de 6 meses; Ninos de 6 meses a < 1 año; Niños de 1 a 4 años; Personas de 10 a 14 años; Personas de 15 a 19 años; Personas de 20 a 39 años; Personas de 40 a 49 años; Personas de 5 a 9 años; Personas de 50 a 59 años; Personas de 60 años y más | 5.0.1 (2020) |
| 2021 | 301a | Menores de 6 meses; Ninos de 6 meses a < 1 año; Niños de 1 a 4 años; Personas de 10 a 14 años; Personas de 15 a 19 años; Personas de 20 a 39 años; Personas de 40 a 49 años; Personas de 5 a 9 años; Personas de 50 a 59 años; Personas de 60 años y más | 6.0.0 (2021) |
| 2022-2023 | 301a | Menores de 6 meses; Ninos de 6 meses a < 1 año; Niños de 1 a 4 años; Personas de 10 a 14 años; Personas de 15 a 19 años; Personas de 20 a 39 años; Personas de 40 a 49 años; Personas de 5 a 9 años; Personas de 50 a 59 años; Personas de 60 años y más | 6.0.1 (2022) |
| 2024-2025 | 301a | Menores de 6 meses; Ninos de 6 meses a < 1 año; Niños de 1 a 4 años; Personas de 10 a 14 años; Personas de 15 a 19 años; Personas de 20 a 39 años; Personas de 40 a 49 años; Personas de 5 a 9 años; Personas de 50 a 59 años; Personas de 60 años y más | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
