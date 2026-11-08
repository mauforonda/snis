# Egresos

Registros de internación en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | mensual |
| Municipios con registros | 343 |
| Desagregación | sexo |
| Filas | 108.141 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 336.496 |
| 2002 | 424.118 |
| 2003 | 445.281 |
| 2004 | 498.040 |
| 2005 | 517.927 |
| 2006 | 558.335 |
| 2007 | 570.937 |
| 2008 | 604.960 |
| 2009 | 635.212 |
| 2010 | 629.369 |
| 2011 | 697.909 |
| 2012 | 690.889 |
| 2013 | 702.181 |
| 2014 | 727.742 |
| 2015 | 740.783 |
| 2016 | 733.127 |
| 2017 | 717.534 |
| 2018 | 729.138 |
| 2019 | 738.529 |
| 2020 | 540.258 |
| 2021 | 604.530 |
| 2022 | 668.841 |
| 2023 | 763.866 |
| 2024 | 774.788 |
| 2025 | 787.876 |

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
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/internacion/egresos/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/internacion/egresos/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/internacion/egresos/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2007 | 301 | Egresos |  |
| 2008-2013 | 301 | Egresos | 1.0.4 (2013) |
| 2014 | 301 | 13. 3 Egresos | 2.0.0 (2014) |
| 2015 | 301a | Egresos | 3.0.1 (2016) |
| 2016 | 301a | Egresos | 3.0.2 (2016) |
| 2017 | 301a | Egresos | 4.0.0 (2018) |
| 2018 | 301a | Egresos | 4.0.1 (2018) |
| 2019-2020 | 301a | Egresos | 5.0.1 (2020) |
| 2021 | 301a | Egresos | 6.0.0 (2021) |
| 2022-2023 | 301a | Egresos | 6.0.1 (2022) |
| 2024-2025 | 301a | Egresos | 7.0.1 (2026) |
