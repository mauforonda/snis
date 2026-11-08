# Nacidos muertos atendidos por personal de salud

Atenciones y nacimientos registrados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | mensual |
| Municipios con registros | 324 |
| Desagregación | lugar |
| Filas | 3.948 |

Valores de `lugar` (lugar):

- domicilio (2001-2025)
- servicio (2024-2025)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 227 |
| 2002 | 234 |
| 2003 | 255 |
| 2004 | 220 |
| 2005 | 216 |
| 2006 | 217 |
| 2007 | 191 |
| 2008 | 226 |
| 2009 | 317 |
| 2010 | 270 |
| 2011 | 242 |
| 2012 | 188 |
| 2013 | 187 |
| 2014 | 181 |
| 2015 | 115 |
| 2016 | 73 |
| 2017 | 96 |
| 2018 | 85 |
| 2019 | 69 |
| 2020 | 71 |
| 2021 | 69 |
| 2022 | 58 |
| 2023 | 181 |
| 2024 | 1.081 |
| 2025 | 1.288 |

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
from 'datos/servicios/salud_materna_neonatal/nacidos_muertos_atendidos_por_personal_de_salud/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/nacidos_muertos_atendidos_por_personal_de_salud/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2003 | 301 | Nacidos muertos atendidos por personal de sal |  |
| 2004 | 301 | Nacidos muertos atendidos por personal de salud |  |
| 2005-2007 | 301 | Nacidos muertos atendidos por personal de sal |  |
| 2008 | 301 | Nacidos muertos atendidos por personal de salud | 1.0.4 (2013) |
| 2009 | 301 | Nacidos muertos atendidos por personal de salud |  |
| 2010-2013 | 301 | Nacidos muertos atendidos por personal de salud | 1.0.4 (2013) |
| 2014 | 301 | 12.3 Nacidos muertos atendidos por personal de salud | 2.0.0 (2014) |
| 2015 | 301a | Nacidos muertos atendidos por personal de salud | 3.0.1 (2016) |
| 2016 | 301a | Nacidos muertos atendidos por personal de salud | 3.0.2 (2016) |
| 2017 | 301a | Nacidos muertos atendidos por personal de salud | 4.0.0 (2018) |
| 2018 | 301a | Nacidos muertos atendidos por personal de salud | 4.0.1 (2018) |
| 2019-2020 | 301a | Nacidos muertos atendidos por personal de salud | 5.0.1 (2020) |
| 2021 | 301a | Nacidos muertos atendidos por personal de salud | 6.0.0 (2021) |
| 2022-2023 | 301a | Nacidos muertos atendidos por personal de salud | 6.0.1 (2022) |
| 2024-2025 | 301a | 13. Nacidos muertos atendidos por personal de salud | 7.0.1 (2026) |
