"""
Minimal Airflow DAG Skeleton
=============================

Este DAG es un template básico que puedes copiar y adaptar para tus propios pipelines.
Incluye las mejores prácticas del 20% que usarás en 80% de tus DAGs.

Uso:
1. Copiar este archivo a ~/airflow-pareto/dags/
2. Renombrar y modificar según tu pipeline
3. Definir tus funciones de extract/transform/load
4. Configurar scheduling

Autor: Data Engineering Pareto 20/80 Course
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.sensors.filesystem import FileSensor
from datetime import datetime, timedelta
import logging

# ============================================================================
# CONFIGURACIÓN DEFAULT
# ============================================================================

default_args = {
    'owner': 'dataeng',
    'depends_on_past': False,
    'email': ['<YOUR_EMAIL>@example.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,                           # Reintentar 3 veces si falla
    'retry_delay': timedelta(minutes=5),    # Esperar 5 min entre reintentos
    'execution_timeout': timedelta(hours=2) # Timeout máximo de 2 horas
}

# ============================================================================
# FUNCIONES DE TASKS
# ============================================================================

def extract_data(**context):
    """
    Extrae datos desde fuente (CSV, API, DB).
    
    Args:
        **context: Airflow context con info de ejecución
        
    Returns:
        None (escribe datos a disco o retorna via XCom)
    """
    logging.info("Starting data extraction...")
    
    # Obtener fecha de ejecución
    execution_date = context['execution_date']
    logging.info(f"Extraction for date: {execution_date}")
    
    # TODO: Implementar lógica de extracción
    # Ejemplos:
    # - read_csv()
    # - API call con requests
    # - Query a DB con psycopg2/sqlalchemy
    
    # Ejemplo placeholder:
    data_path = f"/tmp/data_{execution_date.strftime('%Y%m%d')}.csv"
    logging.info(f"Data extracted to: {data_path}")
    
    # Opcional: pasar path via XCom para siguiente task
    context['task_instance'].xcom_push(key='data_path', value=data_path)
    
    return "Extract completed"


def transform_data(**context):
    """
    Transforma datos (limpieza, agregaciones, joins).
    
    Args:
        **context: Airflow context
        
    Returns:
        None
    """
    logging.info("Starting data transformation...")
    
    # Obtener path del task anterior via XCom
    data_path = context['task_instance'].xcom_pull(
        task_ids='extract', 
        key='data_path'
    )
    logging.info(f"Transforming data from: {data_path}")
    
    # TODO: Implementar lógica de transformación
    # Ejemplos:
    # - pandas transformations
    # - SQL transformations
    # - Spark job trigger
    
    output_path = data_path.replace('.csv', '_transformed.csv')
    logging.info(f"Transformed data saved to: {output_path}")
    
    context['task_instance'].xcom_push(key='output_path', value=output_path)
    
    return "Transform completed"


def load_data(**context):
    """
    Carga datos a destino (DB, data warehouse, S3).
    
    Args:
        **context: Airflow context
        
    Returns:
        None
    """
    logging.info("Starting data load...")
    
    # Obtener path del task anterior
    output_path = context['task_instance'].xcom_pull(
        task_ids='transform', 
        key='output_path'
    )
    logging.info(f"Loading data from: {output_path}")
    
    # TODO: Implementar lógica de carga
    # Ejemplos:
    # - df.to_sql() para PostgreSQL
    # - COPY command para Snowflake
    # - S3 upload con boto3
    
    rows_loaded = 1000  # placeholder
    logging.info(f"Loaded {rows_loaded} rows successfully")
    
    return "Load completed"


def validate_results(**context):
    """
    Valida que el pipeline se ejecutó correctamente.
    
    Args:
        **context: Airflow context
        
    Returns:
        None
        
    Raises:
        ValueError: Si validación falla
    """
    logging.info("Starting validation...")
    
    # TODO: Implementar checks
    # Ejemplos:
    # - Row count > 0
    # - No duplicados
    # - Valores en rango esperado
    # - Timestamp checks
    
    row_count = 1000  # placeholder - query real DB
    
    if row_count == 0:
        raise ValueError("No data loaded - pipeline failed!")
    
    logging.info(f"Validation passed: {row_count} rows")
    
    return "Validation completed"


# ============================================================================
# DEFINICIÓN DEL DAG
# ============================================================================

with DAG(
    dag_id='etl_pipeline_template',
    default_args=default_args,
    description='Template DAG para pipelines ETL básicos',
    schedule_interval='0 2 * * *',  # Daily at 2 AM (cron expression)
    start_date=datetime(2024, 1, 1),
    catchup=False,  # No ejecutar fechas pasadas
    tags=['etl', 'template', 'pareto'],
    max_active_runs=1  # Solo 1 ejecución a la vez
) as dag:
    
    # ------------------------------------------------------------------------
    # Task 1: Check de prerequisitos (opcional)
    # ------------------------------------------------------------------------
    check_file = FileSensor(
        task_id='check_source_file',
        filepath='/tmp/source_ready.flag',  # Archivo de señal
        poke_interval=60,  # Revisar cada 60 segundos
        timeout=600,  # Timeout después de 10 minutos
        mode='poke'  # 'poke' o 'reschedule'
    )
    
    # ------------------------------------------------------------------------
    # Task 2: Extract
    # ------------------------------------------------------------------------
    extract = PythonOperator(
        task_id='extract',
        python_callable=extract_data,
        provide_context=True
    )
    
    # ------------------------------------------------------------------------
    # Task 3: Transform
    # ------------------------------------------------------------------------
    transform = PythonOperator(
        task_id='transform',
        python_callable=transform_data,
        provide_context=True
    )
    
    # ------------------------------------------------------------------------
    # Task 4: Load
    # ------------------------------------------------------------------------
    load = PythonOperator(
        task_id='load',
        python_callable=load_data,
        provide_context=True
    )
    
    # ------------------------------------------------------------------------
    # Task 5: Validate
    # ------------------------------------------------------------------------
    validate = PythonOperator(
        task_id='validate',
        python_callable=validate_results,
        provide_context=True
    )
    
    # ------------------------------------------------------------------------
    # Task 6: Cleanup (opcional)
    # ------------------------------------------------------------------------
    cleanup = BashOperator(
        task_id='cleanup',
        bash_command='echo "Cleaning up temp files..." && rm -f /tmp/data_*.csv'
    )
    
    # ------------------------------------------------------------------------
    # Task 7: Success notification (opcional)
    # ------------------------------------------------------------------------
    notify_success = BashOperator(
        task_id='notify_success',
        bash_command='echo "Pipeline completed successfully!"'
    )
    
    # ========================================================================
    # DEPENDENCIAS (FLUJO DEL DAG)
    # ========================================================================
    
    # Flujo lineal básico:
    check_file >> extract >> transform >> load >> validate >> cleanup >> notify_success
    
    # Alternativas de flujo:
    # 
    # Paralelo (extract de múltiples fuentes):
    # [extract_source1, extract_source2] >> transform >> load
    # 
    # Condicional (con BranchPythonOperator):
    # check >> [path_a, path_b] >> join
    # 
    # Fan-out (una fuente, múltiples destinos):
    # extract >> [load_db, load_s3, load_warehouse]


# ============================================================================
# NOTAS DE USO
# ============================================================================
"""
PARETO 20% - Lo que DEBES saber de Airflow:

