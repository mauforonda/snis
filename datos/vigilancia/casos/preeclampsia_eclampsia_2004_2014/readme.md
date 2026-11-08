# Preeclampsia severa o eclampsia (2004-2014)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2004-2014. Fuente: SNIS, formularios 302.

## Qué es

| | |
| --- | --- |
| Gestiones | 2004-2014 |
| Periodicidad | semanal |
| Municipios con registros | 300 |
| Desagregación | sexo |
| Filas | 11.184 |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2004 | 1.446 |
| 2005 | 2.083 |
| 2006 | 2.028 |
| 2007 | 6.162 |
| 2008 | 3.196 |
| 2009 | 3.503 |
| 2010 | 3.860 |
| 2011 | 4.115 |
| 2012 | 3.704 |
| 2013 | 4.228 |
| 2014 | 4.164 |

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
| `sexo` | string | mujer u hombre. |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/preeclampsia_eclampsia_2004_2014/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/preeclampsia_eclampsia_2004_2014/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/preeclampsia_eclampsia_2004_2014/datos.parquet'
where gestion = 2014 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Preeclampsia severa o eclampsia (2004-2014) (este dataset): 2004-2014, formulario 302.
- [Preeclampsia y eclampsia (2015-2025)](../../../vigilancia/casos/preeclampsia_eclampsia_2015_2025/readme.md): 2015-2025, formulario 302a.

Las categorías de `diagnostico` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/preeclampsia_eclampsia_2004_2014/datos.parquet',
    'datos/vigilancia/casos/preeclampsia_eclampsia_2015_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2004 | 302 | 52 Preeclampsia severa/eclampsia | 1.0.4 (2013) |
| 2005-2006 | 302 | 48 Preeclampsia severa/eclampsia | 1.0.4 (2013) |
| 2007 | 302 | 47 Preeclampsia severa/eclampsia | 1.0.4 (2013) |
| 2008-2009 | 302 | 46 Preeclampsia severa/eclampsia | 1.0.4 (2013) |
| 2010-2013 | 302 | Preeclampsia severa/eclampsia | 1.0.4 (2013) |
| 2014 | 302 | Preeclampsia severa/eclampsia | 2.0.0 (2014) |
