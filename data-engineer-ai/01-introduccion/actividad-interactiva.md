# Actividades Interactivas - Módulo 1: Introducción al Data Engineering para IA

## Sección 1: Preguntas de Opción Múltiple

### Pregunta 1
**¿Cuál es la responsabilidad principal de un Data Engineer?**

A) Crear modelos de Machine Learning  
B) Diseñar y mantener sistemas que recolectan, almacenan y procesan datos  
C) Hacer análisis estadístico y visualizaciones  
D) Gestionar bases de datos únicamente

**Tu respuesta**: B

---

### Pregunta 2
**¿Qué significa ETL?**

A) Execute, Test, Load  
B) Extract, Transform, Load  
C) Evaluate, Train, Learn  
D) Export, Transfer, Link

**Tu respuesta**: B

---

### Pregunta 3
**¿Cuál es la diferencia principal entre Data Warehouse y Data Lake?**

A) Data Warehouse es más caro que Data Lake  
B) Data Warehouse almacena datos estructurados con esquema definido, Data Lake almacena datos raw en cualquier formato  
C) Data Lake es solo para big data, Data Warehouse para datos pequeños  
D) No hay diferencia real, son términos intercambiables

**Tu respuesta**: B

---

### Pregunta 4
**¿Qué caracteriza al procesamiento en tiempo real (streaming)?**

A) Procesa grandes volúmenes una vez al día  
B) Procesa datos continuamente a medida que llegan  
C) Es más barato que procesamiento batch  
D) Solo funciona con Apache Spark

**Tu respuesta**: B

---

### Pregunta 5
**¿Cuál de estas herramientas NO es típicamente usada por Data Engineers?**

A) Apache Airflow  
B) SQL  
C) Adobe Photoshop  
D) Pandas

**Tu respuesta**: C

---

### Pregunta 6
**¿Qué es un Lakehouse?**

A) Una casa junto a un lago donde trabajan data engineers  
B) Una combinación de Data Lake y Data Warehouse  
C) Un tipo de base de datos NoSQL  
D) Una versión antigua de Data Lake

**Tu respuesta**: B

---

### Pregunta 7
**¿Qué porcentaje del tiempo de un Data Engineer típicamente se dedica a preparación de datos?**

A) 20%  
B) 40%  
C) 60%  
D) 80%

**Tu respuesta**: D

---

### Pregunta 8
**¿Cuál es la función principal de Apache Airflow?**

A) Procesar big data  
B) Orquestar y programar workflows de datos  
C) Almacenar datos  
D) Crear visualizaciones

**Tu respuesta**: B

---

## Sección 2: Verdadero o Falso

Marca V (Verdadero) o F (Falso) para cada afirmación:

1. **Un Data Engineer y un Data Scientist hacen exactamente el mismo trabajo.** F

2. **SQL es un lenguaje esencial para Data Engineers.** V

3. **Los Data Engineers solo trabajan con datos estructurados.** F

4. **Los sistemas de IA modernos pueden funcionar sin Data Engineers.** F

5. **Procesamiento batch es siempre mejor que streaming.** F

6. **Python es el lenguaje más usado en Data Engineering.** V

7. **Data quality es responsabilidad únicamente del equipo de QA.** F

8. **Los pipelines de datos necesitan ser monitoreados continuamente.** V

---

## Sección 3: Relaciona Conceptos

Conecta cada término con su descripción correcta:

**Términos:**
1. Data Lake
2. Apache Airflow
3. ETL
4. Data Warehouse
5. Streaming

**Descripciones:**
A) Orquestador de workflows de datos  
B) Almacén de datos estructurados optimizado para análisis  
C) Procesamiento de datos en tiempo real  
D) Almacenamiento de datos raw en cualquier formato  
E) Extract, Transform, Load

**Tus respuestas:**
1 → D | 2 → A | 3 → E | 4 → B | 5 → C

---

## Sección 4: Completar el Código

### Ejercicio 1
Completa el pipeline ETL básico:

```python
import pandas as pd

def extract():
    """Extrae datos de una fuente"""
    data = {
        'nombre': ['Ana', 'Luis', 'María'],
        'edad': [25, 30, 28]
    }
    df = pd.DataFrame(data)  # Completa aquí
    return df

def transform(df):
    """Agrega una columna calculada"""
    df['edad_en_5_años'] = df['edad'] + 5  # Completa aquí
    return df

def load(df):
    """Guarda los datos"""
    df.to_csv(Filename= index=False)  # Completa el nombre
    print("Datos guardados")

if __name__ == "__main__":
    print("🚀 Iniciando pipeline ETL...")

# Ejecutar pipeline
raw_data = extract()
clean_data = transform(raw_data)
load(clean_data)
```

