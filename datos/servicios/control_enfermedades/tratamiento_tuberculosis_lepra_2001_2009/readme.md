# Tratamientos iniciados de tuberculosis y lepra (2001-2009)

Registros en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2009. Fuente: SNIS, formularios 301.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2009 |
| Periodicidad | mensual |
| Municipios con registros | 316 |
| Desagregación | esquema |
| Filas | 19.199 |

Valores de `esquema` (esquema):

- I (2001-2009)
- II (2001-2009)
- III (2001-2009)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 10.868 |
| 2002 | 11.402 |
| 2003 | 10.347 |
| 2004 | 9.379 |
| 2005 | 8.856 |
| 2006 | 8.466 |
| 2007 | 8.752 |
| 2008 | 8.698 |
| 2009 | 8.879 |

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
| `esquema` | string | Esquema de tratamiento. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2001_2009/datos.parquet'
group by gestion order by gestion;

-- Por gestión y esquema
select gestion, esquema, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2001_2009/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2001_2009/datos.parquet'
where gestion = 2009 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Tratamientos iniciados de tuberculosis y lepra (2001-2009) (este dataset): 2001-2009, formulario 301.
- [Tratamientos iniciados de tuberculosis y lepra (2010-2023)](../../../servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2010_2023/readme.md): 2010-2023, formulario 301, 301a.
- [Tratamientos iniciados de tuberculosis y lepra (2024-2025)](../../../servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2024_2025/readme.md): 2024-2025, formulario 301a.

Las categorías de `esquema` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2001_2009/datos.parquet',
    'datos/servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2010_2023/datos.parquet',
    'datos/servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2024_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2007 | 301 | Tratamientos iniciados con esquema l; Tratamientos iniciados con esquema ll; Tratamientos iniciados con esquema lll |  |
| 2008-2009 | 301 | Tratamientos iniciados con esquema l; Tratamientos iniciados con esquema ll; Tratamientos iniciados con esquema lll | 1.0.4 (2013) |
