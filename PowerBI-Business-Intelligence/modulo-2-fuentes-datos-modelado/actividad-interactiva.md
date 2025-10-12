# Actividades Interactivas - Módulo 2: Fuentes de Datos y Modelado

## Sección 1: Preguntas de Opción Múltiple

### Pregunta 1
**¿Cuál es la diferencia principal entre Import y DirectQuery?**

A) Import es más lento que DirectQuery  
B) Import copia los datos a Power BI, DirectQuery consulta en tiempo real  
C) DirectQuery solo funciona con Excel  
D) No hay diferencia, son lo mismo

**Tu respuesta**: ___

---

### Pregunta 2
**¿Qué herramienta usas en Power BI para limpiar y transformar datos?**

A) DAX Editor  
B) Power Query Editor  
C) Power Pivot  
D) Data Cleaner

**Tu respuesta**: ___

---

### Pregunta 3
**En un esquema estrella, ¿qué tabla va en el centro?**

A) La tabla de dimensión más grande  
B) La tabla de calendario  
C) La tabla de hechos  
D) La tabla de clientes

**Tu respuesta**: ___

---

### Pregunta 4
**¿Qué tipo de relación es más común y recomendada en Power BI?**

A) Muchos a muchos (*:*)  
B) Uno a uno (1:1)  
C) Uno a muchos (1:*)  
D) No se necesitan relaciones

**Tu respuesta**: ___

---

### Pregunta 5
**¿Por qué es importante una tabla de calendario en Power BI?**

A) Solo es decorativa  
B) Permite análisis de tiempo consistentes y funciones de inteligencia temporal  
C) Power BI la requiere obligatoriamente  
D) Para hacer que el modelo se vea más profesional

**Tu respuesta**: ___

---

### Pregunta 6
**¿Qué contiene típicamente una tabla de hechos?**

A) Descripciones de productos  
B) Información de clientes  
C) Transacciones y métricas numéricas  
D) Solo fechas

**Tu respuesta**: ___

---

### Pregunta 7
**¿Cuál es una ventaja del método Import sobre DirectQuery?**

A) Datos siempre actualizados en tiempo real  
B) Mejor rendimiento y acceso a todas las características  
C) No requiere espacio de almacenamiento  
D) Más fácil de configurar

**Tu respuesta**: ___

---

## Sección 2: Verdadero o Falso

Marca V (Verdadero) o F (Falso) para cada afirmación:

1. **Power BI solo puede conectarse a archivos Excel.** ___

2. **Power Query registra automáticamente cada transformación que haces.** ___

3. **Las tablas de dimensiones típicamente tienen más filas que las tablas de hechos.** ___

4. **Debes crear una relación entre cada par de tablas en tu modelo.** ___

5. **El esquema copo de nieve es siempre mejor que el esquema estrella.** ___

6. **Puedes editar datos directamente en Power Query y guardar cambios en el archivo original.** ___

7. **DirectQuery requiere que los datos estén en Power BI.** ___

8. **Una buena práctica es eliminar columnas innecesarias temprano en Power Query.** ___

9. **Las relaciones bidireccionales (Both) deben usarse en todos los casos.** ___

10. **Power Query usa un lenguaje llamado M en el background.** ___

---

## Sección 3: Relaciona Conceptos

Conecta cada término con su definición correcta:

**Términos:**
1. Tabla de Hechos
2. Tabla de Dimensión
3. Power Query
4. Cardinalidad
5. Esquema Estrella
6. ETL
7. Import
8. Relación 1:*

**Definiciones:**
A) Herramienta para transformar y limpiar datos  
B) Copia datos a Power BI para mejor rendimiento  
C) Modelo con hechos al centro y dimensiones alrededor  
D) Contiene transacciones y métricas  
E) Tipo de relación uno a muchos  
F) Describe el contexto de los hechos  
G) Número de registros que se relacionan entre tablas  
H) Extract, Transform, Load

**Tus respuestas:**
1. ___ 2. ___ 3. ___ 4. ___ 5. ___ 6. ___ 7. ___ 8. ___

---

## Sección 4: Identifica el Tipo de Tabla

Para cada tabla, indica si es de **Hechos (H)** o **Dimensión (D)**:

1. **Tabla Ventas** (VentaID, Fecha, ProductoID, Cantidad, Total): ___

2. **Tabla Productos** (ProductoID, Nombre, Categoría, Precio): ___

3. **Tabla Pedidos** (PedidoID, FechaPedido, ClienteID, MontoTotal): ___

4. **Tabla Clientes** (ClienteID, Nombre, Ciudad, País): ___

5. **Tabla Calendario** (Fecha, Año, Mes, Trimestre, DíaSemana): ___

6. **Tabla Transacciones** (TransacciónID, Fecha, Monto, TipoTransacción): ___

