# Chagas agudo (2001-2023)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2003, 2010-2023. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2003, 2010-2023 |
| Periodicidad | semanal |
| Municipios con registros | 242 |
| Desagregación | sexo, edad |
| Filas | 42.226 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001-2003 | <1, 1-4, 5-14, 15-59, 60+ |
| 2010-2014 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |
| 2015-2023 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2001 | 1.708 |
| 2002 | 2.975 |
| 2003 | 2.963 |
| 2010 | 2.595 |
| 2011 | 2.505 |
| 2012 | 2.104 |
| 2013 | 3.203 |
| 2014 | 2.655 |
| 2015 | 19.975 |
| 2016 | 17.892 |
| 2017 | 15.911 |
| 2018 | 13.797 |
| 2019 | 13.950 |
| 2020 | 4.498 |
| 2021 | 5.472 |
| 2022 | 3.064 |
| 2023 | 1.294 |

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
from 'datos/vigilancia/casos/chagas_agudo_2001_2023/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/chagas_agudo_2001_2023/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/chagas_agudo_2001_2023/datos.parquet'
where gestion = 2023 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Chagas agudo (2001-2023) (este dataset): 2001-2023, formulario 302, 302a.
- [Chagas agudo (2024-2025)](../../../vigilancia/casos/chagas_agudo_2024_2025/readme.md): 2024-2025, formulario 302a.

Las categorías de `transmision` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/chagas_agudo_2001_2023/datos.parquet',
    'datos/vigilancia/casos/chagas_agudo_2024_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2001-2003 | 302 | 94.- Enfermedades de chagas aguda |  |  |
| 2010-2013 | 302 | Chagas Agudo | 1.0.4 (2013) | B57 |
| 2014 | 302 | Chagas Agudo | 2.0.0 (2014) | B57 |
| 2015 | 302a | Chagas agudo | 3.0.1 (2016) | B57 |
| 2016 | 302a | Chagas agudo | 3.0.2 (2016) | B57 |
| 2017 | 302a | Chagas agudo | 4.0.0 (2018) | B57 |
| 2018 | 302a | Chagas agudo | 4.0.1 (2018) | B57 |
| 2019-2020 | 302a | Chagas agudo | 5.0.1 (2020) | B57 |
| 2021 | 302a | Chagas agudo | 6.0.0 (2021) | B57 |
| 2022-2023 | 302a | Chagas agudo | 6.0.1 (2022) | B57 |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302, 2001-2007: en las variables cuyas columnas "-M" siempre valen 0, "TOTAL-H" es igual a "TOTAL": "-H" contiene a ambos sexos. Esas variables no tienen sexo. En 2004 el grupo 09 (mortalidad) tampoco tiene sexo: hay 79 muertes maternas en "-H" y 94 en "-M".
