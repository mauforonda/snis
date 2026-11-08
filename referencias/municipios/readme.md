# Municipios

Código y nombre de los 344 municipios de los 9 departamentos, según el padrón de establecimientos de salud del SNIS. Sirve para unir los datasets con otras fuentes por municipio o para completar municipios sin registros.

## Cómo utilizar

| Columna | Descripción |
| --- | --- |
| `municipio_codigo` | Código del municipio, 6 dígitos: departamento (2), provincia (2) y municipio (2). |
| `municipio` | Nombre más reciente del municipio. |
| `provincia_codigo` | Código de la provincia, 4 dígitos. |
| `departamento_codigo` | Código del departamento, 2 dígitos. |
| `departamento` | Nombre del departamento. |

```sql
-- Casos de tos ferina de 2024 por provincia
select m.provincia_codigo, sum(c.casos) as casos
from 'datos/vigilancia/casos/tos_ferina/datos.parquet' c
join 'referencias/municipios/datos.parquet' m using (municipio_codigo)
where c.gestion = 2024 group by all order by casos desc;
```

## De dónde viene

Del padrón de establecimientos que acompaña a los tableros del SNIS ([`descarga/dimensiones/establecimientos`](../../descarga/dimensiones/establecimientos/)). Cuando un municipio cambia de nombre entre gestiones, se usa el más reciente.
