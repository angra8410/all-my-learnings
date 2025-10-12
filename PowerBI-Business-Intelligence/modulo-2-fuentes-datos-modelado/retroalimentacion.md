# Retroalimentación y Soluciones - Módulo 2: Fuentes de Datos y Modelado

## Respuestas a Preguntas de Opción Múltiple

### Pregunta 1: ¿Cuál es la diferencia principal entre Import y DirectQuery?
**Respuesta correcta: B) Import copia los datos a Power BI, DirectQuery consulta en tiempo real**

**Explicación**: Import carga una copia de los datos en Power BI (más rápido pero requiere actualización), mientras que DirectQuery consulta los datos directamente en la fuente cada vez que se usa el informe (siempre actualizado pero más lento).

### Pregunta 2: ¿Qué herramienta usas en Power BI para limpiar y transformar datos?
**Respuesta correcta: B) Power Query Editor**

**Explicación**: Power Query Editor es la herramienta ETL de Power BI donde limpias, transformas y preparas tus datos antes de cargarlos al modelo.

### Pregunta 3: En un esquema estrella, ¿qué tabla va en el centro?
**Respuesta correcta: C) La tabla de hechos**

**Explicación**: En un esquema estrella, la tabla de hechos (transacciones/métricas) va en el centro, rodeada de tablas de dimensiones que proporcionan contexto.

### Pregunta 4: ¿Qué tipo de relación es más común y recomendada en Power BI?
**Respuesta correcta: C) Uno a muchos (1:*)**

**Explicación**: Las relaciones 1:* son las más eficientes y comunes. Un registro en la dimensión se relaciona con muchos en los hechos (ej: un producto aparece en muchas ventas).

### Pregunta 5: ¿Por qué es importante una tabla de calendario en Power BI?
**Respuesta correcta: B) Permite análisis de tiempo consistentes y funciones de inteligencia temporal**

**Explicación**: Una tabla de calendario te permite usar funciones de inteligencia de tiempo (YTD, MTD, etc.) y agregar atributos personalizados como trimestres, días festivos, etc.

### Pregunta 6: ¿Qué contiene típicamente una tabla de hechos?
**Respuesta correcta: C) Transacciones y métricas numéricas**

**Explicación**: Las tablas de hechos contienen eventos medibles: ventas, pedidos, transacciones, con cantidades, montos y claves foráneas a dimensiones.

### Pregunta 7: ¿Cuál es una ventaja del método Import sobre DirectQuery?
**Respuesta correcta: B) Mejor rendimiento y acceso a todas las características**

**Explicación**: Import es más rápido porque los datos están en memoria y permite usar todas las características de Power BI sin limitaciones.

---

## Respuestas a Verdadero o Falso

1. **Power BI solo puede conectarse a archivos Excel.**  
   **FALSO** - Power BI se conecta a 100+ fuentes: Excel, SQL, APIs, servicios cloud, web, y muchas más.

2. **Power Query registra automáticamente cada transformación que haces.**  
   **VERDADERO** - Cada paso se guarda en "Applied Steps" y puedes editarlos o eliminarlos después.

3. **Las tablas de dimensiones típicamente tienen más filas que las tablas de hechos.**  
   **FALSO** - Al contrario: las tablas de hechos tienen muchas transacciones, mientras que las dimensiones tienen relativamente pocos registros descriptivos.

4. **Debes crear una relación entre cada par de tablas en tu modelo.**  
   **FALSO** - Solo creas relaciones donde tenga sentido lógico. No todas las tablas necesitan estar conectadas entre sí.

5. **El esquema copo de nieve es siempre mejor que el esquema estrella.**  
   **FALSO** - En Power BI, el esquema estrella es generalmente preferido por su simplicidad y mejor rendimiento.

6. **Puedes editar datos directamente en Power Query y guardar cambios en el archivo original.**  
   **FALSO** - Power Query transforma datos pero NO modifica los archivos originales. Los cambios solo afectan lo que se carga en Power BI.

7. **DirectQuery requiere que los datos estén en Power BI.**  
   **FALSO** - DirectQuery NO copia datos a Power BI; consulta la fuente original cada vez.

