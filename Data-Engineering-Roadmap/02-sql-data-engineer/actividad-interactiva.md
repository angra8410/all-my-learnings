# 🎯 Actividad Interactiva — Módulo 02: SQL para Data Engineering

## Objetivo General
Dominar SQL avanzado para Data Engineering a través de ejercicios prácticos que cubren desde consultas complejas hasta optimización de performance, utilizando un dataset realista de e-commerce.

---

## 📋 Ejercicio 1: Configuración de la Base de Datos de Práctica (Duración: 25 minutos)

### Objetivo
Crear una base de datos con esquema realista de e-commerce y poblarla con datos de ejemplo para los ejercicios.

### Pasos

1. **Conectarse a PostgreSQL**
```bash
docker exec -it postgres-local psql -U dataeng -d learning_db
```

2. **Crear esquema de tablas**
```sql
-- Tabla de clientes
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    name VARCHAR(100),
    country VARCHAR(50),
    signup_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla de productos
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(200),
    category VARCHAR(50),
    price DECIMAL(10, 2),
    stock_quantity INT
);

-- Tabla de pedidos
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT REFERENCES customers(customer_id),
    order_date TIMESTAMP,
    status VARCHAR(20),
    total_amount DECIMAL(10, 2)
);

-- Tabla de items de pedido
CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(order_id),
    product_id INT REFERENCES products(product_id),
    quantity INT,
    unit_price DECIMAL(10, 2)
);

-- Tabla de logs de eventos (para análisis temporal)
CREATE TABLE events_log (
    event_id SERIAL PRIMARY KEY,
    customer_id INT,
    event_type VARCHAR(50),
    event_timestamp TIMESTAMP,
    metadata JSONB
);
```

**Tu confirmación:**
```
Tablas creadas: ___ (número)
Comando de verificación usado: _______________
```

3. **Poblar con datos de ejemplo**
```sql
-- Insertar clientes
INSERT INTO customers (email, name, country, signup_date) VALUES
('maria@email.com', 'María García', 'España', '2023-01-15'),
('john@email.com', 'John Smith', 'USA', '2023-02-20'),
('ana@email.com', 'Ana López', 'México', '2023-03-10'),
('peter@email.com', 'Peter Brown', 'UK', '2023-04-05'),
('carlos@email.com', 'Carlos Ruiz', 'Argentina', '2023-05-12'),
('lisa@email.com', 'Lisa Wong', 'Canada', '2023-06-18'),
('ahmed@email.com', 'Ahmed Ali', 'Egypt', '2023-07-22'),
('sofia@email.com', 'Sofia Costa', 'Brasil', '2023-08-30'),
('yuki@email.com', 'Yuki Tanaka', 'Japan', '2023-09-14'),
('emma@email.com', 'Emma Miller', 'Australia', '2023-10-20');

-- Insertar productos
INSERT INTO products (product_name, category, price, stock_quantity) VALUES
('Laptop Dell XPS', 'Electronics', 1200.00, 15),
('iPhone 15', 'Electronics', 999.00, 30),
('Silla Gamer', 'Furniture', 299.00, 20),
('Mesa Escritorio', 'Furniture', 199.00, 12),
('Teclado Mecánico', 'Accessories', 89.00, 50),
('Mouse Inalámbrico', 'Accessories', 29.00, 100),
('Monitor 27"', 'Electronics', 349.00, 18),
('Auriculares Bluetooth', 'Accessories', 79.00, 45),
('Webcam HD', 'Electronics', 59.00, 35),
('Lámpara LED', 'Furniture', 39.00, 60);

-- Insertar pedidos y order_items
INSERT INTO orders (customer_id, order_date, status, total_amount) VALUES
(1, '2024-01-10 10:30:00', 'completed', 1488.00),
(2, '2024-01-12 14:15:00', 'completed', 999.00),
(1, '2024-01-15 09:20:00', 'completed', 328.00),
(3, '2024-01-18 11:45:00', 'pending', 199.00),
(4, '2024-01-20 16:30:00', 'completed', 467.00),
(2, '2024-01-25 13:10:00', 'completed', 138.00),
(5, '2024-02-01 10:00:00', 'shipped', 1200.00),
(1, '2024-02-05 15:30:00', 'completed', 89.00),
(6, '2024-02-10 12:20:00', 'completed', 378.00),
(3, '2024-02-14 14:45:00', 'cancelled', 299.00);

INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
(1, 1, 1, 1200.00), (1, 5, 1, 89.00), (1, 6, 1, 29.00), (1, 10, 1, 39.00), (1, 8, 1, 79.00), (1, 9, 1, 59.00),
(2, 2, 1, 999.00),
(3, 3, 1, 299.00), (3, 6, 1, 29.00),
(4, 4, 1, 199.00),
(5, 7, 1, 349.00), (5, 8, 1, 79.00), (5, 6, 1, 29.00), (5, 10, 1, 10.00),
(6, 5, 1, 89.00), (6, 9, 1, 59.00),
(7, 1, 1, 1200.00),
(8, 5, 1, 89.00),
(9, 7, 1, 349.00), (9, 6, 1, 29.00),
(10, 3, 1, 299.00);

-- Insertar eventos
INSERT INTO events_log (customer_id, event_type, event_timestamp, metadata) VALUES
(1, 'page_view', '2024-01-10 10:25:00', '{"page": "laptop-dell"}'),
(1, 'add_to_cart', '2024-01-10 10:28:00', '{"product_id": 1}'),
(1, 'checkout', '2024-01-10 10:30:00', '{"order_id": 1}'),
(2, 'page_view', '2024-01-12 14:10:00', '{"page": "iphone-15"}'),
(2, 'add_to_cart', '2024-01-12 14:14:00', '{"product_id": 2}'),
(2, 'checkout', '2024-01-12 14:15:00', '{"order_id": 2}');
```

