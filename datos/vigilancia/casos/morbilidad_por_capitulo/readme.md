# Morbilidad por capítulo de la CIE-10

Personas atendidas con este diagnóstico en los establecimientos de salud de Bolivia, por semana y municipio, en las gestiones 2001-2003. Fuente: SNIS, formularios 302.

## Qué es

| | |
| --- | --- |
| Gestiones | 2001-2003 |
| Periodicidad | semanal |
| Municipios con registros | 312 |
| Desagregación | capítulo, edad |
| Filas | 802.929 |

Valores de `capitulo` (capítulo):

- Embarazo, parto y puerperio (2001-2003)
- Endocrinas, nutricionales y metabólicas (2001-2003)
- Malformaciones congénitas (2001-2003)
- Ojo y anexos (2001-2003)
- Otras causas (2001-2003)
- Oído y apófisis mastoides (2001-2003)
- Piel y tejido subcutáneo (2001-2003)
- Sangre y trastornos inmunitarios (2001-2003)
- Sistema circulatorio (2001-2003)
- Sistema digestivo (2001-2003)
- Sistema genitourinario (2001-2003)
- Sistema nervioso (2001-2003)
- Sistema osteomuscular (2001-2003)
- Sistema respiratorio (2001-2003)
- Trastornos mentales (2001-2003)
- Traumatismos y envenenamientos (2001-2003)
- Tumores (2001-2003)

Bandas de edad (`edad_grupo`) por gestión:

| Gestiones | Bandas |
| --- | --- |
| 2001-2003 | <1, 1-4, 5-14, 15-59, 60+ |

Total por gestión:

| Gestión | Casos |
| ---: | ---: |
| 2001 | 4.880.187 |
| 2002 | 3.289.997 |
| 2003 | 1.705.113 |

### Advertencias

- Clasificación general por sistema del formulario 2001-2003; puede incluir casos que también se notifican como enfermedades específicas.

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
| `capitulo` | string | Capítulo de la CIE-10. |
| `edad_desde` | number | Edad mínima de la banda, en años (6 meses = 0,5). |
| `edad_hasta` | number | Edad máxima de la banda, en años, sin incluir. Vacía si la banda no tiene límite. |
| `edad_grupo` | string | Banda de edad en texto corto: "<6m" (menos de 6 meses), "1-4", "60+". |
| `casos` | integer | Número de casos en la fila. |

Consultas con [duckdb](https://duckdb.org), desde la raíz del repositorio:

```sql
-- Total por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/morbilidad_por_capitulo/datos.parquet'
group by gestion order by gestion;

-- Por gestión y capitulo
select gestion, capitulo, sum(casos) as casos
from 'datos/vigilancia/casos/morbilidad_por_capitulo/datos.parquet'
group by all order by all;

-- Por departamento en la última gestión
select departamento, sum(casos) as casos
from 'datos/vigilancia/casos/morbilidad_por_capitulo/datos.parquet'
where gestion = 2003 group by all order by casos desc;
```

## De dónde viene

Los datos vienen de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes. Fueron descargados en [`descarga/`](../../../../descarga/) y procesados con el código de [`construccion/`](../../../../construccion/). La versión de SOAPS es la del software del SNIS cuyas reglas describen la variable, con el año de su instalador.

| Gestiones | Formulario | Variable del tablero | SOAPS |
| --- | --- | --- | --- |
| 2001-2003 | 302 | 1.- Enfermedades del Sistema Nervioso; 10.- Enfermedades sistema osteomuscular y tejido conjuntivo; 11.- Enfermedades de la sangre y transtornos inmunitarios; 12.- Enfermedades tumorales; 13.- Complicaciones embarazo, parto y púerperio; 14.- Malformaciones congénitas; 15.- Traumatismos y envenenamiento; 16.- Transtornos mentales y del comportamiento; 17.- Otras causas; 2.- Enfermedades del ojo y anexos; 3.- Enfermedades del oido y apofisis mastoides; 4.- Enfermedades del sistema cardio circulatorio; 5.- Enfermedades del sistema respiratorio; 6.- Enfermedades del sistema digestivo; 7.- Enfermedades del sistema genitourinario; 8.- Enfermedades de piel y celular subcutánea; 9.- Enfermedades endocrinas - nutricionales - metabolicas |  |

Correcciones de rótulos aplicadas (el encabezado del tablero no describía sus columnas):

- 302, 2001-2007: en las variables cuyas columnas "-M" siempre valen 0, "TOTAL-H" es igual a "TOTAL": "-H" contiene a ambos sexos. Esas variables no tienen sexo. En 2004 el grupo 09 (mortalidad) tampoco tiene sexo: hay 79 muertes maternas en "-H" y 94 en "-M".
