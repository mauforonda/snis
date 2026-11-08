# Malaria: viviendas rociadas

Registros en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2003. Fuente: SNIS, formularios 301.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2003 |
| Periodicidad | mensual |
| Municipios con registros | 118 |
| Desagregación |  |
| Filas | 427 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 27.152 |
| 2002 | 23.184 |
| 2003 | 52.138 |

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
from 'datos/servicios/control_enfermedades/malaria_viviendas_rociadas/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/malaria_viviendas_rociadas/datos.parquet'
where gestion = 2003 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Malaria: viviendas rociadas (este dataset): 2001-2003, formulario 301.
- [Malaria: viviendas rociadas por agente comunario](../../../servicios/control_enfermedades/malaria_viviendas_rociadas_por_agente_comunario/readme.md): 2005-2006, formulario 301.
- [Malaria: viviendas rociadas por personal de salud](../../../servicios/control_enfermedades/malaria_viviendas_rociadas_por_personal_de_salud/readme.md): 2005-2006, formulario 301.

Las viviendas rociadas contra la malaria se cuentan en total (2001-2003) y por quién rocía (2005-2006). Consultarlos juntos como una serie supone que las dos categorías suman todas las viviendas rociadas.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/control_enfermedades/malaria_viviendas_rociadas/datos.parquet',
    'datos/servicios/control_enfermedades/malaria_viviendas_rociadas_por_agente_comunario/datos.parquet',
    'datos/servicios/control_enfermedades/malaria_viviendas_rociadas_por_personal_de_salud/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2003 | 301 | Viviendas rociadas |  |
