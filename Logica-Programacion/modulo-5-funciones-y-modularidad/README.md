# Módulo 5: Funciones y Modularidad

## Introducción

¡Bienvenido al Módulo 5! Has aprendido los fundamentos: secuencias, decisiones y repeticiones. Ahora aprenderás a organizar tu código en **funciones**, piezas reutilizables que hacen tu código más limpio, organizado y fácil de mantener.

Las funciones son como mini-programas dentro de tu programa principal. Son bloques de código con un nombre que pueden ser llamados cuando los necesites.

## ¿Qué son las Funciones?

Una **función** es un bloque de código con nombre que realiza una tarea específica y puede ser reutilizado múltiples veces.

### Analogía: Una Receta de Cocina

```
FUNCION hacer_cafe():
    hervir_agua()
    agregar_cafe()
    revolver()
    RETORNAR cafe_listo
FIN FUNCION

// Uso
cafe1 = hacer_cafe()  // Primer café
cafe2 = hacer_cafe()  // Segundo café
```

En lugar de repetir los pasos cada vez, defines la receta una vez y la usas cuando la necesites.

## Conceptos Principales

### 1. Definición de funciones

**Sintaxis básica:**
```
FUNCION nombre_funcion():
    // Código de la función
FIN FUNCION
```

**Ejemplo:**
```
FUNCION saludar():
    ESCRIBIR "¡Hola!"
    ESCRIBIR "Bienvenido al programa"
FIN FUNCION

// Llamar la función
saludar()
```

### 2. Parámetros y argumentos

Los **parámetros** permiten pasar información a la función.

**Sintaxis:**
```
FUNCION nombre_funcion(parametro1, parametro2):
    // Código que usa los parámetros
FIN FUNCION
```

**Ejemplo:**
```
FUNCION saludar_persona(nombre):
    ESCRIBIR "¡Hola,", nombre, "!"
FIN FUNCION

// Llamar con argumentos
saludar_persona("Ana")     // Imprime: ¡Hola, Ana!
saludar_persona("Carlos")  // Imprime: ¡Hola, Carlos!
```

**Múltiples parámetros:**
```
FUNCION calcular_area_rectangulo(base, altura):
    area = base * altura
    ESCRIBIR "El área es:", area
FIN FUNCION

calcular_area_rectangulo(5, 3)  // El área es: 15
```

### 3. Retorno de valores

Las funciones pueden **retornar** (devolver) un valor al código que las llamó.

**Sintaxis:**
```
FUNCION nombre_funcion(parametros):
    // Procesamiento
    RETORNAR resultado
FIN FUNCION
```

**Ejemplo:**
```
FUNCION sumar(a, b):
    resultado = a + b
    RETORNAR resultado
FIN FUNCION

// Uso
total = sumar(5, 3)
ESCRIBIR total  // Imprime: 8
```

**Ejemplo: Calculadora**
```
FUNCION multiplicar(x, y):
    RETORNAR x * y
FIN FUNCION

FUNCION dividir(x, y):
    SI y != 0 ENTONCES
        RETORNAR x / y
    SINO
        RETORNAR "Error: división por cero"
    FIN SI
FIN FUNCION

// Uso
resultado1 = multiplicar(4, 5)     // 20
resultado2 = dividir(10, 2)        // 5
resultado3 = dividir(10, 0)        // Error
```

### 4. Ámbito de variables

El **ámbito** (scope) determina dónde una variable puede ser usada.

**Variables locales:** Solo existen dentro de la función
```
FUNCION ejemplo():
    x = 10  // Variable local
    ESCRIBIR x
FIN FUNCION

ejemplo()    // Imprime: 10
ESCRIBIR x   // Error: x no existe fuera de la función
```

**Variables globales:** Existen en todo el programa
```
edad = 25  // Variable global

FUNCION mostrar_edad():
    ESCRIBIR "Edad:", edad  // Puede leer la variable global
FIN FUNCION

mostrar_edad()  // Imprime: Edad: 25
```

## Implementación Práctica

### Ejercicio 1: Función para calcular área

**Problema:** Crear funciones para calcular áreas de diferentes figuras.

**Pseudocódigo:**
```
FUNCION area_circulo(radio):
    area = 3.14159 * radio * radio
    RETORNAR area
FIN FUNCION

FUNCION area_rectangulo(base, altura):
    RETORNAR base * altura
FIN FUNCION

FUNCION area_triangulo(base, altura):
    RETORNAR (base * altura) / 2
FIN FUNCION

// Programa principal
INICIO
    r = 5
    circulo = area_circulo(r)
    ESCRIBIR "Área del círculo:", circulo
    
    rectangulo = area_rectangulo(10, 5)
    ESCRIBIR "Área del rectángulo:", rectangulo
    
    triangulo = area_triangulo(6, 4)
    ESCRIBIR "Área del triángulo:", triangulo
FIN
```

