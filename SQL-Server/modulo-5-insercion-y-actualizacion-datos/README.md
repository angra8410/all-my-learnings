# Módulo 5: Inserción y Actualización de Datos

## INSERT Avanzado

```sql
-- Insertar múltiples filas
INSERT INTO Productos (Nombre, Precio) VALUES
('Producto 1', 10.00),
('Producto 2', 20.00),
('Producto 3', 30.00);

-- INSERT FROM SELECT
INSERT INTO ProductosArchivo
SELECT * FROM Productos WHERE FechaIngreso < '2024-01-01';
```

## UPDATE - Actualizar Datos

```sql
-- Actualización simple
UPDATE Productos SET Precio = 25.99 WHERE ProductoID = 1;

-- Actualización con cálculo
UPDATE Productos SET Precio = Precio * 1.10;  -- Incremento 10%

-- UPDATE con JOIN
UPDATE P
SET P.Stock = P.Stock - V.Cantidad
FROM Productos P
INNER JOIN Ventas V ON P.ProductoID = V.ProductoID;
```

## DELETE - Eliminar Datos

```sql
-- Eliminar registros específicos
DELETE FROM Productos WHERE Stock = 0;

-- Eliminar con subconsulta
DELETE FROM Clientes
WHERE ClienteID IN (SELECT ClienteID FROM ClientesInactivos);
```

## MERGE - Combinar Operaciones

```sql
MERGE INTO ProductosDestino AS Target
USING ProductosOrigen AS Source
ON Target.ProductoID = Source.ProductoID
WHEN MATCHED THEN UPDATE SET Target.Precio = Source.Precio
WHEN NOT MATCHED THEN INSERT VALUES (Source.Nombre, Source.Precio);
```

## Transacciones

```sql
BEGIN TRANSACTION;
    UPDATE Cuentas SET Saldo = Saldo - 100 WHERE CuentaID = 1;
    UPDATE Cuentas SET Saldo = Saldo + 100 WHERE CuentaID = 2;
COMMIT;
-- O ROLLBACK en caso de error
```

¡Domina la modificación de datos con seguridad! 🚀