4. **Verificar datos insertados**
```sql
SELECT 'customers' as tabla, COUNT(*) as registros FROM customers
UNION ALL
SELECT 'products', COUNT(*) FROM products
UNION ALL
SELECT 'orders', COUNT(*) FROM orders
UNION ALL
SELECT 'order_items', COUNT(*) FROM order_items
UNION ALL
SELECT 'events_log', COUNT(*) FROM events_log;
```

**Tu resultado:**
```
 tabla        | registros 
--------------|----------
 customers    | ______
 products     | ______
 orders       | ______
 order_items  | ______
 events_log   | ______
```

### Verificación
- ✅ 5 tablas creadas correctamente
- ✅ Todas las tablas tienen datos
- ✅ Foreign keys funcionando (intentar insertar orden con customer_id inválido debería fallar)

**Duración:** 25 minutos

---

## 📋 Ejercicio 2: CTEs (Common Table Expressions) y Subconsultas (Duración: 20 minutos)

### Objetivo
Dominar el uso de CTEs para escribir queries complejas de forma legible y mantenible.

### Pasos

1. **Escribir query SIN CTE (menos legible)**
```sql
SELECT 
    c.name,
    (SELECT COUNT(*) FROM orders o WHERE o.customer_id = c.customer_id) as total_orders,
    (SELECT SUM(total_amount) FROM orders o WHERE o.customer_id = c.customer_id) as total_spent
FROM customers c
WHERE (SELECT COUNT(*) FROM orders o WHERE o.customer_id = c.customer_id) > 1;
```

**Resultado:**
```
 name          | total_orders | total_spent
---------------|--------------|------------
_______________________________________________
_______________________________________________
```

2. **Reescribir usando CTEs (más legible)**
```sql
WITH customer_stats AS (
    SELECT 
        customer_id,
        COUNT(*) as total_orders,
        SUM(total_amount) as total_spent,
        AVG(total_amount) as avg_order_value
    FROM orders
    GROUP BY customer_id
)
SELECT 
    c.name,
    c.email,
    cs.total_orders,
    cs.total_spent,
    ROUND(cs.avg_order_value, 2) as avg_order_value
FROM customers c
INNER JOIN customer_stats cs ON c.customer_id = cs.customer_id
WHERE cs.total_orders > 1
ORDER BY cs.total_spent DESC;
```

**Resultado:**
```
 name          | email              | total_orders | total_spent | avg_order_value
---------------|--------------------|--------------| ------------|----------------
_______________________________________________
_______________________________________________
_______________________________________________
```

3. **CTEs anidados (múltiples CTEs)**
```sql
WITH monthly_sales AS (
    SELECT 
        DATE_TRUNC('month', order_date) as month,
        SUM(total_amount) as revenue
    FROM orders
    WHERE status = 'completed'
    GROUP BY DATE_TRUNC('month', order_date)
),
sales_with_growth AS (
    SELECT 
        month,
        revenue,
        LAG(revenue) OVER (ORDER BY month) as prev_month_revenue,
        revenue - LAG(revenue) OVER (ORDER BY month) as revenue_change
    FROM monthly_sales
)
SELECT 
    TO_CHAR(month, 'YYYY-MM') as month,
    ROUND(revenue, 2) as revenue,
    ROUND(prev_month_revenue, 2) as prev_month,
    ROUND(revenue_change, 2) as change,
    ROUND((revenue_change / NULLIF(prev_month_revenue, 0)) * 100, 2) as growth_pct
FROM sales_with_growth
ORDER BY month;
```

**Tu resultado:**
```
 month   | revenue  | prev_month | change   | growth_pct
---------|----------|------------|----------|------------
_______________________________________________
_______________________________________________
_______________________________________________
```

### Verificación
- ✅ Ambas queries (con y sin CTE) devuelven resultados equivalentes
- ✅ Puedes explicar por qué los CTEs son más mantenibles
- ✅ Los CTEs anidados ejecutan sin error

**Duración:** 20 minutos

---

## 📋 Ejercicio 3: Window Functions - Ranking y Análisis Temporal (Duración: 30 minutos)

### Objetivo
Aplicar window functions para análisis avanzado sin colapsar filas.

### Pasos

1. **ROW_NUMBER, RANK, DENSE_RANK**
```sql
SELECT 
    order_id,
    customer_id,
    order_date,
    total_amount,
    ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date) as order_sequence,
    RANK() OVER (ORDER BY total_amount DESC) as amount_rank,
    DENSE_RANK() OVER (ORDER BY total_amount DESC) as dense_rank
FROM orders
ORDER BY customer_id, order_date;
```

**Primeras 5 filas de tu resultado:**
```
 order_id | customer_id | order_date          | total_amount | order_sequence | amount_rank | dense_rank
----------|-------------|---------------------|--------------|----------------|-------------|------------
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________
```

**Pregunta:** ¿Cuál es la diferencia entre RANK y DENSE_RANK?
```
_______________________________________________
_______________________________________________
```

2. **LAG y LEAD - Comparar con pedidos anteriores/siguientes**
```sql
SELECT 
    customer_id,
    order_date,
    total_amount,
    LAG(total_amount) OVER (PARTITION BY customer_id ORDER BY order_date) as prev_order_amount,
    total_amount - LAG(total_amount) OVER (PARTITION BY customer_id ORDER BY order_date) as amount_diff,
    LEAD(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) as next_order_date,
    LEAD(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) - order_date as days_to_next_order
FROM orders
WHERE customer_id IN (1, 2)
ORDER BY customer_id, order_date;
```

**Tu resultado:**
```
 customer_id | order_date          | total_amount | prev_order_amount | amount_diff | next_order_date     | days_to_next_order
-------------|---------------------|--------------|-------------------|-------------|---------------------|--------------------
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________
```

