# Módulo 04 — Transformaciones con dbt

Objetivos:
- Entender el flujo de trabajo con dbt (models, snapshots, tests).
- Implementar transformaciones versionadas y reproducibles.

Contenido:
1. ¿Qué es dbt? conceptos y arquitectura
2. Estructura de un proyecto dbt
3. Models, seeds, snapshots, macros
4. Tests en dbt y documentación (docs)
5. Integración con warehouse (ej. Snowflake / Postgres)
6. Promoción: dev → staging → production

Actividades prácticas:
- Crear proyecto dbt con models para limpiar y moldear raw → staging → marts.
- Añadir tests personalizados y documentación (dbt docs).
- CI: ejecutar dbt run y dbt test en local / pipeline.