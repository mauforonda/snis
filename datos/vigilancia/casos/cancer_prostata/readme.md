# Cáncer de próstata

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2018, 2020-2025. Fuente: SNIS, formularios 302b.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2018, 2020-2025 |
| Periodicidad | mensual |
| Municipios con registros | 168 |
| Desagregación | sexo, edad, nuevo o repetido |
| Filas | 5.699 |

Valores de `caso` (nuevo o repetido):

- nuevo (2015-2018, 2020-2025)
- repetido (2015-2018, 2020-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015 | 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2016 | 15-19, 20-39, 40-49, 50-59, 60+ |
| 2017 | 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2018 | 15-19, 20-39, 40-49, 50-59, 60+ |
| 2020-2022 | 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2023 | 15-19, 20-39, 40-49, 50-59, 60+ |
| 2024-2025 | 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2015 | 3.228 |
| 2016 | 4.236 |
| 2017 | 7.210 |
| 2018 | 8.589 |
| 2020 | 6.167 |
| 2021 | 8.746 |
| 2022 | 12.525 |
| 2023 | 15.281 |
| 2024 | 18.633 |
| 2025 | 22.647 |

### Advertencias

- Registros implausibles: hay filas con una población que la definición excluye. Se publican tal como se registraron; pueden ser errores de registro o de codificación. Están en la tabla "Registros implausibles".

### Registros implausibles

| Sexo | Edad | Casos | % del total | Gestiones | Municipios |
| --- | --- | ---: | ---: | --- | ---: |
| mujer | 10-14 | 24 | 0,02% | 2021-2022 | 3 |
| mujer | 15-19 | 15 | 0,01% | 2022 | 1 |
| mujer | 20-39 | 3 | 0,00% | 2021 | 1 |
| mujer | 40-49 | 2 | 0,00% | 2021 | 1 |

Para excluirlos:

```sql
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/cancer_prostata/datos.parquet'
where not coalesce((sexo = 'mujer' and edad_grupo = '10-14')
    or (sexo = 'mujer' and edad_grupo = '15-19')
    or (sexo = 'mujer' and edad_grupo = '20-39')
    or (sexo = 'mujer' and edad_grupo = '40-49'), false)
group by gestion order by gestion;
```

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
from 'datos/vigilancia/casos/cancer_prostata/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/cancer_prostata/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/cancer_prostata/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2015 | 302b | Cancer de prostata | 3.0.1 (2016) | C61 |
| 2016 | 302b | Cancer de prostata | 3.0.2 (2016) | C61 |
| 2017 | 302b | Cancer de prostata | 4.0.0 (2018) | C61 |
| 2018 | 302b | Cancer de prostata | 4.0.1 (2018) | C61 |
| 2020 | 302b | Cancer de prostata | 5.0.1 (2020) | C61 |
| 2021 | 302b | Cancer de prostata | 6.0.0 (2021) | C61 |
| 2022-2023 | 302b | Cancer de prostata | 6.0.1 (2022) | C61 |
| 2024-2025 | 302b | Cáncer de Próstata | 7.0.1 (2026) | C61 D07 |
