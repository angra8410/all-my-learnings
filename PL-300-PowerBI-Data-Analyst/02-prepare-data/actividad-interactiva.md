# 🎮 Actividad Interactiva 02: Prepare the Data - Ejercicios Prácticos

## 🎯 Objetivo

Dominar Power Query y las transformaciones de datos mediante ejercicios prácticos que cubren: conexión a fuentes de datos, limpieza, transformaciones, merge/append, lenguaje M, profiling y optimización.

**Duración total estimada**: 240-280 minutos (4-4.7 horas)

---

## 📋 Ejercicio 1: Conectar y Explorar Múltiples Fuentes de Datos (30 minutos)

### 🎯 Objetivo
Conectar Power BI a diferentes tipos de fuentes de datos y explorar sus opciones de conexión.

### 📝 Pasos

1. **Conectar a archivo Excel**
   - Abrir Power BI Desktop
   - Get Data > Excel Workbook
   - Descargar sample: Financial Sample (incluido en Power BI)
   - Seleccionar tabla "financials"
   - Clic en "Transform Data" para abrir Power Query

2. **Conectar a archivo CSV**
   - New Source > Text/CSV
   - Crear archivo CSV de prueba o descargar sample data
   - Verificar delimiter detection (coma, punto y coma, tab)
   - Aplicar encoding correcto (UTF-8, Windows-1252)

3. **Conectar a carpeta (Folder)**
   ```
   - New Source > Folder
   - Seleccionar carpeta con múltiples archivos CSV/Excel
   - Power Query detecta automáticamente estructura
   - Combine Files para consolidar
   ```

4. **Conectar a SQL Server** (si tienes acceso)
   ```
   - New Source > SQL Server
   - Server: <YOUR_SERVER>
   - Database: <YOUR_DATABASE>
   - Data Connectivity mode: Import
   - Seleccionar tabla o escribir SQL query
   ```

5. **Conectar a Web (API pública)**
   ```
   - New Source > Web
   - URL ejemplo: https://api.github.com/repos/microsoft/powerbi-desktop-samples
   - Autenticación: Anonymous
   - Explorar estructura JSON
   ```

### ✅ Comprobación

**Fuentes de datos conectadas**:
- ⬜ Excel (Financial Sample)
- ⬜ CSV
- ⬜ Folder (múltiples archivos)
- ⬜ SQL Server / Web

**Número total de queries creadas**: _______________

**Modo de conexión usado** (Import/DirectQuery): _______________

**¿Query folding habilitado** (verificar en View > Query Dependencies): ⬜ Sí ⬜ No ⬜ Parcial

---

## 📋 Ejercicio 2: Transformaciones Básicas de Limpieza (35 minutos)

### 🎯 Objetivo
Aplicar transformaciones comunes para limpiar y preparar datos.

### 📝 Pasos

1. **Remove Columns**
   - En query Financial Sample
   - Seleccionar columnas innecesarias (ej: redundantes, con muchos nulls)
   - Right-click > Remove Columns

2. **Rename Columns**
   - Renombrar columnas a nombres más descriptivos
   - Doble clic en header o Right-click > Rename
   - Usar nombres sin espacios y en snake_case o PascalCase

3. **Change Type**
   - Verificar tipos de datos en cada columna
   - Cambiar tipos incorrectos:
     - Fechas que aparecen como texto
     - Números que aparecen como texto
     - Texto que debería ser categoría

4. **Remove Duplicates**
   - Seleccionar columnas clave (ej: ID, Date, Product)
   - Right-click > Remove Duplicates
   - Verificar count antes y después

5. **Replace Values**
   ```
   - Identificar valores inconsistentes (ej: "USA" vs "United States")
   - Select column > Transform > Replace Values
   - From: "USA"
   - To: "United States"
   ```

6. **Fill Down**
   - Aplicar en columnas con valores repetidos en blanco
   - Select column > Transform > Fill > Down

7. **Trim & Clean**
   - Select text columns > Transform > Format > Trim
   - Transform > Format > Clean (remove non-printable characters)

