# Establecimientos

Una tabla por gestión con el padrón de establecimientos de salud publicado por
el Ministerio de Salud y Deportes de Bolivia.

## Cobertura

- 2005–2017: hojas anuales del libro consolidado usado por los proyectos
  anteriores.
- 2018–2022: estructuras cerradas anuales publicadas por SNIS-VE.
- 2023–2025: exportaciones detalladas del reporte dinámico de estructura,
  generadas el 2 de septiembre de 2026.

Las publicaciones de estructura están disponibles en:

- https://snis.minsalud.gob.bo/publicaciones/category/20-estructura
- https://snis.minsalud.gob.bo/49-estructura-de-establecimientos

Los archivos se copian sin modificar en `recursos/`. Sus nombres se
estandarizaron para que el extractor no dependa del nombre local original.

## Esquema

Cada `{gestion}.parquet` contiene una fila por establecimiento:

```text
gestion
departamento
municipio
municipio_codigo
red_salud
establecimiento
establecimiento_codigo
establecimiento_tipo
establecimiento_subsector
establecimiento_nivel
establecimiento_camas
```

`establecimiento_codigo` es el Código Único de seis dígitos. Los reportes
2023–2025 anteponen los dos dígitos de la gestión; el extractor valida y retira
ese prefijo.

Todos los campos salvo camas están disponibles o son derivables en todas las
fuentes. `establecimiento_tipo` aparece como una columna directa hasta 2022 y
como columnas indicadoras en 2023–2025. Las estructuras 2018–2022 no contienen
el número de camas; en esas gestiones `establecimiento_camas` es nulo.

## Uso

```bash
python dimensiones/establecimientos/extraer_establecimientos.py
python dimensiones/establecimientos/extraer_establecimientos.py 2024 2025
```
