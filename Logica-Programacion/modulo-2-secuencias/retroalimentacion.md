# Retroalimentación y Soluciones - Módulo 2: Secuencias

## Sección 1: Respuestas a Preguntas de Opción Múltiple

### Pregunta 1: ¿Qué es una secuencia en programación?
**Respuesta correcta: A) Un conjunto de instrucciones que se ejecutan en orden**

**Explicación**: Una secuencia es la estructura más básica donde cada instrucción se ejecuta una después de otra, en el orden exacto en que aparecen. Es como seguir una receta paso a paso.

---

### Pregunta 2: ¿Cuál es el orden correcto de una secuencia básica?
**Respuesta correcta: C) Entrada → Procesamiento → Salida**

**Explicación**: Primero LEES los datos (entrada), luego los PROCESAS (cálculos), y finalmente MUESTRAS el resultado (salida). Este es el patrón fundamental de la programación.

---

### Pregunta 3: ¿Qué hace la instrucción `a = a + 1`?
**Respuesta correcta: B) Incrementa el valor de a en 1**

**Explicación**: Esta instrucción:
1. Lee el valor actual de `a`
2. Le suma 1
3. Guarda el resultado nuevamente en `a`
Es muy común para contadores.

---

### Pregunta 4: En una traza de algoritmo, ¿qué información registramos?
**Respuesta correcta: B) Los valores de las variables en cada paso**

**Explicación**: Una traza documenta cómo cambian los valores de las variables después de cada instrucción, permitiéndonos seguir la ejecución del algoritmo paso a paso.

---

### Pregunta 5: ¿Qué es una expresión?
**Respuesta correcta: B) Una combinación de valores y operadores que produce un resultado**

**Explicación**: Una expresión combina valores, variables y operadores para calcular un resultado. Por ejemplo: `area = base * altura` o `total = precio * cantidad`.

---

## Sección 2: Respuestas a Verdadero o Falso

### Pregunta 6: En una secuencia, las instrucciones pueden ejecutarse en cualquier orden.
**Respuesta correcta: Falso**

**Explicación**: ¡El orden es CRUCIAL en las secuencias! Las instrucciones se ejecutan en el orden exacto en que aparecen. Cambiar el orden puede cambiar completamente el resultado o causar errores.

---

### Pregunta 7: Puedes usar una variable antes de asignarle un valor.
**Respuesta correcta: Falso**

**Explicación**: Intentar usar una variable sin valor es un ERROR. Primero debes asignarle un valor:
```
correcto:
x = 5
y = x + 2

incorrecto:
y = x + 2  // Error: x no tiene valor
x = 5
```

---

### Pregunta 8: La instrucción `nombre = "Juan"` es una asignación.
**Respuesta correcta: Verdadero**

**Explicación**: Esta es una asignación que guarda el texto "Juan" en la variable `nombre`. El operador `=` se usa para asignar valores.

---

### Pregunta 9: Una traza ayuda a depurar algoritmos.
**Respuesta correcta: Verdadero**

**Explicación**: Hacer trazas es una técnica fundamental para encontrar errores. Te permite ver exactamente qué valor tiene cada variable en cada momento.

---

## Sección 3: Soluciones a Trazas

### Ejercicio 10: Traza completa

| Paso | Instrucción | x | y | z |
|------|-------------|---|---|---|
| 1    | x = 5       | 5 | ? | ? |
| 2    | y = 10      | 5 | 10| ? |
| 3    | z = x + y   | 5 | 10| 15|
| 4    | x = z * 2   | 30| 10| 15|
| 5    | y = x - z   | 30| 15| 15|

**Valores finales:**
- x = 30
- y = 15
- z = 15

---

### Ejercicio 11: Traza con MOD y división

| Paso | Instrucción | a | b | c |
|------|-------------|---|---|---|
| 1    | a = 8       | 8 | ? | ? |
| 2    | b = 3       | 8 | 3 | ? |
| 3    | c = a MOD b | 8 | 3 | 2 |
| 4    | a = a / b   | 2 | 3 | 2 |
| 5    | b = c + a   | 2 | 4 | 2 |

**Valores finales:**
- a = 2 (8 / 3 = 2 en división entera)
- b = 4
- c = 2 (8 MOD 3 = 2, resto de 8÷3)

---

## Sección 4: Soluciones a Completar Algoritmos

### Ejercicio 12: Área de un triángulo

```
INICIO
    LEER base
    LEER altura
    
    area = (base * altura) / 2
    
    ESCRIBIR "El área es:", area
FIN
```

**Fórmula**: Área del triángulo = (base × altura) / 2

---

### Ejercicio 13: Intercambio de variables

```
INICIO
    a = 10
    b = 20
    
    temp = a
    a = b
    b = temp
    
    ESCRIBIR "a =", a, "b =", b
FIN
```

**Resultado**: a = 20, b = 10

---

## Sección 5: Soluciones a Pseudocódigo

### Ejercicio 14: Operaciones básicas

```
INICIO
    LEER numero1
    LEER numero2
    
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    division = numero1 / numero2
    
    ESCRIBIR "Suma:", suma
    ESCRIBIR "Resta:", resta
    ESCRIBIR "Multiplicación:", multiplicacion
    ESCRIBIR "División:", division
FIN
```