### ✅ Comprobación

**Transformaciones aplicadas**:

| Transformación | Columna | Valores Antes | Valores Después |
|----------------|---------|---------------|-----------------|
| Remove Columns | _______________ | ___ cols | ___ cols |
| Change Type | _______________ | _______ | _______ |
| Remove Duplicates | _______________ | ___ rows | ___ rows |
| Replace Values | _______________ | ___ distinct | ___ distinct |

**Applied Steps count**: _______________

**¿Todos los tipos de datos son correctos?** ⬜ Sí ⬜ No

---

## 📋 Ejercicio 3: Split, Merge y Pivot Columns (40 minutos)

### 🎯 Objetivo
Restructurar datos usando split, merge, pivot y unpivot.

### 📝 Pasos

1. **Split Column by Delimiter**
   - Crear columna con valores delimitados (ej: "FirstName LastName" o "City, State")
   - Select column > Split Column > By Delimiter
   - Delimiter: Space, Comma, Custom
   - Split at: Left-most, Right-most, Each occurrence

2. **Split Column by Positions**
   - Para datos de ancho fijo (ej: "ABC123" → "ABC" y "123")
   - Select column > Split Column > By Number of Characters
   - Number of characters: 3
   - Split: Once, as far left as possible

3. **Merge Columns**
   - Seleccionar múltiples columnas (Ctrl+Click)
   - Transform > Merge Columns
   - Separator: Space, Comma, Custom, None
   - New column name: "FullName" o "Complete Address"

4. **Pivot Column** (columna a encabezado)
   ```
   Ejemplo de datos:
   Product | Metric  | Value
   A       | Sales   | 100
   A       | Units   | 10
   B       | Sales   | 200
   
   Pivot on: Metric
   Values: Value
   
   Resultado:
   Product | Sales | Units
   A       | 100   | 10
   B       | 200   | ?
   ```
   
   - Select column a pivotar > Transform > Pivot Column
   - Values Column: seleccionar columna numérica
   - Advanced options: Aggregate function (Sum, Count, Average, etc.)

5. **Unpivot Columns** (encabezados a columnas)
   ```
   Inverso de Pivot:
   
   Product | Jan | Feb | Mar
   A       | 10  | 20  | 30
   
   Unpivot columns Jan, Feb, Mar
   
   Resultado:
   Product | Attribute | Value
   A       | Jan       | 10
   A       | Feb       | 20
   A       | Mar       | 30
   ```
   
   - Select columns a unpivot > Transform > Unpivot Columns
   - Opciones: Unpivot Columns, Unpivot Other Columns, Unpivot Only Selected Columns

### ✅ Comprobación

**Restructuraciones realizadas**:

- **Split ejecutado en columna**: _______________  
  - Delimiter o posición: _______________
  - Columnas resultantes: _______________ y _______________

- **Merge ejecutado**:  
  - Columnas originales: _______________, _______________
  - Columna resultante: _______________

- **Pivot/Unpivot ejecutado**: ⬜ Pivot ⬜ Unpivot ⬜ Ambos  
  - Filas antes: _______________
  - Filas después: _______________
  - Columnas antes: _______________
  - Columnas después: _______________

---

## 📋 Ejercicio 4: Merge Queries (Joins) (40 minutos)

### 🎯 Objetivo
Combinar datos de múltiples tablas usando diferentes tipos de join.

### 📝 Pasos

1. **Preparar dos queries**
   ```
   Query 1: Sales
   - OrderID, ProductID, Quantity, Amount
   
   Query 2: Products
   - ProductID, ProductName, Category, Price
   ```

2. **Inner Join**
   - Select Sales query
   - Home > Merge Queries
   - Select Products as second table
   - Select ProductID in both tables
   - Join Kind: Inner (only matching rows)
   - Expand columns de Products query

3. **Left Outer Join**
   - Merge Sales con Products
   - Join Kind: Left Outer (all from Sales, matching from Products)
   - Útil para identificar ProductID sin información

