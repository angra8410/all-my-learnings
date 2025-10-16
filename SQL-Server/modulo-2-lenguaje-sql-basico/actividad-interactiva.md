# Actividades Interactivas - Módulo 2: Lenguaje SQL Básico

## Base de Datos de Práctica

Para todos los ejercicios, usa esta base de datos:

```sql
CREATE DATABASE TiendaPractica;
USE TiendaPractica;

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
('Laptop Dell', 'Computadoras', 1200.00, 10, '2024-01-15', 1),
('Mouse Inalámbrico', 'Accesorios', 35.99, 75, '2024-01-20', 1),
('Teclado Mecánico RGB', 'Accesorios', 120.50, 25, '2024-02-01', 1),
('Monitor 27 pulgadas', 'Computadoras', 450.00, 12, '2024-02-10', 1),
('Tablet iPad', 'Tablets', 599.99, 8, '2024-02-15', 1),
('Auriculares Bluetooth', 'Accesorios', 89.99, 40, '2024-03-01', 1),
('Laptop HP', 'Computadoras', 950.00, 5, '2024-03-10', 1),
('Webcam HD', 'Accesorios', 65.00, 20, '2024-03-15', 0),
('Smartphone Samsung', 'Teléfonos', 799.99, 15, '2024-03-20', 1),
('Cargador Portátil', 'Accesorios', 45.50, 60, '2024-04-01', 1);
```

---

## Sección 1: Consultas Básicas con SELECT

### Ejercicio 1
Escribe una consulta para mostrar todos los productos:
```sql


```

### Ejercicio 2
Muestra solo el nombre y precio de todos los productos:
```sql


```

### Ejercicio 3
Muestra los productos con un alias "NombreProducto" y "PrecioUSD":
```sql


```

---

## Sección 2: Filtrado con WHERE

### Ejercicio 4
Muestra productos con precio mayor a $100:
```sql


```

### Ejercicio 5
Muestra productos de la categoría 'Accesorios':
```sql


```

### Ejercicio 6
Muestra productos con stock menor o igual a 15:
```sql


```

### Ejercicio 7
Muestra productos activos con precio entre $50 y $500:
```sql


```

---

## Sección 3: Operadores Lógicos

### Ejercicio 8
Muestra productos de categoría 'Computadoras' O 'Tablets':
```sql


```

### Ejercicio 9
Muestra productos con precio mayor a $100 Y stock mayor a 10:
```sql


```

### Ejercicio 10
Muestra productos que NO sean de categoría 'Accesorios':
```sql


```

---

## Sección 4: Operadores Especiales

### Ejercicio 11
Usa LIKE para encontrar productos que contengan 'Laptop':
```sql


```

### Ejercicio 12
Usa IN para mostrar productos de las categorías: 'Computadoras', 'Tablets', 'Teléfonos':
```sql


```

### Ejercicio 13
Muestra productos ingresados en marzo de 2024:
```sql


```

---

## Sección 5: ORDER BY

### Ejercicio 14
Muestra productos ordenados por precio de menor a mayor:
```sql


```

### Ejercicio 15
Muestra productos ordenados por categoría (A-Z) y luego por precio (mayor a menor):
```sql


```

---

## Sección 6: DISTINCT y TOP

### Ejercicio 16
Muestra todas las categorías únicas:
```sql


```

### Ejercicio 17
Muestra los 3 productos más caros:
```sql


```

---

## Sección 7: Funciones de Agregación

### Ejercicio 18
Cuenta cuántos productos hay en total:
```sql


```

### Ejercicio 19
Calcula el precio promedio de todos los productos:
```sql


```

### Ejercicio 20
Encuentra el precio del producto más caro y más barato:
```sql


```

### Ejercicio 21
Calcula el valor total del inventario (Precio * Stock de todos los productos):
```sql


```

---

## Sección 8: GROUP BY

### Ejercicio 22
Cuenta cuántos productos hay en cada categoría:
```sql


```

### Ejercicio 23
Calcula el precio promedio por categoría:
```sql


```

### Ejercicio 24
Encuentra el stock total por categoría:
```sql


```

---

## Sección 9: HAVING

### Ejercicio 25
Muestra categorías que tienen más de 2 productos:
```sql


```

### Ejercicio 26
Muestra categorías con precio promedio mayor a $100:
```sql


```

---

## Sección 10: Desafíos Integrados

### Ejercicio 27: Reporte de Inventario Bajo
Crea una consulta que muestre productos con stock menor a 10, ordenados por stock ascendente, mostrando nombre, categoría, precio y stock:
```sql


```

### Ejercicio 28: Top Productos por Categoría
Muestra los 2 productos más caros de la categoría 'Accesorios':
```sql


```

### Ejercicio 29: Análisis de Productos Inactivos
Cuenta cuántos productos inactivos hay y muestra su valor total (precio * stock):
```sql


```

### Ejercicio 30: Reporte Completo por Categoría
Crea un reporte que muestre para cada categoría:
- Nombre de la categoría
- Cantidad de productos
- Precio promedio
- Precio mínimo
- Precio máximo
- Stock total

```sql


```

---

## Proyecto Mini: Dashboard de Tienda

Crea un conjunto de consultas que funcionen como un dashboard ejecutivo:

### Consulta 1: Resumen General
```sql
-- Total de productos, categorías únicas, valor total de inventario


```

### Consulta 2: Top 5 Productos Más Valiosos
```sql
-- Productos con mayor valor total (precio * stock)


```

### Consulta 3: Categorías con Bajo Stock
```sql
-- Categorías donde el stock promedio es menor a 20


```

### Consulta 4: Productos para Reposición
```sql
-- Productos activos con stock menor a 10


```

---

## Autoevaluación

**Ejercicios completados:** ___ / 30

**Conceptos que domino:**
- [ ] SELECT básico
- [ ] WHERE con condiciones
- [ ] Operadores AND, OR, NOT
- [ ] LIKE, IN, BETWEEN
- [ ] ORDER BY
- [ ] DISTINCT y TOP
- [ ] COUNT, SUM, AVG, MIN, MAX
- [ ] GROUP BY
- [ ] HAVING

**Lo que necesito repasar:** _______________________________________________

¡Revisa tus respuestas en retroalimentacion.md! 🎉
