# Retroalimentación y Soluciones - Módulo 1: Introducción a la Lógica de Programación

## Sección 1: Respuestas a Preguntas de Opción Múltiple

### Pregunta 1: ¿Qué es un algoritmo?
**Respuesta correcta: B) Una secuencia ordenada de pasos para resolver un problema**

**Explicación**: Un algoritmo es como una receta de cocina: una serie de instrucciones paso a paso que, si se siguen correctamente, llevan a la solución de un problema. No es un lenguaje de programación, ni una computadora, ni un error.

---

### Pregunta 2: ¿Cuál de las siguientes características NO es propia de un buen algoritmo?
**Respuesta correcta: C) Ambiguo**

**Explicación**: Un buen algoritmo debe ser todo lo contrario a ambiguo: debe ser PRECISO. Cada paso debe estar claramente definido sin dejar lugar a interpretaciones. Las características de un buen algoritmo son: preciso, finito, efectivo y ordenado.

---

### Pregunta 3: ¿Qué símbolo se usa en un diagrama de flujo para representar una decisión?
**Respuesta correcta: C) Rombo**

**Explicación**: En los diagramas de flujo:
- **Óvalo** = Inicio/Fin
- **Rectángulo** = Proceso/Acción
- **Rombo** = Decisión/Pregunta
- **Paralelogramo** = Entrada/Salida de datos

---

### Pregunta 4: ¿Cuál es el resultado de la operación 17 MOD 5?
**Respuesta correcta: B) 2**

**Explicación**: El operador MOD (módulo) devuelve el RESTO de una división.
- 17 ÷ 5 = 3 con resto 2
- Por lo tanto: 17 MOD 5 = 2
- Verificación: 5 × 3 = 15, y 17 - 15 = 2

---

### Pregunta 5: En el pensamiento computacional, ¿qué significa "descomposición"?
**Respuesta correcta: B) Dividir un problema grande en partes más pequeñas**

**Explicación**: La descomposición es una de las cuatro pilares del pensamiento computacional. Consiste en tomar un problema complejo y dividirlo en subproblemas más simples y manejables. Es como dividir la tarea de "organizar una fiesta" en: invitar personas, preparar comida, decorar, etc.

---

### Pregunta 6: ¿Cuál de estos NO es un operador de comparación?
**Respuesta correcta: C) &&**

**Explicación**: 
- `&&` es un operador LÓGICO (AND/Y), no de comparación
- Los operadores de comparación son: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Los operadores lógicos son: `&&` (Y), `||` (O), `!` (NO)

---

### Pregunta 7: ¿Qué es pseudocódigo?
**Respuesta correcta: C) Descripción de un algoritmo en lenguaje natural estructurado**

**Explicación**: El pseudocódigo es una forma de escribir algoritmos usando palabras comunes (como "LEER", "SI", "MIENTRAS") en lugar de la sintaxis estricta de un lenguaje de programación. Es una herramienta intermedia entre el pensamiento humano y el código real.

---

### Pregunta 8: ¿Cuál es el propósito principal de un diagrama de flujo?
**Respuesta correcta: B) Representar visualmente la lógica de un algoritmo**

**Explicación**: Los diagramas de flujo permiten visualizar el flujo lógico de un algoritmo de manera gráfica, facilitando su comprensión, análisis y comunicación. Son especialmente útiles para identificar problemas en la lógica antes de programar.

---

## Sección 2: Respuestas a Verdadero o Falso

### Pregunta 9: La lógica de programación depende del lenguaje de programación que uses.
**Respuesta correcta: Falso**

**Explicación**: ¡Este es un punto clave! La lógica de programación es INDEPENDIENTE del lenguaje. Un mismo algoritmo puede implementarse en Python, Java, C++, o cualquier otro lenguaje. La lógica es la IDEA, el lenguaje es solo la HERRAMIENTA para expresarla.

---

### Pregunta 10: Un algoritmo debe tener un número infinito de pasos.
**Respuesta correcta: Falso**

**Explicación**: Un algoritmo DEBE ser finito. Si un algoritmo nunca termina, no es útil. Debe tener un inicio claro y un fin alcanzable. Un bucle infinito accidental es un ERROR, no una característica deseable.

---

### Pregunta 11: El pseudocódigo puede ejecutarse directamente en una computadora.
**Respuesta correcta: Falso**

