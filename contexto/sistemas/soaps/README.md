
**Información de producción de servicios y de vigilancia epidemiológica embedida en los instaladores del Software de Atención Primaria en Salud (SOAPS) que extraemos y organizamos** para interpretar mejor las estadísticas en los formularios 301, 301a y 301b (producción de servicios) y 302, 302a y 302b (vigilancia epidemiológica). Usamos las 10 versiones de SOAPS publicadas por el SNIS entre 2013 y 2026, de la 1.0.4 a la 7.0.1. Con ellas describimos casi todas las variables de vigilancia epidemiológica de 2010 a 2025 y parte de las de 2001 a 2009, y casi todas las variables de producción de servicios del primer nivel (301 y 301a) de 2010 a 2025 y parte de las de 2008 y 2009.

## Tablas

Las estadísticas descargadas de SNIS en la carpeta `descarga/datos` están organizadas en una jerarquía: formulario / gestión / grupo / variable. SOAPS describe una jerarquía compatible y más profunda que aumenta 2 niveles adicionales: subvariable / regla. Una subvariable es representada internamente por una cadena de 9 dígitos donde los primeros 7 están reservados para formulario (3 dígitos) / grupo (2 dígitos) / variable (2 dígitos) más dos últimos dígitos para un código de subvariable. Denominamos a esta cadena la "casilla". En esta casilla los formularios 301 y 301a son representados como 301, el 301b como 304, los formularios 302 y 302a como 302 y el 302b como 305, pero los códigos de grupo y variable coinciden con los valores que ya extraimos en `descarga/datos`. Ésto hace posible relacionar atributos de casillas a las estadísticas que ya descargamos.

Cada fila de las tablas pertenece a una `version` de las reglas y a un `formulario` (`301`, `301a`, `301b`, `302`, `302a` o `302b`). La columna `formulario` separa el 301 y el 302, que se usaron hasta 2014, del 301a y el 302a, porque usan los mismos prefijos. Cada paquete tiene una versión de las reglas, con el nombre de su versión de SOAPS. El paquete 7.0.1 tiene dos: `7.0.1`, que SOAPS usa para las gestiones 2025 y 2026, y `7.0.1 anterior`, la configuración previa. La información más útil que extraimos de SOAPS es:

### Subvariables

Nombres de variables y subvariables en SOAPS útiles para validar que en realidad estamos refiriéndonos a las mismas prestaciones, enfermedades y poblaciones.

| version | formulario | casilla | variable | subvariable |
| --- | --- | --- | --- | --- |
| 2.0.0 | 302 | 302010101 | 1 Sarampión / Rubéola | < de 1 año |
| 2.0.0 | 302 | 302010102 | 1 Sarampión / Rubéola | 1 a 4 años |
| 4.0.0 | 302a | 302012901 | Anomalía Congénita | Menor de 6 meses |
| 7.0.1 | 302a | 302012501 | Influenza  (IRAG ,IRAGI y ETI) | a. Menor de 6 meses |
| 7.0.1 | 302a | 302090901 | Muerte menor de 5 años por diarrea | a. Menor de 6 meses - D |
| 7.0.1 | 302b | 305090201 | Enfermedad Renal Grado 3a | a. Menor de 6 meses - M |
| 1.0.4 | 301 | 301260202 | Talla Baja | 1 a menor de 2 años |
| 4.0.0 | 301a | 301032602 | Trat. de Fracturas dentoalveolares | 5 a 13 Años |
| 7.0.1 | 301a | 301052001 | DIU: Usuarias Nuevas | 10 a 14 |
| 7.0.1 | 301a | 301370101 | BCG | < a 1 año - D |

### Poblaciones

Los valores de `poblacion` dentro de las tablas de variables que publicamos en `descarga/datos` combinan sexo, rangos de edad, estatus de reconsulta y el lugar de la atención en una misma cadena de texto. Dentro de SOAPS esta información si está correctamente estructurada y nos permite reconstruir una tabla con columnas separadas para cada uno de estos atributos.