4. **Full Outer Join**
   - Join Kind: Full Outer
   - Combina todas las filas de ambas tablas
   - Nulls donde no hay match

5. **Left Anti Join**
   - Join Kind: Left Anti
   - Solo filas de Sales que NO tienen match en Products
   - Útil para data quality checks

6. **Expand Merged Column**
   - Clic en ícono de expansión en columna merged
   - Seleccionar campos a traer de la segunda tabla
   - ☑ ProductName ☑ Category ☐ Use original column name as prefix

### ✅ Comprobación

**Merges realizados**:

| Join Type | Query 1 | Query 2 | Key Column | Rows Result |
|-----------|---------|---------|------------|-------------|
| Inner | ___________ | ___________ | ___________ | _______ |
| Left Outer | ___________ | ___________ | ___________ | _______ |
| Full Outer | ___________ | ___________ | ___________ | _______ |
| Left Anti | ___________ | ___________ | ___________ | _______ |

**Columnas expandidas en merge**: _______________

**¿Query folding se mantiene?** ⬜ Sí ⬜ No

---

## 📋 Ejercicio 5: Append Queries (Union) (25 minutos)

### 🎯 Objetivo
Combinar múltiples tablas con estructura similar verticalmente.

### 📝 Pasos

1. **Preparar queries para append**
   - Sales2023
   - Sales2024
   - Sales2025 (misma estructura)

2. **Append Two Tables**
   - Select Sales2023
   - Home > Append Queries
   - Select Sales2024
   - Verifica column matching

3. **Append Three or More Tables**
   - Home > Append Queries > Three or more tables
   - Add Sales2023, Sales2024, Sales2025
   - Verifica orden
   - New query name: "SalesAllYears"

4. **Verificar y limpiar**
   - Check column count (should match)
   - Check data types (should be consistent)
   - Remove duplicate rows si necesario
   - Add column "Source" para tracking (opcional)

### ✅ Comprobación

**Append ejecutado**:

- **Queries combinadas**: _______________, _______________, _______________
- **Filas Query 1**: _______________
- **Filas Query 2**: _______________
- **Filas Query 3**: _______________
- **Total filas en resultado**: _______________
- **Columnas**: _______________ (debe ser igual en todas)

**¿Se agregó columna de tracking de fuente?** ⬜ Sí ⬜ No

---

## 📋 Ejercicio 6: Lenguaje M - Custom Columns y Functions (45 minutos)

### 🎯 Objetivo
Escribir código M para transformaciones personalizadas y funciones reutilizables.

### 📝 Pasos

1. **Add Custom Column con lógica condicional**
   ```m
   // Add Column > Custom Column
   // Name: SalesCategory
   
   if [Sales] < 1000 then "Low"
   else if [Sales] < 5000 then "Medium"
   else "High"
   ```

2. **Add Custom Column con funciones de texto**
   ```m
   // Name: EmailDomain
   
   Text.AfterDelimiter([Email], "@")
   ```

3. **Add Custom Column con funciones de fecha**
   ```m
   // Name: FiscalYear
   // (Fiscal year starts July 1)
   
   let
       CalendarYear = Date.Year([Date]),
       Month = Date.Month([Date]),
       FY = if Month >= 7 then CalendarYear + 1 else CalendarYear
   in
       FY
   ```

4. **Crear función personalizada**
   ```m
   // New Source > Blank Query
   // Name: fnGetDiscount
   
   (amount as number) as number =>
       let
           discount = if amount > 10000 then 0.15
                      else if amount > 5000 then 0.10
                      else 0.05
       in
           discount
   ```

5. **Invocar función personalizada**
   ```m
   // In main query, Add Column > Invoke Custom Function
   // Select fnGetDiscount
   // Parameter: [Amount]
   ```

6. **Try-Otherwise para error handling**
   ```m
   // Add Custom Column: SafeDivision
   
   try [Revenue] / [Quantity] otherwise 0
   ```