**Explicación**: El pseudocódigo es para HUMANOS, no para computadoras. Es una herramienta de diseño y planificación. Para ejecutar en una computadora, debes traducir el pseudocódigo a un lenguaje de programación real (Python, Java, etc.).

---

### Pregunta 12: Una variable puede cambiar su valor durante la ejecución de un programa.
**Respuesta correcta: Verdadero**

**Explicación**: Por eso se llama "variable" - porque su valor puede VARIAR. Ejemplo:
```
edad = 25
edad = 26  // La variable cambió su valor
```
Si el valor nunca cambia, es una CONSTANTE, no una variable.

---

### Pregunta 13: El operador lógico Y (AND) es verdadero si al menos una condición es verdadera.
**Respuesta correcta: Falso**

**Explicación**: Estás confundiendo AND con OR:
- **Y (AND)**: Verdadero solo si AMBAS condiciones son verdaderas
  - Verdadero Y Verdadero = Verdadero
  - Verdadero Y Falso = Falso
- **O (OR)**: Verdadero si AL MENOS UNA condición es verdadera
  - Verdadero O Falso = Verdadero

---

### Pregunta 14: En un diagrama de flujo, el óvalo se usa para representar procesos.
**Respuesta correcta: Falso**

**Explicación**: El óvalo se usa para INICIO y FIN. Los procesos se representan con RECTÁNGULOS. Recuerda:
- Óvalo → Inicio/Fin
- Rectángulo → Proceso
- Rombo → Decisión
- Paralelogramo → Entrada/Salida

---

## Sección 3: Soluciones a "Completa el Algoritmo"

### Ejercicio 15: Algoritmo para hacer un té

```
1. Inicio
2. Tomar una taza
3. Hervir agua (o Calentar agua)
4. Colocar la bolsita de té en la taza
5. Verter el agua caliente en la taza
6. Esperar 3-5 minutos
7. Retirar la bolsita de té
8. Agregar azúcar o miel (opcional)
9. Té listo (o Disfrutar el té)
10. Fin
```

**Nota**: Pueden existir variaciones válidas siempre que mantengan la lógica correcta.

---

### Ejercicio 16: Pseudocódigo para verificar número positivo

```
INICIO
    LEER numero
    SI numero > 0 ENTONCES
        ESCRIBIR "El número es positivo"
    SINO
        ESCRIBIR "El número es negativo o cero"
    FIN_SI
FIN
```

**Explicación**: Un número es positivo si es MAYOR que cero. Los números negativos y el cero no son positivos.

---

## Sección 4: Solución al Diagrama de Flujo

### Ejercicio 17: Diagrama para aprobado/reprobado

```
       ┌─────────┐
       │ Inicio  │
       └────┬────┘
            │
            ▼
    ┌───────────────┐
    │  Leer nota    │
    └───────┬───────┘
            │
            ▼
       ╱─────────╲
      ╱ nota >= 6? ╲
     ╱               ╲
    ╱     Sí    No    ╲
   │       │     │     │
   ▼       ▼     ▼     ▼
       ┌────────┐  ┌────────┐
       │"Aprobó"│  │"Reprobó"│
       └───┬────┘  └───┬────┘
           │           │
           └─────┬─────┘
                 ▼
            ┌─────────┐
            │   Fin   │
            └─────────┘
```

---

## Sección 5: Soluciones a Ejercicios de Pseudocódigo

### Ejercicio 18: Área de un rectángulo

```
INICIO
    LEER base
    LEER altura
    
    area = base * altura
    
    ESCRIBIR "El área del rectángulo es: ", area
FIN
```

**Fórmula**: Área = base × altura

---

### Ejercicio 19: Mayor de dos números

```
INICIO
    LEER numero1
    LEER numero2
    
    SI numero1 > numero2 ENTONCES
        ESCRIBIR "El mayor es: ", numero1
    SINO SI numero2 > numero1 ENTONCES
        ESCRIBIR "El mayor es: ", numero2
    SINO
        ESCRIBIR "Los números son iguales"
    FIN_SI
FIN
```

**Nota**: Es importante considerar el caso en que ambos números sean iguales.

---

### Ejercicio 20: Año bisiesto

```
INICIO
    LEER año
    
    SI (año MOD 400 == 0) ENTONCES
        ESCRIBIR "Es bisiesto"
    SINO SI (año MOD 100 == 0) ENTONCES
        ESCRIBIR "No es bisiesto"
    SINO SI (año MOD 4 == 0) ENTONCES
        ESCRIBIR "Es bisiesto"
    SINO
        ESCRIBIR "No es bisiesto"
    FIN_SI
FIN
```