7. **Tabla Empleados** (EmpleadoID, Nombre, Departamento, Puesto): ___

8. **Tabla InventarioMovimientos** (MovimientoID, Fecha, ProductoID, Cantidad, Tipo): ___

---

## Sección 5: Diseña Relaciones

**Escenario**: Tienes estas 4 tablas en tu modelo:

- **Ventas**: VentaID, FechaVenta, ProductoID, EmpleadoID, Cantidad
- **Productos**: ProductoID, NombreProducto, CategoríaID
- **Empleados**: EmpleadoID, NombreEmpleado, Departamento
- **Calendario**: Fecha, Año, Mes, Trimestre

### Ejercicio A: Define las relaciones

**Relación 1:**
- Tabla origen: _______________
- Campo: _______________
- Tabla destino: _______________
- Campo: _______________
- Cardinalidad: 1:* / 1:1 / *:*

**Relación 2:**
- Tabla origen: _______________
- Campo: _______________
- Tabla destino: _______________
- Campo: _______________
- Cardinalidad: 1:* / 1:1 / *:*

**Relación 3:**
- Tabla origen: _______________
- Campo: _______________
- Tabla destino: _______________
- Campo: _______________
- Cardinalidad: 1:* / 1:1 / *:*

### Ejercicio B: Dibuja el esquema

Dibuja (en papel o mentalmente) cómo se vería este modelo:

**¿Qué tipo de esquema forma?** Estrella / Copo de nieve / Otro

**¿Cuál es la tabla central?** _______________

---

## Sección 6: Transformaciones en Power Query

Para cada escenario, identifica qué transformación necesitas:

### Escenario 1
**Datos originales:**
```
Nombre Completo
Juan Pérez
María García
```

**Resultado deseado:**
```
Nombre | Apellido
Juan   | Pérez
María  | García
```

**Transformación necesaria**: _______________________________________________

---

### Escenario 2
**Datos originales:**
```
Ventas
$1,500.50
$2,300
empty
$450.25
```

**Resultado deseado:**
```
Ventas
1500.50
2300.00
450.25
```

**Transformaciones necesarias:**
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

---

### Escenario 3
**Datos originales:**
```
Fecha      | Producto | Ventas
01/15/2024 | LAPTOP   | 1500
01/15/2024 | laptop   | 2300
01/16/2024 | mouse    | 25
```

**Resultado deseado:**
```
Fecha      | Producto | Ventas
2024-01-15 | Laptop   | 3800
2024-01-16 | Mouse    | 25
```

**Transformaciones necesarias:**
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

---

## Sección 7: Caso Práctico - Restaurante

**Contexto**: Tienes un restaurante y estos archivos de datos:

**ordenes.csv**
```
OrdenID, Fecha, MesaID, MeseroID, Total
1, 2024-01-15, 5, 101, 85.50
2, 2024-01-15, 3, 102, 120.00
3, 2024-01-16, 5, 101, 95.25
```

**detalle_ordenes.csv**
```
DetalleID, OrdenID, PlatoID, Cantidad, Precio
1, 1, 201, 2, 35.00
2, 1, 202, 1, 50.50
3, 2, 203, 3, 120.00
```

**platos.xlsx**
```
PlatoID, NombrePlato, Categoría, PrecioCosto
201, Pasta Alfredo, Italiana, 12.00
202, Filete Mignon, Carnes, 25.00
203, Ensalada César, Ensaladas, 8.00
```

**meseros.xlsx**
```
MeseroID, Nombre, Turno
101, Carlos López, Tarde
102, Ana Martínez, Tarde
```

### Ejercicio A: Identifica tablas de hechos y dimensiones

**Tablas de Hechos:**
1. _______________________________________________
2. _______________________________________________

**Tablas de Dimensiones:**
1. _______________________________________________
2. _______________________________________________

**¿Falta alguna tabla importante?** Sí / No

**Si sí, ¿cuál?** _______________________________________________

---

### Ejercicio B: Diseña el modelo

**Relaciones necesarias:**

Relación 1: _______________ → _______________  
Relación 2: _______________ → _______________  
Relación 3: _______________ → _______________  
Relación 4: _______________ → _______________

**Tipo de esquema**: Estrella / Copo de nieve

---

### Ejercicio C: Transformaciones necesarias

**En la tabla ordenes:**
_______________________________________________
_______________________________________________

**En la tabla platos:**
_______________________________________________
_______________________________________________

**Columnas calculadas que agregarías:**
_______________________________________________
_______________________________________________

---

## Sección 8: Mejores Prácticas

Indica si cada práctica es **Buena (B)** o **Mala (M)**:

