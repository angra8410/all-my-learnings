# Módulo 4: Funciones y Módulos

## Introducción

¡Bienvenido al Módulo 4! Hasta ahora has escrito código línea por línea. Ahora aprenderás a crear **funciones**: bloques de código reutilizables que puedes llamar cuando los necesites.

En este módulo aprenderás:
- Qué son las funciones y por qué usarlas
- Cómo crear funciones con `def`
- Parámetros y argumentos
- Retorno de valores con `return`
- Scope (alcance) de variables
- Módulos y cómo importarlos

## ¿Por qué es importante?

Las funciones te permiten:
- **Reutilizar código**: Escribe una vez, usa muchas veces
- **Organizar mejor**: Divide problemas grandes en partes pequeñas
- **Facilitar mantenimiento**: Cambias en un solo lugar
- **Evitar repetición**: DRY (Don't Repeat Yourself)

**Analogía:** Una función es como una receta de cocina. Una vez que la escribes, puedes usarla siempre que quieras hacer ese plato, sin escribir los pasos cada vez.

## Conceptos Principales

### 1. Crear Funciones con def

**Sintaxis básica:**
```python
def nombre_funcion():
    # código de la función
    print("Hola desde la función")

# Llamar (ejecutar) la función
nombre_funcion()  # Output: Hola desde la función
```

**Ejemplo:**
```python
def saludar():
    print("¡Hola!")
    print("¿Cómo estás?")

saludar()  # Ejecuta la función
saludar()  # Puedes llamarla múltiples veces
```

### 2. Parámetros y Argumentos

Las funciones pueden recibir información (parámetros):

```python
def saludar(nombre):  # nombre es el parámetro
    print(f"¡Hola {nombre}!")

saludar("Ana")     # "Ana" es el argumento
saludar("Carlos")  # "Carlos" es el argumento
```

**Múltiples parámetros:**
```python
def sumar(a, b):
    resultado = a + b
    print(f"{a} + {b} = {resultado}")

sumar(5, 3)   # 5 + 3 = 8
sumar(10, 20) # 10 + 20 = 30
```

**Parámetros por defecto:**
```python
def saludar(nombre="amigo"):  # valor por defecto
    print(f"¡Hola {nombre}!")

saludar()        # ¡Hola amigo!
saludar("Ana")   # ¡Hola Ana!
```

**Argumentos nombrados:**
```python
def presentar(nombre, edad, ciudad):
    print(f"Soy {nombre}, tengo {edad} años y vivo en {ciudad}")

# Orden normal
presentar("Ana", 25, "Madrid")

# Con nombres (orden no importa)
presentar(ciudad="Madrid", nombre="Ana", edad=25)
```

### 3. Retorno de Valores con return

Las funciones pueden devolver valores:

```python
def sumar(a, b):
    return a + b

resultado = sumar(5, 3)  # resultado = 8
print(resultado)  # 8
```

**Diferencia entre print y return:**
```python
# Con print (solo muestra, no guarda)
def sumar_print(a, b):
    print(a + b)

sumar_print(5, 3)  # Imprime 8
x = sumar_print(5, 3)  # x = None (no retorna nada)

# Con return (devuelve el valor)
def sumar_return(a, b):
    return a + b

y = sumar_return(5, 3)  # y = 8
print(y * 2)  # 16 (puedes usar el valor)
```

**Retornar múltiples valores:**
```python
def operaciones(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    return suma, resta, multiplicacion

s, r, m = operaciones(10, 5)
print(s)  # 15
print(r)  # 5
print(m)  # 50
```

**Return early (salida temprana):**
```python
def es_mayor_edad(edad):
    if edad < 18:
        return False  # Sale inmediatamente
    return True

print(es_mayor_edad(20))  # True
print(es_mayor_edad(15))  # False
```

### 4. Scope (Alcance) de Variables

**Variables locales vs globales:**

```python
# Variable global
nombre = "Ana"

def cambiar_nombre():
    nombre = "Carlos"  # Variable local (solo existe aquí)
    print(nombre)  # Carlos

cambiar_nombre()
print(nombre)  # Ana (la global no cambió)
```

**Usando global:**
```python
contador = 0

def incrementar():
    global contador  # Modifica la variable global
    contador += 1

incrementar()
incrementar()
print(contador)  # 2
```

**Mejores prácticas:**
```python
# ✅ Mejor: pasar como parámetro y retornar
contador = 0

def incrementar(valor):
    return valor + 1

contador = incrementar(contador)
contador = incrementar(contador)
print(contador)  # 2
```

### 5. Documentación de Funciones (Docstrings)

```python
def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo.
    
    Args:
        radio (float): El radio del círculo
        
    Returns:
        float: El área del círculo (π * r²)
    """
    import math
    return math.pi * radio ** 2

# Ver la documentación
help(calcular_area_circulo)
```

### 6. Módulos e Importación

**Importar módulos de Python:**
```python
# Importar módulo completo
import math
print(math.pi)  # 3.14159...
print(math.sqrt(16))  # 4.0

# Importar función específica
from math import pi, sqrt
print(pi)  # 3.14159...
print(sqrt(16))  # 4.0

# Importar con alias
import math as m
print(m.pi)

# Importar todo (no recomendado)
from math import *
```

**Módulos útiles:**
```python
# random - Números aleatorios
import random
print(random.randint(1, 10))  # Número entre 1 y 10
print(random.choice(['rojo', 'azul', 'verde']))

# datetime - Fechas y horas
from datetime import datetime
ahora = datetime.now()
print(ahora)

# os - Sistema operativo
import os
print(os.getcwd())  # Directorio actual
```

**Crear tu propio módulo:**

Archivo: `mis_funciones.py`
```python
def saludar(nombre):
    return f"¡Hola {nombre}!"

def sumar(a, b):
    return a + b
```

Archivo: `main.py`
```python
import mis_funciones

print(mis_funciones.saludar("Ana"))
print(mis_funciones.sumar(5, 3))
```

### 7. Funciones Lambda (Anónimas)

Funciones pequeñas de una sola línea:

```python
# Función normal
def cuadrado(x):
    return x ** 2

# Lambda equivalente
cuadrado = lambda x: x ** 2

print(cuadrado(5))  # 25

# Con múltiples parámetros
sumar = lambda a, b: a + b
print(sumar(3, 4))  # 7
```

## Implementación Práctica

### Ejemplo 1: Calculadora de Funciones

```python
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

# Usar las funciones
print(sumar(10, 5))
print(restar(10, 5))
print(multiplicar(10, 5))
print(dividir(10, 5))
```

### Ejemplo 2: Validador de Datos

```python
def validar_email(email):
    """Valida formato básico de email"""
    if '@' in email and '.' in email:
        return True
    return False

def validar_edad(edad):
    """Valida que la edad sea válida"""
    if 0 <= edad <= 120:
        return True
    return False

# Usar
email = input("Email: ")
if validar_email(email):
    print("✓ Email válido")
else:
    print("✗ Email inválido")
```

### Ejemplo 3: Conversor de Temperaturas

```python
def celsius_a_fahrenheit(celsius):
    """Convierte Celsius a Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    """Convierte Fahrenheit a Celsius"""
    return (fahrenheit - 32) * 5/9

# Menú
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")

opcion = input("Opción: ")

if opcion == "1":
    c = float(input("Grados Celsius: "))
    f = celsius_a_fahrenheit(c)
    print(f"{c}°C = {f}°F")
elif opcion == "2":
    f = float(input("Grados Fahrenheit: "))
    c = fahrenheit_a_celsius(f)
    print(f"{f}°F = {c}°C")
```

## Mejores Prácticas

1. **Nombres descriptivos**
   ```python
   # ✅ Bien
   def calcular_promedio(numeros):
       return sum(numeros) / len(numeros)
   
   # ❌ Mal
   def calc(n):
       return sum(n) / len(n)
   ```

2. **Una función, una tarea**
   ```python
   # ✅ Bien (cada función hace una cosa)
   def validar_email(email):
       return '@' in email
   
   def enviar_email(email, mensaje):
       if validar_email(email):
           # enviar
           pass
   ```

3. **Usa docstrings**
   ```python
   def mi_funcion(parametro):
       """Descripción breve de lo que hace"""
       pass
   ```

4. **Retorna valores, no imprimas directamente**
   ```python
   # ✅ Mejor
   def sumar(a, b):
       return a + b
   
   # ❌ Menos flexible
   def sumar(a, b):
       print(a + b)
   ```

## Conceptos clave para recordar

- 🔑 **def**: Define una función
- 🔑 **Parámetros**: Valores que recibe la función
- 🔑 **return**: Devuelve un valor de la función
- 🔑 **Scope**: Alcance de las variables (local vs global)
- 🔑 **Módulo**: Archivo .py con funciones reutilizables
- 🔑 **import**: Importa módulos o funciones
- 🔑 **Docstring**: Documentación de la función

## Próximos pasos

En el Módulo 5 aprenderás sobre:
- Listas y operaciones avanzadas
- Tuplas
- Diccionarios
- Sets (conjuntos)

**¿Qué necesitas saber antes de continuar?**
✅ Crear funciones con def  
✅ Usar parámetros y return  
✅ Importar módulos  
✅ Entender scope de variables  

**¡Ya puedes crear código reutilizable y organizado! 🎉**
