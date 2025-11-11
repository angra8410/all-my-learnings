# Módulo 09 — Testing y Calidad de Datos (Pareto 20/80)

Objetivo general:
Aprender y aplicar el 20% de prácticas de testing y data quality que proporcionan el 80% de la confianza operativa: tests unitarios para transformaciones, checks SQL para calidad y uso de frameworks como Great Expectations o dbt tests.

Resultados de aprendizaje:
- Implementar tests unitarios para funciones Python y jobs Spark.
- Definir y ejecutar checks de calidad (nulls, uniqueness, ranges, row counts).
- Automatizar tests en CI y en pipelines (Airflow/Databricks/dbt/CI).
- Generar reportes de calidad y decisiones de rechazo/promoción de datos.

Duración estimada: 8–12 horas

Prerequisitos:
- Módulos previos: SQL core, Python ETL, Spark/Databricks básicos.
- Entorno: Python venv con pytest y (opcional) Great Expectations instalado.

Pareto 20/80:
- 20% para aprender: row counts, uniqueness, not_null, ranges, smoke tests.
- 80% para practicar: integrar esos checks en pipelines y repetición de tests en CI/airflow.

Estructura del módulo:
- README.md (este archivo)
- actividad-interactiva.md (ejercicios paso a paso y mini-proyectos)
- progreso.md (checklist)
- retroalimentacion.md (rúbrica)
- recursos.md (links, snippets y ejemplos)
- examples/: tests pytest, ejemplos Great Expectations, scripts de QA

Nota:
- Mantén tests ligeros (rápidos) y de bajo costo para ejecutar en CI.
- Los tests más costosos (full end-to-end) deben ejecutarse en cadenas nocturnas o entornos de staging.