1. ___ Importar todas las columnas de una tabla grande, aunque solo uses 3
2. ___ Eliminar columnas innecesarias en Power Query
3. ___ Usar relaciones muchos a muchos para todo
4. ___ Crear una tabla de calendario dedicada
5. ___ Dejar todos los pasos de Power Query sin nombre
6. ___ Usar esquema estrella cuando sea posible
7. ___ Crear relaciones bidireccionales en todos los casos
8. ___ Corregir tipos de datos apropiadamente
9. ___ Duplicar datos en múltiples tablas
10. ___ Documentar transformaciones complejas

---

## Sección 9: Solución de Problemas

Para cada problema, identifica la causa probable y la solución:

### Problema 1
**Situación**: "Mi informe es muy lento al cargar"

**Posibles causas:**
- [ ] Demasiadas columnas importadas innecesarias
- [ ] Modelo mal optimizado
- [ ] Transformaciones complejas en visual en lugar de Power Query
- [ ] Todas las anteriores

**Solución recomendada:**
_______________________________________________
_______________________________________________

---

### Problema 2
**Situación**: "No puedo crear una relación entre dos tablas"

**Posibles causas:**
- [ ] Los campos no tienen el mismo tipo de datos
- [ ] Ya existe una relación indirecta
- [ ] Los valores no coinciden entre tablas
- [ ] La relación causaría ambigüedad

**¿Qué verificarías primero?**
_______________________________________________
_______________________________________________

---

### Problema 3
**Situación**: "Mis totales de ventas están duplicados"

**Causa probable:** _______________________________________________

**Solución:** _______________________________________________

---

## Sección 10: Tabla de Calendario

Diseña los campos que incluirías en una tabla de calendario:

**Campos básicos obligatorios:**
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

**Campos adicionales útiles:**
4. _______________________________________________
5. _______________________________________________
6. _______________________________________________
7. _______________________________________________

**¿Incluirías días festivos?** Sí / No

**Si sí, ¿cómo?** _______________________________________________

---

## Sección 11: Import vs DirectQuery

Completa la tabla comparativa:

| Característica | Import | DirectQuery |
|---------------|--------|-------------|
| Velocidad | _______ | _______ |
| Actualización de datos | _______ | _______ |
| Espacio de almacenamiento | _______ | _______ |
| Funcionalidades disponibles | _______ | _______ |
| Mejor para... | _______ | _______ |

---

## Sección 12: Escenarios de Decisión

Para cada escenario, decide: **Import (I)** o **DirectQuery (DQ)**

1. ___ Dashboard de ventas que se actualiza una vez al día
2. ___ Monitor en tiempo real de transacciones bancarias
3. ___ Análisis histórico de 5 años de datos
4. ___ Sistema de inventario que cambia constantemente
5. ___ Reporte mensual de RH que se genera una vez al mes
6. ___ Dashboard ejecutivo con datos de ayer
7. ___ Monitor de producción en tiempo real
8. ___ Análisis de tendencias de marketing con datos semanales

---

## Sección 13: Mini-Proyecto - Tienda Online

**Contexto**: Diseña el modelo de datos para una tienda online.

**Datos disponibles:**
- Pedidos de clientes
- Productos del catálogo
- Clientes registrados
- Envíos y tracking
- Reseñas de productos

### Paso 1: Define las tablas

**Tablas de Hechos necesarias:**
1. _______________________________________________
2. _______________________________________________

**Tablas de Dimensiones necesarias:**
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________
4. _______________________________________________

### Paso 2: Campos principales

**Para la tabla de hechos Pedidos, incluirías:**
- _______________________________________________
- _______________________________________________
- _______________________________________________
- _______________________________________________
- _______________________________________________

**Para la tabla de dimensión Productos, incluirías:**
- _______________________________________________
- _______________________________________________
- _______________________________________________
- _______________________________________________

### Paso 3: Relaciones

**Dibuja o describe cómo se relacionan:**
_______________________________________________
_______________________________________________
_______________________________________________

### Paso 4: Métricas clave

**¿Qué métricas calcularías?**
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________
4. _______________________________________________

---

## Sección 14: Reflexión y Aplicación

### ¿Qué transformaciones de Power Query usarías más frecuentemente en tu trabajo?

_______________________________________________
_______________________________________________
_______________________________________________

### ¿Qué fuentes de datos tienes disponibles en tu organización/proyecto?

_______________________________________________
_______________________________________________
_______________________________________________

### Diseña mentalmente un modelo para un caso real tuyo

**Descripción del proyecto:**
_______________________________________________
_______________________________________________

**Tablas principales:**
_______________________________________________
_______________________________________________

**Relaciones clave:**
_______________________________________________
_______________________________________________

---

**¡Excelente trabajo!** Revisa tus respuestas en `retroalimentacion.md` y registra tu progreso en `progreso.md`.

