# Actividades Interactivas - Módulo 3: Condicionales

## Sección 1: Preguntas de Opción Múltiple

### Pregunta 1
**¿Qué es un condicional en programación?**

A) Una variable que cambia de valor  
B) Una estructura que permite tomar decisiones según una condición  
C) Un bucle que se repite varias veces  
D) Un tipo de operador aritmético  

---

### Pregunta 2
**¿Cuál es la sintaxis correcta de un IF-ELSE en pseudocódigo?**

A) IF condición THEN código ELSE código END  
B) SI condición ENTONCES código SINO código FIN_SI  
C) IF (condición) { código } ELSE { código }  
D) SI condición: código SINO: código  

---

### Pregunta 3
**¿Cuándo se ejecuta el bloque SINO de un condicional?**

A) Siempre que haya un IF  
B) Cuando la condición del IF es verdadera  
C) Cuando la condición del IF es falsa  
D) Nunca se ejecuta  

---

### Pregunta 4
**¿Qué operador lógico requiere que AMBAS condiciones sean verdaderas?**

A) O (OR)  
B) Y (AND)  
C) NO (NOT)  
D) SI (IF)  

---

### Pregunta 5
**¿Cuál es el resultado de: (5 > 3) Y (10 < 8)?**

A) Verdadero  
B) Falso  
C) Error  
D) Ninguno  

---

### Pregunta 6
**¿Qué significa ELIF (o SINO SI)?**

A) Finalizar el condicional  
B) Evaluar una condición adicional si la anterior fue falsa  
C) Repetir la condición anterior  
D) Negar una condición  

---

### Pregunta 7
**En el operador O (OR), ¿cuándo es el resultado verdadero?**

A) Solo si ambas condiciones son verdaderas  
B) Solo si ambas condiciones son falsas  
C) Si al menos UNA condición es verdadera  
D) Nunca  

---

### Pregunta 8
**¿Qué es un condicional anidado?**

A) Un condicional sin SINO  
B) Un IF dentro de otro IF  
C) Un condicional con muchas condiciones  
D) Un error de sintaxis  

---

## Sección 2: Verdadero o Falso

### Pregunta 9
**El operador NO (NOT) invierte el valor de una condición.**

- [ ] Verdadero
- [ ] Falso

---

### Pregunta 10
**Un programa puede tener múltiples ELIF en un mismo condicional.**

- [ ] Verdadero
- [ ] Falso

---

### Pregunta 11
**La expresión (Verdadero O Falso) resulta en Falso.**

- [ ] Verdadero
- [ ] Falso

---

### Pregunta 12
**Es obligatorio incluir un SINO en cada condicional IF.**

- [ ] Verdadero
- [ ] Falso

---

### Pregunta 13
**Los condicionales anidados pueden tener hasta 2 niveles de profundidad como máximo.**

- [ ] Verdadero
- [ ] Falso

---

### Pregunta 14
**El operador Y (AND) es verdadero si al menos una condición es verdadera.**

- [ ] Verdadero
- [ ] Falso

---

## Sección 3: Evaluación de Expresiones Lógicas

### Ejercicio 15
**Evalúa las siguientes expresiones lógicas:**

a) (8 > 5) Y (3 < 10) = _____

b) (8 > 5) O (3 > 10) = _____

c) NO(5 == 5) = _____

d) (10 >= 10) Y (5 != 3) = _____

e) NO((4 < 2) O (6 > 3)) = _____

f) (Verdadero Y Falso) O Verdadero = _____

---

## Sección 4: Completar Algoritmos

### Ejercicio 16
**Completa el siguiente algoritmo para verificar si un número es par o impar:**

```
INICIO
    LEER numero
    
    SI numero MOD 2 == _____ ENTONCES
        ESCRIBIR "El número es _____"
    SINO
        ESCRIBIR "El número es _____"
    FIN_SI
FIN
```

---

### Ejercicio 17
**Completa el algoritmo para determinar el mayor de dos números:**

```
INICIO
    LEER num1
    LEER num2
    
    SI _____ ENTONCES
        ESCRIBIR "El mayor es:", num1
    SINO SI _____ ENTONCES
        ESCRIBIR "El mayor es:", num2
    SINO
        ESCRIBIR "Los números son _____"
    FIN_SI
FIN
```

---

## Sección 5: Escribir Pseudocódigo

### Ejercicio 18
**Escribe un algoritmo que lea la edad de una persona y determine si puede votar (edad >= 18).**

```
INICIO








FIN
```

---

### Ejercicio 19
**Escribe un algoritmo que lea tres números y determine cuál es el mayor.**

```
INICIO
















FIN
```

---

### Ejercicio 20
**Escribe un algoritmo que lea una calificación numérica (0-100) y muestre la letra correspondiente:**
- A: 90-100
- B: 80-89
- C: 70-79
- D: 60-69
- F: 0-59

```
INICIO






















FIN
```

---

## Sección 6: Traza de Condicionales

### Ejercicio 21
**Realiza la traza del siguiente algoritmo con edad = 16:**

```
INICIO
    edad = 16
    
    SI edad >= 18 ENTONCES
        mensaje = "Mayor de edad"
        puede_votar = Verdadero
    SINO
        mensaje = "Menor de edad"
        puede_votar = Falso
    FIN_SI
    
    ESCRIBIR mensaje
FIN
```

