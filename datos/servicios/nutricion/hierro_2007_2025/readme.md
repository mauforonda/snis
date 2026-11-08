# Personas que recibieron hierro (2007-2025)

Atenciones registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2007-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2007-2025 |
| Periodicidad | mensual |
| Municipios con registros | 344 |
| Desagregación | sexo, edad, embarazo o puerperio |
| Filas | 333.309 |

Valores de `condicion` (embarazo o puerperio):

- embarazada (2007-2025)
- puerpera (2007-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2007-2014 | 6m-1, 2-4 |
| 2015-2020 | <1, 1, 2-4 |
| 2021-2025 | <1, <6m, 1, 2-4 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2007 | 844.792 |
| 2008 | 999.559 |
| 2009 | 861.984 |
| 2010 | 922.909 |
| 2011 | 997.092 |
| 2012 | 1.049.057 |
| 2013 | 1.166.391 |
| 2014 | 1.152.630 |
| 2015 | 1.134.767 |
| 2016 | 1.086.717 |
| 2017 | 1.053.419 |
| 2018 | 1.089.999 |
| 2019 | 1.036.295 |
| 2020 | 818.558 |
| 2021 | 817.939 |
| 2022 | 859.677 |
| 2023 | 869.838 |
| 2024 | 833.554 |
| 2025 | 747.219 |

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
| `condicion` | string | embarazada o puerpera. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/nutricion/hierro_2007_2025/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/nutricion/hierro_2007_2025/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/nutricion/hierro_2007_2025/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Personas que recibieron hierro (2001-2006)](../../../servicios/nutricion/hierro_2001_2006/readme.md): 2001-2006, formulario 301.
- Personas que recibieron hierro (2007-2025) (este dataset): 2007-2025, formulario 301, 301a.

Las categorías de `dosis` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/nutricion/hierro_2001_2006/datos.parquet',
    'datos/servicios/nutricion/hierro_2007_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2007 | 301 | Mujeres embarazadas que recibieron 90 tabletas de; Mujeres puérperas que recibieron 90 tabletas de hi; Niños de 2 años a menores de 5 años con dosis comp; Niños de 6 meses a menores de 2 años con dosis com |  |
| 2008 | 301 | Mujeres embarazadas con dosis completa de hierro; Mujeres puérperas con dosis completa de hierro; Niños de 2 años a menores de 5 años con dosis comp; Niños de 6 meses a menores de 2 años con dosis com | 1.0.4 (2013) |
| 2009 | 301 | Mujeres embarazadas con dosis completa de hierro; Mujeres puérperas con dosis completa de hierro; Niños de 2 años a menores de 5 años con dosis completa de hierro; Niños de 6 meses a menores de 2 años con dosis completa de hierro | 1.0.4 (2013) |
| 2010-2013 | 301 | Mujeres embarazadas con dosis completa de hierro; Mujeres puérperas con dosis completa de hierro; Niños (as) de 2 años a menores de 5 años con dosis completa de hierro; Niños (as) de 6 meses a menores de 2 años con dosis completa de hierro | 1.0.4 (2013) |
| 2014 | 301 | 8.1 Mujeres embarazadas con dosis completa de hierro; 8.2 Mujeres puérperas con dosis completa de hierro; 8.3 Niños (as) de 6 meses a menores de 2 años con dosis completa de hierro; 8.4 Niños (as) de 2 años a menores de 5 años con dosis completa de hierro | 2.0.0 (2014) |
| 2015 | 301a | Mujeres embarazadas con dosis completa de hierro; Mujeres puérperas con dosis completa de hierro; Niñas(os) de 1 año con dosis completa de hierro; Niñas(os) menores de 1 año con dosis completa de hierro; Niños (as) de 2 años a menores de 5 años con dosis completa de hierro | 3.0.1 (2016) |
| 2016 | 301a | Mujeres embarazadas con dosis completa de hierro; Mujeres puérperas con dosis completa de hierro; Niñas(os) de 1 año con dosis completa de hierro; Niñas(os) menores de 1 año con dosis completa de hierro; Niños (as) de 2 años a menores de 5 años con dosis completa de hierro | 3.0.2 (2016) |
| 2017 | 301a | Mujeres embarazadas con dosis completa de hierro; Mujeres puérperas con dosis completa de hierro; Niñas(os) de 1 año con dosis completa de hierro; Niñas(os) menores de 1 año con dosis completa de hierro; Niños (as) de 2 años a menores de 5 años con dosis completa de hierro | 4.0.0 (2018) |
| 2018 | 301a | Mujeres embarazadas con dosis completa de hierro; Mujeres puérperas con dosis completa de hierro; Niñas(os) de 1 año con dosis completa de hierro; Niñas(os) menores de 1 año con dosis completa de hierro; Niños (as) de 2 años a menores de 5 años con dosis completa de hierro | 4.0.1 (2018) |
| 2019-2020 | 301a | Mujeres embarazadas con dosis completa de hierro; Mujeres puérperas con dosis completa de hierro; Niñas(os) de 1 año con dosis completa de hierro; Niñas(os) menores de 1 año con dosis completa de hierro; Niños (as) de 2 años a menores de 5 años con dosis completa de hierro | 5.0.1 (2020) |
| 2021 | 301a | Mujeres embarazadas con dosis completa de hierro; Mujeres puérperas con dosis completa de hierro; Niñas(os) de 1 año con dosis completa de hierro; Niñas(os) menores de 1 año con dosis completa de hierro; Niñas(os) menores de 6 meses con dosis completa de hierro; Niños (as) de 2 años a menores de 5 años con dosis completa de hierro | 6.0.0 (2021) |
| 2022-2023 | 301a | Mujeres embarazadas con dosis completa de hierro; Mujeres puérperas con dosis completa de hierro; Niñas(os) de 1 año con dosis completa de hierro; Niñas(os) menores de 1 año con dosis completa de hierro; Niñas(os) menores de 6 meses con dosis completa de hierro; Niños (as) de 2 años a menores de 5 años con dosis completa de hierro | 6.0.1 (2022) |
| 2024-2025 | 301a | 3. Niñas(os) menores de 6 meses con dosis completa de hierro (a partir de los 4 m); Mujeres embarazadas con dosis completa de hierro; Mujeres puérperas con dosis completa de hierro; Niñas (os) de 2 años a menores de 5 años con dosis completa de hierro; Niñas(os) de 1 año con dosis completa de hierro; Niñas(os) menores de 1 año con dosis completa de hierro | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
