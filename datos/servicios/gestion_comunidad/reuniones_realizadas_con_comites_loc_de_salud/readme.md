# Reuniones realizadas con comités loc. de salud

Actividades registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2025. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2025 |
| Periodicidad | mensual |
| Municipios con registros | 343 |
| Desagregación |  |
| Filas | 22.471 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2015 | 14.920 |
| 2016 | 13.662 |
| 2017 | 13.008 |
| 2018 | 9.686 |
| 2019 | 9.257 |
| 2020 | 8.325 |
| 2021 | 8.780 |
| 2022 | 9.594 |
| 2023 | 10.039 |
| 2024 | 9.820 |
| 2025 | 9.327 |

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
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/gestion_comunidad/reuniones_realizadas_con_comites_loc_de_salud/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/gestion_comunidad/reuniones_realizadas_con_comites_loc_de_salud/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Reuniones realizadas con comités loc. de salud/consejo mun. de salud](../../../servicios/gestion_comunidad/reuniones_realizadas_con_comites_loc_de_salud_consejo_mun_de/readme.md): 2010-2014, formulario 301.
- Reuniones realizadas con comités loc. de salud (este dataset): 2015-2025, formulario 301a.

Hasta 2014 la variable cuenta reuniones con comités locales de salud o con el consejo municipal de salud; desde 2015, sólo con comités locales de salud. Consultarlos juntos como una serie supone que las reuniones con el consejo municipal no cambian la serie.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/gestion_comunidad/reuniones_realizadas_con_comites_loc_de_salud_consejo_mun_de/datos.parquet',
    'datos/servicios/gestion_comunidad/reuniones_realizadas_con_comites_loc_de_salud/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015 | 301a | Nº de reuniones realizadas con Comités Loc. de Salud | 3.0.1 (2016) |
| 2016 | 301a | Nº de reuniones realizadas con Comités Loc. de Salud | 3.0.2 (2016) |
| 2017 | 301a | Nº de reuniones realizadas con Comités Loc. de Salud | 4.0.0 (2018) |
| 2018 | 301a | Nº de reuniones realizadas con Comités Loc. de Salud | 4.0.1 (2018) |
| 2019-2020 | 301a | Nº de reuniones realizadas con Comités Loc. de Salud | 5.0.1 (2020) |
| 2021 | 301a | Nº de reuniones realizadas con Comités Loc. de Salud | 6.0.0 (2021) |
| 2022-2023 | 301a | Nº de reuniones realizadas con Comités Loc. de Salud | 6.0.1 (2022) |
| 2024-2025 | 301a | Nº de reuniones realizadas con Comités Loc. de Salud | 7.0.1 (2026) |
