# Retroalimentación y Soluciones - Módulo 3: Condicionales

## Sección 1: Respuestas a Preguntas de Opción Múltiple

### Pregunta 1: ¿Qué es un condicional en programación?
**Respuesta correcta: B) Una estructura que permite tomar decisiones según una condición**

**Explicación**: Los condicionales son estructuras de control fundamentales que permiten que un programa ejecute diferentes bloques de código según se cumplan o no ciertas condiciones. Son como las bifurcaciones en un camino: dependiendo de la situación, el programa toma un camino u otro.

---

### Pregunta 2: ¿Cuál es la sintaxis correcta de un IF-ELSE en pseudocódigo?
**Respuesta correcta: B) SI condición ENTONCES código SINO código FIN_SI**

**Explicación**: En pseudocódigo en español, usamos palabras como SI, ENTONCES, SINO y FIN_SI. Esta sintaxis es clara y fácil de entender. Las otras opciones mezclan inglés con español o usan sintaxis de lenguajes específicos como JavaScript o Python.

---

### Pregunta 3: ¿Cuándo se ejecuta el bloque SINO de un condicional?
**Respuesta correcta: C) Cuando la condición del IF es falsa**

**Explicación**: El bloque SINO (ELSE) se ejecuta únicamente cuando la condición del SI (IF) es falsa. Es la alternativa que se toma cuando la condición principal no se cumple.

Ejemplo:
```
SI edad >= 18 ENTONCES
    ESCRIBIR "Mayor de edad"    // Se ejecuta si edad >= 18
SINO
    ESCRIBIR "Menor de edad"    // Se ejecuta si edad < 18
FIN_SI
```

---

### Pregunta 4: ¿Qué operador lógico requiere que AMBAS condiciones sean verdaderas?
**Respuesta correcta: B) Y (AND)**

**Explicación**: El operador Y (AND) requiere que AMBAS condiciones sean verdaderas para que el resultado sea verdadero. Si al menos una es falsa, el resultado es falso.

**Tabla de verdad AND:**
| Condición A | Condición B | A Y B |
|-------------|-------------|-------|
| Verdadero   | Verdadero   | Verdadero |
| Verdadero   | Falso       | Falso |
| Falso       | Verdadero   | Falso |
| Falso       | Falso       | Falso |

---

### Pregunta 5: ¿Cuál es el resultado de: (5 > 3) Y (10 < 8)?
**Respuesta correcta: B) Falso**

**Explicación**: 
- Primera condición: 5 > 3 = Verdadero ✓
- Segunda condición: 10 < 8 = Falso ✗
- Resultado: Verdadero Y Falso = **Falso**

Recuerda: el operador Y requiere que AMBAS condiciones sean verdaderas.

---

### Pregunta 6: ¿Qué significa ELIF (o SINO SI)?
**Respuesta correcta: B) Evaluar una condición adicional si la anterior fue falsa**

**Explicación**: ELIF (SINO SI) permite evaluar múltiples condiciones en secuencia. Si la primera condición es falsa, se evalúa la siguiente, y así sucesivamente.

```
SI nota >= 90 ENTONCES
    letra = "A"
SINO SI nota >= 80 ENTONCES    // Se evalúa solo si nota < 90
    letra = "B"
SINO SI nota >= 70 ENTONCES    // Se evalúa solo si nota < 80
    letra = "C"
FIN_SI
```

---

### Pregunta 7: En el operador O (OR), ¿cuándo es el resultado verdadero?
**Respuesta correcta: C) Si al menos UNA condición es verdadera**

**Explicación**: El operador O (OR) es verdadero cuando AL MENOS UNA de las condiciones es verdadera. Solo es falso cuando TODAS las condiciones son falsas.

**Tabla de verdad OR:**
| Condición A | Condición B | A O B |
|-------------|-------------|-------|
| Verdadero   | Verdadero   | Verdadero |
| Verdadero   | Falso       | Verdadero |
| Falso       | Verdadero   | Verdadero |
| Falso       | Falso       | Falso |

---

### Pregunta 8: ¿Qué es un condicional anidado?
**Respuesta correcta: B) Un IF dentro de otro IF**

**Explicación**: Un condicional anidado es cuando colocamos un SI (IF) dentro de otro SI (IF). Esto permite evaluar condiciones más complejas.

```
SI usuario == "admin" ENTONCES
    SI contraseña == "1234" ENTONCES        // IF anidado
        ESCRIBIR "Acceso concedido"
    SINO
        ESCRIBIR "Contraseña incorrecta"
    FIN_SI
SINO
    ESCRIBIR "Usuario no encontrado"
FIN_SI
```

