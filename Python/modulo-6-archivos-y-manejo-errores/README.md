# Módulo 6: Archivos y Manejo de Errores

## Introducción

¡Bienvenido al Módulo 6! Hasta ahora tus programas solo trabajan con datos en memoria (se pierden al cerrar el programa). Ahora aprenderás a:
- **Leer y escribir archivos** para persistir datos
- **Manejar errores** para crear programas robustos que no se rompan

En este módulo aprenderás:
- Operaciones con archivos (abrir, leer, escribir, cerrar)
- Manejo de excepciones con try/except
- Context managers con `with`
- Diferentes modos de apertura de archivos
- Trabajar con archivos CSV y JSON

## ¿Por qué es importante?

El manejo de archivos y errores te permite:
- Guardar datos permanentemente (configuraciones, registros, bases de datos simples)
- Procesar archivos de texto, CSV, JSON
- Crear programas que no se rompen con errores inesperados
- Construir aplicaciones profesionales y confiables

**Analogía:** 
- **Archivos**: Como un cuaderno donde escribes notas que permanecen después de cerrar el programa
- **Manejo de errores**: Como usar un paracaídas de emergencia en un avión

## Conceptos Principales

### 1. Leer Archivos

**Abrir y leer archivo completo:**
```python
# Forma básica
archivo = open("datos.txt", "r")  # 'r' = read (leer)
contenido = archivo.read()
print(contenido)
archivo.close()  # ¡Importante cerrar!

# Forma recomendada (con context manager)
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)
# Se cierra automáticamente
```

**Leer línea por línea:**
```python
with open("datos.txt", "r") as archivo:
    # Opción 1: readline()
    linea1 = archivo.readline()
    linea2 = archivo.readline()
    
    # Opción 2: readlines() (todas las líneas en lista)
    lineas = archivo.readlines()
    
    # Opción 3: Iterar (más eficiente)
    for linea in archivo:
        print(linea.strip())  # strip() elimina \n
```

### 2. Escribir Archivos

```python
# Modo 'w' (write) - Sobrescribe el archivo
with open("salida.txt", "w") as archivo:
    archivo.write("Primera línea\n")
    archivo.write("Segunda línea\n")

# Modo 'a' (append) - Agrega al final
with open("salida.txt", "a") as archivo:
    archivo.write("Línea adicional\n")

# Escribir múltiples líneas
lineas = ["Línea 1\n", "Línea 2\n", "Línea 3\n"]
with open("salida.txt", "w") as archivo:
    archivo.writelines(lineas)
```

**Modos de apertura:**
- `'r'`: Lectura (default)
- `'w'`: Escritura (sobrescribe)
- `'a'`: Agregar al final
- `'r+'`: Lectura y escritura
- `'b'`: Modo binario (ej: `'rb'`, `'wb'`)

### 3. Manejo de Excepciones (try/except)

**Sintaxis básica:**
```python
try:
    # Código que puede fallar
    numero = int(input("Número: "))
    resultado = 10 / numero
    print(resultado)
except:
    # Se ejecuta si hay error
    print("Ocurrió un error")
```

**Capturar excepciones específicas:**
```python
try:
    numero = int(input("Número: "))
    resultado = 10 / numero
except ValueError:
    print("Debes ingresar un número válido")
except ZeroDivisionError:
    print("No se puede dividir por cero")
except Exception as e:
    print(f"Error inesperado: {e}")
```

**try/except/else/finally:**
```python
try:
    archivo = open("datos.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("Archivo no encontrado")
except Exception as e:
    print(f"Error: {e}")
else:
    # Se ejecuta si NO hubo error
    print("Archivo leído exitosamente")
finally:
    # SIEMPRE se ejecuta (error o no)
    try:
        archivo.close()
    except:
        pass
```

**Errores comunes:**
```python
# FileNotFoundError - Archivo no existe
# ValueError - Conversión inválida
# ZeroDivisionError - División por cero
# TypeError - Tipo incorrecto
# KeyError - Clave no existe en diccionario
# IndexError - Índice fuera de rango
```

### 4. Context Managers (with)

El `with` garantiza que el archivo se cierre correctamente:

```python
# ✅ Recomendado - Se cierra automáticamente
with open("datos.txt", "r") as archivo:
    contenido = archivo.read()
# Archivo cerrado automáticamente

# ❌ Manual - Puedes olvidar cerrar
archivo = open("datos.txt", "r")
contenido = archivo.read()
archivo.close()  # Fácil de olvidar
```

### 5. Trabajar con CSV

CSV (Comma-Separated Values) es común para datos tabulares:

```python
import csv

# Leer CSV
with open("datos.csv", "r") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)  # fila es una lista

# Escribir CSV
datos = [
    ["Nombre", "Edad", "Ciudad"],
    ["Ana", "25", "Madrid"],
    ["Carlos", "30", "Barcelona"]
]

with open("salida.csv", "w", newline='') as archivo:
    escritor = csv.writer(archivo)
    escritor.writerows(datos)

# CSV con diccionarios
with open("datos.csv", "r") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        print(fila["Nombre"], fila["Edad"])
```