### ✅ Comprobación

**Código M escrito**:

Custom Column 1:
```m
_________________________________________________________________

_________________________________________________________________
```

Custom Column 2:
```m
_________________________________________________________________

_________________________________________________________________
```

**Función creada**: ⬜ Sí ⬜ No

**Nombre de función**: _______________

**¿Función invocada correctamente?** ⬜ Sí ⬜ No

**¿Try-otherwise usado para handling errors?** ⬜ Sí ⬜ No

---

## 📋 Ejercicio 7: Data Profiling y Quality Checks (30 minutos)

### 🎯 Objetivo
Utilizar herramientas de profiling para detectar problemas de calidad de datos.

### 📝 Pasos

1. **Activar Data Profiling**
   - View tab > Data Preview section
   - ☑ Column quality
   - ☑ Column distribution
   - ☑ Column profile
   - Cambiar profiling de "Based on top 1000 rows" a "Column profiling based on entire data set"

2. **Analizar Column Quality**
   - Revisar cada columna
   - Identificar % Valid, Error, Empty
   - Documentar columnas problemáticas

3. **Analizar Column Distribution**
   - Verificar Distinct vs Unique counts
   - Identificar columnas con pocos valores únicos (candidatas a dimensiones)
   - Detectar valores anómalos en histogramas

4. **Analizar Column Profile**
   - Para columnas numéricas: Min, Max, Average, Std Dev
   - Detectar outliers
   - Para columnas de texto: longitud Min/Max
   - Para fechas: rango de fechas

5. **Resolver problemas detectados**
   - Replace Errors en columnas con errores
   - Fill Down/Up para valores vacíos estratégicos
   - Remove Rows con errores críticos
   - Add Filter para remover outliers extremos

6. **Documentar data quality metrics**
   - Crear tabla de resumen:
     - Columnas con >5% errores
     - Columnas con >20% valores vacíos
     - Outliers detectados y acción tomada

### ✅ Comprobación

**Profiling activado**: ⬜ Column quality ⬜ Column distribution ⬜ Column profile

**Data Quality Report**:

| Columna | Valid % | Error % | Empty % | Distinct | Unique | Acción Tomada |
|---------|---------|---------|---------|----------|--------|---------------|
| ___________ | ___% | ___% | ___% | _____ | _____ | _______________ |
| ___________ | ___% | ___% | ___% | _____ | _____ | _______________ |
| ___________ | ___% | ___% | ___% | _____ | _____ | _______________ |

**Errores totales resueltos**: _______________

**Rows removidos por calidad**: _______________

---

## 📋 Ejercicio 8: Query Optimization y Performance (35 minutos)

### 🎯 Objetivo
Optimizar queries para mejor rendimiento y entender query folding.

### 📝 Pasos

1. **Activar Query Diagnostics**
   - Tools > Session Diagnostics > Start Diagnostics
   - Ejecutar refresh de queries
   - Tools > Session Diagnostics > Stop Diagnostics
   - Revisar archivos generados

2. **Analizar Query Folding**
   - Right-click en último paso > View Native Query
   - Si aparece SQL: Query folding funciona ✅
   - Si error "cannot be folded": Query folding roto ❌

3. **Identificar pasos que rompen folding**
   ```
   Pasos que típicamente rompen folding:
   - Add Column con funciones M complejas
   - Merge con query no-foldable
   - Conversiones de tipo no soportadas por source
   ```

4. **Optimizar orden de pasos**
   ```
   Mala práctica:
   1. Source
   2. Remove other columns
   3. Filter rows
   
   Buena práctica:
   1. Source
   2. Filter rows (reduce data early)
   3. Remove other columns
   ```

5. **Reducir datos temprano**
   - Aplicar filtros lo antes posible en Applied Steps
   - Remover columnas innecesarias temprano
   - Evitar traer todas las columnas con SELECT *

