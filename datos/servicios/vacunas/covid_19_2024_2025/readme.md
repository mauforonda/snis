# Vacuna COVID-19 (2024-2025)

Dosis aplicadas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2024-2025. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2024-2025 |
| Periodicidad | mensual |
| Municipios con registros | 340 |
| Desagregación | dosis, grupo de población, sexo, edad, lugar |
| Filas | 43.672 |

Valores de `dosis` (dosis):

- 1 (2024-2025)
- 2 (2024-2025)
- 3 (2024-2025)
- anual (2024-2025)
- única (2024-2025)

Valores de `grupo` (grupo de población):

- personas inmunodeprimidas (2024-2025)

Valores de `lugar` (lugar):

- dentro (2024-2025)
- fuera (2024-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2024-2025 | 5-9, 10, 11, 12-20, 21-59, 60+ |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2024 | 312.953 |
| 2025 | 267.529 |

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
from 'datos/servicios/vacunas/covid_19_2024_2025/datos.parquet'
group by gestion order by gestion;

-- Por gestión y dosis
select gestion, dosis, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/covid_19_2024_2025/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/covid_19_2024_2025/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Vacuna COVID-19 (2021)](../../../servicios/vacunas/covid_19_2021/readme.md): 2021, formulario 301a.
- [Vacuna COVID-19 (2022)](../../../servicios/vacunas/covid_19_2022/readme.md): 2022, formulario 301a.
- [Vacuna COVID-19 (2023)](../../../servicios/vacunas/covid_19_2023/readme.md): 2023, formulario 301a.
- Vacuna COVID-19 (2024-2025) (este dataset): 2024-2025, formulario 301a.

Las categorías de `dosis` y `grupo` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/vacunas/covid_19_2021/datos.parquet',
    'datos/servicios/vacunas/covid_19_2022/datos.parquet',
    'datos/servicios/vacunas/covid_19_2023/datos.parquet',
    'datos/servicios/vacunas/covid_19_2024_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2024-2025 | 301a | COVID-19 1ra Dosis (inmunodeprimidos); COVID-19 2da Dosis (inmunodeprimidos); COVID-19 3ra Dosis (inmunodeprimidos); COVID-19 Dosis Anual; COVID-19 Dosis Unica | 7.0.1 (2026) |
