# Malaria (sospecha)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2010-2014. Fuente: SNIS, formularios 302.

## Qué es

| | |
| --- | --- |
| Gestiones | 2010-2014 |
| Periodicidad | semanal |
| Municipios con registros | 194 |
| Desagregación | sexo, edad |
| Filas | 46.576 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2010-2014 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2010 | 61.275 |
| 2011 | 58.235 |
| 2012 | 64.738 |
| 2013 | 70.757 |
| 2014 | 52.959 |

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
from 'datos/vigilancia/casos/malaria_sospecha/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/malaria_sospecha/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/malaria_sospecha/datos.parquet'
where gestion = 2014 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Malaria (2001-2009)](../../../vigilancia/casos/malaria_2001_2009/readme.md): 2001-2009, formulario 302.
- [Malaria (2010-2014)](../../../vigilancia/casos/malaria_2010_2014/readme.md): 2010-2014, formulario 302.
- Malaria (sospecha) (este dataset): 2010-2014, formulario 302.
- [Malaria (2015-2025)](../../../vigilancia/casos/malaria_2015_2025/readme.md): 2015-2025, formulario 302a.

En 2010-2014 el formulario notifica por separado los casos de malaria confirmados y los sospechosos; antes y después, una sola variable, "Malaria". Consultarlos juntos como una serie supone que "Malaria" equivale a los confirmados, o a confirmados más sospechosos; el formulario no dice cuál.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/malaria_2001_2009/datos.parquet',
    'datos/vigilancia/casos/malaria_2010_2014/datos.parquet',
    'datos/vigilancia/casos/malaria_sospecha/datos.parquet',
    'datos/vigilancia/casos/malaria_2015_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2010-2013 | 302 | Malaria Sospechosos | 1.0.4 (2013) | Z03 |
| 2014 | 302 | Malaria Sospechosos | 2.0.0 (2014) | Z03 |
