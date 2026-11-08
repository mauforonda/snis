# Acciones preventivas dentro del establecimiento

Atenciones registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2005-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2005-2025 |
| Periodicidad | mensual |
| Municipios con registros | 343 |
| Desagregación | sexo, edad, lugar |
| Filas | 358.572 |

Valores de `lugar` (lugar):

- dentro (2010-2014)
- fuera (2010-2014)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015-2025 | <5, 5-13, 14-19, 20-59, 60+ |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2005 | 581.516 |
| 2006 | 909.901 |
| 2007 | 1.409.065 |
| 2008 | 1.368.073 |
| 2009 | 1.451.968 |
| 2010 | 1.173.825 |
| 2011 | 1.195.346 |
| 2012 | 1.108.303 |
| 2013 | 1.146.873 |
| 2014 | 978.641 |
| 2015 | 900.411 |
| 2016 | 1.084.157 |
| 2017 | 1.181.636 |
| 2018 | 1.344.867 |
| 2019 | 1.248.679 |
| 2020 | 551.817 |
| 2021 | 840.259 |
| 2022 | 1.218.412 |
| 2023 | 1.477.082 |
| 2024 | 1.555.197 |
| 2025 | 1.596.552 |

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
from 'datos/servicios/odontologia/acciones_preventivas/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/odontologia/acciones_preventivas/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/odontologia/acciones_preventivas/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2005-2007 | 301 | Acciones preventivas |  |
| 2008-2009 | 301 | Acciones preventivas | 1.0.4 (2013) |
| 2010-2013 | 301 | Acciones preventivas dentro del establecimiento; Acciones preventivas fuera del establecimiento | 1.0.4 (2013) |
| 2014 | 301 | 310 Acciones preventivas dentro del establecimiento; 311 Acciones preventivas fuera del establecimiento | 2.0.0 (2014) |
| 2015 | 301a | Medidas Preventivas | 3.0.1 (2016) |
| 2016 | 301a | Medidas Preventivas | 3.0.2 (2016) |
| 2017 | 301a | Medidas Preventivas | 4.0.0 (2018) |
| 2018 | 301a | Medidas Preventivas | 4.0.1 (2018) |
| 2019-2020 | 301a | Medidas Preventivas | 5.0.1 (2020) |
| 2021 | 301a | Medidas Preventivas | 6.0.0 (2021) |
| 2022-2023 | 301a | Medidas Preventivas | 6.0.1 (2022) |
| 2024-2025 | 301a | Medidas Preventivas | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
