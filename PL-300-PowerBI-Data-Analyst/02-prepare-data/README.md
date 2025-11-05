# 📊 Módulo 02: Prepare the Data (25-30% del Examen)

## 🎯 Objetivos del Módulo

Al completar este módulo serás capaz de:

- Conectar Power BI a múltiples fuentes de datos (archivos, bases de datos, servicios web, APIs)
- Utilizar Power Query para transformar y limpiar datos
- Aplicar transformaciones comunes (merge, append, pivot, unpivot, split, replace)
- Escribir código en lenguaje M para transformaciones personalizadas
- Perfilar datos para detectar problemas de calidad
- Implementar dataflows en Power BI Service
- Optimizar consultas para mejorar rendimiento
- Aplicar mejores prácticas de ETL en Power BI

## 📚 Contenido Teórico

### 1. Fuentes de Datos en Power BI

#### Categorías de Conectores

**Archivos**:
- Excel (.xlsx, .xls, .xlsm)
- CSV / Text files
- XML
- JSON
- Parquet
- PDF (tablas)
- Carpetas (folder connector)

**Bases de Datos**:
- SQL Server
- Azure SQL Database
- Oracle
- PostgreSQL
- MySQL
- IBM DB2
- Teradata
- Access

**Servicios en la Nube**:
- SharePoint Online
- Dynamics 365
- Salesforce
- Google Analytics
- Azure Blob Storage
- AWS S3
- OneDrive

**APIs y Web**:
- Web (URLs)
- OData feed
- REST APIs
- GraphQL (mediante conector web)

**Otros**:
- Power BI datasets
- Dataflows
- Blank Query (para código M manual)

#### Modos de Conexión

1. **Import** (Importar):
   - Datos se cargan en el modelo Power BI
   - Mejor rendimiento para consultas
   - Limitación de tamaño (1GB en Pro, más en Premium)
   - Requiere refresh programado

2. **DirectQuery**:
   - Queries en tiempo real a la fuente
   - No limitación de tamaño de datos
   - Performance depende de fuente de datos
   - Limitaciones en transformaciones DAX

3. **Composite** (Mixto):
   - Combinación de Import y DirectQuery
   - Agregaciones para performance
   - Disponible en Premium

### 2. Power Query Editor

#### Interfaz Principal

```
┌─────────────────────────────────────────┐
│ Home | Transform | Add Column | View   │ ← Ribbon
├─────────────────────────────────────────┤
│ Queries │ Query Preview              │
│ Panel   │ (Data sample - 1000 rows)   │
│         │                              │
│ Query1  │ Col1   Col2   Col3          │
│ Query2  │ data   data   data          │
│         │ data   data   data          │
├─────────────────────────────────────────┤
│ Applied Steps:                          │
│ - Source                                │
│ - Changed Type                          │
│ - Removed Columns                       │
└─────────────────────────────────────────┘
```

#### Transformaciones Básicas

**Limpieza**:
- Remove Rows (duplicates, errors, blanks, top/bottom)
- Replace Values
- Fill Up / Fill Down
- Trim / Clean
- Remove Duplicates

**Estructura**:
- Remove Columns / Keep Columns
- Rename Columns
- Reorder Columns
- Change Data Type
- Split Column (by delimiter, positions, length)
- Merge Columns

**Agregación**:
- Group By
- Pivot Column
- Unpivot Columns

**Combinar**:
- Merge Queries (Join types: Inner, Left Outer, Right Outer, Full Outer, Left Anti, Right Anti)
- Append Queries (Union)

### 3. Lenguaje M (Power Query Formula Language)

#### Sintaxis Básica

