# Sífilis en la mujer embarazada

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2011-2025. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2011-2025 |
| Periodicidad | semanal |
| Municipios con registros | 286 |
| Desagregación | sexo, edad |
| Filas | 9.239 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2011-2014 | 10-20, 21-59, 60+ |
| 2015-2025 | 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2011 | 959 |
| 2012 | 930 |
| 2013 | 1.023 |
| 2014 | 1.571 |
| 2015 | 1.697 |
| 2016 | 1.519 |
| 2017 | 1.662 |
| 2018 | 1.245 |
| 2019 | 1.261 |
| 2020 | 804 |
| 2021 | 856 |
| 2022 | 849 |
| 2023 | 800 |
| 2024 | 955 |
| 2025 | 1.237 |

### Advertencias

- Registros implausibles: hay filas con una población que la definición excluye. Se publican tal como se registraron; pueden ser errores de registro o de codificación. Están en la tabla "Registros implausibles".

### Registros implausibles

| Sexo | Edad | Casos | % del total | Gestiones | Municipios |
| --- | --- | ---: | ---: | --- | ---: |
| hombre | 21-59 | 10 | 0,06% | 2014 | 1 |
| mujer | 60+ | 331 | 1,91% | 2011-2025 | 67 |

Para excluirlos:

```sql
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/sifilis_embarazada/datos.parquet'
where not coalesce((sexo = 'hombre' and edad_grupo = '21-59')
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
from 'datos/vigilancia/casos/sifilis_embarazada/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/sifilis_embarazada/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/sifilis_embarazada/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2011-2013 | 302 | Sifilis en la mujer embarazada | 1.0.4 (2013) | O98 |
| 2014 | 302 | Sifilis en la mujer embarazada | 2.0.0 (2014) | O98 |
| 2015 | 302a | Sífilis en la mujer embarazada* | 3.0.1 (2016) | O98 |
| 2016 | 302a | Sífilis en la mujer embarazada* | 3.0.2 (2016) | O98 |
| 2017 | 302a | Sífilis en la mujer embarazada* | 4.0.0 (2018) | O98 |
| 2018 | 302a | Sífilis en la mujer embarazada* | 4.0.1 (2018) | O98 |
| 2019-2020 | 302a | Sífilis en la mujer embarazada* | 5.0.1 (2020) | O98 |
| 2021 | 302a | Sífilis en la mujer embarazada* | 6.0.0 (2021) | O98 |
| 2022-2023 | 302a | Sífilis en la mujer embarazada* | 6.0.1 (2022) | O98 |
| 2024-2025 | 302a | 3. Sífilis en la mujer embarazada (confirmado por laboratorio)* | 7.0.1 (2026) | O98 |
