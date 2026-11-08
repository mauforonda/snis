# Reacciones adversas a fármacos antituberculosos (2008-2023)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2008-2023. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2008-2023 |
| Periodicidad | semanal |
| Municipios con registros | 205 |
| Desagregación | gravedad, sexo, edad |
| Filas | 3.146 |

Valores de `gravedad` (gravedad):

- grave (2008-2023)
- leve o moderada (2008-2023)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2008-2014 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |
| 2015 | 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2016 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2017 | 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2018 | <6m, 1-4, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2019 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2020 | 1-4, 5-9, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2021 | 6-11m, 1-4, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2022 | 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2023 | 1-4, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2008 | 459 |
| 2009 | 597 |
| 2010 | 540 |
| 2011 | 262 |
| 2012 | 278 |
| 2013 | 245 |
| 2014 | 281 |
| 2015 | 186 |
| 2016 | 193 |
| 2017 | 198 |
| 2018 | 207 |
| 2019 | 291 |
| 2020 | 65 |
| 2021 | 119 |
| 2022 | 124 |
| 2023 | 112 |

### Advertencias

- En 2015-2023 la variable se llama "RAFA", sin calificar; se publica como leve o moderada porque el formulario notifica las graves aparte.

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
| `gravedad` | string | Gravedad. |
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/reacciones_adversas_antituberculosos_2008_2023/datos.parquet'
group by gestion order by gestion;

-- Por gestión y gravedad
select gestion, gravedad, sum(casos) as casos
from 'datos/vigilancia/casos/reacciones_adversas_antituberculosos_2008_2023/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/reacciones_adversas_antituberculosos_2008_2023/datos.parquet'
where gestion = 2023 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Reacciones adversas a fármacos antituberculosos (2008-2023) (este dataset): 2008-2023, formulario 302, 302a.
- [Reacciones adversas graves a fármacos antituberculosos (2024-2025)](../../../vigilancia/casos/reacciones_adversas_antituberculosos_2024_2025/readme.md): 2024-2025, formulario 302a.

Las categorías de `gravedad` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/reacciones_adversas_antituberculosos_2008_2023/datos.parquet',
    'datos/vigilancia/casos/reacciones_adversas_antituberculosos_2024_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2008-2009 | 302 | 29 RAFA Reacciones adversas (leves y moderadas); 30 RAFA Reacciones adversas (graves) | 1.0.4 (2013) | Y40 Y41 |
| 2010-2013 | 302 | RAFA (graves); RAFA (leves y moderadas) | 1.0.4 (2013) | Y40 Y41 |
| 2014 | 302 | RAFA (graves); RAFA (leves y moderadas) | 2.0.0 (2014) | Y40 Y41 |
| 2015 | 302a | Reaccion Adversa a Farmacos Antituberculosos (RAFA); Reaccion Adversa a Farmacos Antituberculosos RAFA (graves) | 3.0.1 (2016) | Y40 Y41 |
| 2016 | 302a | Reaccion Adversa a Farmacos Antituberculosos (RAFA); Reaccion Adversa a Farmacos Antituberculosos RAFA (graves) | 3.0.2 (2016) | Y40 Y41 |
| 2017 | 302a | Reaccion Adversa a Farmacos Antituberculosos (RAFA); Reaccion Adversa a Farmacos Antituberculosos RAFA (graves) | 4.0.0 (2018) | Y40 Y41 |
| 2018 | 302a | Reaccion Adversa a Farmacos Antituberculosos (RAFA); Reaccion Adversa a Farmacos Antituberculosos RAFA (graves) | 4.0.1 (2018) | Y40 Y41 |
| 2019-2020 | 302a | Reaccion Adversa a Farmacos Antituberculosos (RAFA); Reaccion Adversa a Farmacos Antituberculosos RAFA (graves) | 5.0.1 (2020) | Y40 Y41 |
| 2021 | 302a | Reaccion Adversa a Farmacos Antituberculosos (RAFA); Reaccion Adversa a Farmacos Antituberculosos RAFA (graves) | 6.0.0 (2021) | Y40 Y41 |
| 2022-2023 | 302a | Reaccion Adversa a Farmacos Antituberculosos (RAFA); Reaccion Adversa a Farmacos Antituberculosos RAFA (graves) | 6.0.1 (2022) | Y40 Y41 |
