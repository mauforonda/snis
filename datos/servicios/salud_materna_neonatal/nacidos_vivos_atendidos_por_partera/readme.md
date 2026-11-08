# Nacidos vivos atendidos por partera

Atenciones y nacimientos registrados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2025. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2025 |
| Periodicidad | mensual |
| Municipios con registros | 292 |
| Desagregación | lugar |
| Filas | 4.233 |

Valores de `lugar` (lugar):

- domicilio (2015-2025)
- servicio (2024-2025)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2015 | 1.334 |
| 2016 | 1.065 |
| 2017 | 1.096 |
| 2018 | 950 |
| 2019 | 898 |
| 2020 | 1.065 |
| 2021 | 865 |
| 2022 | 578 |
| 2023 | 333 |
| 2024 | 597 |
| 2025 | 522 |

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
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/nacidos_vivos_atendidos_por_partera/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/nacidos_vivos_atendidos_por_partera/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Nacidos vivos atendidos por partera capacitada u](../../../servicios/salud_materna_neonatal/nacidos_vivos_atendidos_por_partera_capacitada_u/readme.md): 2001-2007, formulario 301.
- [Nacidos vivos atendidos por partera capacitada](../../../servicios/salud_materna_neonatal/nacidos_vivos_atendidos_por_partera_capacitada/readme.md): 2008-2014, formulario 301.
- Nacidos vivos atendidos por partera (este dataset): 2015-2025, formulario 301a.

La variable cambia de nombre: "por partera capacitada u…" (2001-2007, el tablero corta el nombre), "por partera capacitada" (2008-2014) y "por partera" (desde 2015). Consultarlos juntos como una serie supone que las tres cuentan lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/salud_materna_neonatal/nacidos_vivos_atendidos_por_partera_capacitada_u/datos.parquet',
    'datos/servicios/salud_materna_neonatal/nacidos_vivos_atendidos_por_partera_capacitada/datos.parquet',
    'datos/servicios/salud_materna_neonatal/nacidos_vivos_atendidos_por_partera/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015 | 301a | Nacidos vivos atendidos por partera | 3.0.1 (2016) |
| 2016 | 301a | Nacidos vivos atendidos por partera | 3.0.2 (2016) |
| 2017 | 301a | Nacidos vivos atendidos por partera | 4.0.0 (2018) |
| 2018 | 301a | Nacidos vivos atendidos por partera | 4.0.1 (2018) |
| 2019-2020 | 301a | Nacidos vivos atendidos por partera | 5.0.1 (2020) |
| 2021 | 301a | Nacidos vivos atendidos por partera | 6.0.0 (2021) |
| 2022-2023 | 301a | Nacidos vivos atendidos por partera | 6.0.1 (2022) |
| 2024-2025 | 301a | 7. Nacidos vivos atendidos por partera | 7.0.1 (2026) |
