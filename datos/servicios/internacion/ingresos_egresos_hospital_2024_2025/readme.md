# Ingresos y egresos por servicio de internación (2024-2025)

Registros de internación en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2024-2025. Fuente: SNIS, formularios 301b.

## Qué es

| | |
| --- | --- |
| Gestiones | 2024-2025 |
| Periodicidad | mensual |
| Municipios con registros | 96 |
| Desagregación | movimiento, especialidad |
| Filas | 84.484 |

Valores de `movimiento` (movimiento):

- egreso: alta médica (2024-2025)
- egreso: alta solicitada (2024-2025)
- egreso: contrarreferido (2024-2025)
- egreso: defunción a partir de 48 horas (2024-2025)
- egreso: defunción antes de 48 horas (2024-2025)
- egreso: fuga (2024-2025)
- egreso: traslado interno (2024-2025)
- ingreso y egreso el mismo día (2024-2025)
- ingreso: existencia al inicio (2024-2025)
- ingreso: nuevo (2024-2025)
- ingreso: referido (2024-2025)
- ingreso: traslado interno (2024-2025)

Valores de `especialidad` (especialidad):

- Alergologia (2024-2025)
- Anestesiologia (2024)
- Angiologia (2024-2025)
- Cardiologia (2024-2025)
- Cirugia cardiovascular (2024-2025)
- Cirugia gastroenterologica (2024-2025)
- Cirugia general (2024-2025)
- Cirugia maxilo facial (2024-2025)
- Cirugia oftalmologica (2024-2025)
- Cirugia oncologica (2024-2025)
- Cirugia ortopedica y traumatologica (2024-2025)
- Cirugia pediatrica (2024-2025)
- Cirugia plastica (2024-2025)
- Cirugia toracica (2024-2025)
- Coloproctologia (2024-2025)
- Dermatologia (2024-2025)
- Endocrinologia (2024-2025)
- Gastroenterologia (2024-2025)
- Geriatria (2024-2025)
- Ginecologia (2024-2025)
- Ginecologia y obstetricia (2024-2025)
- Hematologia (2024-2025)
- Infectologia (2024-2025)
- Inmunologia (2024-2025)
- Medicina critica y terapia intensiva (2024-2025)
- Medicina general (2024-2025)
- Medicina interna (2024-2025)
- Nefrologia (2024-2025)
- Neonatologia (2024-2025)
- Neumologia (2024-2025)
- Neurocirugia (2024-2025)
- Neurologia (2024-2025)
- Nutricion (2024)
- Obstetricia (2024-2025)
- Oftalmologia (2024-2025)
- Oncologia (2024-2025)
- Otorrinolaringologia (2024-2025)
- Otras especialidades (2024)
- Otros especialidades (2024-2025)
- Pediatria (2024-2025)
- Perinatologia (2024-2025)
- Psicologia (2024)
- Psiquiatria (2024-2025)
- Quemados (2024-2025)
- Reumatologia (2024-2025)
- Septico (2024)
- Toxicologia (2024-2025)
- Traumatologia (2024-2025)
- Unidad de cuidados intermedios (uci) (2024)
- Urologia (2024-2025)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2024 | 1.713.691 |
| 2025 | 1.782.681 |

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
from 'datos/servicios/internacion/ingresos_egresos_hospital_2024_2025/datos.parquet'
group by gestion order by gestion;

-- Por gestión y movimiento
select gestion, movimiento, sum(cantidad) as cantidad
from 'datos/servicios/internacion/ingresos_egresos_hospital_2024_2025/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/internacion/ingresos_egresos_hospital_2024_2025/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Ingresos y egresos por servicio de internación (2015)](../../../servicios/internacion/ingresos_egresos_hospital_2015/readme.md): 2015, formulario 301b.
- [Ingresos y egresos por servicio de internación (2016-2023)](../../../servicios/internacion/ingresos_egresos_hospital_2016_2023/readme.md): 2016-2023, formulario 301b.
- Ingresos y egresos por servicio de internación (2024-2025) (este dataset): 2024-2025, formulario 301b.

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
| 2024-2025 | 301b | Contrareferidos; Egresos-Alta Fuga; Egresos-Alta Medica; Egresos-Alta Solicitada; Egresos-Defunción a partir de 48 Hrs.; Egresos-Defunción antes de 48 Hrs.; Egresos-Traslado Interno; Ingresos y egresos del mismo dia; Ingresos-Existencia; Ingresos-Nuevos; Ingresos-Traslado Interno; Referidos |  |
