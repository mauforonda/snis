# Vacuna Antirrotavírica (2010-2025)

Dosis aplicadas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2010-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2010-2025 |
| Periodicidad | mensual |
| Municipios con registros | 344 |
| Desagregación | dosis, sexo, edad, lugar |
| Filas | 333.382 |

Valores de `dosis` (dosis):

- 1 (2010-2025)
- 2 (2010-2025)

Valores de `lugar` (lugar):

- dentro (2010-2013, 2015-2025)
- fuera (2010-2013, 2015-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2010-2025 | <1 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2010 | 417.554 |
| 2011 | 440.933 |
| 2012 | 419.339 |
| 2013 | 430.248 |
| 2014 | 431.730 |
| 2015 | 443.412 |
| 2016 | 433.006 |
| 2017 | 416.736 |
| 2018 | 427.013 |
| 2019 | 400.116 |
| 2020 | 370.938 |
| 2021 | 348.305 |
| 2022 | 348.800 |
| 2023 | 341.060 |
| 2024 | 303.267 |
| 2025 | 291.681 |

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
from 'datos/servicios/vacunas/antirrotavirica_2010_2025/datos.parquet'
group by gestion order by gestion;

-- Por gestión y dosis
select gestion, dosis, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/antirrotavirica_2010_2025/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/antirrotavirica_2010_2025/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Vacuna Antirrotavírica (2008-2009)](../../../servicios/vacunas/antirrotavirica_2008_2009/readme.md): 2008-2009, formulario 301.
- Vacuna Antirrotavírica (2010-2025) (este dataset): 2010-2025, formulario 301, 301a.

Las categorías de `dosis` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/vacunas/antirrotavirica_2008_2009/datos.parquet',
    'datos/servicios/vacunas/antirrotavirica_2010_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2010-2011 | 301 | Antirotavirica 1ra. Dosis; Antirotavirica 2ra. Dosis | 1.0.4 (2013) |
| 2012 | 301 | l 17.8 Antirotavirica 1ra. Dosis; l 17.9 Antirotavirica 2ra. Dosis | 1.0.4 (2013) |
| 2013 | 301 | Antirotavirica 1ra. Dosis; Antirotavirica 2ra. Dosis | 1.0.4 (2013) |
| 2014 | 301 | 17.8 Antirotavirica 1ra. Dosis; 17.9 Antirotavirica 2ra. Dosis | 2.0.0 (2014) |
| 2015 | 301a | Total Antirotaviríca 1ra dosis; Total Antirotaviríca 2da dosis | 3.0.1 (2016) |
| 2016 | 301a | Antirotaviríca 1ra dosis; Antirotaviríca 2da dosis | 3.0.2 (2016) |
| 2017 | 301a | Antirotaviríca 1ra dosis; Antirotaviríca 2da dosis | 4.0.0 (2018) |
| 2018 | 301a | Antirotaviríca 1ra dosis; Antirotaviríca 2da dosis | 4.0.1 (2018) |
| 2019-2020 | 301a | Antirotaviríca 1ra dosis; Antirotaviríca 2da dosis | 5.0.1 (2020) |
| 2021 | 301a | Antirotaviríca 1ra dosis; Antirotaviríca 2da dosis | 6.0.0 (2021) |
| 2022-2023 | 301a | Antirotaviríca 1ra dosis; Antirotaviríca 2da dosis | 6.0.1 (2022) |
| 2024-2025 | 301a | Antirotavirica 1ra Dosis; Antirotavirica 2da Dosis | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
