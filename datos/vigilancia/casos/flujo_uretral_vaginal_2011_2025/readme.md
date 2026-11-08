# Flujo uretral o vaginal (2011-2025)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2011-2025. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2011-2025 |
| Periodicidad | semanal |
| Municipios con registros | 342 |
| Desagregación | sexo, edad |
| Filas | 322.269 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2011-2013 | 5-9, 10-20, 21-59, 60+ |
| 2014 | <1, 1-4, 5-9, 10-20, 21-59, 60+ |
| 2015-2025 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2011 | 71.382 |
| 2012 | 80.082 |
| 2013 | 104.097 |
| 2014 | 130.636 |
| 2015 | 168.887 |
| 2016 | 151.437 |
| 2017 | 161.802 |
| 2018 | 177.474 |
| 2019 | 175.433 |
| 2020 | 109.848 |
| 2021 | 143.744 |
| 2022 | 170.890 |
| 2023 | 199.603 |
| 2024 | 202.955 |
| 2025 | 210.273 |

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
from 'datos/vigilancia/casos/flujo_uretral_vaginal_2011_2025/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/flujo_uretral_vaginal_2011_2025/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/flujo_uretral_vaginal_2011_2025/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Flujo uretral o vaginal (2001-2006)](../../../vigilancia/casos/flujo_uretral_vaginal_2001_2006/readme.md): 2001-2006, formulario 302.
- [Flujo uretral o vaginal (2007-2010)](../../../vigilancia/casos/flujo_uretral_vaginal_2007_2010/readme.md): 2007-2010, formulario 302.
- Flujo uretral o vaginal (2011-2025) (este dataset): 2011-2025, formulario 302, 302a.

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
| 2011-2013 | 302 | Flujo uretral (vaginal) | 1.0.4 (2013) | A54 A56 A59 B37 N76 O98 |
| 2014 | 302 | Flujo uretral (vaginal) | 2.0.0 (2014) | A54 A56 A59 B37 N76 O98 |
| 2015 | 302a | Flujo uretral/vaginal | 3.0.1 (2016) | A56 A59 B37 N76 O98 |
| 2016 | 302a | Flujo uretral/vaginal | 3.0.2 (2016) | A56 A59 B37 N76 O98 |
| 2017 | 302a | Flujo uretral/vaginal | 4.0.0 (2018) | A56 A59 B37 N76 O98 |
| 2018 | 302a | Flujo uretral/vaginal | 4.0.1 (2018) | A56 A59 B37 N76 O98 |
| 2019-2020 | 302a | Flujo uretral/vaginal | 5.0.1 (2020) | A56 A59 B37 N76 O98 |
| 2021 | 302a | Flujo uretral/vaginal | 6.0.0 (2021) | A56 A59 B37 N76 O98 |
| 2022-2023 | 302a | Flujo uretral/vaginal | 6.0.1 (2022) | A56 A59 B37 N76 O98 |
| 2024-2025 | 302a | 4. Flujo uretral/vaginal | 7.0.1 (2026) | A56 A59 B37 N76 O98 |
