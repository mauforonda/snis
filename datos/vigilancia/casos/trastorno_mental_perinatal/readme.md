# Trastornos mentales del embarazo, parto y puerperio

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2024-2025. Fuente: SNIS, formularios 302b.

## Qué es

| | |
| --- | --- |
| Gestiones | 2024-2025 |
| Periodicidad | mensual |
| Municipios con registros | 8 |
| Desagregación | sexo, edad, nuevo o repetido |
| Filas | 69 |

Valores de `caso` (nuevo o repetido):

- nuevo (2024-2025)
- repetido (2024-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2024 | 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2025 | 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2024 | 43 |
| 2025 | 71 |

### Advertencias

- SOAPS cuenta esta variable cuando uno de los campos de diagnóstico tiene un código F53 (trastornos del puerperio), sin filtro de sexo. Los hombres de este dataset son pacientes registrados como hombres con ese código: pueden ser errores de sexo o de código. El instructivo de 2024 define el trastorno sólo en la madre.
- Registros implausibles: hay filas con una población que la definición excluye. Se publican tal como se registraron; pueden ser errores de registro o de codificación. Están en la tabla "Registros implausibles".

### Registros implausibles

| Sexo | Edad | Casos | % del total | Gestiones | Municipios |
| --- | --- | ---: | ---: | --- | ---: |
| hombre | 10-14 | 7 | 6,14% | 2024-2025 | 2 |
| hombre | 15-19 | 4 | 3,51% | 2024 | 1 |
| hombre | 20-39 | 31 | 27,19% | 2024-2025 | 5 |
| hombre | 40-49 | 8 | 7,02% | 2024-2025 | 4 |
| hombre | 5-9 | 2 | 1,75% | 2024 | 1 |
| hombre | 50-59 | 8 | 7,02% | 2025 | 2 |
| hombre | 60+ | 5 | 4,39% | 2025 | 2 |
| mujer | 60+ | 4 | 3,51% | 2024-2025 | 2 |

Para excluirlos:

```sql
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/trastorno_mental_perinatal/datos.parquet'
where not coalesce((sexo = 'hombre' and edad_grupo = '10-14')
    or (sexo = 'hombre' and edad_grupo = '15-19')
    or (sexo = 'hombre' and edad_grupo = '20-39')
    or (sexo = 'hombre' and edad_grupo = '40-49')
    or (sexo = 'hombre' and edad_grupo = '5-9')
    or (sexo = 'hombre' and edad_grupo = '50-59')
    or (sexo = 'hombre' and edad_grupo = '60+')
    or (sexo = 'mujer' and edad_grupo = '60+'), false)
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
from 'datos/vigilancia/casos/trastorno_mental_perinatal/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/trastorno_mental_perinatal/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/trastorno_mental_perinatal/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2024-2025 | 302b | Trastornos mental asociado al embarazo parto y pue | 7.0.1 (2026) | F53 |