3. **Running totals y Moving averages**
```sql
SELECT 
    order_date::DATE as date,
    total_amount,
    -- Running total (acumulado)
    SUM(total_amount) OVER (ORDER BY order_date) as running_total,
    -- Media móvil 3 pedidos
    ROUND(
        AVG(total_amount) OVER (
            ORDER BY order_date 
            ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
        ), 
        2
    ) as moving_avg_3,
    -- Count acumulado
    COUNT(*) OVER (ORDER BY order_date) as cumulative_orders
FROM orders
WHERE status = 'completed'
ORDER BY order_date;
```

**Tu resultado (primeras 6 filas):**
```
 date       | total_amount | running_total | moving_avg_3 | cumulative_orders
------------|--------------|---------------|--------------|-------------------
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________
```

4. **FIRST_VALUE y LAST_VALUE - Comparar con primero/último**
```sql
SELECT 
    customer_id,
    order_date,
    total_amount,
    FIRST_VALUE(total_amount) OVER (
        PARTITION BY customer_id 
        ORDER BY order_date
    ) as first_order_amount,
    LAST_VALUE(total_amount) OVER (
        PARTITION BY customer_id 
        ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) as last_order_amount
FROM orders
ORDER BY customer_id, order_date;
```

**¿Por qué es importante usar "ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING" con LAST_VALUE?**
```
_______________________________________________
_______________________________________________
```

### Verificación
- ✅ Comprendes la diferencia entre RANK y DENSE_RANK
- ✅ Puedes calcular running totals
- ✅ Entiendes cómo funciona la cláusula ROWS BETWEEN

**Duración:** 30 minutos

---

## 📋 Ejercicio 4: JOINs Complejos - Múltiples Tablas (Duración: 25 minutos)

### Objetivo
Dominar diferentes tipos de JOINs y su aplicación en análisis de datos.

### Pasos

1. **INNER JOIN - Solo coincidencias**
```sql
SELECT 
    c.name as customer_name,
    o.order_id,
    o.order_date,
    p.product_name,
    oi.quantity,
    oi.unit_price,
    (oi.quantity * oi.unit_price) as line_total
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON oi.product_id = p.product_id
WHERE o.status = 'completed'
ORDER BY c.name, o.order_date;
```

**Número de filas devueltas:** _______

**Primeras 3 filas:**
```
 customer_name | order_id | order_date          | product_name      | quantity | unit_price | line_total
---------------|----------|---------------------|-------------------|----------|------------|------------
_______________________________________________
_______________________________________________
_______________________________________________
```

2. **LEFT JOIN - Encontrar clientes sin pedidos**
```sql
SELECT 
    c.customer_id,
    c.name,
    c.email,
    COUNT(o.order_id) as order_count,
    COALESCE(SUM(o.total_amount), 0) as total_spent
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id AND o.status = 'completed'
GROUP BY c.customer_id, c.name, c.email
ORDER BY order_count ASC, c.name;
```

**Clientes con 0 pedidos:**
```
 customer_id | name  | email | order_count | total_spent
-------------|-------|-------|-------------|------------
_______________________________________________
_______________________________________________
```

3. **SELF JOIN - Encontrar pedidos del mismo cliente en mismo día**
```sql
SELECT DISTINCT
    o1.order_id as order1_id,
    o2.order_id as order2_id,
    o1.customer_id,
    o1.order_date::DATE as order_date
FROM orders o1
INNER JOIN orders o2 ON 
    o1.customer_id = o2.customer_id 
    AND o1.order_date::DATE = o2.order_date::DATE
    AND o1.order_id < o2.order_id
ORDER BY o1.order_date;
```

**¿Hay clientes con múltiples pedidos en el mismo día? (Sí/No):** _______

4. **FULL OUTER JOIN - Identificar orphans**
```sql
-- Crear tabla temporal con productos "huérfanos" (sin ventas)
WITH products_sold AS (
    SELECT DISTINCT product_id
    FROM order_items
)
SELECT 
    p.product_id,
    p.product_name,
    p.category,
    CASE 
        WHEN ps.product_id IS NULL THEN 'No vendido'
        ELSE 'Vendido'
    END as status
FROM products p
FULL OUTER JOIN products_sold ps ON p.product_id = ps.product_id
ORDER BY status, p.product_id;
```

**Productos NO vendidos:**
```
 product_id | product_name | category | status
------------|--------------|----------|--------
_______________________________________________
_______________________________________________
```

### Verificación
- ✅ INNER JOIN solo muestra coincidencias
- ✅ LEFT JOIN preserva todos los registros de la tabla izquierda
- ✅ Puedes usar SELF JOIN para comparar filas de la misma tabla
- ✅ FULL OUTER JOIN identifica registros sin match en ambas tablas

**Duración:** 25 minutos

---

## 📋 Ejercicio 5: GROUP BY Avanzado y Agregaciones (Duración: 25 minutos)

### Objetivo
Dominar agregaciones complejas con GROUP BY, HAVING, y funciones de agregación.

### Pasos

1. **GROUP BY básico con múltiples agregaciones**
```sql
SELECT 
    p.category,
    COUNT(DISTINCT oi.order_id) as orders_with_category,
    SUM(oi.quantity) as total_units_sold,
    ROUND(SUM(oi.quantity * oi.unit_price), 2) as total_revenue,
    ROUND(AVG(oi.unit_price), 2) as avg_unit_price,
    ROUND(MIN(oi.unit_price), 2) as min_price,
    ROUND(MAX(oi.unit_price), 2) as max_price
FROM products p
INNER JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.category
ORDER BY total_revenue DESC;
```

**Tu resultado:**
```
 category    | orders_with_category | total_units_sold | total_revenue | avg_unit_price | min_price | max_price
-------------|----------------------|------------------|---------------|----------------|-----------|------------
_______________________________________________
_______________________________________________
_______________________________________________
```

