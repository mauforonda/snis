# Malaria (2015-2025)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2015-2025. Fuente: SNIS, formularios 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2025 |
| Periodicidad | semanal |
| Municipios con registros | 147 |
| Desagregación | sexo, edad |
| Filas | 95.015 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015-2025 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2015 | 59.394 |
| 2016 | 52.870 |
| 2017 | 53.335 |
| 2018 | 54.656 |
| 2019 | 37.417 |
| 2020 | 32.724 |
| 2021 | 26.353 |
| 2022 | 25.867 |
| 2023 | 44.629 |
| 2024 | 47.998 |
| 2025 | 31.794 |

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
from 'datos/vigilancia/casos/malaria_2015_2025/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/malaria_2015_2025/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/malaria_2015_2025/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Malaria (2001-2009)](../../../vigilancia/casos/malaria_2001_2009/readme.md): 2001-2009, formulario 302.
- [Malaria (2010-2014)](../../../vigilancia/casos/malaria_2010_2014/readme.md): 2010-2014, formulario 302.
- Malaria (2015-2025) (este dataset): 2015-2025, formulario 302a.

En 2010-2014 la variable es "Malaria confirmados" y el formulario notifica los casos sospechosos aparte; antes y después, "Malaria". Consultarlos juntos como una serie supone que las definiciones cuentan lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/malaria_2001_2009/datos.parquet',
    'datos/vigilancia/casos/malaria_2010_2014/datos.parquet',
    'datos/vigilancia/casos/malaria_2015_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

- [Malaria (2001-2009)](../../../vigilancia/casos/malaria_2001_2009/readme.md): 2001-2009, formulario 302.
- [Malaria (2010-2014)](../../../vigilancia/casos/malaria_2010_2014/readme.md): 2010-2014, formulario 302.
- [Malaria (sospecha)](../../../vigilancia/casos/malaria_sospecha/readme.md): 2010-2014, formulario 302.
- Malaria (2015-2025) (este dataset): 2015-2025, formulario 302a.

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
| 2015 | 302a | Malaria | 3.0.1 (2016) | B50 B51 B52 B53 B54 |
| 2016 | 302a | Malaria | 3.0.2 (2016) | B50 B51 B52 B53 B54 |
| 2017 | 302a | Malaria | 4.0.0 (2018) | B50 B51 B52 B53 B54 |
| 2018 | 302a | Malaria | 4.0.1 (2018) | B50 B51 B52 B53 B54 |
| 2019-2020 | 302a | Malaria | 5.0.1 (2020) | B50 B51 B52 B53 B54 |
| 2021 | 302a | Malaria | 6.0.0 (2021) | B50 B51 B52 B53 B54 |
| 2022-2023 | 302a | Malaria | 6.0.1 (2022) | B50 B51 B52 B53 B54 |
| 2024-2025 | 302a | 6. Malaria | 7.0.1 (2026) | B50 B51 B52 B53 B54 |
