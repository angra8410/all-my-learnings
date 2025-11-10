# Retroalimentación y Soluciones - Módulo 4: Bucles

## Sección 1: Respuestas a Preguntas de Opción Múltiple

### Pregunta 1: ¿Qué es un bucle en programación?
**Respuesta correcta: B) Una estructura que repite código mientras se cumple una condición**

**Explicación**: Los bucles son estructuras de control que permiten ejecutar un bloque de código múltiples veces automáticamente, sin tener que escribir el mismo código repetidamente.

### Pregunta 2: ¿Cuál es la diferencia principal entre MIENTRAS y PARA?
**Respuesta correcta: C) PARA se usa cuando sabemos cuántas veces repetir, MIENTRAS cuando no**

**Explicación**: PARA es ideal para iteraciones con un número conocido de repeticiones. MIENTRAS se usa cuando la condición de parada depende de factores que cambian durante la ejecución.

### Pregunta 3: ¿Cuándo se evalúa la condición en un bucle MIENTRAS?
**Respuesta correcta: C) Antes de cada iteración**

**Explicación**: La condición se verifica ANTES de ejecutar el bloque de código en cada iteración.

### Pregunta 4: ¿Qué es un bucle infinito?
**Respuesta correcta: B) Un bucle cuya condición nunca se vuelve falsa**

**Explicación**: Un bucle infinito ocurre cuando la condición de salida nunca se cumple, causando que el programa se quede ejecutando indefinidamente.

### Pregunta 5: En un bucle PARA, ¿qué sucede con la variable de control?
**Respuesta correcta: B) Se incrementa o decrementa automáticamente en cada iteración**

**Explicación**: La variable de control del bucle PARA cambia automáticamente en cada iteración según el paso definido.

### Pregunta 6: ¿Cuál es el propósito de un contador en un bucle?
**Respuesta correcta: B) Llevar registro del número de iteraciones**

**Explicación**: Los contadores rastrean cuántas veces se ha ejecutado un bucle o cuántos elementos cumplen cierta condición.

### Pregunta 7: ¿Qué es un acumulador?
**Respuesta correcta: A) Una variable que va sumando valores en cada iteración**

**Explicación**: Un acumulador es una variable que acumula (suma, multiplica, etc.) valores a lo largo de las iteraciones del bucle.

### Pregunta 8: ¿Cuántas veces se ejecuta este bucle?
**Respuesta correcta: B) 10 veces**

**Explicación**: De i=1 hasta i=10 inclusive son 10 iteraciones.

## Sección 2: Respuestas a Verdadero o Falso

### Pregunta 9: Un bucle MIENTRAS puede no ejecutarse nunca...
**Respuesta correcta: Verdadero**

### Pregunta 10: Un bucle PARA siempre se ejecuta al menos una vez.
**Respuesta correcta: Falso**

### Pregunta 11: Es posible tener bucles anidados.
**Respuesta correcta: Verdadero**

### Pregunta 12: Un contador debe inicializarse antes del bucle.
**Respuesta correcta: Verdadero**

### Pregunta 13: La única forma de salir de un bucle MIENTRAS...
**Respuesta correcta: Verdadero** (en pseudocódigo básico)

### Pregunta 14: Un acumulador siempre debe inicializarse en 0.
**Respuesta correcta: Falso** (depende de la operación)

## Sección 3: Soluciones a Trazas

### Ejercicio 15: Traza de bucle MIENTRAS

| Iteración | i | suma | ¿Condición verdadera? |
|-----------|---|------|----------------------|
| Inicio    | 1 | 0    | -                    |
| 1         | 1 | 1    | Sí (1<=3)            |
| 2         | 2 | 3    | Sí (2<=3)            |
| 3         | 3 | 6    | Sí (3<=3)            |
| Salida    | 4 | 6    | No (4>3)             |

**Salida del programa:** 6

### Ejercicio 16: Traza bucle PARA

| Iteración | i | producto |
|-----------|---|----------|
| Inicio    | - | 1        |
| 1         | 1 | 1        |
| 2         | 2 | 2        |
| 3         | 3 | 6        |
| 4         | 4 | 24       |

**Salida final:** 24
**Calcula:** El factorial de 4

## Sección 4: Soluciones a Completar Algoritmos

### Ejercicio 17:
```
i = 1
MIENTRAS i <= 5 HACER
    i = i + 1
```

### Ejercicio 18:
```
PARA i = 1 HASTA 10 HACER
    suma = suma + i
```

## Sección 5: Soluciones a Pseudocódigo

### Ejercicio 19: Números pares
```
INICIO
    i = 2
    MIENTRAS i <= 20 HACER
        ESCRIBIR i
        i = i + 2
    FIN MIENTRAS
FIN
```

### Ejercicio 20: Factorial
```
INICIO
    LEER n
    factorial = 1
    PARA i = 1 HASTA n HACER
        factorial = factorial * i
    FIN PARA
    ESCRIBIR factorial
FIN
```

### Ejercicio 21: Promedio
```
INICIO
    suma = 0
    PARA i = 1 HASTA 5 HACER
        LEER numero
        suma = suma + numero
    FIN PARA
    promedio = suma / 5
    ESCRIBIR promedio
FIN
```

## Ejercicios Restantes

**Ejercicio 22:** Contador de pares: inicializar contador en 0, iterar de 1 a 20, incrementar contador si i MOD 2 == 0

**Ejercicio 23:** Acumulador de impares: suma = 0, iterar de 1 a 50 con paso 2

**Ejercicio 24:** Falta incrementar i dentro del bucle (bucle infinito)

**Ejercicio 25:** El contador se incrementa en lugar de decrementar (bucle infinito)

**Ejercicio 26-30:** Ver README para ejemplos completos

## Autoevaluación
- Opción múltiple: ___ de 8
- Verdadero/Falso: ___ de 6
- Trazas: ___ de 2
- Completar: ___ de 2  
- Pseudocódigo: ___ de 3
- Contadores/Acumuladores: ___ de 2
- Errores: ___ de 2
- Anidados: ___ de 2
- Aplicaciones: ___ de 2
- Integrador: ___ de 1

**Total: ___ de 30 puntos**

¡Felicidades por completar el Módulo 4! 🎉
