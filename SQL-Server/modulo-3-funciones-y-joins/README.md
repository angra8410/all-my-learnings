# Módulo 3: Funciones y JOINs

## Introducción

Las bases de datos relacionales obtienen su poder de la capacidad de **relacionar tablas entre sí**. Los JOINs son la herramienta fundamental para combinar datos de múltiples tablas. En este módulo dominarás esta técnica esencial.

## ¿Qué son los JOINs?

Imagina que tienes dos listas:
- **Lista A**: Clientes (ID, Nombre)
- **Lista B**: Pedidos (ID, ClienteID, Total)

Un JOIN te permite combinar ambas listas para ver "qué cliente hizo qué pedido".

## Tipos de JOINs

### INNER JOIN - Intersección

Devuelve solo las filas que tienen coincidencias en AMBAS tablas.

```sql
SELECT 
    C.Nombre,
    P.Total,
    P.Fecha
FROM Clientes C
INNER JOIN Pedidos P ON C.ClienteID = P.ClienteID;
```

**Analogía**: Es como una fiesta donde solo entran las personas que están en ambas listas (invitados Y confirmados).

### LEFT JOIN (LEFT OUTER JOIN)

Devuelve TODAS las filas de la tabla izquierda, con o sin coincidencia en la derecha.

```sql
SELECT 
    C.Nombre,
    P.Total
FROM Clientes C
LEFT JOIN Pedidos P ON C.ClienteID = P.ClienteID;
-- Muestra todos los clientes, incluso si no tienen pedidos
```

**Analogía**: Todos los invitados aparecen en la lista, confirmaron o no.

### RIGHT JOIN (RIGHT OUTER JOIN)

Lo opuesto a LEFT JOIN: todas las filas de la tabla derecha.

```sql
SELECT 
    C.Nombre,
    P.Total
FROM Clientes C
RIGHT JOIN Pedidos P ON C.ClienteID = P.ClienteID;
-- Muestra todos los pedidos, incluso si no tienen cliente asociado
```

### FULL OUTER JOIN

Devuelve todas las filas de ambas tablas, con o sin coincidencias.

```sql
SELECT 
    C.Nombre,
    P.Total
FROM Clientes C
FULL OUTER JOIN Pedidos P ON C.ClienteID = P.ClienteID;
```

### CROSS JOIN - Producto Cartesiano

Combina cada fila de la primera tabla con cada fila de la segunda.

```sql
SELECT * 
FROM Colores
CROSS JOIN Tallas;
-- Si tienes 5 colores y 3 tallas, obtienes 15 combinaciones
```

## Funciones Avanzadas

### Funciones de Texto

```sql
-- Concatenar con separador
SELECT CONCAT(Nombre, ' ', Apellido) AS NombreCompleto FROM Empleados;

-- Formato
SELECT FORMAT(Precio, 'C', 'es-MX') AS PrecioFormateado FROM Productos;

-- LEFT, RIGHT
SELECT LEFT(Codigo, 3) AS Prefijo FROM Productos;
SELECT RIGHT(Codigo, 4) AS Sufijo FROM Productos;

-- CHARINDEX (buscar posición)
SELECT CHARINDEX('@', Email) AS PosicionArroba FROM Usuarios;
```

### Funciones de Fecha Avanzadas

```sql
-- Último día del mes
SELECT EOMONTH(GETDATE()) AS UltimoDiaMes;

-- Diferencia en diferentes unidades
SELECT DATEDIFF(YEAR, FechaNacimiento, GETDATE()) AS Edad FROM Personas;
SELECT DATEDIFF(MONTH, FechaContratacion, GETDATE()) AS MesesTrabajados FROM Empleados;

-- Formatear fechas
SELECT FORMAT(GETDATE(), 'dd/MM/yyyy') AS FechaFormateada;
SELECT FORMAT(GETDATE(), 'MMMM yyyy', 'es-ES') AS MesAnio;
```

### CASE - Condicionales en SQL

```sql
-- CASE simple
SELECT 
    Nombre,
    Precio,
    CASE 
        WHEN Precio < 50 THEN 'Económico'
        WHEN Precio BETWEEN 50 AND 200 THEN 'Medio'
        ELSE 'Premium'
    END AS Categoria
FROM Productos;

-- CASE con múltiples condiciones
SELECT 
    Nombre,
    Stock,
    CASE 
        WHEN Stock = 0 THEN 'Sin stock'
        WHEN Stock < 10 THEN 'Stock bajo'
        WHEN Stock < 50 THEN 'Stock normal'
        ELSE 'Stock alto'
    END AS EstadoInventario
FROM Productos;
```

### ISNULL y COALESCE

```sql
-- ISNULL: Reemplaza NULL con un valor
SELECT Nombre, ISNULL(Telefono, 'Sin teléfono') AS Telefono FROM Clientes;

-- COALESCE: Primer valor no nulo
SELECT COALESCE(TelefonoCelular, TelefonoFijo, Email, 'Sin contacto') AS Contacto
FROM Clientes;
```

## Caso Práctico Completo

```sql
CREATE DATABASE EmpresaDB;
USE EmpresaDB;

CREATE TABLE Departamentos (
    DepartamentoID INT PRIMARY KEY IDENTITY,
    Nombre NVARCHAR(100) NOT NULL
);

CREATE TABLE Empleados (
    EmpleadoID INT PRIMARY KEY IDENTITY,
    Nombre NVARCHAR(100) NOT NULL,
    DepartamentoID INT,
    Salario DECIMAL(10,2),
    FechaContratacion DATE,
    FOREIGN KEY (DepartamentoID) REFERENCES Departamentos(DepartamentoID)
);

-- Insertar datos
INSERT INTO Departamentos VALUES ('Ventas'), ('TI'), ('RRHH');

INSERT INTO Empleados VALUES 
('Ana García', 1, 45000, '2020-01-15'),
('Carlos López', 2, 55000, '2019-06-10'),
('María Rodríguez', 1, 42000, '2021-03-20'),
('Luis Martínez', 3, 48000, '2018-09-05');

-- Consulta con JOIN
SELECT 
    E.Nombre AS Empleado,
    D.Nombre AS Departamento,
    E.Salario,
    DATEDIFF(YEAR, E.FechaContratacion, GETDATE()) AS AniosTrabajados,
    CASE 
        WHEN E.Salario < 45000 THEN 'Junior'
        WHEN E.Salario BETWEEN 45000 AND 55000 THEN 'Semi-Senior'
        ELSE 'Senior'
    END AS Nivel
FROM Empleados E
INNER JOIN Departamentos D ON E.DepartamentoID = D.DepartamentoID;
```

## Conceptos Clave

- 🔑 **INNER JOIN**: Solo coincidencias
- 🔑 **LEFT JOIN**: Todos de la izquierda
- 🔑 **RIGHT JOIN**: Todos de la derecha
- 🔑 **FULL JOIN**: Todos de ambas
- 🔑 **CASE**: Lógica condicional
- 🔑 **ISNULL/COALESCE**: Manejar valores nulos

¡Practica combinando tablas! Es la habilidad más importante en SQL. 🚀
