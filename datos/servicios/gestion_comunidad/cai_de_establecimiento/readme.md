# CAI de establecimiento

Actividades registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2010-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2010-2025 |
| Periodicidad | mensual |
| Municipios con registros | 343 |
| Desagregación |  |
| Filas | 31.677 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2010 | 5.858 |
| 2011 | 5.645 |
| 2012 | 5.189 |
| 2013 | 6.044 |
| 2014 | 6.434 |
| 2015 | 6.070 |
| 2016 | 7.107 |
| 2017 | 7.687 |
| 2018 | 8.625 |
| 2019 | 9.137 |
| 2020 | 5.720 |
| 2021 | 7.139 |
| 2022 | 9.195 |
| 2023 | 9.769 |
| 2024 | 8.752 |
| 2025 | 7.925 |

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
from 'datos/servicios/gestion_comunidad/cai_de_establecimiento/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/gestion_comunidad/cai_de_establecimiento/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [CAI de sector realizados](../../../servicios/gestion_comunidad/cai_de_sector_realizados/readme.md): 2004-2009, formulario 301.
- CAI de establecimiento (este dataset): 2010-2025, formulario 301, 301a.

Hasta 2009 la variable es "CAI de sector realizados"; desde 2010, "CAI de establecimiento". Consultarlos juntos como una serie supone que las dos cuentan lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/gestion_comunidad/cai_de_sector_realizados/datos.parquet',
    'datos/servicios/gestion_comunidad/cai_de_establecimiento/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2010-2013 | 301 | Nº de CAI de establecimiento | 1.0.4 (2013) |
| 2014 | 301 | 10.2. Nº de CAI de establecimiento | 2.0.0 (2014) |
| 2015 | 301a | N° de CAI de establecimiento | 3.0.1 (2016) |
| 2016 | 301a | N° de CAI de establecimiento | 3.0.2 (2016) |
| 2017 | 301a | N° de CAI de establecimiento | 4.0.0 (2018) |
| 2018 | 301a | N° de CAI de establecimiento | 4.0.1 (2018) |
| 2019-2020 | 301a | N° de CAI de establecimiento | 5.0.1 (2020) |
| 2021 | 301a | N° de CAI de establecimiento | 6.0.0 (2021) |
| 2022-2023 | 301a | N° de CAI de establecimiento | 6.0.1 (2022) |
| 2024-2025 | 301a | N° de CAI de establecimiento | 7.0.1 (2026) |
