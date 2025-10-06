# Módulo 8: Recursión

## Introducción

La **recursión** es una técnica donde una función se llama a sí misma. Es como una muñeca rusa: dentro de cada muñeca hay otra más pequeña, hasta llegar a la más pequeña.

## Conceptos Principales

### 1. Funciones recursivas

Una función recursiva tiene dos partes esenciales:
- **Caso base**: Condición que detiene la recursión
- **Caso recursivo**: Llamada a sí misma con un problema más pequeño

**Estructura:**
```
FUNCION recursiva(parametro):
    SI caso_base ENTONCES
        RETORNAR resultado_base
    SINO
        RETORNAR recursiva(parametro_reducido)
    FIN SI
FIN FUNCION
```

### 2. Caso base y caso recursivo

**Ejemplo: Factorial**
```
FUNCION factorial(n):
    // Caso base
    SI n == 0 O n == 1 ENTONCES
        RETORNAR 1
    FIN SI
    
    // Caso recursivo
    RETORNAR n * factorial(n - 1)
FIN FUNCION

// factorial(5) = 5 * factorial(4)
//              = 5 * 4 * factorial(3)
//              = 5 * 4 * 3 * factorial(2)
//              = 5 * 4 * 3 * 2 * factorial(1)
//              = 5 * 4 * 3 * 2 * 1 = 120
```

### 3. Pila de llamadas

Cada llamada recursiva se apila hasta llegar al caso base.

```
factorial(3)
  factorial(2)
    factorial(1)  ← Caso base, empieza a retornar
    retorna 1
  retorna 2 * 1 = 2
retorna 3 * 2 = 6
```

### 4. Recursión vs iteración

**Recursivo:**
```
FUNCION suma_recursiva(n):
    SI n == 0 ENTONCES
        RETORNAR 0
    FIN SI
    RETORNAR n + suma_recursiva(n - 1)
FIN FUNCION
```

**Iterativo:**
```
FUNCION suma_iterativa(n):
    suma = 0
    PARA i DESDE 1 HASTA n HACER
        suma = suma + i
    FIN PARA
    RETORNAR suma
FIN FUNCION
```

## Implementación Práctica

### Ejercicio 1: Factorial recursivo

```
FUNCION factorial(n):
    SI n <= 1 ENTONCES
        RETORNAR 1
    FIN SI
    RETORNAR n * factorial(n - 1)
FIN FUNCION

// Uso
LEER numero
resultado = factorial(numero)
ESCRIBIR "Factorial de", numero, "=", resultado
```

### Ejercicio 2: Fibonacci recursivo

```
FUNCION fibonacci(n):
    SI n == 0 ENTONCES
        RETORNAR 0
    FIN SI
    SI n == 1 ENTONCES
        RETORNAR 1
    FIN SI
    RETORNAR fibonacci(n-1) + fibonacci(n-2)
FIN FUNCION

// Serie: 0, 1, 1, 2, 3, 5, 8, 13, 21...
```

### Ejercicio 3: Suma de dígitos

```
FUNCION suma_digitos(n):
    SI n < 10 ENTONCES
        RETORNAR n
    FIN SI
    RETORNAR (n MOD 10) + suma_digitos(n / 10)
FIN FUNCION

// suma_digitos(123) = 3 + suma_digitos(12)
//                   = 3 + 2 + suma_digitos(1)
//                   = 3 + 2 + 1 = 6
```

## Mejores Prácticas

1. **Siempre define un caso base**: Sin él, recursión infinita
2. **Asegura que avanza al caso base**: El parámetro debe reducirse
3. **Considera el rendimiento**: La recursión consume memoria (stack)
4. **Usa iteración para casos simples**: Más eficiente en memoria

## Conceptos Clave

- 🔑 **Recursión**: Función que se llama a sí misma
- 🔑 **Caso base**: Condición de parada
- 🔑 **Caso recursivo**: Llamada con problema reducido
- 🔑 **Pila**: Estructura que almacena llamadas

## Motivación Final

¡Impresionante! 🎉 La recursión es elegante y poderosa. Dominarla es signo de pensamiento computacional avanzado.

**¡Ahora piensas en múltiples dimensiones! 🌀✨**
