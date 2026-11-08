# Meningitis meningocócica

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2014. Fuente: SNIS, formularios 302.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2014 |
| Periodicidad | semanal |
| Municipios con registros | 34 |
| Desagregación | edad |
| Filas | 202 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001-2002 | <1, 1-4, 5-14, 15-59 |
| 2003 | <1, 15-59 |
| 2004 | <1, 1-4, 5-14, 15-59 |
| 2005 | <1, 1-4, 15-59, 60+ |
| 2006 | <1, 5-14, 15-59, 60+ |
| 2007 | <1, 1-4, 15-59 |
| 2008-2009 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |
| 2010 | <1, 1-4, 5-9, 10-20, 21-59 |
| 2011 | <1, 5-9, 21-59 |
| 2012 | <1, 5-9, 10-20, 21-59 |
| 2013 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |
| 2014 | <1, 1-4, 5-9, 10-20, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2001 | 9 |
| 2002 | 32 |
| 2003 | 11 |
| 2004 | 19 |
| 2005 | 15 |
| 2006 | 5 |
| 2007 | 10 |
| 2008 | 26 |
| 2009 | 29 |
| 2010 | 15 |
| 2011 | 4 |
| 2012 | 13 |
| 2013 | 19 |
| 2014 | 19 |

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
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/meningitis_meningococica/datos.parquet'
group by gestion order by gestion;

-- Por gestión y edad_grupo
select gestion, edad_grupo, sum(casos) as casos
from 'datos/vigilancia/casos/meningitis_meningococica/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/meningitis_meningococica/datos.parquet'
where gestion = 2014 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Meningitis por Haemophilus influenzae](../../../vigilancia/casos/meningitis_haemophilus/readme.md): 2001-2003, formulario 302.
- Meningitis meningocócica (este dataset): 2001-2014, formulario 302.
- [Meningitis (sección otras infecciones, 2001-2003)](../../../vigilancia/casos/meningitis_seccion_otras_infecciones/readme.md): 2001-2003, formulario 302.
- [Meningitis tuberculosa](../../../vigilancia/casos/meningitis_tuberculosa/readme.md): 2001-2003, formulario 302.

En 2001-2003 el formulario registra esta enfermedad en dos secciones, con cifras distintas: "Sospecha diagnóstica" y otra sección. No sabemos qué cuenta cada una. La de sospecha continúa desde 2004: para una serie larga, use esa. No las sume: un caso puede estar en ambas.

- Meningitis meningocócica (este dataset): 2001-2014, formulario 302.
- [Enfermedad meningocócica](../../../vigilancia/casos/enfermedad_meningococica/readme.md): 2015-2025, formulario 302a.

Hasta 2014 el formulario notifica la meningitis meningocócica; desde 2015, la enfermedad meningocócica, una definición más amplia. Consultarlos juntos como una serie supone que la definición más amplia no cambia la serie.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/meningitis_meningococica/datos.parquet',
    'datos/vigilancia/casos/enfermedad_meningococica/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2001-2003 | 302 | 29.- Meningitis meningococcica |  |  |
| 2004 | 302 | 12 Menin. Meningocócica |  |  |
| 2005-2009 | 302 | 10 Menin. Meningocócica |  |  |
| 2010-2013 | 302 | Meningitis meningocócica | 1.0.4 (2013) | A39 |
| 2014 | 302 | Meningitis meningocócica | 2.0.0 (2014) | A39 |
