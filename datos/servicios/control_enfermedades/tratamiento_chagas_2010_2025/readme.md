# Tratamientos de chagas (2010-2025)

Registros en los establecimientos de salud de Bolivia, por mes y municipio, en las gestiones 2010-2025. Fuente: SNIS, formularios 301, 301a.

## Qué es

| | |
| --- | --- |
| Gestiones | 2010-2025 |
| Periodicidad | mensual |
| Municipios con registros | 200 |
| Desagregación | sexo, edad, embarazo o puerperio, tratamiento iniciado o concluido |
| Filas | 21.266 |

Valores de `tratamiento` (tratamiento iniciado o concluido):

- concluido (2010-2013, 2015-2025)
- iniciado (2010-2013, 2015-2025)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2010-2025 | <1, 1-4, 5-14, 15+ |

Total por gestión:

| Gestión | Cantidad |
| ---: | ---: |
| 2010 | 9.663 |
| 2011 | 10.854 |
| 2012 | 5.567 |
| 2013 | 8.089 |
| 2014 | 8.741 |
| 2015 | 7.999 |
| 2016 | 10.337 |
| 2017 | 9.575 |
| 2018 | 5.332 |
| 2019 | 3.971 |
| 2020 | 2.423 |
| 2021 | 4.111 |
| 2022 | 5.281 |
| 2023 | 4.310 |
| 2024 | 4.268 |
| 2025 | 4.251 |

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
| `tratamiento` | string | Estado del tratamiento: iniciado o concluido. |
| `cantidad` | integer | Número de cantidad en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tratamiento_chagas_2010_2025/datos.parquet'
group by gestion order by gestion;

-- Por gestión y sexo
select gestion, sexo, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tratamiento_chagas_2010_2025/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(cantidad) as cantidad
from 'datos/servicios/control_enfermedades/tratamiento_chagas_2010_2025/datos.parquet'
where gestion = 2025 group by all order by cantidad desc;
```

## Datasets relacionados

Estos datasets cuentan algo parecido con otras categorías, otra definición, otro nombre u otro formulario. El repositorio no los une.

- [Tratamientos de chagas (2001-2006)](../../../servicios/control_enfermedades/tratamiento_chagas_2001_2006/readme.md): 2001-2006, formulario 301.
- [Tratamientos de chagas (2008-2009)](../../../servicios/control_enfermedades/tratamiento_chagas_2008_2009/readme.md): 2008-2009, formulario 301.
- Tratamientos de chagas (2010-2025) (este dataset): 2010-2025, formulario 301, 301a.

Las categorías de `tratamiento` cambian entre estos periodos; el readme de cada uno las lista. Consultarlos juntos como una serie supone que los conjuntos de categorías de cada periodo cuentan, en total, lo mismo.

Para consultarlos juntos, con ese supuesto:

```sql
select gestion, sum(cantidad) as cantidad
from read_parquet([
    'datos/servicios/control_enfermedades/tratamiento_chagas_2001_2006/datos.parquet',
    'datos/servicios/control_enfermedades/tratamiento_chagas_2008_2009/datos.parquet',
    'datos/servicios/control_enfermedades/tratamiento_chagas_2010_2025/datos.parquet'
], union_by_name = true)
group by gestion order by gestion;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2010-2011 | 301 | Tratamientos 1 año a menores de 5 años de edad; Tratamientos 5 años a menores de 15 años de edad; Tratamientos RN a menores de 1 año de edad; Tratamientos de 15 años y más; Tratamientos en mujeres post parto | 1.0.4 (2013) |
| 2012 | 301 | l 25.1 Tratamientos RN a menores de 1 año de edad; l 25.2 Tratamientos 1 año a menores de 5 años de edad; l 25.3 Tratamientos 5 años a menores de 15 años de edad; l 25.4 Tratamientos de 15 años y más; l 25.5 Tratamientos en mujeres post parto | 1.0.4 (2013) |
| 2013 | 301 | Tratamientos 1 año a menores de 5 años de edad; Tratamientos 5 años a menores de 15 años de edad; Tratamientos RN a menores de 1 año de edad; Tratamientos de 15 años y más; Tratamientos en mujeres post parto | 1.0.4 (2013) |
| 2014 | 301 | 25.1 Tratamientos RN a menores de 1 año de edad; 25.2 Tratamientos 1 año a menores de 5 años de edad; 25.3 Tratamientos 5 años a menores de 15 años de edad; 25.4 Tratamientos de 15 años y más; 25.5 Tratamientos en mujeres post parto | 2.0.0 (2014) |
| 2015 | 301a | Total Tratamientos 1 año a menores de 5 años de edad; Total Tratamientos 5 años a menores de 15 años de edad; Total Tratamientos RN a menores de 1 año de edad; Total Tratamientos de 15 años y más; Total Tratamientos en mujeres post parto | 3.0.1 (2016) |
| 2016 | 301a | Tratamientos 1 año a menores de 5 años de edad; Tratamientos 5 años a menores de 15 años de edad; Tratamientos RN a menores de 1 año de edad; Tratamientos de 15 años y más; Tratamientos en mujeres post parto | 3.0.2 (2016), 7.0.1 (2026) |
| 2017 | 301a | Tratamientos 1 año a menores de 5 años de edad; Tratamientos 5 años a menores de 15 años de edad; Tratamientos RN a menores de 1 año de edad; Tratamientos de 15 años y más; Tratamientos en mujeres post parto | 4.0.0 (2018), 7.0.1 (2026) |
| 2018 | 301a | Tratamientos 1 año a menores de 5 años de edad; Tratamientos 5 años a menores de 15 años de edad; Tratamientos RN a menores de 1 año de edad; Tratamientos de 15 años y más; Tratamientos en mujeres post parto | 4.0.1 (2018), 7.0.1 (2026) |
| 2019-2020 | 301a | Tratamientos 1 año a menores de 5 años de edad; Tratamientos 5 años a menores de 15 años de edad; Tratamientos RN a menores de 1 año de edad; Tratamientos de 15 años y más; Tratamientos en mujeres post parto | 5.0.1 (2020), 7.0.1 (2026) |
| 2021 | 301a | Tratamientos 1 año a menores de 5 años de edad; Tratamientos 5 años a menores de 15 años de edad; Tratamientos RN a menores de 1 año de edad; Tratamientos de 15 años y más; Tratamientos en mujeres post parto | 6.0.0 (2021), 7.0.1 (2026) |
| 2022-2023 | 301a | Tratamientos 1 año a menores de 5 años de edad; Tratamientos 5 años a menores de 15 años de edad; Tratamientos RN a menores de 1 año de edad; Tratamientos de 15 años y más; Tratamientos en mujeres post parto | 6.0.1 (2022), 7.0.1 (2026) |
| 2024-2025 | 301a | Tratamientos 1 año a menores de 5 años de edad; Tratamientos 5 años a menores de 15 años de edad; Tratamientos RN a menores de 1 año de edad; Tratamientos de 15 años y más; Tratamientos en mujeres post parto | 7.0.1 (2026) |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 301 y 301a, tratamientos de chagas, leishmaniasis y en mujeres posparto: el tablero repite las columnas de sexo ("FEMENINO" y "FEMENINO.1"). En 2020 los totales dicen "TOTAL Iniciado" y "TOTAL Concluido", y coinciden con la primera y la segunda columna: la primera es tratamiento iniciado y la repetida, concluido.
- Algunas variables no tienen columnas de detalle con valores, sólo el total: se publica el total, sin desagregación.
