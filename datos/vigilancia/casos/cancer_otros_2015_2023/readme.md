# Cáncer de otras localizaciones (2015-2023)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2018, 2020-2023. Fuente: SNIS, formularios 302b.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2018, 2020-2023 |
| Periodicidad | mensual |
| Municipios con registros | 270 |
| Desagregación | sexo, edad, nuevo o repetido |
| Filas | 32.132 |

Valores de `caso` (nuevo o repetido):

- nuevo (2015-2018, 2020-2023)
- repetido (2015-2018, 2020-2023)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015-2018 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2020-2023 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2015 | 17.218 |
| 2016 | 10.397 |
| 2017 | 21.078 |
| 2018 | 28.187 |
| 2020 | 25.526 |
| 2021 | 57.392 |
| 2022 | 79.808 |
| 2023 | 99.397 |

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
from 'datos/vigilancia/casos/cancer_otros_2015_2023/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/cancer_otros_2015_2023/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/cancer_otros_2015_2023/datos.parquet'
where gestion = 2023 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Cáncer de otras localizaciones (2015-2023) (este dataset): 2015-2023, formulario 302b.
- [Cáncer de otras localizaciones (2024-2025)](../../../vigilancia/casos/cancer_otros_2024_2025/readme.md): 2024-2025, formulario 302b.

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
| 2015 | 302b | Cancer en sus distintas formas | 3.0.1 (2016) | C00 C01 C02 C03 C04 C05 C06 C07 C08 C09 C10 C11 C12 C13 C14 C15 C16 C17 C18 C19 C20 C21 C22 C23 C24 C25 C26 C30 C31 C32 C33 C34 C37 C38 C39 C40 C41 C43 C44 C45 C46 C47 C48 C49 C51 C52 C56 C57 C58 C60 C96 C97 |
| 2016 | 302b | Cancer en sus distintas formas | 3.0.2 (2016) | C00 C01 C02 C03 C04 C05 C06 C07 C08 C09 C10 C11 C12 C13 C14 C15 C16 C17 C18 C19 C20 C21 C22 C23 C24 C25 C26 C30 C31 C32 C33 C34 C37 C38 C39 C40 C41 C43 C44 C45 C46 C47 C48 C49 C51 C52 C56 C57 C58 C60 C96 C97 |
| 2017 | 302b | Cancer en sus distintas formas | 4.0.0 (2018) | C00 C01 C02 C03 C04 C05 C06 C07 C08 C09 C10 C11 C12 C13 C14 C15 C16 C17 C18 C19 C20 C21 C22 C23 C24 C25 C26 C30 C31 C32 C33 C34 C37 C38 C39 C40 C41 C43 C44 C45 C46 C47 C48 C49 C51 C52 C56 C57 C58 C60 C96 C97 |
| 2018 | 302b | Cancer en sus distintas formas | 4.0.1 (2018) | C00 C01 C02 C03 C04 C05 C06 C07 C08 C09 C10 C11 C12 C13 C14 C15 C16 C17 C18 C19 C20 C21 C22 C23 C24 C25 C26 C30 C31 C32 C33 C34 C37 C38 C39 C40 C41 C43 C44 C45 C46 C47 C48 C49 C51 C52 C56 C57 C58 C60 C96 C97 |
| 2020 | 302b | Cancer en sus distintas formas | 5.0.1 (2020) | C00 C01 C02 C03 C04 C05 C06 C07 C08 C09 C10 C11 C12 C13 C14 C15 C16 C17 C18 C19 C20 C21 C22 C23 C24 C25 C26 C30 C31 C32 C33 C34 C37 C38 C39 C40 C41 C43 C44 C45 C46 C47 C48 C49 C51 C52 C56 C57 C58 C60 C96 C97 |
| 2021 | 302b | Cancer en sus distintas formas | 6.0.0 (2021) | C00 C01 C02 C03 C04 C05 C06 C07 C08 C09 C10 C11 C12 C13 C14 C15 C16 C17 C18 C19 C20 C21 C22 C23 C24 C25 C26 C30 C31 C32 C33 C34 C37 C38 C39 C40 C41 C43 C44 C45 C46 C47 C48 C49 C51 C52 C56 C57 C58 C60 C96 C97 |
| 2022-2023 | 302b | Cancer en sus distintas formas | 6.0.1 (2022) | C00 C01 C02 C03 C04 C05 C06 C07 C08 C09 C10 C11 C12 C13 C14 C15 C16 C17 C18 C19 C20 C21 C22 C23 C24 C25 C26 C30 C31 C32 C33 C34 C37 C38 C39 C40 C41 C43 C44 C45 C46 C47 C48 C49 C51 C52 C56 C57 C58 C60 C96 C97 |
