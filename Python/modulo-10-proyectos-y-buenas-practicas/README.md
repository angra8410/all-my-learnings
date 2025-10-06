# Módulo 10: Proyectos y Buenas Prácticas

## Introducción

¡Felicitaciones por llegar al Módulo 10! Este es el módulo final donde consolidarás todo lo aprendido. Aprenderás a crear proyectos completos, seguir buenas prácticas profesionales y prepararte para el mundo real del desarrollo Python.

En este módulo aprenderás:
- Estructura de proyectos Python
- Buenas prácticas de código (PEP 8)
- Testing con unittest y pytest
- Documentación efectiva
- Control de versiones con Git
- Virtual environments
- Empaquetado y distribución
- Debugging y profiling

## ¿Por qué es importante?

Estas prácticas te permiten:
- Crear código mantenible y profesional
- Trabajar en equipo eficientemente
- Detectar bugs antes de producción
- Facilitar que otros usen tu código
- Ser un desarrollador más empleable

**Analogía:** Es como aprender a construir una casa completa, no solo conocer los materiales. Sabes qué va primero, cómo organizar todo y cómo asegurar que dure años.

## Conceptos Principales

### 1. Estructura de Proyectos

**Proyecto pequeño:**
```
mi_proyecto/
│
├── mi_paquete/
│   ├── __init__.py
│   ├── modulo1.py
│   └── modulo2.py
│
├── tests/
│   ├── __init__.py
│   ├── test_modulo1.py
│   └── test_modulo2.py
│
├── docs/
│   └── README.md
│
├── requirements.txt
├── setup.py
├── .gitignore
└── README.md
```

**Proyecto mediano/grande:**
```
mi_proyecto/
│
├── src/
│   └── mi_paquete/
│       ├── __init__.py
│       ├── core/
│       ├── utils/
│       └── api/
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── conftest.py
│
├── docs/
├── scripts/
├── config/
├── requirements/
│   ├── base.txt
│   ├── dev.txt
│   └── prod.txt
│
├── .env.example
├── .gitignore
├── README.md
├── setup.py
└── LICENSE
```

### 2. PEP 8 - Guía de Estilo

**Convenciones de nombres:**
```python
# Variables y funciones: snake_case
nombre_usuario = "Ana"
def calcular_total():
    pass

# Clases: PascalCase
class MiClase:
    pass

# Constantes: MAYUSCULAS
MAX_INTENTOS = 3
PI = 3.14159

# Módulos: lowercase
# archivo: mi_modulo.py
```

**Espaciado:**
```python
# ✅ Correcto
def funcion(a, b):
    resultado = a + b
    return resultado

x = 1
y = 2
z = x + y

# ❌ Incorrecto
def funcion( a,b ):
    resultado=a+b
    return resultado

x=1
y=2
z=x+y
```

**Longitud de línea:**
```python
# Máximo 79 caracteres por línea
# ✅ Correcto
resultado = funcion_muy_larga(
    parametro1,
    parametro2,
    parametro3
)

# Imports
# ✅ Correcto
import os
import sys
from typing import List, Dict

# ❌ Incorrecto
import os, sys
```

### 3. Testing

**unittest (incluido en Python):**
```python
import unittest

def sumar(a, b):
    return a + b

class TestSumar(unittest.TestCase):
    def test_suma_positivos(self):
        self.assertEqual(sumar(2, 3), 5)
    
    def test_suma_negativos(self):
        self.assertEqual(sumar(-1, -1), -2)
    
    def test_suma_cero(self):
        self.assertEqual(sumar(5, 0), 5)

if __name__ == '__main__':
    unittest.main()
```

**pytest (más moderno):**
```python
# test_matematicas.py
def sumar(a, b):
    return a + b

def test_suma_positivos():
    assert sumar(2, 3) == 5

def test_suma_negativos():
    assert sumar(-1, -1) == -2

def test_suma_cero():
    assert sumar(5, 0) == 5

# Ejecutar: pytest test_matematicas.py
```

**Fixtures en pytest:**
```python
import pytest

@pytest.fixture
def datos_prueba():
    return [1, 2, 3, 4, 5]

def test_suma(datos_prueba):
    assert sum(datos_prueba) == 15

def test_longitud(datos_prueba):
    assert len(datos_prueba) == 5
```

### 4. Documentación

**Docstrings:**
```python
def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.
    
    Args:
        base (float): La base del rectángulo
        altura (float): La altura del rectángulo
    
    Returns:
        float: El área del rectángulo (base × altura)
    
    Examples:
        >>> calcular_area_rectangulo(5, 3)
        15.0
    
    Raises:
        ValueError: Si base o altura son negativos
    """
    if base < 0 or altura < 0:
        raise ValueError("Base y altura deben ser positivos")
    return base * altura
```

**README.md completo:**
```markdown
# Mi Proyecto

Descripción breve del proyecto.

## Instalación

```bash
pip install -r requirements.txt
```

## Uso

```python
from mi_paquete import MiClase

obj = MiClase()
obj.metodo()
```

## Tests

```bash
pytest
```

## Licencia

MIT
```

### 5. Virtual Environments

```bash
# Crear entorno virtual
python -m venv venv

# Activar
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Crear requirements.txt
pip freeze > requirements.txt

# Desactivar
deactivate
```

### 6. Git y Control de Versiones

**.gitignore para Python:**
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
env/
*.egg-info/
dist/
build/

# IDEs
.vscode/
.idea/
*.swp

