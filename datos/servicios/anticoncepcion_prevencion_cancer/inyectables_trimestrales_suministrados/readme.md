# Inyectables trimestrales suministrados

Atenciones registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | mensual |
| Municipios con registros | 344 |
| Desagregación | edad |
| Filas | 184.328 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015-2023 | <15, 15-19, 20-34, 35-49, 50+ |
| 2024-2025 | <10, 10-14, 15-19, 20-34, 35-49, 50+ |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 135.721 |
| 2002 | 200.526 |
| 2003 | 269.928 |
| 2004 | 276.423 |
| 2005 | 288.751 |
| 2006 | 293.030 |
| 2007 | 317.363 |
| 2008 | 342.210 |
| 2009 | 324.096 |
| 2010 | 216.222 |
| 2011 | 251.255 |
| 2012 | 262.362 |
| 2013 | 280.906 |
| 2014 | 299.657 |
| 2015 | 283.701 |
| 2016 | 269.572 |
| 2017 | 258.218 |
| 2018 | 231.760 |
| 2019 | 219.503 |
| 2020 | 175.160 |
| 2021 | 182.515 |
| 2022 | 193.150 |
| 2023 | 195.866 |
| 2024 | 189.146 |
| 2025 | 175.370 |

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
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/anticoncepcion_prevencion_cancer/inyectables_trimestrales_suministrados/datos.parquet'
group by gestion order by gestion;

-- Por gestión y edad_grupo
select gestion, edad_grupo, sum(cantidad) as cantidad
from 'datos/servicios/anticoncepcion_prevencion_cancer/inyectables_trimestrales_suministrados/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/anticoncepcion_prevencion_cancer/inyectables_trimestrales_suministrados/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2003 | 301 | Número de inyectables trimestrales suministra |  |
| 2004 | 301 | Número de inyectables trimestrales suministrados |  |
| 2005-2007 | 301 | Número de inyectables trimestrales suministra |  |
| 2008-2009 | 301 | Número de inyectables trimestrales suministra | 1.0.4 (2013) |
| 2010-2013 | 301 | Número de inyectables trimestrales suministrados | 1.0.4 (2013) |
| 2014 | 301 | 5.06 Número de inyectables trimestrales suministrados | 2.0.0 (2014) |
| 2015-2016 | 301a | Número de inyectables trimestrales suministrados |  |
| 2017 | 301a | Número de inyectables trimestrales suministrados | 4.0.0 (2018) |
| 2018 | 301a | Número de inyectables trimestrales suministrados | 4.0.1 (2018) |
| 2019-2020 | 301a | Número de inyectables trimestrales suministrados | 5.0.1 (2020) |
| 2021 | 301a | Número de inyectables trimestrales suministrados | 6.0.0 (2021) |
| 2022-2023 | 301a | Número de inyectables trimestrales suministrados | 6.0.1 (2022) |
| 2024-2025 | 301a | Número de inyectables trimestrales suministrados | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 301a, anticoncepción y prevención del cáncer (2015-2016) e interrupción legal del embarazo (2021): las variables tienen cinco columnas sin rótulo ("Número de condones entregados", "...1" a "...4"). Son las bandas de edad <15, 15-19, 20-34, 35-49 y 50+, en ese orden. En anticoncepción las proporciones coinciden con las de 2017 (muestras de PAP 2016: 0,3 %, 7,1 %, 48,5 %, 32,0 % y 12,2 %; 2017: 0,3 %, 7,1 %, 48,4 %, 31,7 % y 12,5 %). En la interrupción legal del embarazo, el encabezado de 2022 une cada columna numerada con su banda ("A. < 15", "B. 15 A 19 ... 1"). En 2022 la segunda banda de las causales riesgo de salud de la madre y malformación dice "15 A 49"; es 15-19.
- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
