# Módulo 7: Buenas Prácticas

## Introducción

En este módulo aprenderás las buenas prácticas esenciales para construir sistemas de datos confiables, mantenibles y escalables. Cubriremos testing, monitoring, logging, data quality y CI/CD.

## Objetivos del Módulo

Al finalizar este módulo, serás capaz de:

- 🎯 Implementar testing para pipelines de datos
- 🎯 Configurar logging efectivo
- 🎯 Implementar monitoring y alertas
- 🎯 Validar calidad de datos
- 🎯 Configurar CI/CD para datos
- 🎯 Documentar sistemas de datos

## ¿Por qué es importante?

Los pipelines de datos fallan. Datos malos causan malas decisiones. Sin testing, monitoring y validaciones, estás volando a ciegas. Las buenas prácticas previenen problemas costosos.

## Conceptos Principales

### 1. Testing de Pipelines

**Tipos de tests**:
- **Unit tests**: Testean funciones individuales
- **Integration tests**: Testean componentes juntos
- **Data tests**: Validan datos

**Unit testing con pytest**:
```python
# test_transformations.py
import pytest
import pandas as pd
from pipeline import clean_data, aggregate_sales

def test_clean_data_removes_nulls():
    # Arrange
    df = pd.DataFrame({
        'name': ['Alice', None, 'Bob'],
        'value': [10, 20, 30]
    })
    
    # Act
    result = clean_data(df)
    
    # Assert
    assert result['name'].isna().sum() == 0
    assert len(result) == 2  # Removed 1 row

def test_aggregate_sales_sums_correctly():
    df = pd.DataFrame({
        'date': ['2024-01-01', '2024-01-01', '2024-01-02'],
        'amount': [100, 50, 200]
    })
    
    result = aggregate_sales(df)
    
    assert result.loc[result['date'] == '2024-01-01', 'amount'].values[0] == 150
    assert len(result) == 2

# Ejecutar: pytest test_transformations.py
```

**Testing de Airflow DAGs**:
```python
# test_dags.py
from airflow.models import DagBag

def test_dag_loads():
    """Verifica que DAG se carga sin errores"""
    dagbag = DagBag()
    assert len(dagbag.import_errors) == 0

def test_dag_structure():
    """Valida estructura del DAG"""
    from dags.etl_pipeline import dag
    
    assert len(dag.tasks) == 3
    assert dag.schedule_interval == '@daily'
    
    # Verificar dependencias
    task_ids = [task.task_id for task in dag.tasks]
    assert 'extract' in task_ids
    assert 'transform' in task_ids
    assert 'load' in task_ids
```

### 2. Data Quality con Great Expectations

```python
import great_expectations as gx

# Crear contexto
context = gx.get_context()

# Definir expectativas
expectation_suite = context.create_expectation_suite(
    "sales_suite",
    overwrite_existing=True
)

# Cargar datos
df = pd.read_csv("sales.csv")
batch = context.sources.pandas_default.read_dataframe(df)

# Definir expectations
batch.expect_column_values_to_not_be_null("customer_id")
batch.expect_column_values_to_be_between("price", min_value=0, max_value=10000)
batch.expect_column_values_to_be_in_set("status", ["pending", "completed", "cancelled"])

# Validar
results = batch.validate()

if not results.success:
    print("⚠️ Validación falló:")
    for result in results.results:
        if not result.success:
            print(f"  - {result.expectation_config.expectation_type}")
```

**Custom data tests**:
```python
def validate_sales_data(df: pd.DataFrame) -> dict:
    """Valida datos de ventas"""
    issues = []
    
    # Check 1: No nulls en columnas clave
    key_columns = ['customer_id', 'product_id', 'amount']
    for col in key_columns:
        null_count = df[col].isna().sum()
        if null_count > 0:
            issues.append(f"{col} tiene {null_count} valores nulos")
    
    # Check 2: Valores positivos
    if (df['amount'] < 0).any():
        issues.append("Encontrados amounts negativos")
    
    # Check 3: Fechas válidas
    try:
        pd.to_datetime(df['date'])
    except:
        issues.append("Fechas inválidas")
    
    # Check 4: No duplicados
    duplicates = df.duplicated(subset=['order_id']).sum()
    if duplicates > 0:
        issues.append(f"{duplicates} order_ids duplicados")
    
    return {
        'valid': len(issues) == 0,
        'issues': issues
    }

# Uso en pipeline
validation = validate_sales_data(df)
if not validation['valid']:
    raise ValueError(f"Data quality issues: {validation['issues']}")
```

