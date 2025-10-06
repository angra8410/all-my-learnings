# Módulo 3: Estructuras de Control

## Introducción

¡Bienvenido al Módulo 3! Hasta ahora tus programas ejecutan líneas secuencialmente, de arriba a abajo. Ahora aprenderás a:
- **Tomar decisiones** con `if`, `elif`, `else`
- **Repetir acciones** con `for` y `while`
- **Controlar el flujo** con `break`, `continue`, `pass`

En este módulo aprenderás:
- Condicionales (if/elif/else)
- Bucles for
- Bucles while
- Control de flujo avanzado

## ¿Por qué es importante?

Sin estructuras de control, tus programas serían como robots que solo siguen instrucciones fijas. Con ellas, puedes:
- Validar datos del usuario
- Repetir tareas automáticamente
- Crear menús interactivos
- Procesar listas de elementos
- ¡Crear juegos!

**Analogía:** Es como agregar cerebro a tu programa. Ahora puede pensar ("si esto, entonces aquello") y repetir tareas ("haz esto 10 veces").

## Conceptos Principales

### 1. Condicionales: if, elif, else

Los condicionales permiten ejecutar código solo si se cumple una condición.

**Sintaxis básica:**
```python
if condicion:
    # código que se ejecuta si es True
    print("Condición cumplida")
```

**Ejemplo simple:**
```python
edad = 18

if edad >= 18:
    print("Eres mayor de edad")
```

**if-else (dos opciones):**
```python
edad = 16

if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

**if-elif-else (múltiples opciones):**
```python
nota = 85

if nota >= 90:
    print("Calificación: A")
elif nota >= 80:
    print("Calificación: B")
elif nota >= 70:
    print("Calificación: C")
elif nota >= 60:
    print("Calificación: D")
else:
    print("Calificación: F")
```

**⚠️ Importante:** La indentación (espacios) es OBLIGATORIA en Python.

```python
# ✅ Correcto
if True:
    print("Hola")  # 4 espacios de indentación

# ❌ Error
if True:
print("Hola")  # Sin indentación = ERROR
```

**Condiciones compuestas:**
```python
edad = 25
tiene_licencia = True

# AND (ambas deben ser True)
if edad >= 18 and tiene_licencia:
    print("Puedes conducir")

# OR (al menos una debe ser True)
if edad < 18 or not tiene_licencia:
    print("No puedes conducir")
```

**Condicionales anidados:**
```python
edad = 25
tiene_dinero = True

if edad >= 18:
    if tiene_dinero:
        print("Puedes entrar al casino")
    else:
        print("Eres mayor pero no tienes dinero")
else:
    print("Eres menor de edad")
```

### 2. Bucle for: Repetir con Iteración

El bucle `for` repite código un número definido de veces o para cada elemento de una secuencia.

**Sintaxis básica:**
```python
for variable in secuencia:
    # código a repetir
```

**Ejemplo con range():**
```python
# Imprime números del 0 al 4
for i in range(5):
    print(i)
# Output: 0, 1, 2, 3, 4

# Del 1 al 5
for i in range(1, 6):
    print(i)
# Output: 1, 2, 3, 4, 5

# De 2 en 2
for i in range(0, 10, 2):
    print(i)
# Output: 0, 2, 4, 6, 8
```

**Iterar sobre strings:**
```python
nombre = "Python"
for letra in nombre:
    print(letra)
# Output: P, y, t, h, o, n (uno por línea)
```

**Iterar sobre listas:**
```python
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print(f"Me gusta la {fruta}")
```

**Bucles anidados:**
```python
# Tabla de multiplicar
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
```

### 3. Bucle while: Repetir con Condición

El bucle `while` repite mientras una condición sea verdadera.

**Sintaxis:**
```python
while condicion:
    # código a repetir
```

**Ejemplo básico:**
```python
contador = 0
while contador < 5:
    print(contador)
    contador += 1
# Output: 0, 1, 2, 3, 4
```

**Validación de input:**
```python
contraseña = ""
while contraseña != "python123":
    contraseña = input("Ingresa la contraseña: ")
print("¡Acceso concedido!")
```

**⚠️ Cuidado con bucles infinitos:**
```python
# ❌ NUNCA TERMINA (bucle infinito)
while True:
    print("Esto nunca para")

# ✅ Con condición de salida
while True:
    respuesta = input("¿Continuar? (s/n): ")
    if respuesta == "n":
        break  # Sale del bucle
