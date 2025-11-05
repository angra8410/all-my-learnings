# 📊 Módulo 02 — SQL para Data Engineering

## 🎯 Objetivos de Aprendizaje

Al completar este módulo serás capaz de:

1. **Escribir consultas SQL avanzadas** utilizando CTEs, subconsultas y window functions
2. **Optimizar queries** para grandes volúmenes de datos con índices y query planning
3. **Realizar operaciones MERGE y UPSERT** para mantener datos actualizados
4. **Implementar técnicas de deduplicación** para garantizar calidad de datos
5. **Aplicar window functions** para cálculos complejos (ranking, moving averages, lag/lead)
6. **Diseñar y ejecutar JOINs complejos** entre múltiples tablas
7. **Utilizar agregaciones avanzadas** con GROUP BY, HAVING y ROLLUP
8. **Analizar planes de ejecución** para identificar cuellos de botella

## 📚 Contenido Teórico

### 1. SQL para Data Engineering vs SQL Tradicional

Como Data Engineer, usarás SQL de forma diferente a un analista:

| Aspecto | Analista de Datos | Data Engineer |
|---------|-------------------|---------------|
| **Volumen** | Cientos/miles de filas | Millones/billones de filas |
| **Enfoque** | Insights y reportes | Pipelines y transformaciones |
| **Performance** | Segundos aceptables | Optimización crítica |
| **Escritura vs Lectura** | Principalmente lectura | Escritura intensiva (ETL) |
| **Complejidad** | Queries ad-hoc | Queries reutilizables, versionados |

### 2. Common Table Expressions (CTEs)

Las CTEs hacen el código más legible y mantenible:

```sql
-- Sin CTE (difícil de leer)
SELECT 
    customer_id,
    (SELECT AVG(amount) FROM orders o2 WHERE o2.customer_id = o1.customer_id) as avg_order
FROM orders o1;

-- Con CTE (claro y estructurado)
WITH customer_averages AS (
    SELECT 
        customer_id,
        AVG(amount) as avg_order
    FROM orders
    GROUP BY customer_id
)
SELECT * FROM customer_averages;
```

**Ventajas:**
- ✅ Código más legible y mantenible
- ✅ Reutilización dentro de la misma query
- ✅ Facilita debugging (puedes ejecutar solo el CTE)
- ✅ Mejor para queries complejas con múltiples pasos

### 3. Window Functions

Permiten cálculos a través de conjuntos de filas relacionadas **sin colapsar** las filas:

```sql
SELECT 
    customer_id,
    order_date,
    amount,
    -- Ranking dentro de cada cliente
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) as order_sequence,
    -- Total acumulado
    SUM(amount) OVER (PARTITION BY customer_id ORDER BY order_date) as running_total,
    -- Media móvil 3 pedidos
    AVG(amount) OVER (
        PARTITION BY customer_id 
        ORDER BY order_date 
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) as moving_avg_3
FROM orders;
```

**Funciones window comunes:**
- `ROW_NUMBER()`: Número de fila único
- `RANK()`: Ranking con gaps para empates
- `DENSE_RANK()`: Ranking sin gaps
- `LAG()` / `LEAD()`: Valor de fila anterior/siguiente
- `FIRST_VALUE()` / `LAST_VALUE()`: Primer/último valor de la ventana

### 4. MERGE y UPSERT

Operaciones críticas en ETL para actualizar/insertar datos:

```sql
-- MERGE (estándar SQL)
MERGE INTO target_table t
USING source_table s
ON t.id = s.id
WHEN MATCHED THEN
    UPDATE SET 
        t.value = s.value,
        t.updated_at = CURRENT_TIMESTAMP
WHEN NOT MATCHED THEN
    INSERT (id, value, created_at)
    VALUES (s.id, s.value, CURRENT_TIMESTAMP);

-- UPSERT en PostgreSQL (ON CONFLICT)
INSERT INTO target_table (id, value)
VALUES (1, 'new_value')
ON CONFLICT (id) 
DO UPDATE SET 
    value = EXCLUDED.value,
    updated_at = CURRENT_TIMESTAMP;
```

**Casos de uso:**
- Actualizar dimensiones en un data warehouse
- Sincronizar datos de staging a producción
- Mantener tablas de configuración actualizadas

### 5. Deduplicación

Técnica esencial para limpieza de datos:

```sql
-- Método 1: Usando ROW_NUMBER() - Más eficiente
DELETE FROM table
WHERE id IN (
    SELECT id FROM (
        SELECT 
            id,
            ROW_NUMBER() OVER (
                PARTITION BY email, created_date 
                ORDER BY updated_at DESC
            ) as rn
        FROM table
    ) t
    WHERE rn > 1
);

-- Método 2: Usando DISTINCT ON (PostgreSQL)
INSERT INTO clean_table
SELECT DISTINCT ON (email, created_date) *
FROM dirty_table
ORDER BY email, created_date, updated_at DESC;
```

### 6. JOINs Avanzados

