# Beneficiarios(as) (niños/as) nuevos(as) del bono juana azurduy

Actividades registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2010-2014. Fuente: SNIS, formularios 301.

## Qué es

| | |
| --- | --- |
| Gestiones | 2010-2014 |
| Periodicidad | mensual |
| Municipios con registros | 340 |
| Desagregación |  |
| Filas | 13.858 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2010 | 73.029 |
| 2011 | 94.858 |
| 2012 | 80.853 |
| 2013 | 98.019 |
| 2014 | 85.547 |

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
from 'datos/servicios/gestion_comunidad/beneficiarios_as_ninos_as_nuevos_as_del_bono_juana_azurduy/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/gestion_comunidad/beneficiarios_as_ninos_as_nuevos_as_del_bono_juana_azurduy/datos.parquet'
where gestion = 2014 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2010-2013 | 301 | N° de beneficiarios(as) (niños/as) nuevos(as) del bono Juana Azurduy | 1.0.4 (2013) |
| 2014 | 301 | 10.6. N° de beneficiarios(as) (niños/as) nuevos(as) del bono Juana Azurduy | 2.0.0 (2014) |
