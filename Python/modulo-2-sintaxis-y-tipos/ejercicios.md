# Ejercicios - Módulo 2: Sintaxis y Tipos de Datos

## Sección 1: Preguntas de Opción Múltiple

### Pregunta 1
**¿Cuál es una forma CORRECTA de nombrar una variable?**

A) 1numero  
B) mi-variable  
C) mi_variable  
D) mi variable  

---

### Pregunta 2
**¿Qué tipo de dato es `True`?**

A) string  
B) int  
C) float  
D) bool  

---

### Pregunta 3
**¿Qué retorna `type(3.14)`?**

A) int  
B) float  
C) string  
D) decimal  

---

### Pregunta 4
**¿Qué imprime `print("Hola" * 3)`?**

A) HolaHolaHola  
B) Hola Hola Hola  
C) Hola 3  
D) Error  

---

### Pregunta 5
**¿Qué hace la función `input()`?**

A) Imprime en pantalla  
B) Lee información del usuario  
C) Convierte a número  
D) Calcula operaciones  

---

### Pregunta 6
**¿Qué tipo de dato retorna SIEMPRE `input()`?**

A) int  
B) float  
C) string  
D) bool  

---

### Pregunta 7
**¿Cuál es la forma correcta de formatear con f-strings?**

A) print("Hola {nombre}")  
B) print(f"Hola {nombre}")  
C) print("Hola" + nombre)  
D) print("Hola", nombre)  

---

### Pregunta 8
**¿Qué imprime `print(10 // 3)`?**

A) 3.33  
B) 3  
C) 4  
D) 3.0  

---

## Sección 2: Verdadero o Falso

### Pregunta 9
**Las variables en Python pueden empezar con un número.**

- [ ] Verdadero
- [ ] Falso

---

### Pregunta 10
**`5 == 5` retorna `True`.**

- [ ] Verdadero
- [ ] Falso

---

### Pregunta 11
**`"5" == 5` retorna `True`.**

- [ ] Verdadero
- [ ] Falso

---

### Pregunta 12
**Se pueden usar tanto comillas simples `'` como dobles `"` para strings.**

- [ ] Verdadero
- [ ] Falso

---

## Sección 3: Completar el Código

### Ejercicio 13
Crea una variable llamada `nombre` con tu nombre:

```python
______ = "_________"
```

---

### Ejercicio 14
Convierte el string "25" a número entero:

```python
edad_texto = "25"
edad = ___(edad_texto)
```

---

### Ejercicio 15
Completa el f-string:

```python
nombre = "Ana"
edad = 25
print(__"Mi nombre es {_____} y tengo {____} años")
```

---

## Sección 4: ¿Qué imprime?

### Ejercicio 16
```python
x = 10
x += 5
print(x)
```
**Respuesta:** _______________

---

### Ejercicio 17
```python
nombre = "Python"
print(nombre[0])
```
**Respuesta:** _______________

---

### Ejercicio 18
```python
print(len("Hola"))
```
**Respuesta:** _______________

---

### Ejercicio 19
```python
print(10 % 3)
```
**Respuesta:** _______________

---

### Ejercicio 20
```python
print(type(3.0))
```
**Respuesta:** _______________

---

## Sección 5: Encuentra el Error

### Ejercicio 21
```python
edad = input("Tu edad: ")
print(edad + 10)
```
**Error:** _______________________________________________
**Corrección:**
```python

```

---

### Ejercicio 22
```python
nombre = input("Nombre: ")
print("Hola {nombre}")
```
**Error:** _______________________________________________
**Corrección:**
```python

```

---

### Ejercicio 23
```python
precio-total = 100
```
**Error:** _______________________________________________
**Corrección:**
```python

```

---

## Sección 6: Ejercicios Prácticos

### Ejercicio 24: Calculadora Simple
Crea un programa que pida dos números y muestre:
- Suma
- Resta
- Multiplicación
- División

**Tu código:**
```python




```

---

### Ejercicio 25: Información Personal
Crea un programa que pida:
- Nombre
- Edad
- Ciudad

Y muestre: "Hola [nombre], tienes [edad] años y vives en [ciudad]"

**Tu código:**
```python




```

---

### Ejercicio 26: Área de un Círculo
Pide el radio y calcula el área (π × r²). Usa PI = 3.14159

**Tu código:**
```python




```

---

### Ejercicio 27: Conversor de Moneda
Convierte dólares a tu moneda local. Pide cantidad en dólares y muestra el equivalente.

**Tu código:**
```python




```

---

## Sección 7: Pensamiento Crítico

### Pregunta 28
**¿Por qué es importante convertir el resultado de `input()` cuando necesitas hacer operaciones matemáticas?**

_______________________________________________
_______________________________________________
_______________________________________________

---

### Pregunta 29
**¿Cuál es la diferencia entre `10 / 3` y `10 // 3`?**

_______________________________________________
_______________________________________________

---

### Pregunta 30
**¿Para qué sirven los f-strings? ¿Por qué son mejores que concatenar con `+`?**

_______________________________________________
_______________________________________________
_______________________________________________

---

## Sección 8: Proyecto Mini

### Ejercicio 31: Calculadora de IMC (Índice de Masa Corporal)

Crea un programa que:
1. Pida el nombre del usuario
2. Pida el peso en kg
3. Pida la altura en metros
4. Calcule el IMC: peso / (altura²)
5. Muestre el resultado formateado con 2 decimales

**Ejemplo de salida:**
```
=== CALCULADORA DE IMC ===
Nombre: Ana
Peso (kg): 60
Altura (m): 1.65

Hola Ana, tu IMC es: 22.04
```

**Tu código completo:**
```python




```

---

## Sección 9: Desafío Extra ⭐

### Ejercicio 32: Conversión de Tiempo

Crea un programa que convierta segundos a horas, minutos y segundos.

**Ejemplo:**
- Input: 3665 segundos
- Output: 1 hora, 1 minuto, 5 segundos

**Pistas:**
- 1 hora = 3600 segundos
- 1 minuto = 60 segundos
- Usa división entera `//` y módulo `%`

**Tu código:**
```python




```

---

### Ejercicio 33: Detector de Palíndromo Simple

Crea un programa que verifique si una palabra de 5 letras es palíndromo (se lee igual al derecho y al revés).

**Ejemplos de palíndromos:** radar, salas, anana

**Pista:** Compara `palabra[0]` con `palabra[-1]`, etc.

**Tu código:**
```python




```

---

## Sección 10: Investigación

### Ejercicio 34
Investiga y explica qué hace el método `.strip()` en strings.

**Explicación:**
_______________________________________________
_______________________________________________

**Ejemplo de uso:**
```python

```

---

### Ejercicio 35
Investiga qué es el operador `**=` y da un ejemplo.

**Explicación:**
_______________________________________________

**Ejemplo:**
```python

```

---

## Autoevaluación

### ¿Cuántas preguntas respondiste correctamente?

- Opción múltiple (1-8): ___ / 8
- Verdadero/Falso (9-12): ___ / 4
- Completar código (13-15): ___ / 3
- ¿Qué imprime? (16-20): ___ / 5
- Encuentra el error (21-23): ___ / 3
- Prácticos (24-27): ___ / 4
- Pensamiento crítico (28-30): ___ / 3

**Total:** ___ / 30

### Reflexión

**El concepto más difícil fue:**
_______________________________________________

**El ejercicio más útil fue:**
_______________________________________________

**Algo nuevo que aprendí:**
_______________________________________________

---

**¡Excelente trabajo! Completa tu archivo `progreso.md` para registrar este logro. 🎉**