```sql
-- INNER JOIN: Solo registros coincidentes
SELECT o.*, c.name
FROM orders o
INNER JOIN customers c ON o.customer_id = c.id;

-- LEFT JOIN: Todos de izquierda + coincidencias de derecha
SELECT c.name, COALESCE(COUNT(o.id), 0) as order_count
FROM customers c
LEFT JOIN orders o ON c.id = o.customer_id
GROUP BY c.id, c.name;

-- FULL OUTER JOIN: Todos de ambas tablas
SELECT 
    COALESCE(c.id, o.customer_id) as customer_id,
    c.name,
    o.order_id
FROM customers c
FULL OUTER JOIN orders o ON c.id = o.customer_id;

-- CROSS JOIN: Producto cartesiano (útil para generar combinaciones)
SELECT 
    d.date,
    p.product_id
FROM date_dimension d
CROSS JOIN products p
WHERE d.date BETWEEN '2024-01-01' AND '2024-12-31';

-- SELF JOIN: Comparar filas dentro de la misma tabla
SELECT 
    e1.name as employee,
    e2.name as manager
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.id;
```

### 7. GROUP BY y Agregaciones Avanzadas

```sql
-- GROUP BY con múltiples dimensiones
SELECT 
    DATE_TRUNC('month', order_date) as month,
    category,
    COUNT(*) as order_count,
    SUM(amount) as total_revenue,
    AVG(amount) as avg_order_value
FROM orders
GROUP BY DATE_TRUNC('month', order_date), category;

-- HAVING: Filtrar después de agrupar
SELECT 
    customer_id,
    COUNT(*) as order_count
FROM orders
GROUP BY customer_id
HAVING COUNT(*) > 5;

-- ROLLUP: Subtotales y gran total
SELECT 
    COALESCE(region, 'TOTAL') as region,
    COALESCE(category, 'ALL') as category,
    SUM(sales) as total_sales
FROM sales_data
GROUP BY ROLLUP (region, category);
```

### 8. Optimización de Performance

#### Índices
```sql
-- Crear índice en columna única
CREATE INDEX idx_orders_customer_id ON orders(customer_id);

-- Índice compuesto (orden importa!)
CREATE INDEX idx_orders_date_status ON orders(order_date, status);

-- Índice parcial (solo para filas que cumplen condición)
CREATE INDEX idx_active_orders ON orders(order_date) 
WHERE status = 'active';
```

#### Query Planning
```sql
-- Ver plan de ejecución
EXPLAIN SELECT * FROM orders WHERE customer_id = 123;

-- Ver plan con costos y tiempos reales
EXPLAIN ANALYZE 
SELECT o.*, c.name
FROM orders o
JOIN customers c ON o.customer_id = c.id
WHERE o.order_date > '2024-01-01';
```

**Indicadores de problemas:**
- 🚨 **Seq Scan** en tablas grandes → Considera agregar índice
- 🚨 **Nested Loop** con tablas grandes → Verifica estadísticas
- 🚨 **Sort** costoso → Considera índice en columnas de ORDER BY
- 🚨 Estimaciones muy incorrectas → Ejecuta `ANALYZE` en las tablas

## 🏋️ Actividades Prácticas

Ver `actividad-interactiva.md` para ejercicios detallados que cubren:

1. Configuración de base de datos con datos de ejemplo
2. SELECT avanzado con CTEs
3. Window functions para análisis temporal
4. JOINs complejos entre múltiples tablas
5. GROUP BY y agregaciones
6. MERGE/UPSERT para actualización incremental
7. Deduplicación de registros duplicados
8. Optimización con índices y EXPLAIN
9. Queries de producción realistas
10. Mini-proyecto: Pipeline ETL completo

## 📝 Entregables

Al finalizar este módulo deberías tener:

1. ✅ Base de datos PostgreSQL con tablas de práctica pobladas
2. ✅ Scripts SQL documentados de todos los ejercicios
3. ✅ Al menos 3 queries optimizadas con índices
4. ✅ Un ejemplo completo de MERGE/UPSERT funcionando
5. ✅ Comprensión de cuándo usar cada tipo de JOIN
6. ✅ Capacidad de leer y entender planes de ejecución

## 🎯 Criterios de Éxito

- [ ] Puedes escribir CTEs anidados para queries complejas
- [ ] Dominas al menos 5 window functions diferentes
- [ ] Entiendes la diferencia entre INNER, LEFT, RIGHT y FULL OUTER JOIN
- [ ] Puedes implementar UPSERT para actualización incremental
- [ ] Sabes usar ROW_NUMBER() para deduplicación
- [ ] Comprendes cómo leer EXPLAIN y identificar problemas de performance
- [ ] Puedes escribir queries que procesen millones de filas eficientemente

## 📚 Recursos Adicionales

Ver archivo `recursos.md` para:
- Tutoriales SQL avanzado
- Guías de optimización específicas por motor (PostgreSQL, MySQL, etc.)
- Datasets de práctica con millones de filas
- Cheat sheets de window functions
- Documentación de funciones por motor de base de datos

## ⏭️ Siguiente Paso

Una vez completado este módulo, estarás listo para **Módulo 03: Python para Data Engineering**, donde aprenderás a automatizar estas queries SQL y construir pipelines de extracción y transformación de datos.

---

**💡 Consejo**: SQL es el lenguaje más importante para un Data Engineer. Dedica tiempo extra a este módulo si es necesario. Dominar SQL avanzado te diferenciará en entrevistas y proyectos reales.

**⏱️ Duración estimada**: 12-15 horas (teoría + prácticas + proyecto mini-ETL)