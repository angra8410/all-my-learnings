# Módulo 1: Introducción a la Lógica de Programación

## Introducción

¡Bienvenido al fascinante mundo de la lógica de programación! Este es el punto de partida de tu viaje hacia el pensamiento computacional. Aquí aprenderás a pensar como un programador, incluso antes de escribir tu primera línea de código.

La lógica de programación es la base fundamental de todo desarrollo de software. Es la habilidad de dividir problemas complejos en pasos más simples y organizados que una computadora pueda ejecutar.

## ¿Qué es la Lógica de Programación?

La **lógica de programación** es la capacidad de organizar el pensamiento de manera estructurada para resolver problemas. Es como aprender a dar instrucciones tan claras y precisas que cualquiera (o cualquier máquina) pueda seguirlas sin confusión.

### Ejemplo de la Vida Cotidiana: Hacer un Sándwich

Imagina que le explicas a alguien que nunca ha hecho un sándwich cómo preparar uno:

**Instrucciones imprecisas:**
- Pon ingredientes en el pan

**Instrucciones con lógica de programación:**
1. Tomar dos rebanadas de pan
2. Colocar la primera rebanada en un plato
3. Agregar jamón sobre la rebanada
4. Agregar queso sobre el jamón
5. Colocar la segunda rebanada encima
6. Sándwich listo

La segunda versión es **secuencial**, **clara** y **específica**. ¡Así piensa un programador!

## ¿Por qué es importante?

La lógica de programación es importante porque:

1. **Es independiente del lenguaje**: Aprender lógica te permite programar en cualquier lenguaje (Python, Java, JavaScript, C++, etc.)

2. **Desarrolla el pensamiento analítico**: Te enseña a descomponer problemas grandes en partes manejables

3. **Mejora la resolución de problemas**: Aplicas esta habilidad no solo en programación, sino en la vida diaria

4. **Es la base de la automatización**: Permite crear soluciones que ahorran tiempo y esfuerzo

5. **Te diferencia como profesional**: La capacidad de pensar lógicamente es altamente valorada en cualquier industria

## Conceptos Principales

### 1. Algoritmo

Un **algoritmo** es una secuencia finita de pasos bien definidos para resolver un problema o realizar una tarea.

**Características de un buen algoritmo:**
- ✅ **Preciso**: Cada paso está claramente definido
- ✅ **Finito**: Tiene un inicio y un fin
- ✅ **Efectivo**: Resuelve el problema planteado
- ✅ **Ordenado**: Los pasos siguen una secuencia lógica

**Ejemplo: Algoritmo para cepillarse los dientes**
```
1. Inicio
2. Tomar el cepillo de dientes
3. Aplicar pasta dental en el cepillo
4. Abrir la llave del agua
5. Mojar el cepillo
6. Cerrar la llave
7. Cepillar los dientes durante 2 minutos
8. Abrir la llave
9. Enjuagar la boca
10. Enjuagar el cepillo
11. Cerrar la llave
12. Secar la boca
13. Fin
```

### 2. Pensamiento Computacional

El **pensamiento computacional** es la forma de razonar que permite:

- **Descomposición**: Dividir un problema grande en partes más pequeñas
- **Reconocimiento de patrones**: Identificar similitudes y repeticiones
- **Abstracción**: Enfocarse en lo importante, ignorar detalles innecesarios
- **Diseño de algoritmos**: Crear pasos ordenados para resolver el problema

**Ejemplo: Organizar una fiesta**

**Descomposición:**
- Invitar personas
- Preparar comida
- Decorar el lugar
- Organizar música

**Reconocimiento de patrones:**
- Cada invitado necesita: invitación + confirmación
- Cada platillo requiere: compra de ingredientes + preparación

**Abstracción:**
- No importa qué canción específica, solo que haya música
- No importa el color exacto de los globos, solo que decore

### 3. Diagramas de Flujo

Los **diagramas de flujo** son representaciones gráficas de un algoritmo. Usan símbolos estándar para representar diferentes tipos de operaciones:

**Símbolos principales:**

```
┌─────────┐
│  Inicio │  ← Óvalo: Inicio o Fin
│   Fin   │
└─────────┘

┌──────────────┐
│  Proceso o   │  ← Rectángulo: Acción o proceso
│  Acción      │
└──────────────┘

╱─────────────╲
│  ¿Decisión?  │  ← Rombo: Pregunta o decisión
╲─────────────╱

┌──────────────┐
│ Entrada o    │  ← Paralelogramo: Entrada/Salida de datos
│ Salida       │
└──────────────┘
```

