# Desarrollo infantil temprano

Niñas y niños evaluados, por resultado en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2024-2025. Fuente: SNIS, formularios 302b.

## Qué es

| | |
| --- | --- |
| Gestiones | 2024-2025 |
| Periodicidad | mensual |
| Municipios con registros | 265 |
| Desagregación | resultado, sexo, edad |
| Filas | 32.371 |

Valores de `resultado` (resultado):

- adecuado (2024-2025)
- rezago grave (2024-2025)
- rezago leve (2024-2025)
- rezago moderado (2024-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2024-2025 | <1, 1, 2-4 |

Total por gestión:

| Gestión | Personas |
| ---: | ---: |
| 2024 | 242.989 |
| 2025 | 293.041 |

## Cómo utilizar

Cada fila da el número de personas de un periodo, un municipio y una población. Para obtener un total, sume las filas: el dataset no tiene filas de total. Una combinación sin fila significa que no hubo registros. Las convenciones de tiempo, territorio y población están en el [catálogo](../../../README.md#cómo-leer-los-datos).

| Columna | Tipo | Descripción |
| --- | --- | --- |
| `gestion` | integer | Año calendario (gestión) del registro. |
| `mes` | integer | Mes, de 1 a 12. |
| `fecha_inicio` | date | Primer día de la semana o del mes. |
| `departamento` | string | Nombre del departamento. |
| `municipio` | string | Nombre del municipio. |
| `municipio_codigo` | string | Código del municipio, 6 dígitos: departamento (2), provincia (2) y municipio (2). |
| `resultado` | string | Resultado. |
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `personas` | integer | Número de personas en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(personas) as personas
from 'datos/vigilancia/desarrollo_infantil/desarrollo_infantil/datos.parquet'
group by gestion order by gestion;

-- Por gestión y resultado
select gestion, resultado, sum(personas) as personas
from 'datos/vigilancia/desarrollo_infantil/desarrollo_infantil/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(personas) as personas
from 'datos/vigilancia/desarrollo_infantil/desarrollo_infantil/datos.parquet'
where gestion = 2025 group by all order by personas desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2024-2025 | 302b | Desarrollo adecuado; Rezago Grave en el Desarrollo; Rezago Leve en el desarrollo; Rezago Moderado en el desarrollo | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302b, grupos 01, 05, 06, 07 y 10: el segundo nivel dice NUEVO/REPETIDO, pero las reglas de SOAPS dividen estas variables por sexo. Las muertes por cáncer de mama y de cuello uterino están en REPETIDO en todas las gestiones 2016-2025, y el tabaco y el alcohol (grupo 01, 2024-2025) están sobre todo en NUEVO: REPETIDO es mujer y NUEVO es hombre.
