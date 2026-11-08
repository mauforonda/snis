# Vacuna Hepatitis B (2015-2020)

Dosis aplicadas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2020. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2020 |
| Periodicidad | mensual |
| Municipios con registros | 338 |
| Desagregación | dosis, grupo de población, sexo, lugar |
| Filas | 36.002 |

Valores de `dosis` (dosis):

- 1 (2015-2020)
- 2 (2015-2020)
- 3 (2015-2020)

Valores de `grupo` (grupo de población):

- personal de salud (2015-2020)
- personas con VIH (2015-2020)

Valores de `lugar` (lugar):

- dentro (2015-2020)
- fuera (2015-2020)

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2015 | 29.158 |
| 2016 | 33.904 |
| 2017 | 38.684 |
| 2018 | 92.677 |
| 2019 | 59.890 |
| 2020 | 34.606 |

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
| `grupo` | string | Grupo de población al que se dirige la vacuna. |
| `sexo` | string | mujer u hombre. |
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/hepatitis_b_2015_2020/datos.parquet'
group by gestion order by gestion;

-- Por gestión y dosis
select gestion, dosis, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/hepatitis_b_2015_2020/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/hepatitis_b_2015_2020/datos.parquet'
where gestion = 2020 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Vacuna Hepatitis B (2010-2014)](../../../servicios/vacunas/hepatitis_b_2010_2014/readme.md): 2010-2014, formulario 301.
- Vacuna Hepatitis B (2015-2020) (este dataset): 2015-2020, formulario 301a.
- [Vacuna Hepatitis B (2021-2025)](../../../servicios/vacunas/hepatitis_b_2021_2025/readme.md): 2021-2025, formulario 301a.

Las categorías de `dosis` y `grupo` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/vacunas/hepatitis_b_2010_2014/datos.parquet',
    'datos/servicios/vacunas/hepatitis_b_2015_2020/datos.parquet',
    'datos/servicios/vacunas/hepatitis_b_2021_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015 | 301a | Total Hepatitis B 1ra. dosis población vulnerable (VIH); Total Hepatitis B 1ra. dosis trabajadores de Salud; Total Hepatitis B 2da. dosis población vulnerable (VIH); Total Hepatitis B 2da. dosis trabajadores de Salud; Total Hepatitis B 3ra. dosis población vulnerable (VIH); Total Hepatitis B 3ra. dosis trabajadores de Salud | 3.0.1 (2016) |
| 2016 | 301a | Hepatitis B 1ra. dosis población vulnerable (VIH); Hepatitis B 1ra. dosis trabajadores de Salud; Hepatitis B 2da. dosis población vulnerable (VIH); Hepatitis B 2da. dosis trabajadores de Salud; Hepatitis B 3ra. dosis población vulnerable (VIH); Hepatitis B 3ra. dosis trabajadores de Salud | 3.0.2 (2016) |
| 2017 | 301a | Hepatitis B 1ra. dosis población vulnerable (VIH); Hepatitis B 1ra. dosis trabajadores de Salud; Hepatitis B 2da. dosis población vulnerable (VIH); Hepatitis B 2da. dosis trabajadores de Salud; Hepatitis B 3ra. dosis población vulnerable (VIH); Hepatitis B 3ra. dosis trabajadores de Salud | 4.0.0 (2018) |
| 2018 | 301a | Hepatitis B 1ra. dosis población vulnerable (VIH); Hepatitis B 1ra. dosis trabajadores de Salud; Hepatitis B 2da. dosis población vulnerable (VIH); Hepatitis B 2da. dosis trabajadores de Salud; Hepatitis B 3ra. dosis población vulnerable (VIH); Hepatitis B 3ra. dosis trabajadores de Salud | 4.0.1 (2018) |
| 2019-2020 | 301a | Hepatitis B 1ra. dosis población vulnerable (VIH); Hepatitis B 1ra. dosis trabajadores de Salud; Hepatitis B 2da. dosis población vulnerable (VIH); Hepatitis B 2da. dosis trabajadores de Salud; Hepatitis B 3ra. dosis población vulnerable (VIH); Hepatitis B 3ra. dosis trabajadores de Salud | 5.0.1 (2020) |
