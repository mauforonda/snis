# Construcción

Código que convierte la copia de los tableros del SNIS ([`descarga/`](../descarga/README.md)) en los datasets de
[`datos/`](../datos/README.md) y su documentación. Las convenciones de los datos están en el
[catálogo](../datos/README.md#cómo-leer-los-datos); aquí se explica cómo se producen.

## Cómo ejecutar

Con Python 3.12 y las dependencias de [`requirements.txt`](requirements.txt), desde esta carpeta:

```bash
python p01_inventario.py
python p02_poblaciones.py vigilancia
python p02_poblaciones.py servicios
python p03_series.py
python p04_datasets.py vigilancia
python p04_datasets.py servicios
python p05_documentacion.py
```

Los pasos escriben archivos de trabajo en `intermedios/` (fuera de git). La construcción completa tarda unos 4
minutos y usa hasta 5 GB de memoria: duckdb tiene un límite de memoria, escribe en disco lo que no cabe y
agrega cada formulario por separado.

## Pasos

| Paso | Qué hace | Archivos |
| --- | --- | --- |
| 1. Inventario | Une el índice de la descarga con las versiones y los códigos CIE-10 de SOAPS, y resume las etiquetas de población de cada variable. | `p01_inventario.py` |
| 2. Poblaciones | Traduce cada etiqueta del tablero ("e. 10 a 14 años - F \| NUEVO9") a atributos: sexo, edad, caso, lugar y otros. Elige qué etiquetas se publican: el detalle, o el total si no hay detalle. | `p02_poblaciones.py`, `poblacion.py` |
| 3. Series | Asigna cada variable-gestión a un dataset, con las reglas por nombre de la variable. Separa el 301a del 301b y divide por periodo los datasets cuyas categorías o definición cambian. | `p03_series.py`, `conceptos.py` (vigilancia), `conceptos_servicios.py` (servicios) |
| 4. Datasets | Lee los valores positivos, les aplica los pasos 2 y 3 y escribe un parquet por dataset, sólo con las columnas que tienen valores. | `p04_datasets.py` |
| 5. Documentación | Calcula los hechos de cada dataset y escribe su `datapackage.json`, su `readme.md` (con los datasets relacionados) y el catálogo. | `p05_documentacion.py` |

`comun.py` tiene las rutas, las clasificaciones (carpetas), la conexión a duckdb y `Relacion`.

## Reglas

Todas las decisiones están en tres módulos, cada una con su motivo o su evidencia:

- `poblacion.py`: cómo se lee una etiqueta. `CORRECCIONES` describe cada grupo de variables cuyo encabezado no
  describe sus columnas, con la evidencia; el catálogo y los readme copian estos textos.
- `conceptos.py` (vigilancia):
  - cada `Regla` reconoce variables por su nombre normalizado y declara la población posible (para señalar
    registros implausibles) y una nota sobre lo que cuenta la serie;
  - `FAMILIAS` une en un dataset las partes de una enfermedad o los grados de una condición, con una columna que
    las distingue;
  - `CORTES` divide una serie en las gestiones en que cambia su definición.
- `conceptos_servicios.py` (servicios): el grupo del tablero da la clasificación y, a veces, la edad o el
  lugar; el nombre da atributos como la dosis o el método. Sin regla, cada nombre normalizado es un dataset, y
  las variables con el mismo nombre en distintas gestiones o formularios forman una serie. Cuando las variables
  de un grupo son bandas de edad, el nombre del dataset es el del grupo. `NOTAS` agrega advertencias.

Los dos módulos de conceptos tienen una lista `RELACIONES`: datasets que cuentan algo parecido con otro nombre,
otra definición o en otra sección del formulario, y qué supone unirlos. Los nombres de los datasets vienen del
tablero: el más largo de las variables que el dataset une, porque el índice corta o abrevia algunos.

Tres reglas valen para todos los datasets (paso 3):

- Un dataset tiene un solo conjunto de categorías y una sola definición en todas sus gestiones. Si cambian, el
  dataset se divide en periodos (`hepatitis_viral_2001_2014`, `hepatitis_viral_2015_2020`). Nada supone que
  dos conjuntos de categorías o dos definiciones cuentan lo mismo: la documentación los enlaza y da la consulta
  para unirlos. Un cambio de rótulo que no cambia lo que se cuenta (ortografía, numeración) no divide un
  dataset.
- Un dataset no une el 301a (servicios de primer nivel) con el 301b (segundo y tercer nivel): son registros
  complementarios. Si una variable tiene el mismo nombre en los dos, el dataset del 301b lleva `_301b`.
- Una nota describe lo que cuenta el dataset. Lo que cambia entre datasets no es una nota: es una relación.

Para cambiar un dataset, cambie la regla y ejecute otra vez los pasos 3 a 5. La documentación nunca se edita a
mano.

## Verificaciones

La construcción se detiene si:

- una etiqueta con valores queda sin traducir (paso 2);
- una variable-gestión con valores no aporta filas (paso 2);
- una variable-gestión con valores no tiene serie (paso 3);
- una familia usa el identificador de otra serie (`conceptos.py`);
- una relación declarada nombra un dataset que no existe (paso 5);
- la suma publicada no es igual a la suma de las etiquetas usadas, en cada formulario (paso 4).

Dos etiquetas de una variable-gestión sólo se suman en una fila cuando la etiqueta no distingue su población: pasa
en el formulario 302 de 2004, grupo 09 (mortalidad sin sexo). El paso 2 informa cuántas son.