```

### 4. break, continue y pass

**break:** Sale del bucle inmediatamente
```python
for i in range(10):
    if i == 5:
        break  # Sale cuando i es 5
    print(i)
# Output: 0, 1, 2, 3, 4
```

**continue:** Salta a la siguiente iteración
```python
for i in range(5):
    if i == 2:
        continue  # Salta el 2
    print(i)
# Output: 0, 1, 3, 4
```

**pass:** No hace nada (placeholder)
```python
for i in range(5):
    if i == 2:
        pass  # Por ahora no hace nada, pero no da error
    print(i)
# Output: 0, 1, 2, 3, 4
```

### 5. Comprensión de Listas (Avanzado)

Una forma compacta de crear listas:

```python
# Forma tradicional
cuadrados = []
for i in range(5):
    cuadrados.append(i ** 2)
# [0, 1, 4, 9, 16]

# Comprensión de lista (una línea)
cuadrados = [i ** 2 for i in range(5)]
# [0, 1, 4, 9, 16]

# Con condición
pares = [i for i in range(10) if i % 2 == 0]
# [0, 2, 4, 6, 8]
```

## Implementación Práctica

### Ejemplo 1: Verificador de Edad

```python
print("=== VERIFICADOR DE EDAD ===")
edad = int(input("¿Cuántos años tienes? "))

if edad < 0:
    print("Edad inválida")
elif edad < 13:
    print("Eres un niño")
elif edad < 18:
    print("Eres adolescente")
elif edad < 65:
    print("Eres adulto")
else:
    print("Eres adulto mayor")
```

### Ejemplo 2: Tabla de Multiplicar

```python
numero = int(input("¿Qué tabla quieres? "))

print(f"\nTabla del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
```

### Ejemplo 3: Adivina el Número

```python
import random

numero_secreto = random.randint(1, 10)
intentos = 0

print("=== ADIVINA EL NÚMERO (1-10) ===")

while True:
    intento = int(input("Tu número: "))
    intentos += 1
    
    if intento == numero_secreto:
        print(f"¡Correcto! Lo adivinaste en {intentos} intentos")
        break
    elif intento < numero_secreto:
        print("Muy bajo, intenta de nuevo")
    else:
        print("Muy alto, intenta de nuevo")
```

### Ejemplo 4: Menú Interactivo

```python
while True:
    print("\n=== MENÚ PRINCIPAL ===")
    print("1. Saludar")
    print("2. Despedirse")
    print("3. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "1":
        nombre = input("¿Cómo te llamas? ")
        print(f"¡Hola {nombre}!")
    elif opcion == "2":
        print("¡Hasta luego!")
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida")
```

## Mejores Prácticas

1. **Evita bucles infinitos**
   ```python
   # ✅ Siempre ten una forma de salir
   while condicion:
       # ...
       if algo:
           break
   ```

2. **Usa for cuando sabes cuántas iteraciones**
   ```python
   # ✅ For cuando conoces la cantidad
   for i in range(10):
       print(i)
   
   # ✅ While cuando depende de una condición
   while usuario_activo:
       # ...
   ```

3. **Indentación consistente (4 espacios)**
   ```python
   # ✅ Usa siempre 4 espacios
   if True:
       print("Correcto")
   ```

4. **Nombres descriptivos en bucles**
   ```python
   # ✅ Bien
   for estudiante in estudiantes:
       print(estudiante)
   
   # ❌ Menos claro
   for x in estudiantes:
       print(x)
   ```

## Conceptos clave para recordar

- 🔑 **if/elif/else**: Tomar decisiones en el código
- 🔑 **for**: Repetir un número conocido de veces
- 🔑 **while**: Repetir mientras una condición sea verdadera
- 🔑 **break**: Salir de un bucle inmediatamente
- 🔑 **continue**: Saltar a la siguiente iteración
- 🔑 **Indentación**: Obligatoria en Python (4 espacios)
- 🔑 **range()**: Genera secuencias de números

## Próximos pasos

En el Módulo 4 aprenderás sobre:
- Funciones (crear tu propio código reutilizable)
- Módulos (organizar código en archivos)
- Parámetros y retorno de valores

**¿Qué necesitas saber antes de continuar?**
✅ Usar if/elif/else correctamente  
✅ Crear bucles for y while  
✅ Entender break y continue  
✅ Respetar la indentación  

**¡Ya puedes crear programas que piensan y repiten! 🎉**
