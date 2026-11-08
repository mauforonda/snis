# Tétanos (2001-2009)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2009. Fuente: SNIS, formularios 302.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2009 |
| Periodicidad | semanal |
| Municipios con registros | 81 |
| Desagregación | tipo, sexo, edad |
| Filas | 309 |

Valores de `tipo` (tipo):

- adulto (2001-2009)
- neonatal (2001-2009)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001 | <1, 5-14, 15-59, 60+ |
| 2002 | <1, 1-4, 15-59, 60+ |
| 2003-2007 | <1, 1-4, 5-14, 15-59, 60+ |
| 2008 | <1, 5-9, 10-20, 21-59, 60+ |
| 2009 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2001 | 18 |
| 2002 | 31 |
| 2003 | 22 |
| 2004 | 36 |
| 2005 | 85 |
| 2006 | 68 |
| 2007 | 65 |
| 2008 | 33 |
| 2009 | 57 |

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
| `tipo` | string | Tipo. |
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/tetanos_2001_2009/datos.parquet'
group by gestion order by gestion;

-- Por gestión y tipo
select gestion, tipo, sum(casos) as casos
from 'datos/vigilancia/casos/tetanos_2001_2009/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/tetanos_2001_2009/datos.parquet'
where gestion = 2009 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Tétanos (2001-2009) (este dataset): 2001-2009, formulario 302.
- [Tétanos (neonatal y del adulto) (2010-2025)](../../../vigilancia/casos/tetanos_2010_2025/readme.md): 2010-2025, formulario 302, 302a.

Las categorías de `tipo` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/tetanos_2001_2009/datos.parquet',
    'datos/vigilancia/casos/tetanos_2010_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2001-2003 | 302 | 38.- Tétanos neonatal; 39.- Tétanos de adulto | 1.0.4 (2013) | A33 A34 A35 |
| 2004-2006 | 302 | 15 Tétanos neonatal; 16 Tétanos del adulto | 1.0.4 (2013) | A33 A34 A35 |
| 2007 | 302 | 15 Tétanos neonatal; 16 Tétanos | 1.0.4 (2013) | A33 A34 A35 |
| 2008-2009 | 302 | 16 Tétanos neonatal; 17 Tétanos | 1.0.4 (2013) | A33 A34 A35 |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302, 2001-2007: en las variables cuyas columnas "-M" siempre valen 0, "TOTAL-H" es igual a "TOTAL": "-H" contiene a ambos sexos. Esas variables no tienen sexo. En 2004 el grupo 09 (mortalidad) tampoco tiene sexo: hay 79 muertes maternas en "-H" y 94 en "-M".