```m
let
    // Paso 1: Define fuente de datos
    Source = Excel.Workbook(File.Contents("C:\Data\Sales.xlsx"), null, true),
    
    // Paso 2: Selecciona tabla
    SalesTable = Source{[Item="Sales",Kind="Table"]}[Data],
    
    // Paso 3: Cambia tipos de datos
    ChangedType = Table.TransformColumnTypes(SalesTable, {
        {"Date", type date},
        {"Amount", type number},
        {"Customer", type text}
    }),
    
    // Paso 4: Filtra datos
    FilteredRows = Table.SelectRows(ChangedType, each [Amount] > 100),
    
    // Paso 5: Agrega columna calculada
    AddedColumn = Table.AddColumn(FilteredRows, "Year", each Date.Year([Date]))
in
    AddedColumn
```

#### Funciones M Comunes

**Texto**:
- `Text.Upper()`, `Text.Lower()`, `Text.Proper()`
- `Text.Length()`, `Text.Start()`, `Text.End()`
- `Text.Trim()`, `Text.Clean()`
- `Text.Replace()`, `Text.Remove()`
- `Text.Split()`, `Text.Combine()`

**Números**:
- `Number.Round()`, `Number.RoundUp()`, `Number.RoundDown()`
- `Number.Abs()`, `Number.Mod()`
- `Number.From()` (conversión)

**Fechas**:
- `Date.Year()`, `Date.Month()`, `Date.Day()`
- `Date.DayOfWeek()`, `Date.AddDays()`, `Date.AddMonths()`
- `Date.StartOfMonth()`, `Date.EndOfMonth()`
- `DateTime.LocalNow()`, `DateTime.From()`

**Tablas**:
- `Table.SelectRows()` (filtrar)
- `Table.SelectColumns()` (seleccionar columnas)
- `Table.AddColumn()` (agregar columna)
- `Table.TransformColumns()` (transformar)
- `Table.ReplaceValue()` (reemplazar)
- `Table.Group()` (agrupar)
- `Table.Join()` (merge)
- `Table.Combine()` (append)

**Lógica**:
- `if... then... else`
- `and`, `or`, `not`
- `try... otherwise`

### 4. Perfilado de Datos (Data Profiling)

#### Activar Profiling

En Power Query Editor:
- View tab > Data Preview section
- ☑ Column quality
- ☑ Column distribution
- ☑ Column profile

#### Métricas de Calidad

**Column Quality**:
- Valid %
- Error %
- Empty %

**Column Distribution**:
- Distinct values
- Unique values
- Histograma de distribución

**Column Profile** (basado en primeras 1000 o todas las filas):
- Count
- Error
- Empty
- Distinct
- Unique
- Min / Max (para números y fechas)
- Average, Standard Deviation (números)

### 5. Dataflows

#### Qué son los Dataflows

- ETL centralizado en Power BI Service
- Reutilización de transformaciones entre datasets
- Almacenamiento en Azure Data Lake (Premium)
- Scheduled refresh independiente

#### Componentes

1. **Linked Entities**: Reutilizan queries existentes
2. **Computed Entities**: Transformaciones adicionales sobre linked entities
3. **Refresh**: Programación independiente del dataset

#### Cuándo Usar Dataflows

✅ Usar cuando:
- Múltiples datasets usan misma fuente
- Transformaciones complejas compartidas
- Separar ETL de modelo semántico
- Premium workspace disponible

❌ No usar cuando:
- Datos simples de una sola fuente
- Solo un dataset consume los datos
- No tienes Premium capacity

### 6. Optimización de Consultas

#### Mejores Prácticas

1. **Query Folding**:
   - Permitir que transformaciones se ejecuten en la fuente
   - Evitar pasos que "rompen" el folding:
     - Add Column con M functions complejas
     - Merge de queries no foldables
     - Algunas transformaciones de texto

2. **Reducir Datos Temprano**:
   - Filtrar filas lo antes posible
   - Remover columnas innecesarias al inicio
   - Aplicar SELECT específico en queries SQL

3. **Evitar Pasos Innecesarios**:
   - Revisar Applied Steps y eliminar redundantes
   - Combinar pasos cuando sea posible

