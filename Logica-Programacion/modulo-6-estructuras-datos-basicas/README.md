# Módulo 6: Estructuras de Datos Básicas

## Introducción

¡Bienvenido al Módulo 6! Hasta ahora has trabajado con variables individuales, pero ¿qué pasa cuando necesitas manejar muchos datos relacionados? Las **estructuras de datos** te permiten organizar y almacenar múltiples valores de manera eficiente.

Las estructuras de datos son como contenedores que organizan información relacionada, permitiéndote trabajar con colecciones de datos en lugar de variables individuales.

## Conceptos Principales

### 1. Arreglos/Listas

Un **arreglo** o **lista** es una colección ordenada de elementos del mismo tipo.

**Declaración:**
```
numeros = [1, 2, 3, 4, 5]
nombres = ["Ana", "Juan", "María"]
```

**Características:**
- Elementos ordenados (tienen posición)
- Acceso por índice (normalmente desde 0)
- Tamaño fijo o dinámico según el lenguaje

### 2. Acceso por índice

**Sintaxis:**
```
elemento = lista[indice]
```

**Ejemplo:**
```
frutas = ["manzana", "pera", "uva", "naranja"]

ESCRIBIR frutas[0]  // manzana
ESCRIBIR frutas[2]  // uva
```

### 3. Recorrido de estructuras

**Con bucle FOR:**
```
calificaciones = [85, 90, 78, 92, 88]

PARA i DESDE 0 HASTA longitud(calificaciones)-1 HACER
    ESCRIBIR "Calificación", i+1, ":", calificaciones[i]
FIN PARA
```

**Con bucle PARA CADA (FOR EACH):**
```
PARA CADA fruta EN frutas HACER
    ESCRIBIR fruta
FIN PARA
```

### 4. Operaciones básicas

**Agregar elementos:**
```
lista.agregar(elemento)
```

**Eliminar elementos:**
```
lista.eliminar(indice)
```

**Buscar elementos:**
```
SI elemento EN lista ENTONCES
    ESCRIBIR "Encontrado"
FIN SI
```

## Implementación Práctica

### Ejercicio 1: Gestión de calificaciones

```
INICIO
    calificaciones = []
    
    PARA i DESDE 1 HASTA 5 HACER
        ESCRIBIR "Ingrese calificación", i
        LEER nota
        calificaciones.agregar(nota)
    FIN PARA
    
    suma = 0
    PARA CADA nota EN calificaciones HACER
        suma = suma + nota
    FIN PARA
    
    promedio = suma / longitud(calificaciones)
    ESCRIBIR "Promedio:", promedio
FIN
```

### Ejercicio 2: Lista de compras

```
FUNCION agregar_producto(lista, producto):
    lista.agregar(producto)
    ESCRIBIR "Producto agregado:", producto
FIN FUNCION

FUNCION mostrar_lista(lista):
    ESCRIBIR "=== LISTA DE COMPRAS ==="
    PARA i DESDE 0 HASTA longitud(lista)-1 HACER
        ESCRIBIR (i+1), ".", lista[i]
    FIN PARA
FIN FUNCION

// Uso
compras = []
agregar_producto(compras, "Leche")
agregar_producto(compras, "Pan")
agregar_producto(compras, "Huevos")
mostrar_lista(compras)
```

### Ejercicio 3: Agenda de contactos

```
nombres = []
telefonos = []

FUNCION agregar_contacto(nombre, telefono):
    nombres.agregar(nombre)
    telefonos.agregar(telefono)
    ESCRIBIR "Contacto agregado"
FIN FUNCION

FUNCION buscar_contacto(nombre):
    PARA i DESDE 0 HASTA longitud(nombres)-1 HACER
        SI nombres[i] == nombre ENTONCES
            ESCRIBIR "Teléfono:", telefonos[i]
            RETORNAR
        FIN SI
    FIN PARA
    ESCRIBIR "Contacto no encontrado"
FIN FUNCION
```

## Mejores Prácticas

1. **Inicializa las estructuras**: Siempre crea la estructura antes de usarla
2. **Verifica límites**: Asegúrate de no acceder índices inválidos
3. **Usa nombres descriptivos**: `calificaciones_estudiantes` mejor que `lista1`
4. **Itera con cuidado**: Verifica el tamaño antes de recorrer

## Conceptos Clave

- 🔑 **Arreglo/Lista**: Colección ordenada de elementos
- 🔑 **Índice**: Posición de un elemento en la lista
- 🔑 **Recorrido**: Visitar cada elemento de la estructura
- 🔑 **Operaciones**: Agregar, eliminar, buscar elementos

## Motivación Final

¡Excelente! 🎉 Ahora puedes trabajar con colecciones de datos, un paso crucial hacia programas más complejos y útiles.

**¡Dominas las estructuras de datos básicas! 📊**
