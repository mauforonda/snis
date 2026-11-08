# Usuarias de anticoncepción (2015-2025)

Atenciones registradas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2025. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2025 |
| Periodicidad | mensual |
| Municipios con registros | 343 |
| Desagregación | método, usuaria nueva o continua, edad |
| Filas | 692.879 |

Valores de `metodo` (método):

- DIU (2015-2025)
- condón femenino (2015-2025)
- condón masculino (2015-2025)
- implante subdérmico (2015-2025)
- inyectable trimestral (2015-2025)
- métodos naturales (2015-2025)
- píldora (2015-2025)

Valores de `usuaria` (usuaria nueva o continua):

- continua (2015-2025)
- nueva (2015-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015-2023 | <15, 15-19, 20-34, 35-49, 50+ |
| 2024-2025 | <10, 10-14, 15-19, 20-34, 35-49, 50+ |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2015 | 678.387 |
| 2016 | 630.176 |
| 2017 | 643.574 |
| 2018 | 616.339 |
| 2019 | 553.354 |
| 2020 | 440.771 |
| 2021 | 485.583 |
| 2022 | 524.661 |
| 2023 | 562.462 |
| 2024 | 549.563 |
| 2025 | 537.509 |

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
| `metodo` | string | Método anticonceptivo. |
| `usuaria` | string | Usuaria nueva o continua. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/anticoncepcion_prevencion_cancer/usuarias_anticoncepcion_2015_2025/datos.parquet'
group by gestion order by gestion;

-- Por gestión y metodo
select gestion, metodo, sum(cantidad) as cantidad
from 'datos/servicios/anticoncepcion_prevencion_cancer/usuarias_anticoncepcion_2015_2025/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/anticoncepcion_prevencion_cancer/usuarias_anticoncepcion_2015_2025/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Usuarias de anticoncepción (2001-2014)](../../../servicios/anticoncepcion_prevencion_cancer/usuarias_anticoncepcion_2001_2014/readme.md): 2001-2014, formulario 301.
- Usuarias de anticoncepción (2015-2025) (este dataset): 2015-2025, formulario 301a.

Las categorías de `metodo` y `usuaria` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/anticoncepcion_prevencion_cancer/usuarias_anticoncepcion_2001_2014/datos.parquet',
    'datos/servicios/anticoncepcion_prevencion_cancer/usuarias_anticoncepcion_2015_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015-2016 | 301a | Condón Femenino: Usuarias Continuas; Condón Femenino: Usuarias Nuevas; Condón Masculino: Usuarias (os) Continuas (os); Condón Masculino: Usuarias (os) Nuevas (os); DIU: Usuarias Continuas; DIU: Usuarias Nuevas; Implante subdérmico: Usuarias Continuas; Implante subdérmico: Usuarias Nuevas; Inyectable Trimestral: Usuarias Continuas; Inyectable Trimestral: Usuarias Nuevas; Métodos naturales: Usuarias Continuas; Métodos naturales: Usuarias Nuevas; Píldora: Usuarias Continuas; Píldora: Usuarias Nuevas |  |
| 2017 | 301a | Condón Femenino: Usuarias Continuas; Condón Femenino: Usuarias Nuevas; Condón Masculino: Usuarias (os) Continuas (os); Condón Masculino: Usuarias (os) Nuevas (os); DIU: Usuarias Continuas; DIU: Usuarias Nuevas; Implante subdérmico: Usuarias Continuas; Implante subdérmico: Usuarias Nuevas; Inyectable Trimestral: Usuarias Continuas; Inyectable Trimestral: Usuarias Nuevas; Métodos naturales: Usuarias Continuas; Métodos naturales: Usuarias Nuevas; Píldora: Usuarias Continuas; Píldora: Usuarias Nuevas | 4.0.0 (2018) |
| 2018 | 301a | Condón Femenino: Usuarias Continuas; Condón Femenino: Usuarias Nuevas; Condón Masculino: Usuarias (os) Continuas (os); Condón Masculino: Usuarias (os) Nuevas (os); DIU: Usuarias Continuas; DIU: Usuarias Nuevas; Implante subdérmico: Usuarias Continuas; Implante subdérmico: Usuarias Nuevas; Inyectable Trimestral: Usuarias Continuas; Inyectable Trimestral: Usuarias Nuevas; Métodos naturales: Usuarias Continuas; Métodos naturales: Usuarias Nuevas; Píldora: Usuarias Continuas; Píldora: Usuarias Nuevas | 4.0.1 (2018) |
| 2019-2020 | 301a | Condón Femenino: Usuarias Continuas; Condón Femenino: Usuarias Nuevas; Condón Masculino: Usuarias (os) Continuas (os); Condón Masculino: Usuarias (os) Nuevas (os); DIU: Usuarias Continuas; DIU: Usuarias Nuevas; Implante subdérmico: Usuarias Continuas; Implante subdérmico: Usuarias Nuevas; Inyectable Trimestral: Usuarias Continuas; Inyectable Trimestral: Usuarias Nuevas; Métodos naturales: Usuarias Continuas; Métodos naturales: Usuarias Nuevas; Píldora: Usuarias Continuas; Píldora: Usuarias Nuevas | 5.0.1 (2020) |
| 2021 | 301a | Condón Femenino: Usuarias Continuas; Condón Femenino: Usuarias Nuevas; Condón Masculino: Usuarias (os) Continuas (os); Condón Masculino: Usuarias (os) Nuevas (os); DIU: Usuarias Continuas; DIU: Usuarias Nuevas; Implante subdérmico: Usuarias Continuas; Implante subdérmico: Usuarias Nuevas; Inyectable Trimestral: Usuarias Continuas; Inyectable Trimestral: Usuarias Nuevas; Métodos naturales: Usuarias Continuas; Métodos naturales: Usuarias Nuevas; Píldora: Usuarias Continuas; Píldora: Usuarias Nuevas | 6.0.0 (2021) |
| 2022-2023 | 301a | Condón Femenino: Usuarias Continuas; Condón Femenino: Usuarias Nuevas; Condón Masculino: Usuarias (os) Continuas (os); Condón Masculino: Usuarias (os) Nuevas (os); DIU: Usuarias Continuas; DIU: Usuarias Nuevas; Implante subdérmico: Usuarias Continuas; Implante subdérmico: Usuarias Nuevas; Inyectable Trimestral: Usuarias Continuas; Inyectable Trimestral: Usuarias Nuevas; Métodos naturales: Usuarias Continuas; Métodos naturales: Usuarias Nuevas; Píldora: Usuarias Continuas; Píldora: Usuarias Nuevas | 6.0.1 (2022) |
| 2024-2025 | 301a | Condón Femenino: Usuarias Continuas; Condón Femenino: Usuarias Nuevas; Condón Masculino: Usuarias (os) Continuas (os); Condón Masculino: Usuarias (os) Nuevas (os); DIU: Usuarias Continuas; DIU: Usuarias Nuevas; Implante subdérmico: Usuarias Continuas; Implante subdérmico: Usuarias Nuevas; Inyectable Trimestral: Usuarias Continuas; Inyectable Trimestral: Usuarias Nuevas; Métodos naturales: Usuarias Continuas; Métodos naturales: Usuarias Nuevas; Píldora: Usuarias Continuas; Píldora: Usuarias Nuevas | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 301a, anticoncepción y prevención del cáncer (2015-2016) e interrupción legal del embarazo (2021): las variables tienen cinco columnas sin rótulo ("Número de condones entregados", "...1" a "...4"). Son las bandas de edad <15, 15-19, 20-34, 35-49 y 50+, en ese orden. En anticoncepción las proporciones coinciden con las de 2017 (muestras de PAP 2016: 0,3 %, 7,1 %, 48,5 %, 32,0 % y 12,2 %; 2017: 0,3 %, 7,1 %, 48,4 %, 31,7 % y 12,5 %). En la interrupción legal del embarazo, el encabezado de 2022 une cada columna numerada con su banda ("A. < 15", "B. 15 A 19 ... 1"). En 2022 la segunda banda de las causales riesgo de salud de la madre y malformación dice "15 A 49"; es 15-19.
