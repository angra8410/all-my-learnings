# Módulo 2: Lenguaje SQL Básico

## Introducción

En el Módulo 1 aprendiste a crear bases de datos y tablas, e insertar datos básicos. Ahora es momento de **consultar** esa información de formas más inteligentes. Este módulo se enfoca en el arte de hacer preguntas precisas a tu base de datos.

## La cláusula SELECT

SELECT es el comando más usado en SQL. Es como hacer preguntas a tu base de datos: "¿qué productos tienes?", "¿cuáles cuestan menos de $50?", "¿quién es el cliente más antiguo?".

### Sintaxis básica:
```sql
SELECT columna1, columna2, ...
FROM tabla
WHERE condición
ORDER BY columna;
```

### Seleccionar todas las columnas:
```sql
-- El asterisco (*) significa "todas las columnas"
SELECT * FROM Productos;
```

### Seleccionar columnas específicas:
```sql
-- Solo las columnas que necesitas (más eficiente)
SELECT Nombre, Precio FROM Productos;
```

### Renombrar columnas en resultados (ALIAS):
```sql
-- Usa AS para dar nombres más claros
SELECT 
    Nombre AS NombreProducto,
    Precio AS PrecioUnitario
FROM Productos;
```

## La cláusula WHERE - Filtrar Datos

WHERE es como un filtro: solo muestra las filas que cumplen una condición.

### Comparaciones básicas:
```sql
-- Igual a
SELECT * FROM Productos WHERE Precio = 100;

-- Mayor que
SELECT * FROM Productos WHERE Precio > 50;

-- Menor o igual que
SELECT * FROM Productos WHERE Stock <= 10;

-- Diferente de
SELECT * FROM Productos WHERE Categoria != 'Electrónica';
-- o
SELECT * FROM Productos WHERE Categoria <> 'Electrónica';
```

### Operadores lógicos:

**AND - Todas las condiciones deben cumplirse:**
```sql
-- Productos caros y con poco stock
SELECT * FROM Productos 
WHERE Precio > 100 AND Stock < 5;
```

**OR - Al menos una condición debe cumplirse:**
```sql
-- Productos baratos O en oferta
SELECT * FROM Productos 
WHERE Precio < 20 OR EnOferta = 1;
```

**NOT - Niega una condición:**
```sql
-- Productos que NO son de categoría Electrónica
SELECT * FROM Productos 
WHERE NOT Categoria = 'Electrónica';
```

**Combinando operadores:**
```sql
-- Usa paréntesis para claridad
SELECT * FROM Productos 
WHERE (Precio > 100 OR EnOferta = 1) 
  AND Stock > 0;
```

### Operadores especiales:

**BETWEEN - Rango de valores:**
```sql
-- Productos entre $50 y $200
SELECT * FROM Productos 
WHERE Precio BETWEEN 50 AND 200;
-- Equivale a: Precio >= 50 AND Precio <= 200
```

**IN - Lista de valores:**
```sql
-- Productos de categorías específicas
SELECT * FROM Productos 
WHERE Categoria IN ('Electrónica', 'Computadoras', 'Tablets');
-- Equivale a: Categoria = 'Electrónica' OR Categoria = 'Computadoras' OR ...
```

**LIKE - Búsqueda de patrones:**
```sql
-- Productos que empiezan con 'Lap'
SELECT * FROM Productos WHERE Nombre LIKE 'Lap%';

-- Productos que terminan con 'Pro'
SELECT * FROM Productos WHERE Nombre LIKE '%Pro';

-- Productos que contienen 'Plus'
SELECT * FROM Productos WHERE Nombre LIKE '%Plus%';

-- Patrones más complejos
-- _ representa un solo carácter
SELECT * FROM Productos WHERE Codigo LIKE 'PR_123';
```

**IS NULL / IS NOT NULL - Valores nulos:**
```sql
-- Productos sin descripción
SELECT * FROM Productos WHERE Descripcion IS NULL;

-- Productos con descripción
SELECT * FROM Productos WHERE Descripcion IS NOT NULL;
```

## ORDER BY - Ordenar Resultados

Ordena los resultados por una o más columnas.

```sql
-- Orden ascendente (A-Z, 0-9, menor a mayor) - por defecto
SELECT * FROM Productos ORDER BY Precio;
SELECT * FROM Productos ORDER BY Precio ASC;

-- Orden descendente (Z-A, 9-0, mayor a menor)
SELECT * FROM Productos ORDER BY Precio DESC;

-- Ordenar por múltiples columnas
SELECT * FROM Productos 
ORDER BY Categoria ASC, Precio DESC;
-- Primero por categoría (A-Z), luego por precio (mayor a menor)
```