---

### Ejercicio 2
Completa la validación de datos:

```python
def validate_email(email: str) -> bool:
    """Valida que un email sea válido"""
    return '@' in email and '.' in email  # Completa aquí

def clean_data(df):
    """Limpia DataFrame eliminando valores nulos"""
    return df.dropna()  # Completa con método de pandas

# Test
assert validate_email("user@example.com") == True
assert validate_email("invalid-email") == False  # Completa aquí
```

---

## Sección 5: Análisis de Casos

### Caso 1: E-commerce en Crecimiento

**Contexto:**
Una tienda online procesa 10,000 pedidos diarios. Necesitan:
- Reportes de ventas actualizados cada noche
- Detección de fraude en tiempo real
- Recomendaciones de productos

**Preguntas:**

1. **¿Qué tipo de procesamiento usarías para los reportes de ventas?**
   - [x ] Batch (una vez al día)
   - [ ] Streaming (tiempo real)
   
   **Justifica**: Batch, porque ellos necesitan los reportes todos los dias en la noche.
   
3. **¿Y para detección de fraude?**
   - [ ] Batch
   - [x] Streaming
   
   **Justifica**: Se necesita monitorizar transacciones fraudulentas en tiempo real.

4. **¿Qué tecnologías recomendarías para cada necesidad?**
   - Reportes: power bi, snowflake
   - Fraude: kafka, flink, redis, seldon, snowflake
   - Recomendaciones: ___________________________________________

---

### Caso 2: Sistema RAG para Documentación

**Contexto:**
Una empresa quiere crear un chatbot que responda preguntas sobre sus manuales técnicos (1000+ documentos PDF).

**Preguntas:**

1. **¿Qué pasos del pipeline de datos son necesarios?**
   
   Ordena del 1 al 6:
   - [5] Generar embeddings
   - [1] Extraer texto de PDFs
   - [2] Almacenar en base vectorial
   - [4] Dividir texto en chunks
   - [3] Limpiar y normalizar texto
   - [6] Implementar búsqueda semántica

2. **¿Qué rol juega el Data Engineer aquí?**
   
   Es quien Extrae, almacena, hace data transformation, modela, sirve el modèlo e itera cuantas veces sea necesario.
   ___________________________________________

3. **¿Batch o streaming para este caso?**
   
   Batch

---

## Sección 6: Diseño de Arquitectura

### Ejercicio: Tu Primer Diseño

**Escenario:**
Diseña una arquitectura simple para este caso:

**Requisito**: Una app de análisis de redes sociales que:
1. Recolecta tweets sobre un tema cada hora
2. Analiza sentimiento (positivo/negativo)
3. Genera dashboard con tendencias

**Tu diseño (dibuja o describe):**

```
INGESTA:
¿De dónde vienen los datos?
Los datos se obtienen desde X a travès de la API de ellos

ALMACENAMIENTO:
¿Dónde los guardas?
S3

PROCESAMIENTO:
¿Cómo los procesas?
Se hace anàlisis de sentimiento, se buscan las palabras y se hace un chunk de lo que se necesita para preparar los datos en vectores

VISUALIZACIÓN:
¿Cómo los muestras?
Yo los muestro a travès de una herramienta de BI

HERRAMIENTAS:
¿Qué tecnologías usarías?
Airflow, power bi, kafka
```

---

## Sección 7: Ejercicios Prácticos de Código

### Ejercicio 1: Pipeline ETL Completo

**Tarea**: Crea un pipeline que procese datos de ventas.

**Archivo**: `ventas_etl.py`

