# Módulo 2: Fuentes de Datos y Modelado

## Introducción

¡Bienvenido al Módulo 2! Ahora que entiendes qué es BI y Power BI, es momento de trabajar con datos reales. En este módulo aprenderás:

- Conectar Power BI a diferentes fuentes de datos
- Importar vs DirectQuery vs Live Connection
- Introducción a Power Query Editor
- Transformaciones básicas de datos
- Modelado de datos y relaciones
- Esquemas estrella y copo de nieve
- Buenas prácticas en modelado

## ¿Por qué es importante?

**"Un buen modelo de datos es el 80% del éxito en Power BI"**

Sin datos bien estructurados y modelados, las mejores visualizaciones no servirán de nada. Un modelo sólido:

- ✅ Mejora el rendimiento de tus informes
- ✅ Facilita la creación de medidas y cálculos
- ✅ Hace que tus análisis sean más precisos
- ✅ Permite escalar tu solución conforme creces
- ✅ Reduce errores y ambigüedades

## Conceptos Principales

### 1. Fuentes de Datos en Power BI

Power BI puede conectarse a más de 100 fuentes diferentes:

**Archivos locales:**
- 📄 Excel (.xlsx, .xls, .csv)
- 📊 CSV/TXT (texto delimitado)
- 📁 Carpetas (múltiples archivos)
- 🗂️ XML, JSON
- 📈 Power BI Desktop (.pbix)

**Bases de datos:**
- 🗄️ SQL Server
- 🐬 MySQL, PostgreSQL
- 🔷 Azure SQL Database
- ☁️ Oracle, IBM DB2
- 📦 Access

**Servicios en la nube:**
- ☁️ SharePoint Online
- 📊 Google Analytics
- 💼 Salesforce
- 📧 Dynamics 365
- 📈 Google Sheets

**Web:**
- 🌐 Páginas web (web scraping)
- 🔗 APIs REST
- 📡 OData feeds

### 2. Métodos de Conectividad

**Import (Importar)** - El más común
- Los datos se copian a Power BI
- ✅ Mejor rendimiento
- ✅ Todas las características disponibles
- ⚠️ Requiere espacio de almacenamiento
- ⚠️ Necesita actualizaciones programadas

**Ejemplo de uso**: Reportes de ventas que se actualizan diariamente.

**DirectQuery**
- Power BI consulta los datos en tiempo real
- ✅ Datos siempre actualizados
- ✅ No requiere almacenamiento local
- ⚠️ Más lento que Import
- ⚠️ Algunas limitaciones en transformaciones

**Ejemplo de uso**: Dashboard en vivo de un sistema de inventario.

**Live Connection**
- Conexión directa a modelos semánticos existentes
- Se usa con Analysis Services o Power BI Service
- ✅ Reutiliza modelos empresariales
- ⚠️ No puedes modificar el modelo

### 3. Power Query Editor - Tu Herramienta de Transformación

**Power Query** es donde preparas y limpias tus datos. Es como una cocina donde preparas los ingredientes antes de cocinar.

**Operaciones comunes en Power Query:**

**Limpieza de datos:**
- Eliminar filas vacías
- Rellenar valores faltantes
- Corregir tipos de datos
- Eliminar duplicados
- Reemplazar valores

**Transformaciones:**
- Dividir columnas (ej: separar nombre completo en nombre y apellido)
- Combinar columnas
- Pivotar/Despivotar tablas
- Agregar columnas calculadas
- Filtrar filas

**Ejemplo práctico:**
```
Datos originales (Excel):
Nombre Completo | Ventas
Juan Pérez      | $1,500
María García    | $2,300

Después de Power Query:
Nombre | Apellido | Ventas
Juan   | Pérez    | 1500
María  | García   | 2300
```

**Características importantes:**
- ✨ Todo es visual (no necesitas código)
- 📝 Cada paso se registra automáticamente
- 🔄 Pasos son repetibles y editables
- 🎯 Lenguaje M subyacente (avanzado, opcional)

