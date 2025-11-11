# Actividad Interactiva — Airflow Orchestration

🎯 Objetivo
Crear, probar y desplegar un DAG de Airflow que orqueste: ingest CSV -> Spark job (Databricks) -> dbt run -> tests -> notificación.

🛠 Ejercicio 1: Preparar entorno Airflow (local) (20 minutos)  
Objetivo: Levantar Airflow local con Docker Compose o con pip.

Pasos (Docker Compose):
```bash
# Desde la carpeta airflow-docker (ejemplo)
docker compose up -d
# Verificar
docker compose ps
```
Verificación: Airflow web UI accesible en http://localhost:8080 -> Sí / No

Duración: 20 minutos

🔧 Ejercicio 2: Crear DAG skeleton (30 minutos)  
Objetivo: Escribir un DAG que tenga tasks: ingest -> spark_job -> dbt -> tests -> notify.

Ejemplo DAG (resources/airflow_dag_example.py):
```python
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'dataeng',
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}

with DAG('sales_pipeline', start_date=datetime(2024,1,1), schedule_interval='@daily', default_args=default_args, catchup=False) as dag:
    ingest = BashOperator(
        task_id='ingest_csv',
        bash_command='python /opt/airflow/dags/scripts/ingest_csv.py'
    )

    run_dbt = BashOperator(
        task_id='run_dbt',
        bash_command='cd /opt/airflow/dags/dbt && dbt run'
    )

    run_tests = BashOperator(
        task_id='run_tests',
        bash_command='pytest -q /opt/airflow/dags/tests'
    )

    notify = BashOperator(
        task_id='notify',
        bash_command='echo "Pipeline finished"'
    )

    ingest >> run_dbt >> run_tests >> notify
```
Verificación: Guarda DAG y verifica en UI que aparece -> Sí / No

Duración: 30 minutos

🔁 Ejercicio 3: Integración con Databricks (40 minutos)  
Objetivo: Llamar a un job Databricks desde Airflow usando DatabricksSubmitRunOperator (o REST).

Pasos (ejemplo simplificado):
```python
from airflow.providers.databricks.operators.databricks import DatabricksRunNowOperator

run_databricks = DatabricksRunNowOperator(
    task_id='run_databricks',
    databricks_conn_id='databricks_default',
    job_id=12345,
    json={}
)
```
Verificación: Job run id in logs: _______________

Duración: 40 minutos

🧪 Ejercicio 4: Test y QA del DAG (30 minutos)  
Objetivo: Ejecutar tasks localmente y simular fallos para verificar retries y alerting.

Pasos:
```bash
airflow tasks test sales_pipeline ingest_csv 2025-01-01
```
Verificación: exit code 0 / logs muestran success -> _______________

Duración: 30 minutos

📦 Mini-proyecto (2 horas)  
Objetivo: Implementar DAG que corra diariamente, documentar SLA y alerting, y añadir dag-level tests (e.g., unit tests para funciones Python y smoke tests).

Entregables:
- dags/sales_pipeline.py
- scripts/ingest_csv.py
- README con runbook de fallo
Duración: 2 horas
