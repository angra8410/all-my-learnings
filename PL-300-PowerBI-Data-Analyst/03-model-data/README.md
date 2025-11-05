# 📊 Módulo 03: Model the Data (25-30% del Examen)

## 🎯 Objetivos del Módulo

Al completar este módulo serás capaz de:

- Diseñar modelos de datos eficientes (esquemas estrella y copo de nieve)
- Crear y configurar relaciones entre tablas
- Implementar jerarquías, grupos y bins
- Escribir medidas DAX (funciones básicas e intermedias)
- Crear columnas calculadas y tablas calculadas
- Optimizar modelos para mejor rendimiento
- Aplicar mejores prácticas de modelado dimensional

## 📚 Contenido Teórico

### 1. Fundamentos de Modelado de Datos

####  Star Schema (Esquema Estrella)

```
         DimProduct
              |
         DimCustomer---FactSales---DimDate
              |
         DimGeography
```

**Características**:
- Tabla de hechos (Fact) en el centro
- Tablas de dimensiones (Dim) alrededor
- Relaciones directas entre Fact y Dims
- Denormalización de dimensiones

#### Snowflake Schema (Copo de Nieve)

```
    DimProductSubcategory
              |
         DimProduct
              |
          FactSales
```

**Características**:
- Dimensiones normalizadas
- Relaciones en múltiples niveles
- Menos redundancia de datos
- Más joins en queries

### 2. Relaciones en Power BI

#### Tipos de Cardinalidad

- **One-to-Many (1:*)**: Más común (Dim a Fact)
- **Many-to-One (*:1)**: Inverso de 1:*
- **One-to-One (1:1)**: Rara, generalmente indica problema de diseño
- **Many-to-Many (*:*)**: Requiere tabla puente (bridge table)

#### Direccionalidad de Filtros

- **Single (Una dirección)**: Default, filtros fluyen de "one" a "many"
- **Both (Bidireccional)**: Filtros en ambas direcciones (usar con precaución)

#### Cross-Filter Direction

```
DimProduct -----(1:*) (Single)-----> FactSales
(Filters flow this way →)
```

### 3. DAX Fundamentos

#### Contextos en DAX

**Row Context**: Evalúa fila por fila (columnas calculadas)
**Filter Context**: Filtros activos en el modelo (medidas)

#### Funciones Básicas

**Agregación**:
```dax
Total Sales = SUM(FactSales[SalesAmount])
Average Price = AVERAGE(FactSales[UnitPrice])
Count Orders = COUNT(FactSales[OrderID])
Distinct Products = DISTINCTCOUNT(FactSales[ProductID])
```

**Lógica**:
```dax
Sales Category = 
IF(
    [Total Sales] > 100000,
    "High",
    IF([Total Sales] > 50000, "Medium", "Low")
)
```

**CALCULATE** (La función más importante):
```dax
Sales 2023 = 
CALCULATE(
    [Total Sales],
    DimDate[Year] = 2023
)

Sales Red Products = 
CALCULATE(
    [Total Sales],
    DimProduct[Color] = "Red"
)
```

#### Time Intelligence

```dax
YTD Sales = 
TOTALYTD(
    [Total Sales],
    DimDate[Date]
)

Sales Last Year = 
CALCULATE(
    [Total Sales],
    SAMEPERIODLASTYEAR(DimDate[Date])
)

YoY Growth = 
DIVIDE(
    [Total Sales] - [Sales Last Year],
    [Sales Last Year]
)
```

### 4. Columnas Calculadas vs Medidas vs Tablas Calculadas

| Aspecto | Columna Calculada | Medida | Tabla Calculada |
|---------|------------------|--------|-----------------|
| **Cuándo se calcula** | Durante refresh | En query time | Durante refresh |
| **Contexto** | Row context | Filter context | N/A |
| **Almacenamiento** | Sí (ocupa espacio) | No | Sí |
| **Uso típico** | Categorización | Agregaciones | Reference tables, calendars |
| **Performance** | Impacto en refresh | Impacto en query | Impacto en refresh y tamaño |

### 5. Mejores Prácticas de Modelado

✅ **Hacer**:
- Usar esquemas estrella cuando sea posible
- Relaciones 1:* con single direction por default
- Medidas en lugar de columnas calculadas cuando sea posible
- Nombrar tablas Fact y Dim claramente
- Crear tabla de calendario (Date table)
- Marcar tabla de fechas como Date Table

❌ **Evitar**:
- Relaciones many-to-many sin tabla puente
- Bidirectional filters sin necesidad clara
- Columnas calculadas para agregaciones
- Relaciones circulares
- Dependencias complejas entre medidas

## 🎯 Habilidades Clave para el Examen

- [ ] Diseñar esquema estrella
- [ ] Crear relaciones 1:* correctamente
- [ ] Configurar cross-filter direction
- [ ] Escribir medidas básicas (SUM, AVERAGE, COUNT)
- [ ] Usar CALCULATE con filtros
- [ ] Implementar time intelligence (YTD, YoY)
- [ ] Crear columnas calculadas
- [ ] Generar tabla de calendario con DAX
- [ ] Crear jerarquías (Year > Quarter > Month > Day)
- [ ] Optimizar modelos (eliminar columnas, tipos de datos)

## ⏱️ Duración Estimada

- **Lectura**: 3-4 horas
- **Actividades prácticas**: 15-18 horas
- **Total**: 18-22 horas

## ✅ Próximos Pasos

1. ✅ Completar lectura de README
2. ⬜ Realizar actividad-interactiva.md
3. ⬜ Actualizar progreso.md
4. ⬜ Continuar con Módulo 04

---

**Peso en examen**: 25-30%  
**Nivel**: ⭐⭐⭐⭐ Intermedio-Avanzado  
**Prerequisitos**: Módulo 02 completado

¡Continúa con la [Actividad Interactiva 03](actividad-interactiva.md)!