| version | formulario | casilla | regla_id | sexo | edad_unidad | edad_min | edad_max | reconsulta | lugar |
| --- | --- | --- | ---: | --- | --- | ---: | ---: | --- | --- |
| 7.0.1 | 302a | 302012501 | 5028 | MASCULINO | meses | 0 | 5 | false | |
| 7.0.1 | 302a | 302012501 | 5029 | FEMENINO | meses | 0 | 5 | false | |
| 7.0.1 | 302a | 302090901 | 11610 | MASCULINO | meses | 0 | 5 | | DENTRO |
| 7.0.1 | 302a | 302090901 | 11617 | FEMENINO | meses | 0 | 5 | | FUERA |
| 7.0.1 | 302b | 305090201 | 10202 | MASCULINO | meses | 0 | 5 | false | |
| 7.0.1 | 302b | 305090201 | 10203 | MASCULINO | meses | 0 | 5 | true | |
| 7.0.1 | 301a | 301052001 | 2337 | | años | 10 | 14 | | |
| 7.0.1 | 301a | 301370101 | 4000 | MASCULINO | años | 0 | 1 | | DENTRO |

### Cuadernos

El cuaderno, o libro de registro, donde se anotan las atenciones, útil para comprender el contexto de las consultas donde se producen los datos. Una regla puede contar atenciones de más de un cuaderno.

| version | formulario | casilla | regla_id | cuaderno_codigo | cuaderno |
| --- | --- | --- | ---: | ---: | --- |
| 7.0.1 | 302a | 302012501 | 5028 | 1 | CONSULTA EXTERNA |
| 7.0.1 | 302a | 302012501 | 5028 | 4 | ATENCION INTEGRAL DEL NIÑO(A) MENOR DE 5 AÑOS |
| 7.0.1 | 302a | 302012501 | 5028 | 5 | SEGUIMIENTO DE INTERNACIONES |
| 7.0.1 | 301a | 301052001 | 2337 | 2 | CONTROL PRENATAL, PARTO PUERPERIO |
| 7.0.1 | 301a | 301052001 | 2337 | 3 | ANTICONCEPCION |
| 7.0.1 | 301a | 301370101 | 4000 | 10 | VACUNAS |

### Unidades de registro

La columna de `valor` en nuestras tablas en `descarga/datos` puede estar contando muchas cosas. Dentro de SOAPS encontramos las unidades de estos valores y las reglas que se siguen para agregarlos en estadísticas. Cada fila es un campo del cuaderno que la regla compara. El `tipo` del campo indica qué cuenta la regla: 3 es un diagnóstico, 15 un valor de una lista, 0 una marca, como una dosis de vacuna, y 1 un número que el personal ya contó y anotó en el cuaderno, que SOAPS sólo suma.

| version | formulario | casilla | regla_id | campo | tipo | conector | valor_registrado |
| --- | --- | --- | ---: | --- | ---: | --- | --- |
| 7.0.1 | 302a | 302012501 | 5028 | DIAGNOSTICO I | 3 | OR | |
| 7.0.1 | 302a | 302012501 | 5028 | DIAGNOSTICO II | 3 | OR | |
| 7.0.1 | 302a | 302012501 | 5028 | DIAGNOSTICO III | 3 | OR | |
| 7.0.1 | 302a | 302090901 | 11610 | MORTALIDAD, CAUSAS < 5 AÑOS | 15 | DEP2 | [MUERTE MENOR 5 AÑOS POR DIARREA] |
| 7.0.1 | 302a | 302090901 | 11610 | MORTALIDAD (DENTRO, FUERA) | 15 | DEP1 | [DENTRO] |
| 7.0.1 | 302b | 305060101 | 11300 | PESO PARA LA TALLA(PESO/TALLA) | 15 | AND | [Obesidad (O)] |
| 7.0.1 | 301a | 301052001 | 2337 | METODOS ANTICONCEPTIVOS MODERNOS | 15 | OR | [DIU-NUEVA] |
| 7.0.1 | 301a | 301180101 | 2200 | Nº DE SINTOMÁTICOS RESPIRATORIOS IDENTIFICADOS - F | 1 | OR | |
| 7.0.1 | 301a | 301370101 | 4000 | BGC - DENTRO | 0 | | |

