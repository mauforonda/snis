# Consulta externa por especialidad

Atenciones registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2025. Fuente: SNIS, formularios 301b.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2025 |
| Periodicidad | mensual |
| Municipios con registros | 106 |
| Desagregación | sexo, edad, nuevo o repetido, especialidad |
| Filas | 1.904.265 |

Valores de `especialidad` (especialidad):

- Alergologia (2015-2025)
- Anestesiologia (2015-2025)
- Angiologia (2015-2021, 2023-2025)
- Cardiologia (2015-2025)
- Cirugia cardiovascular (2015-2025)
- Cirugia gastroenterologica (2015-2025)
- Cirugia general (2015-2025)
- Cirugia maxilo facial (2015-2025)
- Cirugia oftalmologica (2015-2018, 2021-2025)
- Cirugia oncologica (2015-2025)
- Cirugia ortopedica y traumatologica (2015-2025)
- Cirugia pediatrica (2015-2025)
- Cirugia plastica (2015-2025)
- Cirugia toracica (2015-2025)
- Coloproctologia (2015-2025)
- Colposcopia (2015-2024)
- Dermatologia (2015-2025)
- Endocrinologia (2015-2025)
- Estomatologia (2015, 2017-2023, 2025)
- Foniatria (2015-2025)
- Gastroenterologia (2015-2025)
- Geriatria (2015-2025)
- Ginecologia (2015-2025)
- Ginecologia y obstetricia (2015-2025)
- Hematologia (2015-2025)
- Infectologia (2015-2025)
- Inmunologia (2015-2025)
- Mastologia (2015-2025)
- Medicina critica y terapia intensiva (2015-2025)
- Medicina del trabajo (2015-2025)
- Medicina familiar (2015-2025)
- Medicina familiar y comunitaria (safci) (2015-2025)
- Medicina fisica y rehabilitacion (fisioterapia) (2015-2025)
- Medicina general (2015-2025)
- Medicina interna (2015-2025)
- Medicina tradicional (2015-2020, 2022-2025)
- Medicina tropical (2015-2025)
- Nefrologia (2015-2025)
- Neonatologia (2015-2025)
- Neumologia (2015-2025)
- Neurocirugia (2015-2025)
- Neurologia (2015-2025)
- Nutricion (2015-2025)
- Obstetricia (2015-2025)
- Odontologia (2015-2025)
- Odontologia - endodoncia (2015-2025)
- Odontologia pediatrica (2015-2025)
- Oftalmologia (2015-2025)
- Oncologia (2015-2025)
- Otorrinolaringologia (2015-2025)
- Otros especialidades (2015-2025)
- Pediatria (2015-2025)
- Proctologia (2015-2025)
- Psicologia (2015-2025)
- Psiquiatria (2015-2025)
- Quemados (2015-2025)
- Radioterapia (2015-2024)
- Reumatologia (2015-2025)
- Traumatologia (2015-2025)
- Traumatologia y ortopedia infantil (2015-2025)
- y 8 valores más (ver `datapackage.json`)

Valores de `caso` (nuevo o repetido):

- nuevo (2015-2025)
- repetido (2015-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015-2025 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2015 | 4.335.180 |
| 2016 | 5.429.750 |
| 2017 | 6.079.053 |
| 2018 | 6.943.381 |
| 2019 | 6.545.341 |
| 2020 | 7.263.706 |
| 2021 | 5.498.108 |
| 2022 | 7.214.155 |
| 2023 | 8.560.460 |
| 2024 | 9.291.712 |
| 2025 | 9.706.612 |

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
| `especialidad` | string | Especialidad del hospital que atiende. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/consultas/consulta_externa_por_especialidad/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/consultas/consulta_externa_por_especialidad/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/consultas/consulta_externa_por_especialidad/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015-2025 | 301b | 1 a 4 años; 10 a 14 años; 15 a 19 años; 20 a 39 años; 40 a 49 años; 5 a 9 años; 50 a 59 años; 6 meses a menor de 1 año; 60 y más; Menor de 6 meses |  |
