# Embarazo en adolescentes (menores de 20 años)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2004-2014. Fuente: SNIS, formularios 302.

## Qué es

| | |
| --- | --- |
| Gestiones | 2004-2014 |
| Periodicidad | semanal |
| Municipios con registros | 339 |
| Desagregación | sexo |
| Filas | 73.008 |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2004 | 48.636 |
| 2005 | 65.093 |
| 2006 | 67.884 |
| 2007 | 67.395 |
| 2008 | 74.954 |
| 2009 | 77.839 |
| 2010 | 84.299 |
| 2011 | 82.861 |
| 2012 | 78.504 |
| 2013 | 90.005 |
| 2014 | 85.500 |

## Cómo utilizar

Cada fila da el número de casos de un periodo, un municipio y una población. Para obtener un total, sume las filas: el dataset no tiene filas de total. Una combinación sin fila significa que no hubo registros. Las convenciones de tiempo, territorio y población están en el [catálogo](../../../README.md#cómo-leer-los-datos).

| Columna | Tipo | Descripción |
| --- | --- | --- |
| `gestion` | integer | Año calendario (gestión) del registro. |
| `semana` | integer | Semana epidemiológica, de 1 a 53. Va de domingo a sábado. |
| `fecha_inicio` | date | Primer día de la semana o del mes. |
| `departamento` | string | Nombre del departamento. |
| `municipio` | string | Nombre del municipio. |
| `municipio_codigo` | string | Código del municipio, 6 dígitos: departamento (2), provincia (2) y municipio (2). |
| `sexo` | string | mujer u hombre. |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/embarazo_adolescente/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/embarazo_adolescente/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/embarazo_adolescente/datos.parquet'
where gestion = 2014 group by all order by casos desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2004 | 302 | 51Embarazo en adolecente (menor de 20 años) |  |
| 2005-2006 | 302 | 47 Embarazo en adolecente (menor de 20 años) |  |
| 2007 | 302 | 46 Embarazo en adolecente (menor de 20 años) |  |
| 2008-2009 | 302 | 45 Embarazo en adolecente (menor de 20 años) |  |
| 2010-2013 | 302 | Embarazo en adolescente (< de 20 años) | 1.0.4 (2013) |
| 2014 | 302 | Embarazo en adolescente (< de 20 años) | 2.0.0 (2014) |