---

## Sección 2: Respuestas a Verdadero o Falso

### Pregunta 9: El operador NO (NOT) invierte el valor de una condición.
**Respuesta correcta: Verdadero**

**Explicación**: El operador NO (NOT) invierte el valor booleano:
- NO(Verdadero) = Falso
- NO(Falso) = Verdadero

Ejemplo:
```
esta_lloviendo = Falso
SI NO(esta_lloviendo) ENTONCES    // NO(Falso) = Verdadero
    ESCRIBIR "Buen día para salir"
FIN_SI
```

---

### Pregunta 10: Un programa puede tener múltiples ELIF en un mismo condicional.
**Respuesta correcta: Verdadero**

**Explicación**: Puedes tener tantos ELIF (SINO SI) como necesites para evaluar múltiples condiciones diferentes.

```
SI nota >= 90 ENTONCES
    letra = "A"
SINO SI nota >= 80 ENTONCES
    letra = "B"
SINO SI nota >= 70 ENTONCES
    letra = "C"
SINO SI nota >= 60 ENTONCES
    letra = "D"
SINO
    letra = "F"
FIN_SI
```

---

### Pregunta 11: La expresión (Verdadero O Falso) resulta en Falso.
**Respuesta correcta: Falso**

**Explicación**: La expresión (Verdadero O Falso) resulta en **Verdadero**, no Falso. El operador O (OR) es verdadero cuando AL MENOS UNA condición es verdadera.

---

### Pregunta 12: Es obligatorio incluir un SINO en cada condicional IF.
**Respuesta correcta: Falso**

**Explicación**: El SINO (ELSE) es opcional. Puedes tener un IF sin SINO si solo necesitas ejecutar código cuando la condición es verdadera.

```
// Válido: IF sin SINO
SI edad >= 18 ENTONCES
    ESCRIBIR "Puede votar"
FIN_SI
```

---

### Pregunta 13: Los condicionales anidados pueden tener hasta 2 niveles de profundidad como máximo.
**Respuesta correcta: Falso**

**Explicación**: No hay un límite técnico en la cantidad de niveles de anidación. Sin embargo, por claridad y buenas prácticas, se recomienda no anidar demasiado (generalmente no más de 3-4 niveles) para mantener el código legible.

---

### Pregunta 14: El operador Y (AND) es verdadero si al menos una condición es verdadera.
**Respuesta correcta: Falso**

**Explicación**: Esto describe el operador O (OR), no el Y (AND). El operador Y requiere que AMBAS condiciones sean verdaderas para que el resultado sea verdadero.

---

## Sección 3: Soluciones a Evaluación de Expresiones Lógicas

### Ejercicio 15: Evaluación de expresiones lógicas

**a) (8 > 5) Y (3 < 10) = Verdadero**
- 8 > 5 = Verdadero
- 3 < 10 = Verdadero
- Verdadero Y Verdadero = **Verdadero**

**b) (8 > 5) O (3 > 10) = Verdadero**
- 8 > 5 = Verdadero
- 3 > 10 = Falso
- Verdadero O Falso = **Verdadero**

**c) NO(5 == 5) = Falso**
- 5 == 5 = Verdadero
- NO(Verdadero) = **Falso**

**d) (10 >= 10) Y (5 != 3) = Verdadero**
- 10 >= 10 = Verdadero (es igual)
- 5 != 3 = Verdadero (son diferentes)
- Verdadero Y Verdadero = **Verdadero**

**e) NO((4 < 2) O (6 > 3)) = Falso**
- 4 < 2 = Falso
- 6 > 3 = Verdadero
- Falso O Verdadero = Verdadero
- NO(Verdadero) = **Falso**

**f) (Verdadero Y Falso) O Verdadero = Verdadero**
- Verdadero Y Falso = Falso
- Falso O Verdadero = **Verdadero**

---

## Sección 4: Soluciones a Completar Algoritmos

### Ejercicio 16: Número par o impar

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

**Explicación**: Un número es par si al dividirlo entre 2 el resto es 0. El operador MOD devuelve el resto de la división.

---

### Ejercicio 17: Mayor de dos números

```
INICIO
    LEER num1
    LEER num2
    
    SI num1 > num2 ENTONCES
        ESCRIBIR "El mayor es:", num1
    SINO SI num2 > num1 ENTONCES
        ESCRIBIR "El mayor es:", num2
    SINO
        ESCRIBIR "Los números son iguales"
    FIN_SI
FIN
```

**Explicación**: Comparamos ambos números. Si ninguno es mayor que el otro, entonces son iguales.

