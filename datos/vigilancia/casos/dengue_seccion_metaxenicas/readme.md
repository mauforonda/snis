# Dengue (sección enfermedades metaxénicas)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2004, 2015-2020. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2004, 2015-2020 |
| Periodicidad | semanal |
| Municipios con registros | 162 |
| Desagregación | sexo, edad |
| Filas | 30.098 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001-2004 | <1, 1-4, 5-14, 15-59, 60+ |
| 2015-2019 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2020 | 10-14, 20-39, 50-59 |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2001 | 116 |
| 2002 | 753 |
| 2003 | 4.722 |
| 2004 | 6.260 |
| 2015 | 27.013 |
| 2016 | 32.325 |
| 2017 | 9.171 |
| 2018 | 7.686 |
| 2019 | 3.619 |
| 2020 | 3 |

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
from 'datos/vigilancia/casos/dengue_seccion_metaxenicas/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/dengue_seccion_metaxenicas/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/dengue_seccion_metaxenicas/datos.parquet'
where gestion = 2020 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Dengue (sección enfermedades metaxénicas) (este dataset): 2001-2020, formulario 302, 302a.
- [Dengue hemorrágico (2002-2004)](../../../vigilancia/casos/dengue_2002_2004/readme.md): 2002-2004, formulario 302.
- [Dengue por clasificación clínica (2005-2014)](../../../vigilancia/casos/dengue_2005_2014/readme.md): 2005-2014, formulario 302.
- [Dengue grave (2015-2018)](../../../vigilancia/casos/dengue_2015_2018/readme.md): 2015-2018, formulario 302a.
- [Dengue por clasificación clínica (2019-2025)](../../../vigilancia/casos/dengue_2019_2025/readme.md): 2019-2025, formulario 302a.

El formulario registra el dengue en dos secciones, con cifras distintas: enfermedades metaxénicas (2001-2004 y 2015-2020), sin clasificación clínica, y dengue por clasificación clínica. En 2015-2018 la clasificación clínica sólo tiene dengue grave: la mayoría de los casos de esos años está en la sección de enfermedades metaxénicas. No las sume: un caso puede estar en ambas.

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2001-2003 | 302 | 93.- Dengue |  |  |
| 2004 | 302 | 25 Dengue |  |  |
| 2015 | 302a | Dengue | 3.0.1 (2016) | A90 |
| 2016 | 302a | Dengue | 3.0.2 (2016) | A90 |
| 2017 | 302a | Dengue | 4.0.0 (2018) | A90 |
| 2018-2020 | 302a | Dengue | 4.0.1 (2018) | A90 |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302, 2001-2007: en las variables cuyas columnas "-M" siempre valen 0, "TOTAL-H" es igual a "TOTAL": "-H" contiene a ambos sexos. Esas variables no tienen sexo. En 2004 el grupo 09 (mortalidad) tampoco tiene sexo: hay 79 muertes maternas en "-H" y 94 en "-M".
