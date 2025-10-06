# Módulo 9: Python Avanzado

## Introducción

¡Bienvenido al Módulo 9! Aquí explorarás conceptos avanzados que te convertirán en un programador Python más sofisticado y eficiente.

En este módulo aprenderás:
- Decoradores
- Generadores e iteradores
- Context managers
- Funciones lambda avanzadas
- List/dict/set comprehensions avanzadas
- args y kwargs
- Type hints
- Expresiones regulares

## ¿Por qué es importante?

Estos conceptos te permiten:
- Escribir código más elegante y eficiente
- Entender código profesional de terceros
- Optimizar el uso de memoria
- Crear abstracciones poderosas

**Analogía:** Es como pasar de ser un chef casero a un chef profesional: conoces las mismas técnicas básicas, pero ahora las dominas y puedes crear platillos más sofisticados.

## Conceptos Principales

### 1. Decoradores

Los decoradores son funciones que modifican el comportamiento de otras funciones:

```python
# Decorador simple
def mi_decorador(func):
    def wrapper():
        print("Antes de la función")
        func()
        print("Después de la función")
    return wrapper

@mi_decorador
def saludar():
    print("¡Hola!")

saludar()
# Output:
# Antes de la función
# ¡Hola!
# Después de la función
```

**Decorador con argumentos:**
```python
def decorador(func):
    def wrapper(*args, **kwargs):
        print(f"Llamando a {func.__name__}")
        resultado = func(*args, **kwargs)
        print(f"Resultado: {resultado}")
        return resultado
    return wrapper

@decorador
def sumar(a, b):
    return a + b

sumar(3, 5)
```

**Decoradores útiles:**
```python
import time

def cronometrar(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"{func.__name__} tomó {fin - inicio:.4f} segundos")
        return resultado
    return wrapper

@cronometrar
def operacion_lenta():
    time.sleep(1)
    return "Completado"

operacion_lenta()
```

### 2. Generadores

Los generadores producen valores sobre demanda, ahorrando memoria:

```python
# Función normal (crea lista completa en memoria)
def numeros_cuadrados(n):
    resultado = []
    for i in range(n):
        resultado.append(i ** 2)
    return resultado

# Generador (crea valores uno a uno)
def numeros_cuadrados_gen(n):
    for i in range(n):
        yield i ** 2

# Usar generador
for cuadrado in numeros_cuadrados_gen(5):
    print(cuadrado)  # 0, 1, 4, 9, 16
```

**Generator expressions:**
```python
# Similar a list comprehension pero con ()
cuadrados = (x ** 2 for x in range(10))
print(next(cuadrados))  # 0
print(next(cuadrados))  # 1

# Útil para grandes datasets
suma = sum(x ** 2 for x in range(1000000))
```

**Ejemplo práctico:**
```python
def leer_archivo_grande(archivo):
    """Lee archivo línea por línea sin cargar todo en memoria"""
    with open(archivo, 'r') as f:
        for linea in f:
            yield linea.strip()

# Usar
for linea in leer_archivo_grande("datos.txt"):
    procesar(linea)
```

### 3. Context Managers

Ya usaste `with` para archivos. Puedes crear tus propios context managers:

```python
class MiContextManager:
    def __enter__(self):
        print("Entrando al contexto")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saliendo del contexto")
        return False  # Propaga excepciones

with MiContextManager() as cm:
    print("Dentro del contexto")

# Output:
# Entrando al contexto
# Dentro del contexto
# Saliendo del contexto
```

**Con decorador contextlib:**
```python
from contextlib import contextmanager

@contextmanager
def cronometro():
    inicio = time.time()
    yield
    fin = time.time()
    print(f"Tiempo: {fin - inicio:.4f}s")

with cronometro():
    # Código a medir
    time.sleep(1)
```

### 4. *args y **kwargs

Para funciones con argumentos variables:

```python
# *args: Argumentos posicionales variables
def sumar_todos(*args):
    return sum(args)

print(sumar_todos(1, 2, 3))  # 6
print(sumar_todos(1, 2, 3, 4, 5))  # 15

# **kwargs: Argumentos nombrados variables
def imprimir_info(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

imprimir_info(nombre="Ana", edad=25, ciudad="Madrid")

# Combinados
def funcion_completa(arg1, arg2, *args, kwarg1="default", **kwargs):
    print(f"arg1: {arg1}")
    print(f"arg2: {arg2}")
    print(f"args: {args}")
    print(f"kwarg1: {kwarg1}")
    print(f"kwargs: {kwargs}")

funcion_completa(1, 2, 3, 4, 5, kwarg1="personalizado", extra="dato")
```

**Desempaquetar:**
```python
# Desempaquetar lista
numeros = [1, 2, 3, 4, 5]
print(*numeros)  # 1 2 3 4 5

# Desempaquetar diccionario
datos = {"nombre": "Ana", "edad": 25}
imprimir_info(**datos)
```

