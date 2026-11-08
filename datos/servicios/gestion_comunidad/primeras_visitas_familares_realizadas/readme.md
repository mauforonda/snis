# Primeras visitas familares realizadas

Actividades registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2024-2025. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2024-2025 |
| Periodicidad | mensual |
| Municipios con registros | 342 |
| Desagregación |  |
| Filas | 7.115 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2024 | 540.364 |
| 2025 | 656.096 |

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
from 'datos/servicios/gestion_comunidad/primeras_visitas_familares_realizadas/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/gestion_comunidad/primeras_visitas_familares_realizadas/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Visitas familiares realizadas](../../../servicios/gestion_comunidad/visitas_familiares_realizadas/readme.md): 2015-2023, formulario 301a.
- Primeras visitas familares realizadas (este dataset): 2024-2025, formulario 301a.
- [Segundas visitas familiares realizadas](../../../servicios/gestion_comunidad/segundas_visitas_familiares_realizadas/readme.md): 2024-2025, formulario 301a.
- [Terceras visitas familiares](../../../servicios/gestion_comunidad/terceras_visitas_familiares/readme.md): 2024-2025, formulario 301a.

Hasta 2023 el formulario cuenta las visitas familiares realizadas; desde 2024, la primera, la segunda y la tercera visita. Consultarlos juntos como una serie supone que las tres suman lo mismo que "visitas realizadas"; el formulario no lo dice.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/gestion_comunidad/visitas_familiares_realizadas/datos.parquet',
    'datos/servicios/gestion_comunidad/primeras_visitas_familares_realizadas/datos.parquet',
    'datos/servicios/gestion_comunidad/segundas_visitas_familiares_realizadas/datos.parquet',
    'datos/servicios/gestion_comunidad/terceras_visitas_familiares/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2024-2025 | 301a | Nro de Primeras visitas Familares realizadas | 7.0.1 (2026) |
