# Módulo 2: ETL Pipelines

## Introducción

En este módulo profundizaremos en el diseño e implementación de pipelines ETL (Extract, Transform, Load) robustos y escalables. Aprenderás a orquestar workflows complejos usando Apache Airflow, la herramienta más popular en la industria.

## Objetivos del Módulo

Al finalizar este módulo, serás capaz de:

- 🎯 Diseñar pipelines ETL eficientes y mantenibles
- 🎯 Implementar transformaciones complejas con Pandas y SQL
- 🎯 Orquestar workflows usando Apache Airflow
- 🎯 Manejar errores y reintentos en pipelines
- 🎯 Implementar logging y monitoring
- 🎯 Aplicar mejores prácticas de ETL

## ¿Por qué es importante?

Los pipelines ETL son el corazón de cualquier sistema de datos. Un pipeline bien diseñado significa datos confiables, procesamiento eficiente y sistemas escalables. Las empresas dependen de estos pipelines para tomar decisiones basadas en datos.

## Conceptos Principales

### 1. Anatomía de un Pipeline ETL

**Extract (Extracción)**
- Obtener datos de múltiples fuentes
- APIs REST, bases de datos, archivos, streams
- Manejo de autenticación y rate limits
- Validación inicial de datos

**Transform (Transformación)**
- Limpieza de datos
- Normalización y estandarización
- Enriquecimiento con datos adicionales
- Agregaciones y cálculos
- Validaciones de calidad

**Load (Carga)**
- Inserción en destino (warehouse, database, lake)
- Estrategias: full load, incremental, upsert
- Validación post-carga
- Actualización de metadatos

### 2. Apache Airflow: El Orquestador

**¿Qué es Airflow?**
- Plataforma para programar y monitorear workflows
- Define workflows como código (DAGs)
- Interfaz web para monitoreo
- Gestión de dependencias entre tareas
- Reintentos automáticos y alertas

**Conceptos clave:**

```python
# DAG: Directed Acyclic Graph
# Define el flujo de trabajo

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

dag = DAG(
    'mi_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule='@daily',  # Ejecuta diariamente
    catchup=False
)

# Tareas del pipeline
extract_task = PythonOperator(
    task_id='extract',
    python_callable=extract_data,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform',
    python_callable=transform_data,
    dag=dag
)

# Definir dependencias
extract_task >> transform_task  # extract debe completarse antes
```

### 3. Patrones de ETL

**Full Load (Carga Completa)**
```python
def full_load():
    # Extraer TODOS los datos cada vez
    data = extract_all_records()
    # Reemplazar tabla destino
    load_replace(data)
```
- **Pros**: Simple, estado consistente
- **Contras**: Lento para grandes volúmenes

**Incremental Load (Carga Incremental)**
```python
def incremental_load(last_timestamp):
    # Solo datos nuevos desde último run
    new_data = extract_since(last_timestamp)
    # Agregar a tabla existente
    load_append(new_data)
```
- **Pros**: Eficiente, rápido
- **Contras**: Más complejo, requiere tracking

**Upsert (Update + Insert)**
```python
def upsert_load(data):
    # Actualiza si existe, inserta si no
    for record in data:
        if exists(record['id']):
            update(record)
        else:
            insert(record)
```
- **Pros**: Maneja actualizaciones
- **Contras**: Más lento que append

### 4. Transformaciones con Pandas

**Limpieza de datos:**
```python
import pandas as pd

def clean_data(df):
    # Eliminar duplicados
    df = df.drop_duplicates()
    
    # Manejar nulos
    df['price'] = df['price'].fillna(0)
    
    # Normalizar strings
    df['name'] = df['name'].str.lower().str.strip()
    
    # Convertir tipos
    df['date'] = pd.to_datetime(df['date'])
    
    return df
```

**Agregaciones:**
```python
def aggregate_sales(df):
    return df.groupby('date').agg({
        'amount': 'sum',
        'quantity': 'count',
        'price': 'mean'
    }).reset_index()
```

### 5. Manejo de Errores

**Estrategias de retry:**
```python
from airflow.operators.python import PythonOperator

task = PythonOperator(
    task_id='extract_api',
    python_callable=extract_from_api,
    retries=3,  # Reintentar 3 veces
    retry_delay=timedelta(minutes=5)
)
```

