# Malaria: tratamientos iniciados en el mes por agente comun

Registros en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2005-2006. Fuente: SNIS, formularios 301.

## Qué es

| | |
| --- | --- |
| Gestiones | 2005-2006 |
| Periodicidad | mensual |
| Municipios con registros | 57 |
| Desagregación |  |
| Filas | 226 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2005 | 624 |
| 2006 | 1.073 |

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
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_por_agente_comun/datos.parquet'
group by gestion order by gestion;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_por_agente_comun/datos.parquet'
where gestion = 2006 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Malaria: tratamientos iniciados en el mes](../../../servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes/readme.md): 2001-2003, formulario 301.
- [Malaria: tratamientos iniciados en el mes para p.falciparu](../../../servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_para_p_falciparu/readme.md): 2004, formulario 301.
- [Malaria: tratamientos iniciados en el mes para p.vivax](../../../servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_para_p_vivax/readme.md): 2004, formulario 301.
- Malaria: tratamientos iniciados en el mes por agente comun (este dataset): 2005-2006, formulario 301.
- [Malaria: tratamientos iniciados en el mes por personal de](../../../servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_por_personal_de/readme.md): 2005-2006, formulario 301.
- [Malaria: tratamientos iniciados por sospecha](../../../servicios/control_enfermedades/malaria_tratamientos_iniciados_por_sospecha/readme.md): 2007-2014, formulario 301.

Los tratamientos de malaria iniciados cambian de categorías casi cada gestión: en total (2001-2003), por especie (2004), por quién trata (2005-2006) y por sospecha (2007-2014). En 2001-2003 el formulario cuenta también los tratamientos iniciados por sospecha, en otro dataset. Consultarlos juntos como una serie supone que las categorías de cada gestión suman todos los tratamientos iniciados.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes/datos.parquet',
    'datos/servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_para_p_falciparu/datos.parquet',
    'datos/servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_para_p_vivax/datos.parquet',
    'datos/servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_por_agente_comun/datos.parquet',
    'datos/servicios/control_enfermedades/malaria_tratamientos_iniciados_en_el_mes_por_personal_de/datos.parquet',
    'datos/servicios/control_enfermedades/malaria_tratamientos_iniciados_por_sospecha/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2005-2006 | 301 | Tratamientos iniciados en el mes por agente comun |  |
