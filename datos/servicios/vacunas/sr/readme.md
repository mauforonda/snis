# Vacuna SR (sarampión y rubéola)

Dosis aplicadas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2007, 2021-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2007, 2021-2025 |
| Periodicidad | mensual |
| Municipios con registros | 343 |
| Desagregación | sexo, edad, lugar |
| Filas | 77.073 |

Valores de `lugar` (lugar):

- dentro (2001-2007, 2021-2025)
- fuera (2001-2007, 2021-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001-2007 | 2-4 |
| 2024-2025 | 5-9, 10, 11, 12-20, 21-59 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 198.905 |
| 2002 | 208.148 |
| 2003 | 377.790 |
| 2004 | 75.988 |
| 2005 | 71.577 |
| 2006 | 44.940 |
| 2007 | 401.218 |
| 2021 | 124.479 |
| 2022 | 201.784 |
| 2023 | 348.347 |
| 2024 | 73.397 |
| 2025 | 1.250.458 |

## Cómo utilizar

Cada fila da el número de cantidad de un periodo, un municipio y una población. Para obtener un total, sume las filas: el dataset no tiene filas de total. Una combinación sin fila significa que no hubo registros. Las convenciones de tiempo, territorio y población están en el [catálogo](../../../README.md#cómo-leer-los-datos).

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
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/sr/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/sr/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/sr/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2007 | 301 | Vacunaciones dentro de servicio; Vacunaciones fuera de servicio |  |
| 2021 | 301a | 17.21 SR | 6.0.0 (2021) |
| 2022-2023 | 301a | 17.21 SR | 6.0.1 (2022) |
| 2024-2025 | 301a | SR | 7.0.1 (2026) |
