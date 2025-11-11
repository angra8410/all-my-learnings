# Módulo 07 — dbt / SQL Transforms (Pareto 20/80)

Objetivo general:
Aprender el 20% esencial de trabajar con transformaciones SQL versionadas (dbt o patrones dbt-like sobre Delta/Snowflake) que generan el 80% del valor: modelos modulares, tests, documentación y promoción a entornos.

Resultados de aprendizaje:
- Inicializar un proyecto dbt (o estructurar SQL models) para producción.
- Crear modelos staging → marts y tests básicos (not_null, uniqueness).
- Generar documentación y ejecutar `dbt run` / `dbt test`.
- Conectar dbt a un backend (Delta via dbt-spark, Postgres o Snowflake).

Duración estimada: 8-12 horas
Prerequisitos: SQL avanzado, acceso a warehouse o Databricks con dbt-spark.

Pareto 20/80:
- 20%: models (staging/marts), seeds, tests simple, docs
- 80%: escribir modelos para casos reales y agregar tests para calidad

Estructura:
- README + actividad + progreso + retroalimentacion + recursos
- Ejemplo de modelo SQL y tests incluidos en /examples