### Ejercicio 2: Función de validación

**Problema:** Crear una función que valide si una edad es válida.

**Pseudocódigo:**
```
FUNCION es_edad_valida(edad):
    SI (edad >= 0) Y (edad <= 120) ENTONCES
        RETORNAR Verdadero
    SINO
        RETORNAR Falso
    FIN SI
FIN FUNCION

// Uso
INICIO
    LEER edad_usuario
    
    SI es_edad_valida(edad_usuario) ENTONCES
        ESCRIBIR "Edad válida:", edad_usuario
    SINO
        ESCRIBIR "Edad inválida"
    FIN SI
FIN
```

### Ejercicio 3: Calculadora modular

**Problema:** Crear una calculadora usando funciones.

**Pseudocódigo:**
```
FUNCION sumar(a, b):
    RETORNAR a + b
FIN FUNCION

FUNCION restar(a, b):
    RETORNAR a - b
FIN FUNCION

FUNCION multiplicar(a, b):
    RETORNAR a * b
FIN FUNCION

FUNCION dividir(a, b):
    SI b != 0 ENTONCES
        RETORNAR a / b
    SINO
        RETORNAR "Error"
    FIN SI
FIN FUNCION

FUNCION mostrar_menu():
    ESCRIBIR "=== CALCULADORA ==="
    ESCRIBIR "1. Sumar"
    ESCRIBIR "2. Restar"
    ESCRIBIR "3. Multiplicar"
    ESCRIBIR "4. Dividir"
    ESCRIBIR "5. Salir"
FIN FUNCION

// Programa principal
INICIO
    opcion = 0
    
    MIENTRAS opcion != 5 HACER
        mostrar_menu()
        LEER opcion
        
        SI opcion >= 1 Y opcion <= 4 ENTONCES
            LEER num1
            LEER num2
            
            SI opcion == 1 ENTONCES
                ESCRIBIR "Resultado:", sumar(num1, num2)
            SINO SI opcion == 2 ENTONCES
                ESCRIBIR "Resultado:", restar(num1, num2)
            SINO SI opcion == 3 ENTONCES
                ESCRIBIR "Resultado:", multiplicar(num1, num2)
            SINO
                ESCRIBIR "Resultado:", dividir(num1, num2)
            FIN SI
        FIN SI
    FIN MIENTRAS
FIN
```

## Mejores Prácticas

### 1. Una función, una responsabilidad
- ✅ Cada función debe hacer una cosa y hacerla bien
- ❌ No mezcles múltiples tareas en una función

### 2. Nombres descriptivos
- ✅ `calcular_promedio()`, `validar_email()`, `convertir_temperatura()`
- ❌ `func1()`, `hacer()`, `procesar()`

### 3. Funciones pequeñas
- ✅ Mantén las funciones cortas (máximo 20-30 líneas)
- ✅ Si es muy larga, divídela en funciones más pequeñas

### 4. Documenta tus funciones
```
FUNCION calcular_imc(peso, altura):
    // Calcula el Índice de Masa Corporal
    // Parámetros:
    //   peso: peso en kilogramos
    //   altura: altura en metros
    // Retorna: IMC calculado
    
    imc = peso / (altura * altura)
    RETORNAR imc
FIN FUNCION
```

### 5. Retorna siempre el mismo tipo
- ✅ Una función debe retornar siempre el mismo tipo de dato
- ❌ No retornes a veces número y a veces texto

## Conceptos Clave para Recordar

- 🔑 **Función**: Bloque de código reutilizable con nombre
- 🔑 **Parámetros**: Valores que recibe la función
- 🔑 **Retorno**: Valor que devuelve la función
- 🔑 **Ámbito**: Dónde una variable es accesible
- 🔑 **Modularidad**: Dividir el código en partes independientes

## Próximos Pasos

En el Módulo 6 aprenderás sobre:
- Estructuras de datos básicas
- Arreglos y listas
- Operaciones con colecciones
- Búsqueda y ordenamiento básico

**¿Qué necesitas saber antes de continuar?**
✅ Cómo definir y llamar funciones  
✅ Usar parámetros y retorno  
✅ Entender el ámbito de variables  
✅ Crear código modular  

## Motivación Final

¡Fantástico! 🎉 Ahora puedes crear código **organizado** y **reutilizable**.

Las funciones son la base de la programación profesional. Con ellas puedes:
- Evitar repetir código
- Organizar programas complejos
- Trabajar en equipo más fácilmente
- Crear bibliotecas de código reutilizable

Recuerda:
- Las funciones hacen tu código más legible
- Un buen programador escribe funciones pequeñas y claras
- La modularidad es clave en proyectos grandes

> "El código es como el humor. Cuando tienes que explicarlo, es malo." - Cory House

**¡Tu código ahora es profesional! 💼✨**

