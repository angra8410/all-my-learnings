# Módulo 3: Condicionales

## Introducción

¡Bienvenido al Módulo 3! Hasta ahora has aprendido a crear secuencias lineales, pero ¿qué pasa cuando necesitas que tu programa tome decisiones?

Los **condicionales** son estructuras que permiten que un programa ejecute diferentes acciones dependiendo de si una condición es verdadera o falsa. Son como las bifurcaciones en un camino: dependiendo de la situación, tomas un camino u otro.

## ¿Qué son los Condicionales?

Los **condicionales** son estructuras de control que permiten ejecutar diferentes bloques de código según se cumplan o no ciertas condiciones.

### Analogía: El Semáforo

```
SI la luz está en verde ENTONCES
    Avanza
SINO SI la luz está en amarillo ENTONCES
    Prepárate para detenerte
SINO
    Detente (luz roja)
FIN SI
```

El automóvil toma diferentes acciones según el color del semáforo.

## ¿Por qué son importantes?

Los condicionales son esenciales porque:

1. **Permiten la toma de decisiones**: Los programas pueden responder de manera diferente a distintas situaciones
2. **Hacen los programas inteligentes**: Pueden adaptarse según las circunstancias
3. **Son fundamentales en la lógica**: La mayoría de los programas necesitan tomar decisiones
4. **Reflejan el pensamiento humano**: Tomamos decisiones constantemente basadas en condiciones

## Conceptos Principales

### 1. Estructuras IF-ELSE

La estructura **IF-ELSE** (SI-SINO) evalúa una condición y ejecuta un bloque de código u otro.

**Sintaxis básica:**
```
SI condición ENTONCES
    // Código si la condición es verdadera
SINO
    // Código si la condición es falsa
FIN SI
```

**Diagrama de flujo:**
```
       ╱─────────╲
      ╱ ¿condición?╲
     ╱   verdadera? ╲
    ╱                ╲
   ╱   Sí      No     ╲
  │     │       │      │
  ▼     ▼       ▼      ▼
  ┌──────┐    ┌──────┐
  │Código│    │Código│
  │ SI   │    │ SINO │
  └──┬───┘    └──┬───┘
     │           │
     └─────┬─────┘
           ▼
```

**Ejemplo en pseudocódigo:**
```
LEER edad

SI edad >= 18 ENTONCES
    ESCRIBIR "Eres mayor de edad"
SINO
    ESCRIBIR "Eres menor de edad"
FIN SI
```

### 2. Condiciones múltiples (ELIF)

**ELIF** (SINO SI) permite evaluar múltiples condiciones en secuencia.

**Sintaxis:**
```
SI condición1 ENTONCES
    // Código si condición1 es verdadera
SINO SI condición2 ENTONCES
    // Código si condición2 es verdadera
SINO SI condición3 ENTONCES
    // Código si condición3 es verdadera
SINO
    // Código si ninguna condición es verdadera
FIN SI
```

**Ejemplo: Sistema de calificaciones**
```
LEER nota

SI nota >= 90 ENTONCES
    ESCRIBIR "Calificación: A - Excelente"
SINO SI nota >= 80 ENTONCES
    ESCRIBIR "Calificación: B - Muy bien"
SINO SI nota >= 70 ENTONCES
    ESCRIBIR "Calificación: C - Bien"
SINO SI nota >= 60 ENTONCES
    ESCRIBIR "Calificación: D - Suficiente"
SINO
    ESCRIBIR "Calificación: F - Reprobado"
FIN SI
```

### 3. Operadores lógicos

Los **operadores lógicos** permiten combinar múltiples condiciones.

**Operador Y (AND):**
- Verdadero solo si AMBAS condiciones son verdaderas

```
SI (edad >= 18) Y (tiene_licencia == Verdadero) ENTONCES
    ESCRIBIR "Puede conducir"
FIN SI
```