### 4. Modelado de Datos

**¿Qué es un modelo de datos?**

Un modelo de datos define cómo se relacionan tus tablas entre sí. Es como un mapa que muestra cómo conectar diferentes piezas de información.

**Componentes clave:**

**Tablas de Hechos (Fact Tables)**
- Contienen datos transaccionales o métricas
- Ejemplo: Tabla de Ventas con cada transacción
- Típicamente tienen muchas filas
- Columnas: Cantidad, Precio, Fecha, IDs de dimensiones

**Tablas de Dimensiones (Dimension Tables)**
- Describen el contexto de los hechos
- Ejemplo: Tabla de Productos, Clientes, Fechas
- Menos filas que las tablas de hechos
- Columnas: Atributos descriptivos (Nombre, Categoría, País)

**Analogía**: 
- **Hechos** = Las transacciones en tu recibo de compra
- **Dimensiones** = Información sobre qué compraste, dónde, cuándo

### 5. Relaciones entre Tablas

**Tipos de relaciones:**

**Uno a muchos (1:*)** - La más común
- Un registro en la tabla de dimensión se relaciona con muchos en la tabla de hechos
- Ejemplo: Un producto puede aparecer en muchas ventas

```
Tabla Productos (1)  →  Tabla Ventas (*)
ProductoID: 1            ProductoID: 1 (5 ventas)
Nombre: Laptop           ProductoID: 1 (más ventas)
```

**Uno a uno (1:1)** - Poco común
- Un registro relacionado con solo un registro en otra tabla
- Ejemplo: Empleado → Detalle de empleado

**Muchos a muchos (*.*)** - Evitar cuando sea posible
- Requiere tabla puente/intermediaria
- Más complejo de manejar

**Cardinalidad y dirección del filtro:**
- **Cardinalidad**: Cuántos registros se relacionan (1:*, 1:1)
- **Dirección del filtro**: En qué dirección fluyen los filtros
  - **Unidireccional** (Single): Filtros van en una dirección
  - **Bidireccional** (Both): Filtros van en ambas direcciones ⚠️ Usar con cuidado

### 6. Esquemas de Modelado

**Esquema Estrella (Star Schema)** - ⭐ Recomendado

```
        Dimensión Producto
               |
Dimensión ← Hechos Ventas → Dimensión Cliente
  Fecha         |
           Dimensión
           Ubicación
```

**Características:**
- ✅ Simple y fácil de entender
- ✅ Excelente rendimiento
- ✅ Fácil de mantener
- Una tabla de hechos central
- Dimensiones conectadas directamente

**Esquema Copo de Nieve (Snowflake Schema)**

```
        Producto → Categoría
             |
        Hechos Ventas → Cliente → Ciudad → País
             |
           Fecha
```

**Características:**
- Dimensiones normalizadas (divididas)
- ⚠️ Más complejo
- ⚠️ Puede ser más lento
- Ahorra espacio (menos duplicación)
- Generalmente se prefiere estrella en Power BI

### 7. Tabla de Calendario (Date Table)

**¡MUY IMPORTANTE!** Una tabla de calendario es esencial para análisis de tiempo.

**¿Por qué necesitas una tabla de calendario?**
- Permite análisis consistentes por fecha
- Habilita inteligencia de tiempo (YTD, MTD, etc.)
- Puedes agregar atributos (trimestre, semana, día festivo)

**Ejemplo de tabla de calendario:**
```
Fecha       | Año  | Mes | Trimestre | DíaSemana | EsFinDeSemana
2024-01-01  | 2024 | 1   | Q1        | Lunes     | No
2024-01-02  | 2024 | 1   | Q1        | Martes    | No
2024-01-06  | 2024 | 1   | Q1        | Sábado    | Sí
```

