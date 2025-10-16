# Módulo 1: Introducción al Data Engineering para IA

## Introducción

¡Bienvenido al primer módulo del curso de Data Engineering para Sistemas de IA! En este módulo estableceremos los fundamentos necesarios para comprender qué es el Data Engineering, por qué es crucial para los sistemas de IA modernos, y qué herramientas y técnicas utilizarás a lo largo del curso.

## Objetivos del Módulo

Al finalizar este módulo, serás capaz de:

- 🎯 Comprender el rol y responsabilidades de un Data Engineer
- 🎯 Identificar las diferencias entre Data Engineer, Data Scientist y ML Engineer
- 🎯 Conocer las arquitecturas de datos modernas (batch vs streaming, data lakes, data warehouses)
- 🎯 Familiarizarte con el ecosistema de herramientas de Data Engineering
- 🎯 Entender cómo los datos alimentan sistemas de IA y ML
- 🎯 Configurar tu entorno de desarrollo

## ¿Por qué es importante?

Los sistemas de IA más sofisticados del mundo (ChatGPT, recomendaciones de Netflix, búsqueda de Google) no funcionarían sin Data Engineers que construyan y mantengan la infraestructura de datos subyacente. 

**Dato importante**: Se estima que Data Engineers pasan 80% de su tiempo en preparación de datos y solo 20% en modelado. ¡Los datos de calidad son el fundamento de la IA!

## Conceptos Principales

### 1. ¿Qué es Data Engineering?

**Data Engineering** es la disciplina de diseñar, construir y mantener sistemas que recolectan, almacenan, procesan y proveen datos de manera confiable, escalable y eficiente.

**Analogía del mundo real:**

Imagina que eres el gerente de una gran cadena de restaurantes. Los Data Engineers son como tu equipo de logística:
- **Recolectan** ingredientes de proveedores (fuentes de datos)
- **Almacenan** en bodegas organizadas (data warehouses)
- **Procesan** y preparan los ingredientes (pipelines ETL)
- **Entregan** a las cocinas justo cuando se necesitan (APIs de datos)
- **Aseguran calidad** de los ingredientes (data quality)
- **Mantienen** la cadena de frío y frescura (data reliability)

### 2. El Rol del Data Engineer

**Responsabilidades principales:**

✅ **Diseñar arquitecturas de datos**
- Decidir cómo organizar y almacenar datos
- Elegir las tecnologías apropiadas
- Diseñar para escalabilidad

✅ **Construir pipelines de datos**
- ETL/ELT (Extract, Transform, Load)
- Procesamiento batch y streaming
- Orquestación de workflows

✅ **Garantizar calidad de datos**
- Validación y limpieza
- Manejo de datos faltantes
- Testing de pipelines

✅ **Optimizar rendimiento**
- Queries eficientes
- Almacenamiento optimizado
- Costos controlados

✅ **Colaborar con equipos**
- Data Scientists necesitan datos limpios
- ML Engineers necesitan features
- Analistas necesitan reportes

### 3. Data Engineer vs Data Scientist vs ML Engineer

| Aspecto | Data Engineer | Data Scientist | ML Engineer |
|---------|---------------|----------------|-------------|
| **Foco principal** | Infraestructura de datos | Insights y análisis | Modelos en producción |
| **Habilidades clave** | ETL, SQL, Pipelines | Estadística, ML, Visualización | ML, MLOps, Escalabilidad |
| **Herramientas** | Airflow, Spark, SQL | Python, R, Jupyter | TensorFlow, PyTorch, MLflow |
| **Entregables** | Pipelines, APIs de datos | Reportes, modelos | Modelos en producción |
| **Lenguajes** | Python, SQL, Scala | Python, R, SQL | Python, Go |

**En proyectos pequeños**, una persona puede hacer varios roles.  
**En empresas grandes**, cada rol es especializado.

### 4. Arquitecturas de Datos Modernas

#### A) Data Warehouse vs Data Lake vs Lakehouse

