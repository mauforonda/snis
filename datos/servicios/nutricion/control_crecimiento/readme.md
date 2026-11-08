# Control de crecimiento infantil

Atenciones registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2001-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2025 |
| Periodicidad | mensual |
| Municipios con registros | 344 |
| Desagregación | sexo, edad, nuevo o repetido, lugar |
| Filas | 1.149.138 |

Valores de `lugar` (lugar):

- dentro (2015-2025)
- fuera (2015-2025)

Valores de `caso` (nuevo o repetido):

- nuevo (2001-2013, 2015-2025)
- repetido (2001-2004, 2007-2013, 2015-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001-2006 | <2, 2-4 |
| 2007-2025 | <1, 1, 2-4 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2001 | 1.085.347 |
| 2002 | 1.170.620 |
| 2003 | 1.334.289 |
| 2004 | 1.416.144 |
| 2005 | 1.476.875 |
| 2006 | 1.510.463 |
| 2007 | 2.475.757 |
| 2008 | 3.013.866 |
| 2009 | 3.445.693 |
| 2010 | 3.964.001 |
| 2011 | 4.257.426 |
| 2012 | 4.248.286 |
| 2013 | 4.592.296 |
| 2014 | 4.946.368 |
| 2015 | 5.057.427 |
| 2016 | 5.029.003 |
| 2017 | 4.804.067 |
| 2018 | 4.780.585 |
| 2019 | 4.239.261 |
| 2020 | 2.672.926 |
| 2021 | 3.150.966 |
| 2022 | 3.451.144 |
| 2023 | 3.713.879 |
| 2024 | 3.498.672 |
| 2025 | 3.264.342 |

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
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `caso` | string | nuevo, repetido, seguimiento o primera, como lo registra el formulario. |
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/nutricion/control_crecimiento/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/nutricion/control_crecimiento/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/nutricion/control_crecimiento/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2003 | 301 | Controles nuevos en niños de 2 años a < de 5 años; Controles nuevos en niños menores de 2 años; Controles repetidos en niños de 2 años a < de 5 añ; Controles repetidos en niños menores de 2 años |  |
| 2004 | 301 | Controles nuevos en niños de 2 años a < de 5 años; Controles nuevos en niños menores de 2 años; Controles repetidos en niños de 2 años de < 5 años; Controles repetidos en niños menores de 2 años |  |
| 2005-2006 | 301 | Controles nuevos en niños de 2 años a < de 5 a; Controles nuevos en niños menores de 2 años; Controles repetidos en niños de 2 años de < 5; Controles repetidos en niños menores de 2 años |  |
| 2007 | 301 | Control del niño de 1 año a menor de 2 años; Control del niño de 2 años a menor de 5 años; Control del niño menor de 1 año |  |
| 2008-2013 | 301 | Control del niño (a) de 1 año a menor de 2 años; Control del niño (a) de 2 años a menor de 5 años; Control del niño menor de 1 año | 1.0.4 (2013) |
| 2014 | 301 | 6.1 Control del niño menor de 1 año; 6.2 Control del niño (a) de 1 año a menor de 2 años; 6.3 Control del niño (a) de 2 años a menor de 5 años | 2.0.0 (2014) |
| 2015 | 301a | Control del niño(a) de 1 año a menor de 2 años dentro del establecimiento; Control del niño(a) de 1 año a menor de 2 años fuera del establecimiento; Control del niño(a) de 2 años a menor de 5 años dentro del establecimiento; Control del niño(a) de 2 años a menor de 5 años fuera del establecimiento; Control del niño(a) menor de 1 año dentro del establecimiento; Control del niño(a) menor de 1 año fuera del establecimiento | 3.0.1 (2016) |
| 2016 | 301a | Control del niño(a) de 1 año a menor de 2 años dentro del establecimiento; Control del niño(a) de 1 año a menor de 2 años fuera del establecimiento; Control del niño(a) de 2 años a menor de 5 años dentro del establecimiento; Control del niño(a) de 2 años a menor de 5 años fuera del establecimiento; Control del niño(a) menor de 1 año dentro del establecimiento; Control del niño(a) menor de 1 año fuera del establecimiento | 3.0.2 (2016) |
| 2017 | 301a | Control del niño(a) de 1 año a menor de 2 años dentro del establecimiento; Control del niño(a) de 1 año a menor de 2 años fuera del establecimiento; Control del niño(a) de 2 años a menor de 5 años dentro del establecimiento; Control del niño(a) de 2 años a menor de 5 años fuera del establecimiento; Control del niño(a) menor de 1 año dentro del establecimiento; Control del niño(a) menor de 1 año fuera del establecimiento | 4.0.0 (2018) |
| 2018 | 301a | Control del niño(a) de 1 año a menor de 2 años dentro del establecimiento; Control del niño(a) de 1 año a menor de 2 años fuera del establecimiento; Control del niño(a) de 2 años a menor de 5 años dentro del establecimiento; Control del niño(a) de 2 años a menor de 5 años fuera del establecimiento; Control del niño(a) menor de 1 año dentro del establecimiento; Control del niño(a) menor de 1 año fuera del establecimiento | 4.0.1 (2018) |
| 2019-2020 | 301a | Control del niño(a) de 1 año a menor de 2 años dentro del establecimiento; Control del niño(a) de 1 año a menor de 2 años fuera del establecimiento; Control del niño(a) de 2 años a menor de 5 años dentro del establecimiento; Control del niño(a) de 2 años a menor de 5 años fuera del establecimiento; Control del niño(a) menor de 1 año dentro del establecimiento; Control del niño(a) menor de 1 año fuera del establecimiento | 5.0.1 (2020) |
| 2021 | 301a | Control del niño(a) de 1 año a menor de 2 años dentro del establecimiento; Control del niño(a) de 1 año a menor de 2 años fuera del establecimiento; Control del niño(a) de 2 años a menor de 5 años dentro del establecimiento; Control del niño(a) de 2 años a menor de 5 años fuera del establecimiento; Control del niño(a) menor de 1 año dentro del establecimiento; Control del niño(a) menor de 1 año fuera del establecimiento | 6.0.0 (2021) |
| 2022-2023 | 301a | Control del niño(a) de 1 año a menor de 2 años dentro del establecimiento; Control del niño(a) de 1 año a menor de 2 años fuera del establecimiento; Control del niño(a) de 2 años a menor de 5 años dentro del establecimiento; Control del niño(a) de 2 años a menor de 5 años fuera del establecimiento; Control del niño(a) menor de 1 año dentro del establecimiento; Control del niño(a) menor de 1 año fuera del establecimiento | 6.0.1 (2022) |
| 2024-2025 | 301a | Control del niño(a) de 1 año a menor de 2 años dentro del establecimiento; Control del niño(a) de 1 año a menor de 2 años fuera del establecimiento; Control del niño(a) de 2 años a menor de 5 años dentro del establecimiento; Control del niño(a) de 2 años a menor de 5 años fuera del establecimiento; Control del niño(a) menor de 1 año dentro del establecimiento; Control del niño(a) menor de 1 año fuera del establecimiento | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 301, control de crecimiento, 2008-2009: el primer nivel dice siempre NUEVO; el segundo dice NUEVO/REPETIDO y sus totales coinciden con "TOTAL NUEVO" y "TOTAL REPETIDO": vale el segundo.
- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
