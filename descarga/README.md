# Descarga

Copia fiel de los tableros de estadísticas del SNIS (Ministerio de Salud y Deportes de Bolivia), 2001–2025, por municipio y por semana o mes. Es la primera etapa del repositorio. Las tablas para análisis están en [`../datos`](../datos).

## Contenido

| Ruta | Qué es |
| --- | --- |
| `fuentes.csv` | Un tablero por formulario y gestión: `formulario`, `gestion`, `url`, `periodo` (`semana` o `mes`). |
| `dimensiones/variables/` | Grupos y variables que ofrece cada tablero, por gestión. Es la lista de tareas de descarga. |
| `dimensiones/establecimientos/` | Padrón de establecimientos por gestión. Da el código de municipio a cada fila descargada. |
| `datos/<formulario>/<gestion>/<grupo>/<variable>.parquet` | Datos descargados. |
| `indice.csv` | Una fila por variable y gestión: archivo, si la descarga tuvo éxito, filas y error. |
| `extraer_snis.py` | Programa de descarga. |

Formularios:

- `301` (2001–2014), `301a` (primer nivel, 2015–2025) y `301b` (segundo y tercer nivel, 2015–2025): producción de servicios.
- `302` (2001–2014), `302a` (2015–2025) y `302b` (enfermedades no transmisibles y factores de riesgo, 2015–2025): vigilancia epidemiológica.

## Esquema de los datos

| Campo | Descripción |
| --- | --- |
| `gestion` | Año. |
| `periodo` | Semana epidemiológica (302, 302a) o mes (301, 301a, 301b, 302b). |
| `municipio_codigo` | Código de municipio. Está guardado sin el cero inicial (5 caracteres); el código estándar tiene 6 dígitos `DDPPMM`. |
| `poblacion` | Etiqueta de columna del tablero. Puede combinar edad, sexo, caso nuevo o repetido, lugar y especialidad, separados por ` \| `. |
| `valor` | Número de atenciones, casos u otra unidad, según la variable. |

## Cómo se descargó

El tablero devuelve una tabla cruzada: una fila por municipio con registros en la variable y el periodo, una columna por categoría de población. `extraer_snis.py` pide cada variable por municipio y periodo, convierte la tabla a formato largo, quita la fila de total por municipio, descarta celdas vacías y conserva los ceros escritos. Cuando dos municipios tienen el mismo nombre, repite la consulta por departamento.

## Cobertura

- 8.209 variables-gestión, 128,7 millones de filas.
- 5 descargas fallaron (301b 2015, grupo 03) por errores del servidor. Están en `indice.csv` con `descargado = False`.
- El tablero 302b de 2019 no existe. La gestión 2026 está en `fuentes.csv` pero no se descargó.
- El Ministerio publica otros tableros con los mismos formularios desde 2008, los [reportes dinámicos](https://estadisticas.minsalud.gob.bo/Reportes_Dinamicos/Menu_rep_dinamicos.aspx). No se descargaron ni se compararon con esta copia.

## Reproducción

```bash
python dimensiones/variables/extraer_variables.py
python dimensiones/establecimientos/extraer_establecimientos.py
python extraer_snis.py
```

`extraer_snis.py --help` muestra las opciones para limitar gestiones, formularios y número de procesos.