### Enfermedades

Las enfermedades que se monitorean cambian entre gestiones y son descritas con nombres y códigos propios del SNIS. Tener representaciones de estas enfermedades en clasificaciones estándarizadas nos ayudaría a crear series de tiempo entre gestiones y comparar resultados con otros países. Logramos identificar códigos CIE-10 para las enfermedades monitoreadas dentro de SOAPS. A primera vista estos códigos corresponden a la variación CIE-10-CM que publica en CDC norteamericano más algunas variaciones locales. Extraemos los códigos que incluye SOAPS sin modificaciones. Las reglas de producción de servicios casi no usan diagnósticos: sólo algunas casillas del 301 tienen enfermedades.

| version | formulario | casilla | regla_id | cie_codigo | cie_alfa | cie_descripcion |
| --- | --- | --- | ---: | ---: | --- | --- |
| 7.0.1 | 302a | 302012501 | 5028 | 10274 | J10 | Influenza debida a virus de la influenza identificado |
| 7.0.1 | 302a | 302012501 | 5028 | 10275 | J10.0 | Influenza con neumonía, debida a virus de la influenza identificado |
| 7.0.1 | 302a | 302012501 | 5028 | 10276 | J10.1 | Influenza con otras manifestaciones respiratorias, debida a  virus de la influenza identificado |
| 7.0.1 | 302b | 305090201 | 10202 | 78053 | N18.31 | Insuficiencia renal crónica de grado 3a |

### Versiones del índice

Para cada entrada 301, 301a, 301b, 302, 302a y 302b del índice, la versión de SOAPS cuyas reglas corresponden a esa variable y gestión. Las entradas sin una versión que coincida quedan vacías.

| formulario | gestion | grupo_codigo | variable_codigo | version |
| --- | ---: | --- | --- | --- |
| 301 | 2012 | 05 | 01 | 1.0.4 |
| 302 | 2012 | 01 | 01 | 1.0.4 |
| 302a | 2015 | 01 | 25 | 3.0.1 |
| 302a | 2017 | 01 | 25 | 4.0.0 |
| 302a | 2018 | 01 | 29 | 4.0.1 |
| 302a | 2019 | 01 | 25 | 5.0.1 |
| 302a | 2021 | 01 | 25 | 6.0.0 |
| 302a | 2025 | 01 | 25 | 7.0.1 |

`asignar.py` compara cada versión que tiene la variable con la entrada del índice, en este orden:

1. El nombre de la variable en el índice y en la versión.
2. Las poblaciones de los datos y las subvariables de la versión, por rango de edad. En el 301, la etiqueta de los datos empieza con el nombre de la variable, que se quita antes de comparar.
3. La fecha del paquete y la gestión. La versión 7.0.1 declara las gestiones 2025 y 2026.

Una entrada recibe la mejor versión sólo si el nombre y las poblaciones se parecen lo suficiente. Los umbrales y las reglas de comparación están al inicio de `asignar.py`.

### Límites

