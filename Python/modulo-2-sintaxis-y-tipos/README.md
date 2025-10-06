# Módulo 2: Sintaxis y Tipos de Datos en Python

## Introducción

Bienvenido al Módulo 2. Ya sabes ejecutar Python y usar `print()`. Ahora aprenderás a **guardar información** y trabajar con diferentes **tipos de datos**. Es como aprender a usar diferentes contenedores en la cocina: tienes frascos para líquidos, cajas para sólidos, y cada uno tiene un propósito.

En este módulo aprenderás:
- Variables (cómo guardar información)
- Tipos de datos básicos (números, texto, booleanos)
- Operadores
- Conversión entre tipos
- Input del usuario

## ¿Por qué es importante?

Sin variables, solo podrías mostrar texto fijo. Con variables, puedes:
- Guardar el nombre del usuario y usarlo en todo el programa
- Hacer cálculos complejos
- Tomar decisiones basadas en datos
- Crear programas interactivos

**Analogía:** Es la diferencia entre una calculadora que solo muestra "5" y una que puede hacer `edad = 25` y luego calcular `edad + 10`.

## Conceptos Principales

### 1. Variables: Cajas para Guardar Información

Una **variable** es como una caja etiquetada donde guardas un valor.

```python
nombre = "Ana"
edad = 25
altura = 1.65
es_estudiante = True
```

**Analogía del mundo real:**

Imagina tu closet con cajas:
- Caja "Zapatos" → contiene zapatos
- Caja "Libros" → contiene libros
- Caja "nombre" → contiene "Ana"
- Caja "edad" → contiene 25

**Reglas para nombrar variables:**

✅ **Correcto:**
```python
nombre = "Juan"
edad_usuario = 30
precio_total = 99.99
numero1 = 10
mi_variable = "Hola"
```

❌ **Incorrecto:**
```python
1nombre = "Juan"     # No puede empezar con número
mi-variable = "Hola" # No puede tener guiones
print = 5            # No usar palabras reservadas de Python
mi variable = 10     # No puede tener espacios
```

**Convenciones (no obligatorias, pero recomendadas):**
```python
# snake_case para variables (Python estilo)
nombre_completo = "Ana García"
precio_con_iva = 100

# MAYUSCULAS para constantes
PI = 3.14159
MAX_INTENTOS = 3
```

### 2. Tipos de Datos Básicos

Python tiene varios tipos de datos. Los más importantes son:

#### 2.1 Strings (Cadenas de texto)

```python
nombre = "Ana"
apellido = 'García'  # Comillas simples o dobles
mensaje = """Este es un
mensaje de
varias líneas"""

# Concatenación (unir strings)
nombre_completo = nombre + " " + apellido  # "Ana García"

# Repetición
saludo = "Hola " * 3  # "Hola Hola Hola "

# Longitud
longitud = len(nombre)  # 3
```

**Métodos útiles de strings:**
```python
texto = "Python es Genial"

print(texto.upper())      # "PYTHON ES GENIAL"
print(texto.lower())      # "python es genial"
print(texto.replace("Genial", "Increíble"))  # "Python es Increíble"
print(texto.split())      # ['Python', 'es', 'Genial']
print(texto.count("e"))   # 2 (cuántas veces aparece 'e')
```

**Indexing (acceder a caracteres):**
```python
palabra = "Python"
#          012345  (índices positivos)
#         -654321  (índices negativos)

print(palabra[0])    # 'P' (primer caracter)
print(palabra[5])    # 'n' (último caracter)
print(palabra[-1])   # 'n' (último, forma corta)
print(palabra[0:3])  # 'Pyt' (del 0 al 2, NO incluye 3)
print(palabra[2:])   # 'thon' (del 2 al final)
print(palabra[:4])   # 'Pyth' (del inicio al 3)
```

#### 2.2 Números Enteros (int)

```python
edad = 25
temperatura = -10
año = 2024

# Operaciones
suma = 10 + 5        # 15
resta = 10 - 5       # 5
multiplicacion = 10 * 5  # 50
division = 10 / 3    # 3.333... (siempre retorna float)
division_entera = 10 // 3  # 3 (descarta decimales)
modulo = 10 % 3      # 1 (resto de la división)
potencia = 2 ** 3    # 8 (2 elevado a 3)
```

**Ejemplo práctico:**
```python
# ¿Es un número par?
numero = 8
es_par = (numero % 2 == 0)  # True si es par
```

#### 2.3 Números Decimales (float)

```python
precio = 19.99
pi = 3.14159
temperatura = -2.5

# Cuidado con la precisión
resultado = 0.1 + 0.2  # 0.30000000000000004 (error de punto flotante)

# Redondear
print(round(3.14159, 2))  # 3.14 (2 decimales)
```

#### 2.4 Booleanos (bool)

```python
es_estudiante = True
tiene_licencia = False

# Operadores lógicos
print(True and True)   # True
print(True and False)  # False
print(True or False)   # True
print(not True)        # False

# Comparaciones (retornan booleanos)
print(5 > 3)     # True
print(5 < 3)     # False
print(5 == 5)    # True (igualdad)
print(5 != 3)    # True (diferente)
print(5 >= 5)    # True (mayor o igual)
```

### 3. Conversión de Tipos (Type Casting)

A veces necesitas convertir un tipo en otro:

```python
# String a número
edad_texto = "25"
edad_numero = int(edad_texto)     # 25 (int)
precio_texto = "19.99"
precio_numero = float(precio_texto)  # 19.99 (float)

# Número a string
edad = 25
edad_texto = str(edad)  # "25"

# A booleano
print(bool(1))      # True
print(bool(0))      # False
print(bool(""))     # False (string vacío)
print(bool("Hola")) # True (string con contenido)
```

