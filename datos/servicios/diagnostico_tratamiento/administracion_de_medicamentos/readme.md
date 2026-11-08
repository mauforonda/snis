# Administracion de medicamentos

Estudios y procedimientos realizados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2024-2025. Fuente: SNIS, formularios 301b.

## Qué es

| | |
| --- | --- |
| Gestiones | 2024-2025 |
| Periodicidad | mensual |
| Municipios con registros | 69 |
| Desagregación | servicio |
| Filas | 2.608 |

Valores de `servicio` (servicio):

- consulta externa (2024-2025)
- emergencia (2024-2025)
- internación (2024-2025)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2024 | 3.792.487 |
| 2025 | 5.208.607 |

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
| `servicio` | string | Servicio que atiende o pide el estudio. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/diagnostico_tratamiento/administracion_de_medicamentos/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/diagnostico_tratamiento/administracion_de_medicamentos/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2024-2025 | 301b | Administracion de medicamentos |  |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 301b, actividades de enfermería, 2024-2025: cada variable tiene tres columnas sin rótulo ("Sueros", "Sueros1", "Sueros2") que suman el total. El formulario 301b de 2024 tiene, en ese orden, las columnas emergencias, consulta externa e internación, y el instructivo de 2024 nombra los mismos servicios: se publican como esos servicios.