### 5. Type Hints (Anotaciones de Tipo)

```python
def saludar(nombre: str) -> str:
    return f"Hola {nombre}"

def sumar(a: int, b: int) -> int:
    return a + b

# Tipos más complejos
from typing import List, Dict, Optional, Union

def procesar_lista(items: List[int]) -> List[int]:
    return [x * 2 for x in items]

def buscar_usuario(id: int) -> Optional[Dict[str, str]]:
    # Puede retornar Dict o None
    if id == 1:
        return {"nombre": "Ana", "email": "ana@example.com"}
    return None

def convertir(valor: Union[int, str]) -> str:
    # Puede recibir int o str
    return str(valor)
```

### 6. Expresiones Regulares

Para búsqueda de patrones en texto:

```python
import re

# Buscar patrón
texto = "Mi email es ana@example.com"
patron = r'\w+@\w+\.\w+'
match = re.search(patron, texto)
if match:
    print(match.group())  # ana@example.com

# Encontrar todos
texto = "Los números son: 123, 456, 789"
numeros = re.findall(r'\d+', texto)
print(numeros)  # ['123', '456', '789']

# Reemplazar
texto = "Hola mundo, mundo cruel"
nuevo = re.sub(r'mundo', 'Python', texto)
print(nuevo)  # Hola Python, Python cruel

# Dividir
texto = "uno,dos,tres,cuatro"
partes = re.split(r',', texto)
print(partes)  # ['uno', 'dos', 'tres', 'cuatro']
```

**Patrones comunes:**
```python
# Email
email_patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

# Teléfono (formato: 123-456-7890)
telefono_patron = r'^\d{3}-\d{3}-\d{4}$'

# URL
url_patron = r'https?://[\w\.-]+\.\w+'

# Validar
def validar_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(patron, email) is not None
```

### 7. Funciones Lambda Avanzadas

```python
# Lambda con map
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))

# Lambda con filter
pares = list(filter(lambda x: x % 2 == 0, numeros))

# Lambda con reduce
from functools import reduce
suma = reduce(lambda x, y: x + y, numeros)

# Lambda en sorted
personas = [
    {"nombre": "Ana", "edad": 25},
    {"nombre": "Carlos", "edad": 30},
    {"nombre": "Elena", "edad": 22}
]
ordenado = sorted(personas, key=lambda p: p["edad"])
```

### 8. Comprehensions Avanzadas

```python
# Nested comprehension
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
plana = [num for fila in matriz for num in fila]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Comprehension con if/else
numeros = [1, 2, 3, 4, 5]
resultado = ["par" if x % 2 == 0 else "impar" for x in numeros]

# Dict comprehension avanzada
palabras = ["hola", "mundo", "python"]
longitudes = {palabra: len(palabra) for palabra in palabras}

# Set comprehension con filtro
cuadrados_pares = {x ** 2 for x in range(10) if x % 2 == 0}
```

## Implementación Práctica

### Ejemplo 1: Sistema de Caché con Decorador

```python
def cache(func):
    resultados = {}
    def wrapper(*args):
        if args in resultados:
            print(f"Usando caché para {args}")
            return resultados[args]
        resultado = func(*args)
        resultados[args] = resultado
        return resultado
    return wrapper

@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Calcula
print(fibonacci(10))  # Usa caché
```

### Ejemplo 2: Procesador de Logs con Generador

```python
def procesar_logs(archivo):
    """Procesa logs grandes línea por línea"""
    with open(archivo, 'r') as f:
        for linea in f:
            if 'ERROR' in linea:
                yield linea.strip()

def contar_errores_por_tipo(archivo):
    errores = {}
    for log in procesar_logs(archivo):
        tipo = log.split(':')[0]
        errores[tipo] = errores.get(tipo, 0) + 1
    return errores
```

## Mejores Prácticas

1. **Usa type hints para código más claro**
   ```python
   def calcular(x: int, y: int) -> int:
       return x + y
   ```

2. **Generadores para grandes datasets**
   ```python
   # ✅ Eficiente en memoria
   datos = (procesar(x) for x in range(1000000))
   ```

3. **Decoradores para funcionalidad transversal**
   ```python
   @autenticar
   @registrar
   def funcion_sensible():
       pass
   ```

## Conceptos clave para recordar

- 🔑 **Decoradores**: Modifican funciones
- 🔑 **Generadores**: Producen valores sobre demanda
- 🔑 **yield**: Crea generador
- 🔑 **Context managers**: Gestionan recursos
- 🔑 ***args/**kwargs**: Argumentos variables
- 🔑 **Type hints**: Anotaciones de tipo
- 🔑 **Regex**: Patrones de texto

## Próximos pasos

En el Módulo 10 aprenderás sobre:
- Proyectos completos
- Buenas prácticas de código
- Testing
- Documentación
- Deployment

**¡Ya dominas Python a nivel avanzado! 🎉**
