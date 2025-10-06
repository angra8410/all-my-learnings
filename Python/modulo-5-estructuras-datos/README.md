# Módulo 5: Estructuras de Datos

## Introducción

¡Bienvenido al Módulo 5! Hasta ahora has trabajado con variables individuales. Ahora aprenderás a manejar **colecciones de datos**: grupos de elementos organizados de diferentes formas.

En este módulo aprenderás:
- **Listas**: Colecciones ordenadas y modificables
- **Tuplas**: Colecciones ordenadas e inmutables
- **Diccionarios**: Pares clave-valor
- **Sets (Conjuntos)**: Colecciones sin duplicados

## ¿Por qué es importante?

Las estructuras de datos te permiten:
- Almacenar múltiples valores relacionados
- Organizar información eficientemente
- Procesar grandes cantidades de datos
- Crear programas más complejos y útiles

**Analogía:** Es como tener diferentes tipos de contenedores:
- **Lista**: Una caja de zapatos numerada (orden importante, puedes cambiar contenido)
- **Tupla**: Una cápsula del tiempo sellada (orden fijo, no modificable)
- **Diccionario**: Una agenda telefónica (nombre → número)
- **Set**: Una bolsa de canicas únicas (sin duplicados)

## Conceptos Principales

### 1. Listas

Las listas son colecciones ordenadas y modificables.

**Crear listas:**
```python
# Lista vacía
numeros = []
frutas = list()

# Lista con elementos
colores = ["rojo", "azul", "verde"]
numeros = [1, 2, 3, 4, 5]
mixta = [1, "hola", True, 3.14]  # Puede mezclar tipos
```

**Acceder a elementos:**
```python
frutas = ["manzana", "banana", "naranja"]
#          0          1         2         (índices positivos)
#         -3         -2        -1         (índices negativos)

print(frutas[0])   # manzana
print(frutas[-1])  # naranja (último)
print(frutas[1:3]) # ['banana', 'naranja'] (slicing)
```

**Modificar listas:**
```python
frutas = ["manzana", "banana", "naranja"]

# Cambiar elemento
frutas[1] = "pera"  # ['manzana', 'pera', 'naranja']

# Agregar al final
frutas.append("uva")  # ['manzana', 'pera', 'naranja', 'uva']

# Insertar en posición
frutas.insert(1, "fresa")  # ['manzana', 'fresa', 'pera', 'naranja', 'uva']

# Eliminar por valor
frutas.remove("pera")  # Elimina la primera ocurrencia

# Eliminar por índice
del frutas[0]  # Elimina 'manzana'
eliminado = frutas.pop()  # Elimina y retorna el último

# Limpiar lista
frutas.clear()  # []
```

**Operaciones útiles:**
```python
numeros = [3, 1, 4, 1, 5, 9, 2, 6]

# Longitud
len(numeros)  # 8

# Ordenar
numeros.sort()  # [1, 1, 2, 3, 4, 5, 6, 9] (modifica original)
sorted(numeros)  # Retorna nueva lista ordenada

# Invertir
numeros.reverse()  # Invierte in-place

# Contar
numeros.count(1)  # 2 (aparece 2 veces)

# Encontrar índice
numeros.index(4)  # 2 (posición del 4)

# Verificar existencia
4 in numeros  # True
10 in numeros  # False
```

**Iterar sobre listas:**
```python
frutas = ["manzana", "banana", "naranja"]

# Forma simple
for fruta in frutas:
    print(fruta)

# Con índice
for i, fruta in enumerate(frutas):
    print(f"{i}: {fruta}")
```

### 2. Tuplas

Tuplas son como listas pero **inmutables** (no se pueden modificar).

```python
# Crear tuplas
coordenadas = (10, 20)
colores = ("rojo", "azul", "verde")
un_elemento = (42,)  # Coma necesaria para tupla de 1 elemento

# Acceder
print(coordenadas[0])  # 10
print(colores[1:])     # ('azul', 'verde')

# NO se puede modificar
# coordenadas[0] = 15  # ❌ ERROR

# Desempaquetar
x, y = coordenadas  # x=10, y=20
r, g, b = colores   # r='rojo', g='azul', b='verde'

# Operaciones
len(coordenadas)  # 2
10 in coordenadas # True
```

**¿Cuándo usar tuplas?**
- Datos que no deben cambiar (coordenadas, fechas)
- Retornar múltiples valores de funciones
- Claves de diccionarios (listas no pueden)

### 3. Diccionarios

Diccionarios almacenan pares **clave: valor**.

```python
# Crear diccionarios
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid"
}

# Diccionario vacío
vacio = {}
vacio = dict()

# Acceder a valores
print(persona["nombre"])  # Ana
print(persona.get("edad"))  # 25
print(persona.get("telefono", "No disponible"))  # Default si no existe

# Modificar/Agregar
persona["edad"] = 26  # Modificar
persona["email"] = "ana@email.com"  # Agregar nueva clave

# Eliminar
del persona["ciudad"]
email = persona.pop("email")  # Elimina y retorna valor

# Verificar existencia de clave
"nombre" in persona  # True
"telefono" in persona  # False
```

**Iterar sobre diccionarios:**
```python
persona = {"nombre": "Ana", "edad": 25, "ciudad": "Madrid"}

# Solo claves
for clave in persona:
    print(clave)

# Solo valores
for valor in persona.values():
    print(valor)

# Claves y valores
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
```