8. **Una buena práctica es eliminar columnas innecesarias temprano en Power Query.**  
   **VERDADERO** - Eliminar columnas innecesarias al principio mejora el rendimiento y reduce el tamaño del modelo.

9. **Las relaciones bidireccionales (Both) deben usarse en todos los casos.**  
   **FALSO** - Las relaciones bidireccionales pueden causar ambigüedad y problemas de rendimiento. Úsalas solo cuando sea absolutamente necesario.

10. **Power Query usa un lenguaje llamado M en el background.**  
    **VERDADERO** - Aunque usas la interfaz visual, Power Query genera código en lenguaje M automáticamente.

---

## Respuestas a Relaciona Conceptos

1. Tabla de Hechos → **D** (Contiene transacciones y métricas)
2. Tabla de Dimensión → **F** (Describe el contexto de los hechos)
3. Power Query → **A** (Herramienta para transformar y limpiar datos)
4. Cardinalidad → **G** (Número de registros que se relacionan entre tablas)
5. Esquema Estrella → **C** (Modelo con hechos al centro y dimensiones alrededor)
6. ETL → **H** (Extract, Transform, Load)
7. Import → **B** (Copia datos a Power BI para mejor rendimiento)
8. Relación 1:* → **E** (Tipo de relación uno a muchos)

---

## Soluciones - Identifica el Tipo de Tabla

1. Tabla Ventas → **H** (Hechos) - Transacciones individuales
2. Tabla Productos → **D** (Dimensión) - Describe los productos
3. Tabla Pedidos → **H** (Hechos) - Transacciones de pedidos
4. Tabla Clientes → **D** (Dimensión) - Describe los clientes
5. Tabla Calendario → **D** (Dimensión) - Describe las fechas
6. Tabla Transacciones → **H** (Hechos) - Eventos transaccionales
7. Tabla Empleados → **D** (Dimensión) - Describe empleados
8. Tabla InventarioMovimientos → **H** (Hechos) - Eventos de movimiento

---

## Soluciones - Diseña Relaciones

**Relación 1:**
- Tabla origen: **Productos**
- Campo: **ProductoID**
- Tabla destino: **Ventas**
- Campo: **ProductoID**
- Cardinalidad: **1:***

**Relación 2:**
- Tabla origen: **Empleados**
- Campo: **EmpleadoID**
- Tabla destino: **Ventas**
- Campo: **EmpleadoID**
- Cardinalidad: **1:***

**Relación 3:**
- Tabla origen: **Calendario**
- Campo: **Fecha**
- Tabla destino: **Ventas**
- Campo: **FechaVenta**
- Cardinalidad: **1:***

**Tipo de esquema**: **Estrella** (Ventas al centro, tres dimensiones alrededor)

---

## Soluciones - Transformaciones en Power Query

### Escenario 1: Dividir nombre completo
**Transformación necesaria**: "Split Column" → By Delimiter → Space

### Escenario 2: Limpiar ventas
**Transformaciones necesarias:**
1. Remove Rows → Remove Blank Rows
2. Replace Values → $ → (vacío)
3. Replace Values → , → (vacío)
4. Change Type → Decimal Number

### Escenario 3: Normalizar y agrupar
**Transformaciones necesarias:**
1. Capitalize Each Word (en columna Producto)
2. Change Type (Fecha a Date)
3. Group By (Fecha y Producto) → Sum de Ventas

---

## Solución - Caso Práctico Restaurante

### Ejercicio A: Tablas de hechos y dimensiones

**Tablas de Hechos:**
1. ordenes (transacciones de órdenes)
2. detalle_ordenes (líneas de orden)

**Tablas de Dimensiones:**
1. platos
2. meseros

**¿Falta alguna tabla?** Sí - **Tabla Calendario** (esencial para análisis temporal)

### Ejercicio B: Relaciones necesarias

- Relación 1: **Calendario** → **ordenes** (Fecha)
- Relación 2: **meseros** → **ordenes** (MeseroID)
- Relación 3: **ordenes** → **detalle_ordenes** (OrdenID)
- Relación 4: **platos** → **detalle_ordenes** (PlatoID)

**Tipo de esquema**: **Estrella** con dos niveles (ordenes y detalle_ordenes como hechos)

### Ejercicio C: Transformaciones

