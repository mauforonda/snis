# Vacuna Hepatitis B (2010-2014)

Dosis aplicadas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2010-2014. Fuente: SNIS, formularios 301.

## Qué es

| | |
| --- | --- |
| Gestiones | 2010-2014 |
| Periodicidad | mensual |
| Municipios con registros | 315 |
| Desagregación | dosis, grupo de población, lugar |
| Filas | 8.059 |

Valores de `dosis` (dosis):

- 1 (2010-2014)
- 2 (2010-2014)
- 3 (2010-2014)

Valores de `grupo` (grupo de población):

- personal de salud (2010-2014)

Valores de `lugar` (lugar):

- dentro (2010-2013)
- fuera (2010-2013)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2010 | 26.553 |
| 2011 | 14.913 |
| 2012 | 15.613 |
| 2013 | 43.949 |
| 2014 | 60.255 |

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
| `grupo` | string | Grupo de población al que se dirige la vacuna. |
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/hepatitis_b_2010_2014/datos.parquet'
group by gestion order by gestion;

-- Por gestión y dosis
select gestion, dosis, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/hepatitis_b_2010_2014/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/hepatitis_b_2010_2014/datos.parquet'
where gestion = 2014 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Vacuna Hepatitis B (2010-2014) (este dataset): 2010-2014, formulario 301.
- [Vacuna Hepatitis B (2015-2020)](../../../servicios/vacunas/hepatitis_b_2015_2020/readme.md): 2015-2020, formulario 301a.
- [Vacuna Hepatitis B (2021-2025)](../../../servicios/vacunas/hepatitis_b_2021_2025/readme.md): 2021-2025, formulario 301a.

Las categorías de `dosis` y `grupo` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/vacunas/hepatitis_b_2010_2014/datos.parquet',
    'datos/servicios/vacunas/hepatitis_b_2015_2020/datos.parquet',
    'datos/servicios/vacunas/hepatitis_b_2021_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2010-2011 | 301 | Trabajador de Salud Hepatitis B 1ra dosis; Trabajador de Salud Hepatitis B 2da dosis; Trabajador de Salud Hepatitis B 3ra dosis | 1.0.4 (2013) |
| 2012 | 301 | l 21.6 Trabajador de Salud Hepatitis B 1ra dosis; l 21.7 Trabajador de Salud Hepatitis B 2da dosis; l 21.8 Trabajador de Salud Hepatitis B 3ra dosis | 1.0.4 (2013) |
| 2013 | 301 | Trabajador de Salud Hepatitis B 1ra dosis; Trabajador de Salud Hepatitis B 2da dosis; Trabajador de Salud Hepatitis B 3ra dosis | 1.0.4 (2013) |
| 2014 | 301 | 21.6 Trabajador de Salud Hepatitis B 1ra dosis; 21.7 Trabajador de Salud Hepatitis B 2da dosis; 21.8 Trabajador de Salud Hepatitis B 3ra dosis | 2.0.0 (2014) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