## DISTINCT - Eliminar Duplicados

```sql
-- Ver todas las categorías únicas
SELECT DISTINCT Categoria FROM Productos;

-- Combinaciones únicas
SELECT DISTINCT Categoria, Marca FROM Productos;
```

## TOP - Limitar Resultados

```sql
-- Los 10 productos más caros
SELECT TOP 10 * FROM Productos 
ORDER BY Precio DESC;

-- Los 5 clientes más recientes
SELECT TOP 5 * FROM Clientes 
ORDER BY FechaRegistro DESC;

-- Top con porcentaje
SELECT TOP 10 PERCENT * FROM Productos 
ORDER BY Ventas DESC;
```

## Funciones de Agregación

Calculan valores a partir de múltiples filas.

### COUNT - Contar filas:
```sql
-- Total de productos
SELECT COUNT(*) AS TotalProductos FROM Productos;

-- Productos activos
SELECT COUNT(*) FROM Productos WHERE Activo = 1;

-- Contar valores no nulos
SELECT COUNT(Descripcion) FROM Productos;
```

### SUM - Sumar valores:
```sql
-- Valor total del inventario
SELECT SUM(Precio * Stock) AS ValorInventario 
FROM Productos;
```

### AVG - Promedio:
```sql
-- Precio promedio
SELECT AVG(Precio) AS PrecioPromedio FROM Productos;
```

### MIN y MAX - Valores mínimo y máximo:
```sql
-- Producto más barato y más caro
SELECT 
    MIN(Precio) AS MasBarato,
    MAX(Precio) AS MasCaro
FROM Productos;
```

## GROUP BY - Agrupar Datos

Agrupa filas que tienen valores iguales en columnas específicas.

```sql
-- Total de productos por categoría
SELECT 
    Categoria,
    COUNT(*) AS CantidadProductos
FROM Productos
GROUP BY Categoria;

-- Precio promedio por categoría
SELECT 
    Categoria,
    AVG(Precio) AS PrecioPromedio,
    MIN(Precio) AS MasBarato,
    MAX(Precio) AS MasCaro
FROM Productos
GROUP BY Categoria;

-- Ventas por mes
SELECT 
    YEAR(FechaVenta) AS Anio,
    MONTH(FechaVenta) AS Mes,
    SUM(Total) AS VentasMes
FROM Ventas
GROUP BY YEAR(FechaVenta), MONTH(FechaVenta)
ORDER BY Anio, Mes;
```

## HAVING - Filtrar Grupos

HAVING es como WHERE, pero para grupos creados con GROUP BY.

```sql
-- Categorías con más de 10 productos
SELECT 
    Categoria,
    COUNT(*) AS Total
FROM Productos
GROUP BY Categoria
HAVING COUNT(*) > 10;

-- Categorías con precio promedio mayor a $100
SELECT 
    Categoria,
    AVG(Precio) AS PrecioPromedio
FROM Productos
GROUP BY Categoria
HAVING AVG(Precio) > 100;
```

**Diferencia WHERE vs HAVING:**
- WHERE filtra filas ANTES de agrupar
- HAVING filtra grupos DESPUÉS de agrupar

```sql
-- Correcto: WHERE antes, HAVING después
SELECT 
    Categoria,
    AVG(Precio) AS PrecioPromedio
FROM Productos
WHERE Activo = 1  -- Filtra productos activos
GROUP BY Categoria
HAVING AVG(Precio) > 50;  -- Filtra categorías con promedio > 50
```

## Operadores Matemáticos

```sql
-- Suma, resta, multiplicación, división
SELECT 
    Nombre,
    Precio,
    Precio * 0.16 AS IVA,
    Precio * 1.16 AS PrecioConIVA,
    Precio - (Precio * 0.10) AS PrecioConDescuento
FROM Productos;

-- Módulo (resto de división)
SELECT 10 % 3 AS Resto;  -- Resultado: 1
```

## Funciones de Cadena (String)

```sql
-- Concatenar
SELECT Nombre + ' - ' + Categoria AS Descripcion FROM Productos;

-- Mayúsculas y minúsculas
SELECT UPPER(Nombre), LOWER(Categoria) FROM Productos;

-- Longitud
SELECT Nombre, LEN(Nombre) AS Longitud FROM Productos;

-- Subcadenas
SELECT SUBSTRING(Nombre, 1, 10) AS NombreCorto FROM Productos;

-- Reemplazar
SELECT REPLACE(Descripcion, 'viejo', 'nuevo') FROM Productos;

-- Quitar espacios
SELECT TRIM(Nombre) FROM Productos;  -- Ambos lados
SELECT LTRIM(Nombre) FROM Productos; -- Izquierda
SELECT RTRIM(Nombre) FROM Productos; -- Derecha
```