```python
import pandas as pd
from datetime import datetime

# Datos de ejemplo
ventas_raw = {
    'fecha': ['2024-01-01', '2024-01-02', '2024-01-01'],
    'producto': ['laptop', 'MOUSE', 'Teclado  '],
    'precio': [1000, 25, None],
    'cantidad': [2, 10, 5]
}

# TODO: Implementa las siguientes funciones

def extract_data(data_dict):
    """Convierte dict a DataFrame"""
    df = pd.DataFrame(data_dict)
    pass

def transform_data(df):
    """
    Aplica las siguientes transformaciones:
    1. Normalizar nombres de productos (lowercase, sin espacios extra)
    2. Llenar precios None con 0
    3. Calcular columna 'total' = precio * cantidad
    4. Convertir fecha a datetime
    """
    df[normalizar_nombres] = df['nombre'].str.lower().str.replace(" ", "", regex=False)
    df[llenar precios None con 0] = df['precio'].fillna(0)
    df[total] = df[precio] * df[cantidad]
    df[convertirfecha] = pd.to_datetime(df['fecha'])
    pass

def validate_data(df):
    """
    Valida que:
    1. No hay precios negativos
    2. Cantidad es mayor que 0
    3. Producto no es string vacío
    Retorna True si pasa todas las validaciones
    """
    
    df[nopreciosnegativos] = df[precios]>=0
    df[cantidadmayorquecero]= df[cantidad]>0
    df['productonovacio'] = df['producto'].notna() & df['producto'].astype(str).str.strip().ne('')
    df['valid'] = df['nopreciosnegativos'] & df['cantidadmayorquecero'] & df['productonovacio']
    return df['valid'].all()

    pass

def load_data(df, filename='ventas_clean.csv'):
    """Guarda en CSV"""
    df.to_csv(filename, index=False)
    print(f"✅ Datos cargados en {filename}")
    pass

# Ejecutar pipeline
if __name__ == "__main__":
    print("🚀 Iniciando pipeline ETL...")
    
    # ETL
    raw_data = extract()
    transformed_data = transform(raw_data)
    load(transformed_data)
    
    print("✨ Pipeline completado exitosamente!")
```

**Bonus**: Agrega logging para saber qué hace cada paso.
import logging
import pandas as pd

def validate_simple(df: pd.DataFrame,
                    price_col: str = 'precio',
                    qty_col: str = 'cantidad',
                    prod_col: str = 'producto') -> bool:
    """
    Validación simple:
      1) precio >= 0
      2) cantidad > 0
      3) producto no es cadena vacía ni NaN

    Devuelve True si TODAS las filas cumplen las 3 reglas.
    Imprime conteos simples de filas que fallan cada regla.
    """
    # Logging muy simple
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    logger = logging.getLogger("validate_simple")

    # Trabajamos con copia para no mutar el original
    df = df.copy()

    # Convertir columnas numéricas (no numérico -> NaN)
    prices = pd.to_numeric(df[price_col], errors='coerce')
    qty = pd.to_numeric(df[qty_col], errors='coerce')

    # Producto como string y strip() para quitar espacios
    prod = df[prod_col].astype(str).str.strip()

    # Máscaras de validación
    mask_price = prices >= 0
    mask_qty = qty > 0
    mask_prod = df[prod_col].notna() & (prod != '')

    # Conteos e info simple
    total = len(df)
    n_price_bad = (~mask_price).sum()
    n_qty_bad = (~mask_qty).sum()
    n_prod_bad = (~mask_prod).sum()

    logger.info(f"Total filas: {total}")
    logger.info(f"Filas con precio negativo: {int(n_price_bad)}")
    logger.info(f"Filas con cantidad <= 0 o no numérica: {int(n_qty_bad)}")
    logger.info(f"Filas con producto vacío o NaN: {int(n_prod_bad)}")

    # Resultado combinado: True si todas las filas son válidas
    valid = mask_price & mask_qty & mask_prod
    return valid.all()
---

### Ejercicio 2: Análisis de Logs

**Tarea**: Procesa logs de una aplicación web.

**Archivo**: `log_processor.py`

```python
import pandas as pd

# Logs de ejemplo
logs = """
2024-01-15 10:30:15 INFO User login successful - user_id: 123
2024-01-15 10:30:20 ERROR Database connection failed - retrying...
2024-01-15 10:30:45 INFO User 456 viewed product page
2024-01-15 10:31:10 WARNING High memory usage: 85%
2024-01-15 10:31:25 INFO Purchase completed - order_id: 789
"""

# TODO: Implementa
def parse_logs(log_string):
    """
    Convierte logs a DataFrame con columnas:
    - timestamp
    - level (INFO, ERROR, WARNING)
    - message
    """
    # Tu código aquí
    pass

def analyze_logs(df):
    """
    Calcula:
    - Total de logs por nivel
    - Número de errores
    - Primera y última entrada
    """
    # Tu código aquí
    pass

# Ejecutar
if __name__ == "__main__":
    # Tu código aquí
    pass
```

---

### Ejercicio 3: Configuración de Entorno

**Tarea**: Configura tu entorno de desarrollo completo.

