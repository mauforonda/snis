# Sarampión y rubéola (2001-2003)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2003. Fuente: SNIS, formularios 302.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2003 |
| Periodicidad | semanal |
| Municipios con registros | 116 |
| Desagregación | enfermedad, edad |
| Filas | 1.562 |

Valores de `enfermedad` (enfermedad):

- rubéola (2001-2003)
- sarampión (2001-2003)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001 | <1, 1-4, 5-14, 15-59, 60+ |
| 2002 | <1, 1-4, 5-14, 15-59 |
| 2003 | <1, 1-4, 5-14, 15-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2001 | 2.014 |
| 2002 | 723 |
| 2003 | 303 |

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
| `enfermedad` | string | Enfermedad. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/sarampion_rubeola_2001_2003/datos.parquet'
group by gestion order by gestion;

-- Por gestión y enfermedad
select gestion, enfermedad, sum(casos) as casos
from 'datos/vigilancia/casos/sarampion_rubeola_2001_2003/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/sarampion_rubeola_2001_2003/datos.parquet'
where gestion = 2003 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Sarampión y rubéola (2001-2003) (este dataset): 2001-2003, formulario 302.
- [Sarampión y rubéola (2004)](../../../vigilancia/casos/sarampion_rubeola_2004/readme.md): 2004, formulario 302.
- [Sarampión o rubéola (2005-2025)](../../../vigilancia/casos/sarampion_rubeola_2005_2025/readme.md): 2005-2025, formulario 302, 302a.

Las categorías de `enfermedad` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/sarampion_rubeola_2001_2003/datos.parquet',
    'datos/vigilancia/casos/sarampion_rubeola_2004/datos.parquet',
    'datos/vigilancia/casos/sarampion_rubeola_2005_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2001-2003 | 302 | 18.- Sarampión; 19.- Rubéola | 1.0.4 (2013) | B05 B06 |
