# Tratamientos iniciados de tuberculosis y lepra (2024-2025)

Registros en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2024-2025. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2024-2025 |
| Periodicidad | mensual |
| Municipios con registros | 292 |
| Desagregación | esquema, sexo |
| Filas | 4.370 |

Valores de `esquema` (esquema):

- de tb sensible (2024-2025)
- modificado para tb (2024-2025)
- multibacilar (2024-2025)
- paucibacilar (2024-2025)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2024 | 9.676 |
| 2025 | 11.771 |

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
| `sexo` | string | mujer u hombre. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2024_2025/datos.parquet'
group by gestion order by gestion;

-- Por gestión y esquema
select gestion, esquema, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2024_2025/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2024_2025/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Tratamientos iniciados de tuberculosis y lepra (2001-2009)](../../../servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2001_2009/readme.md): 2001-2009, formulario 301.
- [Tratamientos iniciados de tuberculosis y lepra (2010-2023)](../../../servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2010_2023/readme.md): 2010-2023, formulario 301, 301a.
- Tratamientos iniciados de tuberculosis y lepra (2024-2025) (este dataset): 2024-2025, formulario 301a.

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
| 2024-2025 | 301a | Tratamientos iniciados con esquema de TB sensible; Tratamientos iniciados con esquema modificado para TB; Tratamientos iniciados con esquema multibacilar; Tratamientos iniciados con esquema paucibacilar | 7.0.1 (2026) |