**Ejemplo práctico:**
```python
edad = input("¿Cuántos años tienes? ")  # input() siempre retorna string
edad_numero = int(edad)  # Convertir a número
print("El próximo año tendrás", edad_numero + 1, "años")
```

### 4. Input del Usuario

```python
# Pedir información al usuario
nombre = input("¿Cómo te llamas? ")
print("Hola", nombre)

# Recuerda: input() SIEMPRE retorna string
edad = input("¿Cuántos años tienes? ")  # Esto es string "25"
edad = int(edad)  # Ahora es número 25
```

**Ejemplo completo:**
```python
print("=== CALCULADORA DE EDAD ===")
nombre = input("Nombre: ")
edad = int(input("Edad actual: "))

print("\nHola", nombre)
print("Tienes", edad, "años")
print("En 10 años tendrás", edad + 10, "años")
print("Hace 5 años tenías", edad - 5, "años")
```

### 5. F-strings (Formateo Moderno)

La forma más moderna y legible de formatear strings:

```python
nombre = "Ana"
edad = 25

# Forma antigua
print("Hola, soy " + nombre + " y tengo " + str(edad) + " años")

# Forma moderna (f-strings) - ¡Mucho mejor!
print(f"Hola, soy {nombre} y tengo {edad} años")

# Con expresiones
precio = 100
print(f"Con IVA: ${precio * 1.16}")

# Con formato
pi = 3.14159
print(f"Pi redondeado: {pi:.2f}")  # 3.14
```

### 6. Operadores Avanzados

```python
# Operadores de asignación compuestos
x = 10
x += 5   # x = x + 5  → 15
x -= 3   # x = x - 3  → 12
x *= 2   # x = x * 2  → 24
x /= 4   # x = x / 4  → 6.0

# Comparaciones encadenadas
edad = 25
print(18 < edad < 65)  # True (equivale a: edad > 18 and edad < 65)

# Operador ternario
edad = 20
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
```

## Implementación Práctica

### Ejemplo 1: Conversor de Temperatura

```python
print("=== CONVERSOR CELSIUS A FAHRENHEIT ===")
celsius = float(input("Temperatura en Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C = {fahrenheit}°F")
```

### Ejemplo 2: Calculadora de Propina

```python
print("=== CALCULADORA DE PROPINA ===")
cuenta = float(input("Total de la cuenta: $"))
porcentaje = float(input("Porcentaje de propina (10, 15, 20): "))

propina = cuenta * (porcentaje / 100)
total = cuenta + propina

print(f"\nCuenta: ${cuenta:.2f}")
print(f"Propina ({porcentaje}%): ${propina:.2f}")
print(f"Total a pagar: ${total:.2f}")
```

### Ejemplo 3: Datos Personales

```python
print("=== FORMULARIO DE REGISTRO ===")
nombre = input("Nombre completo: ")
edad = int(input("Edad: "))
altura = float(input("Altura en metros: "))
es_estudiante = input("¿Eres estudiante? (si/no): ").lower() == "si"

print("\n=== RESUMEN ===")
print(f"Nombre: {nombre}")
print(f"Edad: {edad} años")
print(f"Altura: {altura}m")
print(f"Estudiante: {'Sí' if es_estudiante else 'No'}")
```

## Mejores Prácticas

1. **Nombres descriptivos**
   ```python
   # ✅ Bien
   precio_con_iva = 100 * 1.16
   
   # ❌ Mal
   p = 100 * 1.16
   ```

2. **Un tipo por variable**
   ```python
   # Evita cambiar el tipo de una variable
   edad = 25      # int
   edad = "25"    # Ahora string - confuso!
   ```

3. **Usa f-strings para formateo**
   ```python
   # ✅ Moderno y legible
   print(f"Hola {nombre}, tienes {edad} años")
   
   # ❌ Antiguo
   print("Hola " + nombre + ", tienes " + str(edad) + " años")
   ```

4. **Valida input del usuario**
   ```python
   try:
       edad = int(input("Edad: "))
   except:
       print("Debes ingresar un número")
   ```

5. **Constantes en MAYÚSCULAS**
   ```python
   IVA = 0.16
   MAX_INTENTOS = 3
   PI = 3.14159
   ```

## Conceptos clave para recordar

- 🔑 **Variable**: Caja para guardar un valor con un nombre
- 🔑 **String**: Texto entre comillas ("Hola" o 'Hola')
- 🔑 **int**: Números enteros (1, 2, -5, 100)
- 🔑 **float**: Números decimales (3.14, 19.99)
- 🔑 **bool**: True o False
- 🔑 **input()**: Obtener información del usuario (siempre retorna string)
- 🔑 **type()**: Ver el tipo de una variable
- 🔑 **f-strings**: Formateo moderno con f"Hola {variable}"

## Próximos pasos

En el Módulo 3 aprenderás sobre:
- Condicionales (if, elif, else)
- Bucles (for, while)
- Control de flujo

**¿Qué necesitas saber antes de continuar?**
✅ Crear y usar variables  
✅ Diferenciar tipos de datos  
✅ Convertir entre tipos  
✅ Usar input() y f-strings  
✅ Operaciones básicas con cada tipo  

## Tabla de Referencia Rápida

| Tipo | Ejemplo | Operaciones Comunes |
|------|---------|---------------------|
| `str` | `"Hola"` | `+`, `*`, `.upper()`, `.lower()`, `len()` |
| `int` | `42` | `+`, `-`, `*`, `/`, `//`, `%`, `**` |
| `float` | `3.14` | `+`, `-`, `*`, `/`, `round()` |
| `bool` | `True` | `and`, `or`, `not` |

**¡Sigue practicando! La única forma de aprender programación es programando. 🚀**