2. **HAVING - Filtrar después de agrupar**
```sql
SELECT 
    c.customer_id,
    c.name,
    COUNT(o.order_id) as order_count,
    ROUND(SUM(o.total_amount), 2) as total_spent,
    ROUND(AVG(o.total_amount), 2) as avg_order_value
FROM customers c
INNER JOIN orders o ON c.customer_id = o.customer_id
WHERE o.status = 'completed'
GROUP BY c.customer_id, c.name
HAVING COUNT(o.order_id) >= 2 AND SUM(o.total_amount) > 500
ORDER BY total_spent DESC;
```

**Pregunta:** ¿Cuál es la diferencia entre WHERE y HAVING?
```
_______________________________________________
_______________________________________________
```

**Clientes que califican:**
```
 customer_id | name | order_count | total_spent | avg_order_value
-------------|------|-------------|-------------|----------------
_______________________________________________
_______________________________________________
```

3. **GROUP BY con expresiones y DATE_TRUNC**
```sql
SELECT 
    DATE_TRUNC('week', order_date) as week_start,
    COUNT(*) as orders_count,
    COUNT(DISTINCT customer_id) as unique_customers,
    ROUND(SUM(total_amount), 2) as weekly_revenue,
    ROUND(SUM(total_amount) / COUNT(*), 2) as avg_order_value
FROM orders
WHERE status IN ('completed', 'shipped')
GROUP BY DATE_TRUNC('week', order_date)
ORDER BY week_start;
```

**Tu resultado:**
```
 week_start          | orders_count | unique_customers | weekly_revenue | avg_order_value
---------------------|--------------|------------------|----------------|------------------
_______________________________________________
_______________________________________________
_______________________________________________
```

4. **ROLLUP - Subtotales y gran total**
```sql
SELECT 
    COALESCE(p.category, 'TOTAL') as category,
    COALESCE(p.product_name, 'Subtotal') as product,
    SUM(oi.quantity) as units_sold,
    ROUND(SUM(oi.quantity * oi.unit_price), 2) as revenue
FROM products p
INNER JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY ROLLUP (p.category, p.product_name)
ORDER BY p.category NULLS LAST, p.product_name NULLS LAST;
```

**Observa los subtotales por categoría y el gran total:**
```
 category    | product            | units_sold | revenue
-------------|--------------------|-----------|---------
_______________________________________________
_______________________________________________
_______________________________________________
... (incluye subtotales y TOTAL)
_______________________________________________
```

### Verificación
- ✅ WHERE filtra ANTES de agrupar, HAVING filtra DESPUÉS
- ✅ Puedes usar expresiones en GROUP BY (ej: DATE_TRUNC)
- ✅ ROLLUP genera subtotales jerárquicos

**Duración:** 25 minutos

---

## 📋 Ejercicio 6: MERGE/UPSERT - Actualizaciones Incrementales (Duración: 30 minutos)

### Objetivo
Implementar operaciones UPSERT (INSERT o UPDATE) típicas en pipelines ETL.

### Pasos

1. **Crear tabla staging y target**
```sql
-- Tabla target (destino final)
CREATE TABLE customer_summary (
    customer_id INT PRIMARY KEY,
    total_orders INT,
    total_spent DECIMAL(10, 2),
    last_order_date TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla staging (datos nuevos/actualizados)
CREATE TABLE customer_summary_staging (
    customer_id INT,
    total_orders INT,
    total_spent DECIMAL(10, 2),
    last_order_date TIMESTAMP
);
```

2. **Poblar staging con datos calculados**
```sql
INSERT INTO customer_summary_staging (customer_id, total_orders, total_spent, last_order_date)
SELECT 
    customer_id,
    COUNT(*) as total_orders,
    SUM(total_amount) as total_spent,
    MAX(order_date) as last_order_date
FROM orders
WHERE status = 'completed'
GROUP BY customer_id;
```

**Verificar datos en staging:**
```sql
SELECT * FROM customer_summary_staging ORDER BY customer_id;
```

**Número de registros en staging:** _______

3. **Implementar UPSERT con INSERT ... ON CONFLICT (PostgreSQL)**
```sql
INSERT INTO customer_summary (customer_id, total_orders, total_spent, last_order_date, updated_at)
SELECT 
    customer_id,
    total_orders,
    total_spent,
    last_order_date,
    CURRENT_TIMESTAMP
FROM customer_summary_staging
ON CONFLICT (customer_id) 
DO UPDATE SET
    total_orders = EXCLUDED.total_orders,
    total_spent = EXCLUDED.total_spent,
    last_order_date = EXCLUDED.last_order_date,
    updated_at = CURRENT_TIMESTAMP;
```

**Verificar resultado:**
```sql
SELECT * FROM customer_summary ORDER BY total_spent DESC;
```

**Tu resultado:**
```
 customer_id | total_orders | total_spent | last_order_date     | updated_at
-------------|--------------|-------------|---------------------|------------
_______________________________________________
_______________________________________________
_______________________________________________
```

4. **Agregar nuevos datos y re-ejecutar UPSERT**
```sql
-- Simular un nuevo pedido para customer_id = 1
INSERT INTO orders (customer_id, order_date, status, total_amount)
VALUES (1, CURRENT_TIMESTAMP, 'completed', 450.00);

-- Recalcular staging
TRUNCATE customer_summary_staging;
INSERT INTO customer_summary_staging (customer_id, total_orders, total_spent, last_order_date)
SELECT 
    customer_id,
    COUNT(*) as total_orders,
    SUM(total_amount) as total_spent,
    MAX(order_date) as last_order_date
FROM orders
WHERE status = 'completed'
GROUP BY customer_id;

-- Re-ejecutar UPSERT
INSERT INTO customer_summary (customer_id, total_orders, total_spent, last_order_date, updated_at)
SELECT customer_id, total_orders, total_spent, last_order_date, CURRENT_TIMESTAMP
FROM customer_summary_staging
ON CONFLICT (customer_id) 
DO UPDATE SET
    total_orders = EXCLUDED.total_orders,
    total_spent = EXCLUDED.total_spent,
    last_order_date = EXCLUDED.last_order_date,
    updated_at = CURRENT_TIMESTAMP;

-- Verificar que customer_id = 1 fue actualizado
SELECT * FROM customer_summary WHERE customer_id = 1;
```