# Configuración local
.env
config.local.py

# OS
.DS_Store
Thumbs.db
```

**Workflow básico:**
```bash
# Inicializar repo
git init
git add .
git commit -m "Initial commit"

# Crear rama
git checkout -b feature/nueva-funcionalidad

# Hacer cambios
git add archivo.py
git commit -m "Agregar nueva funcionalidad"

# Merge
git checkout main
git merge feature/nueva-funcionalidad

# Push
git push origin main
```

### 7. Logging

```python
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='app.log'
)

logger = logging.getLogger(__name__)

def procesar_datos(datos):
    logger.info("Iniciando procesamiento")
    try:
        resultado = operacion_compleja(datos)
        logger.info("Procesamiento exitoso")
        return resultado
    except Exception as e:
        logger.error(f"Error en procesamiento: {e}")
        raise

# Niveles: DEBUG, INFO, WARNING, ERROR, CRITICAL
logger.debug("Mensaje de debug")
logger.info("Información general")
logger.warning("Advertencia")
logger.error("Error")
logger.critical("Error crítico")
```

### 8. Debugging

```python
# Usando pdb (Python Debugger)
import pdb

def funcion_compleja(x):
    pdb.set_trace()  # Pausa aquí
    resultado = x * 2
    return resultado

# Comandos útiles en pdb:
# n (next): Siguiente línea
# s (step): Entrar en función
# c (continue): Continuar
# p variable: Ver valor
# l (list): Ver código
# q (quit): Salir
```

## Implementación Práctica

### Proyecto Completo: Sistema de Tareas

**Estructura:**
```
todo_app/
├── src/
│   └── todo/
│       ├── __init__.py
│       ├── models.py
│       ├── storage.py
│       └── cli.py
├── tests/
│   ├── test_models.py
│   └── test_storage.py
├── requirements.txt
└── README.md
```

**models.py:**
```python
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class Tarea:
    """Representa una tarea."""
    id: int
    titulo: str
    completada: bool = False
    creada: datetime = datetime.now()
    
    def completar(self):
        """Marca la tarea como completada."""
        self.completada = True
    
    def __str__(self):
        estado = "✓" if self.completada else "○"
        return f"[{estado}] {self.titulo}"
```

**storage.py:**
```python
import json
from typing import List
from .models import Tarea

class AlmacenamientoTareas:
    """Gestiona el almacenamiento de tareas en JSON."""
    
    def __init__(self, archivo: str = "tareas.json"):
        self.archivo = archivo
    
    def guardar(self, tareas: List[Tarea]) -> None:
        """Guarda tareas en archivo JSON."""
        datos = [
            {
                "id": t.id,
                "titulo": t.titulo,
                "completada": t.completada
            }
            for t in tareas
        ]
        with open(self.archivo, 'w') as f:
            json.dump(datos, f, indent=2)
    
    def cargar(self) -> List[Tarea]:
        """Carga tareas desde archivo JSON."""
        try:
            with open(self.archivo, 'r') as f:
                datos = json.load(f)
            return [Tarea(**t) for t in datos]
        except FileNotFoundError:
            return []
```

**test_models.py:**
```python
import pytest
from todo.models import Tarea

def test_crear_tarea():
    tarea = Tarea(id=1, titulo="Test")
    assert tarea.titulo == "Test"
    assert tarea.completada == False

def test_completar_tarea():
    tarea = Tarea(id=1, titulo="Test")
    tarea.completar()
    assert tarea.completada == True
```

## Mejores Prácticas

1. **Principio DRY (Don't Repeat Yourself)**
   ```python
   # ❌ Repetitivo
   print("Hola Ana")
   print("Hola Carlos")
   
   # ✅ Mejor
   def saludar(nombre):
       print(f"Hola {nombre}")
   ```

2. **Principio KISS (Keep It Simple, Stupid)**
   ```python
   # ✅ Simple y claro
   def es_par(numero):
       return numero % 2 == 0
   ```

3. **Usa type hints**
   ```python
   def procesar(datos: List[int]) -> int:
       return sum(datos)
   ```

4. **Testea tu código**
   - Escribe tests para funciones críticas
   - Apunta a >80% de cobertura

5. **Documenta**
   - README claro
   - Docstrings en funciones públicas
   - Comentarios para lógica compleja

## Conceptos clave para recordar

- 🔑 **PEP 8**: Guía de estilo oficial
- 🔑 **Testing**: pytest o unittest
- 🔑 **Docstrings**: Documenta funciones
- 🔑 **Virtual env**: Aísla dependencias
- 🔑 **Git**: Control de versiones
- 🔑 **Logging**: Registra eventos
- 🔑 **DRY**: No te repitas

## Próximos Pasos

¡Has completado el curso de Python! Ahora puedes:

1. **Practicar** en plataformas como:
   - LeetCode
   - HackerRank
   - Codewars

2. **Crear proyectos** propios:
   - API REST
   - Web scraper
   - Bot de automatización
   - Análisis de datos

3. **Especializarte** en:
   - Data Science (Pandas, NumPy, Scikit-learn)
   - Web Development (Django, Flask, FastAPI)
   - Automatización (Selenium, Scrapy)
   - Machine Learning (TensorFlow, PyTorch)

4. **Contribuir** a proyectos open source en GitHub

**¡Felicitaciones! Eres oficialmente un desarrollador Python. Sigue practicando y nunca dejes de aprender. 🎉🐍🚀**