6. **Usar parámetros para conexiones**
   ```m
   // Create Parameter
   Home > Manage Parameters > New Parameter
   Name: ServerName
   Type: Text
   Default: "MyServer"
   
   // Use in connection
   Source = Sql.Database(ServerName, "MyDatabase")
   ```

7. **Review y limpieza**
   - Eliminar Applied Steps redundantes
   - Combinar pasos similares cuando sea posible
   - Renombrar steps para claridad

### ✅ Comprobación

**Query Diagnostics ejecutado**: ⬜ Sí ⬜ No

**Query Folding Status**:

| Query | Folding Works | Native Query Visible |
|-------|---------------|---------------------|
| ___________ | ⬜ Sí ⬜ No | ⬜ Sí ⬜ No |
| ___________ | ⬜ Sí ⬜ No | ⬜ Sí ⬜ No |

**Optimizaciones aplicadas**:
- ⬜ Filtros movidos arriba en Applied Steps
- ⬜ Columnas removidas temprano
- ⬜ Pasos redundantes eliminados
- ⬜ Parámetros creados para reutilización

**Performance mejorado** (tiempo de refresh):
- Antes: _______________ segundos
- Después: _______________ segundos
- Mejora: _______________% 

---

## 📊 Resumen de Tiempo

| Ejercicio | Duración Estimada | Duración Real |
|-----------|-------------------|---------------|
| 1. Conectar Fuentes de Datos | 30 min | _______ min |
| 2. Transformaciones Básicas | 35 min | _______ min |
| 3. Split, Merge, Pivot | 40 min | _______ min |
| 4. Merge Queries (Joins) | 40 min | _______ min |
| 5. Append Queries | 25 min | _______ min |
| 6. Lenguaje M | 45 min | _______ min |
| 7. Data Profiling | 30 min | _______ min |
| 8. Optimization | 35 min | _______ min |
| **TOTAL** | **280 min (4.7 hrs)** | **_______ min** |

---

## ✅ Checklist Final de Verificación

### Habilidades Desarrolladas
- [ ] Conectar a múltiples tipos de fuentes de datos
- [ ] Aplicar transformaciones básicas de limpieza
- [ ] Split y merge de columnas
- [ ] Pivot y unpivot datos
- [ ] Merge queries con diferentes join types
- [ ] Append múltiples queries
- [ ] Escribir código M para custom columns
- [ ] Crear y usar funciones personalizadas en M
- [ ] Usar data profiling para detectar problemas
- [ ] Optimizar queries para performance
- [ ] Verificar query folding

### Archivos Generados
- [ ] Al menos 5 queries en Power Query Editor
- [ ] 1-2 funciones personalizadas creadas
- [ ] Parámetros configurados (opcional)
- [ ] Query diagnostics ejecutados y revisados

### Conocimientos Clave
- [ ] Entiendo diferencia entre Import y DirectQuery
- [ ] Sé cuándo usar Merge vs Append
- [ ] Conozco los tipos de Join y cuándo usar cada uno
- [ ] Puedo escribir código M básico
- [ ] Entiendo qué es query folding y por qué importa
- [ ] Sé cómo optimizar queries para performance

---

## 🎯 Criterios de Éxito

Has completado exitosamente este módulo si:

✅ Completaste al menos 7 de 8 ejercicios  
✅ Tienes queries funcionales con múltiples transformaciones  
✅ Escribiste al menos 2 custom columns con código M  
✅ Realizaste merge y append exitosamente  
✅ Usaste data profiling y resolviste problemas detectados  
✅ Optimizaste al menos una query y mejoraste performance  

---

## 📝 Notas y Observaciones

Espacio para tus notas personales:

_______________________________________________

_______________________________________________

_______________________________________________

---

## 🚀 Siguiente Paso

¡Excelente trabajo! Actualiza tu archivo `progreso.md` con tu avance y continúa con:

**[Módulo 03: Model the Data →](../03-model-data/README.md)**

---

**Tiempo total**: 240-280 minutos  
**Dificultad**: ⭐⭐⭐ Intermedio  
**Última actualización**: Noviembre 2025