**Ejemplo: Diagrama de flujo para determinar si hace frío**

```
    ┌─────────┐
    │ Inicio  │
    └────┬────┘
         │
         ▼
┌─────────────────┐
│ Leer temperatura│
└────────┬────────┘
         │
         ▼
    ╱────────────╲
   ╱ ¿Temp < 15°? ╲
  ╱                ╲
 ╱                  ╲
╱                    ╲
│     Sí  │  No      │
▼         ▼          ▼
┌──────────┐  ┌──────────┐
│"Hace frío"│  │"No hace  │
│           │  │ frío"    │
└─────┬────┘  └────┬─────┘
      │            │
      └──────┬─────┘
             ▼
        ┌─────────┐
        │   Fin   │
        └─────────┘
```

### 4. Pseudocódigo

El **pseudocódigo** es una forma de escribir algoritmos usando lenguaje natural estructurado, similar al código real pero sin la sintaxis estricta de un lenguaje de programación.

**Ejemplo: Verificar si un número es par**

```
INICIO
    LEER numero
    SI numero MOD 2 == 0 ENTONCES
        ESCRIBIR "El número es par"
    SINO
        ESCRIBIR "El número es impar"
    FIN_SI
FIN
```

**Ventajas del pseudocódigo:**
- Fácil de entender para cualquier persona
- No depende de un lenguaje específico
- Permite enfocarse en la lógica, no en la sintaxis
- Facilita la comunicación entre programadores

### 5. Variables y Datos

Una **variable** es un espacio en la memoria que almacena un valor que puede cambiar durante la ejecución del programa.

Piensa en las variables como **cajas etiquetadas** donde guardas información:

```
┌──────────────┐
│  edad = 25   │  ← Caja llamada "edad" que contiene el valor 25
└──────────────┘

┌──────────────┐
│ nombre="Ana" │  ← Caja llamada "nombre" que contiene "Ana"
└──────────────┘
```

**Tipos de datos básicos:**

- **Números enteros**: 1, 42, -5, 0
- **Números decimales**: 3.14, -2.5, 0.001
- **Texto (cadenas)**: "Hola", "Python", "123"
- **Booleanos**: Verdadero o Falso

### 6. Operadores Básicos

Los **operadores** son símbolos que realizan operaciones sobre valores y variables:

**Operadores aritméticos:**
- `+` Suma: 5 + 3 = 8
- `-` Resta: 5 - 3 = 2
- `*` Multiplicación: 5 * 3 = 15
- `/` División: 6 / 2 = 3
- `MOD` Módulo (resto): 7 MOD 3 = 1

**Operadores de comparación:**
- `==` Igual a: 5 == 5 → Verdadero
- `!=` Diferente de: 5 != 3 → Verdadero
- `>` Mayor que: 5 > 3 → Verdadero
- `<` Menor que: 3 < 5 → Verdadero
- `>=` Mayor o igual: 5 >= 5 → Verdadero
- `<=` Menor o igual: 3 <= 5 → Verdadero

**Operadores lógicos:**
- `Y (AND)`: Verdadero si ambas condiciones son verdaderas
- `O (OR)`: Verdadero si al menos una condición es verdadera
- `NO (NOT)`: Invierte el valor (Verdadero → Falso, Falso → Verdadero)

## Implementación Práctica

### Ejercicio 1: Tu Primer Algoritmo

Escribe un algoritmo para preparar una taza de café:

```
1. Inicio
2. Tomar una taza
3. Agregar café instantáneo a la taza
4. Hervir agua
5. Verter agua caliente en la taza
6. Agregar azúcar (opcional)
7. Agregar leche (opcional)
8. Revolver la mezcla
9. Esperar 1 minuto
10. El café está listo
11. Fin
```

### Ejercicio 2: Crear un Diagrama de Flujo Simple

**Problema**: Determinar si una persona puede votar (edad >= 18)

