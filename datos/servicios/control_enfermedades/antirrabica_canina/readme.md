# Antirrábica canina

Registros en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2009. Fuente: SNIS, formularios 301.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2009 |
| Periodicidad | mensual |
| Municipios con registros | 325 |
| Desagregación |  |
| Filas | 14.806 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 1.136.208 |
| 2002 | 680.812 |
| 2003 | 767.999 |
| 2004 | 925.370 |
| 2005 | 1.459.357 |
| 2006 | 1.675.494 |
| 2007 | 1.856.202 |
| 2008 | 2.260.586 |
| 2009 | 2.206.375 |

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
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/antirrabica_canina/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/antirrabica_canina/datos.parquet'
where gestion = 2009 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2009 | 301 | Antirrábica canina |  |
