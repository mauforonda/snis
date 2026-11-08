# Talla para la edad

Atenciones registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2010-2014. Fuente: SNIS, formularios 301.

## Qué es

| | |
| --- | --- |
| Gestiones | 2010-2014 |
| Periodicidad | mensual |
| Municipios con registros | 340 |
| Desagregación | clasificación, sexo, edad |
| Filas | 223.662 |

Valores de `clasificacion` (clasificación):

- baja (2010-2014)
- normal (2010-2014)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2010-2014 | <1, 1, 2-4 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2010 | 3.632.379 |
| 2011 | 4.037.830 |
| 2012 | 4.059.235 |
| 2013 | 4.397.362 |
| 2014 | 3.938.998 |

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
| `clasificacion` | string | Clasificación. |
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/nutricion/talla_para_la_edad/datos.parquet'
group by gestion order by gestion;

-- Por gestión y clasificacion
select gestion, clasificacion, sum(cantidad) as cantidad
from 'datos/servicios/nutricion/talla_para_la_edad/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/nutricion/talla_para_la_edad/datos.parquet'
where gestion = 2014 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2010 | 301 | Talla Baja; Talla Normal | 1.0.4 (2013) |
| 2011 | 301 | l 9.1 Talla Normal; l 9.2 Talla Baja | 1.0.4 (2013) |
| 2012 | 301 | l Talla Baja; l Talla Normal | 1.0.4 (2013) |
| 2013 | 301 | a Baja; a Normal | 1.0.4 (2013) |
| 2014 | 301 | Total Talla Baja; Total Talla Normal | 2.0.0 (2014) |
