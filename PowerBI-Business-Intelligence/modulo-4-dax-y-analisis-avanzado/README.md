# Módulo 4: DAX y Análisis Avanzado

## Introducción

¡Bienvenido al corazón de Power BI! DAX (Data Analysis Expressions) es el lenguaje que te permite crear medidas y cálculos poderosos. En este módulo aprenderás:

- ¿Qué es DAX y por qué es importante?
- Columnas calculadas vs Medidas
- Funciones DAX fundamentales
- Inteligencia de tiempo (Time Intelligence)
- Contextos de filtro y de fila
- Medidas avanzadas y KPIs dinámicos

## ¿Por qué es importante?

DAX transforma Power BI de una herramienta de visualización a una plataforma de análisis avanzado:

- ✅ Crea métricas de negocio complejas
- ✅ Calcula comparaciones temporales (YoY, MoM)
- ✅ Construye KPIs dinámicos
- ✅ Implementa lógica de negocio personalizada
- ✅ Realiza análisis what-if

## Conceptos Principales

### 1. ¿Qué es DAX?

**DAX (Data Analysis Expressions)** es un lenguaje de fórmulas similar a Excel pero diseñado para trabajar con datos relacionales y realizar agregaciones dinámicas.

**Ejemplo simple:**
```DAX
Venta Total = SUM(Ventas[Monto])
```

**Ventajas sobre Excel:**
- Trabaja con millones de filas eficientemente
- Maneja relaciones entre tablas
- Actualiza automáticamente con filtros
- Contextos de evaluación dinámicos

### 2. Columnas Calculadas vs Medidas

**Columna Calculada**
- Se calcula fila por fila
- Se almacena en el modelo
- Ocupa memoria
- Se evalúa al cargar/refrescar datos

**Ejemplo:**
```DAX
Margen = Ventas[Precio] - Ventas[Costo]
```

**Cuándo usar**: Necesitas el valor para filtrar o agrupar.

**Medida (Measure)**
- Se calcula dinámicamente
- No se almacena
- Respeta contextos de filtro
- Se evalúa al usar en visual

**Ejemplo:**
```DAX
Venta Total = SUM(Ventas[Monto])
```

**Cuándo usar**: Para agregaciones y KPIs (lo más común).

**Regla general**: Usa medidas siempre que puedas.

### 3. Funciones DAX Fundamentales

**Agregación:**
```DAX
SUM(Ventas[Monto])           // Suma
AVERAGE(Ventas[Monto])       // Promedio
MIN(Ventas[Monto])           // Mínimo
MAX(Ventas[Monto])           // Máximo
COUNT(Ventas[VentaID])       // Contar
DISTINCTCOUNT(Ventas[ClienteID]) // Contar únicos
```

**Lógica:**
```DAX
IF(condición, valor_si_verdadero, valor_si_falso)
SWITCH(expresión, valor1, resultado1, valor2, resultado2)
AND(condición1, condición2)
OR(condición1, condición2)
```

**Filtrado:**
```DAX
CALCULATE(expresión, filtro1, filtro2, ...)
FILTER(tabla, condición)
ALL(tabla)                    // Ignora filtros
ALLEXCEPT(tabla, columna)     // Ignora todos excepto
```

**Relaciones:**
```DAX
RELATED(tabla_relacionada[columna])      // 1 lado a muchos
RELATEDTABLE(tabla_relacionada)          // Muchos a 1 lado
```

**Información:**
```DAX
ISBLANK(valor)
COUNTROWS(tabla)
VALUES(columna)              // Valores únicos en contexto
```

### 4. Inteligencia de Tiempo (Time Intelligence)

**Requisito**: Tabla de calendario continua.

**Funciones comunes:**
```DAX
// Acumulados
TOTALYTD(expresión, fechas)          // Year to date
TOTALMTD(expresión, fechas)          // Month to date
TOTALQTD(expresión, fechas)          // Quarter to date

// Comparaciones temporales
SAMEPERIODLASTYEAR(fechas)           // Mismo período año anterior
DATEADD(fechas, -1, YEAR)            // Restar 1 año
PREVIOUSMONTH(fechas)                // Mes anterior
PREVIOUSQUARTER(fechas)              // Trimestre anterior

// Rangos
DATESBETWEEN(fechas, fecha_inicio, fecha_fin)
DATESYTD(fechas)                     // Fechas YTD
```

**Ejemplo práctico:**
```DAX
Ventas YTD = TOTALYTD([Venta Total], Calendario[Fecha])

Ventas Año Anterior = 
CALCULATE(
    [Venta Total],
    SAMEPERIODLASTYEAR(Calendario[Fecha])
)

Crecimiento YoY = 
DIVIDE(
    [Venta Total] - [Ventas Año Anterior],
    [Ventas Año Anterior]
)
```

### 5. Contextos en DAX

**Contexto de Filtro**
- Filtros aplicados a la medida
- Proviene de slicers, filtros, filas/columnas de visual

**Ejemplo**: Si filtras "2024", todas las medidas se calculan solo para 2024.