**Checklist técnico:**
- [x] Python 3.10+ instalado
- [x] Entorno virtual creado
- [x] pandas, numpy, jupyter instalados
- [x] Docker instalado y funcionando
- [x] Git configurado
- [x] Cuenta GitHub creada
- [ ] Cuenta AWS Free Tier creada (opcional para módulos futuros)

**Verifica tu setup:**

```bash
# Crea archivo verify_setup.py
python verify_setup.py
```

```python
# verify_setup.py
import sys

def check_python_version():
    version = sys.version_info
    if version.major >= 3 and version.minor >= 10:
        print("✅ Python version OK:", sys.version)
    else:
        print("❌ Python version too old. Need 3.10+")

def check_packages():
    required = ['pandas', 'numpy', 'requests']
    for package in required:
        try:
            __import__(package)
            print(f"✅ {package} installed")
        except ImportError:
            print(f"❌ {package} NOT installed")

if __name__ == "__main__":
    print("🔍 Verificando setup...\n")
    check_python_version()
    check_packages()
    print("\n✨ Verificación completa!")
```

---

## Sección 8: Investigación y Pensamiento Crítico

### Pregunta 1: Investigación de Herramientas

**Tarea**: Investiga y compara dos orquestadores.

| Característica | Apache Airflow | Prefect |
|----------------|----------------|---------|
| Año de creación | 2014 | 2018 |
| Lenguaje | Python (DAGs en Python) | Python (Flows/Tasks en Python)
| Ventajas | - Muy maduro y ampliamente adoptado; gran ecosistema de operadores/integraciones. | ___ |
| Desventajas | ___ | ___ |
| Casos de uso ideales | Airbnb | Perfect |

**¿Cuál elegirías para un proyecto personal y por qué?**
Airflow, me parece que encajaria mas en lo que tengo pensado hacer, y tambien por la madurez que ya tiene, mas de una decada.
___________________________________________

---

### Pregunta 2: Análisis de Arquitectura Real

**Tarea**: Investiga la arquitectura de datos de Netflix.

1. **¿Qué problemas de datos tiene Netflix?**
   Escala masiva: ingesta, almacenamiento y procesamiento de petabytes de eventos por día (logs, métricas, eventos de reproducción).
Latencia/consistencia: necesidad de respuestas en tiempo real para personalización, recomendaciones y enrutamiento.
Heterogeneidad de datos: eventos en tiempo real, telemetría, logs, métricas, datos transaccionales y datasets de entrenamiento.
Calidad y gobernanza: asegurar calidad, trazabilidad y metadata (linaje, esquemas) para ML/BI en un ecosistema distribuido.
Evolución de esquemas: cambios frecuentes en eventos/telemetría deben gestionarse sin romper consumidores.
Disponibilidad y multi‑región: replicación y tolerancia a fallos para servir a usuarios globales.
Observabilidad y debugging: gran volumen requiere buenas herramientas para monitoreo, alertas y root‑cause analysis.
Costos: optimizar almacenamiento y cómputo en la nube (S3, EMR, etc.) para workloads muy grandes.

2. **¿Qué tecnologías usa?** (Investiga en internet)
   Cloud / almacenamiento:
Amazon Web Services: S3 (data lake), EC2, EMR, Lambda (usos varios).
Ingesta / transporte de eventos:
Suro (Netflix OSS) — sistema de transporte/ingesta de eventos; y uso de sistemas de streaming como Apache Kafka (o soluciones internas/híbridas) según necesidad.
Procesamiento en streaming / near‑real‑time:
Mantis (Netflix OSS) — plataforma de stream processing en tiempo real; también usan frameworks como Flink/Spark Streaming en ciertos casos.
Procesamiento batch / ML:
Apache Spark (sobre EMR) para ETL y entrenamiento; Hadoop/Hive históricamente (migración de HDFS → S3).
Query y análitica interactiva:
Presto (ahora Trino en otros sitios, pero Netflix impulsa Presto) para consultas interactivas a gran escala.
Orquestación y ejecución:
Genie (Netflix OSS) para orquestar jobs; además control propio sobre scheduling y runners.
Almacenamiento de estado / bases:
Cassandra (uso en casos de almacenamiento NoSQL), MySQL y caches como EVCache (memcached‑based) para baja latencia.
Metadata / gobernanza:
Metacat (Netflix OSS) y otros servicios internos para catálogo/metadata/linaje.
Observabilidad / monitoring:
Atlas (metrics, Netflix OSS), Spinnaker (deploy), herramientas internas de logging y dashboards.
Formatos y herramientas del ecosistema:
Parquet/Avro/ORC para datos columnados; Jupyter/Zeppelin para exploración; Python stack (pandas, numpy), frameworks ML (TensorFlow / PyTorch u otros según equipo).
Infraestructura contenedorizada / orquestación:
Titus (Netflix OSS) para contenedores; Kubernetes en algunos contextos.
Nota: Netflix además aporta muchos proyectos OSS (Suro, Mantis, Genie, Metacat, EVCache, Atlas, Titus, Spinnaker) — la adopción exacta de cada componente puede variar con el tiempo.