**¿El total_orders y total_spent de customer_id=1 aumentaron? (Sí/No):** _______

**Nuevos valores:**
```
 customer_id | total_orders | total_spent | last_order_date     | updated_at
-------------|--------------|-------------|---------------------|------------
_______________________________________________
```

### Verificación
- ✅ UPSERT inserta registros nuevos
- ✅ UPSERT actualiza registros existentes
- ✅ El campo updated_at se actualiza correctamente
- ✅ Comprendes el flujo staging → target

**Duración:** 30 minutos

---

## 📋 Ejercicio 7: Deduplicación de Datos (Duración: 25 minutos)

### Objetivo
Aplicar técnicas de deduplicación usando window functions, crítico para calidad de datos.

### Pasos

1. **Crear tabla con duplicados intencionales**
```sql
CREATE TABLE customer_events_duplicated (
    event_id SERIAL,
    customer_id INT,
    event_type VARCHAR(50),
    event_date DATE,
    value DECIMAL(10, 2)
);

-- Insertar datos con duplicados
INSERT INTO customer_events_duplicated (customer_id, event_type, event_date, value) VALUES
(1, 'purchase', '2024-01-10', 100.00),
(1, 'purchase', '2024-01-10', 100.00), -- duplicado exacto
(1, 'purchase', '2024-01-10', 105.00), -- duplicado con valor diferente
(2, 'login', '2024-01-15', NULL),
(2, 'login', '2024-01-15', NULL), -- duplicado exacto
(3, 'purchase', '2024-01-20', 200.00),
(3, 'purchase', '2024-01-20', 200.00),
(3, 'purchase', '2024-01-20', 200.00); -- triplicado
```

**Total registros:** 
```sql
SELECT COUNT(*) FROM customer_events_duplicated;
```
**Resultado:** _______

2. **Identificar duplicados con ROW_NUMBER()**
```sql
SELECT 
    event_id,
    customer_id,
    event_type,
    event_date,
    value,
    ROW_NUMBER() OVER (
        PARTITION BY customer_id, event_type, event_date, value 
        ORDER BY event_id
    ) as row_num
FROM customer_events_duplicated
ORDER BY customer_id, event_date, event_id;
```

**Registros con row_num > 1 son duplicados:**
```
 event_id | customer_id | event_type | event_date | value  | row_num
----------|-------------|------------|------------|--------|--------
_______________________________________________
_______________________________________________
_______________________________________________
```

3. **Eliminar duplicados - Método 1: DELETE con subconsulta**
```sql
-- Primero, ver cuáles se eliminarían
SELECT event_id 
FROM (
    SELECT 
        event_id,
        ROW_NUMBER() OVER (
            PARTITION BY customer_id, event_type, event_date, value 
            ORDER BY event_id
        ) as row_num
    FROM customer_events_duplicated
) t
WHERE row_num > 1;
```

**IDs a eliminar:** _______________________

```sql
-- Ahora eliminar
DELETE FROM customer_events_duplicated
WHERE event_id IN (
    SELECT event_id FROM (
        SELECT 
            event_id,
            ROW_NUMBER() OVER (
                PARTITION BY customer_id, event_type, event_date, value 
                ORDER BY event_id
            ) as row_num
        FROM customer_events_duplicated
    ) t
    WHERE row_num > 1
);
```

**Registros eliminados:** _______

4. **Verificar que no quedan duplicados**
```sql
SELECT COUNT(*) as total_after_dedup FROM customer_events_duplicated;

-- Ver datos finales
SELECT * FROM customer_events_duplicated ORDER BY customer_id, event_date;
```

**Total después de deduplicación:** _______

**¿Cuántos duplicados se eliminaron?** _______

5. **Método 2: DISTINCT ON (PostgreSQL) - Crear tabla limpia**
```sql
-- Recrear tabla con duplicados
TRUNCATE customer_events_duplicated;
INSERT INTO customer_events_duplicated (customer_id, event_type, event_date, value) VALUES
(1, 'purchase', '2024-01-10', 100.00),
(1, 'purchase', '2024-01-10', 100.00),
(1, 'purchase', '2024-01-10', 105.00), -- queremos mantener el valor más alto
(2, 'login', '2024-01-15', NULL),
(2, 'login', '2024-01-15', NULL),
(3, 'purchase', '2024-01-20', 200.00),
(3, 'purchase', '2024-01-20', 200.00),
(3, 'purchase', '2024-01-20', 200.00);

-- Usar DISTINCT ON para quedarnos con el valor más alto por grupo
CREATE TABLE customer_events_clean AS
SELECT DISTINCT ON (customer_id, event_type, event_date)
    customer_id,
    event_type,
    event_date,
    value
FROM customer_events_duplicated
ORDER BY customer_id, event_type, event_date, value DESC NULLS LAST;

SELECT * FROM customer_events_clean ORDER BY customer_id, event_date;
```

**Resultado (debe tener solo registros únicos):**
```
 customer_id | event_type | event_date | value
-------------|------------|------------|-------
_______________________________________________
_______________________________________________
_______________________________________________
```

