# Muerte por malaria (P. falciparum)

Muertes por esta causa en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2004. Fuente: SNIS, formularios 302.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2004 |
| Periodicidad | semanal |
| Municipios con registros | 10 |
| Desagregación | lugar |
| Filas | 11 |

Total por gestión:

| Gestión | Defunciones |
| ---: | ---: |
| 2001 | 3 |
| 2002 | 1 |
| 2003 | 3 |
| 2004 | 6 |

## Cómo utilizar

Cada fila da el número de defunciones de un periodo, un municipio y una población. Para obtener un total, sume las filas: el dataset no tiene filas de total. Una combinación sin fila significa que no hubo registros. Las convenciones de tiempo, territorio y población están en el [catálogo](../../../README.md#cómo-leer-los-datos).

| Columna | Tipo | Descripción |
| --- | --- | --- |
| `gestion` | integer | Año calendario (gestión) del registro. |
| `semana` | integer | Semana epidemiológica, de 1 a 53. Va de domingo a sábado. |
| `fecha_inicio` | date | Primer día de la semana o del mes. |
| `departamento` | string | Nombre del departamento. |
| `municipio` | string | Nombre del municipio. |
| `municipio_codigo` | string | Código del municipio, 6 dígitos: departamento (2), provincia (2) y municipio (2). |
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `defunciones` | integer | Número de defunciones en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_malaria/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(defunciones) as defunciones
from 'datos/vigilancia/defunciones/muerte_malaria/datos.parquet'
where gestion = 2004 group by all order by defunciones desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2003 | 302 | 75.- Muerte por malaria (P. Falciparum) |  |
| 2004 | 302 | 43 Muerte por Malaria (P. Falciparum) |  |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302, 2001-2007: en las variables cuyas columnas "-M" siempre valen 0, "TOTAL-H" es igual a "TOTAL": "-H" contiene a ambos sexos. Esas variables no tienen sexo. En 2004 el grupo 09 (mortalidad) tampoco tiene sexo: hay 79 muertes maternas en "-H" y 94 en "-M".
- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