## Funciones de Fecha

```sql
-- Fecha y hora actual
SELECT GETDATE() AS FechaHoraActual;

-- Fecha actual sin hora
SELECT CAST(GETDATE() AS DATE) AS FechaSoloActual;

-- Extraer partes
SELECT 
    YEAR(FechaVenta) AS Anio,
    MONTH(FechaVenta) AS Mes,
    DAY(FechaVenta) AS Dia,
    DATEPART(WEEK, FechaVenta) AS Semana
FROM Ventas;

-- Nombres de meses y días
SELECT DATENAME(MONTH, GETDATE()) AS NombreMes;
SELECT DATENAME(WEEKDAY, GETDATE()) AS NombreDia;

-- Agregar/restar tiempo
SELECT DATEADD(DAY, 30, GETDATE()) AS Dentro30Dias;
SELECT DATEADD(MONTH, -3, GETDATE()) AS Hace3Meses;

-- Diferencia entre fechas
SELECT DATEDIFF(DAY, FechaInicio, FechaFin) AS DiasTranscurridos
FROM Proyectos;
```

## Caso Práctico: Tienda Online

```sql
-- Base de datos de ejemplo
CREATE DATABASE TiendaOnline;
USE TiendaOnline;

CREATE TABLE Productos (
    ProductoID INT PRIMARY KEY IDENTITY,
    Nombre NVARCHAR(100) NOT NULL,
    Categoria NVARCHAR(50),
    Precio DECIMAL(10,2) NOT NULL,
    Stock INT DEFAULT 0,
    FechaIngreso DATE,
    Activo BIT DEFAULT 1
);

INSERT INTO Productos VALUES
('Laptop HP', 'Computadoras', 899.99, 15, '2024-01-10', 1),
('Mouse Logitech', 'Accesorios', 25.50, 50, '2024-01-15', 1),
('Teclado Mecánico', 'Accesorios', 85.00, 30, '2024-01-20', 1),
('Monitor Samsung', 'Computadoras', 299.99, 8, '2024-02-01', 1),
('Tablet Android', 'Tablets', 199.99, 20, '2024-02-05', 1);

-- Consultas útiles:

-- 1. Productos con stock bajo (menos de 10)
SELECT Nombre, Stock 
FROM Productos 
WHERE Stock < 10;

-- 2. Top 3 productos más caros
SELECT TOP 3 Nombre, Precio 
FROM Productos 
ORDER BY Precio DESC;

-- 3. Productos por categoría
SELECT 
    Categoria,
    COUNT(*) AS CantidadProductos,
    AVG(Precio) AS PrecioPromedio
FROM Productos
GROUP BY Categoria;

-- 4. Valor total del inventario
SELECT SUM(Precio * Stock) AS ValorTotal FROM Productos;
```

## Mejores Prácticas

1. **Sé específico con SELECT**
   ```sql
   ✅ SELECT Nombre, Precio FROM Productos;
   ❌ SELECT * FROM Productos; -- Solo usa cuando realmente necesites todo
   ```

2. **Usa ALIAS descriptivos**
   ```sql
   SELECT COUNT(*) AS TotalClientes FROM Clientes;
   ```

3. **Indenta tu código SQL**
   ```sql
   SELECT 
       Categoria,
       AVG(Precio) AS Promedio
   FROM Productos
   WHERE Activo = 1
   GROUP BY Categoria
   HAVING AVG(Precio) > 100
   ORDER BY Promedio DESC;
   ```

4. **Filtra lo antes posible**
   ```sql
   -- WHERE reduce filas antes de procesar
   SELECT AVG(Precio)
   FROM Productos
   WHERE Activo = 1;  -- Filtra primero
   ```

5. **Comenta consultas complejas**
   ```sql
   -- Reporte de productos con bajo stock
   -- Solo productos activos, ordenados por urgencia
   SELECT ...
   ```

## Conceptos Clave

- 🔑 **SELECT**: Consultar datos
- 🔑 **WHERE**: Filtrar filas
- 🔑 **ORDER BY**: Ordenar resultados
- 🔑 **DISTINCT**: Eliminar duplicados
- 🔑 **TOP**: Limitar resultados
- 🔑 **GROUP BY**: Agrupar datos
- 🔑 **HAVING**: Filtrar grupos
- 🔑 **Funciones de agregación**: COUNT, SUM, AVG, MIN, MAX

## Próximos Pasos

En el **Módulo 3** aprenderás:
- JOINs (unir tablas)
- Funciones avanzadas
- CASE statements
- Subconsultas básicas

¡Practica mucho! La maestría viene con la repetición. 🚀
