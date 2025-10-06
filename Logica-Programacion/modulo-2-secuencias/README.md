# Módulo 2: Secuencias

## Introducción

¡Bienvenido al Módulo 2! Ahora que comprendes qué es un algoritmo y cómo pensarlo lógicamente, es momento de profundizar en las **secuencias**: la forma más básica y fundamental de estructurar un algoritmo.

Una secuencia es simplemente un conjunto de instrucciones que se ejecutan **una después de otra**, en orden estricto, de arriba hacia abajo. Es la base sobre la que se construyen todos los programas.

## ¿Qué es una Secuencia?

Una **secuencia** es una estructura de control donde las instrucciones se ejecutan en el orden exacto en que aparecen, sin saltos ni repeticiones.

### Analogía: Preparar un Café

```
1. Llenar la tetera con agua
2. Encender la estufa
3. Colocar la tetera en la estufa
4. Esperar que hierva el agua
5. Verter agua en la taza con café
6. Agregar azúcar
7. Revolver
```

Cada paso DEBE ejecutarse en orden. No puedes revolver antes de verter el agua, ni verter agua antes de que hierva.

## ¿Por qué son importantes?

Las secuencias son importantes porque:

1. **Son la base de todo**: Incluso los programas más complejos están compuestos por secuencias
2. **Garantizan el orden**: Aseguran que las operaciones se realicen en el momento correcto
3. **Son predecibles**: Siempre producen el mismo resultado con las mismas entradas
4. **Facilitan la depuración**: Es fácil seguir el flujo de ejecución paso a paso

## Conceptos Principales

### 1. Ejecución Lineal

La **ejecución lineal** significa que el programa avanza de una línea a la siguiente, sin interrupciones.

**Diagrama de flujo:**
```
    ┌─────────┐
    │ Inicio  │
    └────┬────┘
         │
         ▼
    ┌─────────┐
    │ Paso 1  │
    └────┬────┘
         │
         ▼
    ┌─────────┐
    │ Paso 2  │
    └────┬────┘
         │
         ▼
    ┌─────────┐
    │ Paso 3  │
    └────┬────┘
         │
         ▼
    ┌─────────┐
    │   Fin   │
    └─────────┘
```

### 2. Entrada de Datos

La **entrada** es el proceso de recibir información del usuario o de otra fuente.

**Pseudocódigo:**
```
LEER nombre
LEER edad
LEER ciudad
```

**Ejemplo en la vida real:**
- Un cajero automático PIDE tu PIN (entrada)
- Un formulario web SOLICITA tu email (entrada)
- Una calculadora RECIBE los números (entrada)

### 3. Procesamiento

El **procesamiento** es cuando realizamos operaciones con los datos recibidos.

**Pseudocódigo:**
```
LEER radio
area = 3.14159 * radio * radio
perimetro = 2 * 3.14159 * radio
```

**Tipos de procesamiento:**
- Cálculos matemáticos
- Transformaciones de datos
- Concatenación de texto
- Comparaciones

### 4. Salida de Datos

La **salida** es mostrar resultados al usuario o enviarlos a otro sistema.

**Pseudocódigo:**
```
ESCRIBIR "El área es: ", area
ESCRIBIR "El perímetro es: ", perimetro
```

**Ejemplo en la vida real:**
- Un cajero MUESTRA tu saldo (salida)
- Una calculadora MUESTRA el resultado (salida)
- Una app ENVÍA una notificación (salida)

### 5. Asignación de Variables

La **asignación** es guardar un valor en una variable.

**Sintaxis general:**
```
variable = valor
```

**Ejemplos:**
```
nombre = "María"
edad = 25
altura = 1.65
es_estudiante = Verdadero
```

**Reglas importantes:**
- El valor de la derecha se almacena en la variable de la izquierda
- Una variable puede cambiar su valor
- Puedes usar el valor anterior de una variable para calcular el nuevo

**Ejemplo:**
```
contador = 0
contador = contador + 1  // Ahora contador vale 1
contador = contador + 1  // Ahora contador vale 2
```

### 6. Expresiones

Una **expresión** es una combinación de valores, variables y operadores que produce un resultado.

**Expresiones aritméticas:**
```
total = precio * cantidad
promedio = (nota1 + nota2 + nota3) / 3
area = base * altura / 2
```

**Expresiones con texto:**
```
nombre_completo = nombre + " " + apellido
mensaje = "Hola, " + nombre + "!"
```

**Expresiones mixtas:**
```
mensaje = "Tu edad es: " + edad
resultado = "Total a pagar: $" + (precio * cantidad)
```

### 7. Trazas de Algoritmos

Una **traza** es el seguimiento paso a paso de la ejecución de un algoritmo, anotando los valores de las variables en cada momento.

**Ejemplo de algoritmo:**
```
INICIO
    a = 10
    b = 5
    c = a + b
    a = c * 2
    b = a - c
    ESCRIBIR a, b, c
FIN
```

**Tabla de traza:**