**Reglas del año bisiesto:**
1. Si es divisible por 400 → ES bisiesto (ej: 2000)
2. Si es divisible por 100 → NO es bisiesto (ej: 1900)
3. Si es divisible por 4 → ES bisiesto (ej: 2024)
4. De lo contrario → NO es bisiesto (ej: 2023)

---

## Sección 6: Orientación para Resolución de Problemas

### Ejercicio 21: Algoritmo de la vida cotidiana

**Ejemplo: Preparar el desayuno**

```
1. Inicio
2. Ir a la cocina
3. Abrir el refrigerador
4. Sacar los huevos
5. Sacar la leche
6. Cerrar el refrigerador
7. Encender la estufa
8. Colocar sartén en la estufa
9. Agregar aceite al sartén
10. Romper dos huevos en el sartén
11. Cocinar durante 3 minutos
12. Servir en un plato
13. Apagar la estufa
14. Servir un vaso de leche
15. Desayuno listo
16. Fin
```

**Evaluación**: Tu algoritmo debe ser específico, ordenado y completo.

---

### Ejercicio 22: Pensamiento computacional - Organizar mochila

**Descomposición:**
1. Revisar horario de clases
2. Seleccionar libros necesarios
3. Seleccionar útiles escolares
4. Preparar lunch/merienda

**Reconocimiento de patrones:**
- Cada materia requiere: libro + cuaderno + útiles específicos
- Cada día sigo el mismo proceso de revisión

**Abstracción:**
- No importa el color de los cuadernos
- No importa la marca de los útiles
- Lo importante: tener todo lo necesario para las clases

**Algoritmo:**
1. Revisar horario del día siguiente
2. Para cada materia del día:
   - Guardar libro correspondiente
   - Guardar cuaderno correspondiente
   - Guardar útiles específicos
3. Agregar materiales generales (lapiceros, borrador)
4. Preparar y guardar lunch
5. Verificar que no falte nada
6. Cerrar mochila

---

### Ejercicio 23: Análisis de algoritmo

**a) ¿Qué hace este algoritmo?**
Cuenta la cantidad de dígitos que tiene un número.

**b) Si ingreso 1234, ¿qué resultado mostrará?**
"Dígitos: 4"

**Explicación del proceso:**
- Inicio: numero = 1234, contador = 0
- Iteración 1: numero = 123, contador = 1
- Iteración 2: numero = 12, contador = 2
- Iteración 3: numero = 1, contador = 3
- Iteración 4: numero = 0, contador = 4
- Fin del bucle, muestra: "Dígitos: 4"

**c) ¿Qué pasaría si ingreso 0?**
El bucle no se ejecuta (porque 0 no es mayor que 0), y mostraría "Dígitos: 0". 

**Nota**: Este es un caso especial que podría considerarse un error, ya que el número 0 tiene 1 dígito, no 0.

---

## Sección 7: Solución al Ejercicio Integrador

### Ejercicio 24: Cajero Automático Simplificado

**Pseudocódigo:**
```
INICIO
    LEER saldo_inicial
    
    ESCRIBIR "Saldo disponible: ", saldo_inicial
    ESCRIBIR "Ingrese cantidad a retirar: "
    LEER cantidad
    
    SI cantidad <= saldo_inicial ENTONCES
        saldo_inicial = saldo_inicial - cantidad
        ESCRIBIR "Retiro exitoso"
        ESCRIBIR "Nuevo saldo: ", saldo_inicial
    SINO
        ESCRIBIR "Error: Saldo insuficiente"
        ESCRIBIR "Saldo disponible: ", saldo_inicial
    FIN_SI
FIN
```

