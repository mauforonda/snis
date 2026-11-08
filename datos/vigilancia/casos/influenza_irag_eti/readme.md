# Influenza (IRAG, IRAGI y ETI)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2015-2025. Fuente: SNIS, formularios 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2025 |
| Periodicidad | semanal |
| Municipios con registros | 191 |
| Desagregación | sexo, edad |
| Filas | 27.414 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015-2025 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2015 | 1.042 |
| 2016 | 3.220 |
| 2017 | 2.704 |
| 2018 | 8.043 |
| 2019 | 2.853 |
| 2020 | 3.628 |
| 2021 | 1.200 |
| 2022 | 2.300 |
| 2023 | 14.599 |
| 2024 | 28.386 |
| 2025 | 27.391 |

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
from 'datos/vigilancia/casos/influenza_irag_eti/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/influenza_irag_eti/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/influenza_irag_eti/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2015 | 302a | Influenza (IRAG ,IRAGI y ETI) | 3.0.1 (2016) | J10 J11 |
| 2016 | 302a | Influenza (IRAG ,IRAGI y ETI) | 3.0.2 (2016) | J10 J11 |
| 2017 | 302a | Influenza (IRAG ,IRAGI y ETI) | 4.0.0 (2018) | J10 J11 |
| 2018 | 302a | Influenza (IRAG ,IRAGI y ETI) | 4.0.1 (2018) | J10 J11 |
| 2019-2020 | 302a | Influenza (IRAG ,IRAGI y ETI) | 5.0.1 (2020) | J10 J11 |
| 2021 | 302a | Influenza (IRAG ,IRAGI y ETI) | 6.0.0 (2021) | J10 J11 |
| 2022-2023 | 302a | Influenza (IRAG ,IRAGI y ETI) | 6.0.1 (2022) | J10 J11 |
| 2024 | 302a | Influenza (IRAG ,IRAGI y ETI) | 7.0.1 (2026) | J10 J11 |
| 2025 | 302a | 15. Influenza (IRAG ,IRAGI y ETI) | 7.0.1 (2026) | J10 J11 |