### 6. Trabajar con JSON

JSON es ideal para datos estructurados:

```python
import json

# Leer JSON
with open("datos.json", "r") as archivo:
    datos = json.load(archivo)
    print(datos)

# Escribir JSON
persona = {
    "nombre": "Ana",
    "edad": 25,
    "ciudad": "Madrid",
    "hobbies": ["leer", "programar"]
}

with open("persona.json", "w") as archivo:
    json.dump(persona, archivo, indent=4)

# Convertir objeto Python a string JSON
json_string = json.dumps(persona, indent=2)

# Convertir string JSON a objeto Python
objeto = json.loads(json_string)
```

### 7. Verificar Existencia de Archivos

```python
import os

# Verificar si existe
if os.path.exists("datos.txt"):
    print("El archivo existe")

# Verificar si es archivo
if os.path.isfile("datos.txt"):
    print("Es un archivo")

# Verificar si es directorio
if os.path.isdir("carpeta"):
    print("Es un directorio")

# Obtener tamaño
tamaño = os.path.getsize("datos.txt")
print(f"Tamaño: {tamaño} bytes")
```

## Implementación Práctica

### Ejemplo 1: Sistema de Registro

```python
def registrar_usuario():
    nombre = input("Nombre: ")
    email = input("Email: ")
    
    try:
        with open("usuarios.txt", "a") as archivo:
            archivo.write(f"{nombre},{email}\n")
        print("✓ Usuario registrado")
    except Exception as e:
        print(f"Error al guardar: {e}")

def listar_usuarios():
    try:
        with open("usuarios.txt", "r") as archivo:
            print("\n=== USUARIOS REGISTRADOS ===")
            for linea in archivo:
                nombre, email = linea.strip().split(",")
                print(f"{nombre} - {email}")
    except FileNotFoundError:
        print("No hay usuarios registrados")
    except Exception as e:
        print(f"Error: {e}")

# Menú
while True:
    print("\n1. Registrar usuario")
    print("2. Listar usuarios")
    print("3. Salir")
    
    opcion = input("Opción: ")
    
    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        listar_usuarios()
    elif opcion == "3":
        break
```

### Ejemplo 2: Configuración en JSON

```python
import json

CONFIG_FILE = "config.json"

def cargar_config():
    try:
        with open(CONFIG_FILE, "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        # Configuración por defecto
        return {
            "idioma": "es",
            "tema": "claro",
            "notificaciones": True
        }

def guardar_config(config):
    with open(CONFIG_FILE, "w") as archivo:
        json.dump(config, archivo, indent=4)

# Usar
config = cargar_config()
print(f"Idioma: {config['idioma']}")

# Modificar
config['tema'] = 'oscuro'
guardar_config(config)
```

### Ejemplo 3: Procesador de CSV

```python
import csv

def analizar_ventas(archivo_csv):
    try:
        ventas_totales = 0
        productos_vendidos = 0
        
        with open(archivo_csv, "r") as archivo:
            lector = csv.DictReader(archivo)
            
            for fila in lector:
                precio = float(fila["precio"])
                cantidad = int(fila["cantidad"])
                ventas_totales += precio * cantidad
                productos_vendidos += cantidad
        
        print(f"Ventas totales: ${ventas_totales:.2f}")
        print(f"Productos vendidos: {productos_vendidos}")
        
    except FileNotFoundError:
        print("Archivo no encontrado")
    except KeyError as e:
        print(f"Columna faltante: {e}")
    except Exception as e:
        print(f"Error: {e}")

analizar_ventas("ventas.csv")
```

## Mejores Prácticas

1. **Siempre usa `with` para archivos**
   ```python
   # ✅ Correcto
   with open("archivo.txt", "r") as f:
       contenido = f.read()
   ```

2. **Maneja errores específicos**
   ```python
   # ✅ Mejor
   try:
       ...
   except FileNotFoundError:
       print("Archivo no existe")
   except ValueError:
       print("Valor inválido")
   ```

3. **No captures todos los errores sin razón**
   ```python
   # ❌ Malo (oculta todos los errores)
   try:
       ...
   except:
       pass
   ```

4. **Usa rutas relativas o absolutas claras**
   ```python
   import os
   ruta = os.path.join("data", "archivo.txt")
   ```

## Conceptos clave para recordar

- 🔑 **open()**: Abre archivos (modos: r, w, a)
- 🔑 **with**: Context manager (cierra automáticamente)
- 🔑 **try/except**: Maneja errores sin romper el programa
- 🔑 **FileNotFoundError**: Archivo no existe
- 🔑 **json.load/dump**: Leer/escribir JSON
- 🔑 **csv.reader/writer**: Trabajar con CSV

## Próximos pasos

En el Módulo 7 aprenderás sobre:
- Programación Orientada a Objetos (POO)
- Clases y objetos
- Herencia y polimorfismo

**¡Ya puedes crear programas que persisten datos y manejan errores! 🎉**