```
    ┌─────────┐
    │ Inicio  │
    └────┬────┘
         │
         ▼
┌─────────────────┐
│   Leer edad     │
└────────┬────────┘
         │
         ▼
    ╱────────────╲
   ╱ ¿edad >= 18? ╲
  ╱                ╲
 ╱      Sí    No    ╲
│         │    │     │
▼         ▼    ▼     ▼
      ┌────────┐  ┌────────┐
      │"Puede  │  │"No puede│
      │ votar" │  │ votar" │
      └───┬────┘  └───┬────┘
          │           │
          └─────┬─────┘
                ▼
           ┌─────────┐
           │   Fin   │
           └─────────┘
```

### Ejercicio 3: Pseudocódigo para Calcular el Promedio

```
INICIO
    LEER nota1
    LEER nota2
    LEER nota3
    
    promedio = (nota1 + nota2 + nota3) / 3
    
    ESCRIBIR "El promedio es: ", promedio
    
    SI promedio >= 7 ENTONCES
        ESCRIBIR "Aprobado"
    SINO
        ESCRIBIR "Reprobado"
    FIN_SI
FIN
```

### Ejercicio 4: Problema del Número Mayor

**Pseudocódigo para encontrar el mayor de tres números:**

```
INICIO
    LEER numero1
    LEER numero2
    LEER numero3
    
    SI (numero1 > numero2) Y (numero1 > numero3) ENTONCES
        mayor = numero1
    SINO SI (numero2 > numero1) Y (numero2 > numero3) ENTONCES
        mayor = numero2
    SINO
        mayor = numero3
    FIN_SI
    
    ESCRIBIR "El número mayor es: ", mayor
FIN
```

## Mejores Prácticas

### 1. Claridad sobre Complejidad
- ✅ Escribe algoritmos simples y fáciles de entender
- ✅ Usa nombres descriptivos para variables: `edad_estudiante` mejor que `e`
- ❌ No compliques innecesariamente la solución

### 2. Planifica Antes de Programar
- ✅ Dibuja un diagrama de flujo o escribe pseudocódigo primero
- ✅ Identifica claramente el problema a resolver
- ✅ Piensa en casos especiales y excepciones

### 3. Divide y Conquista
- ✅ Separa problemas grandes en subproblemas más pequeños
- ✅ Resuelve cada parte por separado
- ✅ Combina las soluciones al final

### 4. Prueba Mentalmente
- ✅ "Ejecuta" tu algoritmo mentalmente con datos de ejemplo
- ✅ Verifica que funcione en casos normales y extremos
- ✅ Asegúrate de que siempre llegue a un fin

### 5. Documenta tu Razonamiento
- ✅ Agrega comentarios explicando "por qué" haces algo
- ✅ Anota suposiciones importantes
- ✅ Describe casos especiales

## Conceptos Clave para Recordar

- 🔑 **Algoritmo**: Secuencia ordenada y finita de pasos para resolver un problema
- 🔑 **Pensamiento Computacional**: Habilidad de descomponer, abstraer y crear soluciones sistemáticas
- 🔑 **Diagrama de Flujo**: Representación gráfica de un algoritmo usando símbolos estándar
- 🔑 **Pseudocódigo**: Descripción de un algoritmo en lenguaje natural estructurado
- 🔑 **Variable**: Espacio de memoria que almacena un valor que puede cambiar
- 🔑 **Operadores**: Símbolos que realizan operaciones (aritméticas, comparación, lógicas)

## Próximos Pasos

En el Módulo 2 aprenderás sobre:
- Secuencias y ejecución lineal de instrucciones
- Entrada y salida de datos
- Expresiones y asignaciones
- Trazas de algoritmos

**¿Qué necesitas saber antes de continuar?**
✅ Qué es un algoritmo  
✅ Cómo crear un diagrama de flujo básico  
✅ Qué es el pseudocódigo  
✅ Conceptos de variables y operadores  

## Motivación Final

¡Felicidades por completar el Módulo 1! 🎉

Has dado el primer paso más importante: **aprender a pensar lógicamente**. 

Recuerda:
- Todo programador experto comenzó donde estás ahora
- La lógica de programación es una habilidad que se desarrolla con práctica
- Cada problema que resuelves fortalece tu pensamiento computacional
- No necesitas memorizar, necesitas entender

> "La lógica te llevará de A a B. La imaginación te llevará a todas partes." - Albert Einstein

**La lógica de programación es tu superpoder.** Con ella, puedes crear soluciones a problemas reales, automatizar tareas, y dar vida a tus ideas. ¡El único límite es tu creatividad!

**¡Estás listo para el Módulo 2! 🚀**
