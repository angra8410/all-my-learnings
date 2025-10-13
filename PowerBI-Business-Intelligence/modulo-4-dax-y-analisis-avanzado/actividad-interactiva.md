# Actividades Interactivas - Módulo 4: DAX y Análisis Avanzado

## Sección 1: Preguntas de Opción Múltiple

### Pregunta 1
**¿Cuál es la diferencia principal entre una columna calculada y una medida?**
A) No hay diferencia
B) La columna se calcula fila por fila y se almacena; la medida se calcula dinámicamente
C) Las medidas son más lentas
D) Las columnas solo funcionan con texto

**Tu respuesta**: ___

### Pregunta 2
**¿Qué función DAX usarías para sumar valores?**
A) ADD()
B) TOTAL()
C) SUM()
D) AGGREGATE()

**Tu respuesta**: ___

### Pregunta 3
**¿Qué función es la más importante para modificar contextos de filtro?**
A) FILTER()
B) CALCULATE()
C) SUM()
D) IF()

**Tu respuesta**: ___

### Pregunta 4
**¿Qué necesitas para usar funciones de Time Intelligence?**
A) Nada especial
B) Una tabla de calendario continua
C) Excel instalado
D) Power BI Premium

**Tu respuesta**: ___

### Pregunta 5
**¿Qué función usarías para evitar errores de división por cero?**
A) /
B) SUM()
C) DIVIDE()
D) IF()

**Tu respuesta**: ___

---

## Sección 2: Escribe Medidas DAX

### Ejercicio 1: Medida básica
**Crea una medida que sume todos los montos de ventas**

```DAX
Venta Total = _______________________________________________
```

### Ejercicio 2: Promedio
**Crea una medida que calcule el precio promedio**

```DAX
Precio Promedio = _______________________________________________
```

### Ejercicio 3: Contar únicos
**Cuenta cuántos clientes únicos hay**

```DAX
Clientes Únicos = _______________________________________________
```

### Ejercicio 4: Medida con CALCULATE
**Calcula ventas solo para el canal "Online"**

```DAX
Ventas Online = _______________________________________________
```

### Ejercicio 5: YTD (Year to Date)
**Calcula ventas acumuladas del año**

```DAX
Ventas YTD = _______________________________________________
```

---

## Sección 3: Verdadero o Falso

1. **Las columnas calculadas se almacenan en el modelo y ocupan memoria.** ___
2. **Las medidas son siempre mejores que las columnas calculadas.** ___
3. **CALCULATE es la función más poderosa de DAX.** ___
4. **Puedes usar medidas dentro de columnas calculadas.** ___
5. **Time Intelligence requiere una tabla de calendario.** ___
6. **DIVIDE maneja automáticamente la división por cero.** ___
7. **Variables (VAR) hacen el código más eficiente.** ___
8. **SUM y SUMX hacen exactamente lo mismo.** ___
9. **RELATED funciona del lado "muchos" al lado "uno".** ___
10. **Siempre debes usar / en lugar de DIVIDE.** ___

---

## Sección 4: Identifica Errores

### Código 1
```DAX
Venta Total = Ventas[Monto]
```
**Error**: _______________________________________________
**Corrección**: _______________________________________________

### Código 2
```DAX
Margen % = [Ganancia] / [Venta Total]
```
**Error**: _______________________________________________
**Corrección**: _______________________________________________

### Código 3
```DAX
Ventas 2023 = SUM(Ventas[Monto], Año = 2023)
```
**Error**: _______________________________________________
**Corrección**: _______________________________________________

---

## Sección 5: Caso Práctico

**Contexto**: Tienda de electrónicos con ventas mensuales.

### Crea las siguientes medidas:

**1. Venta Total**
```DAX
_______________________________________________
```

**2. Costo Total**
```DAX
_______________________________________________
```

**3. Margen de Ganancia** (Venta - Costo)
```DAX
_______________________________________________
```

**4. Margen %** (Ganancia / Venta)
```DAX
_______________________________________________
```

**5. Ventas Mes Anterior**
```DAX
_______________________________________________
```

**6. Crecimiento MoM %**
```DAX
_______________________________________________
```

**7. Ventas YTD**
```DAX
_______________________________________________
```

---

## Sección 6: Reflexión

### ¿Qué función DAX te pareció más útil?
_______________________________________________

### ¿Cuál fue tu mayor desafío con DAX?
_______________________________________________

### ¿Cómo aplicarás DAX en tu trabajo?
_______________________________________________

---

**¡Excelente trabajo!** Revisa soluciones en `retroalimentacion.md`.