**En ordenes:**
- Asegurar tipo de datos correcto (Fecha como Date, Total como Decimal)
- Verificar que no haya filas vacías

**En platos:**
- Asegurar Categoría esté capitalizada consistentemente
- Verificar tipos de datos

**Columnas calculadas:**
- En detalle_ordenes: Margen = Precio - PrecioCosto
- En ordenes: DíaSemana (de la fecha)

---

## Soluciones - Mejores Prácticas

1. **M** - Importar solo lo necesario
2. **B** - Mejora rendimiento
3. **M** - Evita cuando sea posible
4. **B** - Esencial para análisis temporal
5. **M** - Dificulta mantenimiento
6. **B** - Mejor rendimiento
7. **M** - Solo cuando sea necesario
8. **B** - Previene errores
9. **M** - Aumenta tamaño y errores
10. **B** - Facilita mantenimiento

---

## Soluciones - Problemas

### Problema 1: Informe lento
**Todas las anteriores** ✓
**Solución**: Eliminar columnas innecesarias en Power Query, optimizar modelo (relaciones correctas, tipos de datos apropiados), mover filtros de visuales a Power Query.

### Problema 2: No puedo crear relación
**Verificar primero**: Que ambos campos tengan el mismo tipo de datos (ej: ambos números o ambos texto).

### Problema 3: Totales duplicados
**Causa probable**: Relación muchos a muchos o relación bidireccional causando propagación incorrecta de filtros.
**Solución**: Revisar y corregir las relaciones del modelo.

---

## Solución - Tabla de Calendario

**Campos básicos:**
1. Fecha (única para cada día)
2. Año
3. Mes (número y nombre)

**Campos adicionales:**
4. Trimestre
5. DíaSemana
6. NúmeroDeSemana
7. EsFinDeSemana (Sí/No)

**Días festivos**: Sí, con columna booleana "EsDíaFestivo" o tabla separada relacionada.

---

## Solución - Import vs DirectQuery

| Característica | Import | DirectQuery |
|---------------|--------|-------------|
| Velocidad | Rápido | Más lento |
| Actualización | Programada | Tiempo real |
| Almacenamiento | Requiere espacio | No requiere |
| Funcionalidades | Todas | Algunas limitadas |
| Mejor para... | Reportes históricos | Datos en vivo |

---

## Solución - Escenarios de Decisión

1. **I** - Actualización diaria suficiente
2. **DQ** - Necesita tiempo real
3. **I** - Datos históricos, mejor rendimiento
4. **DQ** - Cambios constantes
5. **I** - Generación mensual
6. **I** - Datos de ayer, no necesita tiempo real
7. **DQ** - Monitor en vivo
8. **I** - Datos semanales

---

## Evaluación de Desempeño

### Si acertaste 90% o más: 🌟 ¡Excelente!
Dominas los conceptos de modelado de datos. Estás listo para crear modelos profesionales.

**Próximos pasos:**
- Practica con datasets reales
- Experimenta con Power Query
- Diseña tu primer modelo completo

### Si acertaste 70-89%: 💪 ¡Muy bien!
Comprendes los fundamentos. Algunos conceptos necesitan práctica.

**Recomendaciones:**
- Repasa relaciones y cardinalidad
- Practica más con Power Query
- Revisa esquemas estrella vs copo de nieve

### Si acertaste menos de 70%: 📚 Continúa aprendiendo
El modelado es complejo. Es normal necesitar más tiempo.

**Recomendaciones:**
- Revisa el README con ejemplos
- Dibuja modelos en papel
- Comienza con modelos simples
- Busca tutoriales en video

---

## Preparación para el Siguiente Módulo

**Antes del Módulo 3, asegúrate de:**

✅ Entender diferencia entre hechos y dimensiones  
✅ Saber crear relaciones básicas  
✅ Conocer Power Query y sus transformaciones  
✅ Comprender Import vs DirectQuery  
✅ Poder diseñar un esquema estrella simple

**En el Módulo 3 aprenderás:**
- Tipos de visualizaciones y cuándo usarlas
- Crear gráficos efectivos
- Diseñar dashboards profesionales
- Principios de storytelling visual

---

**¡Felicitaciones!** El modelado es la base de todo. Has dado un paso gigante. 🎉

