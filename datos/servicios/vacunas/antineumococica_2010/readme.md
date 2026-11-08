# Vacuna Antineumocócica (2010)

Dosis aplicadas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2010. Fuente: SNIS, formularios 301.

## Qué es

| | |
| --- | --- |
| Gestiones | 2010 |
| Periodicidad | mensual |
| Municipios con registros | 16 |
| Desagregación | dosis, edad, lugar |
| Filas | 23 |

Valores de `dosis` (dosis):

- 1 (2010)
- 2 (2010)

Valores de `lugar` (lugar):

- dentro (2010)
- fuera (2010)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2010 | <1 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2010 | 98 |

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
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/antineumococica_2010/datos.parquet'
group by gestion order by gestion;

-- Por gestión y dosis
select gestion, dosis, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/antineumococica_2010/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/antineumococica_2010/datos.parquet'
where gestion = 2010 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Vacuna Antineumocócica (2010) (este dataset): 2010, formulario 301.
- [Vacuna Antineumocócica (2011-2025)](../../../servicios/vacunas/antineumococica_2011_2025/readme.md): 2011-2025, formulario 301, 301a.

Las categorías de `dosis` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/vacunas/antineumococica_2010/datos.parquet',
    'datos/servicios/vacunas/antineumococica_2011_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2010 | 301 | Neumocócica 1ra. Dosis; Neumocócica 2da. Dosis | 1.0.4 (2013) |
