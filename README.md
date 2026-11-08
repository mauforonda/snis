# Estadísticas del SNIS de Bolivia

Datos de salud de Bolivia de 2001 a 2025, por municipio y por semana o mes, preparados para investigación. Vienen
de los tableros del Sistema Nacional de Información en Salud (SNIS) del Ministerio de Salud y Deportes: casos y
muertes que notifica la vigilancia epidemiológica, y consultas, vacunas, partos y otras prestaciones de los
establecimientos de salud.

**Para usar los datos, empiece por el [catálogo](datos/README.md).** Lista todos los datasets con sus gestiones,
periodicidad y desagregación, y explica cómo leerlos. Cada dataset tiene su propio `readme.md`.

```sql
-- duckdb, desde esta carpeta: casos de tos ferina por gestión
select gestion, sum(casos) as casos
from 'datos/vigilancia/casos/tos_ferina/datos.parquet'
group by gestion order by gestion;
```

## Contenido

| Carpeta | Qué contiene |
| --- | --- |
| [`datos/`](datos/README.md) | Los datasets para análisis: datos en parquet, `readme.md` y `datapackage.json`. |
| [`referencias/`](referencias/municipios/readme.md) | Tablas de apoyo: códigos y nombres de municipios. |
| [`descarga/`](descarga/README.md) | Copia fiel de los tableros del SNIS y el programa que la descarga. |
| [`contexto/`](contexto/README.md) | Formularios, instructivos y reglas del software SOAPS que ayudan a interpretar los tableros. |
| [`construccion/`](construccion/README.md) | Código que convierte la descarga en los datasets y su documentación. |

## Cómo reproducir

1. `descarga/`: descargar los tableros ([instrucciones](descarga/README.md)).
2. `contexto/sistemas/soaps/`: extraer las reglas de SOAPS ([instrucciones](contexto/sistemas/soaps/README.md)).
3. `construccion/`: construir y documentar los datasets ([instrucciones](construccion/README.md)).