**Traza:**
| Paso | Variable | Valor | ¿Se ejecutó? |
|------|----------|-------|--------------|
| 1    | edad     |       |              |
| 2    | ¿edad >= 18? |   | Sí / No      |
| 3    | mensaje  |       |              |
| 4    | puede_votar |    |              |

**Salida del programa:** _______________________

---

### Ejercicio 22
**Realiza la traza con nota = 85:**

```
INICIO
    nota = 85
    
    SI nota >= 90 ENTONCES
        letra = "A"
    SINO SI nota >= 80 ENTONCES
        letra = "B"
    SINO SI nota >= 70 ENTONCES
        letra = "C"
    SINO
        letra = "F"
    FIN_SI
    
    ESCRIBIR "Calificación:", letra
FIN
```

**¿Qué condiciones se evaluaron?**
1. nota >= 90: _______
2. nota >= 80: _______
3. nota >= 70: _______

**Valor final de letra:** _______

---

## Sección 7: Detección de Errores

### Ejercicio 23
**¿Qué está mal en este algoritmo?**

```
INICIO
    LEER temperatura
    
    SI temperatura > 30
        ESCRIBIR "Hace calor"
    SINO
        ESCRIBIR "Hace frío"
FIN
```

**Error encontrado:**
_______________________________________________

**Corrección:**
```





```

---

### Ejercicio 24
**Identifica el error lógico:**

```
INICIO
    LEER edad
    
    SI edad < 18 ENTONCES
        ESCRIBIR "Puede votar"
    SINO
        ESCRIBIR "No puede votar"
    FIN_SI
FIN
```

**Error:**
_______________________________________________

**Corrección:**
_______________________________________________

---

## Sección 8: Operadores Lógicos

### Ejercicio 25
**Escribe un algoritmo que determine si una persona puede conducir. Requiere: edad >= 18 Y tener licencia.**

```
INICIO









FIN
```

---

### Ejercicio 26
**Escribe un algoritmo para un descuento en tienda. Si el cliente es estudiante O es adulto mayor, recibe 15% de descuento.**

```
INICIO














FIN
```

---

## Sección 9: Condicionales Anidados

### Ejercicio 27
**Escribe un algoritmo para un cajero automático que:**
1. Verifique el PIN (debe ser 1234)
2. Si el PIN es correcto, verifique si hay saldo suficiente
3. Si hay saldo, permita el retiro
4. Si no, muestre mensaje de fondos insuficientes

```
INICIO




















FIN
```

---

## Sección 10: Ejercicio Integrador

### Ejercicio 28: Sistema de Admisión Universitaria

**Crea un algoritmo completo que determine si un estudiante es admitido a la universidad:**

**Criterios:**
- Promedio >= 80 Y examen >= 70 → Admitido directamente
- Promedio >= 70 Y examen >= 60 → Admitido condicionalmente
- En cualquier otro caso → No admitido

**El algoritmo debe:**
1. Leer el promedio del estudiante
2. Leer la calificación del examen
3. Determinar el estatus de admisión
4. Mostrar mensaje apropiado

**Tu pseudocódigo:**
```
INICIO
























FIN
```

**Casos de prueba:**
- Promedio: 85, Examen: 75 → Resultado esperado: _______
- Promedio: 75, Examen: 65 → Resultado esperado: _______
- Promedio: 65, Examen: 80 → Resultado esperado: _______

---

## Sección 11: Aplicación Práctica

### Ejercicio 29: Calculadora de IMC (Índice de Masa Corporal)

**Crea un algoritmo que:**
1. Lea peso (kg) y altura (m)
2. Calcule IMC = peso / (altura * altura)
3. Determine la categoría:
   - IMC < 18.5: "Bajo peso"
   - IMC 18.5-24.9: "Peso normal"
   - IMC 25-29.9: "Sobrepeso"
   - IMC >= 30: "Obesidad"

```
INICIO


























FIN
```

---

### Ejercicio 30: Sistema de Calificaciones Completo

**Diseña un algoritmo que:**
1. Lea 3 calificaciones de exámenes
2. Calcule el promedio
3. Determine si aprobó (promedio >= 60)
4. Si aprobó, determine la letra (A, B, C, D)
5. Si no aprobó, muestre mensaje de reprobado

```
INICIO
































FIN
```

---

## Reflexión Final

**¿Qué concepto te pareció más útil?**
_______________________________________________
_______________________________________________

**¿Qué desafíos encontraste?**
_______________________________________________
_______________________________________________

**¿En qué situaciones de la vida real usarías condicionales?**
_______________________________________________
_______________________________________________
_______________________________________________

**¿Qué diferencia notas entre usar Y (AND) y O (OR)?**
_______________________________________________
_______________________________________________

**Ejercicio más desafiante:**
_______________________________________________

**¿Cómo te ayudarán los condicionales en tus futuros programas?**
_______________________________________________
_______________________________________________
_______________________________________________

---

¡Excelente trabajo! Revisa tus respuestas en `retroalimentacion.md` para verificar tu aprendizaje. 🎉
