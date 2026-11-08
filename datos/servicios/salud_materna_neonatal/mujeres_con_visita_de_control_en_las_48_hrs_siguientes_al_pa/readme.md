# Mujeres con visita de control en las 48 hrs siguientes al parto

Atenciones y nacimientos registrados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2025. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2025 |
| Periodicidad | mensual |
| Municipios con registros | 343 |
| Desagregación | edad, lugar |
| Filas | 74.309 |

Valores de `lugar` (lugar):

- domicilio (2015-2025)
- servicio (2015-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2024 | <10, 10-14, 15-19, 20-34, 35-49, 50+ |
| 2025 | 10-14, 15-19, 20-34, 35-49, 50+ |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2015 | 118.998 |
| 2016 | 147.177 |
| 2017 | 148.339 |
| 2018 | 145.950 |
| 2019 | 146.041 |
| 2020 | 140.147 |
| 2021 | 131.771 |
| 2022 | 133.161 |
| 2023 | 130.908 |
| 2024 | 116.371 |
| 2025 | 113.168 |

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
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/mujeres_con_visita_de_control_en_las_48_hrs_siguientes_al_pa/datos.parquet'
group by gestion order by gestion;

-- Por gestión y edad_grupo
select gestion, edad_grupo, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/mujeres_con_visita_de_control_en_las_48_hrs_siguientes_al_pa/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/mujeres_con_visita_de_control_en_las_48_hrs_siguientes_al_pa/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015 | 301a | Mujeres con visita de control en las 48 hrs siguientes al parto | 3.0.1 (2016) |
| 2016 | 301a | Mujeres con visita de control en las 48 hrs siguientes al parto | 3.0.2 (2016) |
| 2017 | 301a | Mujeres con visita de control en las 48 hrs siguientes al parto | 4.0.0 (2018) |
| 2018 | 301a | Mujeres con visita de control en las 48 hrs siguientes al parto | 4.0.1 (2018) |
| 2019-2020 | 301a | Mujeres con visita de control en las 48 hrs siguientes al parto | 5.0.1 (2020) |
| 2021 | 301a | Mujeres con visita de control en las 48 hrs siguientes al parto | 6.0.0 (2021) |
| 2022-2023 | 301a | Mujeres con visita de control en las 48 hrs siguientes al parto | 6.0.1 (2022) |
| 2024-2025 | 301a | Mujeres con visita de control en las 48 hrs siguientes al parto | 7.0.1 (2026) |