- Las versiones anteriores a 7.0.1 tienen las listas de valores sin etiquetas, así que no tienen `valor_registrado`, y sólo tienen `lugar` cuando el nombre del campo lo dice, como en «PENTAVALENTE 1RA DOSIS - DENTRO». Para el sexo usamos las etiquetas de 7.0.1, porque los códigos son los mismos.
- En las versiones 3.0.1 a 6.0.1, el lector no recupera el identificador de las enfermedades. Lo tomamos de las versiones 1.0.4, 2.0.0 y 7.0.1, que dan el mismo código y descripción para cada identificador.
- Las reglas del 301 y del 302 no tienen nombres. Sus nombres vienen del catálogo de subvariables más reciente hasta 2014 del mismo paquete (2013 en 1.0.4), que no existe en el paquete 7.0.1.
- SOAPS es el sistema del primer nivel de atención. Para el 301b, el formulario de los hospitales, sólo tiene 3 casillas de cirugías, sin nombres, así que ninguna entrada del 301b recibe una versión.
- Las casillas del 301 de 2001 a 2007 no coinciden con las de SOAPS.

## Reproducción

1. Descarga los paquetes de SOAPS y guárdalos en `../fuentes/`. `paquetes.py` tiene la SHA-256 de cada archivo. La versión 1.0.4 ya no está en el portal del SNIS; su enlace es una copia en Internet Archive.

| Versión | Archivo | Fecha |
| --- | --- | --- |
| 1.0.4 | [SETUP_SOAPS__104_01022013.rar](https://web.archive.org/web/20150410142113/http://snis.minsalud.gob.bo/documentacion/software-snis/ACTUALIZA_SOAPS_104_01022013.rar) | 2013-02-06 |
| 2.0.0 | [SETUP_SOAPS_200_2582014 1.rar](https://snis.minsalud.gob.bo/publicaciones?task=download.send&id=506&catid=37&m=0) | 2014-08-27 |
| 3.0.1 | [ACTUALIZA_SOAPS_3.0.1_310120160.rar](https://snis.minsalud.gob.bo/publicaciones?task=download.send&id=504&catid=36&m=0) | 2016-01-31 |
| 3.0.2 | [ACTUALIZA_SOAPS_3.0.2_26102016.rar](https://snis.minsalud.gob.bo/publicaciones?task=download.send&id=505&catid=36&m=0) | 2016-10-26 |
| 4.0.0 | [SETUP_SOAPS_400.rar](https://snis.minsalud.gob.bo/publicaciones?task=download.send&id=701&catid=15&m=0) | 2018-01-09 |
| 4.0.1 | [Instalador SOAPS 401.rar](https://snis.minsalud.gob.bo/publicaciones?task=download.send&id=779&catid=37&m=0) | 2018-07-03 |
| 5.0.1 | [SETUP_SOAPS_501.rar](https://snis.minsalud.gob.bo/publicaciones?task=download.send&id=931&catid=37&m=0) | 2020-05-11 |
| 6.0.0 | [SOAPS_600.rar](https://snis.minsalud.gob.bo/publicaciones?task=download.send&id=970&catid=37&m=0) | 2021-06-02 |
| 6.0.1 | [Instalador SOAPS 601.rar](https://snis.minsalud.gob.bo/publicaciones?task=download.send&id=990&catid=37&m=0) | 2022-06-02 |
| 7.0.1 | [SERVIDOR_SOAPS_7.rar](https://snis.minsalud.gob.bo/publicaciones?task=download.send&id=1217&catid=2&m=0) | 2026-08-31 |

2. Instala las dependencias.

Necesitas `git`, `unrar`, el SDK de .NET 8 (`dotnet`, o su ruta en la variable `DOTNET`) y Python 3.12 o superior.

```sh
pip install -r requirements.txt
```

3. Compila el lector de respaldos de bases de datos.

```sh
python lector/compilar.py lector/bin/
```

4. Extrae los artefactos con información relevante a una carpeta temporal.

```sh
python extraer.py lector/bin/lector.dll intermedios/ ../fuentes/*.rar
```

5. Construye las tablas desde datos en la carpeta temporal.

```sh
python construir.py intermedios/ tablas/
```

6. Asigna una versión de SOAPS a cada entrada de producción de servicios y de vigilancia epidemiológica del índice.

```sh
python asignar.py ../../../descarga/indice.csv ../../../descarga/datos/ tablas/
```
