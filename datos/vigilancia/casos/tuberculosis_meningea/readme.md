# Tuberculosis meníngea

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2010-2016, 2018-2025. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2010-2016, 2018-2025 |
| Periodicidad | semanal |
| Municipios con registros | 60 |
| Desagregación | sexo, edad |
| Filas | 275 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2010-2012 | <1, 1-4 |
| 2013-2014 | 1-4 |
| 2015 | <6m, 1-4 |
| 2016 | 6-11m, 1-4 |
| 2018-2019 | 1-4 |
| 2020 | <6m, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2021 | <6m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2022 | 15-19, 20-39, 50-59, 60+ |
| 2023 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2024 | <6m, 6-11m, 1-4, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2025 | <6m, 1-4, 5-9, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2010 | 12 |
| 2011 | 31 |
| 2012 | 5 |
| 2013 | 1 |
| 2014 | 5 |
| 2015 | 4 |
| 2016 | 2 |
| 2018 | 9 |
| 2019 | 4 |
| 2020 | 27 |
| 2021 | 31 |
| 2022 | 15 |
| 2023 | 49 |
| 2024 | 60 |
| 2025 | 52 |

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
from 'datos/vigilancia/casos/tuberculosis_meningea/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/tuberculosis_meningea/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/tuberculosis_meningea/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Meningitis tuberculosa en menores de 5 años](../../../vigilancia/casos/meningitis_tb_menor_5/readme.md): 2001-2009, formulario 302.
- [Meningitis tuberculosa](../../../vigilancia/casos/meningitis_tuberculosa/readme.md): 2001-2003, formulario 302.
- Tuberculosis meníngea (este dataset): 2010-2025, formulario 302, 302a.

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

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2010-2013 | 302 | Tuberculosis Meningea | 1.0.4 (2013) | A17 |
| 2014 | 302 | Tuberculosis Meningea | 2.0.0 (2014) | A17 |
| 2015 | 302a | Tuberculosis Meningea | 3.0.1 (2016) | A17 |
| 2016 | 302a | Tuberculosis Meningea | 3.0.2 (2016) | A17 |
| 2018 | 302a | Tuberculosis Meningea | 4.0.1 (2018) | A17 |
| 2019-2020 | 302a | Tuberculosis Meningea | 5.0.1 (2020) | A17 |
| 2021 | 302a | Tuberculosis Meningea | 6.0.0 (2021) | A17 |
| 2022-2023 | 302a | Tuberculosis Meningea | 6.0.1 (2022) | A17 |
| 2024-2025 | 302a | 1. Tuberculosis Meningea | 7.0.1 (2026) | A17 |
