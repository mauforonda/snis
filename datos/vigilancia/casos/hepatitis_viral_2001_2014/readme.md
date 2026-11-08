# Hepatitis viral (2001-2014)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2014. Fuente: SNIS, formularios 302.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2014 |
| Periodicidad | semanal |
| Municipios con registros | 271 |
| Desagregación | sexo, edad |
| Filas | 33.469 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001-2007 | <1, 1-4, 5-14, 15-59, 60+ |
| 2008-2014 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2001 | 2.578 |
| 2002 | 4.843 |
| 2003 | 4.707 |
| 2004 | 5.802 |
| 2005 | 5.325 |
| 2006 | 4.171 |
| 2007 | 5.797 |
| 2008 | 3.656 |
| 2009 | 4.282 |
| 2010 | 5.875 |
| 2011 | 4.679 |
| 2012 | 6.163 |
| 2013 | 6.150 |
| 2014 | 5.472 |

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
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/hepatitis_viral_2001_2014/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/hepatitis_viral_2001_2014/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/hepatitis_viral_2001_2014/datos.parquet'
where gestion = 2014 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Hepatitis viral (2001-2014) (este dataset): 2001-2014, formulario 302.
- [Hepatitis viral (2015-2020)](../../../vigilancia/casos/hepatitis_viral_2015_2020/readme.md): 2015-2020, formulario 302a.
- [Hepatitis viral (2021-2023)](../../../vigilancia/casos/hepatitis_viral_2021_2023/readme.md): 2021-2023, formulario 302a.
- [Hepatitis viral (2024-2025)](../../../vigilancia/casos/hepatitis_viral_2024_2025/readme.md): 2024-2025, formulario 302a.

Las categorías de `tipo` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/hepatitis_viral_2001_2014/datos.parquet',
    'datos/vigilancia/casos/hepatitis_viral_2015_2020/datos.parquet',
    'datos/vigilancia/casos/hepatitis_viral_2021_2023/datos.parquet',
    'datos/vigilancia/casos/hepatitis_viral_2024_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2001-2003 | 302 | 41.- Hepatitis viral | 1.0.4 (2013) | B15 B16 B17 B18 B19 |
| 2004-2007 | 302 | 17 Hepatitis | 1.0.4 (2013) | B15 B16 B17 B18 B19 |
| 2008-2009 | 302 | 18 Hepatitis viral | 1.0.4 (2013) | B15 B16 B17 B18 B19 |
| 2010-2013 | 302 | Hepatitis viral | 1.0.4 (2013) | B15 B16 B17 B18 B19 |
| 2014 | 302 | Hepatitis viral | 2.0.0 (2014) | B15 B16 B17 B18 B19 |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302, 2001-2007: en las variables cuyas columnas "-M" siempre valen 0, "TOTAL-H" es igual a "TOTAL": "-H" contiene a ambos sexos. Esas variables no tienen sexo. En 2004 el grupo 09 (mortalidad) tampoco tiene sexo: hay 79 muertes maternas en "-H" y 94 en "-M".
