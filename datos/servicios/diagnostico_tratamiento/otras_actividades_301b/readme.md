# Otras actividades (formulario 301b)

Estudios y procedimientos realizados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2024-2025. Fuente: SNIS, formularios 301b.

## Qué es

| | |
| --- | --- |
| Gestiones | 2024-2025 |
| Periodicidad | mensual |
| Municipios con registros | 83 |
| Desagregación | servicio |
| Filas | 3.651 |

Valores de `servicio` (servicio):

- consulta externa (2024-2025)
- emergencia (2024-2025)
- internación (2024-2025)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2024 | 37.539.932 |
| 2025 | 64.548.169 |

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
from 'datos/servicios/diagnostico_tratamiento/otras_actividades_301b/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/diagnostico_tratamiento/otras_actividades_301b/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Otras actividades](../../../servicios/diagnostico_tratamiento/otras_actividades/readme.md): 2015-2025, formulario 301a.
- Otras actividades (formulario 301b) (este dataset): 2024-2025, formulario 301b.

El formulario 301a registra los servicios de primer nivel y el 301b, los de segundo y tercer nivel: son registros complementarios, no partes de un total. Sumarlos supone que ninguna atención se registra en los dos.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/diagnostico_tratamiento/otras_actividades/datos.parquet',
    'datos/servicios/diagnostico_tratamiento/otras_actividades_301b/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2024-2025 | 301b | Otras Actividades |  |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 301b, actividades de enfermería, 2024-2025: cada variable tiene tres columnas sin rótulo ("Sueros", "Sueros1", "Sueros2") que suman el total. El formulario 301b de 2024 tiene, en ese orden, las columnas emergencias, consulta externa e internación, y el instructivo de 2024 nombra los mismos servicios: se publican como esos servicios.
