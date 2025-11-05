# 🎮 Actividad Interactiva 03: Model the Data - Ejercicios Prácticos

## 🎯 Objetivo

Dominar el modelado de datos en Power BI mediante diseño de esquemas, creación de relaciones, DAX básico e intermedio, y optimización de modelos.

**Duración total estimada**: 270-300 minutos (4.5-5 horas)

---

## 📋 Ejercicio 1: Diseñar Esquema Estrella (35 minutos)

### 🎯 Objetivo
Transformar un modelo desnormalizado en un esquema estrella eficiente.

### 📝 Pasos

1. **Analizar datos fuente**
   - Cargar dataset con ventas, productos, clientes, fechas en una sola tabla
   - Identificar campos que pertenecen a dimensiones vs hechos

2. **Crear tabla de hechos (FactSales)**
   ```
   Campos a mantener:
   - OrderID (clave)
   - DateKey (FK a DimDate)
   - ProductKey (FK a DimProduct)
   - CustomerKey (FK a DimCustomer)
   - Quantity (medible)
   - UnitPrice (medible)
   - SalesAmount (medible)
   ```

3. **Crear dimensiones**
   - DimProduct: ProductKey, ProductName, Category, Subcategory, Color
   - DimCustomer: CustomerKey, CustomerName, City, State, Country
   - DimDate: DateKey, Date, Year, Quarter, Month, MonthName, Day

4. **Separar tablas en Power Query**
   - Reference query original
   - Remove columns para crear Fact
   - Remove Duplicates para crear Dims

### ✅ Comprobación

**Esquema diseñado**:

| Tabla | Tipo | Columnas | Filas Aprox |
|-------|------|----------|-------------|
| FactSales | Fact | _______ | _______ |
| DimProduct | Dimension | _______ | _______ |
| DimCustomer | Dimension | _______ | _______ |
| DimDate | Dimension | _______ | _______ |

**¿Esquema es estrella?** ⬜ Sí ⬜ No

---

## 📋 Ejercicio 2: Crear y Configurar Relaciones (40 minutos)

### 🎯 Objetivo
Establecer relaciones correctas entre tablas fact y dimensions.

### 📝 Pasos

1. **Ir a Model View**
   - Clic en ícono de modelo (lado izquierdo)
   - Organizar tablas (Fact en centro, Dims alrededor)

2. **Crear relaciones automáticamente**
   - Home > Manage Relationships > Autodetect
   - Revisar relaciones sugeridas

3. **Crear relaciones manualmente**
   ```
   DimProduct[ProductKey] ---(1:*)---> FactSales[ProductKey]
   - From: DimProduct[ProductKey]
   - To: FactSales[ProductKey]
   - Cardinality: One to Many (1:*)
   - Cross filter direction: Single
   - Make this relationship active: ✓
   ```

4. **Configurar propiedades**
   - Verificar cardinalidad (1:* para todas las dims)
   - Cross-filter direction: Single por default
   - Marcar relaciones como activas

5. **Gestionar relaciones inactivas** (si existen)
   - Identificar múltiples relaciones entre mismas tablas
   - Marcar una como active, otras como inactive
   - Usar USERELATIONSHIP en DAX para relaciones inactivas

### ✅ Comprobación

**Relaciones creadas**:

| From Table | From Column | To Table | To Column | Cardinality | Direction |
|-----------|-------------|----------|-----------|-------------|-----------|
| ___________ | ___________ | FactSales | ___________ | 1:* | Single |
| ___________ | ___________ | FactSales | ___________ | 1:* | Single |
| ___________ | ___________ | FactSales | ___________ | 1:* | Single |

**Total relaciones**: _______

**¿Todas las relaciones son 1:*?** ⬜ Sí ⬜ No

**¿Hay relaciones bidireccionales?** ⬜ Sí ⬜ No (debería ser No)

---

## 📋 Ejercicio 3: Crear Tabla de Calendario con DAX (35 minutos)

### 🎯 Objetivo
Generar tabla de calendario completa usando DAX para time intelligence.

### 📝 Pasos

