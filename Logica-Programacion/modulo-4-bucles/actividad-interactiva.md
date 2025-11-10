# Actividades Interactivas - Módulo 4: Bucles

## Sección 1: Preguntas de Opción Múltiple

### Pregunta 1
**¿Qué es un bucle en programación?**

A) Una variable que cambia de valor  
B) Una estructura que repite código mientras se cumple una condición  
C) Un condicional con múltiples opciones  
D) Un error en el programa  

---

### Pregunta 2
**¿Cuál es la diferencia principal entre MIENTRAS y PARA?**

A) No hay diferencia  
B) MIENTRAS se usa cuando sabemos cuántas veces repetir, PARA cuando no  
C) PARA se usa cuando sabemos cuántas veces repetir, MIENTRAS cuando no  
D) MIENTRAS es más rápido que PARA  

---

### Pregunta 3
**¿Cuándo se evalúa la condición en un bucle MIENTRAS?**

A) Después de cada iteración  
B) Solo al final del bucle  
C) Antes de cada iteración  
D) Una sola vez al inicio  

---

### Pregunta 4
**¿Qué es un bucle infinito?**

A) Un bucle que se ejecuta muy rápido  
B) Un bucle cuya condición nunca se vuelve falsa  
C) Un bucle que tiene muchas iteraciones  
D) Un tipo especial de bucle PARA  

---

### Pregunta 5
**En un bucle PARA, ¿qué sucede con la variable de control?**

A) Se mantiene constante  
B) Se incrementa o decrementa automáticamente en cada iteración  
C) Se elimina después del bucle  
D) Solo existe fuera del bucle  

---

### Pregunta 6
**¿Cuál es el propósito de un contador en un bucle?**

A) Detener el programa  
B) Llevar registro del número de iteraciones  
C) Almacenar el resultado final  
D) Verificar errores  

---

### Pregunta 7
**¿Qué es un acumulador?**

A) Una variable que va sumando valores en cada iteración  
B) Un tipo de bucle  
C) Un operador matemático  
D) Una estructura de datos  

---

### Pregunta 8
**¿Cuántas veces se ejecuta este bucle? `PARA i = 1 HASTA 10 HACER`**

A) 9 veces  
B) 10 veces  
C) 11 veces  
D) Infinitas veces  

---

## Sección 2: Verdadero o Falso

### Pregunta 9
**Un bucle MIENTRAS puede no ejecutarse nunca si la condición es falsa desde el inicio.**

- [ ] Verdadero
- [ ] Falso

---

### Pregunta 10
**Un bucle PARA siempre se ejecuta al menos una vez.**

- [ ] Verdadero
- [ ] Falso

---

### Pregunta 11
**Es posible tener un bucle dentro de otro bucle (bucles anidados).**

- [ ] Verdadero
- [ ] Falso

---

### Pregunta 12
**Un contador debe inicializarse antes del bucle.**

- [ ] Verdadero
- [ ] Falso

---

### Pregunta 13
**La única forma de salir de un bucle MIENTRAS es que la condición sea falsa.**

- [ ] Verdadero
- [ ] Falso

---

### Pregunta 14
**Un acumulador siempre debe inicializarse en 0.**

- [ ] Verdadero
- [ ] Falso

---

## Sección 3: Traza de Bucles Simples

### Ejercicio 15
**Realiza la traza del siguiente bucle:**

```
INICIO
    i = 1
    suma = 0
    
    MIENTRAS i <= 3 HACER
        suma = suma + i
        i = i + 1
    FIN MIENTRAS
    
    ESCRIBIR suma
FIN
```

| Iteración | i | suma | ¿Condición verdadera? |
|-----------|---|------|----------------------|
| Inicio    |   |      |                      |
| 1         |   |      |                      |
| 2         |   |      |                      |
| 3         |   |      |                      |
| Salida    |   |      |                      |

**Salida del programa:** _______

---

### Ejercicio 16
**Realiza la traza de este bucle PARA:**

```
INICIO
    producto = 1
    
    PARA i = 1 HASTA 4 HACER
        producto = producto * i
    FIN PARA
    
    ESCRIBIR producto
FIN
```

| Iteración | i | producto |
|-----------|---|----------|
| Inicio    |   |          |
| 1         |   |          |
| 2         |   |          |
| 3         |   |          |
| 4         |   |          |

**Salida final:** _______

**¿Qué calcula este algoritmo?** _______________________

---

## Sección 4: Completar Algoritmos

### Ejercicio 17
**Completa el bucle para imprimir números del 1 al 5:**

