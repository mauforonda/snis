# Influenza pandémica

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2008-2014. Fuente: SNIS, formularios 302.

## Qué es

| | |
| --- | --- |
| Gestiones | 2008-2014 |
| Periodicidad | semanal |
| Municipios con registros | 90 |
| Desagregación | edad |
| Filas | 4.628 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2008 | 1-4, 5-9, 10-20, 21-59, 60+ |
| 2009-2014 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2008 | 35 |
| 2009 | 14.118 |
| 2010 | 3.102 |
| 2011 | 5.581 |
| 2012 | 2.247 |
| 2013 | 2.812 |
| 2014 | 2.465 |

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
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/influenza_pandemica/datos.parquet'
group by gestion order by gestion;

-- Por gestión y edad_grupo
select gestion, edad_grupo, sum(casos) as casos
from 'datos/vigilancia/casos/influenza_pandemica/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/influenza_pandemica/datos.parquet'
where gestion = 2014 group by all order by casos desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2008-2009 | 302 | 15 Influenza Aviar - Pandemica | 1.0.4 (2013) | J11 |
| 2010-2013 | 302 | Influenza / Pandémica | 1.0.4 (2013) | J11 |
| 2014 | 302 | Influenza / Pandémica | 2.0.0 (2014) | J11 |