### 3. Logging Efectivo

**Setup de logging**:
```python
import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name: str):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Console handler
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    
    # File handler con rotación
    file_handler = RotatingFileHandler(
        'pipeline.log',
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    file_handler.setLevel(logging.DEBUG)
    
    # Formato
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    console.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    
    logger.addHandler(console)
    logger.addHandler(file_handler)
    
    return logger

# Uso
logger = setup_logger('etl_pipeline')

def extract_data():
    logger.info("Iniciando extracción...")
    try:
        data = fetch_from_api()
        logger.info(f"Extraídos {len(data)} registros")
        return data
    except Exception as e:
        logger.error(f"Error en extracción: {e}", exc_info=True)
        raise
```

**Structured logging con structlog**:
```python
import structlog

logger = structlog.get_logger()

logger.info(
    "pipeline_started",
    pipeline_name="sales_etl",
    source="api",
    expected_records=1000
)

logger.warning(
    "data_quality_issue",
    issue_type="missing_values",
    column="price",
    count=5
)
```

### 4. Monitoring y Alertas

**Métricas clave a monitorear**:
- Pipeline success rate
- Execution time
- Data freshness
- Data volume
- Error rates
- Data quality scores

**Con Prometheus + Grafana**:
```python
from prometheus_client import Counter, Histogram, Gauge, start_http_server
import time

# Definir métricas
pipeline_runs = Counter('pipeline_runs_total', 'Total pipeline executions')
pipeline_errors = Counter('pipeline_errors_total', 'Total pipeline errors')
execution_time = Histogram('pipeline_duration_seconds', 'Pipeline execution time')
records_processed = Gauge('records_processed', 'Number of records processed')

def run_pipeline():
    pipeline_runs.inc()
    
    start_time = time.time()
    try:
        # Tu pipeline aquí
        data = extract()
        transformed = transform(data)
        load(transformed)
        
        records_processed.set(len(transformed))
        
    except Exception as e:
        pipeline_errors.inc()
        raise
    finally:
        duration = time.time() - start_time
        execution_time.observe(duration)

# Exponer métricas
start_http_server(8000)
```

**Alertas con AWS CloudWatch**:
```python
import boto3

cloudwatch = boto3.client('cloudwatch')

def send_metric(metric_name: str, value: float):
    cloudwatch.put_metric_data(
        Namespace='DataPipeline',
        MetricData=[{
            'MetricName': metric_name,
            'Value': value,
            'Unit': 'Count'
        }]
    )

def send_alarm_if_needed(error_count: int, threshold: int = 5):
    if error_count >= threshold:
        cloudwatch.put_metric_alarm(
            AlarmName='PipelineErrors',
            MetricName='ErrorCount',
            Threshold=threshold,
            ComparisonOperator='GreaterThanThreshold',
            EvaluationPeriods=1,
            AlarmActions=['arn:aws:sns:us-east-1:123:alerts']
        )
```

### 5. CI/CD para Datos

**GitHub Actions para pipelines**:
```yaml
# .github/workflows/data-pipeline.yml
name: Data Pipeline CI/CD

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest great-expectations
    
    - name: Run unit tests
      run: pytest tests/
    
    - name: Run data quality tests
      run: great_expectations checkpoint run sales_checkpoint
    
    - name: Lint code
      run: |
        pip install flake8
        flake8 src/ --max-line-length=100
  
  deploy:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    
    steps:
    - name: Deploy to Airflow
      run: |
        # Copiar DAGs a Airflow
        aws s3 cp dags/ s3://airflow-dags/ --recursive
```

