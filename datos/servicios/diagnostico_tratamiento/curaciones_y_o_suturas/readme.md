# Curaciones y/o suturas

Estudios y procedimientos realizados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | mensual |
| Municipios con registros | 344 |
| Desagregación |  |
| Filas | 98.364 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 909.415 |
| 2002 | 1.205.518 |
| 2003 | 1.339.583 |
| 2004 | 1.469.902 |
| 2005 | 1.569.444 |
| 2006 | 1.601.824 |
| 2007 | 1.753.612 |
| 2008 | 1.929.439 |
| 2009 | 1.914.578 |
| 2010 | 2.138.385 |
| 2011 | 2.061.614 |
| 2012 | 3.615.621 |
| 2013 | 5.328.676 |
| 2014 | 3.483.676 |
| 2015 | 2.634.823 |
| 2016 | 2.899.896 |
| 2017 | 2.664.214 |
| 2018 | 3.030.443 |
| 2019 | 2.998.425 |
| 2020 | 2.441.113 |
| 2021 | 5.161.178 |
| 2022 | 6.736.442 |
| 2023 | 9.854.841 |
| 2024 | 12.209.577 |
| 2025 | 4.880.533 |

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
from 'datos/servicios/diagnostico_tratamiento/curaciones_y_o_suturas/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/diagnostico_tratamiento/curaciones_y_o_suturas/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Curaciones y/o suturas (este dataset): 2001-2025, formulario 301, 301a.
- [Curaciones y/o suturas (formulario 301b)](../../../servicios/diagnostico_tratamiento/curaciones_y_o_suturas_301b/readme.md): 2024-2025, formulario 301b.

El formulario 301a registra los servicios de primer nivel y el 301b, los de segundo y tercer nivel: son registros complementarios, no partes de un total. Sumarlos supone que ninguna atención se registra en los dos.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/diagnostico_tratamiento/curaciones_y_o_suturas/datos.parquet',
    'datos/servicios/diagnostico_tratamiento/curaciones_y_o_suturas_301b/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2007 | 301 | Curaciones y/o suturas |  |
| 2008-2013 | 301 | Curaciones y/o suturas | 1.0.4 (2013) |
| 2014 | 301 | 7.3 Curaciones y/o suturas | 2.0.0 (2014) |
| 2015 | 301a | Curaciones y/o suturas | 3.0.1 (2016) |
| 2016 | 301a | Curaciones y/o suturas | 3.0.2 (2016) |
| 2017 | 301a | Curaciones y/o suturas | 4.0.0 (2018) |
| 2018 | 301a | Curaciones y/o suturas | 4.0.1 (2018) |
| 2019-2020 | 301a | Curaciones y/o suturas | 5.0.1 (2020) |
| 2021 | 301a | Curaciones y/o suturas | 6.0.0 (2021) |
| 2022-2023 | 301a | Curaciones y/o suturas | 6.0.1 (2022) |
| 2024-2025 | 301a | Curaciones y/o suturas | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
