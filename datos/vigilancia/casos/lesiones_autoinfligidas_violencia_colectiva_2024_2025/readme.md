# Lesiones autoinfligidas y violencia colectiva (2024-2025)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2024-2025. Fuente: SNIS, formularios 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2024-2025 |
| Periodicidad | semanal |
| Municipios con registros | 230 |
| Desagregación | tipo, sexo, edad |
| Filas | 7.794 |

Valores de `tipo` (tipo):

- lesiones autoinfligidas (2024-2025)
- violencia colectiva (2024-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2024-2025 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2024 | 5.905 |
| 2025 | 5.257 |

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
| `tipo` | string | Tipo. |
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/lesiones_autoinfligidas_violencia_colectiva_2024_2025/datos.parquet'
group by gestion order by gestion;

-- Por gestión y tipo
select gestion, tipo, sum(casos) as casos
from 'datos/vigilancia/casos/lesiones_autoinfligidas_violencia_colectiva_2024_2025/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/lesiones_autoinfligidas_violencia_colectiva_2024_2025/datos.parquet'
where gestion = 2025 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Lesiones autoinfligidas y violencia colectiva (2015-2023)](../../../vigilancia/casos/lesiones_autoinfligidas_violencia_colectiva_2015_2023/readme.md): 2015-2023, formulario 302a.
- Lesiones autoinfligidas y violencia colectiva (2024-2025) (este dataset): 2024-2025, formulario 302a.

Las categorías de `tipo` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/lesiones_autoinfligidas_violencia_colectiva_2015_2023/datos.parquet',
    'datos/vigilancia/casos/lesiones_autoinfligidas_violencia_colectiva_2024_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2024 | 302a | 8. Otras violencias por lesiones autoinflingidas; 9. Otras violencias por lesiones colectivas | 7.0.1 (2026) | X60 X61 X62 X63 X64 X65 X66 X67 X68 X69 X70 X71 X72 X73 X74 X75 X76 X77 X78 X79 X80 X81 X82 X83 X84 X85 X86 X87 X88 X89 X90 X91 X92 X93 X94 X95 X96 X97 X98 X99 Y00 Y01 Y02 Y03 Y07 Y08 Y09 |
| 2025 | 302a | 08. Otras violencias por lesiones autoinflingidas; 09. Otras violencias por lesiones colectivas | 7.0.1 (2026) | X60 X61 X62 X63 X64 X65 X66 X67 X68 X69 X70 X71 X72 X73 X74 X75 X76 X77 X78 X79 X80 X81 X82 X83 X84 X85 X86 X87 X88 X89 X90 X91 X92 X93 X94 X95 X96 X97 X98 X99 Y00 Y01 Y02 Y03 Y07 Y08 Y09 |
