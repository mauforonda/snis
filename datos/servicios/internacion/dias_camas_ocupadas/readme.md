# Dias cama ocupada

Registros de internación en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2025. Fuente: SNIS, formularios 301b.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2025 |
| Periodicidad | mensual |
| Municipios con registros | 95 |
| Desagregación | especialidad |
| Filas | 66.628 |

Valores de `especialidad` (especialidad):

- Anestesiologia (2015-2018, 2021-2022, 2024)
- Cardiologia (2015-2025)
- Cirugia cardiovascular (2015-2025)
- Cirugia gastroenterologica (2015-2017, 2019-2025)
- Cirugia general (2015-2025)
- Cirugia maxilo facial (2015-2025)
- Cirugia oncologica (2015-2025)
- Cirugia ortopedica y traumatologica (2015-2025)
- Cirugia pediatrica (2015-2025)
- Cirugia plastica (2015-2025)
- Cirugia toracica (2015-2025)
- Coloproctologia (2015-2025)
- Dermatologia (2015-2025)
- Endocrinologia (2015-2025)
- Gastroenterologia (2015-2025)
- Geriatria (2015-2025)
- Ginecologia (2015-2025)
- Ginecologia y obstetricia (2015-2025)
- Hematologia (2015-2025)
- Infectologia (2015-2025)
- Medicina critica y terapia intensiva (2015-2025)
- Medicina general (2015-2025)
- Medicina interna (2015-2025)
- Nefrologia (2015-2025)
- Neonatologia (2015-2025)
- Neumologia (2015-2025)
- Neurocirugia (2015-2025)
- Neurologia (2015-2025)
- Nutricion (2015-2018, 2021-2024)
- Obstetricia (2015-2025)
- Oftalmologia (2015-2025)
- Oncologia (2015-2025)
- Otorrinolaringologia (2015-2025)
- Otros especialidades (2015-2025)
- Pediatria (2015-2025)
- Perinatologia (2015, 2018, 2021-2025)
- Psicologia (2015-2024)
- Psiquiatria (2015-2025)
- Quemados (2015-2025)
- Reumatologia (2015-2025)
- Toxicologia (2015-2025)
- Traumatologia (2015-2025)
- Unidad de cuidados intermedios (uci) (2015-2024)
- Urologia (2015-2025)
- Cirugia oftalmologica (2016-2017, 2020, 2023-2025)
- Angiologia (2017-2025)
- Otras especialidades (2017, 2019-2024)
- Alergologia (2018, 2020-2023, 2025)
- Inmunologia (2018-2025)
- Septico (2020-2024)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2015 | 2.084.257 |
| 2016 | 2.458.033 |
| 2017 | 2.893.435 |
| 2018 | 3.274.901 |
| 2019 | 3.203.068 |
| 2020 | 4.852.338 |
| 2021 | 2.724.919 |
| 2022 | 3.024.478 |
| 2023 | 3.445.185 |
| 2024 | 3.491.970 |
| 2025 | 3.446.473 |

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
| `especialidad` | string | Especialidad del hospital que atiende. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/internacion/dias_camas_ocupadas/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/internacion/dias_camas_ocupadas/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015-2025 | 301b | Dias Cama Ocupada |  |