**Cómo crear una tabla de calendario:**
- Opción 1: DAX - `CALENDAR()` o `CALENDARAUTO()`
- Opción 2: Power Query
- Opción 3: Importar desde SQL/Excel

## Implementación Práctica

### Ejercicio 1: Conectar a un archivo Excel

**Escenario**: Tienes un archivo Excel con ventas mensuales.

**Pasos simulados:**

1. **Obtener Datos** → Excel Workbook
2. **Seleccionar archivo** de tu computadora
3. **Seleccionar tabla/hoja** a importar
4. **Transformar datos** (opcional) o **Cargar** directamente

**Preguntas de reflexión:**
- ¿Qué datos tienes en Excel que podrías analizar?
- _______________________________________________
- ¿Están limpios o necesitan transformación?
- _______________________________________________

### Ejercicio 2: Transformaciones básicas en Power Query

**Escenario**: Tienes estos datos sucios:

```
Fecha       | Producto  | Ventas
01/15/2024  | laptop    | $1500.50
empty       | Mouse     | 25
01/16/2024  | LAPTOP    | $2,300
```

**Transformaciones necesarias:**
1. **Eliminar filas vacías** → Remove blank rows
2. **Corregir tipo de datos** → Fecha como Date, Ventas como Decimal
3. **Estandarizar texto** → Capitalize Each Word en Producto
4. **Limpiar columna Ventas** → Remove $ y ,

**Resultado esperado:**
```
Fecha       | Producto | Ventas
2024-01-15  | Laptop   | 1500.50
2024-01-16  | Mouse    | 25.00
2024-01-16  | Laptop   | 2300.00
```

### Ejercicio 3: Diseñar un modelo simple

**Escenario**: Tienes 3 tablas de una tienda:

**Tabla Ventas** (Hechos)
- VentaID
- FechaVenta
- ProductoID
- ClienteID
- Cantidad
- PrecioUnitario

**Tabla Productos** (Dimensión)
- ProductoID
- NombreProducto
- Categoría
- PrecioCosto

**Tabla Clientes** (Dimensión)
- ClienteID
- NombreCliente
- Ciudad
- País

**Tu tarea:**

**1. Identifica la tabla de hechos**: _______________

**2. Identifica las tablas de dimensiones**: 
- _______________
- _______________

**3. Define las relaciones:**
- Tabla1: ___________ relacionada con Tabla2: ___________ 
  - Campo: ___________ → Campo: ___________
  - Cardinalidad: 1:* / 1:1 / *:*

- Tabla1: ___________ relacionada con Tabla2: ___________ 
  - Campo: ___________ → Campo: ___________
  - Cardinalidad: 1:* / 1:1 / *:*

**4. ¿Qué esquema formaría?** Estrella / Copo de nieve

### Ejercicio 4: Caso práctico - Librería

**Tienes estos datos en archivos separados:**

**ventas.csv**
```
ID, Fecha, LibroID, Cantidad, Total
1, 2024-01-15, 101, 2, 45.00
2, 2024-01-15, 102, 1, 30.00
3, 2024-01-16, 101, 1, 22.50
```

**libros.xlsx**
```
LibroID, Título, Autor, Género, Precio
101, "Cien años", García Márquez, Ficción, 22.50
102, "El Alquimista", Paulo Coelho, Ficción, 30.00
103, "Sapiens", Yuval Harari, No Ficción, 35.00
```

**Diseña el modelo:**

**Transformaciones en Power Query:**
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

**Relaciones a crear:**
_______________________________________________
_______________________________________________

**Columnas calculadas que agregarías:**
_______________________________________________
_______________________________________________

## Mejores Prácticas

### 1. En Power Query

**✅ Hacer:**
- Eliminar columnas innecesarias temprano (mejora rendimiento)
- Usar nombres descriptivos para pasos y consultas
- Documentar transformaciones complejas
- Corregir tipos de datos apropiadamente
- Usar carpetas para organizar consultas