### Verificación
- ✅ Identificas duplicados con ROW_NUMBER()
- ✅ Puedes eliminar duplicados con DELETE + subconsulta
- ✅ Conoces DISTINCT ON como alternativa en PostgreSQL
- ✅ Comprendes cómo elegir qué registro mantener (ORDER BY en window function)

**Duración:** 25 minutos

---

## 📋 Ejercicio 8: Optimización con Índices y EXPLAIN (Duración: 30 minutos)

### Objetivo
Aprender a identificar queries lentas y optimizarlas con índices.

### Pasos

1. **Crear tabla grande para pruebas de performance**
```sql
-- Generar tabla con 100,000 registros
CREATE TABLE large_orders AS
SELECT 
    generate_series(1, 100000) as order_id,
    (random() * 1000)::INT + 1 as customer_id,
    CURRENT_DATE - (random() * 365)::INT as order_date,
    (random() * 1000)::DECIMAL(10, 2) as amount,
    CASE 
        WHEN random() < 0.7 THEN 'completed'
        WHEN random() < 0.9 THEN 'shipped'
        ELSE 'pending'
    END as status;

-- Verificar
SELECT COUNT(*) FROM large_orders;
```

**Total registros creados:** _______

2. **Query SIN índice - Ver plan de ejecución**
```sql
EXPLAIN ANALYZE
SELECT * FROM large_orders 
WHERE customer_id = 500 AND status = 'completed';
```

**Tu plan de ejecución (copia las líneas clave):**
```
_______________________________________________
_______________________________________________
_______________________________________________
Execution Time: _______ ms
```

**Tipo de scan usado:** _______ (Seq Scan o Index Scan)

3. **Crear índice en customer_id**
```sql
CREATE INDEX idx_large_orders_customer ON large_orders(customer_id);

-- Re-ejecutar query
EXPLAIN ANALYZE
SELECT * FROM large_orders 
WHERE customer_id = 500 AND status = 'completed';
```

**Nuevo plan:**
```
_______________________________________________
_______________________________________________
Execution Time: _______ ms
```

**¿Mejoró el tiempo? (Sí/No):** _______  
**¿Ahora usa Index Scan? (Sí/No):** _______

4. **Crear índice compuesto (mejor para esta query)**
```sql
-- Eliminar índice anterior
DROP INDEX idx_large_orders_customer;

-- Crear índice compuesto
CREATE INDEX idx_large_orders_customer_status ON large_orders(customer_id, status);

-- Re-ejecutar
EXPLAIN ANALYZE
SELECT * FROM large_orders 
WHERE customer_id = 500 AND status = 'completed';
```

**Tiempo con índice compuesto:** _______ ms

**¿Es más rápido que el índice simple? (Sí/No):** _______

5. **Índice parcial (solo para status='completed')**
```sql
CREATE INDEX idx_large_orders_completed ON large_orders(customer_id, order_date)
WHERE status = 'completed';

-- Query que se beneficia
EXPLAIN ANALYZE
SELECT * FROM large_orders 
WHERE customer_id = 500 AND status = 'completed'
ORDER BY order_date DESC
LIMIT 10;
```

**Tiempo con índice parcial:** _______ ms

**Ventaja de índices parciales:**
```
_______________________________________________
_______________________________________________
```

6. **VACUUM y ANALYZE - Actualizar estadísticas**
```sql
-- Actualizar estadísticas para el query planner
ANALYZE large_orders;

-- Ver estadísticas
SELECT 
    schemaname,
    tablename,
    n_live_tup as live_rows,
    n_dead_tup as dead_rows,
    last_analyze
FROM pg_stat_user_tables
WHERE tablename = 'large_orders';
```

**Estadísticas:**
```
 schemaname | tablename    | live_rows | dead_rows | last_analyze
------------|--------------|-----------|-----------|-------------
_______________________________________________
```

### Verificación
- ✅ Seq Scan escanea toda la tabla (lento en tablas grandes)
- ✅ Index Scan usa índice (mucho más rápido)
- ✅ Índices compuestos ayudan con queries multi-columna
- ✅ Índices parciales reducen tamaño y mejoran performance para subconjuntos
- ✅ ANALYZE actualiza estadísticas para el query planner

**Duración:** 30 minutos

---

## 📋 Ejercicio 9: Queries de Producción Realistas (Duración: 35 minutos)

### Objetivo
Aplicar todos los conceptos en queries complejas típicas de entornos de producción.

### Pasos

1. **Dashboard de métricas de negocio**
```sql
WITH daily_metrics AS (
    SELECT 
        order_date::DATE as date,
        COUNT(*) as orders,
        COUNT(DISTINCT customer_id) as unique_customers,
        SUM(total_amount) as revenue
    FROM orders
    WHERE status IN ('completed', 'shipped')
    GROUP BY order_date::DATE
),
metrics_with_ma AS (
    SELECT 
        date,
        orders,
        unique_customers,
        revenue,
        AVG(revenue) OVER (
            ORDER BY date 
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ) as revenue_7day_ma,
        LAG(revenue, 7) OVER (ORDER BY date) as revenue_7days_ago
    FROM daily_metrics
)
SELECT 
    date,
    orders,
    unique_customers,
    ROUND(revenue, 2) as revenue,
    ROUND(revenue_7day_ma, 2) as revenue_7day_ma,
    ROUND(((revenue - revenue_7days_ago) / NULLIF(revenue_7days_ago, 0)) * 100, 2) as wow_growth_pct
FROM metrics_with_ma
ORDER BY date DESC
LIMIT 10;
```

**Tu resultado (primeras 5 filas):**
```
 date       | orders | unique_customers | revenue  | revenue_7day_ma | wow_growth_pct
------------|--------|------------------|----------|-----------------|----------------
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________
```

