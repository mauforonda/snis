# Interrupciones legales del embarazo (2024-2025)

Atenciones y nacimientos registrados en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2024-2025. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2024-2025 |
| Periodicidad | mensual |
| Municipios con registros | 51 |
| Desagregación | causal, trimestre, edad |
| Filas | 1.011 |

Valores de `causal` (causal):

- malformación congénita incompatible con la vida (2024-2025)
- riesgo para la salud de la madre (2024-2025)
- violencia sexual (2024-2025)

Valores de `trimestre` (trimestre):

- 1.º (2024-2025)
- 2.º (2024-2025)
- 3.º (2024-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2024-2025 | <10, 10-14, 15-19, 20-34, 35-49, 50+ |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2024 | 2.348 |
| 2025 | 1.717 |

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
| `trimestre` | string | Trimestre del embarazo. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/interrupcion_legal_embarazo_2024_2025/datos.parquet'
group by gestion order by gestion;

-- Por gestión y causal
select gestion, causal, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/interrupcion_legal_embarazo_2024_2025/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/salud_materna_neonatal/interrupcion_legal_embarazo_2024_2025/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Interrupciones legales del embarazo (2021-2023)](../../../servicios/salud_materna_neonatal/interrupcion_legal_embarazo_2021_2023/readme.md): 2021-2023, formulario 301a.
- Interrupciones legales del embarazo (2024-2025) (este dataset): 2024-2025, formulario 301a.

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
| 2024-2025 | 301a | ILE en el 1er trimestre de embarazo causal Malformacion Congenita incompatible con la vida; ILE en el 1er trimestre del embarazo por causal Riesgo de Salud de la madre; ILE en el 1er trimestre del embarazo por causal Violencia Sexual; ILE en el 2do trimestre de embarazo causal Malformacion Congenita incompatible con la vida; ILE en el 2do trimestre del embarazo por causal Riesgo de Salud de la madre; ILE en el 2do trimestre del embarazo por causal Violencia Sexual; ILE en el 3er trimestre de embarazo causal Malformacion Congenita incompatible con la vida; ILE en el 3er trimestre del embarazo por causal Riesgo de Salud de la madre; ILE en el 3er trimestre del embarazo por causal Violencia Sexual | 7.0.1 (2026) |
