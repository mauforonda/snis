# Inyectables

Estudios y procedimientos realizados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | mensual |
| Municipios con registros | 344 |
| Desagregación |  |
| Filas | 99.213 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 3.925.932 |
| 2002 | 4.951.288 |
| 2003 | 5.425.215 |
| 2004 | 6.586.156 |
| 2005 | 7.161.720 |
| 2006 | 8.018.866 |
| 2007 | 8.448.055 |
| 2008 | 8.937.467 |
| 2009 | 9.801.783 |
| 2010 | 10.462.563 |
| 2011 | 11.977.121 |
| 2012 | 12.235.850 |
| 2013 | 13.225.633 |
| 2014 | 14.362.642 |
| 2015 | 15.086.273 |
| 2016 | 16.349.798 |
| 2017 | 17.576.819 |
| 2018 | 19.531.178 |
| 2019 | 19.291.420 |
| 2020 | 14.745.985 |
| 2021 | 21.811.706 |
| 2022 | 24.499.433 |
| 2023 | 27.099.879 |
| 2024 | 27.435.459 |
| 2025 | 27.383.865 |

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
from 'datos/servicios/diagnostico_tratamiento/inyectables/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/diagnostico_tratamiento/inyectables/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Inyectables (este dataset): 2001-2025, formulario 301, 301a.
- [Inyectable (formulario 301b)](../../../servicios/diagnostico_tratamiento/inyectables_301b/readme.md): 2024-2025, formulario 301b.

El formulario 301a registra los servicios de primer nivel y el 301b, los de segundo y tercer nivel: son registros complementarios, no partes de un total. Sumarlos supone que ninguna atención se registra en los dos.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/diagnostico_tratamiento/inyectables/datos.parquet',
    'datos/servicios/diagnostico_tratamiento/inyectables_301b/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2007 | 301 | Inyectables |  |
| 2008-2013 | 301 | Inyectables | 1.0.4 (2013) |
| 2014 | 301 | 7.2 Inyectables | 2.0.0 (2014) |
| 2015 | 301a | Inyectables | 3.0.1 (2016) |
| 2016 | 301a | Inyectables | 3.0.2 (2016) |
| 2017 | 301a | Inyectables | 4.0.0 (2018) |
| 2018 | 301a | Inyectables | 4.0.1 (2018) |
| 2019-2020 | 301a | Inyectables | 5.0.1 (2020) |
| 2021 | 301a | Inyectables | 6.0.0 (2021) |
| 2022-2023 | 301a | Inyectables | 6.0.1 (2022) |
| 2024-2025 | 301a | Inyectables | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