1. default_args:
   - retries: Siempre configurar (3 es buen default)
   - retry_delay: Espacio entre reintentos
   - email_on_failure: Para alertas

2. schedule_interval:
   - None: Manual trigger only
   - '@daily': Cada día a medianoche
   - '0 2 * * *': Cron expression (2 AM diario)
   - '@hourly', '@weekly', '@monthly'

3. Operators más usados:
   - PythonOperator: Ejecutar función Python
   - BashOperator: Ejecutar comando shell
   - FileSensor: Esperar archivo
   - DummyOperator: Placeholder (para organización)

4. XCom:
   - Pasar datos pequeños entre tasks
   - xcom_push(key, value) para enviar
   - xcom_pull(task_ids, key) para recibir

5. Context variables útiles:
   - execution_date: Fecha lógica de ejecución
   - task_instance: Info del task actual
   - dag_run: Info de la ejecución del DAG

6. Best practices:
   - catchup=False: Evitar backfills accidentales
   - max_active_runs=1: Evitar ejecuciones paralelas conflictivas
   - Usar logging en lugar de print
   - Idempotencia: DAG debe dar mismo resultado si se re-ejecuta

TROUBLESHOOTING común:

- DAG no aparece: Revisar syntax errors con `python <dag_file>.py`
- Task falla: Ver logs en Airflow UI > Task > Log
- Dependency issues: Verificar flow con `airflow dags show <dag_id>`
- Backfill: `airflow dags backfill <dag_id> -s <start> -e <end>`

NEXT STEPS:

1. Copiar este template
2. Renombrar dag_id
3. Implementar funciones extract/transform/load
4. Ajustar schedule_interval
5. Testear localmente
6. Deploy a Airflow
"""
