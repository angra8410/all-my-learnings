# Retroalimentación y Soluciones - Módulo 4: DAX y Análisis Avanzado

## Respuestas Opción Múltiple

1. **B)** Columna: fila por fila, almacenada. Medida: dinámica, no almacenada.
2. **C)** SUM() es la función de agregación para sumar.
3. **B)** CALCULATE() modifica contextos de filtro.
4. **B)** Time Intelligence requiere tabla de calendario continua.
5. **C)** DIVIDE() maneja división por cero automáticamente.

---

## Soluciones - Escribe Medidas

### Ejercicio 1
```DAX
Venta Total = SUM(Ventas[Monto])
```

### Ejercicio 2
```DAX
Precio Promedio = AVERAGE(Ventas[Precio])
```

### Ejercicio 3
```DAX
Clientes Únicos = DISTINCTCOUNT(Ventas[ClienteID])
```

### Ejercicio 4
```DAX
Ventas Online = CALCULATE([Venta Total], Ventas[Canal] = "Online")
```

### Ejercicio 5
```DAX
Ventas YTD = TOTALYTD([Venta Total], Calendario[Fecha])
```

---

## Verdadero o Falso

1. **V** - Columnas calculadas se almacenan
2. **F** - Depende del caso de uso
3. **V** - CALCULATE es fundamental
4. **F** - No se puede (error común)
5. **V** - Requisito para Time Intelligence
6. **V** - Retorna BLANK si divisor es cero
7. **V** - Más eficientes y legibles
8. **F** - SUMX itera fila por fila
9. **V** - Del lado "muchos" obtiene datos del lado "uno"
10. **F** - Siempre usa DIVIDE

---

## Soluciones - Errores

### Código 1
**Error**: Falta agregación
**Corrección**: `Venta Total = SUM(Ventas[Monto])`

### Código 2
**Error**: Debería usar DIVIDE
**Corrección**: `Margen % = DIVIDE([Ganancia], [Venta Total])`

### Código 3
**Error**: Sintaxis incorrecta
**Corrección**: `Ventas 2023 = CALCULATE(SUM(Ventas[Monto]), Calendario[Año] = 2023)`

---

## Caso Práctico - Soluciones

```DAX
Venta Total = SUM(Ventas[Monto])

Costo Total = SUM(Ventas[Costo])

Margen Ganancia = [Venta Total] - [Costo Total]

Margen % = DIVIDE([Margen Ganancia], [Venta Total])

Ventas Mes Anterior = CALCULATE([Venta Total], PREVIOUSMONTH(Calendario[Fecha]))

Crecimiento MoM % = DIVIDE([Venta Total] - [Ventas Mes Anterior], [Ventas Mes Anterior])

Ventas YTD = TOTALYTD([Venta Total], Calendario[Fecha])
```

---

## Evaluación

### 90%+: 🌟 Excelente
Dominas DAX básico. Sigue practicando con casos complejos.

### 70-89%: 💪 Muy bien
Entiendes fundamentos. Practica más Time Intelligence.

### <70%: 📚 Continúa
DAX es complejo. Practica con ejemplos simples primero.

---

**¡Felicitaciones!** DAX es tu nuevo superpoder. 🚀
