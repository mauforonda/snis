# Intoxicación por plaguicidas (2021-2025)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2021-2025. Fuente: SNIS, formularios 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2021-2025 |
| Periodicidad | semanal |
| Municipios con registros | 254 |
| Desagregación | agente, sexo, edad |
| Filas | 5.977 |

Valores de `agente` (agente):

- halogenados (2021-2025)
- herbicidas y fungicidas (2021-2025)
- organofosforados y carbamatos (2021-2025)
- otros plaguicidas e insecticidas (2021-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2021-2025 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2021 | 1.347 |
| 2022 | 1.272 |
| 2023 | 1.370 |
| 2024 | 1.547 |
| 2025 | 1.425 |

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
| `agente` | string | Agente de la intoxicación. |
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/intoxicacion_plaguicidas_2021_2025/datos.parquet'
group by gestion order by gestion;

-- Por gestión y agente
select gestion, agente, sum(casos) as casos
from 'datos/vigilancia/casos/intoxicacion_plaguicidas_2021_2025/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/intoxicacion_plaguicidas_2021_2025/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Intoxicación por organofosforados y carbamatos (2001-2003)](../../../vigilancia/casos/intoxicacion_plaguicidas_2001_2003/readme.md): 2001-2003, formulario 302.
- [Intoxicación por plaguicidas (2004-2020)](../../../vigilancia/casos/intoxicacion_plaguicidas_2004_2020/readme.md): 2004-2020, formulario 302, 302a.
- Intoxicación por plaguicidas (2021-2025) (este dataset): 2021-2025, formulario 302a.

Las categorías de `agente` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/intoxicacion_plaguicidas_2001_2003/datos.parquet',
    'datos/vigilancia/casos/intoxicacion_plaguicidas_2004_2020/datos.parquet',
    'datos/vigilancia/casos/intoxicacion_plaguicidas_2021_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2021 | 302a | Halogenados; Herbicida y fungicida; Organofosforados , carbamatos; Otros plaguicidas/insecticidas | 6.0.0 (2021) | T60 X48 |
| 2022-2023 | 302a | Halogenados; Herbicida y fungicida; Organofosforados , carbamatos; Otros plaguicidas/insecticidas | 6.0.1 (2022) | T60 X48 |
| 2024-2025 | 302a | 1. Organofosforados , carbamatos; 2. Halogenados; 3. Herbicida y fungicida; 4. Otros plaguicidas/insecticidas | 7.0.1 (2026) | T60 X48 X68 Y18 |
