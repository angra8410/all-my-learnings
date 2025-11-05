# 📊 Módulo 04: Visualize and Analyze the Data (25-30% del Examen)

## 🎯 Objetivos del Módulo

Al completar este módulo serás capaz de:

- Crear visualizaciones efectivas y profesionales
- Aplicar principios de diseño visual y UX
- Implementar interactividad (slicers, drill-through, bookmarks)
- Desarrollar cálculos DAX avanzados para análisis
- Configurar tooltips personalizados y formato condicional
- Optimizar rendimiento de informes
- Usar funciones de Q&A y quick insights

## 📚 Contenido Teórico

### 1. Principios de Visualización Efectiva

#### Reglas de Oro
- **Simplicidad**: Menos es más
- **Claridad**: Mensaje obvio en 5 segundos
- **Consistencia**: Colores y formatos uniformes
- **Jerarquía visual**: Guiar la atención del usuario

#### Tipos de Visuales y Cuándo Usarlos

| Visual | Usar Para | No Usar Para |
|--------|-----------|--------------|
| Bar/Column Chart | Comparaciones, rankings | Tendencias temporales largas |
| Line Chart | Tendencias en el tiempo | Comparaciones categóricas |
| Pie Chart | Proporciones (max 5 categorías) | Muchas categorías |
| Table/Matrix | Detalles exactos | Tendencias, patrones |
| Card | KPIs únicos | Múltiples métricas |
| Map | Datos geográficos | Datos sin componente geográfico |
| Scatter Plot | Correlaciones | Datos categóricos |

### 2. DAX Avanzado para Análisis

#### Iteradores
```dax
SUMX, AVERAGEX, COUNTX, MINX, MAXX
```

#### Variables
```dax
Profit Margin % = 
VAR TotalSales = [Total Sales]
VAR TotalCost = [Total Cost]
VAR Profit = TotalSales - TotalCost
RETURN
DIVIDE(Profit, TotalSales, 0)
```

#### Ranking
```dax
RANKX, TOPN
```

## ⏱️ Duración Estimada

- **Lectura**: 2-3 horas
- **Actividades**: 14-17 horas
- **Total**: 16-20 horas

## ✅ Próximos Pasos

1. ✅ Completar lectura
2. ⬜ Realizar actividad-interactiva.md
3. ⬜ Continuar con Módulo 05

---

**Peso en examen**: 25-30%  
**Nivel**: ⭐⭐⭐ Intermedio  

¡Continúa con la [Actividad Interactiva 04](actividad-interactiva.md)!