**Try-catch con logging:**
```python
import logging

def extract_data():
    try:
        data = api.fetch_data()
        logging.info(f"Extracted {len(data)} records")
        return data
    except ConnectionError as e:
        logging.error(f"Connection failed: {e}")
        raise  # Re-lanzar para que Airflow lo detecte
    except ValueError as e:
        logging.warning(f"Data issue: {e}")
        return []  # Retornar vacío pero no fallar
```

### 6. Idempotencia

**Principio**: Un pipeline debe poder ejecutarse múltiples veces produciendo el mismo resultado.

```python
# Mal: No idempotente
def process_sales():
    sales = extract_all()
    db.insert(sales)  # Duplica en cada ejecución

# Bien: Idempotente
def process_sales(date):
    sales = extract_for_date(date)
    db.delete_for_date(date)  # Limpia primero
    db.insert(sales)  # Inserta limpio
```

## Implementación Práctica

### Ejercicio 1: Pipeline ETL con Pandas

```python
import pandas as pd
from datetime import datetime

def extract_sales_data():
    """Simula extracción de API"""
    return pd.DataFrame({
        'order_id': [1, 2, 3, 2],  # Duplicado
        'product': ['Laptop ', 'Mouse', None, 'mouse'],
        'price': [1000, 25, 50, None],
        'quantity': [1, 2, 1, 2],
        'date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-02']
    })

def transform_sales_data(df):
    """Transforma y limpia"""
    # Eliminar duplicados
    df = df.drop_duplicates(subset=['order_id', 'date'])
    
    # Limpiar productos
    df['product'] = df['product'].fillna('Unknown')
    df['product'] = df['product'].str.lower().str.strip()
    
    # Llenar precios con promedio
    df['price'] = df['price'].fillna(df['price'].mean())
    
    # Calcular total
    df['total'] = df['price'] * df['quantity']
    
    # Convertir fecha
    df['date'] = pd.to_datetime(df['date'])
    
    # Agregar metadata
    df['processed_at'] = datetime.now()
    
    return df

def load_sales_data(df):
    """Carga a destino"""
    df.to_csv('sales_clean.csv', index=False)
    return len(df)

# Ejecutar pipeline
raw_data = extract_sales_data()
clean_data = transform_sales_data(raw_data)
rows_loaded = load_sales_data(clean_data)
print(f"Pipeline completado: {rows_loaded} registros")
```

### Ejercicio 2: Tu Primer DAG en Airflow

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def extract(**context):
    # Extrae datos
    data = {'records': 100}
    context['task_instance'].xcom_push(key='data', value=data)
    print("✅ Extract completado")

def transform(**context):
    # Obtiene datos de extract
    ti = context['task_instance']
    data = ti.xcom_pull(key='data', task_ids='extract')
    # Transforma
    transformed = {'records': data['records'] * 2}
    ti.xcom_push(key='transformed', value=transformed)
    print("✅ Transform completado")

def load(**context):
    # Obtiene datos transformados
    ti = context['task_instance']
    data = ti.xcom_pull(key='transformed', task_ids='transform')
    print(f"✅ Load completado: {data['records']} records")

# Definir DAG
default_args = {
    'owner': 'data-engineer',
    'depends_on_past': False,
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'etl_pipeline_example',
    default_args=default_args,
    description='Pipeline ETL de ejemplo',
    schedule=timedelta(days=1),
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['etl', 'example']
)

# Crear tareas
extract_task = PythonOperator(
    task_id='extract',
    python_callable=extract,
    dag=dag
)

transform_task = PythonOperator(
    task_id='transform',
    python_callable=transform,
    dag=dag
)

load_task = PythonOperator(
    task_id='load',
    python_callable=load,
    dag=dag
)

# Definir flujo
extract_task >> transform_task >> load_task
```

## Mejores Prácticas

### 1. Diseño de Pipelines

✅ **Mantén tareas pequeñas y enfocadas**
```python
# Bueno: Tareas separadas
extract_customers >> transform_customers >> load_customers
extract_orders >> transform_orders >> load_orders

# Malo: Todo en una tarea gigante
do_everything()
```

✅ **Usa XCom para pasar datos pequeños**
```python
# Para datos pequeños (metadatos, counts)
ti.xcom_push(key='count', value=100)

