# Módulo 4: Subconsultas y CTEs

## Introducción

Las subconsultas y CTEs (Common Table Expressions) son herramientas poderosas que te permiten escribir consultas más complejas y legibles.

## Subconsultas

Una subconsulta es una consulta dentro de otra consulta.

### Subconsulta en WHERE

```sql
-- Empleados con salario mayor al promedio
SELECT Nombre, Salario
FROM Empleados
WHERE Salario > (SELECT AVG(Salario) FROM Empleados);
```

### Subconsulta en FROM

```sql
-- Usar resultado de una consulta como tabla
SELECT AVG(TotalVentas) AS PromedioVentas
FROM (
    SELECT EmpleadoID, SUM(Monto) AS TotalVentas
    FROM Ventas
    GROUP BY EmpleadoID
) AS VentasPorEmpleado;
```

### Subconsulta con IN

```sql
-- Clientes que han hecho pedidos
SELECT Nombre
FROM Clientes
WHERE ClienteID IN (SELECT DISTINCT ClienteID FROM Pedidos);
```

## CTEs (Common Table Expressions)

Los CTEs hacen el código más legible y son ideales para consultas complejas.

```sql
-- CTE básico
WITH EmpleadosActivos AS (
    SELECT * FROM Empleados WHERE Activo = 1
)
SELECT * FROM EmpleadosActivos WHERE Salario > 50000;

-- CTE recursivo (ejemplo: jerarquía)
WITH Jerarquia AS (
    SELECT EmpleadoID, Nombre, JefeID, 1 AS Nivel
    FROM Empleados
    WHERE JefeID IS NULL
    
    UNION ALL
    
    SELECT E.EmpleadoID, E.Nombre, E.JefeID, J.Nivel + 1
    FROM Empleados E
    INNER JOIN Jerarquia J ON E.JefeID = J.EmpleadoID
)
SELECT * FROM Jerarquia;
```

## Conceptos Clave

- 🔑 **Subconsultas**: Consultas anidadas
- 🔑 **CTEs**: Consultas temporales con nombre
- 🔑 **EXISTS**: Verifica existencia
- 🔑 **ANY/ALL**: Comparaciones con conjuntos

¡Las subconsultas y CTEs son esenciales para consultas avanzadas! 🚀
