# Mujeres con muestra de citologia cervico vaginal

Atenciones registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | mensual |
| Municipios con registros | 344 |
| Desagregación | edad |
| Filas | 176.399 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015-2023 | <15, 15-19, 20-34, 35-49, 50+ |
| 2024-2025 | <10, 10-14, 15-19, 20-34, 35-49, 50+ |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 176.612 |
| 2002 | 193.271 |
| 2003 | 190.539 |
| 2004 | 209.273 |
| 2005 | 252.075 |
| 2006 | 250.360 |
| 2007 | 312.374 |
| 2008 | 316.703 |
| 2009 | 336.644 |
| 2010 | 344.893 |
| 2011 | 382.169 |
| 2012 | 383.401 |
| 2013 | 449.571 |
| 2014 | 441.113 |
| 2015 | 456.821 |
| 2016 | 470.704 |
| 2017 | 477.863 |
| 2018 | 519.360 |
| 2019 | 511.709 |
| 2020 | 238.469 |
| 2021 | 341.123 |
| 2022 | 431.529 |
| 2023 | 483.231 |
| 2024 | 519.816 |
| 2025 | 483.153 |

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
from 'datos/servicios/anticoncepcion_prevencion_cancer/mujeres_con_muestras_de_pap_tomadas/datos.parquet'
group by gestion order by gestion;

-- Por gestión y edad_grupo
select gestion, edad_grupo, sum(cantidad) as cantidad
from 'datos/servicios/anticoncepcion_prevencion_cancer/mujeres_con_muestras_de_pap_tomadas/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/anticoncepcion_prevencion_cancer/mujeres_con_muestras_de_pap_tomadas/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2003 | 301 | Mujeres con muestra de citologia cervico vaginal |  |
| 2004-2007 | 301 | Mujeres con muestra de PAP tomada |  |
| 2008-2009 | 301 | Mujeres con muestra de PAP tomada | 1.0.4 (2013) |
| 2010-2013 | 301 | Mujeres con muestra de PAP | 1.0.4 (2013) |
| 2014 | 301 | 5.18 Mujeres con muestra de PAP | 2.0.0 (2014) |
| 2015-2016 | 301a | Número de mujeres con muestras de PAP tomadas |  |
| 2017 | 301a | Número de mujeres con muestras de PAP tomadas | 4.0.0 (2018) |
| 2018 | 301a | Número de mujeres con muestras de PAP tomadas | 4.0.1 (2018) |
| 2019-2020 | 301a | Número de mujeres con muestras de PAP tomadas | 5.0.1 (2020) |
| 2021 | 301a | Número de mujeres con muestras de PAP tomadas | 6.0.0 (2021) |
| 2022-2023 | 301a | Número de mujeres con muestras de PAP tomadas | 6.0.1 (2022) |
| 2024-2025 | 301a | Número de mujeres con muestras de PAP tomadas | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 301a, anticoncepción y prevención del cáncer (2015-2016) e interrupción legal del embarazo (2021): las variables tienen cinco columnas sin rótulo ("Número de condones entregados", "...1" a "...4"). Son las bandas de edad <15, 15-19, 20-34, 35-49 y 50+, en ese orden. En anticoncepción las proporciones coinciden con las de 2017 (muestras de PAP 2016: 0,3 %, 7,1 %, 48,5 %, 32,0 % y 12,2 %; 2017: 0,3 %, 7,1 %, 48,4 %, 31,7 % y 12,5 %). En la interrupción legal del embarazo, el encabezado de 2022 une cada columna numerada con su banda ("A. < 15", "B. 15 A 19 ... 1"). En 2022 la segunda banda de las causales riesgo de salud de la madre y malformación dice "15 A 49"; es 15-19.
- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