**Tabla de verdad AND:**
| A | B | A Y B |
|---|---|-------|
| V | V | V     |
| V | F | F     |
| F | V | F     |
| F | F | F     |

**Operador O (OR):**
- Verdadero si AL MENOS UNA condición es verdadera

```
SI (es_fin_de_semana == Verdadero) O (es_festivo == Verdadero) ENTONCES
    ESCRIBIR "No hay clases"
FIN SI
```

**Tabla de verdad OR:**
| A | B | A O B |
|---|---|-------|
| V | V | V     |
| V | F | V     |
| F | V | V     |
| F | F | F     |

**Operador NO (NOT):**
- Invierte el valor de la condición

```
SI NO(esta_lloviendo) ENTONCES
    ESCRIBIR "Puedes salir a caminar"
FIN SI
```

**Combinación de operadores:**
```
SI (edad >= 13) Y (edad <= 19) ENTONCES
    ESCRIBIR "Es adolescente"
FIN SI

SI (dia == "Sábado") O (dia == "Domingo") ENTONCES
    ESCRIBIR "Es fin de semana"
FIN SI
```

### 4. Condicionales anidados

Un **condicional anidado** es un IF dentro de otro IF.

**Estructura:**
```
SI condición1 ENTONCES
    SI condición2 ENTONCES
        // Código si ambas condiciones son verdaderas
    FIN SI
FIN SI
```

**Ejemplo: Sistema de acceso**
```
LEER usuario
LEER contraseña

SI usuario == "admin" ENTONCES
    SI contraseña == "1234" ENTONCES
        ESCRIBIR "Acceso concedido"
        ESCRIBIR "Bienvenido Administrador"
    SINO
        ESCRIBIR "Contraseña incorrecta"
    FIN SI
SINO
    ESCRIBIR "Usuario no encontrado"
FIN SI
```

**Diagrama de flujo:**
```
    ╱──────────────╲
   ╱ ¿usuario OK?   ╲
  ╱                  ╲
 ╱   Sí        No     ╲
│     │         │      │
│     ▼         ▼      │
│ ╱──────────╲  Usuario│
│╱¿contraseña╲  incorrecto
││    OK?    │         │
│╲          ╱          │
│ ╲ Sí  No╱           │
│   │    │            │
│   ▼    ▼            │
│ Acceso Contraseña   │
│ OK     incorrecta   │
└──────────┬──────────┘
           ▼
```

## Implementación Práctica

### Ejercicio 1: Verificar edad para votar

**Problema:** Determinar si una persona puede votar según su edad.

**Pseudocódigo:**
```
INICIO
    ESCRIBIR "Ingrese su edad:"
    LEER edad
    
    SI edad >= 18 ENTONCES
        ESCRIBIR "Usted puede votar"
        ESCRIBIR "Es su derecho y responsabilidad cívica"
    SINO
        años_faltantes = 18 - edad
        ESCRIBIR "No puede votar aún"
        ESCRIBIR "Le faltan", años_faltantes, "años"
    FIN SI
FIN
```

**Casos de prueba:**
- Entrada: 20 → Salida: "Usted puede votar"
- Entrada: 15 → Salida: "No puede votar aún. Le faltan 3 años"
- Entrada: 18 → Salida: "Usted puede votar"

### Ejercicio 2: Calcular calificación con letra

**Problema:** Convertir una calificación numérica a letra (A, B, C, D, F).

**Pseudocódigo:**
```
INICIO
    LEER calificacion
    
    SI calificacion >= 90 ENTONCES
        letra = "A"
        mensaje = "Excelente"
    SINO SI calificacion >= 80 ENTONCES
        letra = "B"
        mensaje = "Muy bien"
    SINO SI calificacion >= 70 ENTONCES
        letra = "C"
        mensaje = "Bien"
    SINO SI calificacion >= 60 ENTONCES
        letra = "D"
        mensaje = "Suficiente"
    SINO
        letra = "F"
        mensaje = "Reprobado"
    FIN SI
    
    ESCRIBIR "Calificación:", letra
    ESCRIBIR "Comentario:", mensaje
FIN
```