2. **RFM Analysis (Recency, Frequency, Monetary)**
```sql
WITH customer_rfm AS (
    SELECT 
        customer_id,
        MAX(order_date) as last_order_date,
        COUNT(*) as frequency,
        SUM(total_amount) as monetary
    FROM orders
    WHERE status = 'completed'
    GROUP BY customer_id
),
rfm_scores AS (
    SELECT 
        customer_id,
        CURRENT_DATE - last_order_date::DATE as recency_days,
        frequency,
        monetary,
        NTILE(5) OVER (ORDER BY CURRENT_DATE - last_order_date::DATE DESC) as r_score,
        NTILE(5) OVER (ORDER BY frequency) as f_score,
        NTILE(5) OVER (ORDER BY monetary) as m_score
    FROM customer_rfm
)
SELECT 
    c.name,
    r.recency_days,
    r.frequency,
    ROUND(r.monetary, 2) as total_spent,
    r.r_score,
    r.f_score,
    r.m_score,
    (r.r_score + r.f_score + r.m_score) as rfm_total,
    CASE 
        WHEN (r.r_score + r.f_score + r.m_score) >= 12 THEN 'VIP'
        WHEN (r.r_score + r.f_score + r.m_score) >= 9 THEN 'Loyal'
        WHEN (r.r_score + r.f_score + r.m_score) >= 6 THEN 'Potential'
        ELSE 'At Risk'
    END as customer_segment
FROM rfm_scores r
INNER JOIN customers c ON r.customer_id = c.customer_id
ORDER BY rfm_total DESC;
```

**Tus segmentos de clientes:**
```
 name          | recency_days | frequency | total_spent | r_score | f_score | m_score | rfm_total | customer_segment
---------------|--------------|-----------|-------------|---------|---------|---------|-----------|------------------
_______________________________________________
_______________________________________________
_______________________________________________
```

3. **Cohort analysis - Retención por mes de signup**
```sql
WITH customer_cohorts AS (
    SELECT 
        c.customer_id,
        DATE_TRUNC('month', c.signup_date) as cohort_month,
        DATE_TRUNC('month', o.order_date) as order_month
    FROM customers c
    LEFT JOIN orders o ON c.customer_id = o.customer_id AND o.status = 'completed'
),
cohort_data AS (
    SELECT 
        cohort_month,
        order_month,
        COUNT(DISTINCT customer_id) as customers
    FROM customer_cohorts
    WHERE order_month IS NOT NULL
    GROUP BY cohort_month, order_month
),
cohort_sizes AS (
    SELECT 
        cohort_month,
        COUNT(DISTINCT customer_id) as cohort_size
    FROM customers
    GROUP BY DATE_TRUNC('month', signup_date)
)
SELECT 
    TO_CHAR(cd.cohort_month, 'YYYY-MM') as cohort,
    TO_CHAR(cd.order_month, 'YYYY-MM') as order_month,
    cd.customers,
    cs.cohort_size,
    ROUND((cd.customers::DECIMAL / cs.cohort_size) * 100, 2) as retention_pct
FROM cohort_data cd
INNER JOIN cohort_sizes cs ON cd.cohort_month = cs.cohort_month
ORDER BY cd.cohort_month, cd.order_month;
```

**Tus datos de cohort:**
```
 cohort  | order_month | customers | cohort_size | retention_pct
---------|-------------|-----------|-------------|---------------
_______________________________________________
_______________________________________________
_______________________________________________
```

### Verificación
- ✅ Puedes combinar CTEs, window functions y agregaciones
- ✅ Entiendes NTILE para segmentación
- ✅ Comprendes análisis de cohortes

**Duración:** 35 minutos

---

## 📋 Ejercicio 10: Mini-Proyecto ETL Completo (Duración: 45 minutos)

### Objetivo
Crear un pipeline ETL completo: extracción, transformación, carga con validaciones.

### Pasos

1. **Diseñar modelo de tablas destino (warehouse)**
```sql
-- Dimension: Customers
CREATE TABLE dim_customers (
    customer_key SERIAL PRIMARY KEY,
    customer_id INT UNIQUE,
    email VARCHAR(255),
    name VARCHAR(100),
    country VARCHAR(50),
    signup_date DATE,
    customer_segment VARCHAR(20),
    valid_from TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    valid_to TIMESTAMP,
    is_current BOOLEAN DEFAULT TRUE
);

-- Fact: Daily Sales
CREATE TABLE fact_daily_sales (
    sales_date DATE,
    customer_key INT REFERENCES dim_customers(customer_key),
    product_category VARCHAR(50),
    order_count INT,
    revenue DECIMAL(12, 2),
    PRIMARY KEY (sales_date, customer_key, product_category)
);
```

2. **ETL Paso 1: Cargar dimensión de clientes con SCD Type 2**
```sql
-- Calcular segmento de cliente
WITH customer_segments AS (
    SELECT 
        c.customer_id,
        c.email,
        c.name,
        c.country,
        c.signup_date,
        COUNT(o.order_id) as order_count,
        SUM(o.total_amount) as total_spent,
        CASE 
            WHEN COALESCE(SUM(o.total_amount), 0) > 1000 THEN 'VIP'
            WHEN COALESCE(SUM(o.total_amount), 0) > 500 THEN 'Regular'
            ELSE 'New'
        END as segment
    FROM customers c
    LEFT JOIN orders o ON c.customer_id = o.customer_id AND o.status = 'completed'
    GROUP BY c.customer_id, c.email, c.name, c.country, c.signup_date
)
INSERT INTO dim_customers (customer_id, email, name, country, signup_date, customer_segment, is_current)
SELECT customer_id, email, name, country, signup_date, segment, TRUE
FROM customer_segments
ON CONFLICT (customer_id) DO NOTHING;
```

**Registros insertados en dim_customers:** _______

