# Tratamientos iniciados de tuberculosis y lepra (2010-2023)

Registros en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2010-2023. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2010-2023 |
| Periodicidad | mensual |
| Municipios con registros | 327 |
| Desagregación | esquema, sexo |
| Filas | 30.042 |

Valores de `esquema` (esquema):

- I (2010-2023)
- II (2010-2023)
- III (2010-2023)
- multibacilar (2010-2023)
- paucibacilar (2010-2023)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2010 | 8.578 |
| 2011 | 8.823 |
| 2012 | 9.199 |
| 2013 | 9.102 |
| 2014 | 13.767 |
| 2015 | 8.452 |
| 2016 | 8.823 |
| 2017 | 8.564 |
| 2018 | 8.604 |
| 2019 | 7.975 |
| 2020 | 5.809 |
| 2021 | 7.186 |
| 2022 | 8.061 |
| 2023 | 9.530 |

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
| `esquema` | string | Esquema de tratamiento. |
| `sexo` | string | mujer u hombre. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2010_2023/datos.parquet'
group by gestion order by gestion;

-- Por gestión y esquema
select gestion, esquema, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2010_2023/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2010_2023/datos.parquet'
where gestion = 2023 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Tratamientos iniciados de tuberculosis y lepra (2001-2009)](../../../servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2001_2009/readme.md): 2001-2009, formulario 301.
- Tratamientos iniciados de tuberculosis y lepra (2010-2023) (este dataset): 2010-2023, formulario 301, 301a.
- [Tratamientos iniciados de tuberculosis y lepra (2024-2025)](../../../servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2024_2025/readme.md): 2024-2025, formulario 301a.

Las categorías de `esquema` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2001_2009/datos.parquet',
    'datos/servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2010_2023/datos.parquet',
    'datos/servicios/control_enfermedades/tratamiento_tuberculosis_lepra_2024_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2010-2011 | 301 | Tratamientos iniciados con esquema l; Tratamientos iniciados con esquema ll; Tratamientos iniciados con esquema lll; Tratamientos iniciados con esquema multibacilar (P.Q.T.); Tratamientos iniciados con esquema pausibacilar (P.Q.T.) | 1.0.4 (2013) |
| 2012 | 301 | l 23.5 Tratamientos iniciados con esquema l; l 23.6 Tratamientos iniciados con esquema ll; l 23.7 Tratamientos iniciados con esquema lll; l 2310 Tratamientos iniciados con esquema pausibacilar (P.Q.T.); l 2311 Tratamientos iniciados con esquema multibacilar (P.Q.T.) | 1.0.4 (2013) |
| 2013 | 301 | Tratamientos iniciados con esquema l; Tratamientos iniciados con esquema ll; Tratamientos iniciados con esquema lll; Tratamientos iniciados con esquema multibacilar (P.Q.T.); Tratamientos iniciados con esquema pausibacilar (P.Q.T.) | 1.0.4 (2013) |
| 2014 | 301 | 23.5 Tratamientos iniciados con esquema l; 23.6 Tratamientos iniciados con esquema ll; 23.7 Tratamientos iniciados con esquema lll; 2310 Tratamientos iniciados con esquema pausibacilar (P.Q.T.); 2311 Tratamientos iniciados con esquema multibacilar (P.Q.T.) | 2.0.0 (2014) |
| 2015 | 301a | Total Tratamientos iniciados con esquema I; Total Tratamientos iniciados con esquema II; Total Tratamientos iniciados con esquema III; Total Tratamientos iniciados con esquema multibacilar; Total Tratamientos iniciados con esquema pausibacilar | 3.0.1 (2016) |
| 2016 | 301a | Tratamientos iniciados con esquema I; Tratamientos iniciados con esquema II; Tratamientos iniciados con esquema III; Tratamientos iniciados con esquema multibacilar; Tratamientos iniciados con esquema pausibacilar | 3.0.2 (2016) |
| 2017 | 301a | Tratamientos iniciados con esquema I; Tratamientos iniciados con esquema II; Tratamientos iniciados con esquema III; Tratamientos iniciados con esquema multibacilar; Tratamientos iniciados con esquema pausibacilar | 4.0.0 (2018) |
| 2018 | 301a | Tratamientos iniciados con esquema I; Tratamientos iniciados con esquema II; Tratamientos iniciados con esquema III; Tratamientos iniciados con esquema multibacilar; Tratamientos iniciados con esquema pausibacilar | 4.0.1 (2018) |
| 2019-2020 | 301a | Tratamientos iniciados con esquema I; Tratamientos iniciados con esquema II; Tratamientos iniciados con esquema III; Tratamientos iniciados con esquema multibacilar; Tratamientos iniciados con esquema pausibacilar | 5.0.1 (2020) |
| 2021 | 301a | Tratamientos iniciados con esquema I; Tratamientos iniciados con esquema II; Tratamientos iniciados con esquema III; Tratamientos iniciados con esquema multibacilar; Tratamientos iniciados con esquema pausibacilar | 6.0.0 (2021) |
| 2022-2023 | 301a | Tratamientos iniciados con esquema I; Tratamientos iniciados con esquema II; Tratamientos iniciados con esquema III; Tratamientos iniciados con esquema multibacilar; Tratamientos iniciados con esquema pausibacilar | 6.0.1 (2022) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