3. **¿Batch o streaming?**
   Ambos — enfoque híbrido:
Streaming / real‑time: para personalización en la reproducción, métricas en tiempo real, alertas y decisiones que requieren baja latencia (usando Mantis, Suro/Kafka, stream processors).
Batch: para feature engineering a gran escala, ETL y entrenamiento de modelos (Spark/EMR sobre S3), procesamientos periódicos y backfills.
En la práctica Netflix usa una arquitectura que combina pipelines streaming (para latencia y eventos) y pipelines batch (para computación a gran escala y reproducibilidad), integrando ambos resultados en la infraestructura de serving y en su feature store/capas de serving.

4. **¿Qué puedes aprender de su arquitectura?**
   wow, todavia estoy digiriendo todo la arquitectura de netflix

---

### Pregunta 3: Tu Caso de Uso

**Piensa en un proyecto personal que te gustaría hacer.**

**Describe:**
1. **¿Qué problema resuelve?**
   ___________________________________________

2. **¿Qué datos necesitas?**
   ___________________________________________

3. **¿De dónde vienen esos datos?**
   ___________________________________________

4. **¿Cómo los procesarías?** (Describe tu pipeline)
   ___________________________________________

5. **¿Qué herramientas usarías?**
   ___________________________________________

---

## Sección 9: Desafío del Módulo 🏆

### Proyecto Mini: Pipeline de Datos Meteorológicos

**Objetivo**: Crear un pipeline ETL que procese datos del clima.

**Requisitos:**

1. **Extract**: Usar API pública del clima (ejemplo: OpenWeatherMap)
2. **Transform**: 
   - Convertir temperatura de Kelvin a Celsius
   - Extraer fecha/hora
   - Calcular promedio, máxima, mínima del día
3. **Load**: Guardar en CSV con formato limpio
4. **Bonus**: Generar gráfico simple de temperatura

**Estructura sugerida:**

```python
# weather_pipeline.py
import requests
import pandas as pd
from datetime import datetime

API_KEY = "tu_api_key"  # Obtener de openweathermap.org
CITY = "Madrid"

def extract_weather_data(city, api_key):
    """Llama a la API y obtiene datos"""
    # Tu código aquí
    pass

def transform_weather_data(raw_data):
    """Transforma y limpia los datos"""
    # Tu código aquí
    pass

def load_weather_data(df, filename):
    """Guarda en CSV"""
    # Tu código aquí
    pass

def run_pipeline():
    """Ejecuta el pipeline completo"""
    print("🌤️ Iniciando pipeline meteorológico...")
    # Tu código aquí
    pass

if __name__ == "__main__":
    run_pipeline()
```

**Criterios de éxito:**
- [ ] Pipeline se ejecuta sin errores
- [ ] Datos se guardan correctamente
- [ ] Transformaciones aplicadas
- [ ] Código comentado
- [ ] Manejo básico de errores

---

## Autoevaluación

### ¿Cuántas preguntas/ejercicios completaste?

- Opción múltiple (1-8): ___ / 8
- Verdadero/Falso (1-8): ___ / 8
- Relacionar conceptos: ___ / 5
- Completar código: ___ / 2
- Análisis de casos: ___ / 2
- Ejercicios prácticos: ___ / 3
- Investigación: ___ / 3
- Desafío del módulo: ___ / 1

**Total**: ___ / 32

### Reflexión

**Lo que mejor entendí:**
___________________________________________
___________________________________________

**Lo que más me costó:**
___________________________________________
___________________________________________

**Preguntas que me quedaron:**
___________________________________________
___________________________________________

**Tiempo dedicado al módulo:** ___ horas

---

**Siguiente paso**: Revisa [retroalimentacion.md](retroalimentacion.md) para ver las soluciones y explicaciones, luego registra tu progreso en [progreso.md](progreso.md).

**¡Excelente trabajo! 🎉**
