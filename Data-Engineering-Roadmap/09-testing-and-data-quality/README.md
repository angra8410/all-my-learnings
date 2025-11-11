# Módulo 09 — Testing y Calidad de Datos (Pareto 20/80)

Objetivo general:
Aprender el 20% de prácticas de testing y data quality que proporcionan el 80% de la confianza operativa: tests unitarios para transformaciones, checks SQL para calidad, y uso de frameworks como Great Expectations o dbt tests.

Resultados de aprendizaje:
- Implementar tests unitarios para funciones Python y jobs Spark.
- Definir y ejecutar checks de calidad (nulls, uniqueness, ranges, row counts).
- Automatizar tests en CI y en pipelines (Airflow/Databricks/dbt).

Duración estimada: 8-12 horas

Pareto 20/80:
- 20%: row counts, uniqueness, not_null, ranges, basic assertions in pytest/GE
- 80%: aplicar tests repetidamente en pipelines y crear criterios de alerta y rechazo

Estructura del módulo: actividad-interactiva.md, progreso.md, retroalimentacion.md, recursos.md, ejemplos de tests en /examples.
