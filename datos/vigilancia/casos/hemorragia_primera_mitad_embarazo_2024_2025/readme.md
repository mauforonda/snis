# Hemorragia de la primera mitad del embarazo (2024-2025)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2024-2025. Fuente: SNIS, formularios 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2024-2025 |
| Periodicidad | semanal |
| Municipios con registros | 180 |
| Desagregación | desenlace, sexo, edad, lugar |
| Filas | 11.577 |

Valores de `desenlace` (desenlace):

- no especificado (2024-2025)
- terminó en aborto (2024-2025)

Valores de `lugar` (lugar):

- dentro (2024-2025)
- fuera (2024-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2024-2025 | 10-14, 15-19, 20-39, 40-49, 50-59 |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2024 | 20.570 |
| 2025 | 20.698 |

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
| `desenlace` | string | Desenlace. |
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/hemorragia_primera_mitad_embarazo_2024_2025/datos.parquet'
group by gestion order by gestion;

-- Por gestión y desenlace
select gestion, desenlace, sum(casos) as casos
from 'datos/vigilancia/casos/hemorragia_primera_mitad_embarazo_2024_2025/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/hemorragia_primera_mitad_embarazo_2024_2025/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Hemorragia de la primera mitad del embarazo (2001-2009)](../../../vigilancia/casos/hemorragia_primera_mitad_embarazo_2001_2009/readme.md): 2001-2009, formulario 302.
- [Hemorragia de la primera mitad del embarazo (2010-2014)](../../../vigilancia/casos/hemorragia_primera_mitad_embarazo_2010_2014/readme.md): 2010-2014, formulario 302.
- [Hemorragia de la primera mitad del embarazo (2015-2023)](../../../vigilancia/casos/hemorragia_primera_mitad_embarazo_2015_2023/readme.md): 2015-2023, formulario 302a.
- Hemorragia de la primera mitad del embarazo (2024-2025) (este dataset): 2024-2025, formulario 302a.

Las categorías de `desenlace` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo. En 2024 las dos partes suman lo mismo que la variable única de 2023 (20.570 y 19.761). En 2010-2014 suman unos 32 mil, más que la variable única de 2009 (21.905) y de 2015 (20.426): pueden superponerse.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/hemorragia_primera_mitad_embarazo_2001_2009/datos.parquet',
    'datos/vigilancia/casos/hemorragia_primera_mitad_embarazo_2010_2014/datos.parquet',
    'datos/vigilancia/casos/hemorragia_primera_mitad_embarazo_2015_2023/datos.parquet',
    'datos/vigilancia/casos/hemorragia_primera_mitad_embarazo_2024_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2024-2025 | 302a | 1. Hemorragia de la primera mitad del embarazo (< 22 sem); 2. Hemorragia de la primera mitad del embarazo (< 22 sem) que termino en aborto | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302a, grupo 10, 2024-2025: el segundo nivel dice FEMENINO/MASCULINO, pero SOAPS 7.0.1 divide por lugar. Las complicaciones atendidas dentro del establecimiento son muchas más que fuera (preeclampsia 2025: 2.513 frente a 137): MASCULINO es dentro y FEMENINO es fuera.
