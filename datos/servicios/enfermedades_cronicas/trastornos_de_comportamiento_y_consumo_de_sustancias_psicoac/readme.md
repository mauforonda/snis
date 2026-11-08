# Trastornos de comportamiento y consumo de sustancias psicoactivas

Atenciones registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2010-2014. Fuente: SNIS, formularios 301.

## Qué es

| | |
| --- | --- |
| Gestiones | 2010-2014 |
| Periodicidad | mensual |
| Municipios con registros | 169 |
| Desagregación | sexo |
| Filas | 1.582 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2010 | 2.109 |
| 2011 | 2.825 |
| 2012 | 3.074 |
| 2013 | 4.026 |
| 2014 | 2.233 |

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
from 'datos/servicios/enfermedades_cronicas/trastornos_de_comportamiento_y_consumo_de_sustancias_psicoac/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/enfermedades_cronicas/trastornos_de_comportamiento_y_consumo_de_sustancias_psicoac/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/enfermedades_cronicas/trastornos_de_comportamiento_y_consumo_de_sustancias_psicoac/datos.parquet'
where gestion = 2014 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2010-2011 | 301 | Trastornos de comportamiento y consumo de sustancias psicoactivas | 1.0.4 (2013) | F10 F11 F12 F13 F14 F15 F16 F17 F18 F19 |
| 2012 | 301 | l 1612 Trastornos de comportamiento y consumo de sustancias psicoactivas | 1.0.4 (2013) | F10 F11 F12 F13 F14 F15 F16 F17 F18 F19 |
| 2013 | 301 | Trastornos de comportamiento y consumo de sustancias psicoactivas | 1.0.4 (2013) | F10 F11 F12 F13 F14 F15 F16 F17 F18 F19 |
| 2014 | 301 | 1612 Trastornos de comportamiento y consumo de sustancias psicoactivas | 2.0.0 (2014) | F10 F11 F12 F13 F14 F15 F16 F17 F18 F19 |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
