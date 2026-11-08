# Otras violencias (causas externas)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2007-2014. Fuente: SNIS, formularios 302.

## Qué es

| | |
| --- | --- |
| Gestiones | 2007-2014 |
| Periodicidad | semanal |
| Municipios con registros | 321 |
| Desagregación | sexo, edad |
| Filas | 59.799 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2007 | <1, 1-4, 5-14, 15-59, 60+ |
| 2008-2014 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2007 | 10.643 |
| 2008 | 29.821 |
| 2009 | 44.691 |
| 2010 | 19.999 |
| 2011 | 24.342 |
| 2012 | 24.334 |
| 2013 | 28.586 |
| 2014 | 23.953 |

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
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/otras_violencias/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/otras_violencias/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/otras_violencias/datos.parquet'
where gestion = 2014 group by all order by casos desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2007 | 302 | 37 Otras violencias (causas externas) |  |  |
| 2008-2009 | 302 | 34 Otras violencias (accidentes, agresiones, leer instructivo) | 1.0.4 (2013) | Y04 Y05 Y06 Y07 |
| 2010-2013 | 302 | Otras violencias (accidentes, agresiones, leer in | 1.0.4 (2013) | Y04 Y05 Y06 Y07 |
| 2014 | 302 | Otras violencias (accidentes, agresiones, leer in | 2.0.0 (2014) | Y04 Y05 Y06 Y07 |
