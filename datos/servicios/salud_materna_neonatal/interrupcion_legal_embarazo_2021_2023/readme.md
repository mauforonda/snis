# Interrupciones legales del embarazo (2021-2023)

Atenciones y nacimientos registrados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2021-2023. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2021-2023 |
| Periodicidad | mensual |
| Municipios con registros | 58 |
| Desagregación | causal, edad |
| Filas | 666 |

Valores de `causal` (causal):

- malformación congénita incompatible con la vida (2021-2023)
- riesgo para la salud de la madre (2021-2023)
- violencia sexual (2021-2023)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2021-2023 | <15, 15-19, 20-34, 35-49 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2021 | 759 |
| 2022 | 920 |
| 2023 | 1.117 |

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
| `causal` | string | Causal legal. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/interrupcion_legal_embarazo_2021_2023/datos.parquet'
group by gestion order by gestion;

-- Por gestión y causal
select gestion, causal, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/interrupcion_legal_embarazo_2021_2023/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/interrupcion_legal_embarazo_2021_2023/datos.parquet'
where gestion = 2023 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Interrupciones legales del embarazo (2021-2023) (este dataset): 2021-2023, formulario 301a.
- [Interrupciones legales del embarazo (2024-2025)](../../../servicios/salud_materna_neonatal/interrupcion_legal_embarazo_2024_2025/readme.md): 2024-2025, formulario 301a.

Las categorías de `causal` y `trimestre` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/salud_materna_neonatal/interrupcion_legal_embarazo_2021_2023/datos.parquet',
    'datos/servicios/salud_materna_neonatal/interrupcion_legal_embarazo_2024_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2021-2023 | 301a | Interrupciones Legales del Embarazo por Malformación Congenita incompatible con la vida; Interrupciones Legales del Embarazo por Riesgo de Salud de la Madre; N° de Interrupciones Legales del Embarazo por Violencia Sexual |  |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 301a, anticoncepción y prevención del cáncer (2015-2016) e interrupción legal del embarazo (2021): las variables tienen cinco columnas sin rótulo ("Número de condones entregados", "...1" a "...4"). Son las bandas de edad <15, 15-19, 20-34, 35-49 y 50+, en ese orden. En anticoncepción las proporciones coinciden con las de 2017 (muestras de PAP 2016: 0,3 %, 7,1 %, 48,5 %, 32,0 % y 12,2 %; 2017: 0,3 %, 7,1 %, 48,4 %, 31,7 % y 12,5 %). En la interrupción legal del embarazo, el encabezado de 2022 une cada columna numerada con su banda ("A. < 15", "B. 15 A 19 ... 1"). En 2022 la segunda banda de las causales riesgo de salud de la madre y malformación dice "15 A 49"; es 15-19.
