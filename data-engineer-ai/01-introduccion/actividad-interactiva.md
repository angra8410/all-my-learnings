# Actividades Interactivas - Módulo 1: Introducción al Data Engineering para IA

## Sección 1: Preguntas de Opción Múltiple

### Pregunta 1
**¿Cuál es la responsabilidad principal de un Data Engineer?**

A) Crear modelos de Machine Learning  
B) Diseñar y mantener sistemas que recolectan, almacenan y procesan datos  
C) Hacer análisis estadístico y visualizaciones  
D) Gestionar bases de datos únicamente

**Tu respuesta**: ___

---

### Pregunta 2
**¿Qué significa ETL?**

A) Execute, Test, Load  
B) Extract, Transform, Load  
C) Evaluate, Train, Learn  
D) Export, Transfer, Link

**Tu respuesta**: ___

---

### Pregunta 3
**¿Cuál es la diferencia principal entre Data Warehouse y Data Lake?**

A) Data Warehouse es más caro que Data Lake  
B) Data Warehouse almacena datos estructurados con esquema definido, Data Lake almacena datos raw en cualquier formato  
C) Data Lake es solo para big data, Data Warehouse para datos pequeños  
D) No hay diferencia real, son términos intercambiables

**Tu respuesta**: ___

---

### Pregunta 4
**¿Qué caracteriza al procesamiento en tiempo real (streaming)?**

A) Procesa grandes volúmenes una vez al día  
B) Procesa datos continuamente a medida que llegan  
C) Es más barato que procesamiento batch  
D) Solo funciona con Apache Spark

**Tu respuesta**: ___

---

### Pregunta 5
**¿Cuál de estas herramientas NO es típicamente usada por Data Engineers?**

A) Apache Airflow  
B) SQL  
C) Adobe Photoshop  
D) Pandas

**Tu respuesta**: ___

---

### Pregunta 6
**¿Qué es un Lakehouse?**

A) Una casa junto a un lago donde trabajan data engineers  
B) Una combinación de Data Lake y Data Warehouse  
C) Un tipo de base de datos NoSQL  
D) Una versión antigua de Data Lake

**Tu respuesta**: ___

---

### Pregunta 7
**¿Qué porcentaje del tiempo de un Data Engineer típicamente se dedica a preparación de datos?**

A) 20%  
B) 40%  
C) 60%  
D) 80%

**Tu respuesta**: ___

---

### Pregunta 8
**¿Cuál es la función principal de Apache Airflow?**

A) Procesar big data  
B) Orquestar y programar workflows de datos  
C) Almacenar datos  
D) Crear visualizaciones

**Tu respuesta**: ___

---

## Sección 2: Verdadero o Falso

Marca V (Verdadero) o F (Falso) para cada afirmación:

1. **Un Data Engineer y un Data Scientist hacen exactamente el mismo trabajo.** ___

2. **SQL es un lenguaje esencial para Data Engineers.** ___

3. **Los Data Engineers solo trabajan con datos estructurados.** ___

4. **Los sistemas de IA modernos pueden funcionar sin Data Engineers.** ___

5. **Procesamiento batch es siempre mejor que streaming.** ___

6. **Python es el lenguaje más usado en Data Engineering.** ___

7. **Data quality es responsabilidad únicamente del equipo de QA.** ___

8. **Los pipelines de datos necesitan ser monitoreados continuamente.** ___

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
1 → ___ | 2 → ___ | 3 → ___ | 4 → ___ | 5 → ___

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
    df = ___________(data)  # Completa aquí
    return df

def transform(df):
    """Agrega una columna calculada"""
    df['edad_en_5_años'] = df['edad'] + ___  # Completa aquí
    return df

def load(df):
    """Guarda los datos"""
    df.to_csv('_________.csv', index=False)  # Completa el nombre
    print("Datos guardados")

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
    return '___' in email and '.' in email  # Completa aquí

def clean_data(df):
    """Limpia DataFrame eliminando valores nulos"""
    return df.________()  # Completa con método de pandas

# Test
assert validate_email("user@example.com") == True
assert validate_email("invalid-email") == ___  # Completa aquí
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
   - [ ] Batch (una vez al día)
   - [ ] Streaming (tiempo real)
   
   **Justifica**: ___________________________________________

2. **¿Y para detección de fraude?**
   - [ ] Batch
   - [ ] Streaming
   
   **Justifica**: ___________________________________________

3. **¿Qué tecnologías recomendarías para cada necesidad?**
   - Reportes: ___________________________________________
   - Fraude: ___________________________________________
   - Recomendaciones: ___________________________________________

---

### Caso 2: Sistema RAG para Documentación

**Contexto:**
Una empresa quiere crear un chatbot que responda preguntas sobre sus manuales técnicos (1000+ documentos PDF).

**Preguntas:**

1. **¿Qué pasos del pipeline de datos son necesarios?**
   
   Ordena del 1 al 6:
   - [ ] Generar embeddings
   - [ ] Extraer texto de PDFs
   - [ ] Almacenar en base vectorial
   - [ ] Dividir texto en chunks
   - [ ] Limpiar y normalizar texto
   - [ ] Implementar búsqueda semántica

2. **¿Qué rol juega el Data Engineer aquí?**
   
   ___________________________________________
   ___________________________________________

3. **¿Batch o streaming para este caso?**
   
   ___________________________________________

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
___________________________________________

ALMACENAMIENTO:
¿Dónde los guardas?
___________________________________________

PROCESAMIENTO:
¿Cómo los procesas?
___________________________________________

VISUALIZACIÓN:
¿Cómo los muestras?
___________________________________________

HERRAMIENTAS:
¿Qué tecnologías usarías?
___________________________________________
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
    # Tu código aquí
    pass

def transform_data(df):
    """
    Aplica las siguientes transformaciones:
    1. Normalizar nombres de productos (lowercase, sin espacios extra)
    2. Llenar precios None con 0
    3. Calcular columna 'total' = precio * cantidad
    4. Convertir fecha a datetime
    """
    # Tu código aquí
    pass

def validate_data(df):
    """
    Valida que:
    1. No hay precios negativos
    2. Cantidad es mayor que 0
    3. Producto no es string vacío
    Retorna True si pasa todas las validaciones
    """
    # Tu código aquí
    pass

def load_data(df, filename='ventas_clean.csv'):
    """Guarda en CSV"""
    # Tu código aquí
    pass

# Ejecutar pipeline completo
if __name__ == "__main__":
    # Tu código aquí
    pass
```

**Bonus**: Agrega logging para saber qué hace cada paso.

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
- [ ] Python 3.10+ instalado
- [ ] Entorno virtual creado
- [ ] pandas, numpy, jupyter instalados
- [ ] Docker instalado y funcionando
- [ ] Git configurado
- [ ] Cuenta GitHub creada
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
| Año de creación | ___ | ___ |
| Lenguaje | ___ | ___ |
| Ventajas | ___ | ___ |
| Desventajas | ___ | ___ |
| Casos de uso ideales | ___ | ___ |

**¿Cuál elegirías para un proyecto personal y por qué?**
___________________________________________
___________________________________________

---

### Pregunta 2: Análisis de Arquitectura Real

**Tarea**: Investiga la arquitectura de datos de Netflix.

1. **¿Qué problemas de datos tiene Netflix?**
   ___________________________________________

2. **¿Qué tecnologías usa?** (Investiga en internet)
   ___________________________________________

3. **¿Batch o streaming?**
   ___________________________________________

4. **¿Qué puedes aprender de su arquitectura?**
   ___________________________________________

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