**Contexto de Fila**
- Evaluación fila por fila
- Ocurre en columnas calculadas
- También en funciones iteradoras (SUMX, AVERAGEX)

**CALCULATE** - La función más importante
Modifica el contexto de filtro:

```DAX
Ventas Online = 
CALCULATE(
    [Venta Total],
    Ventas[Canal] = "Online"
)

Ventas Sin Filtro Región = 
CALCULATE(
    [Venta Total],
    ALL(Regiones)
)
```

### 6. Medidas Avanzadas Comunes

**Ticket Promedio:**
```DAX
Ticket Promedio = 
DIVIDE(
    SUM(Ventas[Monto]),
    DISTINCTCOUNT(Ventas[TransaccionID])
)
```

**Ranking:**
```DAX
Ranking Producto = 
RANKX(
    ALL(Productos[Nombre]),
    [Venta Total],,
    DESC
)
```

**Porcentaje del Total:**
```DAX
% del Total = 
DIVIDE(
    [Venta Total],
    CALCULATE([Venta Total], ALL(Productos))
)
```

**Top N:**
```DAX
Ventas Top 10 Productos = 
CALCULATE(
    [Venta Total],
    TOPN(10, Productos, [Venta Total], DESC)
)
```

## Implementación Práctica

### Ejercicio 1: Crea tu primera medida

**Datos**: Tabla Ventas con columnas [Cantidad] y [PrecioUnitario]

**Medida a crear:**
```DAX
Ingresos Totales = 
SUMX(
    Ventas,
    Ventas[Cantidad] * Ventas[PrecioUnitario]
)
```

**Tu turno - Escribe la medida:**
_______________________________________________

### Ejercicio 2: Comparación temporal

**Objetivo**: Calcular ventas del mes anterior

**Medida:**
```DAX
Ventas Mes Anterior = 
CALCULATE(
    [Venta Total],
    PREVIOUSMONTH(Calendario[Fecha])
)
```

**Ahora calcula la diferencia:**
_______________________________________________

### Ejercicio 3: Medida condicional

**Objetivo**: Clasificar ventas como "Alta", "Media", "Baja"

**Escribe la medida:**
_______________________________________________

## Mejores Prácticas

### ✅ Hacer:
- Usar medidas en lugar de columnas calculadas cuando sea posible
- Dar nombres descriptivos (`Venta Total` no `Medida1`)
- Usar DIVIDE en lugar de `/` (maneja división por cero)
- Formatear medidas apropiadamente (moneda, porcentaje)
- Documentar medidas complejas
- Usar variables (VAR) para cálculos complejos

### ❌ Evitar:
- Columnas calculadas para agregaciones simples
- Medidas dentro de columnas calculadas
- Nombres genéricos (`Medida1`, `Cálculo2`)
- Divisiones sin protección de cero
- Medidas muy complejas sin variables

### Ejemplo con variables:
```DAX
KPI Ventas = 
VAR VentasActuales = [Venta Total]
VAR VentasObjetivo = 1000000
VAR Diferencia = VentasActuales - VentasObjetivo
VAR PorcentajeLogro = DIVIDE(VentasActuales, VentasObjetivo)
RETURN
    IF(PorcentajeLogro >= 1, "✓ Meta alcanzada", "⚠ Por debajo de meta")
```

## Conceptos Clave para Recordar

💡 **DAX** = Lenguaje de fórmulas para análisis de datos

📊 **Medidas** > Columnas calculadas (en la mayoría de casos)

⏱️ **Time Intelligence** = Funciones para análisis temporal

🎯 **CALCULATE** = La función más poderosa (modifica contextos)

🔢 **DIVIDE** = Siempre úsala para evitar errores

📈 **Variables (VAR)** = Hacen código más legible y eficiente

## Próximos Pasos

En el **Módulo 5: Interactividad y Publicación**, aprenderás a:
- Crear filtros y slicers interactivos
- Implementar drill-through y drill-down
- Botones y navegación
- Publicar en Power BI Service
- Compartir y colaborar

**Recursos recomendados:**
- 📚 DAX Guide (dax.guide)
- 🎥 SQLBI - Canales de Marco Russo y Alberto Ferrari
- 📖 "Definitive Guide to DAX" - SQLBI
- 🛠️ DAX Studio (herramienta gratuita)

## Motivación Final

> "DAX es como una navaja suiza. Domínala y podrás resolver cualquier desafío analítico." - Alberto Ferrari

DAX puede parecer intimidante al principio. Es normal. Cada experto en DAX comenzó escribiendo medidas simples. La clave es:

1. Practica con datos reales
2. Comienza simple (SUM, COUNT)
3. Avanza gradualmente (CALCULATE, Time Intelligence)
4. No tengas miedo de experimentar
5. Google y comunidades son tus amigos

**Con práctica constante, DAX se volverá tu superpoder en Power BI.**

---

**Tiempo estimado**: 6-8 horas  
**Dificultad**: Avanzado ⭐⭐⭐⭐☆  
**Prerrequisitos**: Módulos 1-3, modelo con tabla de calendario
