# Cáncer de otras localizaciones (2024-2025)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2024-2025. Fuente: SNIS, formularios 302b.

## Qué es

| | |
| --- | --- |
| Gestiones | 2024-2025 |
| Periodicidad | mensual |
| Municipios con registros | 188 |
| Desagregación | sexo, edad, nuevo o repetido |
| Filas | 14.459 |

Valores de `caso` (nuevo o repetido):

- nuevo (2024-2025)
- repetido (2024-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2024-2025 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2024 | 91.136 |
| 2025 | 99.836 |

### Advertencias

- Excluye las localizaciones que el formulario notifica aparte.

## Cómo utilizar

Cada fila da el número de casos de un periodo, un municipio y una población. Para obtener un total, sume las filas: el dataset no tiene filas de total. Una combinación sin fila significa que no hubo registros. Las convenciones de tiempo, territorio y población están en el [catálogo](../../../README.md#cómo-leer-los-datos).

| Columna | Tipo | Descripción |
| --- | --- | --- |
| `gestion` | integer | Año calendario (gestión) del registro. |
| `mes` | integer | Mes, de 1 a 12. |
| `fecha_inicio` | date | Primer día de la semana o del mes. |
| `departamento` | string | Nombre del departamento. |
| `municipio` | string | Nombre del municipio. |
| `municipio_codigo` | string | Código del municipio, 6 dígitos: departamento (2), provincia (2) y municipio (2). |
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `caso` | string | nuevo, repetido, seguimiento o primera, como lo registra el formulario. |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/cancer_otros_2024_2025/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/cancer_otros_2024_2025/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/cancer_otros_2024_2025/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Cáncer de otras localizaciones (2015-2023)](../../../vigilancia/casos/cancer_otros_2015_2023/readme.md): 2015-2023, formulario 302b.
- Cáncer de otras localizaciones (2024-2025) (este dataset): 2024-2025, formulario 302b.

En 2024 el formulario notifica aparte tiroides, pulmón, estómago, colon y recto, piel y linfomas: desde entonces esta variable excluye esas localizaciones. Consultarlos juntos como una serie supone que las definiciones cuentan lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/cancer_otros_2015_2023/datos.parquet',
    'datos/vigilancia/casos/cancer_otros_2024_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2024-2025 | 302b | Cáncer en sus distintas formas | 7.0.1 (2026) | C00 C01 C02 C03 C04 C05 C06 C07 C08 C09 C10 C11 C12 C13 C14 C15 C17 C18 C19 C22 C23 C24 C25 C26 C30 C31 C32 C33 C34 C37 C38 C39 C40 C41 C42 C45 C46 C47 C48 C49 C51 C52 C56 C57 C58 C60 C62 C63 C64 C65 C66 C67 C68 C69 C70 C71 C72 C74 C75 C76 C77 C78 C79 C80 C96 C97 D00 D01 D02 D04 D05 D07 D09 |
