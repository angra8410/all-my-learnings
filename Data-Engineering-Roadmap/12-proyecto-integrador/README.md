# Módulo 12 — Proyecto integrador (End-to-End)

Objetivos:
- Construir y entregar un pipeline end-to-end en la nube con orquestación, transformaciones y un data mart listo para análisis.

Requerimientos del proyecto:
- Ingesta desde 2 fuentes (API + CSV)
- Almacenamiento raw en S3/GCS
- Transformaciones versionadas con dbt (raw → staging → marts)
- Orquestación con Airflow (DAGs reproducibles)
- Warehouse (Snowflake o equivalente) con esquema dimensional
- Tests automatizados y CI/CD que ejecute tests y despliegue

Entregables:
1. Código fuente en carpeta del repo (scripts, dbt project, DAGs)
2. Documentación: README del proyecto, instrucciones de despliegue
3. Demo: notebook o dashboard que consulte el data mart
4. Informe de evaluación y checklist de progreso

Evaluación:
- Correcta ejecución de pipeline (40%)
- Calidad del modelado y tests (30%)
- Documentación y reproducibilidad (20%)
- Observabilidad y manejo de errores (10%)

Duración estimada: 2-3 semanas (proyecto final)