1. **Crear tabla DimDate con DAX**
   ```dax
   DimDate = 
   ADDCOLUMNS(
       CALENDAR(DATE(2020,1,1), DATE(2025,12,31)),
       "Year", YEAR([Date]),
       "Quarter", "Q" & FORMAT([Date], "Q"),
       "QuarterNum", QUARTER([Date]),
       "Month", MONTH([Date]),
       "MonthName", FORMAT([Date], "MMMM"),
       "MonthShort", FORMAT([Date], "MMM"),
       "Day", DAY([Date]),
       "DayOfWeek", WEEKDAY([Date]),
       "DayName", FORMAT([Date], "DDDD"),
       "WeekNum", WEEKNUM([Date])
   )
   ```

2. **Agregar columnas adicionales**
   ```dax
   // Is Weekend
   IsWeekend = DimDate[DayOfWeek] IN {1, 7}
   
   // Fiscal Year (starts July 1)
   FiscalYear = 
   IF(
       MONTH(DimDate[Date]) >= 7,
       YEAR(DimDate[Date]) + 1,
       YEAR(DimDate[Date])
   )
   ```

3. **Marcar como Date Table**
   - Select DimDate table
   - Table Tools > Mark as Date Table
   - Select Date column as date column

4. **Relacionar con FactSales**
   - Crear relación: DimDate[Date] → FactSales[OrderDate]
   - Cardinality: 1:*

### ✅ Comprobación

**Tabla DimDate creada**: ⬜ Sí ⬜ No

**Columnas en DimDate**: _______

**Fecha mínima**: _______

**Fecha máxima**: _______

**¿Marcada como Date Table?** ⬜ Sí ⬜ No

**Relación con FactSales establecida**: ⬜ Sí ⬜ No

---

## 📋 Ejercicio 4: Medidas DAX Básicas (40 minutos)

### 🎯 Objetivo
Crear medidas fundamentales usando funciones de agregación.

### 📝 Pasos

1. **Medidas de agregación simple**
   ```dax
   Total Sales = SUM(FactSales[SalesAmount])
   
   Total Quantity = SUM(FactSales[Quantity])
   
   Average Sale = AVERAGE(FactSales[SalesAmount])
   
   Order Count = COUNT(FactSales[OrderID])
   
   Distinct Customers = DISTINCTCOUNT(FactSales[CustomerKey])
   ```

2. **Medidas con CALCULATE**
   ```dax
   Sales USA = 
   CALCULATE(
       [Total Sales],
       DimCustomer[Country] = "USA"
   )
   
   Sales Red Products = 
   CALCULATE(
       [Total Sales],
       DimProduct[Color] = "Red"
   )
   
   Sales Q1 = 
   CALCULATE(
       [Total Sales],
       DimDate[Quarter] = "Q1"
   )
   ```

3. **Medidas condicionales**
   ```dax
   High Value Orders = 
   CALCULATE(
       [Order Count],
       FactSales[SalesAmount] > 1000
   )
   
   Sales Category = 
   SWITCH(
       TRUE(),
       [Total Sales] > 1000000, "High",
       [Total Sales] > 500000, "Medium",
       "Low"
   )
   ```

4. **Organizar en carpetas (Display Folders)**
   - Select medidas relacionadas
   - Properties > Display Folder: "Sales Metrics"

### ✅ Comprobación

**Medidas DAX creadas**:

| Nombre Medida | Función Principal | Resultado Esperado |
|---------------|------------------|-------------------|
| Total Sales | SUM | _______________ |
| Order Count | COUNT | _______________ |
| Sales USA | CALCULATE | _______________ |
| High Value Orders | CALCULATE + Filter | _______________ |

**Total medidas creadas**: _______

**¿Medidas organizadas en folders?** ⬜ Sí ⬜ No

---

## 📋 Ejercicio 5: Time Intelligence con DAX (45 minutos)

### 🎯 Objetivo
Implementar cálculos de time intelligence para análisis temporal.

### 📝 Pasos

1. **Year-to-Date (YTD)**
   ```dax
   YTD Sales = 
   TOTALYTD(
       [Total Sales],
       DimDate[Date]
   )
   ```

2. **Quarter-to-Date (QTD)**
   ```dax
   QTD Sales = 
   TOTALQTD(
       [Total Sales],
       DimDate[Date]
   )
   ```

