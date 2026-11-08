# Muerte materna

Muertes por esta causa en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | semanal |
| Municipios con registros | 276 |
| Desagregación | sexo, edad, lugar |
| Filas | 3.544 |

Valores de `lugar` (lugar):

- dentro (2001-2003, 2005-2015)
- fuera (2001-2003, 2005-2015)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015 | 15-19, 20-39, 40-49, 50-59 |

Total por gestión:

| Gestión | Defunciones |
| ---: | ---: |
| 2001 | 162 |
| 2002 | 180 |
| 2003 | 157 |
| 2004 | 173 |
| 2005 | 181 |
| 2006 | 213 |
| 2007 | 160 |
| 2008 | 170 |
| 2009 | 208 |
| 2010 | 180 |
| 2011 | 223 |
| 2012 | 185 |
| 2013 | 175 |
| 2014 | 133 |
| 2015 | 122 |
| 2016 | 122 |
| 2017 | 100 |
| 2018 | 140 |
| 2019 | 101 |
| 2020 | 153 |
| 2021 | 161 |
| 2022 | 132 |
| 2023 | 118 |
| 2024 | 92 |
| 2025 | 99 |

### Advertencias

- Desde 2015 cuenta las muertes maternas notificadas; las confirmadas son otro dataset.

## Cómo utilizar

Cada fila da el número de defunciones de un periodo, un municipio y una población. Para obtener un total, sume las filas: el dataset no tiene filas de total. Una combinación sin fila significa que no hubo registros. Las convenciones de tiempo, territorio y población están en el [catálogo](../../../README.md#cómo-leer-los-datos).

| Columna | Tipo | Descripción |
| --- | --- | --- |
| `gestion` | integer | Año calendario (gestión) del registro. |
| `semana` | integer | Semana epidemiológica, de 1 a 53. Va de domingo a sábado. |
| `fecha_inicio` | date | Primer día de la semana o del mes. |
| `departamento` | string | Nombre del departamento. |
| `municipio` | string | Nombre del municipio. |
| `municipio_codigo` | string | Código del municipio, 6 dígitos: departamento (2), provincia (2) y municipio (2). |
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `defunciones` | integer | Número de defunciones en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_materna/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_materna/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_materna/datos.parquet'
where gestion = 2025 group by all order by defunciones desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2003 | 302 | 70.- Muerte materna; 95.- Muerte materna | 1.0.4 (2013) |
| 2004 | 302 | 37 Muerte materna |  |
| 2005-2007 | 302 | 38 Muerte materna | 1.0.4 (2013) |
| 2008-2009 | 302 | 37 Muerte materna | 1.0.4 (2013) |
| 2010-2013 | 302 | Muerte materna | 1.0.4 (2013) |
| 2014 | 302 | Muerte materna | 2.0.0 (2014) |
| 2015 | 302a | Muerte materna notificada | 3.0.1 (2016) |
| 2016 | 302a | Muerte materna notificada | 3.0.2 (2016) |
| 2017 | 302a | Muerte materna notificada | 4.0.0 (2018) |
| 2018 | 302a | Muerte materna notificada | 4.0.1 (2018) |
| 2019-2020 | 302a | Muerte materna notificada | 5.0.1 (2020) |
| 2021 | 302a | Sospecha de muerte materna | 6.0.0 (2021) |
| 2022-2023 | 302a | Muerte materna notificada | 5.0.1 (2020) |
| 2024-2025 | 302a | 1. Muerte materna notificada | 5.0.1 (2020) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302, 2001-2007: en las variables cuyas columnas "-M" siempre valen 0, "TOTAL-H" es igual a "TOTAL": "-H" contiene a ambos sexos. Esas variables no tienen sexo. En 2004 el grupo 09 (mortalidad) tampoco tiene sexo: hay 79 muertes maternas en "-H" y 94 en "-M".
- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
