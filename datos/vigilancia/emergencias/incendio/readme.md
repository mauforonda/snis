# Incendio

Eventos y personas afectadas en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2010-2025. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2010-2025 |
| Periodicidad | semanal |
| Municipios con registros | 161 |
| Desagregación | medida |
| Filas | 966 |

Valores de `medida` (medida):

- eventos (2010-2015, 2024-2025)
- personas_afectadas (2010-2015, 2024-2025)
- personas_fallecidas (2010-2011, 2013, 2015, 2024-2025)
- pacientes_atendidos (2025)
- personas_damnificadas (2025)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2010 | 1.574 |
| 2011 | 1.611 |
| 2012 | 141 |
| 2013 | 537 |
| 2014 | 84 |
| 2015 | 41 |
| 2016 | 321 |
| 2017 | 2.756 |
| 2018 | 36 |
| 2019 | 5.854 |
| 2020 | 6.347 |
| 2021 | 488 |
| 2022 | 1.950 |
| 2023 | 6.343 |
| 2024 | 3.699 |
| 2025 | 3.466 |

## Cómo utilizar

Cada fila da el número de cantidad de un periodo, un municipio y una población. Para obtener un total, sume las filas: el dataset no tiene filas de total. Una combinación sin fila significa que no hubo registros. Las convenciones de tiempo, territorio y población están en el [catálogo](../../../README.md#cómo-leer-los-datos).

| Columna | Tipo | Descripción |
| --- | --- | --- |
| `gestion` | integer | Año calendario (gestión) del registro. |
| `semana` | integer | Semana epidemiológica, de 1 a 53. Va de domingo a sábado. |
| `fecha_inicio` | date | Primer día de la semana o del mes. |
| `departamento` | string | Nombre del departamento. |
| `municipio` | string | Nombre del municipio. |
| `municipio_codigo` | string | Código del municipio, 6 dígitos: departamento (2), provincia (2) y municipio (2). |
| `medida` | string | Qué se cuenta: eventos, personas afectadas, fallecidas, damnificadas o pacientes atendidos. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/vigilancia/emergencias/incendio/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/vigilancia/emergencias/incendio/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2010-2013 | 302 | Incendio | 1.0.4 (2013) |
| 2014 | 302 | Incendio | 2.0.0 (2014) |
| 2015 | 302a | Incendio |  |
| 2016 | 302a | Incendio | 3.0.2 (2016) |
| 2017 | 302a | Incendio | 4.0.0 (2018) |
| 2018 | 302a | Incendio | 4.0.1 (2018) |
| 2019-2020 | 302a | Incendio | 5.0.1 (2020) |
| 2021 | 302a | Incendio | 6.0.0 (2021) |
| 2022-2023 | 302a | Incendio | 6.0.1 (2022) |
| 2024 | 302a | Incendio |  |
| 2025 | 302a | 04. Incendio | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
