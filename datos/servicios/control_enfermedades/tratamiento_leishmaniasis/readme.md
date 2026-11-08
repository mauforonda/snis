# Tratamientos de leishmaniasis

Registros en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2010-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2010-2025 |
| Periodicidad | mensual |
| Municipios con registros | 177 |
| Desagregación | forma clínica, sexo, tratamiento iniciado o concluido |
| Filas | 18.750 |

Valores de `forma_clinica` (forma clínica):

- cutanea (2010-2025)
- mucosa (2010-2025)
- mucosa y cutanea (2010-2025)
- visceral (2010-2025)

Valores de `tratamiento` (tratamiento iniciado o concluido):

- concluido (2010-2013, 2015-2025)
- iniciado (2010-2013, 2015-2025)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2010 | 2.073 |
| 2011 | 2.346 |
| 2012 | 2.982 |
| 2013 | 3.482 |
| 2014 | 3.558 |
| 2015 | 2.955 |
| 2016 | 2.846 |
| 2017 | 4.004 |
| 2018 | 4.425 |
| 2019 | 4.054 |
| 2020 | 3.520 |
| 2021 | 3.866 |
| 2022 | 3.760 |
| 2023 | 6.188 |
| 2024 | 2.580 |
| 2025 | 2.417 |

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
| `forma_clinica` | string | Forma clínica. |
| `sexo` | string | mujer u hombre. |
| `tratamiento` | string | Estado del tratamiento: iniciado o concluido. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tratamiento_leishmaniasis/datos.parquet'
group by gestion order by gestion;

-- Por gestión y forma_clinica
select gestion, forma_clinica, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tratamiento_leishmaniasis/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tratamiento_leishmaniasis/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2010-2011 | 301 | Tratamientos de Leishmania cutánea; Tratamientos de Leishmania mucosa; Tratamientos de Leishmania mucosa y cutánea; Tratamientos de Leishmania visceral | 1.0.4 (2013) |
| 2012 | 301 | l 23.1 Tratamientos de Leishmania cutánea; l 23.2 Tratamientos de Leishmania mucosa; l 23.3 Tratamientos de Leishmania mucosa y cutánea; l 23.4 Tratamientos de Leishmania visceral | 1.0.4 (2013) |
| 2013 | 301 | Tratamientos de Leishmania cutánea; Tratamientos de Leishmania mucosa; Tratamientos de Leishmania mucosa y cutánea; Tratamientos de Leishmania visceral | 1.0.4 (2013) |
| 2014 | 301 | 23.1 Tratamientos de Leishmania cutánea; 23.2 Tratamientos de Leishmania mucosa; 23.3 Tratamientos de Leishmania mucosa y cutánea; 23.4 Tratamientos de Leishmania visceral | 2.0.0 (2014) |
| 2015 | 301a | Total Tratamientos de Leishmania cutánea; Total Tratamientos de Leishmania mucosa; Total Tratamientos de Leishmania mucosa y cutánea; Total Tratamientos de Leishmania visceral | 3.0.1 (2016) |
| 2016 | 301a | Tratamientos de Leishmania cutánea; Tratamientos de Leishmania mucosa; Tratamientos de Leishmania mucosa y cutánea; Tratamientos de Leishmania visceral | 3.0.2 (2016) |
| 2017 | 301a | Tratamientos de Leishmania cutánea; Tratamientos de Leishmania mucosa; Tratamientos de Leishmania mucosa y cutánea; Tratamientos de Leishmania visceral | 4.0.0 (2018) |
| 2018 | 301a | Tratamientos de Leishmania cutánea; Tratamientos de Leishmania mucosa; Tratamientos de Leishmania mucosa y cutánea; Tratamientos de Leishmania visceral | 4.0.1 (2018) |
| 2019-2020 | 301a | Tratamientos de Leishmania cutánea; Tratamientos de Leishmania mucosa; Tratamientos de Leishmania mucosa y cutánea; Tratamientos de Leishmania visceral | 5.0.1 (2020) |
| 2021 | 301a | Tratamientos de Leishmania cutánea; Tratamientos de Leishmania mucosa; Tratamientos de Leishmania mucosa y cutánea; Tratamientos de Leishmania visceral | 6.0.0 (2021) |
| 2022-2023 | 301a | Tratamientos de Leishmania cutánea; Tratamientos de Leishmania mucosa; Tratamientos de Leishmania mucosa y cutánea; Tratamientos de Leishmania visceral | 6.0.1 (2022) |
| 2024-2025 | 301a | Tratamientos de Leishmania cutánea; Tratamientos de Leishmania mucosa; Tratamientos de Leishmania mucosa y cutánea (mucosa); Tratamientos de Leishmania visceral | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 301 y 301a, tratamientos de chagas, leishmaniasis y en mujeres posparto: el tablero repite las columnas de sexo ("FEMENINO" y "FEMENINO.1"). En 2020 los totales dicen "TOTAL Iniciado" y "TOTAL Concluido", y coinciden con la primera y la segunda columna: la primera es tratamiento iniciado y la repetida, concluido.
- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