```
INICIO
    i = _____
    
    MIENTRAS i <= _____ HACER
        ESCRIBIR i
        i = _____
    FIN MIENTRAS
FIN
```

---

### Ejercicio 18
**Completa el bucle PARA para sumar números del 1 al 10:**

```
INICIO
    suma = 0
    
    PARA i = _____ HASTA _____ HACER
        suma = suma + _____
    FIN PARA
    
    ESCRIBIR "La suma es:", suma
FIN
```

---

## Sección 5: Escribir Pseudocódigo con Bucles

### Ejercicio 19
**Escribe un algoritmo que muestre los números pares del 2 al 20 usando un bucle MIENTRAS.**

```
INICIO












FIN
```

---

### Ejercicio 20
**Escribe un algoritmo que calcule el factorial de un número usando un bucle PARA.**

Recuerda: factorial de 5 = 5 × 4 × 3 × 2 × 1 = 120

```
INICIO














FIN
```

---

### Ejercicio 21
**Escribe un algoritmo que lea 5 números y calcule su promedio.**

```
INICIO
















FIN
```

---

## Sección 6: Contadores y Acumuladores

### Ejercicio 22
**Escribe un algoritmo que cuente cuántos números pares hay entre 1 y 20.**

```
INICIO














FIN
```

---

### Ejercicio 23
**Escribe un algoritmo que sume todos los números impares del 1 al 50.**

```
INICIO














FIN
```

---

## Sección 7: Detección de Errores

### Ejercicio 24
**¿Qué está mal en este bucle?**

```
INICIO
    i = 1
    
    MIENTRAS i <= 10 HACER
        ESCRIBIR i
    FIN MIENTRAS
FIN
```

**Error encontrado:**
_______________________________________________

**Corrección:**
_______________________________________________

---

### Ejercicio 25
**Identifica el problema:**

```
INICIO
    contador = 5
    
    MIENTRAS contador > 0 HACER
        ESCRIBIR contador
        contador = contador + 1
    FIN MIENTRAS
FIN
```

**Error:**
_______________________________________________

**¿Qué sucederá?**
_______________________________________________

**Corrección:**
_______________________________________________

---

## Sección 8: Bucles Anidados

### Ejercicio 26
**Escribe un algoritmo que imprima una tabla de multiplicar del 1 al 5 (para los números del 1 al 10).**

Ejemplo de salida:
```
1 x 1 = 1
1 x 2 = 2
...
5 x 10 = 50
```

```
INICIO


















FIN
```

---

### Ejercicio 27
**Escribe un algoritmo que imprima un patrón de asteriscos:**

```
*
**
***
****
*****
```

```
INICIO














FIN
```

---

## Sección 9: Aplicaciones Prácticas

### Ejercicio 28: Validación de Entrada

**Escribe un algoritmo que pida un número entre 1 y 10, y siga pidiendo hasta que el usuario ingrese un valor válido.**

```
INICIO
















FIN
```

---

### Ejercicio 29: Calculadora de Promedio

**Escribe un algoritmo que:**
1. Pida al usuario cuántas calificaciones va a ingresar
2. Lea todas las calificaciones
3. Calcule y muestre el promedio

```
INICIO




















FIN
```

---

## Sección 10: Ejercicio Integrador

### Ejercicio 30: Sistema de Votación

**Crea un algoritmo que:**
1. Pida el número de votantes
2. Para cada votante, registre su voto (A, B, o C)
3. Cuente los votos de cada candidato
4. Determine y muestre el ganador

```
INICIO






























FIN
```

**Casos de prueba:**
- 5 votantes: A, A, B, C, A → Ganador: A (3 votos)
- 4 votantes: B, B, C, C → Empate

---

## Reflexión Final

**¿Qué tipo de bucle prefieres y por qué?**
_______________________________________________
_______________________________________________

**¿Cuál fue el ejercicio más desafiante?**
_______________________________________________

**¿En qué situaciones de la vida real usarías bucles?**
_______________________________________________
_______________________________________________
_______________________________________________

**¿Qué diferencia encontraste entre usar bucles y repetir código manualmente?**
_______________________________________________
_______________________________________________

**¿Cómo evitarías crear un bucle infinito?**
_______________________________________________
_______________________________________________

**¿Qué aprendiste sobre contadores y acumuladores?**
_______________________________________________
_______________________________________________

---

¡Excelente trabajo! Revisa tus respuestas en `retroalimentacion.md` para verificar tu aprendizaje. 🎉
