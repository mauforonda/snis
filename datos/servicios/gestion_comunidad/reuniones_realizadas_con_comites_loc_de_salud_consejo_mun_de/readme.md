# Reuniones realizadas con comités loc. de salud/consejo mun. de salud

Actividades registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2010-2014. Fuente: SNIS, formularios 301.

## Qué es

| | |
| --- | --- |
| Gestiones | 2010-2014 |
| Periodicidad | mensual |
| Municipios con registros | 338 |
| Desagregación |  |
| Filas | 9.046 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2010 | 5.462 |
| 2011 | 5.652 |
| 2012 | 5.679 |
| 2013 | 6.323 |
| 2014 | 8.826 |

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
from 'datos/servicios/gestion_comunidad/reuniones_realizadas_con_comites_loc_de_salud_consejo_mun_de/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/gestion_comunidad/reuniones_realizadas_con_comites_loc_de_salud_consejo_mun_de/datos.parquet'
where gestion = 2014 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Reuniones realizadas con comités loc. de salud/consejo mun. de salud (este dataset): 2010-2014, formulario 301.
- [Reuniones realizadas con comités loc. de salud](../../../servicios/gestion_comunidad/reuniones_realizadas_con_comites_loc_de_salud/readme.md): 2015-2025, formulario 301a.

Hasta 2014 la variable cuenta reuniones con comités locales de salud o con el consejo municipal de salud; desde 2015, sólo con comités locales de salud. Consultarlos juntos como una serie supone que las reuniones con el consejo municipal no cambian la serie.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/gestion_comunidad/reuniones_realizadas_con_comites_loc_de_salud_consejo_mun_de/datos.parquet',
    'datos/servicios/gestion_comunidad/reuniones_realizadas_con_comites_loc_de_salud/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2010-2013 | 301 | N° de reuniones realizadas con Comités Loc. De Salud/Consejo Mun. De Salud | 1.0.4 (2013) |
| 2014 | 301 | 10.4. N° de reuniones realizadas con Comités Loc. De Salud/Consejo Mun. De Salud | 2.0.0 (2014) |
