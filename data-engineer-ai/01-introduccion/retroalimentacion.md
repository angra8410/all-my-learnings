# Retroalimentación y Soluciones - Módulo 1: Introducción al Data Engineering para IA

## Respuestas a Preguntas de Opción Múltiple

### Pregunta 1: ¿Cuál es la responsabilidad principal de un Data Engineer?
**Respuesta correcta: B) Diseñar y mantener sistemas que recolectan, almacenan y procesan datos**

**Explicación**: Aunque un Data Engineer puede tocar otras áreas, su responsabilidad core es construir y mantener la infraestructura de datos. Los modelos de ML son responsabilidad de ML Engineers/Data Scientists, los análisis son de Data Analysts, y las bases de datos son solo una parte del trabajo de un DE.

---

### Pregunta 2: ¿Qué significa ETL?
**Respuesta correcta: B) Extract, Transform, Load**

**Explicación**: ETL es el proceso fundamental en data engineering:
- **Extract**: Obtener datos de fuentes (APIs, bases de datos, archivos)
- **Transform**: Limpiar, normalizar, enriquecer los datos
- **Load**: Guardar en el destino final (warehouse, lake, database)

---

### Pregunta 3: ¿Cuál es la diferencia principal entre Data Warehouse y Data Lake?
**Respuesta correcta: B) Data Warehouse almacena datos estructurados con esquema definido, Data Lake almacena datos raw en cualquier formato**

**Explicación**:
- **Data Warehouse**: Datos estructurados, limpios, con esquema definido. Como una biblioteca organizada.
- **Data Lake**: Datos raw, cualquier formato (JSON, CSV, imágenes, logs). Como un almacén donde guardas todo "por si acaso".

No es sobre precio ni tamaño, sino sobre el nivel de estructura y procesamiento.

---

### Pregunta 4: ¿Qué caracteriza al procesamiento en tiempo real (streaming)?
**Respuesta correcta: B) Procesa datos continuamente a medida que llegan**

**Explicación**: Streaming procesa datos de forma continua, evento por evento, con latencia muy baja (segundos o menos). Batch procesa en lotes periódicos (horas o días). El costo y la tecnología son diferentes, pero la característica definitoria es el procesamiento continuo.

---

### Pregunta 5: ¿Cuál de estas herramientas NO es típicamente usada por Data Engineers?
**Respuesta correcta: C) Adobe Photoshop**

**Explicación**: Photoshop es para diseño gráfico, no tiene relación con data engineering. Airflow (orquestación), SQL (queries) y Pandas (procesamiento) son herramientas esenciales para DEs.

---

### Pregunta 6: ¿Qué es un Lakehouse?
**Respuesta correcta: B) Una combinación de Data Lake y Data Warehouse**

**Explicación**: Lakehouse es una arquitectura moderna que combina:
- La flexibilidad y bajo costo del Data Lake
- Las capacidades de consulta y transacciones del Data Warehouse
- Ejemplos: Databricks Delta Lake, Apache Iceberg

---

### Pregunta 7: ¿Qué porcentaje del tiempo de un Data Engineer típicamente se dedica a preparación de datos?
**Respuesta correcta: D) 80%**

**Explicación**: La regla 80/20 es famosa en data science: 80% del tiempo se va en preparar datos (limpieza, validación, transformación) y solo 20% en modelado/análisis. Por eso los Data Engineers son tan valiosos.

---

### Pregunta 8: ¿Cuál es la función principal de Apache Airflow?
**Respuesta correcta: B) Orquestar y programar workflows de datos**

**Explicación**: Airflow es un orquestador. Define, programa y monitorea workflows (DAGs - Directed Acyclic Graphs). No procesa big data (eso es Spark), no almacena (eso son databases), no visualiza (eso es BI).

---

## Respuestas a Verdadero o Falso

1. **Un Data Engineer y un Data Scientist hacen exactamente el mismo trabajo.**  
   **FALSO** - Aunque colaboran, sus roles son diferentes. DE construye infraestructura y pipelines, DS hace análisis y modelos. DE enfoca en "cómo" mover datos, DS en "qué" hacer con ellos.

