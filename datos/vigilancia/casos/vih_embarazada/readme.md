# VIH reactivo en la mujer embarazada

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2010-2025. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2010-2025 |
| Periodicidad | semanal |
| Municipios con registros | 226 |
| Desagregación | sexo, edad |
| Filas | 8.213 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2010 | 10-20, 21-59 |
| 2011 | 10-20, 21-59, 60+ |
| 2012 | 10-20, 21-59 |
| 2013-2014 | 10-20, 21-59, 60+ |
| 2015-2017 | 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2018 | 10-14, 15-19, 20-39, 40-49, 50-59 |
| 2019 | 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2020 | 10-14, 15-19, 20-39, 40-49, 50-59 |
| 2021 | 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2022 | 10-14, 15-19, 20-39, 40-49, 50-59 |
| 2023 | 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2024-2025 | 10-14, 15-19, 20-39, 40-49, 50-59 |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2010 | 320 |
| 2011 | 426 |
| 2012 | 154 |
| 2013 | 2.607 |
| 2014 | 8.203 |
| 2015 | 10.584 |
| 2016 | 3.449 |
| 2017 | 3.157 |
| 2018 | 2.329 |
| 2019 | 1.986 |
| 2020 | 857 |
| 2021 | 3.211 |
| 2022 | 2.005 |
| 2023 | 1.265 |
| 2024 | 1.343 |
| 2025 | 1.095 |

### Advertencias

- Registros implausibles: hay filas con una población que la definición excluye. Se publican tal como se registraron; pueden ser errores de registro o de codificación. Están en la tabla "Registros implausibles".

### Registros implausibles

| Sexo | Edad | Casos | % del total | Gestiones | Municipios |
| --- | --- | ---: | ---: | --- | ---: |
| hombre | 15-19 | 2 | 0,00% | 2017, 2023 | 1 |
| mujer | 60+ | 136 | 0,32% | 2011, 2013-2017, 2019, 2021, 2023 | 9 |

Para excluirlos:

```sql
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/vih_embarazada/datos.parquet'
where not coalesce((sexo = 'hombre' and edad_grupo = '15-19')
    or (sexo = 'mujer' and edad_grupo = '60+'), false)
group by gestion order by gestion;
```

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
from 'datos/vigilancia/casos/vih_embarazada/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/vih_embarazada/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/vih_embarazada/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2010-2013 | 302 | VIH Mujer Embarazada | 1.0.4 (2013) | Z21 |
| 2014 | 302 | VIH Mujer Embarazada | 2.0.0 (2014) | Z21 |
| 2015 | 302a | Prueba rápida reactiva de VIH en Mujer Embarazada | 3.0.1 (2016) |  |
| 2016 | 302a | Prueba rápida reactiva de VIH en Mujer Embarazada | 3.0.2 (2016) |  |
| 2017 | 302a | Prueba rápida reactiva de VIH en Mujer Embarazada | 4.0.0 (2018) |  |
| 2018 | 302a | Prueba rápida reactiva de VIH en Mujer Embarazada | 4.0.1 (2018) |  |
| 2019-2020 | 302a | Prueba rápida reactiva de VIH en Mujer Embarazada | 5.0.1 (2020) |  |
| 2021 | 302a | Prueba rápida reactiva de VIH en Mujer Embarazada | 6.0.0 (2021) |  |
| 2022-2023 | 302a | Prueba rápida reactiva de VIH en Mujer Embarazada | 6.0.1 (2022) |  |
| 2024-2025 | 302a | 7. Prueba rápida reactiva de VIH en Mujer Embarazada | 7.0.1 (2026) |  |
