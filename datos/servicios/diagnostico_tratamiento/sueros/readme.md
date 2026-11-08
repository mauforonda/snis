# Sueros

Estudios y procedimientos realizados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | mensual |
| Municipios con registros | 344 |
| Desagregación |  |
| Filas | 94.834 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 690.188 |
| 2002 | 827.057 |
| 2003 | 1.126.924 |
| 2004 | 1.179.967 |
| 2005 | 1.226.801 |
| 2006 | 1.487.077 |
| 2007 | 1.708.072 |
| 2008 | 1.791.298 |
| 2009 | 1.919.171 |
| 2010 | 2.168.723 |
| 2011 | 2.494.023 |
| 2012 | 2.415.197 |
| 2013 | 2.507.345 |
| 2014 | 2.792.598 |
| 2015 | 3.011.348 |
| 2016 | 3.194.525 |
| 2017 | 3.701.501 |
| 2018 | 4.240.719 |
| 2019 | 4.244.116 |
| 2020 | 3.744.815 |
| 2021 | 4.907.403 |
| 2022 | 4.900.404 |
| 2023 | 6.245.344 |
| 2024 | 6.883.054 |
| 2025 | 6.469.374 |

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
from 'datos/servicios/diagnostico_tratamiento/sueros/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/diagnostico_tratamiento/sueros/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Sueros (este dataset): 2001-2025, formulario 301, 301a.
- [Sueros (formulario 301b)](../../../servicios/diagnostico_tratamiento/sueros_301b/readme.md): 2024-2025, formulario 301b.

El formulario 301a registra los servicios de primer nivel y el 301b, los de segundo y tercer nivel: son registros complementarios, no partes de un total. Sumarlos supone que ninguna atención se registra en los dos.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/diagnostico_tratamiento/sueros/datos.parquet',
    'datos/servicios/diagnostico_tratamiento/sueros_301b/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2007 | 301 | Sueros |  |
| 2008-2013 | 301 | Sueros | 1.0.4 (2013) |
| 2014 | 301 | 7.1 Sueros | 2.0.0 (2014) |
| 2015 | 301a | Sueros | 3.0.1 (2016) |
| 2016 | 301a | Sueros | 3.0.2 (2016) |
| 2017 | 301a | Sueros | 4.0.0 (2018) |
| 2018 | 301a | Sueros | 4.0.1 (2018) |
| 2019-2020 | 301a | Sueros | 5.0.1 (2020) |
| 2021 | 301a | Sueros | 6.0.0 (2021) |
| 2022-2023 | 301a | Sueros | 6.0.1 (2022) |
| 2024-2025 | 301a | Sueros | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
