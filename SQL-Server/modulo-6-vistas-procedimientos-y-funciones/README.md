# Módulo 6: Vistas, Procedimientos y Funciones

## Vistas (Views)

Las vistas son consultas guardadas que se comportan como tablas virtuales.

```sql
-- Crear vista
CREATE VIEW VistaEmpleadosActivos AS
SELECT EmpleadoID, Nombre, Departamento, Salario
FROM Empleados
WHERE Activo = 1;

-- Usar vista
SELECT * FROM VistaEmpleadosActivos WHERE Salario > 50000;
```

## Procedimientos Almacenados (Stored Procedures)

```sql
-- Crear procedimiento
CREATE PROCEDURE sp_ObtenerEmpleadosPorDepartamento
    @DepartamentoID INT
AS
BEGIN
    SELECT * FROM Empleados WHERE DepartamentoID = @DepartamentoID;
END;

-- Ejecutar procedimiento
EXEC sp_ObtenerEmpleadosPorDepartamento @DepartamentoID = 1;

-- Procedimiento con múltiples parámetros
CREATE PROCEDURE sp_InsertarProducto
    @Nombre NVARCHAR(100),
    @Precio DECIMAL(10,2),
    @Stock INT = 0  -- Valor por defecto
AS
BEGIN
    INSERT INTO Productos (Nombre, Precio, Stock)
    VALUES (@Nombre, @Precio, @Stock);
END;
```

## Funciones Definidas por el Usuario

### Funciones Escalares

```sql
-- Retorna un solo valor
CREATE FUNCTION fn_CalcularIVA (@Precio DECIMAL(10,2))
RETURNS DECIMAL(10,2)
AS
BEGIN
    RETURN @Precio * 0.16;
END;

-- Usar función
SELECT Nombre, Precio, dbo.fn_CalcularIVA(Precio) AS IVA FROM Productos;
```

### Funciones de Tabla

```sql
-- Retorna una tabla
CREATE FUNCTION fn_EmpleadosPorSalario (@SalarioMinimo DECIMAL(10,2))
RETURNS TABLE
AS
RETURN (
    SELECT * FROM Empleados WHERE Salario >= @SalarioMinimo
);

-- Usar función
SELECT * FROM dbo.fn_EmpleadosPorSalario(50000);
```

## Triggers (Disparadores)

```sql
-- Trigger AFTER INSERT
CREATE TRIGGER trg_AuditarInserciones
ON Productos
AFTER INSERT
AS
BEGIN
    INSERT INTO AuditoriaProductos (ProductoID, Accion, Fecha)
    SELECT ProductoID, 'INSERT', GETDATE() FROM inserted;
END;
```

## Conceptos Clave

- 🔑 **Vistas**: Consultas reutilizables
- 🔑 **Stored Procedures**: Lógica almacenada
- 🔑 **Funciones**: Retornan valores
- 🔑 **Triggers**: Acciones automáticas

¡Automatiza y reutiliza tu código SQL! 🚀