3. **Período anterior (Previous Period)**
   ```dax
   Sales Last Year = 
   CALCULATE(
       [Total Sales],
       SAMEPERIODLASTYEAR(DimDate[Date])
   )
   
   Sales Last Month = 
   CALCULATE(
       [Total Sales],
       DATEADD(DimDate[Date], -1, MONTH)
   )
   ```

4. **Year-over-Year Growth**
   ```dax
   YoY Growth = 
   DIVIDE(
       [Total Sales] - [Sales Last Year],
       [Sales Last Year],
       0
   )
   
   YoY Growth % = 
   FORMAT([YoY Growth], "0.0%")
   ```

5. **Moving Average (promedio móvil)**
   ```dax
   Sales 3M MA = 
   CALCULATE(
       [Total Sales],
       DATESINPERIOD(
           DimDate[Date],
           LASTDATE(DimDate[Date]),
           -3,
           MONTH
       )
   ) / 3
   ```

### ✅ Comprobación

**Time Intelligence Measures**:

| Medida | Función DAX | Valor Actual | Valor Esperado |
|--------|-------------|--------------|----------------|
| YTD Sales | TOTALYTD | ___________ | ___________ |
| Sales Last Year | SAMEPERIODLASTYEAR | ___________ | ___________ |
| YoY Growth % | DIVIDE | ___________ | ___________ |

**¿DimDate marcada como Date Table?** ⬜ Sí (requerido)

**¿Time intelligence funciona correctamente?** ⬜ Sí ⬜ No

---

## 📋 Ejercicio 6: Columnas Calculadas y Tablas Calculadas (35 minutos)

### 🎯 Objetivo
Crear columnas y tablas calculadas cuando sean apropiadas.

### 📝 Pasos

1. **Columnas calculadas en dimension**
   ```dax
   // En DimProduct
   Product Full Name = 
   DimProduct[Category] & " - " & DimProduct[ProductName]
   
   // En DimCustomer
   Customer Location = 
   DimCustomer[City] & ", " & DimCustomer[State]
   ```

2. **Columnas calculadas en fact (usar con precaución)**
   ```dax
   // En FactSales
   Total Line Amount = 
   FactSales[Quantity] * FactSales[UnitPrice]
   
   // Categoría de venta
   Sale Category = 
   IF(
       FactSales[SalesAmount] > 1000,
       "High Value",
       "Standard"
   )
   ```

3. **Tabla calculada: Summary Table**
   ```dax
   ProductSummary = 
   SUMMARIZE(
       FactSales,
       DimProduct[ProductName],
       DimProduct[Category],
       "Total Sales", [Total Sales],
       "Total Quantity", [Total Quantity]
   )
   ```

4. **Tabla calculada: Parameter Table**
   ```dax
   TopN Parameter = 
   DATATABLE(
       "Value", INTEGER,
       "Label", STRING,
       {
           {5, "Top 5"},
           {10, "Top 10"},
           {20, "Top 20"},
           {50, "Top 50"}
       }
   )
   ```

### ✅ Comprobación

**Columnas calculadas creadas**: _______

| Tabla | Columna | Fórmula DAX (simplificada) |
|-------|---------|----------------------------|
| ___________ | ___________ | ___________________________ |
| ___________ | ___________ | ___________________________ |

**Tablas calculadas creadas**: _______

**¿Se usaron columnas calculadas solo cuando necesario?** ⬜ Sí ⬜ No

---

## 📋 Ejercicio 7: Jerarquías y Agrupaciones (30 minutos)

### 🎯 Objetivo
Crear jerarquías para drilling y agrupaciones para categorización.

### 📝 Pasos

1. **Crear jerarquía de fechas**
   ```
   - En DimDate, seleccionar Year column
   - Right-click > Create Hierarchy
   - Nombre: Date Hierarchy
   - Arrastrar Quarter, Month, Day a la jerarquía
   ```

2. **Crear jerarquía de productos**
   ```
   Product Hierarchy:
   - Category
   - Subcategory
   - ProductName
   ```

3. **Crear jerarquía geográfica**
   ```
   Geography Hierarchy:
   - Country
   - State
   - City
   ```

4. **Crear grupos (bins)**
   ```
   - En FactSales, seleccionar SalesAmount
   - Right-click > New Group
   - Group type: Bin
   - Bin size: 500
   - Nombre: Sales Range
   ```

### ✅ Comprobación

**Jerarquías creadas**:

