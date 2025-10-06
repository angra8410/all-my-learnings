# Módulo 1: Introducción a Python

## ¿Qué es Python?

Imagina que quieres dar instrucciones a una computadora, pero no hablas su idioma (ceros y unos). Python es como un **traductor amigable** que te permite escribir instrucciones en un lenguaje casi humano, y él se encarga de traducirlo para que la computadora lo entienda.

Python es un **lenguaje de programación** creado por Guido van Rossum en 1991. Se llama así por el grupo de comedia británico "Monty Python", ¡no por la serpiente! 🐍

### ¿Por qué Python es especial?

1. **Fácil de leer**: El código Python parece casi inglés. Si escribes `print("Hola")`, es obvio que imprime "Hola".

2. **Versátil**: Puedes hacer de todo:
   - Páginas web (Instagram, Spotify)
   - Inteligencia Artificial (ChatGPT, sistemas de recomendación)
   - Análisis de datos (científicos, empresas)
   - Automatización de tareas
   - Juegos
   - ¡Y mucho más!

3. **Amigable para principiantes**: No necesitas ser un genio de las matemáticas. Si puedes seguir una receta de cocina, ¡puedes programar en Python!

4. **Comunidad enorme**: Millones de personas usan Python. Si tienes una duda, alguien ya la resolvió.

### Ejemplo cotidiano: La Receta de Cocina

Programar es como seguir una receta:

```
Receta: Hacer un sándwich
1. Toma 2 rebanadas de pan
2. Unta mantequilla en ambas
3. Agrega jamón
4. Agrega queso
5. Junta las rebanadas
6. ¡Listo!
```

En Python sería algo así:

```python
pan = 2
mantequilla = "untada"
jamón = "agregado"
queso = "agregado"

print("¡Sándwich listo!")
```

## ¿Por qué aprender Python?

### 🎯 Es el lenguaje #1 para principiantes
Empresas como Google, Netflix, NASA lo usan. Es el lenguaje más demandado en empleos tech.

### 💼 Oportunidades laborales
- Científico de Datos
- Desarrollador Backend
- Ingeniero de Machine Learning
- Automatización y DevOps
- Analista de Datos

### 🚀 Proyectos que puedes crear
- Bot de Telegram que responde mensajes
- Programa que organiza tus archivos automáticamente
- Analizador de tus canciones favoritas de Spotify
- Sistema de recomendación de películas
- Juegos simples como Snake o Adivina el Número

## Conceptos Principales

### 1. ¿Qué es programar?

**Programar** es dar instrucciones a una computadora para que haga algo. Es como ser el director de una orquesta: tú decides qué instrumento toca cuándo y cómo.

**Ejemplo del mundo real:**
Cuando usas una aplicación de delivery:
1. Seleccionas comida (input/entrada)
2. La app calcula el precio (proceso)
3. Te muestra el total y tiempo de entrega (output/salida)

Todo eso es **código** funcionando.

### 2. Instalación de Python