2. **SQL es un lenguaje esencial para Data Engineers.**  
   **VERDADERO** - SQL es el lenguaje universal para trabajar con datos. Todo Data Engineer debe dominarlo. Es tan importante como Python.

3. **Los Data Engineers solo trabajan con datos estructurados.**  
   **FALSO** - Los DEs trabajan con todo tipo de datos: estructurados (SQL), semi-estructurados (JSON, XML), no estructurados (texto, imágenes, logs).

4. **Los sistemas de IA modernos pueden funcionar sin Data Engineers.**  
   **FALSO** - Los sistemas de IA necesitan datos de calidad, pipelines confiables y infraestructura escalable. Todo esto lo proveen Data Engineers. ChatGPT, por ejemplo, requiere enormes pipelines de datos.

5. **Procesamiento batch es siempre mejor que streaming.**  
   **FALSO** - Depende del caso de uso. Batch es mejor para reportes periódicos y procesamiento masivo. Streaming es mejor para tiempo real (fraude, alertas). Cada uno tiene su lugar.

6. **Python es el lenguaje más usado en Data Engineering.**  
   **VERDADERO** - Python es el lenguaje dominante por su ecosistema (Pandas, Spark, Airflow). Aunque SQL es igualmente importante, Python es el "pegamento" que une todo.

7. **Data quality es responsabilidad únicamente del equipo de QA.**  
   **FALSO** - Data quality es responsabilidad de TODOS, especialmente de Data Engineers. DEs deben implementar validaciones, tests y monitoring desde el inicio.

8. **Los pipelines de datos necesitan ser monitoreados continuamente.**  
   **VERDADERO** - Los pipelines pueden fallar por muchas razones (fuentes caídas, cambios de esquema, datos corruptos). Monitoring continuo es esencial para detectar y resolver problemas rápidamente.

---

## Respuestas a Relaciona Conceptos

**Correctas:**
1. Data Lake → **D** (Almacenamiento de datos raw en cualquier formato)
2. Apache Airflow → **A** (Orquestador de workflows de datos)
3. ETL → **E** (Extract, Transform, Load)
4. Data Warehouse → **B** (Almacén de datos estructurados optimizado para análisis)
5. Streaming → **C** (Procesamiento de datos en tiempo real)

---

## Soluciones a Completar el Código

### Ejercicio 1: Pipeline ETL Básico

```python
import pandas as pd

def extract():
    """Extrae datos de una fuente"""
    data = {
        'nombre': ['Ana', 'Luis', 'María'],
        'edad': [25, 30, 28]
    }
    df = pd.DataFrame(data)  # Solución
    return df

def transform(df):
    """Agrega una columna calculada"""
    df['edad_en_5_años'] = df['edad'] + 5  # Solución
    return df

def load(df):
    """Guarda los datos"""
    df.to_csv('personas_procesadas.csv', index=False)  # Solución
    print("Datos guardados")

# Ejecutar pipeline
raw_data = extract()
clean_data = transform(raw_data)
load(clean_data)
```

**Explicación**:
- `pd.DataFrame(data)`: Convierte un diccionario en DataFrame de Pandas
- `df['edad'] + 5`: Pandas permite operaciones vectorizadas sobre columnas
- `'personas_procesadas.csv'`: Nombre descriptivo para el archivo de salida

---

### Ejercicio 2: Validación de Datos

```python
def validate_email(email: str) -> bool:
    """Valida que un email sea válido"""
    return '@' in email and '.' in email  # Solución

def clean_data(df):
    """Limpia DataFrame eliminando valores nulos"""
    return df.dropna()  # Solución

# Test
assert validate_email("user@example.com") == True
assert validate_email("invalid-email") == False  # Solución
```

**Explicación**:
- `'@' in email`: Verifica que el string contenga @
- `df.dropna()`: Método de Pandas que elimina filas con valores NaN/None
- Validación básica (en producción usarías regex más complejas)

---

## Análisis de Casos: Soluciones

### Caso 1: E-commerce en Crecimiento

**1. ¿Qué tipo de procesamiento para reportes de ventas?**
✅ **Batch (una vez al día)**