---

## Sección 5: Soluciones a Escribir Pseudocódigo

### Ejercicio 18: Verificar si puede votar

```
INICIO
    ESCRIBIR "Ingrese su edad:"
    LEER edad
    
    SI edad >= 18 ENTONCES
        ESCRIBIR "Usted puede votar"
    SINO
        años_faltantes = 18 - edad
        ESCRIBIR "No puede votar aún"
        ESCRIBIR "Le faltan", años_faltantes, "años"
    FIN_SI
FIN
```

**Casos de prueba:**
- Entrada: 20 → Salida: "Usted puede votar"
- Entrada: 15 → Salida: "No puede votar aún. Le faltan 3 años"

---

### Ejercicio 19: Mayor de tres números

```
INICIO
    ESCRIBIR "Ingrese tres números:"
    LEER num1
    LEER num2
    LEER num3
    
    SI (num1 >= num2) Y (num1 >= num3) ENTONCES
        mayor = num1
    SINO SI (num2 >= num1) Y (num2 >= num3) ENTONCES
        mayor = num2
    SINO
        mayor = num3
    FIN_SI
    
    ESCRIBIR "El número mayor es:", mayor
FIN
```

**Explicación**: Usamos operadores lógicos Y para verificar si un número es mayor o igual que los otros dos.

---

### Ejercicio 20: Calificación con letra

```
INICIO
    ESCRIBIR "Ingrese la calificación (0-100):"
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
    FIN_SI
    
    ESCRIBIR "Calificación:", letra
    ESCRIBIR "Comentario:", mensaje
FIN
```

**Nota importante**: Las condiciones deben ir de mayor a menor. Si empezáramos con `>= 60`, un 95 también cumpliría esa condición.

---

## Sección 6: Soluciones a Traza de Condicionales

### Ejercicio 21: Traza con edad = 16

**Traza:**
| Paso | Variable | Valor | ¿Se ejecutó? |
|------|----------|-------|--------------|
| 1    | edad     | 16    | Sí           |
| 2    | ¿edad >= 18? | Falso | No (va al SINO) |
| 3    | mensaje  | "Menor de edad" | Sí |
| 4    | puede_votar | Falso | Sí |

**Salida del programa:** "Menor de edad"

**Explicación**: Como edad (16) no es >= 18, la condición es falsa y se ejecuta el bloque SINO.

---

### Ejercicio 22: Traza con nota = 85

**¿Qué condiciones se evaluaron?**
1. nota >= 90: Falso (85 no es >= 90)
2. nota >= 80: Verdadero (85 sí es >= 80) ✓
3. nota >= 70: No se evalúa (ya se cumplió la condición anterior)

**Valor final de letra:** "B"

**Explicación**: Las condiciones ELIF se evalúan en orden. Cuando una es verdadera, se ejecuta su bloque y se sale del condicional sin evaluar las demás.

---

## Sección 7: Soluciones a Detección de Errores

### Ejercicio 23: Error de sintaxis

**Error encontrado:** Falta ENTONCES después de la condición y falta FIN_SI al final.

**Corrección:**
```
INICIO
    LEER temperatura
    
    SI temperatura > 30 ENTONCES
        ESCRIBIR "Hace calor"
    SINO
        ESCRIBIR "Hace frío"
    FIN_SI
FIN
```

---

### Ejercicio 24: Error lógico

**Error:** La lógica está invertida. Dice "Puede votar" cuando edad < 18, pero debería ser al revés.

**Corrección:**
```
INICIO
    LEER edad
    
    SI edad >= 18 ENTONCES
        ESCRIBIR "Puede votar"
    SINO
        ESCRIBIR "No puede votar"
    FIN_SI
FIN
```

**Explicación**: Este es un error de lógica, no de sintaxis. El código es válido sintácticamente, pero produce resultados incorrectos.

---

## Sección 8: Soluciones a Operadores Lógicos

### Ejercicio 25: Puede conducir

```
INICIO
    ESCRIBIR "Ingrese su edad:"
    LEER edad
    
    ESCRIBIR "¿Tiene licencia? (SI/NO):"
    LEER tiene_licencia
    
    SI (edad >= 18) Y (tiene_licencia == "SI") ENTONCES
        ESCRIBIR "Puede conducir"
    SINO
        ESCRIBIR "No puede conducir"
        
        SI edad < 18 ENTONCES
            ESCRIBIR "Razón: Es menor de edad"
        FIN_SI
        
        SI tiene_licencia == "NO" ENTONCES
            ESCRIBIR "Razón: No tiene licencia"
        FIN_SI
    FIN_SI
FIN
```

