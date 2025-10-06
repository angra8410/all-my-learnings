# Módulo 4: Bucles

## Introducción

¡Bienvenido al Módulo 4! Ya sabes crear secuencias y tomar decisiones. Ahora aprenderás una de las herramientas más poderosas de la programación: los **bucles** (también llamados ciclos o loops).

Los bucles permiten que tu programa repita instrucciones múltiples veces automáticamente, sin tener que escribir el mismo código una y otra vez.

## ¿Qué son los Bucles?

Un **bucle** es una estructura de control que permite ejecutar un bloque de código múltiples veces mientras se cumpla una condición o para un número determinado de repeticiones.

### Analogía: Lavarse los Dientes

```
PARA cada diente EN boca HACER
    Cepillar diente
FIN PARA
```

En lugar de escribir "Cepillar diente 1, Cepillar diente 2, ..." 32 veces, usamos un bucle.

## ¿Por qué son importantes?

Los bucles son fundamentales porque:

1. **Automatizan tareas repetitivas**: Evitan código duplicado
2. **Ahorran tiempo**: Una línea de código puede ejecutarse miles de veces
3. **Procesan colecciones**: Permiten trabajar con listas de datos
4. **Son eficientes**: Permiten operaciones masivas rápidamente
5. **Están en todas partes**: Casi todos los programas usan bucles

## Conceptos Principales

### 1. Bucle MIENTRAS (WHILE)

El bucle **MIENTRAS** repite un bloque de código **mientras** una condición sea verdadera.

**Sintaxis:**
```
MIENTRAS condición HACER
    // Código a repetir
FIN MIENTRAS
```

**Características:**
- La condición se evalúa **antes** de cada iteración
- Si la condición es falsa desde el principio, el bucle nunca se ejecuta
- **Peligro**: Si la condición nunca se vuelve falsa, el bucle es infinito

**Diagrama de flujo:**
```
         ┌─────────┐
         │ Inicio  │
         └────┬────┘
              │
              ▼
        ╱───────────╲
       ╱ ¿condición  ╲
      ╱   verdadera?  ╲
     ╱                 ╲
    ╱   Sí        No    ╲
   │     │         │     │
   │     ▼         ▼     │
   │  ┌──────┐  ┌─────┐ │
   │  │Código│  │ Fin │ │
   │  │bucle │  └─────┘ │
   │  └──┬───┘          │
   │     │              │
   └─────┘              │
                        ▼
```

**Ejemplo: Contador simple**
```
INICIO
    contador = 1
    
    MIENTRAS contador <= 5 HACER
        ESCRIBIR "Número:", contador
        contador = contador + 1
    FIN MIENTRAS
    
    ESCRIBIR "Fin del bucle"
FIN
```

**Salida:**
```
Número: 1
Número: 2
Número: 3
Número: 4
Número: 5
Fin del bucle
```

**Ejemplo: Validar entrada**
```
INICIO
    contraseña = ""
    
    MIENTRAS contraseña != "secreto" HACER
        ESCRIBIR "Ingrese la contraseña:"
        LEER contraseña
        
        SI contraseña != "secreto" ENTONCES
            ESCRIBIR "Contraseña incorrecta. Intente de nuevo."
        FIN SI
    FIN MIENTRAS
    
    ESCRIBIR "¡Acceso concedido!"
FIN
```

### 2. Bucle PARA (FOR)

El bucle **PARA** repite un bloque de código un **número específico** de veces.

**Sintaxis:**
```
PARA variable DESDE inicio HASTA fin HACER
    // Código a repetir
FIN PARA
```

**Características:**
- El número de iteraciones se conoce de antemano
- La variable de control se actualiza automáticamente
- Más seguro que MIENTRAS (no puede ser infinito)

**Ejemplo: Tabla de multiplicar**
```
INICIO
    LEER numero
    
    ESCRIBIR "Tabla del", numero
    
    PARA i DESDE 1 HASTA 10 HACER
        resultado = numero * i
        ESCRIBIR numero, "x", i, "=", resultado
    FIN PARA
FIN
```

**Salida (para numero = 5):**
```
Tabla del 5
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```

**Ejemplo: Contar hacia atrás**
```
PARA i DESDE 10 HASTA 1 CON PASO -1 HACER
    ESCRIBIR i
FIN PARA
ESCRIBIR "¡Despegue!"
```

### 3. Contadores y acumuladores

**Contador:** Variable que se incrementa (o decrementa) en cada iteración.

```
contador = 0

PARA i DESDE 1 HASTA 100 HACER
    contador = contador + 1
FIN PARA

ESCRIBIR "Total de iteraciones:", contador
```

**Acumulador:** Variable que acumula (suma) valores en cada iteración.

```
suma = 0

PARA i DESDE 1 HASTA 100 HACER
    suma = suma + i
FIN PARA

ESCRIBIR "Suma de 1 a 100:", suma  // Resultado: 5050
```

**Ejemplo completo: Calcular promedio**
```
INICIO
    suma = 0
    contador = 0
    
    ESCRIBIR "¿Cuántas calificaciones ingresará?"
    LEER cantidad
    
    PARA i DESDE 1 HASTA cantidad HACER
        ESCRIBIR "Ingrese calificación", i
        LEER nota
        suma = suma + nota
        contador = contador + 1
    FIN PARA
    
    promedio = suma / contador
    ESCRIBIR "El promedio es:", promedio
FIN
```

### 4. Control de bucles (BREAK, CONTINUE)

**BREAK:** Termina el bucle inmediatamente.

