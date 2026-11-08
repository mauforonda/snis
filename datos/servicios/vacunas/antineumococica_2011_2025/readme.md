# Vacuna Antineumocócica (2011-2025)

Dosis aplicadas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2011-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2011-2025 |
| Periodicidad | mensual |
| Municipios con registros | 343 |
| Desagregación | dosis, sexo, edad, lugar |
| Filas | 414.987 |

Valores de `dosis` (dosis):

- 1 (2011-2025)
- 2 (2011-2025)
- 3 (2011-2025)

Valores de `lugar` (lugar):

- dentro (2011-2013, 2015-2025)
- fuera (2011-2013, 2015-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2011-2025 | <1 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2011 | 168 |
| 2012 | 73 |
| 2013 | 15.890 |
| 2014 | 630.131 |
| 2015 | 663.180 |
| 2016 | 658.016 |
| 2017 | 633.314 |
| 2018 | 632.674 |
| 2019 | 592.357 |
| 2020 | 538.591 |
| 2021 | 514.208 |
| 2022 | 518.176 |
| 2023 | 502.702 |
| 2024 | 443.612 |
| 2025 | 424.681 |

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
from 'datos/servicios/vacunas/antineumococica_2011_2025/datos.parquet'
group by gestion order by gestion;

-- Por gestión y dosis
select gestion, dosis, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/antineumococica_2011_2025/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/antineumococica_2011_2025/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Vacuna Antineumocócica (2010)](../../../servicios/vacunas/antineumococica_2010/readme.md): 2010, formulario 301.
- Vacuna Antineumocócica (2011-2025) (este dataset): 2011-2025, formulario 301, 301a.

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
| 2011 | 301 | Neumocócica 1ra. Dosis; Neumocócica 2da. Dosis; Neumocócica 3ra. Dosis | 1.0.4 (2013) |
| 2012 | 301 | l 1710 Neumocócica 1ra. Dosis; l 1711 Neumocócica 2da. Dosis; l 1712 Neumocócica 3ra. Dosis | 1.0.4 (2013) |
| 2013 | 301 | Neumocócica 1ra. Dosis; Neumocócica 2da. Dosis; Neumocócica 3ra. Dosis | 1.0.4 (2013) |
| 2014 | 301 | 1710 Neumocócica 1ra. Dosis; 1711 Neumocócica 2da. Dosis; 1712 Neumocócica 3ra. Dosis | 2.0.0 (2014) |
| 2015 | 301a | Total Antineumocócica 1ra dosis; Total Antineumocócica 2da dosis; Total Antineumocócica 3ra dosis | 3.0.1 (2016) |
| 2016 | 301a | Antineumocócica 1ra dosis; Antineumocócica 2da dosis; Antineumocócica 3ra dosis | 3.0.2 (2016) |
| 2017 | 301a | Antineumocócica 1ra dosis; Antineumocócica 2da dosis; Antineumocócica 3ra dosis | 4.0.0 (2018) |
| 2018 | 301a | Antineumocócica 1ra dosis; Antineumocócica 2da dosis; Antineumocócica 3ra dosis | 4.0.1 (2018) |
| 2019-2020 | 301a | Antineumocócica 1ra dosis; Antineumocócica 2da dosis; Antineumocócica 3ra dosis | 5.0.1 (2020) |
| 2021 | 301a | Antineumocócica 1ra dosis; Antineumocócica 2da dosis; Antineumocócica 3ra dosis | 6.0.0 (2021) |
| 2022-2023 | 301a | Antineumocócica 1ra dosis; Antineumocócica 2da dosis; Antineumocócica 3ra dosis | 6.0.1 (2022) |
| 2024-2025 | 301a | Antineumococica 1ra Dosis; Antineumococica 2da Dosis; Antineumococica 3ra Dosis | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