---

### Ejercicio 26: Descuento en tienda

```
INICIO
    ESCRIBIR "Ingrese el precio del producto:"
    LEER precio
    
    ESCRIBIR "¿Es estudiante? (SI/NO):"
    LEER es_estudiante
    
    ESCRIBIR "¿Es adulto mayor? (SI/NO):"
    LEER es_adulto_mayor
    
    SI (es_estudiante == "SI") O (es_adulto_mayor == "SI") ENTONCES
        descuento = precio * 0.15
        precio_final = precio - descuento
        
        ESCRIBIR "Tiene descuento del 15%"
        ESCRIBIR "Descuento: $", descuento
        ESCRIBIR "Precio final: $", precio_final
    SINO
        ESCRIBIR "Precio final: $", precio
    FIN_SI
FIN
```

---

## Sección 9: Solución a Condicionales Anidados

### Ejercicio 27: Cajero automático

```
INICIO
    saldo = 1000  // Saldo inicial
    
    ESCRIBIR "Ingrese su PIN:"
    LEER pin
    
    SI pin == 1234 ENTONCES
        ESCRIBIR "PIN correcto"
        ESCRIBIR "Saldo disponible: $", saldo
        
        ESCRIBIR "Ingrese monto a retirar:"
        LEER monto
        
        SI monto <= saldo ENTONCES
            saldo = saldo - monto
            ESCRIBIR "Retiro exitoso"
            ESCRIBIR "Tome su dinero: $", monto
            ESCRIBIR "Nuevo saldo: $", saldo
        SINO
            ESCRIBIR "Fondos insuficientes"
            ESCRIBIR "Saldo disponible: $", saldo
        FIN_SI
    SINO
        ESCRIBIR "PIN incorrecto"
        ESCRIBIR "Acceso denegado"
    FIN_SI
FIN
```

---

## Sección 10: Solución al Ejercicio Integrador

### Ejercicio 28: Sistema de Admisión Universitaria

```
INICIO
    ESCRIBIR "Sistema de Admisión Universitaria"
    ESCRIBIR "=================================="
    
    ESCRIBIR "Ingrese el promedio del estudiante (0-100):"
    LEER promedio
    
    ESCRIBIR "Ingrese la calificación del examen (0-100):"
    LEER examen
    
    SI (promedio >= 80) Y (examen >= 70) ENTONCES
        ESCRIBIR "¡FELICIDADES!"
        ESCRIBIR "Estudiante ADMITIDO DIRECTAMENTE"
        ESCRIBIR "Ha cumplido con los requisitos de excelencia"
    SINO SI (promedio >= 70) Y (examen >= 60) ENTONCES
        ESCRIBIR "ADMITIDO CONDICIONALMENTE"
        ESCRIBIR "Deberá mantener promedio >= 70 en el primer semestre"
    SINO
        ESCRIBIR "NO ADMITIDO"
        ESCRIBIR "No cumple con los requisitos mínimos"
        
        SI promedio < 70 ENTONCES
            ESCRIBIR "Promedio insuficiente (mínimo 70)"
        FIN_SI
        
        SI examen < 60 ENTONCES
            ESCRIBIR "Calificación de examen insuficiente (mínimo 60)"
        FIN_SI
    FIN_SI
FIN
```

**Casos de prueba:**
- Promedio: 85, Examen: 75 → **Admitido directamente**
- Promedio: 75, Examen: 65 → **Admitido condicionalmente**
- Promedio: 65, Examen: 80 → **No admitido** (promedio < 70)

---

## Sección 11: Soluciones a Aplicación Práctica

### Ejercicio 29: Calculadora de IMC

```
INICIO
    ESCRIBIR "Calculadora de IMC"
    ESCRIBIR "=================="
    
    ESCRIBIR "Ingrese su peso (kg):"
    LEER peso
    
    ESCRIBIR "Ingrese su altura (metros):"
    LEER altura
    
    // Calcular IMC
    imc = peso / (altura * altura)
    
    ESCRIBIR "Su IMC es:", imc
    
    // Determinar categoría
    SI imc < 18.5 ENTONCES
        categoria = "Bajo peso"
        recomendacion = "Consulte a un nutricionista"
    SINO SI imc <= 24.9 ENTONCES
        categoria = "Peso normal"
        recomendacion = "Mantenga hábitos saludables"
    SINO SI imc <= 29.9 ENTONCES
        categoria = "Sobrepeso"
        recomendacion = "Considere ejercicio y dieta balanceada"
    SINO
        categoria = "Obesidad"
        recomendacion = "Consulte a un médico"
    FIN_SI
    
    ESCRIBIR "Categoría:", categoria
    ESCRIBIR "Recomendación:", recomendacion
FIN
```