**❌ Evitar:**
- Demasiadas transformaciones complejas (afecta rendimiento)
- Mezclar datos y presentación
- Dejar pasos sin nombre claro

### 2. En Modelado

**✅ Hacer:**
- Usar esquema estrella cuando sea posible
- Crear tabla de calendario dedicada
- Relaciones 1:* siempre que puedas
- Nombres claros y consistentes
- Ocultar columnas técnicas que los usuarios no necesitan

**❌ Evitar:**
- Relaciones muchos a muchos sin razón clara
- Relaciones bidireccionales innecesarias
- Tablas sin relaciones (islas)
- Duplicar datos innecesariamente

### 3. Convenciones de nombres

**Tablas:**
- Hechos: `Ventas`, `Transacciones`, `Pedidos`
- Dimensiones: `Dim_Producto`, `Dim_Cliente` o simplemente `Producto`, `Cliente`
- Calendario: `Calendario`, `Dim_Fecha`, `Calendar`

**Columnas:**
- Descriptivas y en español consistente
- Evitar espacios (usar PascalCase o snake_case)
- Prefijos para claridad: `ID_`, `Nombre_`, `Fecha_`

### 4. Rendimiento

**Optimizaciones:**
- ✅ Importar solo las columnas necesarias
- ✅ Filtrar datos en Power Query (no en visualizaciones)
- ✅ Usar tipos de datos apropiados (integer vs decimal)
- ✅ Deshabilitar auto-date/time hierarchy si no lo necesitas
- ✅ Comprimir modelo eliminando columnas redundantes

## Conceptos Clave para Recordar

📊 **Fuentes de datos**: Power BI se conecta a 100+ fuentes (Excel, SQL, web, cloud)

🔄 **Import vs DirectQuery**: Import copia datos (rápido), DirectQuery consulta en tiempo real

🧹 **Power Query**: Herramienta visual para limpiar y transformar datos

⭐ **Esquema Estrella**: Modelo recomendado (hechos al centro, dimensiones alrededor)

🔗 **Relaciones 1:***: El tipo más común y eficiente de relación

📅 **Tabla Calendario**: Esencial para análisis de tiempo

🎯 **Tabla de Hechos**: Transacciones/métricas (muchas filas)

📋 **Tabla de Dimensión**: Contexto/atributos (menos filas)

## Próximos Pasos

En el **Módulo 3: Visualizaciones Efectivas**, aprenderás a:
- Tipos de visualizaciones y cuándo usar cada una
- Crear gráficos efectivos e interactivos
- Formatear visualizaciones profesionalmente
- Diseñar dashboards atractivos
- Contar historias con datos

**Recursos recomendados:**
- 📚 Documentación: "Power Query in Power BI"
- 🎥 Video: "Star Schema Basics" - SQLBI
- 📖 Artículo: "Best Practices for Data Modeling"
- 🛠️ Práctica: Datasets de ejemplo en Microsoft Learn

## Motivación Final

> "Datos sin estructura son solo ruido. Un buen modelo convierte ese ruido en música." - Anónimo

El modelado de datos puede parecer abstracto al principio, pero es **la habilidad más valiosa** que desarrollarás en Power BI. Un analista con excelentes visualizaciones pero mal modelado creará informes lentos y problemáticos. Un analista con buen modelado y visualizaciones básicas creará informes escalables y confiables.

**Invierte tiempo en aprender modelado** - Te ahorrará semanas de frustración más adelante.

La buena noticia: Con práctica, el modelado se vuelve intuitivo. Pronto estarás diseñando modelos estelares sin pensarlo dos veces.

---

**Tiempo estimado del módulo**: 4-5 horas  
**Dificultad**: Intermedio ⭐⭐☆☆☆  
**Prerrequisitos**: Módulo 1 completado, Power BI Desktop instalado (recomendado)

