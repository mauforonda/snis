# Partos atendidos por proveedor calificado

Atenciones y nacimientos registrados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2025. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2025 |
| Periodicidad | mensual |
| Municipios con registros | 341 |
| Desagregación | edad, lugar |
| Filas | 53.411 |

Valores de `lugar` (lugar):

- domicilio (2015-2025)
- servicio (2015-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2024-2025 | <10, 10-14, 15-19, 20-34, 35-49, 50+ |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2015 | 126.541 |
| 2016 | 144.734 |
| 2017 | 157.314 |
| 2018 | 172.763 |
| 2019 | 165.911 |
| 2020 | 149.272 |
| 2021 | 134.767 |
| 2022 | 139.877 |
| 2023 | 136.718 |
| 2024 | 117.549 |
| 2025 | 114.039 |

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
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `lugar` | string | Dónde ocurrió la atención o el evento: dentro o fuera del establecimiento; servicio o domicilio. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/partos_atendidos_por_proveedor_calificado/datos.parquet'
group by gestion order by gestion;

-- Por gestión y edad_grupo
select gestion, edad_grupo, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/partos_atendidos_por_proveedor_calificado/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/partos_atendidos_por_proveedor_calificado/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Partos atendidos por personal de salud](../../../servicios/salud_materna_neonatal/partos_atendidos_por_personal_de_salud/readme.md): 2001-2014, formulario 301.
- [Partos atendidos por personal de salud calificado](../../../servicios/salud_materna_neonatal/partos_atendidos_por_personal_de_salud_calificado/readme.md): 2015-2025, formulario 301a.
- Partos atendidos por proveedor calificado (este dataset): 2015-2025, formulario 301a.

Hasta 2014 el formulario 301 cuenta los partos atendidos por personal de salud; desde 2015 el 301a separa proveedor calificado (médicos) y personal de salud calificado (enfermería), según su instructivo. Consultarlos juntos como una serie supone que los dos grupos de 2015 suman lo mismo que "personal de salud".

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/salud_materna_neonatal/partos_atendidos_por_personal_de_salud/datos.parquet',
    'datos/servicios/salud_materna_neonatal/partos_atendidos_por_personal_de_salud_calificado/datos.parquet',
    'datos/servicios/salud_materna_neonatal/partos_atendidos_por_proveedor_calificado/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015 | 301a | Partos atendidos por proveedor calificado | 3.0.1 (2016) |
| 2016 | 301a | Partos atendidos por proveedor calificado | 3.0.2 (2016) |
| 2017 | 301a | Partos atendidos por proveedor calificado | 4.0.0 (2018) |
| 2018 | 301a | Partos atendidos por proveedor calificado | 4.0.1 (2018) |
| 2019-2020 | 301a | Partos atendidos por proveedor calificado | 5.0.1 (2020) |
| 2021 | 301a | Partos atendidos por proveedor calificado | 6.0.0 (2021) |
| 2022-2023 | 301a | Partos atendidos por proveedor calificado | 6.0.1 (2022) |
| 2024-2025 | 301a | Partos atendidos por proveedor calificado | 7.0.1 (2026) |
