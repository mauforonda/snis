# Consultas odontológicas

Atenciones registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | mensual |
| Municipios con registros | 343 |
| Desagregación | sexo, edad, nuevo o repetido, embarazo o puerperio |
| Filas | 920.956 |

Valores de `condicion` (embarazo o puerperio):

- embarazada o puerpera (2010-2014)
- embarazada (2015-2025)
- puerpera (2015-2025)

Valores de `caso` (nuevo o repetido):

- nuevo (2001-2025)
- repetido (2001-2009, 2015-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2004-2009 | <5, 5+ |
| 2010-2011 | <5, 5-59, 60+ |
| 2012 | <5, 5-60, 60+ |
| 2013-2014 | <5, 5-59, 60+ |
| 2015-2025 | <5, 5-13, 14-19, 20-59, 60+ |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 1.247.250 |
| 2002 | 1.375.779 |
| 2003 | 1.732.071 |
| 2004 | 2.122.249 |
| 2005 | 2.243.623 |
| 2006 | 2.391.283 |
| 2007 | 2.821.820 |
| 2008 | 2.596.373 |
| 2009 | 2.636.605 |
| 2010 | 2.081.575 |
| 2011 | 2.246.823 |
| 2012 | 2.391.083 |
| 2013 | 2.698.247 |
| 2014 | 2.784.227 |
| 2015 | 3.431.693 |
| 2016 | 3.790.305 |
| 2017 | 3.910.519 |
| 2018 | 4.091.130 |
| 2019 | 4.103.497 |
| 2020 | 1.956.825 |
| 2021 | 2.709.857 |
| 2022 | 3.672.536 |
| 2023 | 4.477.479 |
| 2024 | 4.666.534 |
| 2025 | 4.676.586 |

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
| `condicion` | string | embarazada o puerpera. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/odontologia/consulta_odontologica/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/odontologia/consulta_odontologica/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/odontologia/consulta_odontologica/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2003 | 301 | Repetidas; nuevas |  |
| 2004 | 301 | Nuevas en menores de 5 años; Nuevas en personas de 5 años y más; Repetidas en menores de 5 años; Repetidas en personas de 5 años y más |  |
| 2005-2007 | 301 | Consultas nuevas en menores de 5 años; Consultas nuevas en personas de 5 años y más; Consultas repetidas en menores de 5 años; Consultas repetidas en personas de 5 años y más |  |
| 2008-2009 | 301 | Consultas nuevas en menores de 5 años; Consultas nuevas en personas de 5 años y más; Consultas repetidas en menores de 5 años; Consultas repetidas en personas de 5 años y más | 1.0.4 (2013) |
| 2010-2011 | 301 | Consultas nuevas a Mujer Embarazada o Puérpera; Consultas nuevas de 5 a 59 años; Consultas nuevas de 60 años y más; Consultas nuevas menores de 5 años | 1.0.4 (2013), 2.0.0 (2014) |
| 2012 | 301 | Consultas nuevas a Mujer Embarazada o Puérpera; Consultas nuevas de 5 a 60 años; Consultas nuevas de 60 años y más; Consultas nuevas menores de 5 años | 1.0.4 (2013) |
| 2013 | 301 | Consultas nuevas a Mujer Embarazada o Puérpera; Consultas nuevas de 5 a 59 años; Consultas nuevas de 60 años y más; Consultas nuevas menores de 5 años | 1.0.4 (2013), 2.0.0 (2014) |
| 2014 | 301 | 3.2 Consultas nuevas menores de 5 años; 3.3 Consultas nuevas de 5 a 59 años; 3.4 Consultas nuevas de 60 años y más; 3.5 Consultas nuevas a Mujer Embarazada o Puérpera | 2.0.0 (2014) |
| 2015-2025 | 301a | Consulta Nueva; Consulta Repetida | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