**Data Warehouse:**
- Datos **estructurados** y limpios
- Optimizado para análisis y BI
- Esquema definido antes de cargar (schema-on-write)
- Ejemplos: Snowflake, Redshift, BigQuery

**Data Lake:**
- Datos **raw** en cualquier formato
- Almacenamiento masivo y barato
- Esquema al leer (schema-on-read)
- Ejemplos: S3, Azure Data Lake, HDFS

**Lakehouse:**
- Lo mejor de ambos mundos
- Datos raw + capacidades de warehouse
- Transacciones ACID sobre data lakes
- Ejemplos: Databricks Delta Lake, Apache Iceberg

#### B) Batch vs Streaming

**Procesamiento Batch:**
- Procesa grandes volúmenes de datos en intervalos
- Ejemplo: Reportes diarios, entrenamientos de modelos
- Herramientas: Apache Spark, dbt, Airflow

**Procesamiento Streaming:**
- Procesa datos en tiempo real
- Ejemplo: Detección de fraude, recomendaciones live
- Herramientas: Kafka, Flink, Kinesis

### 5. El Data Engineer en Sistemas de IA

Los sistemas de IA modernos dependen de Data Engineers para:

**Para entrenamiento de modelos:**
- Recolectar y limpiar datos de entrenamiento
- Crear datasets balanceados
- Versionar datasets
- Generar features

**Para sistemas RAG (Retrieval Augmented Generation):**
- Ingestar documentos de múltiples fuentes
- Chunking y preprocesamiento de texto
- Generar embeddings
- Mantener bases de datos vectoriales actualizadas

**Para inferencia:**
- Proveer features en tiempo real
- Gestionar caché de predicciones
- Logging de inputs/outputs
- Monitoreo de data drift

### 6. El Ecosistema de Herramientas

**Lenguajes:**
- 🐍 **Python**: El lenguaje principal
- 💾 **SQL**: Esencial para datos
- ☕ **Scala**: Para Spark (opcional)

**Orquestación:**
- 🎵 **Apache Airflow**: Orquestador más popular
- 🔄 **Prefect**: Alternativa moderna
- ⚡ **Dagster**: Enfocado en data assets

**Procesamiento:**
- ⚡ **Apache Spark**: Procesamiento distribuido
- 🐼 **Pandas**: Procesamiento local
- 🐻‍❄️ **Polars**: Pandas pero más rápido
- 🔨 **dbt**: Transformaciones SQL

**Almacenamiento:**
- 🗄️ **PostgreSQL**: Base relacional confiable
- 🪣 **S3**: Object storage en AWS
- 🏔️ **Snowflake**: Data warehouse cloud
- 📊 **Redshift**: Data warehouse de AWS

**IA/ML:**
- 🦜 **LangChain**: Framework para LLMs
- 🤗 **Hugging Face**: Modelos pre-entrenados
- 📊 **MLflow**: Tracking de experimentos
- 🎯 **Pinecone/Chroma**: Bases vectoriales

**Cloud:**
- ☁️ **AWS**: Más usado en empresas
- 🔵 **Azure**: Fuerte en corporate
- 🔴 **GCP**: Excelente para ML

### 7. Ciclo de Vida de un Proyecto de Datos

```
1. INGESTA
   ↓ Recolectar datos de fuentes
   
2. ALMACENAMIENTO
   ↓ Guardar en data lake/warehouse
   
3. TRANSFORMACIÓN
   ↓ Limpiar, normalizar, enriquecer
   
4. MODELADO (opcional)
   ↓ Entrenar modelos ML
   
5. SERVICIO
   ↓ APIs, dashboards, aplicaciones
   
6. MONITOREO
   ↓ Observabilidad y alertas
```

Este ciclo se repite continuamente.

## Implementación Práctica

### Ejercicio 1: Configuración del Entorno

**Objetivo**: Preparar tu máquina para el curso.

**Pasos:**

1. **Instalar Python 3.10+**
```bash
python --version  # Verificar versión
```

