# Camas

Registros de internación en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2016-2025. Fuente: SNIS, formularios 301b.

## Qué es

| | |
| --- | --- |
| Gestiones | 2016-2025 |
| Periodicidad | mensual |
| Municipios con registros | 97 |
| Desagregación | especialidad |
| Filas | 67.005 |

Valores de `especialidad` (especialidad):

- Alergologia (2016-2025)
- Anestesiologia (2016-2019, 2021-2024)
- Cardiologia (2016-2025)
- Cirugia cardiovascular (2016-2025)
- Cirugia gastroenterologica (2016-2017, 2019-2025)
- Cirugia general (2016-2025)
- Cirugia maxilo facial (2016-2025)
- Cirugia oftalmologica (2016-2018, 2020, 2023-2025)
- Cirugia oncologica (2016-2025)
- Cirugia ortopedica y traumatologica (2016-2025)
- Cirugia pediatrica (2016-2025)
- Cirugia plastica (2016-2025)
- Cirugia toracica (2016-2025)
- Coloproctologia (2016-2025)
- Dermatologia (2016-2025)
- Endocrinologia (2016-2025)
- Gastroenterologia (2016-2025)
- Geriatria (2016-2025)
- Ginecologia (2016-2025)
- Ginecologia y obstetricia (2016-2025)
- Hematologia (2016-2025)
- Infectologia (2016-2025)
- Medicina critica y terapia intensiva (2016-2025)
- Medicina general (2016-2025)
- Medicina interna (2016-2025)
- Nefrologia (2016-2025)
- Neonatologia (2016-2025)
- Neumologia (2016-2025)
- Neurocirugia (2016-2025)
- Neurologia (2016-2025)
- Nutricion (2016-2018, 2021-2024)
- Obstetricia (2016-2025)
- Oftalmologia (2016-2025)
- Oncologia (2016-2025)
- Otorrinolaringologia (2016-2025)
- Otros especialidades (2016-2025)
- Pediatria (2016-2025)
- Psicologia (2016-2024)
- Psiquiatria (2016-2025)
- Quemados (2016-2025)
- Reumatologia (2016-2025)
- Septico (2016-2024)
- Toxicologia (2016-2025)
- Traumatologia (2016-2025)
- Unidad de cuidados intermedios (uci) (2016-2024)
- Urologia (2016-2025)
- Angiologia (2017-2025)
- Otras especialidades (2017, 2019-2024)
- Perinatologia (2017-2018, 2021-2025)
- Inmunologia (2018-2025)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2016 | 149.387 |
| 2017 | 172.361 |
| 2018 | 188.919 |
| 2019 | 186.184 |
| 2020 | 383.884 |
| 2021 | 205.675 |
| 2022 | 220.724 |
| 2023 | 225.764 |
| 2024 | 234.179 |
| 2025 | 240.433 |

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
from 'datos/servicios/internacion/camas/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/internacion/camas/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2016-2025 | 301b | Camas |  |
