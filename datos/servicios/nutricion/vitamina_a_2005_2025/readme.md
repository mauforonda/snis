# Personas que recibieron vitamina A (2005-2025)

Atenciones registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2005-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2005-2025 |
| Periodicidad | mensual |
| Municipios con registros | 344 |
| Desagregación | dosis, sexo, edad, embarazo o puerperio |
| Filas | 404.367 |

Valores de `dosis` (dosis):

- 1 (2005-2025)
- 2 (2005-2025)
- única (2005-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2005-2014 | 6-11m, 1-4 |
| 2015-2025 | <1, 1, 2-4 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2005 | 1.237.256 |
| 2006 | 1.180.969 |
| 2007 | 1.248.504 |
| 2008 | 1.302.816 |
| 2009 | 1.291.285 |
| 2010 | 1.227.921 |
| 2011 | 1.286.978 |
| 2012 | 1.236.742 |
| 2013 | 1.302.142 |
| 2014 | 1.262.496 |
| 2015 | 1.320.058 |
| 2016 | 1.296.369 |
| 2017 | 1.234.735 |
| 2018 | 1.248.074 |
| 2019 | 1.138.516 |
| 2020 | 877.466 |
| 2021 | 952.508 |
| 2022 | 967.910 |
| 2023 | 975.679 |
| 2024 | 944.781 |
| 2025 | 884.354 |

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
| `condicion` | string | embarazada o puerpera. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/nutricion/vitamina_a_2005_2025/datos.parquet'
group by gestion order by gestion;

-- Por gestión y dosis
select gestion, dosis, sum(cantidad) as cantidad
from 'datos/servicios/nutricion/vitamina_a_2005_2025/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/nutricion/vitamina_a_2005_2025/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Personas que recibieron vitamina A (2001-2003)](../../../servicios/nutricion/vitamina_a_2001_2003/readme.md): 2001-2003, formulario 301.
- [Personas que recibieron vitamina A (2004)](../../../servicios/nutricion/vitamina_a_2004/readme.md): 2004, formulario 301.
- Personas que recibieron vitamina A (2005-2025) (este dataset): 2005-2025, formulario 301, 301a.

Las categorías de `dosis` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/nutricion/vitamina_a_2001_2003/datos.parquet',
    'datos/servicios/nutricion/vitamina_a_2004/datos.parquet',
    'datos/servicios/nutricion/vitamina_a_2005_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2005-2006 | 301 | Mujeres puérperas que recibieron dosis única d; Niños 1 a 4 años con 2da dosis de vitamina A; Niños de 1 a 4 años con 1ra dosis vitamina A; Niños de 6 a 11 meses con dosis única de vitam |  |
| 2007 | 301 | Mujeres puérperas que recibieron dosis única de vi; Niños de 1 año a menores de 5 años con 1ra dosis v; Niños de 1 año a menores de 5 años con 2da dosis v; Niños de 6 a 11 meses con dosis única de vitamina |  |
| 2008 | 301 | Mujeres puérperas que recibieron dosis única de vi; Niños de 1 año a menores de 5 años con 1ra dosis v; Niños de 1 año a menores de 5 años con 2da dosis v; Niños de 6 a 11 meses con dosis única de vitamina | 1.0.4 (2013) |
| 2009 | 301 | Mujeres puérperas que recibieron dosis única de vitamina A; Niños de 1 año a menores de 5 años con 1ra dosis vitamina A; Niños de 1 año a menores de 5 años con 2da dosis vitamina A; Niños de 6 a 11 meses con dosis única de vitamina A | 1.0.4 (2013) |
| 2010-2013 | 301 | Mujeres puérperas con dosis única de vitamina A; Niños (as) de 1 año a menores de 5 años con 1ra dosis vitamina A; Niños (as) de 1 año a menores de 5 años con 2da dosis vitamina A; Niños (as) de 6 meses a menor de 1 año con dosis única de vitamina A | 1.0.4 (2013) |
| 2014 | 301 | 8.5 Mujeres puérperas con dosis única de vitamina A; 8.6 Niños (as) de 6 meses a menor de 1 año con dosis única de vitamina A; 8.7 Niños (as) de 1 año a menores de 5 años con 1ra dosis vitamina A; 8.8 Niños (as) de 1 año a menores de 5 años con 2da dosis vitamina A | 2.0.0 (2014) |
| 2015 | 301a | Mujeres puérperas con dosis única de vitamina A; Niñas(os) de 1 año con 1ra. dosis de vitamina A; Niñas(os) de 1 año con 2da. dosis de vitamina A; Niñas(os) de 2 años a menores de 5 años con 1ra dosis vitamina A; Niñas(os) de 2 años a menores de 5 años con 2da dosis vitamina A; Niñas(os) menores de 1 año con dosis única de vitamina A | 3.0.1 (2016) |
| 2016 | 301a | Mujeres puérperas con dosis única de vitamina A; Niñas(os) de 1 año con 1ra. dosis de vitamina A; Niñas(os) de 1 año con 2da. dosis de vitamina A; Niñas(os) de 2 años a menores de 5 años con 1ra dosis vitamina A; Niñas(os) de 2 años a menores de 5 años con 2da dosis vitamina A; Niñas(os) menores de 1 año con dosis única de vitamina A | 3.0.2 (2016) |
| 2017 | 301a | Mujeres puérperas con dosis única de vitamina A; Niñas(os) de 1 año con 1ra. dosis de vitamina A; Niñas(os) de 1 año con 2da. dosis de vitamina A; Niñas(os) de 2 años a menores de 5 años con 1ra dosis vitamina A; Niñas(os) de 2 años a menores de 5 años con 2da dosis vitamina A; Niñas(os) menores de 1 año con dosis única de vitamina A | 4.0.0 (2018) |
| 2018 | 301a | Mujeres puérperas con dosis única de vitamina A; Niñas(os) de 1 año con 1ra. dosis de vitamina A; Niñas(os) de 1 año con 2da. dosis de vitamina A; Niñas(os) de 2 años a menores de 5 años con 1ra dosis vitamina A; Niñas(os) de 2 años a menores de 5 años con 2da dosis vitamina A; Niñas(os) menores de 1 año con dosis única de vitamina A | 4.0.1 (2018) |
| 2019-2020 | 301a | Mujeres puérperas con dosis única de vitamina A; Niñas(os) de 1 año con 1ra. dosis de vitamina A; Niñas(os) de 1 año con 2da. dosis de vitamina A; Niñas(os) de 2 años a menores de 5 años con 1ra dosis vitamina A; Niñas(os) de 2 años a menores de 5 años con 2da dosis vitamina A; Niñas(os) menores de 1 año con dosis única de vitamina A | 5.0.1 (2020) |
| 2021 | 301a | Mujeres puérperas con dosis única de vitamina A; Niñas(os) de 1 año con 1ra. dosis de vitamina A; Niñas(os) de 1 año con 2da. dosis de vitamina A; Niñas(os) de 2 años a menores de 5 años con 1ra dosis vitamina A; Niñas(os) de 2 años a menores de 5 años con 2da dosis vitamina A; Niñas(os) menores de 1 año con dosis única de vitamina A | 6.0.0 (2021) |
| 2022-2023 | 301a | Mujeres puérperas con dosis única de vitamina A; Niñas(os) de 1 año con 1ra. dosis de vitamina A; Niñas(os) de 1 año con 2da. dosis de vitamina A; Niñas(os) de 2 años a menores de 5 años con 1ra dosis vitamina A; Niñas(os) de 2 años a menores de 5 años con 2da dosis vitamina A; Niñas(os) menores de 1 año con dosis única de vitamina A | 6.0.1 (2022) |
| 2024-2025 | 301a | Mujeres puérperas con dosis única de vitamina A; Niñas(os) de 1 año con 1ra. dosis de vitamina A; Niñas(os) de 1 año con 2da. dosis de vitamina A; Niñas(os) de 2 años a menores de 5 años con 1ra dosis vitamina A; Niñas(os) de 2 años a menores de 5 años con 2da dosis vitamina A; Niñas(os) menores de 1 año con dosis única de vitamina A | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