**Windows:**
1. Ve a [python.org](https://python.org)
2. Descarga Python 3.11 o superior
3. ¡IMPORTANTE! Marca "Add Python to PATH"
4. Instala

**Mac/Linux:**
Generalmente ya viene instalado. Verifica con:
```bash
python3 --version
```

**Verificar instalación:**
```bash
python --version
# o
python3 --version
```

Deberías ver algo como: `Python 3.11.x`

### 3. Tu primer programa: "Hola Mundo"

Es tradición que tu primer programa diga "Hola Mundo":

```python
print("¡Hola Mundo!")
```

¡Así de simple! Vamos a entenderlo:

- `print()` es una **función** que muestra texto en pantalla
- `"¡Hola Mundo!"` es el **texto** que queremos mostrar
- Los paréntesis `()` son necesarios
- Las comillas `""` indican que es texto

**Variaciones:**
```python
print("Bienvenido a Python")
print("Mi nombre es Ana")
print("2024")
print(42)  # Sin comillas, es un número
```

### 4. El intérprete de Python

Python es **interpretado**, no compilado. ¿Qué significa?

**Analogía del traductor:**
- **Compilado** (como C++): Es como traducir un libro completo del español al inglés antes de leerlo. Todo de una vez.
- **Interpretado** (como Python): Es como tener un traductor simultáneo. Traduce línea por línea mientras hablas.

**Ventajas:**
- Más rápido para probar código
- Errores más fáciles de encontrar
- Más flexible

**Dos formas de usar Python:**

1. **Modo interactivo** (REPL):
```bash
python
>>> print("Hola")
Hola
>>> 2 + 2
4
>>> exit()
```

2. **Archivo .py**:
Crea `mi_programa.py`:
```python
print("Este es mi programa")
```
Ejecuta:
```bash
python mi_programa.py
```

### 5. Comentarios en Python

Los comentarios son notas para humanos, Python las ignora:

```python
# Esto es un comentario de una línea
print("Hola")  # También puedo comentar aquí

"""
Esto es un comentario
de múltiples líneas.
Útil para explicaciones largas.
"""

'''
También puedes usar
comillas simples triples
'''
```

**¿Cuándo usar comentarios?**
- Explica **por qué** haces algo, no **qué** haces
- Documenta funciones complejas
- Marca secciones de código
- Temporalmente "apaga" código para probar

**Ejemplo bueno:**
```python
# Convertimos a minúsculas para comparación sin importar mayúsculas
nombre = nombre.lower()
```

**Ejemplo malo:**
```python
# Imprime hola
print("Hola")  # ¡Ya es obvio!
```

### 6. La filosofía de Python: Zen de Python

Escribe en Python:
```python
import this
```

Verás principios como:
- "Bello es mejor que feo"
- "Explícito es mejor que implícito"
- "Simple es mejor que complejo"
- "La legibilidad cuenta"

Esto significa: **Escribe código que otros (y tu yo del futuro) puedan entender fácilmente**.

## Implementación Práctica

### Ejercicio 1: Tu primer programa personalizado

Crea un archivo `presentacion.py`:

```python
# Mi programa de presentación
print("==========================")
print("¡Hola! Soy estudiante de Python")
print("==========================")
print()  # Línea en blanco
print("Nombre: [Tu nombre aquí]")
print("Objetivo: Aprender Python")
print("Año: 2024")
print()
print("¡Vamos a aprender juntos!")
```

### Ejercicio 2: Experimentar con print()

```python
# Diferentes formas de usar print
print("Una línea")
print("Línea 1", "Línea 2")  # Separa con espacio
print("Línea 1" + "Línea 2")  # Une sin espacio
print("Primera\nSegunda")  # \n = nueva línea
print("Tab\taqui")  # \t = tabulación
```

### Ejercicio 3: Calculadora simple

```python
# Python como calculadora
print(2 + 3)      # Suma: 5
print(10 - 4)     # Resta: 6
print(3 * 5)      # Multiplicación: 15
print(20 / 4)     # División: 5.0
print(2 ** 3)     # Potencia: 8 (2 elevado a 3)
print(10 % 3)     # Módulo (resto): 1
```

## Mejores Prácticas

1. **Nombra tus archivos en minúsculas**
   - ✅ `mi_programa.py`
   - ❌ `MiPrograma.py`

2. **Un programa = un archivo**
   - Mantén programas simples en un solo archivo

3. **Prueba frecuentemente**
   - No escribas 100 líneas sin probar. Escribe 5, prueba, continúa.

4. **Guarda tu trabajo**
   - Usa nombres descriptivos
   - Organiza en carpetas

5. **Lee código de otros**
   - Aprende de ejemplos en internet
   - Intenta entender qué hace cada línea

## Conceptos clave para recordar

- 🔑 **Python**: Lenguaje de programación fácil de leer y versátil
- 🔑 **print()**: Función para mostrar información en pantalla
- 🔑 **Comentarios**: Notas con # para humanos, Python las ignora
- 🔑 **Interpretado**: Python ejecuta código línea por línea
- 🔑 **REPL**: Modo interactivo para probar código rápidamente

## Próximos pasos

En el Módulo 2 aprenderás sobre:
- Variables (cajas para guardar información)
- Tipos de datos (números, texto, booleanos)
- Operaciones básicas
- Input del usuario

**¿Qué necesitas saber antes de continuar?**
✅ Cómo ejecutar un programa Python  
✅ Qué hace `print()`  
✅ Para qué sirven los comentarios  
✅ Diferencia entre texto y números  

## Motivación Final

> "El camino de mil millas comienza con un paso." - Lao Tzu

Acabas de dar tu primer paso en Python. Puede parecer simple imprimir "Hola Mundo", pero cada programador profesional empezó exactamente ahí.

**Recuerda:**
- No necesitas memorizar todo
- Los errores son parte del aprendizaje
- La práctica hace al maestro
- Google es tu amigo
- La comunidad de Python siempre ayuda

**Tu desafío:**
Escribe un programa que imprima 5 cosas que quieres lograr aprendiendo Python. ¡Hazlo TU motivación!

```python
print("Mis objetivos con Python:")
print("1. ________________")
print("2. ________________")
# Continúa...
```

¡Nos vemos en el Módulo 2! 🚀🐍