### Ejercicio 3: Determinar el mayor de tres números

**Problema:** Encontrar el número mayor entre tres números ingresados.

**Pseudocódigo:**
```
INICIO
    LEER num1
    LEER num2
    LEER num3
    
    SI (num1 >= num2) Y (num1 >= num3) ENTONCES
        mayor = num1
    SINO SI (num2 >= num1) Y (num2 >= num3) ENTONCES
        mayor = num2
    SINO
        mayor = num3
    FIN SI
    
    ESCRIBIR "El número mayor es:", mayor
FIN
```

**Casos de prueba:**
- Entrada: 5, 3, 8 → Salida: 8
- Entrada: 10, 10, 5 → Salida: 10
- Entrada: -2, -5, -1 → Salida: -1


## Mejores Prácticas

### 1. Claridad en las Condiciones
- ✅ Usa paréntesis para clarificar condiciones complejas: `SI (edad >= 18) Y (tiene_permiso == Verdadero)`
- ✅ Mantén las condiciones simples y legibles
- ❌ Evita condiciones demasiado complejas en una sola línea

### 2. Orden de las Condiciones
- ✅ Coloca las condiciones más específicas primero
- ✅ Ordena de mayor a menor cuando uses rangos numéricos
- ✅ Considera casos especiales antes que casos generales

### 3. Manejo de Todos los Casos
- ✅ Siempre incluye un SINO para manejar casos no esperados
- ✅ Piensa en casos extremos (valores negativos, cero, muy grandes)
- ✅ Valida las entradas antes de procesarlas

### 4. Evita Redundancia
- ❌ Malo:
  ```
  SI edad >= 18 ENTONCES
      es_adulto = Verdadero
  SINO
      es_adulto = Falso
  FIN SI
  ```
- ✅ Mejor:
  ```
  es_adulto = (edad >= 18)
  ```

### 5. Legibilidad
- ✅ Usa nombres descriptivos para variables booleanas: `esta_aprobado`, `tiene_acceso`
- ✅ Indenta correctamente el código
- ✅ Comenta condiciones complejas

## Conceptos Clave para Recordar

- 🔑 **IF-ELSE**: Ejecuta un bloque u otro según una condición
- 🔑 **ELIF**: Evalúa múltiples condiciones en secuencia
- 🔑 **Operadores lógicos**: Y (AND), O (OR), NO (NOT)
- 🔑 **Condicionales anidados**: IF dentro de otro IF

## Próximos Pasos

En el Módulo 4 aprenderás sobre:
- Bucles MIENTRAS (WHILE)
- Bucles PARA (FOR)
- Repetición controlada de instrucciones
- Contadores y acumuladores

**¿Qué necesitas saber antes de continuar?**
✅ Cómo usar IF-ELSE  
✅ Combinar condiciones con operadores lógicos  
✅ Evaluar condiciones complejas  
✅ Anidar condicionales cuando sea necesario  

## Motivación Final

¡Felicitaciones! 🎉 Ahora tus programas pueden **pensar** y **tomar decisiones**.

Los condicionales son el corazón de la inteligencia en los programas. Con ellos puedes:
- Validar entradas del usuario
- Responder a diferentes situaciones
- Crear flujos de programa complejos
- Implementar lógica de negocio

Recuerda:
- Cada decisión que programas refleja tu pensamiento lógico
- Los condicionales están en el 95% de los programas
- Dominar los condicionales es dominar la lógica de programación

> "La lógica te lleva de A a B. La imaginación te lleva a todas partes, pero los condicionales deciden qué camino tomar." - Adaptado de Albert Einstein

**¡Ahora tus algoritmos son inteligentes! 🧠✨**