**Ejemplo de ejecución:**
- Entrada: peso = 70 kg, altura = 1.75 m
- IMC = 70 / (1.75 * 1.75) = 22.86
- Categoría: "Peso normal"

---

### Ejercicio 30: Sistema de Calificaciones Completo

```
INICIO
    ESCRIBIR "Sistema de Calificaciones"
    ESCRIBIR "========================="
    
    ESCRIBIR "Ingrese calificación del examen 1:"
    LEER calif1
    
    ESCRIBIR "Ingrese calificación del examen 2:"
    LEER calif2
    
    ESCRIBIR "Ingrese calificación del examen 3:"
    LEER calif3
    
    // Calcular promedio
    promedio = (calif1 + calif2 + calif3) / 3
    
    ESCRIBIR "Promedio:", promedio
    
    // Determinar si aprobó
    SI promedio >= 60 ENTONCES
        ESCRIBIR "APROBADO ✓"
        
        // Determinar letra
        SI promedio >= 90 ENTONCES
            letra = "A"
            comentario = "Excelente rendimiento"
        SINO SI promedio >= 80 ENTONCES
            letra = "B"
            comentario = "Muy buen rendimiento"
        SINO SI promedio >= 70 ENTONCES
            letra = "C"
            comentario = "Buen rendimiento"
        SINO
            letra = "D"
            comentario = "Rendimiento suficiente"
        FIN_SI
        
        ESCRIBIR "Calificación:", letra
        ESCRIBIR comentario
    SINO
        ESCRIBIR "REPROBADO ✗"
        ESCRIBIR "Debe cursar nuevamente la materia"
        puntos_faltantes = 60 - promedio
        ESCRIBIR "Le faltaron", puntos_faltantes, "puntos"
    FIN_SI
FIN
```

**Ejemplo de ejecución:**
- Entrada: 85, 90, 88
- Promedio: 87.67
- Resultado: APROBADO ✓, Calificación: B, "Muy buen rendimiento"

---

## Consejos para Mejorar

### Si tuviste dificultades con:

**Condicionales básicos (IF-ELSE):**
- Practica con problemas de la vida real
- Dibuja diagramas de flujo antes de escribir pseudocódigo
- Prueba tu algoritmo con diferentes valores

**Operadores lógicos:**
- Memoriza las tablas de verdad de Y, O y NO
- Practica evaluando expresiones lógicas
- Usa paréntesis para clarificar expresiones complejas

**Condicionales múltiples (ELIF):**
- Recuerda que se evalúan en orden
- Coloca las condiciones más específicas primero
- Asegúrate de cubrir todos los casos

**Condicionales anidados:**
- No anides más de 3 niveles (dificulta la lectura)
- Considera usar operadores lógicos en lugar de anidar
- Indenta correctamente para ver la estructura

---

## Recursos Adicionales Recomendados

1. **Para practicar lógica:**
   - Hacer diagramas de flujo para situaciones cotidianas
   - Resolver problemas de lógica y acertijos
   - Pseudocódigo de rutinas diarias

2. **Para operadores lógicos:**
   - Tarjetas de estudio con tablas de verdad
   - Ejercicios de evaluación de expresiones
   - Problemas que requieran combinar condiciones

3. **Herramientas útiles:**
   - PSeInt (software educativo)
   - draw.io (para diagramas de flujo)
   - Papel y lápiz para trazas

---

## Autoevaluación

**Calcula tu puntaje:**
- Opción múltiple: ___ de 8
- Verdadero/Falso: ___ de 6
- Expresiones lógicas: ___ de 6
- Completar: ___ de 2
- Pseudocódigo: ___ de 3
- Trazas: ___ de 2
- Errores: ___ de 2
- Operadores lógicos: ___ de 2
- Anidados: ___ de 1
- Integrador: ___ de 1
- Aplicación: ___ de 2

**Total: ___ de 35 puntos**

**Interpretación:**
- 30-35: ¡Excelente! Dominas los condicionales
- 24-29: Muy bien, comprendes el concepto
- 18-23: Bien, pero repasa algunos temas
- Menos de 18: Repasa el módulo y practica más

---

**¡Felicidades por completar el Módulo 3! Ahora tus programas pueden tomar decisiones inteligentes. 🎉**

**Próximo paso:** Módulo 4 - Bucles, donde aprenderás a repetir acciones de manera controlada.
