# 🎮 Actividad Interactiva 04: Visualize and Analyze - Ejercicios Prácticos

## 🎯 Objetivo

Dominar creación de visualizaciones efectivas, interactividad y análisis con DAX avanzado.

**Duración total estimada**: 240-270 minutos (4-4.5 horas)

---

## 📋 Ejercicio 1: Dashboard Profesional (35 min)

### Pasos
1. Crear 4 cards para KPIs
2. Line chart para tendencias
3. Bar chart para rankings
4. Map para geografía
5. Table con formato condicional

### ✅ Comprobación
- Visuales creados: _______
- Dashboard claro: ⬜ Sí ⬜ No

---

## 📋 Ejercicio 2: Slicers y Sincronización (30 min)

### Pasos
1. Slicer de fechas (Between type)
2. Slicer de categorías (List)
3. Sync slicers entre páginas
4. Configure interaction entre visuales

### ✅ Comprobación
- Slicers sincronizados: ⬜ Sí ⬜ No

---

## 📋 Ejercicio 3: Drill-Through y Bookmarks (40 min)

### Pasos
1. Crear página drill-through
2. Configurar bookmarks
3. Agregar botones de navegación
4. Selection pane para hide/show

### ✅ Comprobación
- Drill-through funcional: ⬜ Sí ⬜ No
- Bookmarks: _______

---

## 📋 Ejercicio 4: DAX Avanzado (45 min)

### Ejemplos DAX
```dax
// Iteradores
Total Profit = SUMX(FactSales, [Quantity] * ([Price] - [Cost]))

// Variables
Profit % = 
VAR Sales = [Total Sales]
VAR Cost = [Total Cost]
RETURN DIVIDE(Sales - Cost, Sales, 0)

// Ranking
Product Rank = RANKX(ALL(Product), [Total Sales],,DESC)
```

### ✅ Comprobación
- Medidas creadas: _______

---

## 📋 Ejercicio 5: Tooltips Personalizados (30 min)

### Pasos
1. Crear página tooltip (320x240)
2. Agregar visuales pequeños
3. Aplicar a visual principal

### ✅ Comprobación
- Tooltips funcionando: ⬜ Sí ⬜ No

---

## 📋 Ejercicio 6: Formato Condicional (30 min)

### Pasos
1. Background color en table
2. Data bars
3. Icons (arrows, traffic lights)

### ✅ Comprobación
- Formato aplicado: _______

---

## 📋 Ejercicio 7: Q&A Visual (25 min)

### Pasos
1. Insert Q&A visual
2. Probar preguntas
3. Configurar synonyms

### ✅ Comprobación
- Q&A implementado: ⬜ Sí ⬜ No

---

## 📋 Ejercicio 8: Performance Optimization (35 min)

### Pasos
1. Performance Analyzer
2. Reducir visuales por página
3. Optimizar medidas DAX
4. Reducir cardinalidad

### ✅ Comprobación
- Performance antes: _______ ms
- Performance después: _______ ms
- Mejora: _______ %

---

## 📊 Resumen
| Ejercicio | Estimado | Real |
|-----------|----------|------|
| TOTAL | 270 min | _____ min |

---

**Siguiente**: [Módulo 05 →](../05-manage-secure/README.md)

**Última actualización**: Noviembre 2025
