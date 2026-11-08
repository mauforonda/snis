# Vacuna Influenza estacional (2015-2023)

Dosis aplicadas en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2015-2023. Fuente: SNIS, formularios 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2015-2023 |
| Periodicidad | mensual |
| Municipios con registros | 342 |
| Desagregación | dosis, grupo de población, sexo, edad, lugar |
| Filas | 340.802 |

Valores de `dosis` (dosis):

- 1 (2015-2023)
- 2 (2015-2023)
- única (2015-2023)

Valores de `grupo` (grupo de población):

- embarazadas (2015-2023)
- personal de salud (2015-2023)
- personas con enfermedad crónica (2015-2023)
- personas de 60 años y más (2015-2023)

Valores de `lugar` (lugar):

- dentro (2015-2023)
- fuera (2015-2023)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2015-2022 | 6-11m, 7-11m, 1 |
| 2023 | 6-11m, 7-11m, 1, 2-3 |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2015 | 724.974 |
| 2016 | 1.085.928 |
| 2017 | 1.262.676 |
| 2018 | 1.462.177 |
| 2019 | 1.400.135 |
| 2020 | 1.441.366 |
| 2021 | 1.179.688 |
| 2022 | 1.420.478 |
| 2023 | 1.229.829 |

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
from 'datos/servicios/vacunas/influenza_estacional_2015_2023/datos.parquet'
group by gestion order by gestion;

-- Por gestión y dosis
select gestion, dosis, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/influenza_estacional_2015_2023/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/vacunas/influenza_estacional_2015_2023/datos.parquet'
where gestion = 2023 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- Vacuna Influenza estacional (2015-2023) (este dataset): 2015-2023, formulario 301a.
- [Vacuna Influenza estacional (2024-2025)](../../../servicios/vacunas/influenza_estacional_2024_2025/readme.md): 2024-2025, formulario 301a.

Las categorías de `dosis` y `grupo` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/vacunas/influenza_estacional_2015_2023/datos.parquet',
    'datos/servicios/vacunas/influenza_estacional_2024_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2015 | 301a | Total Influenza estacional (6m a 11 m) 1ra. Dosis; Total Influenza estacional (7m a 11 m) 2da. Dosis; Total Influenza estacional a mujeres embarazadas; Total Influenza estacional a personal de salud; Total Influenza estacional a personas con enfermedades crónicas; Total Influenza estacional dosis única; Total Influenza estacional en mayores de 65 años | 3.0.1 (2016) |
| 2016 | 301a | Influenza estacional (6m a 11 m) 1ra. Dosis; Influenza estacional (7m a 11 m) 2da. Dosis; Influenza estacional a mujeres embarazadas; Influenza estacional a personal de salud; Influenza estacional a personas con enfermedades crónicas; Influenza estacional dosis única; Influenza estacional en mayores de 65 años | 3.0.2 (2016) |
| 2017 | 301a | Influenza estacional (6m a 11 m) 1ra. Dosis; Influenza estacional (7m a 11 m) 2da. Dosis; Influenza estacional a mujeres embarazadas; Influenza estacional a personal de salud; Influenza estacional a personas con enfermedades crónicas; Influenza estacional dosis única; Influenza estacional en mayores de 65 años | 4.0.0 (2018) |
| 2018 | 301a | Influenza estacional (6m a 11 m) 1ra. Dosis; Influenza estacional (7m a 11 m) 2da. Dosis; Influenza estacional a mujeres embarazadas; Influenza estacional a personal de salud; Influenza estacional a personas con enfermedades crónicas; Influenza estacional dosis única; Influenza estacional en mayores de 60 años | 4.0.1 (2018) |
| 2019-2020 | 301a | Influenza estacional (6m a 11 m) 1ra. Dosis; Influenza estacional (7m a 11 m) 2da. Dosis; Influenza estacional a mujeres embarazadas; Influenza estacional a personal de salud; Influenza estacional a personas con enfermedades crónicas; Influenza estacional dosis única; Influenza estacional en mayores de 60 años | 5.0.1 (2020) |
| 2021 | 301a | Influenza estacional (6m a 11 m) 1ra. Dosis; Influenza estacional (7m a 11 m) 2da. Dosis; Influenza estacional a mujeres embarazadas; Influenza estacional a personal de salud; Influenza estacional a personas con enfermedades crónicas; Influenza estacional dosis única; Influenza estacional en mayores de 60 años | 6.0.0 (2021) |
| 2022-2023 | 301a | Influenza estacional (6m a 11 m) 1ra. Dosis; Influenza estacional (7m a 11 m) 2da. Dosis; Influenza estacional a mujeres embarazadas; Influenza estacional a personal de salud; Influenza estacional a personas con enfermedades crónicas; Influenza estacional dosis única; Influenza estacional en mayores de 60 años | 6.0.1 (2022) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
