# Violencia física

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2024-2025. Fuente: SNIS, formularios 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2024-2025 |
| Periodicidad | semanal |
| Municipios con registros | 215 |
| Desagregación | ámbito, sexo, edad |
| Filas | 7.224 |

Valores de `ambito` (ámbito):

- familiar (2024-2025)
- otros contextos (2024-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2024-2025 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2024 | 4.600 |
| 2025 | 5.512 |

## Cómo utilizar

Cada fila da el número de casos de un periodo, un municipio y una población. Para obtener un total, sume las filas: el dataset no tiene filas de total. Una combinación sin fila significa que no hubo registros. Las convenciones de tiempo, territorio y población están en el [catálogo](../../../README.md#cómo-leer-los-datos).

| Columna | Tipo | Descripción |
| --- | --- | --- |
| `gestion` | integer | Año calendario (gestión) del registro. |
| `semana` | integer | Semana epidemiológica, de 1 a 53. Va de domingo a sábado. |
| `fecha_inicio` | date | Primer día de la semana o del mes. |
| `departamento` | string | Nombre del departamento. |
| `municipio` | string | Nombre del municipio. |
| `municipio_codigo` | string | Código del municipio, 6 dígitos: departamento (2), provincia (2) y municipio (2). |
| `ambito` | string | Ámbito de la violencia. |
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/violencia_fisica/datos.parquet'
group by gestion order by gestion;

-- Por gestión y ambito
select gestion, ambito, sum(casos) as casos
from 'datos/vigilancia/casos/violencia_fisica/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/violencia_fisica/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Violencia intrafamiliar](../../../vigilancia/casos/violencia_intrafamiliar/readme.md): 2001-2023, formulario 302, 302a.
- [Violencia sexual (familiar y en otros ámbitos) (2015-2023)](../../../vigilancia/casos/violencia_sexual_2015_2023/readme.md): 2015-2023, formulario 302a.
- Violencia física (este dataset): 2024-2025, formulario 302a.
- [Violencia por negligencia o abandono](../../../vigilancia/casos/violencia_negligencia/readme.md): 2024-2025, formulario 302a.
- [Violencia sexual (2024-2025)](../../../vigilancia/casos/violencia_sexual_2024_2025/readme.md): 2024-2025, formulario 302a.

Hasta 2023 el formulario notifica la violencia intrafamiliar; desde 2024 separa la violencia física y la sexual, familiar y en otros contextos (columna `ambito`), y la negligencia o abandono. No sabemos qué partes de 2024 equivalen a la violencia intrafamiliar.

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2024 | 302a | 1. Violencia Fisica Familiar; 2. Violencia Fisica en otros contextos | 7.0.1 (2026) | R45 T74 Y04 Y07 Z61 |
| 2025 | 302a | 01. Violencia Fisica Familiar; 02. Violencia Fisica en otros contextos | 7.0.1 (2026) | R45 T74 Y04 Y07 Z61 |
