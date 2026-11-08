# Vacuna dT (difteria y tétanos) (2008-2025)

Dosis aplicadas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2008-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2008-2025 |
| Periodicidad | mensual |
| Municipios con registros | 344 |
| Desagregación | dosis, sexo, edad, lugar |
| Filas | 696.979 |

Valores de `dosis` (dosis):

- 1 (2008-2025)
- 2 (2008-2025)
- 3 (2008-2025)
- 4 (2008-2025)
- 5 (2008-2025)

Valores de `lugar` (lugar):

- dentro (2010-2013, 2015-2025)
- fuera (2010-2013, 2015-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2008-2009 | 15-49 |
| 2010-2017 | 10-49 |
| 2018-2023 | 7-49 |
| 2024 | 5-9, 10, 11, 12-20, 21-59, 60+ |
| 2025 | 5-9, 10, 11, 12-20, 21-59 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2008 | 935.974 |
| 2009 | 847.044 |
| 2010 | 1.401.406 |
| 2011 | 1.061.548 |
| 2012 | 1.052.415 |
| 2013 | 1.121.307 |
| 2014 | 1.336.409 |
| 2015 | 2.911.801 |
| 2016 | 1.350.723 |
| 2017 | 1.013.297 |
| 2018 | 1.079.137 |
| 2019 | 1.157.844 |
| 2020 | 744.665 |
| 2021 | 913.563 |
| 2022 | 741.991 |
| 2023 | 730.469 |
| 2024 | 858.290 |
| 2025 | 877.955 |

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
| `dosis` | string | Dosis: número (1 a 5), inicial, única, anual o refuerzo. |
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/dt_2008_2025/datos.parquet'
group by gestion order by gestion;

-- Por gestión y dosis
select gestion, dosis, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/dt_2008_2025/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/dt_2008_2025/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Vacuna dT (difteria y tétanos) (2001-2003)](../../../servicios/vacunas/dt_2001_2003/readme.md): 2001-2003, formulario 301.
- [Vacuna dT (difteria y tétanos) (2004-2007)](../../../servicios/vacunas/dt_2004_2007/readme.md): 2004-2007, formulario 301.
- Vacuna dT (difteria y tétanos) (2008-2025) (este dataset): 2008-2025, formulario 301, 301a.

Las categorías de `dosis` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/vacunas/dt_2001_2003/datos.parquet',
    'datos/servicios/vacunas/dt_2004_2007/datos.parquet',
    'datos/servicios/vacunas/dt_2008_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2008 | 301 | Mujeres de 15 a 49 años 1ra dosis de dt; Mujeres de 15 a 49 años 2da dosis de dt; Mujeres de 15 a 49 años 3da dosis de dt; Mujeres de 15 a 49 años 4da dosis de dt; Mujeres de 15 a 49 años 5ta dosis de dt |  |
| 2009 | 301 | Mujeres de 15 a 49 años 1ra dosis de dT; Mujeres de 15 a 49 años 2da dosis de dT; Mujeres de 15 a 49 años 3da dosis de dT; Mujeres de 15 a 49 años 4da dosis de dT; Mujeres de 15 a 49 años 5ta dosis de dT |  |
| 2010-2011 | 301 | Mujeres de 10 a 49 años 1ra dosis de dT; Mujeres de 10 a 49 años 2da dosis de dT; Mujeres de 10 a 49 años 3ra dosis de dT; Mujeres de 10 a 49 años 4ta dosis de dT; Mujeres de 10 a 49 años 5ta dosis de dT | 1.0.4 (2013) |
| 2012 | 301 | l 21.1 Mujeres de 10 a 49 años 1ra dosis de dT; l 21.2 Mujeres de 10 a 49 años 2da dosis de dT; l 21.3 Mujeres de 10 a 49 años 3ra dosis de dT; l 21.4 Mujeres de 10 a 49 años 4ta dosis de dT; l 21.5 Mujeres de 10 a 49 años 5ta dosis de dT | 1.0.4 (2013) |
| 2013 | 301 | Mujeres de 10 a 49 años 1ra dosis de dT; Mujeres de 10 a 49 años 2da dosis de dT; Mujeres de 10 a 49 años 3ra dosis de dT; Mujeres de 10 a 49 años 4ta dosis de dT; Mujeres de 10 a 49 años 5ta dosis de dT | 1.0.4 (2013) |
| 2014 | 301 | 21.1 Mujeres de 10 a 49 años 1ra dosis de dT; 21.2 Mujeres de 10 a 49 años 2da dosis de dT; 21.3 Mujeres de 10 a 49 años 3ra dosis de dT; 21.4 Mujeres de 10 a 49 años 4ta dosis de dT; 21.5 Mujeres de 10 a 49 años 5ta dosis de dT | 2.0.0 (2014) |
| 2015 | 301a | Total dT 1ra. dosis de 10 a 49 años; Total dT 2da. dosis de 10 a 49 años; Total dT 3ra. dosis de 10 a 49 años; Total dT 4ta. dosis de 10 a 49 años; Total dT 5ta. dosis de 10 a 49 años | 3.0.1 (2016) |
| 2016 | 301a | dT 1ra. dosis de 10 a 49 años; dT 2da. dosis de 10 a 49 años; dT 3ra. dosis de 10 a 49 años; dT 4ta. dosis de 10 a 49 años; dT 5ta. dosis de 10 a 49 años | 3.0.2 (2016) |
| 2017 | 301a | dT 1ra. dosis de 10 a 49 años; dT 2da. dosis de 10 a 49 años; dT 3ra. dosis de 10 a 49 años; dT 4ta. dosis de 10 a 49 años; dT 5ta. dosis de 10 a 49 años | 4.0.0 (2018) |
| 2018 | 301a | dT 1ra. dosis de 7 a 49 años; dT 2da. dosis de 7 a 49 años; dT 3ra. dosis de 7 a 49 años; dT 4ta. dosis de 7 a 49 años; dT 5ta. dosis de 7 a 49 años | 4.0.1 (2018) |
| 2019-2020 | 301a | dT 1ra. dosis de 7 a 49 años; dT 2da. dosis de 7 a 49 años; dT 3ra. dosis de 7 a 49 años; dT 4ta. dosis de 7 a 49 años; dT 5ta. dosis de 7 a 49 años | 5.0.1 (2020) |
| 2021 | 301a | dT 1ra. dosis de 7 a 49 años; dT 2da. dosis de 7 a 49 años; dT 3ra. dosis de 7 a 49 años; dT 4ta. dosis de 7 a 49 años; dT 5ta. dosis de 7 a 49 años | 6.0.0 (2021) |
| 2022-2023 | 301a | dT 1ra. dosis de 7 a 49 años; dT 2da. dosis de 7 a 49 años; dT 3ra. dosis de 7 a 49 años; dT 4ta. dosis de 7 a 49 años; dT 5ta. dosis de 7 a 49 años | 6.0.1 (2022) |
| 2024-2025 | 301a | dT 1ra Dosis; dT 2da Dosis; dT 3ra Dosis; dT 4ta Dosis; dT 5ta Dosis | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
