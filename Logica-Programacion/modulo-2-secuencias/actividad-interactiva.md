# Actividades Interactivas - Módulo 2: Secuencias

## Sección 1: Preguntas de Opción Múltiple

### Pregunta 1
**¿Qué es una secuencia en programación?**

A) Un conjunto de instrucciones que se ejecutan en orden
B) Una estructura de repetición
C) Una decisión entre dos opciones
D) Un error en el código

A

### Pregunta 2
**¿Cuál es el orden correcto de una secuencia básica?**

A) Salida → Procesamiento → Entrada
B) Entrada → Salida → Procesamiento
C) Entrada → Procesamiento → Salida
D) Procesamiento → Entrada → Salida

C

### Pregunta 3
**¿Qué hace la instrucción `a = a + 1`?**

A) Compara si a es igual a a + 1
B) Incrementa el valor de a en 1
C) Genera un error
D) No hace nada

B

### Pregunta 4
**En una traza de algoritmo, ¿qué información registramos?**

A) Solo el resultado final
B) Los valores de las variables en cada paso
C) Solo los errores
D) El tiempo de ejecución

B

### Pregunta 5
**¿Qué es una expresión?**

A) Un comentario en el código
B) Una combinación de valores y operadores que produce un resultado
C) Una variable
D) Un mensaje de error

B

## Sección 2: Verdadero o Falso

### Pregunta 6
**En una secuencia, las instrucciones pueden ejecutarse en cualquier orden.**

- [ ] Verdadero
- [X] Falso

---

### Pregunta 7
**Puedes usar una variable antes de asignarle un valor.**

- [ ] Verdadero
- [X] Falso

---

### Pregunta 8
**La instrucción `nombre = "Juan"` es una asignación.**

- [X] Verdadero
- [ ] Falso

---

### Pregunta 9
**Una traza ayuda a depurar algoritmos.**

- [X] Verdadero
- [ ] Falso

---

## Sección 3: Traza de Algoritmos

### Ejercicio 10
**Realiza la traza del siguiente algoritmo:**

```
INICIO            x    y     z
    x = 5         5    ?     ?
    y = 10        5    10    ?
    z = x + y     5    10    15
    x = z * 2     30   10    15    
    y = x - z     15   15    30
  
FIN
```

**Completa la tabla:**

| Paso | Instrucción | x | y | z |
|------|-------------|---|---|---|
| 1    | x = 5       | 5 | ? | ? |
| 2    | y = 10      | 5 |10 | ? |
| 3    | z = x + y   | 5 |10 |15 |
| 4    | x = z * 2   | 5 |10 |30 |
| 5    | y = x - z   |10 |5  |-30|

**Valores finales:**
- x = 30_____
- y = -25_____
- z = 15_____

---

### Ejercicio 11
**Traza el siguiente algoritmo:**

```
INICIO
    a = 8
    b = 3
    c = a MOD b
    a = a / b
    b = c + a
FIN
```
| Paso | Instrucción | a | b | c |
|------|-------------|---|---|---|
| 1    | a = 8       |8  |?  |?  |
| 2    | b = 3       |8  |3  |?  |
| 3    | c = a MOD b |8  |3  |2  |
| 4    | a = a / b   |2.6|3  |2  |
| 5    | b = c + a   |2.6|   |2  |

**Valores finales:**
- a = 2.6_____
- b = 4.6_____
- c = 2_____

---

## Sección 4: Completar Algoritmos

### Ejercicio 12
**Completa el algoritmo para calcular el área de un triángulo:**

```
INICIO
    LEER base
    LEER _________
    
    area = _______________
    
    ESCRIBIR "El área es:", _____
FIN
```

---

### Ejercicio 13
**Completa el algoritmo para intercambiar dos variables:**

```
INICIO
    a = 10
    b = 20
    
    temp = _____
    a = _____
    b = _____
    
    ESCRIBIR "a =", a, "b =", b
FIN
```

---

## Sección 5: Escribir Pseudocódigo

### Ejercicio 14
**Escribe un algoritmo que lea dos números y calcule su suma, resta, multiplicación y división.**

```









```

---

### Ejercicio 15
**Escribe un algoritmo para convertir de kilómetros a metros y centímetros.**

```









```

---

### Ejercicio 16
**Escribe un algoritmo para calcular el precio final de un producto con descuento.**

**Entrada:** precio original, porcentaje de descuento
**Salida:** precio final

```









```

---

## Sección 6: Análisis de Expresiones

### Ejercicio 17
**Evalúa las siguientes expresiones si a = 10, b = 5, c = 2:**

a) `a + b * c = _____`

b) `(a + b) * c = _____`

c) `a / b + c = _____`

d) `a MOD (b - c) = _____`

e) `b * c - a / b = _____`

---

## Sección 7: Detección de Errores

### Ejercicio 18
**Identifica el error en este algoritmo:**

```
INICIO
    ESCRIBIR "Resultado:", resultado
    LEER numero1
    LEER numero2
    resultado = numero1 + numero2
FIN
```

**Error encontrado:**
_______________________________________________

**Solución:**
_______________________________________________

---

### Ejercicio 19
**¿Qué está mal en este algoritmo?**

```
INICIO
    LEER radio
    area = 3.14 * radio
    ESCRIBIR "Área del círculo:", area
FIN
```

**Error:**
_______________________________________________

**Corrección:**
_______________________________________________

---

## Sección 8: Ejercicio Integrador

### Ejercicio 20: Calculadora de Viaje

**Crea un algoritmo completo que:**
1. Lea la distancia del viaje en kilómetros
2. Lea el consumo del auto (litros por km)
3. Lea el precio del combustible por litro
4. Calcule el total de litros necesarios
5. Calcule el costo total del viaje
6. Muestre ambos resultados

**Tu pseudocódigo:**
```













```

---

## Reflexión Final

**¿Qué concepto te resultó más claro?**
_______________________________________________

**¿Qué ejercicio fue más desafiante?**
_______________________________________________

**¿Por qué es importante hacer trazas?**
_______________________________________________

---

¡Revisa tus respuestas en `retroalimentacion.md`! 🎉
