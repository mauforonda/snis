# Hemorragia del parto o puerperio

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2004-2006. Fuente: SNIS, formularios 302.

## Qué es

| | |
| --- | --- |
| Gestiones | 2004-2006 |
| Periodicidad | semanal |
| Municipios con registros | 246 |
| Desagregación | sexo |
| Filas | 3.177 |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2004 | 2.675 |
| 2005 | 1.924 |
| 2006 | 1.641 |

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
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/hemorragia_parto_puerperio/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/hemorragia_parto_puerperio/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/hemorragia_parto_puerperio/datos.parquet'
where gestion = 2006 group by all order by casos desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2004 | 302 | 50 Hemorragia del parto o puerperio |  |
| 2005-2006 | 302 | 46 Hemorragia del parto o puerperio |  |