**Diccionarios anidados:**
```python
estudiantes = {
    "est001": {
        "nombre": "Ana",
        "notas": [8, 9, 7]
    },
    "est002": {
        "nombre": "Carlos",
        "notas": [6, 7, 8]
    }
}

print(estudiantes["est001"]["nombre"])  # Ana
print(estudiantes["est002"]["notas"][0])  # 6
```

### 4. Sets (Conjuntos)

Sets son colecciones **sin orden** y **sin duplicados**.

```python
# Crear sets
numeros = {1, 2, 3, 4, 5}
colores = set(["rojo", "azul", "rojo"])  # {'rojo', 'azul'} (elimina duplicados)

# Agregar/Eliminar
numeros.add(6)
numeros.remove(3)  # Error si no existe
numeros.discard(3)  # No da error si no existe

# Operaciones de conjuntos
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Unión
a | b  # {1, 2, 3, 4, 5, 6}
a.union(b)

# Intersección
a & b  # {3, 4}
a.intersection(b)

# Diferencia
a - b  # {1, 2} (en a pero no en b)
a.difference(b)

# Verificar
3 in a  # True
```

**¿Cuándo usar sets?**
- Eliminar duplicados de una lista
- Operaciones matemáticas de conjuntos
- Búsquedas rápidas (más eficiente que listas)

### 5. Comprensiones (List/Dict Comprehensions)

Forma concisa de crear estructuras de datos:

```python
# Comprensión de listas
cuadrados = [x**2 for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

pares = [x for x in range(20) if x % 2 == 0]
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Comprensión de diccionarios
numeros_cuadrados = {x: x**2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Comprensión de sets
letras_unicas = {letra for letra in "programming"}
# {'a', 'g', 'i', 'm', 'n', 'o', 'p', 'r'}
```

## Implementación Práctica

### Ejemplo 1: Gestión de Contactos

```python
contactos = {}

def agregar_contacto(nombre, telefono):
    contactos[nombre] = telefono
    print(f"✓ {nombre} agregado")

def buscar_contacto(nombre):
    if nombre in contactos:
        print(f"{nombre}: {contactos[nombre]}")
    else:
        print("Contacto no encontrado")

def listar_contactos():
    for nombre, telefono in contactos.items():
        print(f"{nombre}: {telefono}")

# Usar
agregar_contacto("Ana", "555-1234")
agregar_contacto("Carlos", "555-5678")
buscar_contacto("Ana")
listar_contactos()
```

### Ejemplo 2: Estadísticas de Notas

```python
notas = [8, 7, 9, 6, 8, 10, 7, 8]

promedio = sum(notas) / len(notas)
maxima = max(notas)
minima = min(notas)

print(f"Promedio: {promedio:.2f}")
print(f"Nota máxima: {maxima}")
print(f"Nota mínima: {minima}")
print(f"Total de exámenes: {len(notas)}")
```

### Ejemplo 3: Inventario de Tienda

```python
inventario = {
    "manzanas": {"precio": 1.50, "stock": 100},
    "bananas": {"precio": 0.80, "stock": 150},
    "naranjas": {"precio": 2.00, "stock": 80}
}

def mostrar_inventario():
    for producto, datos in inventario.items():
        print(f"{producto.capitalize()}")
        print(f"  Precio: ${datos['precio']}")
        print(f"  Stock: {datos['stock']} unidades")

def vender_producto(producto, cantidad):
    if producto in inventario:
        if inventario[producto]["stock"] >= cantidad:
            inventario[producto]["stock"] -= cantidad
            total = inventario[producto]["precio"] * cantidad
            print(f"Venta exitosa. Total: ${total:.2f}")
        else:
            print("Stock insuficiente")
    else:
        print("Producto no encontrado")

mostrar_inventario()
vender_producto("manzanas", 10)
```

## Mejores Prácticas

1. **Elige la estructura correcta**
   - Lista: Orden importa, datos modificables
   - Tupla: Datos fijos
   - Diccionario: Búsqueda por clave
   - Set: Eliminar duplicados, operaciones de conjuntos

2. **Usa comprensiones para código conciso**
   ```python
   # ✅ Legible
   cuadrados = [x**2 for x in range(10)]
   
   # ❌ Más verboso
   cuadrados = []
   for x in range(10):
       cuadrados.append(x**2)
   ```

3. **Usa get() con diccionarios**
   ```python
   # ✅ Seguro
   valor = diccionario.get("clave", "default")
   
   # ❌ Puede dar error
   valor = diccionario["clave"]
   ```

## Conceptos clave para recordar

- 🔑 **Lista**: Ordenada, modificable, con duplicados
- 🔑 **Tupla**: Ordenada, inmutable
- 🔑 **Diccionario**: Pares clave-valor
- 🔑 **Set**: Sin orden, sin duplicados
- 🔑 **append()**: Agregar a lista
- 🔑 **pop()**: Eliminar y retornar
- 🔑 **items()**: Iterar sobre diccionario

## Próximos pasos

En el Módulo 6 aprenderás sobre:
- Leer y escribir archivos
- Manejo de errores con try/except
- Context managers (with)

**¡Ya puedes trabajar con colecciones de datos complejas! 🎉**
