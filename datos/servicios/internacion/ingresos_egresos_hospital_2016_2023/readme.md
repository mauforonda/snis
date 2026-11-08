# Ingresos y egresos por servicio de internación (2016-2023)

Registros de internación en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2016-2023. Fuente: SNIS, formularios 301b.

## Qué es

| | |
| --- | --- |
| Gestiones | 2016-2023 |
| Periodicidad | mensual |
| Municipios con registros | 72 |
| Desagregación | movimiento, especialidad |
| Filas | 247.183 |

Valores de `movimiento` (movimiento):

- egreso: alta médica (2016-2023)
- egreso: contrarreferido (2016-2023)
- egreso: defunción a partir de 48 horas (2016-2023)
- egreso: defunción antes de 48 horas (2016-2023)
- egreso: traslado interno (2016-2023)
- ingreso y egreso el mismo día (2016-2023)
- ingreso: existencia al inicio (2016-2023)
- ingreso: nuevo (2016-2023)
- ingreso: referido (2016-2023)
- ingreso: traslado interno (2016-2023)

Valores de `especialidad` (especialidad):

- Alergologia (2016-2023)
- Anestesiologia (2016-2018, 2021-2022)
- Cardiologia (2016-2023)
- Cirugia cardiovascular (2016-2023)
- Cirugia gastroenterologica (2016-2017, 2019-2023)
- Cirugia general (2016-2023)
- Cirugia maxilo facial (2016-2023)
- Cirugia oftalmologica (2016-2017, 2020, 2023)
- Cirugia oncologica (2016-2023)
- Cirugia ortopedica y traumatologica (2016-2023)
- Cirugia pediatrica (2016-2023)
- Cirugia plastica (2016-2023)
- Cirugia toracica (2016-2023)
- Coloproctologia (2016-2023)
- Dermatologia (2016-2023)
- Endocrinologia (2016-2023)
- Gastroenterologia (2016-2023)
- Geriatria (2016-2023)
- Ginecologia (2016-2023)
- Ginecologia y obstetricia (2016-2023)
- Hematologia (2016-2023)
- Infectologia (2016-2023)
- Medicina critica y terapia intensiva (2016-2023)
- Medicina general (2016-2023)
- Medicina interna (2016-2023)
- Nefrologia (2016-2023)
- Neonatologia (2016-2023)
- Neumologia (2016-2023)
- Neurocirugia (2016-2023)
- Neurologia (2016-2023)
- Nutricion (2016-2018, 2021-2023)
- Obstetricia (2016-2023)
- Oftalmologia (2016-2023)
- Oncologia (2016-2023)
- Otorrinolaringologia (2016-2023)
- Otros especialidades (2016-2023)
- Pediatria (2016-2023)
- Psicologia (2016-2023)
- Psiquiatria (2016-2023)
- Quemados (2016-2023)
- Reumatologia (2016-2023)
- Toxicologia (2016-2023)
- Traumatologia (2016-2023)
- Unidad de cuidados intermedios (uci) (2016-2023)
- Urologia (2016-2023)
- Angiologia (2017-2023)
- Otras especialidades (2017, 2019-2023)
- Perinatologia (2017-2018, 2021-2023)
- Inmunologia (2018-2023)
- Septico (2020-2023)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2016 | 1.181.597 |
| 2017 | 1.341.101 |
| 2018 | 1.480.501 |
| 2019 | 1.429.826 |
| 2020 | 2.229.042 |
| 2021 | 1.213.228 |
| 2022 | 1.358.939 |
| 2023 | 1.543.873 |

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
| `movimiento` | string | Ingreso o egreso y su tipo. |
| `especialidad` | string | Especialidad del hospital que atiende. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/internacion/ingresos_egresos_hospital_2016_2023/datos.parquet'
group by gestion order by gestion;

-- Por gestión y movimiento
select gestion, movimiento, sum(cantidad) as cantidad
from 'datos/servicios/internacion/ingresos_egresos_hospital_2016_2023/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/internacion/ingresos_egresos_hospital_2016_2023/datos.parquet'
where gestion = 2023 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Ingresos y egresos por servicio de internación (2015)](../../../servicios/internacion/ingresos_egresos_hospital_2015/readme.md): 2015, formulario 301b.
- Ingresos y egresos por servicio de internación (2016-2023) (este dataset): 2016-2023, formulario 301b.
- [Ingresos y egresos por servicio de internación (2024-2025)](../../../servicios/internacion/ingresos_egresos_hospital_2024_2025/readme.md): 2024-2025, formulario 301b.

Las categorías de `movimiento` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/internacion/ingresos_egresos_hospital_2015/datos.parquet',
    'datos/servicios/internacion/ingresos_egresos_hospital_2016_2023/datos.parquet',
    'datos/servicios/internacion/ingresos_egresos_hospital_2024_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2016-2023 | 301b | Alta; Contrareferidos; Defunción antes de 48 Hrs.; Defunción despues de 48 Hrs.; Existencia; Ingresos y egresos del mismo dia; Nuevos; Referidos; Traslado Interno - Egresos; Traslado Interno - Ingresos |  |
