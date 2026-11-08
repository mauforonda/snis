# Ingresos y egresos por servicio de internación (2015)

Registros de internación en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015. Fuente: SNIS, formularios 301b.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015 |
| Periodicidad | mensual |
| Municipios con registros | 51 |
| Desagregación | movimiento, especialidad |
| Filas | 8.064 |

Valores de `movimiento` (movimiento):

- egreso: contrarreferido (2015)
- egreso: defunción a partir de 48 horas (2015)
- egreso: defunción antes de 48 horas (2015)
- egreso: traslado interno (2015)
- ingreso y egreso el mismo día (2015)
- ingreso: traslado interno (2015)

Valores de `especialidad` (especialidad):

- Anestesiologia (2015)
- Cardiologia (2015)
- Cirugia cardiovascular (2015)
- Cirugia gastroenterologica (2015)
- Cirugia general (2015)
- Cirugia maxilo facial (2015)
- Cirugia oncologica (2015)
- Cirugia ortopedica y traumatologica (2015)
- Cirugia pediatrica (2015)
- Cirugia plastica (2015)
- Cirugia toracica (2015)
- Coloproctologia (2015)
- Dermatologia (2015)
- Endocrinologia (2015)
- Gastroenterologia (2015)
- Geriatria (2015)
- Ginecologia (2015)
- Ginecologia y obstetricia (2015)
- Hematologia (2015)
- Infectologia (2015)
- Medicina critica y terapia intensiva (2015)
- Medicina general (2015)
- Medicina interna (2015)
- Nefrologia (2015)
- Neonatologia (2015)
- Neumologia (2015)
- Neurocirugia (2015)
- Neurologia (2015)
- Nutricion (2015)
- Obstetricia (2015)
- Oftalmologia (2015)
- Oncologia (2015)
- Otorrinolaringologia (2015)
- Otros especialidades (2015)
- Pediatria (2015)
- Perinatologia (2015)
- Psicologia (2015)
- Psiquiatria (2015)
- Quemados (2015)
- Reumatologia (2015)
- Toxicologia (2015)
- Traumatologia (2015)
- Unidad de cuidados intermedios (uci) (2015)
- Urologia (2015)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2015 | 105.120 |

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
from 'datos/servicios/internacion/ingresos_egresos_hospital_2015/datos.parquet'
group by gestion order by gestion;

-- Por gestión y movimiento
select gestion, movimiento, sum(cantidad) as cantidad
from 'datos/servicios/internacion/ingresos_egresos_hospital_2015/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/internacion/ingresos_egresos_hospital_2015/datos.parquet'
where gestion = 2015 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Ingresos y egresos por servicio de internación (2015) (este dataset): 2015, formulario 301b.
- [Ingresos y egresos por servicio de internación (2016-2023)](../../../servicios/internacion/ingresos_egresos_hospital_2016_2023/readme.md): 2016-2023, formulario 301b.
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
| 2015 | 301b | Contrareferidos; Defunción antes de 48 Hrs.; Defunción despues de 48 Hrs.; Ingresos y egresos del mismo dia; Traslado Interno - Egresos; Traslado Interno - Ingresos |  |
