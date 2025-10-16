# Actividades Interactivas - Módulo 3: Funciones y JOINs

## Base de Datos de Práctica

```sql
CREATE DATABASE EmpresaPractica;
USE EmpresaPractica;

CREATE TABLE Departamentos (
    DepartamentoID INT PRIMARY KEY IDENTITY,
    Nombre NVARCHAR(100)
);

CREATE TABLE Empleados (
    EmpleadoID INT PRIMARY KEY IDENTITY,
    Nombre NVARCHAR(100),
    DepartamentoID INT,
    Salario DECIMAL(10,2),
    FechaContratacion DATE
);

INSERT INTO Departamentos VALUES ('Ventas'), ('TI'), ('RRHH'), ('Marketing');
INSERT INTO Empleados VALUES 
('Ana García', 1, 45000, '2020-01-15'),
('Carlos López', 2, 55000, '2019-06-10'),
('María Rodríguez', 1, 42000, '2021-03-20'),
('Luis Martínez', 3, 48000, '2018-09-05'),
('Laura Sánchez', NULL, 40000, '2022-01-10');
```

## Ejercicio 1: INNER JOIN básico
Muestra empleados con su departamento:
```sql


```

## Ejercicio 2: LEFT JOIN
Muestra todos los empleados, incluso sin departamento:
```sql


```

## Ejercicio 3: RIGHT JOIN
Muestra todos los departamentos, incluso sin empleados:
```sql


```

## Ejercicio 4: CASE Statement
Clasifica empleados por salario (Junior < 45000, Semi-Senior 45000-50000, Senior > 50000):
```sql


```

## Ejercicio 5: Función DATEDIFF
Calcula años trabajados de cada empleado:
```sql


```

¡Practica y revisa tus respuestas en retroalimentacion.md! 🎉
