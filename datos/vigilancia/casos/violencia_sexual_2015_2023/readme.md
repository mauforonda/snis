# Violencia sexual (familiar y en otros ámbitos) (2015-2023)

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2015-2023. Fuente: SNIS, formularios 302a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2023 |
| Periodicidad | semanal |
| Municipios con registros | 285 |
| Desagregación | sexo, edad |
| Filas | 10.229 |

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015-2022 | <6m, 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |
| 2023 | 6-11m, 1-4, 5-9, 10-14, 15-19, 20-39, 40-49, 50-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2015 | 2.587 |
| 2016 | 2.226 |
| 2017 | 1.809 |
| 2018 | 1.525 |
| 2019 | 1.566 |
| 2020 | 994 |
| 2021 | 1.112 |
| 2022 | 1.346 |
| 2023 | 1.573 |

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
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/violencia_sexual_2015_2023/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(casos) as casos
from 'datos/vigilancia/casos/violencia_sexual_2015_2023/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/violencia_sexual_2015_2023/datos.parquet'
where gestion = 2023 group by all order by casos desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Violencia sexual (familiar y en otros ámbitos) (2015-2023) (este dataset): 2015-2023, formulario 302a.
- [Violencia sexual (2024-2025)](../../../vigilancia/casos/violencia_sexual_2024_2025/readme.md): 2024-2025, formulario 302a.

Las categorías de `ambito` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(casos) as casos
from read_parquet([
    'datos/vigilancia/casos/violencia_sexual_2015_2023/datos.parquet',
    'datos/vigilancia/casos/violencia_sexual_2024_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

- [Violencia intrafamiliar](../../../vigilancia/casos/violencia_intrafamiliar/readme.md): 2001-2023, formulario 302, 302a.
- Violencia sexual (familiar y en otros ámbitos) (2015-2023) (este dataset): 2015-2023, formulario 302a.
- [Violencia física](../../../vigilancia/casos/violencia_fisica/readme.md): 2024-2025, formulario 302a.
- [Violencia por negligencia o abandono](../../../vigilancia/casos/violencia_negligencia/readme.md): 2024-2025, formulario 302a.
- [Violencia sexual (2024-2025)](../../../vigilancia/casos/violencia_sexual_2024_2025/readme.md): 2024-2025, formulario 302a.

Hasta 2023 el formulario notifica la violencia intrafamiliar; desde 2024 separa la violencia física y la sexual, familiar y en otros contextos (columna `ambito`), y la negligencia o abandono. No sabemos qué partes de 2024 equivalen a la violencia intrafamiliar.

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador. Los códigos CIE-10 son las categorías de 3 caracteres de los diagnósticos que esas reglas cuentan; los códigos completos están en `datapackage.json` (`snis.procedencia`).

| Gestiones | Formulario | Variable del tablero | SOAPS | CIE-10 |
| --- | --- | --- | --- | --- |
| 2015 | 302a | Violencia Sexual (familiar, doméstica y/o en otros ámbitos) | 3.0.1 (2016) | Y05 |
| 2016 | 302a | Violencia Sexual (familiar, doméstica y/o en otros ámbitos) | 3.0.2 (2016) | Y05 |
| 2017 | 302a | Violencia Sexual (familiar, doméstica y/o en otros ámbitos) | 4.0.0 (2018) | Y05 |
| 2018 | 302a | Violencia Sexual (familiar, doméstica y/o en otros ámbitos) | 4.0.1 (2018) | Y05 |
| 2019-2020 | 302a | Violencia Sexual (familiar, doméstica y/o en otros ámbitos) | 5.0.1 (2020) | Y05 |
| 2021 | 302a | Violencia Sexual (familiar, doméstica y/o en otros ámbitos) | 6.0.0 (2021) | Y05 |
| 2022-2023 | 302a | Violencia Sexual (familiar, doméstica y/o en otros ámbitos) | 6.0.1 (2022) | Y05 |
