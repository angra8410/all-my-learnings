# Módulo 08 — Airflow Orchestration (Pareto 20/80)

Objetivo general:
Aprender a diseñar y operar DAGs de Airflow que orquesten pipelines de datos con robustez: idempotencia, retries, sensores, integración con Spark/Databricks, y testing de DAGs.

Resultados de aprendizaje:
- Entender la arquitectura Airflow (Scheduler, Webserver, Workers).
- Diseñar DAGs idempotentes y parametrizados.
- Usar operadores relevantes (PythonOperator, BashOperator, SparkSubmitOperator, DatabricksRunNowOperator).
- Manejar conexiones y Variables, XCom y SLA/alerting.

Duración estimada: 10-14 horas
Prerequisitos: Python básico, experiencia con scripts ETL y/o Spark.

Pareto 20/80:
- 20%: DAG design (tasks dependencies, retries, idempotency), operators common
- 80%: practicar escribiendo DAGs que orquesten ingest -> transform -> test -> notify

Estructura del módulo:
- README + actividad + progreso + retroalimentacion + recursos
- Ejemplo DAG incluido en /examples