| Jerarquía | Niveles | Orden |
|-----------|---------|-------|
| Date Hierarchy | _______ | Year > Quarter > Month > Day |
| Product Hierarchy | _______ | Category > Subcategory > Product |
| Geography Hierarchy | _______ | Country > State > City |

**Grupos/Bins creados**: _______

**¿Jerarquías funcionan en visuales (drill down)?** ⬜ Sí ⬜ No

---

## 📋 Ejercicio 8: Optimización del Modelo (40 minutos)

### 🎯 Objetivo
Optimizar el modelo para mejor rendimiento y menor tamaño.

### 📝 Pasos

1. **Analizar tamaño del modelo**
   - View > Performance Analyzer > Start Recording
   - Crear visual y refresh
   - Stop Recording
   - Analizar resultados

2. **Eliminar columnas innecesarias**
   - En Model view, ocultar columnas no usadas
   - Eliminar columnas redundantes (ej: Full Name si hay First + Last)
   - Mantener solo keys necesarias

3. **Optimizar tipos de datos**
   ```
   - Text → Integer para IDs
   - Decimal → Fixed Decimal si rango conocido
   - DateTime → Date si no se necesita hora
   ```

4. **Reducir cardinalidad**
   - Identificar columnas high-cardinality en dimensions
   - Considerar agrupar valores poco frecuentes

5. **Deshabilitar auto date/time**
   - File > Options > Data Load
   - ☐ Auto Date/Time
   - (Usar DimDate en su lugar)

6. **Revisar y optimizar DAX**
   - Usar variables para cálculos intermedios
   - Evitar iteradores cuando no sea necesario
   - Usar DIVIDE en lugar de / para evitar errores

### ✅ Comprobación

**Optimizaciones aplicadas**:

| Optimización | Antes | Después | Mejora |
|--------------|-------|---------|--------|
| Tamaño modelo (MB) | _______ | _______ | _______% |
| Columnas totales | _______ | _______ | _______ menos |
| Query time (ms) | _______ | _______ | _______% |

**Auto Date/Time deshabilitado**: ⬜ Sí ⬜ No

**Tipos de datos optimizados**: ⬜ Sí ⬜ No

---

## 📊 Resumen de Tiempo

| Ejercicio | Duración Estimada | Duración Real |
|-----------|-------------------|---------------|
| 1. Diseñar Esquema Estrella | 35 min | _______ min |
| 2. Crear Relaciones | 40 min | _______ min |
| 3. Tabla de Calendario | 35 min | _______ min |
| 4. Medidas DAX Básicas | 40 min | _______ min |
| 5. Time Intelligence | 45 min | _______ min |
| 6. Columnas y Tablas Calculadas | 35 min | _______ min |
| 7. Jerarquías | 30 min | _______ min |
| 8. Optimización | 40 min | _______ min |
| **TOTAL** | **300 min (5 hrs)** | **_______ min** |

---

## ✅ Checklist Final

### Habilidades Desarrolladas
- [ ] Diseñar esquema estrella
- [ ] Crear y configurar relaciones
- [ ] Generar tabla de calendario con DAX
- [ ] Escribir medidas básicas de agregación
- [ ] Implementar time intelligence
- [ ] Crear columnas y tablas calculadas
- [ ] Configurar jerarquías para drilling
- [ ] Optimizar modelo para performance

### Archivo .pbix
- [ ] Esquema estrella implementado
- [ ] Al menos 10 medidas DAX creadas
- [ ] Time intelligence funcionando
- [ ] Jerarquías configuradas
- [ ] Modelo optimizado

---

## 🎯 Criterios de Éxito

✅ Esquema estrella implementado correctamente  
✅ Relaciones 1:* con single direction  
✅ Tabla de calendario funcional  
✅ Medidas DAX básicas e intermedias creadas  
✅ Time intelligence (YTD, YoY) funcionando  
✅ Modelo optimizado (<50% tamaño original)

---

## 🚀 Siguiente Paso

Actualiza `progreso.md` y continúa con:

**[Módulo 04: Visualize and Analyze the Data →](../04-visualize-analyze/README.md)**

---

**Tiempo total**: 270-300 minutos  
**Dificultad**: ⭐⭐⭐⭐ Intermedio-Avanzado  
**Última actualización**: Noviembre 2025
