# Mujeres con exámen clínico de mama positivos (sospechoso de nódulo neoplásico)

Atenciones registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2025. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2025 |
| Periodicidad | mensual |
| Municipios con registros | 308 |
| Desagregación | edad |
| Filas | 10.752 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015-2023 | <15, 15-19, 20-34, 35-49, 50+ |
| 2024 | <10, 10-14, 15-19, 20-34, 35-49, 50+ |
| 2025 | 10-14, 15-19, 20-34, 35-49, 50+ |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2015 | 5.444 |
| 2016 | 6.668 |
| 2017 | 10.041 |
| 2018 | 16.330 |
| 2019 | 7.503 |
| 2020 | 5.651 |
| 2021 | 6.266 |
| 2022 | 7.669 |
| 2023 | 5.823 |
| 2024 | 5.157 |
| 2025 | 4.559 |

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
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/anticoncepcion_prevencion_cancer/mujeres_con_examen_clinico_de_mama_positivos_sospechoso_de_n/datos.parquet'
group by gestion order by gestion;

-- Por gestión y edad_grupo
select gestion, edad_grupo, sum(cantidad) as cantidad
from 'datos/servicios/anticoncepcion_prevencion_cancer/mujeres_con_examen_clinico_de_mama_positivos_sospechoso_de_n/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/anticoncepcion_prevencion_cancer/mujeres_con_examen_clinico_de_mama_positivos_sospechoso_de_n/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015-2016 | 301a | Número de mujeres con exámen clínico de mama positivos (sospechoso de nódulo neoplásico) |  |
| 2017 | 301a | Número de mujeres con exámen clínico de mama positivos (sospechoso de nódulo neoplásico) | 4.0.0 (2018) |
| 2018 | 301a | Número de mujeres con exámen clínico de mama positivos (sospechoso de nódulo neoplásico) | 4.0.1 (2018) |
| 2019-2020 | 301a | Número de mujeres con exámen clínico de mama positivos (sospechoso de nódulo neoplásico) | 5.0.1 (2020) |
| 2021 | 301a | Número de mujeres con exámen clínico de mama positivos (sospechoso de nódulo neoplásico) | 6.0.0 (2021) |
| 2022-2023 | 301a | Número de mujeres con exámen clínico de mama positivos (sospechoso de nódulo neoplásico) | 6.0.1 (2022) |
| 2024-2025 | 301a | Número de mujeres con exámen clínico de mama positivos (sospechoso de nódulo neoplásico) | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 301a, anticoncepción y prevención del cáncer (2015-2016) e interrupción legal del embarazo (2021): las variables tienen cinco columnas sin rótulo ("Número de condones entregados", "...1" a "...4"). Son las bandas de edad <15, 15-19, 20-34, 35-49 y 50+, en ese orden. En anticoncepción las proporciones coinciden con las de 2017 (muestras de PAP 2016: 0,3 %, 7,1 %, 48,5 %, 32,0 % y 12,2 %; 2017: 0,3 %, 7,1 %, 48,4 %, 31,7 % y 12,5 %). En la interrupción legal del embarazo, el encabezado de 2022 une cada columna numerada con su banda ("A. < 15", "B. 15 A 19 ... 1"). En 2022 la segunda banda de las causales riesgo de salud de la madre y malformación dice "15 A 49"; es 15-19.