**Diagrama de flujo:**
```
       ┌─────────┐
       │ Inicio  │
       └────┬────┘
            │
            ▼
    ┌───────────────────┐
    │ Leer saldo_inicial│
    └────────┬──────────┘
            │
            ▼
    ┌───────────────────┐
    │ Leer cantidad     │
    └────────┬──────────┘
            │
            ▼
       ╱───────────────╲
      ╱ cantidad <=     ╲
     ╱  saldo_inicial?   ╲
    ╱      Sí       No     ╲
   │        │        │      │
   ▼        ▼        ▼      ▼
    ┌──────────────┐  ┌──────────────┐
    │saldo = saldo │  │"Saldo        │
    │- cantidad    │  │insuficiente" │
    └──────┬───────┘  └──────┬───────┘
           │                 │
           ▼                 │
    ┌──────────────┐         │
    │"Retiro       │         │
    │ exitoso"     │         │
    └──────┬───────┘         │
           │                 │
           ▼                 │
    ┌──────────────┐         │
    │Mostrar nuevo │         │
    │saldo         │         │
    └──────┬───────┘         │
           │                 │
           └────────┬────────┘
                    ▼
               ┌─────────┐
               │   Fin   │
               └─────────┘
```

---

## Sección 8: Soluciones a Evaluación de Expresiones

### Ejercicio 25

**a) 10 + 5 * 2 = 20**
Explicación: Primero la multiplicación (5 * 2 = 10), luego la suma (10 + 10 = 20)

**b) (10 + 5) * 2 = 30**
Explicación: Los paréntesis cambian el orden. Primero (10 + 5 = 15), luego (15 * 2 = 30)

**c) 20 / 4 - 3 = 2**
Explicación: Primero la división (20 / 4 = 5), luego la resta (5 - 3 = 2)

**d) 15 MOD 4 = 3**
Explicación: 15 ÷ 4 = 3 con resto 3, por lo tanto 15 MOD 4 = 3

**e) (5 > 3) Y (10 < 8) = Falso**
Explicación: 
- 5 > 3 es Verdadero
- 10 < 8 es Falso
- Verdadero Y Falso = Falso (ambas deben ser verdaderas para que Y sea verdadero)

**f) (5 > 3) O (10 < 8) = Verdadero**
Explicación:
- 5 > 3 es Verdadero
- 10 < 8 es Falso
- Verdadero O Falso = Verdadero (al menos una debe ser verdadera)

**g) NO(5 == 5) = Falso**
Explicación:
- 5 == 5 es Verdadero
- NO(Verdadero) = Falso (el operador NO invierte el valor)

---

## Consejos para Mejorar

### Si tuviste dificultades con:

**Algoritmos:**
- Practica describiendo actividades cotidianas en pasos
- Lee recetas de cocina (son algoritmos reales)
- Intenta explicar procesos a otras personas con máximo detalle

**Diagramas de flujo:**
- Dibuja diagramas para problemas simples primero
- Practica con situaciones de la vida real
- Usa herramientas online gratuitas para dibujar (draw.io, lucidchart)

**Pseudocódigo:**
- Lee mucho pseudocódigo antes de escribir el tuyo
- Empieza con problemas muy simples
- No te preocupes por la sintaxis perfecta, enfócate en la lógica

**Operadores:**
- Practica evaluando expresiones a mano
- Crea tarjetas de estudio con cada operador
- Resuelve ejercicios de matemáticas básicas

**Pensamiento computacional:**
- Aplícalo a problemas cotidianos
- Descompón tareas grandes en tu día a día
- Busca patrones en actividades repetitivas

---

## Recursos Adicionales Recomendados

1. **Para practicar lógica:**
   - Acertijos y rompecabezas lógicos
   - Sudoku y otros juegos de lógica
   - Khan Academy (sección de algoritmos)

2. **Para diagramas de flujo:**
   - draw.io (gratuito, online)
   - Lucidchart (gratuito para estudiantes)
   - Microsoft Visio

3. **Para ejercicios:**
   - PSeInt (software educativo para pseudocódigo)
   - Scratch (programación visual)

---

## Autoevaluación

**Calcula tu puntaje:**
- Opción múltiple: ___ de 8
- Verdadero/Falso: ___ de 6
- Ejercicios de completar: ___ de 2
- Pseudocódigo: ___ de 3
- Ejercicios complejos: ___ de 4
- Evaluación de expresiones: ___ de 7

**Total: ___ de 30 puntos**

**Interpretación:**
- 25-30 puntos: ¡Excelente! Dominas los conceptos fundamentales
- 20-24 puntos: Muy bien, comprendes la mayoría de los conceptos
- 15-19 puntos: Bien, pero necesitas repasar algunos temas
- Menos de 15: Repasa el módulo y practica más ejercicios

---

**¡Felicidades por completar el Módulo 1! Ahora estás listo para avanzar al Módulo 2. 🚀**
