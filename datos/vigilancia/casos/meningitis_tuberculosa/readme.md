# Meningitis tuberculosa

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2003. Fuente: SNIS, formularios 302.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2003 |
| Periodicidad | semanal |
| Municipios con registros | 10 |
| Desagregación | edad |
| Filas | 72 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001 | 1-4, 5-14, 15-59, 60+ |
| 2002 | <1, 1-4, 5-14, 15-59 |
| 2003 | <1, 1-4, 5-14, 15-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2001 | 40 |
| 2002 | 12 |
| 2003 | 32 |

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
from 'datos/vigilancia/casos/meningitis_tuberculosa/datos.parquet'
group by gestion order by gestion;

-- Por gestión y edad_grupo
select gestion, edad_grupo, sum(casos) as casos
from 'datos/vigilancia/casos/meningitis_tuberculosa/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/meningitis_tuberculosa/datos.parquet'
where gestion = 2003 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Meningitis por Haemophilus influenzae](../../../vigilancia/casos/meningitis_haemophilus/readme.md): 2001-2003, formulario 302.
- [Meningitis meningocócica](../../../vigilancia/casos/meningitis_meningococica/readme.md): 2001-2014, formulario 302.
- [Meningitis (sección otras infecciones, 2001-2003)](../../../vigilancia/casos/meningitis_seccion_otras_infecciones/readme.md): 2001-2003, formulario 302.
- Meningitis tuberculosa (este dataset): 2001-2003, formulario 302.

En 2001-2003 el formulario registra esta enfermedad en dos secciones, con cifras distintas: "Sospecha diagnóstica" y otra sección. No sabemos qué cuenta cada una. La de sospecha continúa desde 2004: para una serie larga, use esa. No las sume: un caso puede estar en ambas.

- [Meningitis tuberculosa en menores de 5 años](../../../vigilancia/casos/meningitis_tb_menor_5/readme.md): 2001-2009, formulario 302.
- Meningitis tuberculosa (este dataset): 2001-2003, formulario 302.
- [Tuberculosis meníngea](../../../vigilancia/casos/tuberculosis_meningea/readme.md): 2010-2025, formulario 302, 302a.

El formulario notifica la meningitis tuberculosa en todas las edades (2001-2003) y en menores de 5 años (2001-2009); desde 2010, la tuberculosis meníngea en todas las edades. Consultarlos juntos como una serie supone que las tres variables cuentan lo mismo en las edades que comparten; filtre por edad antes de unirlas.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/meningitis_tb_menor_5/datos.parquet',
    'datos/vigilancia/casos/meningitis_tuberculosa/datos.parquet',
    'datos/vigilancia/casos/tuberculosis_meningea/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2003 | 302 | 36.- Meningitis tuberculosa |  |