**Justificación**: Los reportes de ventas no necesitan actualizarse en tiempo real. Procesar una vez al día (o cada hora) es suficiente y más eficiente. Permite agregar grandes volúmenes sin la complejidad de streaming.

**2. ¿Y para detección de fraude?**
✅ **Streaming (tiempo real)**

**Justificación**: El fraude debe detectarse inmediatamente para prevenir transacciones sospechosas. Cada segundo cuenta. Streaming permite analizar transacciones mientras ocurren.

**3. Tecnologías recomendadas:**
- **Reportes**: 
  - Airflow para orquestación
  - Spark o dbt para transformaciones batch
  - PostgreSQL/Redshift para warehouse
  - Tableau/Metabase para visualización

- **Fraude**: 
  - Kafka o Kinesis para streaming
  - Flink o Spark Streaming para procesamiento
  - Redis para caché de reglas
  - ML model en tiempo real

- **Recomendaciones**: 
  - Sistema híbrido (batch + streaming)
  - Vector database (Pinecone) para similitud
  - ML models pre-entrenados
  - Cache con Redis

---

### Caso 2: Sistema RAG para Documentación

**1. Orden correcto de pasos:**
1. Extraer texto de PDFs
2. Limpiar y normalizar texto
3. Dividir texto en chunks
4. Generar embeddings
5. Almacenar en base vectorial
6. Implementar búsqueda semántica

**Explicación del orden**:
- Primero extraes el contenido raw
- Luego lo limpias (eliminar formato, caracteres especiales)
- Divides en chunks manejables (para contexto del LLM)
- Generas embeddings numéricos de cada chunk
- Los guardas en base vectorial
- Finalmente implementas búsqueda

**2. Rol del Data Engineer:**
El Data Engineer es responsable de:
- Construir el pipeline de ingesta de PDFs
- Implementar procesamiento y chunking robusto
- Mantener la base vectorial actualizada
- Asegurar calidad de datos
- Orquestar el proceso end-to-end
- Monitorear y optimizar performance

**3. ¿Batch o streaming?**
**Batch** - Los documentos técnicos no cambian frecuentemente. Un procesamiento diario o cuando hay updates es suficiente. No necesitas streaming a menos que los docs se actualicen constantemente.

---

## Ejercicios Prácticos: Soluciones

### Ejercicio 1: Pipeline ETL de Ventas

```python
import pandas as pd
from datetime import datetime

ventas_raw = {
    'fecha': ['2024-01-01', '2024-01-02', '2024-01-01'],
    'producto': ['laptop', 'MOUSE', 'Teclado  '],
    'precio': [1000, 25, None],
    'cantidad': [2, 10, 5]
}

def extract_data(data_dict):
    """Convierte dict a DataFrame"""
    df = pd.DataFrame(data_dict)
    print(f"✅ Extracción: {len(df)} filas")
    return df

def transform_data(df):
    """
    Aplica transformaciones
    """
    # 1. Normalizar productos
    df['producto'] = df['producto'].str.lower().str.strip()
    
    # 2. Llenar precios None con 0
    df['precio'] = df['precio'].fillna(0)
    
    # 3. Calcular total
    df['total'] = df['precio'] * df['cantidad']
    
    # 4. Convertir fecha
    df['fecha'] = pd.to_datetime(df['fecha'])
    
    print(f"✅ Transformación completada")
    return df

def validate_data(df):
    """Valida datos"""
    checks = {
        'precios_positivos': (df['precio'] >= 0).all(),
        'cantidad_positiva': (df['cantidad'] > 0).all(),
        'producto_no_vacio': (df['producto'].str.len() > 0).all()
    }
    
    all_valid = all(checks.values())
    
    if all_valid:
        print("✅ Validación: Todos los checks pasaron")
    else:
        print("❌ Validación: Algunos checks fallaron")
        for check, passed in checks.items():
            print(f"  - {check}: {'✅' if passed else '❌'}")
    
    return all_valid

def load_data(df, filename='ventas_clean.csv'):
    """Guarda en CSV"""
    df.to_csv(filename, index=False)
    print(f"✅ Cargado: {filename} ({len(df)} filas)")

if __name__ == "__main__":
    print("🚀 Iniciando pipeline de ventas...\n")
    
    # ETL
    df = extract_data(ventas_raw)
    df = transform_data(df)
    
    # Validar antes de cargar
    if validate_data(df):
        load_data(df)
        print("\n✨ Pipeline completado exitosamente!")
    else:
        print("\n❌ Pipeline falló en validación")
```