3. **ETL Paso 2: Cargar fact table de ventas diarias**
```sql
INSERT INTO fact_daily_sales (sales_date, customer_key, product_category, order_count, revenue)
SELECT 
    o.order_date::DATE as sales_date,
    dc.customer_key,
    p.category as product_category,
    COUNT(DISTINCT o.order_id) as order_count,
    SUM(oi.quantity * oi.unit_price) as revenue
FROM orders o
INNER JOIN dim_customers dc ON o.customer_id = dc.customer_id AND dc.is_current = TRUE
INNER JOIN order_items oi ON o.order_id = oi.order_id
INNER JOIN products p ON oi.product_id = p.product_id
WHERE o.status IN ('completed', 'shipped')
GROUP BY o.order_date::DATE, dc.customer_key, p.category
ON CONFLICT (sales_date, customer_key, product_category)
DO UPDATE SET
    order_count = EXCLUDED.order_count,
    revenue = EXCLUDED.revenue;
```

**Registros insertados en fact_daily_sales:** _______

4. **Validación de calidad de datos**
```sql
-- Validación 1: No debe haber nulls en claves
SELECT 'Nulls en dim_customers.customer_id' as validation,
       COUNT(*) as failing_rows
FROM dim_customers
WHERE customer_id IS NULL
UNION ALL
SELECT 'Nulls en fact_daily_sales.customer_key',
       COUNT(*)
FROM fact_daily_sales
WHERE customer_key IS NULL
UNION ALL
SELECT 'Nulls en fact_daily_sales.sales_date',
       COUNT(*)
FROM fact_daily_sales
WHERE sales_date IS NULL;
```

**¿Hay rows fallidas? (deberían ser 0):**
```
 validation                                 | failing_rows
--------------------------------------------|-------------
_______________________________________________
_______________________________________________
_______________________________________________
```

```sql
-- Validación 2: Revenue no puede ser negativo
SELECT 'Revenue negativo' as validation,
       COUNT(*) as failing_rows
FROM fact_daily_sales
WHERE revenue < 0;
```

**Failing rows:** _______

5. **Query analítica sobre el warehouse**
```sql
SELECT 
    dc.customer_segment,
    fds.product_category,
    COUNT(DISTINCT fds.sales_date) as active_days,
    SUM(fds.order_count) as total_orders,
    ROUND(SUM(fds.revenue), 2) as total_revenue,
    ROUND(AVG(fds.revenue), 2) as avg_daily_revenue
FROM fact_daily_sales fds
INNER JOIN dim_customers dc ON fds.customer_key = dc.customer_key
GROUP BY dc.customer_segment, fds.product_category
ORDER BY total_revenue DESC;
```

**Análisis por segmento y categoría:**
```
 customer_segment | product_category | active_days | total_orders | total_revenue | avg_daily_revenue
------------------|------------------|-------------|--------------|---------------|-------------------
_______________________________________________
_______________________________________________
_______________________________________________
```

6. **Documentar el pipeline ETL**

**Completa el diagrama:**
```
Sources → Staging → Transformations → Target → Validations

1. Sources: _______________________________
2. Staging: _______________________________
3. Transformations: _______________________________
4. Target: _______________________________
5. Validations: _______________________________
```

### Verificación
- ✅ Dimensión cargada con segmentación
- ✅ Fact table con métricas agregadas
- ✅ Validaciones de calidad ejecutadas
- ✅ Queries analíticas funcionando
- ✅ Comprendes el flujo completo ETL

**Duración:** 45 minutos

---

## 📊 Resumen de Tiempo Total

| Ejercicio | Duración |
|-----------|----------|
| 1. Configuración de BD | 25 min |
| 2. CTEs y Subconsultas | 20 min |
| 3. Window Functions | 30 min |
| 4. JOINs Complejos | 25 min |
| 5. GROUP BY Avanzado | 25 min |
| 6. MERGE/UPSERT | 30 min |
| 7. Deduplicación | 25 min |
| 8. Optimización e Índices | 30 min |
| 9. Queries de Producción | 35 min |
| 10. Mini-Proyecto ETL | 45 min |
| **TOTAL** | **290 min (≈5 horas)** |

*Nota: El tiempo puede variar. Dedica tiempo extra si es necesario para consolidar conceptos.*

---

## ✅ Checklist Final

Antes de pasar al Módulo 03, verifica que completaste:

- [ ] Base de datos configurada con esquema e-commerce
- [ ] Puedes escribir y entender CTEs anidados
- [ ] Dominas al menos 6 window functions (ROW_NUMBER, RANK, LAG, LEAD, SUM OVER, AVG OVER)
- [ ] Comprendes todos los tipos de JOIN y cuándo usar cada uno
- [ ] Puedes usar GROUP BY con HAVING y ROLLUP
- [ ] Implementaste UPSERT exitosamente con ON CONFLICT
- [ ] Deduplicas datos usando ROW_NUMBER()
- [ ] Sabes crear índices y leer EXPLAIN ANALYZE
- [ ] Completaste análisis RFM y cohort analysis
- [ ] Construiste un pipeline ETL con validaciones

---

## 🎯 Próximos Pasos

1. **Actualiza tu `progreso.md`** marcando ejercicios completados
2. **Autoevalúate con `retroalimentacion.md`**
3. **Guarda tus scripts SQL** en archivos .sql para referencia futura
4. **Consulta `recursos.md`** para datasets adicionales y tutoriales avanzados
5. **Prepárate para el Módulo 03**: Python para Data Engineering

---

**🎉 ¡Excelente trabajo!** Has dominado SQL avanzado para Data Engineering. Estos conceptos son fundamentales y los usarás diariamente en tu carrera.

**💡 Tip Final**: Practica escribiendo queries sin consultar las soluciones. La fluidez en SQL solo se logra con práctica repetida. Considera hacer estos ejercicios nuevamente después de completar el curso completo.