# Para datos grandes, usa archivos o databases
df.to_parquet('temp_data.parquet')
```

✅ **Implementa checks de calidad**
```python
def data_quality_check(df):
    assert len(df) > 0, "DataFrame vacío"
    assert df['price'].min() >= 0, "Precios negativos"
    assert not df['id'].duplicated().any(), "IDs duplicados"
```

### 2. Configuración

✅ **Usa variables de entorno**
```python
import os

DB_HOST = os.getenv('DB_HOST', 'localhost')
API_KEY = os.getenv('API_KEY')
```

✅ **Centraliza configuración**
```python
# config.py
class Config:
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = int(os.getenv('DB_PORT', 5432))
    BATCH_SIZE = 1000
```

### 3. Logging

✅ **Log información útil**
```python
logging.info(f"Procesando batch {batch_num}/{total_batches}")
logging.warning(f"Encontrados {null_count} valores nulos")
logging.error(f"Error en API: {error_msg}")
```

## De Open Source a Enterprise

### Comparativa de Orquestadores

| Característica | Apache Airflow (OS) | AWS Step Functions | Azure Data Factory | Google Cloud Composer |
|----------------|---------------------|--------------------|--------------------|----------------------|
| **Costo** | Gratis (solo infra) | Pay per execution | Pay per activity | Pay per hora |
| **Setup** | Self-managed | Managed | Managed | Managed (Airflow) |
| **Flexibilidad** | Alta | Media | Media | Alta |
| **Curva aprendizaje** | Empinada | Suave | Media | Media |
| **Integración cloud** | Manual | Nativa AWS | Nativa Azure | Nativa GCP |
| **UI** | Excelente | Básica | Buena | Excelente |

### Transferencia de Habilidades

**De Airflow a cualquier orquestador:**

Los conceptos son universales:
- ✅ DAGs (flujo de trabajo)
- ✅ Tareas y dependencias
- ✅ Scheduling
- ✅ Reintentos y error handling
- ✅ Monitoreo y alertas

**Ejemplo de traducción:**

**Airflow:**
```python
task1 >> task2 >> task3
```

**Step Functions:**
```json
{
  "States": {
    "Task1": {"Next": "Task2"},
    "Task2": {"Next": "Task3"}
  }
}
```

**dbt (para transformaciones SQL):**
```yaml
models:
  - name: sales_clean
    depends_on:
      - ref('sales_raw')
```

### Cuándo usar cada uno

**Airflow (Open Source)**: 
- Control total, customización
- Stack on-premise
- Budget limitado
- Equipo con experiencia en Python

**Step Functions/Data Factory (Enterprise)**:
- Ya en AWS/Azure
- Menos mantenimiento
- Integración nativa
- Escalabilidad automática

## Conceptos Clave para Recordar

- 🔑 **ETL**: Extract, Transform, Load - proceso fundamental
- 🔑 **DAG**: Directed Acyclic Graph - define workflows
- 🔑 **Airflow**: Orquestador líder de la industria
- 🔑 **Idempotencia**: Ejecutar múltiples veces = mismo resultado
- 🔑 **Incremental**: Solo procesar datos nuevos
- 🔑 **XCom**: Compartir datos entre tareas en Airflow

## Próximos Pasos

En el **Módulo 3: Ingesta de Documentos** aprenderás:
- Procesar PDFs, Word, HTML
- Extraer texto y tablas
- Implementar chunking strategies
- Preparar documentos para RAG

## Recursos Adicionales

### Documentación
- 📖 [Apache Airflow Docs](https://airflow.apache.org/docs/)
- 📖 [Pandas User Guide](https://pandas.pydata.org/docs/user_guide/)
- 📖 [AWS Glue ETL](https://docs.aws.amazon.com/glue/)

### Tutoriales
- 🎥 [Airflow Tutorial for Beginners](https://www.youtube.com/watch?v=AHMm1wfGuHE)
- 🎥 [ETL Best Practices](https://www.youtube.com/watch?v=6-oBN3zjrqY)

### Libros
- 📚 "Data Pipelines Pocket Reference" - James Densmore
- 📚 "Fundamentals of Data Engineering" - Joe Reis & Matt Housley

---

**¡Excelente trabajo completando el Módulo 2!** 🎉

Ahora dominas el diseño e implementación de pipelines ETL. Continúa a [actividad-interactiva.md](actividad-interactiva.md) para practicar.