4. **Tipos de Datos Correctos**:
   - Asignar tipos apropiados (fecha, número, texto)
   - Power BI auto-detecta, pero verificar siempre

5. **Referencias vs Duplicates**:
   - Usar Reference cuando quieres modificar una query existente
   - Duplicate crea copia independiente

#### Query Diagnostics

En Power Query:
- Tools > Session Diagnostics > Start Diagnostics
- Ejecutar queries
- Tools > Session Diagnostics > Stop Diagnostics
- Analizar resultados (tiempo, query folding)

## 🎯 Habilidades Clave para el Examen

### Debes Saber Hacer

- [ ] Conectar a archivos (Excel, CSV, JSON, folder)
- [ ] Conectar a bases de datos (SQL Server, Azure SQL)
- [ ] Conectar a web (URLs, APIs con autenticación)
- [ ] Aplicar transformaciones básicas (remove, rename, type)
- [ ] Merge queries (diferentes tipos de join)
- [ ] Append queries (combinar tablas)
- [ ] Pivot y Unpivot columnas
- [ ] Split columns (delimiter, positions)
- [ ] Group by con agregaciones
- [ ] Escribir código M básico para columnas calculadas
- [ ] Identificar errores con profiling
- [ ] Aplicar Replace Errors
- [ ] Crear parámetros de query
- [ ] Entender query folding
- [ ] Configurar refresh programado

### Escenarios de Examen Comunes

**Escenario 1**: Combinar datos de Excel y SQL
- Merge con diferentes join types
- Seleccionar columnas correctas

**Escenario 2**: Limpiar datos desordenados
- Unpivot para normalizar
- Split de columnas
- Replace values

**Escenario 3**: Optimizar performance
- Identificar qué rompe query folding
- Reordenar pasos para eficiencia

**Escenario 4**: API Web con paginación
- Código M para iterar páginas
- Autenticación (API key, OAuth)

## 📊 Comparación de Conectores

| Tipo | Import | DirectQuery | Refresh | Uso Común |
|------|--------|-------------|---------|-----------|
| Excel | ✅ | ❌ | Manual/Scheduled | Datasets pequeños |
| CSV | ✅ | ❌ | Manual/Scheduled | Archivos planos |
| SQL Server | ✅ | ✅ | Scheduled | Data warehouse |
| Azure SQL | ✅ | ✅ | Scheduled | Cloud databases |
| SharePoint | ✅ | ❌ | Scheduled | Colaboración |
| OData | ✅ | ✅ | Scheduled | Web services |
| Web | ✅ | ❌ | Manual/Scheduled | APIs, scraping |

## ⏱️ Duración Estimada

- **Lectura de contenido**: 2-3 horas
- **Actividades prácticas**: 16-19 horas
- **Total**: 18-22 horas

## 📝 Evaluación de Conocimientos Previos

Antes de comenzar, evalúa tu nivel (1-5):

- [ ] Conexión a diferentes fuentes de datos: ___/5
- [ ] Uso de Power Query Editor: ___/5
- [ ] Transformaciones básicas (rename, type, remove): ___/5
- [ ] Merge y Append de tablas: ___/5
- [ ] Lenguaje M: ___/5
- [ ] Pivot y Unpivot: ___/5
- [ ] Data profiling: ___/5

**Total**: ___/35

## ✅ Próximos Pasos

1. ✅ Completar lectura de este README
2. ⬜ Realizar actividad-interactiva.md (8 ejercicios prácticos)
3. ⬜ Actualizar progreso.md
4. ⬜ Revisar retroalimentacion.md
5. ⬜ Explorar recursos.md para profundizar
6. ⬜ Comenzar Módulo 03: Model the Data

---

**Peso en examen**: 25-30%  
**Nivel de dificultad**: ⭐⭐⭐ Intermedio  
**Prerequisitos**: Módulo 01 completado  

¡Continúa con la [Actividad Interactiva 02](actividad-interactiva.md)!
