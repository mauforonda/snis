# Flujo uretral o vaginal (2007-2010)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2007-2010. Fuente: SNIS, formularios 302.

## Qué es

| | |
| --- | --- |
| Gestiones | 2007-2010 |
| Periodicidad | semanal |
| Municipios con registros | 263 |
| Desagregación | sexo, edad |
| Filas | 9.240 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2007 | 5-14, 15-59, 60+ |
| 2008-2010 | 5-9, 10-20, 21-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2007 | 2.984 |
| 2008 | 2.945 |
| 2009 | 2.467 |
| 2010 | 42.182 |

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
from 'datos/vigilancia/casos/flujo_uretral_vaginal_2007_2010/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/flujo_uretral_vaginal_2007_2010/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/flujo_uretral_vaginal_2007_2010/datos.parquet'
where gestion = 2010 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Flujo uretral o vaginal (2001-2006)](../../../vigilancia/casos/flujo_uretral_vaginal_2001_2006/readme.md): 2001-2006, formulario 302.
- Flujo uretral o vaginal (2007-2010) (este dataset): 2007-2010, formulario 302.
- [Flujo uretral o vaginal (2011-2025)](../../../vigilancia/casos/flujo_uretral_vaginal_2011_2025/readme.md): 2011-2025, formulario 302, 302a.

La variable cuenta hombres con flujo uretral (2001-2006), flujo uretral o uretritis sin restringir el sexo (2007-2010) y flujo uretral o vaginal (desde 2011). Consultarlos juntos como una serie supone que las definiciones cuentan lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/flujo_uretral_vaginal_2001_2006/datos.parquet',
    'datos/vigilancia/casos/flujo_uretral_vaginal_2007_2010/datos.parquet',
    'datos/vigilancia/casos/flujo_uretral_vaginal_2011_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2007 | 302 | 20 Flujo uretral (uretritis) |  |  |
| 2008-2009 | 302 | 21 Flujo uretral (uretritis) | 1.0.4 (2013) | A54 A56 A59 B37 N76 O98 |
| 2010 | 302 | Flujo uretral (uretritis) | 1.0.4 (2013) | A54 A56 A59 B37 N76 O98 |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302, 2001-2007: en las variables cuyas columnas "-M" siempre valen 0, "TOTAL-H" es igual a "TOTAL": "-H" contiene a ambos sexos. Esas variables no tienen sexo. En 2004 el grupo 09 (mortalidad) tampoco tiene sexo: hay 79 muertes maternas en "-H" y 94 en "-M".