```
PARA i DESDE 1 HASTA 100 HACER
    LEER numero
    
    SI numero == 0 ENTONCES
        ESCRIBIR "Número 0 detectado. Terminando..."
        BREAK  // Sale del bucle
    FIN SI
    
    ESCRIBIR "Procesando:", numero
FIN PARA
```

**CONTINUE:** Salta a la siguiente iteración del bucle.

```
PARA i DESDE 1 HASTA 10 HACER
    SI i MOD 2 == 0 ENTONCES
        CONTINUE  // Salta números pares
    FIN SI
    
    ESCRIBIR i  // Solo imprime impares: 1, 3, 5, 7, 9
FIN PARA
```

**Comparación BREAK vs CONTINUE:**

```
// Con BREAK (termina el bucle)
PARA i DESDE 1 HASTA 5 HACER
    SI i == 3 ENTONCES
        BREAK
    FIN SI
    ESCRIBIR i
FIN PARA
// Imprime: 1, 2

// Con CONTINUE (salta una iteración)
PARA i DESDE 1 HASTA 5 HACER
    SI i == 3 ENTONCES
        CONTINUE
    FIN SI
    ESCRIBIR i
FIN PARA
// Imprime: 1, 2, 4, 5
```

## Implementación Práctica

### Ejercicio 1: Tabla de multiplicar

**Problema:** Mostrar la tabla de multiplicar de un número del 1 al 10.

**Pseudocódigo:**
```
INICIO
    ESCRIBIR "Ingrese un número:"
    LEER numero
    
    ESCRIBIR "=== Tabla del", numero, "==="
    
    PARA i DESDE 1 HASTA 10 HACER
        resultado = numero * i
        ESCRIBIR numero, "x", i, "=", resultado
    FIN PARA
FIN
```

### Ejercicio 2: Suma de números

**Problema:** Sumar números ingresados hasta que el usuario ingrese 0.

**Pseudocódigo:**
```
INICIO
    suma = 0
    numero = -1  // Valor inicial diferente de 0
    
    ESCRIBIR "Ingrese números (0 para terminar)"
    
    MIENTRAS numero != 0 HACER
        LEER numero
        suma = suma + numero
    FIN MIENTRAS
    
    ESCRIBIR "La suma total es:", suma
FIN
```

### Ejercicio 3: Validar entrada del usuario

**Problema:** Pedir un número entre 1 y 10 hasta que sea válido.

**Pseudocódigo:**
```
INICIO
    numero = 0
    
    MIENTRAS (numero < 1) O (numero > 10) HACER
        ESCRIBIR "Ingrese un número entre 1 y 10:"
        LEER numero
        
        SI (numero < 1) O (numero > 10) ENTONCES
            ESCRIBIR "Error: número fuera de rango"
        FIN SI
    FIN MIENTRAS
    
    ESCRIBIR "Número válido:", numero
FIN
```

## Mejores Prácticas

### 1. Evita Bucles Infinitos
- ✅ Asegúrate de que la condición eventualmente sea falsa
- ✅ Verifica que la variable de control se actualice
- ❌ Cuidado con: `MIENTRAS Verdadero HACER`

### 2. Inicializa Variables
- ✅ Inicializa contadores en 0
- ✅ Inicializa acumuladores en 0
- ✅ Inicializa banderas en Falso

### 3. Usa el Bucle Apropiado
- ✅ PARA: cuando conoces el número de iteraciones
- ✅ MIENTRAS: cuando no sabes cuántas veces repetir
- ❌ No uses MIENTRAS si puedes usar PARA

### 4. Nombres Descriptivos
- ✅ `total_estudiantes`, `suma_calificaciones`
- ❌ `i`, `j`, `k` (excepto para índices simples)

### 5. Mantén el Código Simple
- ✅ Un bucle, una responsabilidad
- ❌ No anides demasiados bucles (máximo 2-3 niveles)

## Conceptos Clave para Recordar

- 🔑 **Bucle MIENTRAS (WHILE)**: Repite mientras la condición sea verdadera
- 🔑 **Bucle PARA (FOR)**: Repite un número específico de veces
- 🔑 **Contador**: Variable que cuenta iteraciones
- 🔑 **Acumulador**: Variable que suma valores
- 🔑 **BREAK**: Termina el bucle inmediatamente
- 🔑 **CONTINUE**: Salta a la siguiente iteración

## Próximos Pasos

En el Módulo 5 aprenderás sobre:
- Funciones y cómo crearlas
- Parámetros y valores de retorno
- Modularidad y reutilización de código
- Ámbito de variables

**¿Qué necesitas saber antes de continuar?**
✅ Cómo usar bucles MIENTRAS y PARA  
✅ Diferencia entre contador y acumulador  
✅ Cuándo usar BREAK y CONTINUE  
✅ Evitar bucles infinitos  

## Motivación Final

¡Increíble! 🎉 Ahora puedes hacer que tus programas **repitan** tareas automáticamente.

Los bucles son el **motor** de la automatización. Con ellos puedes:
- Procesar miles de datos en segundos
- Crear juegos y animaciones
- Validar entradas del usuario
- Realizar cálculos complejos

Recuerda:
- Un bucle bien escrito puede ahorrar horas de trabajo manual
- Los bucles están en el corazón de la eficiencia computacional
- Dominar los bucles es dominar la automatización

> "La computadora es increíblemente rápida, precisa y estúpida. El humano es increíblemente lento, impreciso y brillante. Juntos, con los bucles, son poderosos más allá de toda imaginación." - Adaptado de Albert Einstein

**¡Ahora tus programas son incansables! 🔄💪**

