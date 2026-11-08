# Nacidos vivos con peso menor a 2500 g

Atenciones y nacimientos registrados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | mensual |
| Municipios con registros | 342 |
| Desagregación | lugar |
| Filas | 27.268 |

Valores de `lugar` (lugar):

- servicio (2001-2025)
- domicilio (2008-2025)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 5.816 |
| 2002 | 6.232 |
| 2003 | 6.389 |
| 2004 | 7.017 |
| 2005 | 6.882 |
| 2006 | 6.926 |
| 2007 | 6.469 |
| 2008 | 7.384 |
| 2009 | 7.260 |
| 2010 | 9.687 |
| 2011 | 8.943 |
| 2012 | 8.288 |
| 2013 | 8.856 |
| 2014 | 8.890 |
| 2015 | 10.920 |
| 2016 | 10.274 |
| 2017 | 10.319 |
| 2018 | 10.312 |
| 2019 | 10.124 |
| 2020 | 9.394 |
| 2021 | 9.783 |
| 2022 | 9.325 |
| 2023 | 10.117 |
| 2024 | 8.365 |
| 2025 | 8.441 |

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
from 'datos/servicios/salud_materna_neonatal/nacidos_vivos_con_peso_menor_a_2500g/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/nacidos_vivos_con_peso_menor_a_2500g/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2007 | 301 | Nacidos vivos con peso menor a 2500g |  |
| 2008-2013 | 301 | Nacidos vivos con peso menor a 2500 g.; Nacidos vivos con peso menor a 2500g | 1.0.4 (2013) |
| 2014 | 301 | 11.5 Nacidos vivos con peso menor a 2500g; 12.4 Nacidos vivos con peso menor a 2500 g. | 2.0.0 (2014) |
| 2015 | 301a | Nacidos vivos con peso menor a 2500g | 3.0.1 (2016) |
| 2016 | 301a | Nacidos vivos con peso menor a 2500g | 3.0.2 (2016) |
| 2017 | 301a | Nacidos vivos con peso menor a 2500g | 4.0.0 (2018) |
| 2018 | 301a | Nacidos vivos con peso menor a 2500g | 4.0.1 (2018) |
| 2019-2020 | 301a | Nacidos vivos con peso menor a 2500g | 5.0.1 (2020) |
| 2021 | 301a | Nacidos vivos con peso menor a 2500g | 6.0.0 (2021) |
| 2022-2023 | 301a | Nacidos vivos con peso menor a 2500g | 6.0.1 (2022) |
| 2024-2025 | 301a | 3. Nacidos vivos con peso menor a 2500g | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
