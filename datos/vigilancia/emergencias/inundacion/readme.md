# Inundación

Eventos y personas afectadas en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2010-2025. Fuente: SNIS, formularios 302, 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2010-2025 |
| Periodicidad | semanal |
| Municipios con registros | 144 |
| Desagregación | medida |
| Filas | 999 |

Valores de `medida` (medida):

- eventos (2010-2015, 2024-2025)
- personas_afectadas (2010-2015, 2024-2025)
- personas_fallecidas (2010-2011, 2014, 2024-2025)
- pacientes_atendidos (2025)
- personas_damnificadas (2025)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2010 | 14.316 |
| 2011 | 24.744 |
| 2012 | 3.629 |
| 2013 | 2.281 |
| 2014 | 106.156 |
| 2015 | 4.635 |
| 2016 | 1.267 |
| 2017 | 3.412 |
| 2018 | 8.410 |
| 2019 | 3.709 |
| 2020 | 1.305 |
| 2021 | 8.943 |
| 2022 | 638 |
| 2023 | 1.260 |
| 2024 | 3.001 |
| 2025 | 27.291 |

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
from 'datos/vigilancia/emergencias/inundacion/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/vigilancia/emergencias/inundacion/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2010-2013 | 302 | Inundación | 1.0.4 (2013) |
| 2014 | 302 | Inundación | 2.0.0 (2014) |
| 2015 | 302a | Inundación |  |
| 2016 | 302a | Inundación | 3.0.2 (2016) |
| 2017 | 302a | Inundación | 4.0.0 (2018) |
| 2018 | 302a | Inundación | 4.0.1 (2018) |
| 2019-2020 | 302a | Inundación | 5.0.1 (2020) |
| 2021 | 302a | Inundación | 6.0.0 (2021) |
| 2022-2023 | 302a | Inundación | 6.0.1 (2022) |
| 2024 | 302a | Inundación |  |
| 2025 | 302a | 08. Inundación | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
