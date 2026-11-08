# Vacuna Hepatitis B (2021-2025)

Dosis aplicadas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2021-2025. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2021-2025 |
| Periodicidad | mensual |
| Municipios con registros | 342 |
| Desagregación | dosis, grupo de población, sexo, edad, lugar |
| Filas | 49.990 |

Valores de `dosis` (dosis):

- 1 (2021-2025)
- 2 (2021-2025)
- 3 (2021-2025)

Valores de `grupo` (grupo de población):

- personal de salud (2021-2025)
- personas con VIH (2021-2025)
- personas con enfermedad renal (2021-2025)

Valores de `lugar` (lugar):

- dentro (2021-2025)
- fuera (2021-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2024-2025 | 12-20, 21-59, 60+ |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2021 | 38.603 |
| 2022 | 73.522 |
| 2023 | 69.453 |
| 2024 | 74.297 |
| 2025 | 73.696 |

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
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/hepatitis_b_2021_2025/datos.parquet'
group by gestion order by gestion;

-- Por gestión y dosis
select gestion, dosis, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/hepatitis_b_2021_2025/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/hepatitis_b_2021_2025/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Vacuna Hepatitis B (2010-2014)](../../../servicios/vacunas/hepatitis_b_2010_2014/readme.md): 2010-2014, formulario 301.
- [Vacuna Hepatitis B (2015-2020)](../../../servicios/vacunas/hepatitis_b_2015_2020/readme.md): 2015-2020, formulario 301a.
- Vacuna Hepatitis B (2021-2025) (este dataset): 2021-2025, formulario 301a.

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
| 2021 | 301a | 17.18 Hepatitis B 1ra. dosis población vulnerable enf. Renales; 17.19 Hepatitis B 2da. dosis población vulnerable enf renales; 17.20 Hepatitis B 3ra. dosis población vulnerable enf renales; Hepatitis B 1ra. dosis población vulnerable (VIH); Hepatitis B 1ra. dosis trabajadores de Salud; Hepatitis B 2da. dosis población vulnerable (VIH); Hepatitis B 2da. dosis trabajadores de Salud; Hepatitis B 3ra. dosis población vulnerable (VIH); Hepatitis B 3ra. dosis trabajadores de Salud | 6.0.0 (2021) |
| 2022-2023 | 301a | 17.18 Hepatitis B 1ra. dosis población vulnerable enf. Renales; 17.19 Hepatitis B 2da. dosis población vulnerable enf renales; 17.20 Hepatitis B 3ra. dosis población vulnerable enf renales; Hepatitis B 1ra. dosis población vulnerable (VIH); Hepatitis B 1ra. dosis trabajadores de Salud; Hepatitis B 2da. dosis población vulnerable (VIH); Hepatitis B 2da. dosis trabajadores de Salud; Hepatitis B 3ra. dosis población vulnerable (VIH); Hepatitis B 3ra. dosis trabajadores de Salud | 6.0.1 (2022) |
| 2024-2025 | 301a | Hepatitis B 1ra Dosis Poblacion vulnerable VIH; Hepatitis B 1ra Dosis Poblacion vulnerable renales; Hepatitis B 1ra Dosis trabajadores de Salud; Hepatitis B 2da Dosis Poblacion vulnerable VIH; Hepatitis B 2da Dosis Poblacion vulnerable renales; Hepatitis B 2da Dosis trabajadores de Salud; Hepatitis B 3ra Dosis Poblacion vulnerable VIH; Hepatitis B 3ra Dosis Poblacion vulnerable renales; Hepatitis B 3ra Dosis trabajadores de Salud | 7.0.1 (2026) |