| Paso | Instrucción | a | b | c | Salida |
|------|-------------|---|---|---|--------|
| 1    | a = 10      | 10| ? | ? |        |
| 2    | b = 5       | 10| 5 | ? |        |
| 3    | c = a + b   | 10| 5 | 15|        |
| 4    | a = c * 2   | 30| 5 | 15|        |
| 5    | b = a - c   | 30| 15| 15|        |
| 6    | ESCRIBIR    | 30| 15| 15| 30 15 15|

## Implementación Práctica

### Ejercicio 1: Intercambio de Valores

**Problema:** Intercambiar los valores de dos variables.

**Pseudocódigo:**
```
INICIO
    LEER a
    LEER b
    
    ESCRIBIR "Antes del intercambio:"
    ESCRIBIR "a =", a
    ESCRIBIR "b =", b
    
    // Intercambio usando variable temporal
    temp = a
    a = b
    b = temp
    
    ESCRIBIR "Después del intercambio:"
    ESCRIBIR "a =", a
    ESCRIBIR "b =", b
FIN
```

**Ejemplo de ejecución:**
- Entrada: a = 5, b = 10
- Salida: a = 10, b = 5

### Ejercicio 2: Calcular Promedio

**Pseudocódigo:**
```
INICIO
    LEER calificacion1
    LEER calificacion2
    LEER calificacion3
    
    suma = calificacion1 + calificacion2 + calificacion3
    promedio = suma / 3
    
    ESCRIBIR "El promedio es:", promedio
FIN
```

### Ejercicio 3: Conversión de Temperatura

**Pseudocódigo:**
```
INICIO
    ESCRIBIR "Ingrese temperatura en Celsius:"
    LEER celsius
    
    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15
    
    ESCRIBIR "Temperatura en Fahrenheit:", fahrenheit
    ESCRIBIR "Temperatura en Kelvin:", kelvin
FIN
```

### Ejercicio 4: Calcular Área y Perímetro de un Rectángulo

**Pseudocódigo:**
```
INICIO
    LEER base
    LEER altura
    
    area = base * altura
    perimetro = 2 * (base + altura)
    
    ESCRIBIR "Área:", area
    ESCRIBIR "Perímetro:", perimetro
FIN
```

## Mejores Prácticas

### 1. Orden Lógico
- ✅ Lee todos los datos necesarios ANTES de procesarlos
- ✅ Procesa los datos ANTES de mostrar resultados
- ❌ No intentes usar una variable antes de asignarle un valor

### 2. Nombres Descriptivos
- ✅ `precio_total`, `nombre_completo`, `edad_estudiante`
- ❌ `x`, `a1`, `temp2`

### 3. Comentarios Útiles
- ✅ Explica el "por qué", no el "qué"
- ✅ Documenta fórmulas complejas
- ✅ Anota las unidades de medida

**Ejemplo:**
```
// Convertir de Celsius a Fahrenheit
// Fórmula: F = (C × 9/5) + 32
fahrenheit = (celsius * 9/5) + 32
```

### 4. Validación Mental
- ✅ Haz una traza en papel antes de ejecutar
- ✅ Usa valores de ejemplo simples
- ✅ Verifica el orden de las operaciones

### 5. Inicialización Clara
- ✅ Asigna valores iniciales explícitos
- ✅ No asumas que una variable vale 0 automáticamente

## Conceptos Clave para Recordar

- 🔑 **Secuencia**: Instrucciones que se ejecutan en orden, una tras otra
- 🔑 **Entrada**: Recibir datos del usuario o del sistema
- 🔑 **Procesamiento**: Realizar operaciones con los datos
- 🔑 **Salida**: Mostrar o enviar resultados
- 🔑 **Asignación**: Guardar un valor en una variable (variable = valor)
- 🔑 **Expresión**: Combinación de valores y operadores que produce un resultado
- 🔑 **Traza**: Seguimiento paso a paso de la ejecución de un algoritmo

## Próximos Pasos

En el Módulo 3 aprenderás sobre:
- Condicionales (if/else)
- Toma de decisiones en algoritmos
- Flujos alternativos
- Condiciones compuestas

**¿Qué necesitas saber antes de continuar?**
✅ Cómo funciona la ejecución secuencial  
✅ Entrada, procesamiento y salida  
✅ Asignación de variables  
✅ Cómo hacer una traza de algoritmo  

## Motivación Final

¡Excelente progreso! 🎉

Ya dominas las **secuencias**, que son el 80% de cualquier programa básico. Ahora puedes:
- Leer datos del usuario
- Procesarlos matemáticamente
- Mostrar resultados

Recuerda:
- Las secuencias son simples pero poderosas
- Incluso algoritmos complejos se construyen con secuencias
- Hacer trazas te ayuda a entender y depurar algoritmos

> "Un viaje de mil millas comienza con un solo paso." - Lao Tzu

**¡Cada línea de código que escribes te acerca a tus metas! 🚀**
