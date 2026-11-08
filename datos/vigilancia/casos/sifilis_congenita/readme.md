# Sífilis congénita

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2003, 2015-2025. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2003, 2015-2025 |
| Periodicidad | semanal |
| Municipios con registros | 149 |
| Desagregación | sexo, edad |
| Filas | 2.287 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001 | <1, 1-4, 15-59 |
| 2002 | <1, 1-4, 5-14, 15-59, 60+ |
| 2003 | <1, 15-59 |
| 2015-2025 | <6m |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2001 | 158 |
| 2002 | 182 |
| 2003 | 71 |
| 2015 | 172 |
| 2016 | 164 |
| 2017 | 208 |
| 2018 | 233 |
| 2019 | 285 |
| 2020 | 229 |
| 2021 | 206 |
| 2022 | 244 |
| 2023 | 317 |
| 2024 | 270 |
| 2025 | 330 |

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
from 'datos/vigilancia/casos/sifilis_congenita/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/sifilis_congenita/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/sifilis_congenita/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2001-2003 | 302 | 51.- Sífilis congénita - nacido vivo |  |  |
| 2015 | 302a | Sifilis Congénita | 3.0.1 (2016) | A50 |
| 2016 | 302a | Sifilis Congénita | 3.0.2 (2016) | A50 |
| 2017 | 302a | Sifilis Congénita | 4.0.0 (2018) | A50 |
| 2018 | 302a | Sifilis Congénita | 4.0.1 (2018) | A50 |
| 2019-2020 | 302a | Sifilis Congénita | 5.0.1 (2020) | A50 |
| 2021 | 302a | Sifilis Congénita | 6.0.0 (2021) | A50 |
| 2022-2023 | 302a | Sifilis Congénita | 6.0.1 (2022) | A50 |
| 2024-2025 | 302a | 2. Sifilis Congénita | 7.0.1 (2026) | A50 |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302, 2001-2007: en las variables cuyas columnas "-M" siempre valen 0, "TOTAL-H" es igual a "TOTAL": "-H" contiene a ambos sexos. Esas variables no tienen sexo. En 2004 el grupo 09 (mortalidad) tampoco tiene sexo: hay 79 muertes maternas en "-H" y 94 en "-M".