2. **Crear entorno virtual**
```bash
python -m venv venv-data-eng
source venv-data-eng/bin/activate  # Linux/Mac
venv-data-eng\Scripts\activate     # Windows
```

3. **Instalar dependencias básicas**
```bash
pip install pandas numpy jupyter requests python-dotenv
```

4. **Instalar Docker** (para contenedores)
- Descarga de [docker.com](https://www.docker.com/)
- Verifica: `docker --version`

5. **Configurar Git**
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

### Ejercicio 2: Tu Primer Script de Data Engineering

**Objetivo**: Crear un simple pipeline ETL.

```python
# mi_primer_pipeline.py
import pandas as pd
from datetime import datetime

def extract():
    """Extrae datos de una fuente"""
    # Simulamos datos de ventas
    data = {
        'fecha': ['2024-01-01', '2024-01-02', '2024-01-03'],
        'producto': ['Laptop', 'Mouse', 'Teclado'],
        'precio': [1200, 25, 80],
        'cantidad': [2, 10, 5]
    }
    df = pd.DataFrame(data)
    print("✅ Extracción completada")
    return df

def transform(df):
    """Transforma los datos"""
    # Calcular total de venta
    df['total'] = df['precio'] * df['cantidad']
    
    # Convertir fecha a datetime
    df['fecha'] = pd.to_datetime(df['fecha'])
    
    # Agregar timestamp de procesamiento
    df['procesado_en'] = datetime.now()
    
    print("✅ Transformación completada")
    return df

def load(df, filename='ventas_procesadas.csv'):
    """Carga datos al destino"""
    df.to_csv(filename, index=False)
    print(f"✅ Datos cargados en {filename}")

# Ejecutar pipeline
if __name__ == "__main__":
    print("🚀 Iniciando pipeline ETL...")
    
    # ETL
    raw_data = extract()
    transformed_data = transform(raw_data)
    load(transformed_data)
    
    print("✨ Pipeline completado exitosamente!")
```

**Ejecuta:**
```bash
python mi_primer_pipeline.py
```

### Ejercicio 3: Análisis de un Caso Real

**Caso: Sistema de Recomendación de Netflix**

Investiga y responde:
1. ¿Qué datos necesita Netflix para recomendar series?
2. ¿De dónde vienen esos datos?
3. ¿Cómo se procesan? (batch o streaming)
4. ¿Qué rol juega el Data Engineer?

## Mejores Prácticas

### 1. Diseño de Datos

✅ **Usa convenciones de nombres consistentes**
```python
# Bueno
user_purchase_events
transaction_timestamp

# Malo
UserPurchaseEvents
trans_ts
```

✅ **Documenta tus pipelines**
```python
def process_user_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Procesa datos de usuarios.
    
    Args:
        df: DataFrame con columnas [user_id, name, email, created_at]
    
    Returns:
        DataFrame limpio y normalizado
    """
    # código aquí
```

✅ **Maneja errores gracefully**
```python
try:
    df = extract_data()
except ConnectionError as e:
    logger.error(f"Error conectando a la fuente: {e}")
    # Reintentar o alertar
```

### 2. Código Limpio

✅ **Funciones pequeñas y enfocadas**
```python
# Bueno: cada función hace una cosa
def validate_email(email: str) -> bool:
    return '@' in email

def clean_email(email: str) -> str:
    return email.lower().strip()
```

✅ **Usa type hints**
```python
from typing import List, Dict

def aggregate_sales(sales: List[Dict]) -> float:
    return sum(s['amount'] for s in sales)
```

### 3. Testing

✅ **Testea transformaciones críticas**
```python
import pytest

def test_calculate_total():
    data = {'precio': [10], 'cantidad': [2]}
    df = pd.DataFrame(data)
    result = transform(df)
    assert result['total'][0] == 20
```

## De Open Source a Enterprise

### Comparativa de Herramientas

| Categoría | Open Source | Enterprise | ¿Cuándo usar cada uno? |
|-----------|-------------|------------|------------------------|
| **Orquestación** | Apache Airflow | AWS Step Functions, Azure Data Factory | OS: Control total, customización. Ent: Menos mantenimiento |
| **Data Warehouse** | PostgreSQL, ClickHouse | Snowflake, Redshift, BigQuery | OS: Presupuesto limitado. Ent: Escala y soporte |
| **Processing** | Pandas, Polars | Databricks, AWS Glue | OS: Datos pequeños/medianos. Ent: Big data |
| **Monitoring** | Grafana, Prometheus | Datadog, New Relic | OS: Flexibilidad. Ent: Setup rápido |

### Transferencia de Habilidades

Las habilidades core son **transferibles**:

✅ **Conceptos fundamentales**: ETL, data modeling, quality
- Si aprendes con Airflow → Puedes usar Prefect, Dagster, Step Functions
- Si aprendes SQL en PostgreSQL → Es el mismo en Snowflake, Redshift

✅ **Arquitecturas**: Batch, streaming, lambda architecture
- Los patrones son los mismos en cualquier stack

✅ **Python**: Universal en data engineering
- Funciona con cualquier herramienta cloud o open source

**Consejo**: Aprende los fundamentos con open source (gratis), luego migra a enterprise cuando trabajes en una empresa.

## Conceptos Clave para Recordar

- 🔑 **Data Engineering**: Construir sistemas confiables para mover y transformar datos
- 🔑 **Pipeline ETL**: Extract → Transform → Load
- 🔑 **Data Warehouse**: Almacena datos estructurados para análisis
- 🔑 **Data Lake**: Almacena datos raw en cualquier formato
- 🔑 **Batch vs Streaming**: Procesamiento periódico vs tiempo real
- 🔑 **Data Quality**: La base de buenos sistemas de IA

## Próximos Pasos

En el **Módulo 2: ETL Pipelines** aprenderás:
- Diseñar pipelines ETL complejos
- Usar Apache Airflow para orquestación
- Manejar errores y reintentos
- Mejores prácticas de logging

**¿Qué necesitas saber antes de continuar?**
✅ Qué hace un Data Engineer  
✅ Diferencia entre batch y streaming  
✅ Qué es un pipeline ETL  
✅ Python básico  

## Recursos Adicionales

### Lectura
- 📖 [The Data Engineering Cookbook](https://github.com/andkret/Cookbook) - Guía completa gratuita
- 📖 "Designing Data-Intensive Applications" - Martin Kleppmann
- 📖 AWS Well-Architected Framework - Data Analytics Lens

### Videos
- 🎥 [What is Data Engineering?](https://www.youtube.com/watch?v=qWru-b6m030) - Seattle Data Guy
- 🎥 [Data Engineering Roadmap 2024](https://www.youtube.com/watch?v=iOPafVW2dAU)

### Comunidades
- 💬 r/dataengineering (Reddit)
- 💬 Data Engineering Discord
- 💬 LinkedIn Data Engineering Groups

### Herramientas para Practicar
- 🛠️ [Mode SQL Tutorial](https://mode.com/sql-tutorial/) - Aprende SQL gratis
- 🛠️ [Kaggle Datasets](https://www.kaggle.com/datasets) - Datos para practicar
- 🛠️ [AWS Free Tier](https://aws.amazon.com/free/) - Practica en la nube

## Reflexión Final

> "Los datos son el nuevo petróleo, pero sin refinación (Data Engineering) no valen nada."

Has dado el primer paso en un campo con enorme demanda y oportunidades. El Data Engineering es la base invisible que hace funcionar la IA moderna.

**Tu desafío**: Piensa en un problema que te gustaría resolver con datos. Podría ser:
- Analizar tus gastos personales
- Recomendar películas basado en tu historial
- Predecir demanda de productos
- Automatizar reportes de tu trabajo

Este será tu proyecto motivación durante el curso.

---

**¡Felicitaciones por completar el Módulo 1!** 🎉

Ahora ve a [actividad-interactiva.md](actividad-interactiva.md) para poner en práctica lo aprendido.