**Conceptos clave**:
- `.str.lower()`: Método de strings en Pandas
- `.fillna(0)`: Reemplaza valores nulos
- Validación antes de cargar (data quality)
- Logging informativo en cada paso

---

### Ejercicio 2: Análisis de Logs

```python
import pandas as pd
import re
from datetime import datetime

logs = """
2024-01-15 10:30:15 INFO User login successful - user_id: 123
2024-01-15 10:30:20 ERROR Database connection failed - retrying...
2024-01-15 10:30:45 INFO User 456 viewed product page
2024-01-15 10:31:10 WARNING High memory usage: 85%
2024-01-15 10:31:25 INFO Purchase completed - order_id: 789
"""

def parse_logs(log_string):
    """Convierte logs a DataFrame"""
    lines = log_string.strip().split('\n')
    
    data = []
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.+)'
    
    for line in lines:
        match = re.match(pattern, line)
        if match:
            timestamp, level, message = match.groups()
            data.append({
                'timestamp': pd.to_datetime(timestamp),
                'level': level,
                'message': message
            })
    
    df = pd.DataFrame(data)
    print(f"✅ Parseados {len(df)} logs")
    return df

def analyze_logs(df):
    """Calcula estadísticas"""
    print("\n📊 Análisis de Logs:")
    print("-" * 50)
    
    # Total por nivel
    print("\nTotal por nivel:")
    print(df['level'].value_counts())
    
    # Número de errores
    errors = len(df[df['level'] == 'ERROR'])
    print(f"\n⚠️  Total de errores: {errors}")
    
    # Primera y última entrada
    print(f"\n🕐 Primera entrada: {df['timestamp'].min()}")
    print(f"🕐 Última entrada: {df['timestamp'].max()}")
    
    return {
        'counts_by_level': df['level'].value_counts().to_dict(),
        'errors': errors,
        'first': df['timestamp'].min(),
        'last': df['timestamp'].max()
    }

if __name__ == "__main__":
    print("🔍 Procesando logs...\n")
    df = parse_logs(logs)
    stats = analyze_logs(df)
    print("\n✅ Análisis completado!")
```

**Conceptos clave**:
- Regex para parsing estructurado
- `value_counts()` para agregaciones
- Filtrado con condiciones booleanas
- Análisis de series de tiempo

---

## Desafío del Módulo: Pipeline Meteorológico

### Solución Completa

