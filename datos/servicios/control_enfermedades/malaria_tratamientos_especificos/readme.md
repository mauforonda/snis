# Malaria: tratamientos específicos entregados

Registros en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2025. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2025 |
| Periodicidad | mensual |
| Municipios con registros | 123 |
| Desagregación | sexo, edad, embarazo o puerperio, especie |
| Filas | 8.583 |

Valores de `especie` (especie):

- P. falciparum (2015-2025)
- P. vivax (2015-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015 | <1, 5+ |
| 2016-2025 | <1, 1-4, 5+ |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2015 | 8.580 |
| 2016 | 8.234 |
| 2017 | 5.387 |
| 2018 | 6.590 |
| 2019 | 9.948 |
| 2020 | 12.059 |
| 2021 | 9.965 |
| 2022 | 10.601 |
| 2023 | 10.693 |
| 2024 | 16.169 |
| 2025 | 10.378 |

### Advertencias

- El tablero no nombra estas variables: son columnas por edad del grupo "Malaria" del 301a. Según el instructivo del 301a (2024), cuentan los tratamientos específicos entregados a pacientes confirmados.

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
| `sexo` | string | mujer u hombre. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `condicion` | string | embarazada o puerpera. |
| `especie` | string | Especie de Plasmodium. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/malaria_tratamientos_especificos/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/malaria_tratamientos_especificos/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/malaria_tratamientos_especificos/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Malaria: tratamientos específicos dispensados](../../../servicios/control_enfermedades/malaria_tratamientos_especificos_dispensados/readme.md): 2010-2014, formulario 301.
- Malaria: tratamientos específicos entregados (este dataset): 2015-2025, formulario 301a.

Hasta 2014 el formulario 301 cuenta los tratamientos específicos de malaria dispensados; desde 2015 el 301a cuenta, por edad, los tratamientos específicos entregados a pacientes confirmados. Consultarlos juntos como una serie supone que las dos variables cuentan lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/control_enfermedades/malaria_tratamientos_especificos_dispensados/datos.parquet',
    'datos/servicios/control_enfermedades/malaria_tratamientos_especificos/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015 | 301a | Total De 1 a menores de 5 años; Total De 5 años y más; Total Menores de 1 año; Total Mujer embarazada | 3.0.1 (2016) |
| 2016 | 301a | De 1 a menores de 5 años; De 5 años y más; Menores de 1 año; Mujer embarazada | 3.0.2 (2016) |
| 2017 | 301a | De 1 a menores de 5 años; De 5 años y más; Menores de 1 año; Mujer embarazada | 4.0.0 (2018) |
| 2018 | 301a | De 1 a menores de 5 años; De 5 años y más; Menores de 1 año; Mujer embarazada | 4.0.1 (2018) |
| 2019-2020 | 301a | De 1 a menores de 5 años; De 5 años y más; Menores de 1 año; Mujer embarazada | 5.0.1 (2020) |
| 2021 | 301a | De 1 a menores de 5 años; De 5 años y más; Menores de 1 año; Mujer embarazada | 6.0.0 (2021) |
| 2022-2023 | 301a | De 1 a menores de 5 años; De 5 años y más; Menores de 1 año; Mujer embarazada | 6.0.1 (2022) |
| 2024-2025 | 301a | De 1 a menores de 5 años; De 5 años y más; Menores de 1 año; Mujer embarazada | 7.0.1 (2026) |
