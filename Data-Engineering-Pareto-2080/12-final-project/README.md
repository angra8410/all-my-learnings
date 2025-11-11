# Módulo 12 — Proyecto Integrador (End-to-End)

Objetivo general:
Construir y entregar un pipeline end-to-end que demuestre las habilidades aprendidas: ingestión, almacenamiento raw, transformaciones con Spark/SQL, orquestación con Airflow/Databricks, testing y observabilidad. Proyecto orientado a portfolio profesional.

Visión del proyecto:
Construir un pipeline que consuma:
- Fuente A: CSVs (historical sales)
- Fuente B: API pública (user/market metadata)
Proceso:
- Ingesta → landing storage (raw) → transform (Spark/Scala, dbt-like) → warehouse (Delta/Snowflake) → data mart dimensional → dashboard o notebook de análisis.

Requerimientos mínimos:
- Ingesta automática desde ambas fuentes (script o notebook).
- Dataset raw almacenado (parquet/delta).
- Transformaciones versionadas (dbt o SQL models) que generen al menos 2 marts (fact_sales y dim_customer).
- Orquestación con Airflow o Databricks jobs con DAG reproducible.
- Suite de tests (pytest + SQL checks + GE or dbt tests).
- Observabilidad básica (métricas y alertas).
- Documentación y runbook de despliegue.

Duración estimada: 2–3 semanas (según dedicación)

Entregables obligatorios:
1. Código: scripts, notebooks, DAGs, models en carpeta `project/`.
2. Instrucciones de despliegue: `project/README-deploy.md`.
3. Datasets o enlaces a datasets usados.
4. Demo: notebook o link a dashboard (.pbix o screenshot).
5. Informe de evaluación: `project/evaluation.md` con evidencias de tests, logs, métricas y decisions.

Criterios de evaluación (resumen):
- Ejecución y reproducibilidad del pipeline (40%)
- Calidad del modelado y tests (30%)
- Documentación y reproducibilidad (20%)
- Observabilidad y manejo de errores (10%)

Sugerencias:
- Mantén el proyecto modular y versionado.
- Usa variables de entorno para credenciales y documenta placeholders.
- Si no puedes desplegar en cloud, documenta pasos y provee scripts que funcionen en local.