```python
import requests
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import os

# Configuración
API_KEY = os.getenv('OPENWEATHER_API_KEY', 'tu_api_key_aqui')
CITY = "Madrid"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def extract_weather_data(city, api_key):
    """Llama a la API y obtiene datos"""
    try:
        params = {
            'q': city,
            'appid': api_key
        }
        
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Lanza excepción si hay error
        
        data = response.json()
        print(f"✅ Extracción: Datos obtenidos para {city}")
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"❌ Error en extracción: {e}")
        return None

def transform_weather_data(raw_data):
    """Transforma y limpia los datos"""
    if not raw_data:
        return None
    
    # Extraer información relevante
    transformed = {
        'ciudad': raw_data['name'],
        'pais': raw_data['sys']['country'],
        'temperatura_c': round(raw_data['main']['temp'] - 273.15, 2),
        'temp_min_c': round(raw_data['main']['temp_min'] - 273.15, 2),
        'temp_max_c': round(raw_data['main']['temp_max'] - 273.15, 2),
        'sensacion_termica_c': round(raw_data['main']['feels_like'] - 273.15, 2),
        'humedad_%': raw_data['main']['humidity'],
        'presion_hpa': raw_data['main']['pressure'],
        'descripcion': raw_data['weather'][0]['description'],
        'viento_velocidad_ms': raw_data['wind']['speed'],
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    df = pd.DataFrame([transformed])
    print(f"✅ Transformación: Temperatura convertida a Celsius")
    return df

def load_weather_data(df, filename='weather_data.csv'):
    """Guarda en CSV"""
    if df is None or df.empty:
        print("❌ No hay datos para cargar")
        return
    
    # Agregar a archivo existente o crear nuevo
    if os.path.exists(filename):
        df.to_csv(filename, mode='a', header=False, index=False)
    else:
        df.to_csv(filename, index=False)
    
    print(f"✅ Cargado: {filename}")

def create_visualization(df):
    """Genera gráfico de temperatura (bonus)"""
    if df is None or df.empty:
        return
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    categories = ['Mínima', 'Actual', 'Máxima', 'Sensación']
    values = [
        df['temp_min_c'].values[0],
        df['temperatura_c'].values[0],
        df['temp_max_c'].values[0],
        df['sensacion_termica_c'].values[0]
    ]
    
    ax.bar(categories, values, color=['blue', 'green', 'red', 'orange'])
    ax.set_ylabel('Temperatura (°C)')
    ax.set_title(f"Temperatura en {df['ciudad'].values[0]}")
    ax.grid(axis='y', alpha=0.3)
    
    plt.savefig('temperature_chart.png')
    print("✅ Gráfico guardado: temperature_chart.png")
    plt.close()

def run_pipeline():
    """Ejecuta el pipeline completo"""
    print("🌤️  Iniciando pipeline meteorológico...")
    print("=" * 50)
    
    # ETL
    raw_data = extract_weather_data(CITY, API_KEY)
    
    if raw_data:
        clean_data = transform_weather_data(raw_data)
        load_weather_data(clean_data)
        create_visualization(clean_data)
        
        print("\n📊 Resumen:")
        print(clean_data.to_string(index=False))
        print("\n✨ Pipeline completado exitosamente!")
    else:
        print("\n❌ Pipeline falló en extracción")

if __name__ == "__main__":
    run_pipeline()
```

**Conceptos aplicados**:
- API calls con manejo de errores
- Conversión de unidades (Kelvin a Celsius)
- Append a CSV existente
- Visualización con matplotlib
- Variables de entorno para API keys
- Estructura modular y reutilizable

**Para ejecutar**:
1. Obtén API key gratis en openweathermap.org
2. `export OPENWEATHER_API_KEY='tu_key'` (Linux/Mac)
3. `python weather_pipeline.py`

---

## Mejores Prácticas Aplicadas

### 1. Logging Informativo
```python
print("✅ Paso completado")  # Exitoso
print("❌ Error encontrado")  # Error
print("⚠️  Advertencia")      # Warning
```

### 2. Manejo de Errores
```python
try:
    result = risky_operation()
except SpecificError as e:
    logger.error(f"Error: {e}")
    # Manejar o re-lanzar
```

### 3. Validación de Datos
```python
def validate(df):
    assert not df.empty, "DataFrame vacío"
    assert df['precio'].min() >= 0, "Precios negativos"
    return True
```

### 4. Código Documentado
```python
def function(param: type) -> return_type:
    """
    Descripción clara de qué hace.
    
    Args:
        param: Qué es este parámetro
    
    Returns:
        Qué retorna la función
    """
```

---

## Recursos para Profundizar

### Próximos Pasos
1. **Practica más**: Crea tu propio pipeline con datos que te interesen
2. **Lee documentación**: Pandas, Requests, APIs públicas
3. **Únete a comunidades**: r/dataengineering, Data Engineering Discord
4. **Explora herramientas**: Instala y prueba Airflow localmente

### Datasets para Practicar
- Kaggle Datasets
- Public APIs (GitHub, Weather, News)
- Tu propia data (gastos, hábitos, etc.)

---

**¡Felicitaciones por completar el Módulo 1!** 🎉

Ya entiendes los fundamentos. Ahora estás listo para el **Módulo 2: ETL Pipelines** donde profundizaremos en orquestación con Airflow.

**Sigue practicando y nos vemos en el siguiente módulo!** 🚀
