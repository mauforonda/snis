# Partos atendidos por partera capacitada

Atenciones y nacimientos registrados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2008-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2008-2025 |
| Periodicidad | mensual |
| Municipios con registros | 320 |
| Desagregación | edad, lugar |
| Filas | 8.922 |

Valores de `lugar` (lugar):

- domicilio (2008-2025)
- servicio (2024-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2024 | 10-14, 15-19, 20-34, 35-49, 50+ |
| 2025 | 10-14, 15-19, 20-34, 35-49 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2008 | 3.790 |
| 2009 | 3.131 |
| 2010 | 3.033 |
| 2011 | 2.935 |
| 2012 | 2.366 |
| 2013 | 2.290 |
| 2014 | 1.798 |
| 2015 | 694 |
| 2016 | 411 |
| 2017 | 261 |
| 2018 | 189 |
| 2019 | 245 |
| 2020 | 229 |
| 2021 | 209 |
| 2022 | 137 |
| 2023 | 164 |
| 2024 | 239 |
| 2025 | 202 |

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
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/partos_atendidos_por_partera_capacitada/datos.parquet'
group by gestion order by gestion;

-- Por gestión y edad_grupo
select gestion, edad_grupo, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/partos_atendidos_por_partera_capacitada/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/partos_atendidos_por_partera_capacitada/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Partos atendidos por partera capacitada u otra pe](../../../servicios/salud_materna_neonatal/partos_atendidos_por_partera_capacitada_u_otra_pe/readme.md): 2001-2007, formulario 301.
- Partos atendidos por partera capacitada (este dataset): 2008-2025, formulario 301, 301a.

Hasta 2007 la variable es "partos atendidos por partera capacitada u otra pe…" (el tablero corta el nombre); desde 2008, "por partera capacitada". Consultarlos juntos como una serie supone que la variable no cambió de contenido.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/salud_materna_neonatal/partos_atendidos_por_partera_capacitada_u_otra_pe/datos.parquet',
    'datos/servicios/salud_materna_neonatal/partos_atendidos_por_partera_capacitada/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2008 | 301 | Partos atendidos por partera capacitada |  |
| 2009-2013 | 301 | Partos atendidos por partera capacitada | 1.0.4 (2013) |
| 2014 | 301 | 12.6 Partos atendidos por partera capacitada | 2.0.0 (2014) |
| 2015 | 301a | Partos atendidos por partera capacitada | 3.0.1 (2016) |
| 2016 | 301a | Partos atendidos por partera capacitada | 3.0.2 (2016) |
| 2017 | 301a | Partos atendidos por partera capacitada | 4.0.0 (2018) |
| 2018 | 301a | Partos atendidos por partera capacitada | 4.0.1 (2018) |
| 2019-2020 | 301a | Partos atendidos por partera capacitada | 5.0.1 (2020) |
| 2021 | 301a | Partos atendidos por partera capacitada | 6.0.0 (2021) |
| 2022-2023 | 301a | Partos atendidos por partera capacitada | 6.0.1 (2022) |
| 2024-2025 | 301a | Partos atendidos por partera capacitada | 7.0.1 (2026) |