---

### Ejercicio 15: Conversión de kilómetros

```
INICIO
    LEER kilometros
    
    metros = kilometros * 1000
    centimetros = kilometros * 100000
    
    ESCRIBIR kilometros, "km equivalen a:"
    ESCRIBIR metros, "metros"
    ESCRIBIR centimetros, "centímetros"
FIN
```

**Conversiones:**
- 1 km = 1000 m
- 1 km = 100,000 cm

---

### Ejercicio 16: Precio con descuento

```
INICIO
    LEER precio_original
    LEER porcentaje_descuento
    
    descuento = precio_original * (porcentaje_descuento / 100)
    precio_final = precio_original - descuento
    
    ESCRIBIR "Precio original:", precio_original
    ESCRIBIR "Descuento:", descuento
    ESCRIBIR "Precio final:", precio_final
FIN
```

**Ejemplo:** Precio = 100, Descuento = 20%
- descuento = 100 * 0.20 = 20
- precio_final = 100 - 20 = 80

---

## Sección 6: Soluciones a Expresiones

### Ejercicio 17: Evaluación con a=10, b=5, c=2

**a) `a + b * c = 20`**
- Primero: 5 * 2 = 10
- Luego: 10 + 10 = 20

**b) `(a + b) * c = 30`**
- Primero: (10 + 5) = 15
- Luego: 15 * 2 = 30

**c) `a / b + c = 4`**
- Primero: 10 / 5 = 2
- Luego: 2 + 2 = 4

**d) `a MOD (b - c) = 1`**
- Primero: (5 - 2) = 3
- Luego: 10 MOD 3 = 1

**e) `b * c - a / b = 8`**
- Primero: 5 * 2 = 10
- Luego: 10 / 5 = 2
- Finalmente: 10 - 2 = 8

---

## Sección 7: Soluciones a Detección de Errores

### Ejercicio 18: Error de orden

**Error encontrado:** Se intenta mostrar `resultado` antes de calcularla.

**Solución:**
```
INICIO
    LEER numero1
    LEER numero2
    resultado = numero1 + numero2
    ESCRIBIR "Resultado:", resultado
FIN
```

---

### Ejercicio 19: Fórmula incorrecta

**Error:** La fórmula del área del círculo está incompleta. Falta elevar el radio al cuadrado.

**Corrección:**
```
INICIO
    LEER radio
    area = 3.14 * radio * radio
    ESCRIBIR "Área del círculo:", area
FIN
```

**Fórmula correcta:** A = π × r²

---

## Sección 8: Solución al Ejercicio Integrador

### Ejercicio 20: Calculadora de Viaje

```
INICIO
    // Entrada de datos
    ESCRIBIR "Ingrese distancia del viaje (km):"
    LEER distancia_km
    
    ESCRIBIR "Ingrese consumo del auto (litros/km):"
    LEER consumo_por_km
    
    ESCRIBIR "Ingrese precio del combustible (por litro):"
    LEER precio_por_litro
    
    // Procesamiento
    litros_necesarios = distancia_km * consumo_por_km
    costo_total = litros_necesarios * precio_por_litro
    
    // Salida
    ESCRIBIR "=== RESUMEN DEL VIAJE ==="
    ESCRIBIR "Distancia:", distancia_km, "km"
    ESCRIBIR "Litros necesarios:", litros_necesarios, "L"
    ESCRIBIR "Costo total:", costo_total
FIN
```

**Ejemplo de ejecución:**
- Entrada: 100 km, 0.08 L/km, $1.50/L
- Proceso: 100 * 0.08 = 8 litros, 8 * 1.50 = $12
- Salida: 8 litros, costo $12

---

## Consejos para Mejorar

### Si tuviste dificultades con:

**Trazas:**
- Practica haciendo trazas en papel
- Usa una tabla para organizar valores
- Revisa cada paso lentamente
- Verifica el orden de las operaciones

**Orden de ejecución:**
- Recuerda: siempre de arriba hacia abajo
- No puedes usar una variable antes de crearla
- Lee → Procesa → Muestra

**Expresiones:**
- Recuerda el orden de operaciones (paréntesis primero)
- Practica evaluando expresiones paso a paso
- Usa paréntesis cuando tengas dudas

**Asignaciones:**
- El lado derecho se EVALÚA primero
- El resultado se GUARDA en la variable del lado izquierdo
- `a = a + 1` es válido y común

---

## Autoevaluación

**Calcula tu puntaje:**
- Opción múltiple: ___ de 5
- Verdadero/Falso: ___ de 4
- Trazas: ___ de 2
- Completar: ___ de 2
- Pseudocódigo: ___ de 3
- Expresiones: ___ de 5
- Errores: ___ de 2
- Integrador: ___ de 1

**Total: ___ de 24 puntos**

**Interpretación:**
- 20-24: ¡Excelente! Dominas las secuencias
- 15-19: Muy bien, comprendes el concepto
- 10-14: Bien, pero repasa algunos temas
- Menos de 10: Repasa el módulo y practica más

---

**¡Felicidades por completar el Módulo 2! Ahora dominas las secuencias. 🚀**