**Pre-commit hooks**:
```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.0.0
    hooks:
      - id: black
  
  - repo: https://github.com/pycqa/flake8
    rev: 6.0.0
    hooks:
      - id: flake8
  
  - repo: local
    hooks:
      - id: pytest
        name: pytest
        entry: pytest
        language: system
        pass_filenames: false
        always_run: true
```

### 6. Documentación

**Documentar DAGs**:
```python
from airflow import DAG

dag = DAG(
    'sales_etl',
    description="""
    ETL pipeline para procesar ventas diarias.
    
    Fuente: Sales API
    Destino: Redshift
    Frecuencia: Diario a las 2 AM
    Owner: Data Engineering
    
    Dependencias:
    - API key en Airflow Variables
    - Redshift credentials en Connections
    """,
    doc_md="""
    # Sales ETL Pipeline
    
    Este pipeline extrae datos de ventas del día anterior,
    aplica transformaciones y los carga en el warehouse.
    
    ## Pasos
    1. Extract: Llama a Sales API
    2. Transform: Limpia y agrega datos
    3. Validate: Verifica calidad
    4. Load: Carga a Redshift
    
    ## Monitoreo
    - Slack alerts en fallos
    - Métricas en CloudWatch
    """,
    tags=['sales', 'etl', 'daily']
)
```

**README para proyectos**:
```markdown
# Sales Data Pipeline

## Descripción
Pipeline ETL que procesa datos de ventas diarias.

## Arquitectura
```
API → Airflow → S3 (raw) → Spark → S3 (processed) → Redshift
```

## Setup
```bash
pip install -r requirements.txt
cp .env.example .env  # Configurar variables
```

## Ejecutar
```bash
# Localmente
python run_pipeline.py

# Con Airflow
airflow dags trigger sales_etl
```

## Testing
```bash
pytest tests/
```

## Monitoreo
- Dashboard: http://monitoring.company.com/sales-etl
- Alertas: #data-alerts en Slack
```

## Mejores Prácticas

### 1. Configuration Management
```python
# config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    db_host: str
    db_port: int = 5432
    api_key: str
    log_level: str = "INFO"
    
    class Config:
        env_file = ".env"

settings = Settings()
```

### 2. Error Handling
```python
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=4, max=10)
)
def fetch_from_api():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()
```

### 3. Data Lineage
```python
def track_lineage(source: str, destination: str, transformation: str):
    """Registra lineage de datos"""
    lineage_entry = {
        'timestamp': datetime.now().isoformat(),
        'source': source,
        'destination': destination,
        'transformation': transformation,
        'records': record_count
    }
    
    # Guardar en metastore
    save_to_metastore(lineage_entry)
```

## De Open Source a Enterprise

| Aspecto | Open Source | Enterprise |
|---------|-------------|------------|
| **Testing** | pytest | pytest + custom frameworks |
| **Quality** | Great Expectations | Monte Carlo, Datafold |
| **Monitoring** | Prometheus + Grafana | Datadog, New Relic |
| **CI/CD** | GitHub Actions | Jenkins, CircleCI |

## Conceptos Clave

- 🔑 **Testing**: Unit, integration, data tests
- 🔑 **Data Quality**: Validaciones y expectations
- 🔑 **Logging**: Structured logging
- 🔑 **Monitoring**: Métricas y alertas
- 🔑 **CI/CD**: Automatización de despliegue
- 🔑 **Documentation**: README, docstrings, DAG docs

## Próximos Pasos

En el **Módulo 8: Colaboración e Inglés** aprenderás:
- Inglés técnico para data engineering
- Code reviews efectivas
- Documentación internacional
- Trabajo en equipos distribuidos

## Recursos Adicionales

- 📖 [Great Expectations](https://docs.greatexpectations.io/)
- 📖 [pytest Documentation](https://docs.pytest.org/)
- 📖 [Prometheus Guide](https://prometheus.io/docs/introduction/overview/)
- 📚 "Testing Python" - Brian Okken

---

**¡Excelente trabajo completando el Módulo 7!** 🎉

Ya sabes implementar buenas prácticas profesionales. Continúa a [actividad-interactiva.md](actividad-interactiva.md).
