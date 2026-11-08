# Vacuna dT (difteria y tétanos) (2001-2003)

Dosis aplicadas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2003. Fuente: SNIS, formularios 301.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2003 |
| Periodicidad | mensual |
| Municipios con registros | 312 |
| Desagregación | dosis, sexo, edad |
| Filas | 42.898 |

Valores de `dosis` (dosis):

- 1 (2001-2003)
- 2 (2001-2003)
- 3 (2001-2003)
- 4 (2001-2003)
- 5 (2001-2003)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001-2003 | 15-49 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 1.072.373 |
| 2002 | 941.437 |
| 2003 | 826.760 |

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
| `dosis` | string | Dosis: número (1 a 5), inicial, única, anual o refuerzo. |
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/dt_2001_2003/datos.parquet'
group by gestion order by gestion;

-- Por gestión y dosis
select gestion, dosis, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/dt_2001_2003/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/dt_2001_2003/datos.parquet'
where gestion = 2003 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Vacuna dT (difteria y tétanos) (2001-2003) (este dataset): 2001-2003, formulario 301.
- [Vacuna dT (difteria y tétanos) (2004-2007)](../../../servicios/vacunas/dt_2004_2007/readme.md): 2004-2007, formulario 301.
- [Vacuna dT (difteria y tétanos) (2008-2025)](../../../servicios/vacunas/dt_2008_2025/readme.md): 2008-2025, formulario 301, 301a.

Las categorías de `dosis` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/vacunas/dt_2001_2003/datos.parquet',
    'datos/servicios/vacunas/dt_2004_2007/datos.parquet',
    'datos/servicios/vacunas/dt_2008_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2003 | 301 | Mujeres de 15 a 49 años 1ra dosis de dT; Mujeres de 15 a 49 años 2da dosis de dT; Mujeres de 15 a 49 años 3da dosis de dT; Mujeres de 15 a 49 años 4da dosis de dT; Mujeres de 15 a 49 años 5ta dosis de dT |  |
