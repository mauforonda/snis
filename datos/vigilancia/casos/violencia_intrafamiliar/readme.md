# Violencia intrafamiliar

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2023. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2023 |
| Periodicidad | semanal |
| Municipios con registros | 339 |
| Desagregación | sexo, edad |
| Filas | 70.687 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2004-2007 | <1, 1-4, 5-14, 15-59, 60+ |
| 2008-2014 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |
| 2015-2023 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2001 | 4.181 |
| 2002 | 5.680 |
| 2003 | 6.668 |
| 2004 | 6.850 |
| 2005 | 6.525 |
| 2006 | 6.307 |
| 2007 | 5.632 |
| 2008 | 7.337 |
| 2009 | 6.559 |
| 2010 | 6.998 |
| 2011 | 6.773 |
| 2012 | 6.774 |
| 2013 | 7.770 |
| 2014 | 8.023 |
| 2015 | 6.378 |
| 2016 | 5.689 |
| 2017 | 6.163 |
| 2018 | 4.679 |
| 2019 | 4.601 |
| 2020 | 2.378 |
| 2021 | 2.972 |
| 2022 | 2.911 |
| 2023 | 2.889 |

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
from 'datos/vigilancia/casos/violencia_intrafamiliar/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/violencia_intrafamiliar/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/violencia_intrafamiliar/datos.parquet'
where gestion = 2023 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Violencia intrafamiliar (este dataset): 2001-2023, formulario 302, 302a.
- [Violencia sexual (familiar y en otros ámbitos) (2015-2023)](../../../vigilancia/casos/violencia_sexual_2015_2023/readme.md): 2015-2023, formulario 302a.
- [Violencia física](../../../vigilancia/casos/violencia_fisica/readme.md): 2024-2025, formulario 302a.
- [Violencia por negligencia o abandono](../../../vigilancia/casos/violencia_negligencia/readme.md): 2024-2025, formulario 302a.
- [Violencia sexual (2024-2025)](../../../vigilancia/casos/violencia_sexual_2024_2025/readme.md): 2024-2025, formulario 302a.

Hasta 2023 el formulario notifica la violencia intrafamiliar; desde 2024 separa la violencia física y la sexual, familiar y en otros contextos (columna `ambito`), y la negligencia o abandono. No sabemos qué partes de 2024 equivalen a la violencia intrafamiliar.

- Violencia intrafamiliar (este dataset): 2001-2023, formulario 302, 302a.
- [Violencia intrafamiliar contra niñas y niños](../../../vigilancia/casos/violencia_intrafamiliar_ninez/readme.md): 2001-2003, formulario 302.

En 2001-2003 el formulario notifica aparte la violencia intrafamiliar contra niñas y niños. No sabemos si esos casos están también en la violencia intrafamiliar.

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2001-2003 | 302 | 66.- Violencia contra la mujer; 67.- Violencia contra el hombre |  |  |
| 2004 | 302 | 35 Hombres; 36 Mujeres |  |  |
| 2005-2006 | 302 | 36 Hombres; 37 Mujeres |  |  |
| 2007 | 302 | 36 Intrafamiliar | 1.0.4 (2013) | Y06 Y07 |
| 2008-2009 | 302 | 33 Intrafamiliar/doméstica | 1.0.4 (2013) | Y06 Y07 |
| 2010-2013 | 302 | Intrafamiliar/doméstica | 1.0.4 (2013) | Y06 Y07 |
| 2014 | 302 | Intrafamiliar/doméstica | 2.0.0 (2014) | Y06 Y07 |
| 2015 | 302a | Violencia en la Familia | 3.0.1 (2016) | T74 Y07 |
| 2016 | 302a | Violencia en la Familia | 3.0.2 (2016) | T74 Y07 |
| 2017 | 302a | Violencia en la Familia | 4.0.0 (2018) | T74 Y07 |
| 2018 | 302a | Violencia en la Familia | 4.0.1 (2018) | T74 Y07 |
| 2019-2020 | 302a | Violencia en la Familia | 5.0.1 (2020) | T74 Y07 |
| 2021 | 302a | Violencia en la Familia | 6.0.0 (2021) | T74 Y07 |
| 2022-2023 | 302a | Violencia en la Familia | 6.0.1 (2022) | T74 Y07 |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302, 2001-2007: en las variables cuyas columnas "-M" siempre valen 0, "TOTAL-H" es igual a "TOTAL": "-H" contiene a ambos sexos. Esas variables no tienen sexo. En 2004 el grupo 09 (mortalidad) tampoco tiene sexo: hay 79 muertes maternas en "-H" y 94 en "-M".
- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
