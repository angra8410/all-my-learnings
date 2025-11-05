# Módulo 05 — Orquestación con Apache Airflow

Objetivos:
- Implementar DAGs para orquestar tareas ETL.
- Manejar dependencias, retries, triggers y variables.

Contenido:
1. Introducción a Airflow: conceptos (DAG, task, operator)
2. Instalación y arquitectura (scheduler, webserver, worker)
3. Operadores más usados (PythonOperator, BashOperator, S3, Snowflake)
4. Buenas prácticas: idempotencia, XCom, sensores
5. Programación de DAGs robustos: retries, SLA, alertas
6. Airflow en producción: executor (Local, Celery, Kubernetes)

Actividades prácticas:
- Crear DAG que orquesta: ingestión → dbt run → tests → notificación.
- Simular reintentos y errores controlados.