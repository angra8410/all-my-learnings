# Retroalimentación y Soluciones - Módulo 1: Introducción a SQL Server

## Sección 1: Respuestas a Preguntas de Opción Múltiple

### Pregunta 1: ¿Qué es SQL Server?
**Respuesta correcta: B) Un sistema de gestión de bases de datos relacionales**

**Explicación**: SQL Server es un RDBMS (Relational Database Management System) creado por Microsoft. No es un lenguaje de programación (eso es SQL), ni un navegador, ni un sistema operativo.

---

### Pregunta 2: ¿Qué significa SQL?
**Respuesta correcta: C) Structured Query Language**

**Explicación**: SQL significa "Lenguaje de Consulta Estructurado". Es el lenguaje estándar para comunicarse con bases de datos relacionales.

---

### Pregunta 3: ¿Cuál es la edición de SQL Server gratuita ideal para aprender?
**Respuesta correcta: B) Express**

**Explicación**: SQL Server Express es completamente gratuito y perfecto para aprender. Developer también es gratuito y tiene más características, pero Express es más ligero y fácil de instalar para principiantes.

---

### Pregunta 4: ¿Qué herramienta gráfica se usa para administrar SQL Server?
**Respuesta correcta: C) SQL Server Management Studio (SSMS)**

**Explicación**: SSMS es la herramienta oficial de Microsoft para administrar SQL Server. Ofrece una interfaz gráfica completa para escribir consultas, diseñar tablas y gestionar bases de datos.

---

### Pregunta 5: ¿Qué comando SQL se usa para crear una nueva base de datos?
**Respuesta correcta: B) CREATE DATABASE**

**Explicación**: CREATE DATABASE es el comando estándar en SQL para crear una nueva base de datos. Ejemplo: `CREATE DATABASE MiBaseDatos;`

---

### Pregunta 6: ¿Cuál de estas NO es una base de datos del sistema en SQL Server?
**Respuesta correcta: C) usuarios**

**Explicación**: Las bases de datos del sistema son: master, model, msdb y tempdb. "usuarios" no es una base de datos del sistema; es donde guardarías tus propias bases de datos.

---

### Pregunta 7: ¿Qué tipo de dato usarías para almacenar un nombre con acentos y caracteres especiales?
**Respuesta correcta: C) NVARCHAR**

**Explicación**: NVARCHAR soporta Unicode, lo que permite almacenar caracteres especiales como ñ, acentos (á, é, í), y caracteres de otros idiomas. VARCHAR solo soporta ASCII básico.

---

### Pregunta 8: ¿Qué hace la palabra clave IDENTITY(1,1)?
**Respuesta correcta: B) Auto-incrementa valores comenzando en 1**

**Explicación**: IDENTITY(1,1) hace que SQL Server genere automáticamente valores únicos comenzando en 1 y aumentando de 1 en 1 (1, 2, 3, 4...). Es ideal para claves primarias.

---

## Sección 2: Respuestas Verdadero o Falso

### Pregunta 9: Una tabla en SQL Server es similar a una hoja de cálculo de Excel con filas y columnas
**Respuesta correcta: Verdadero**

**Explicación**: Visualmente, una tabla es muy similar a Excel: tiene filas (registros) y columnas (campos). La diferencia principal es que SQL Server es mucho más poderoso, maneja millones de registros y tiene características avanzadas como índices, relaciones y transacciones.

---

### Pregunta 10: PRIMARY KEY permite tener valores duplicados en una tabla
**Respuesta correcta: Falso**

**Explicación**: PRIMARY KEY garantiza que cada valor sea único y no nulo. Es el identificador único de cada fila. No puede haber dos filas con el mismo PRIMARY KEY.

---

### Pregunta 11: Es obligatorio instalar SSMS para trabajar con SQL Server
**Respuesta correcta: Falso**

**Explicación**: Aunque SSMS es la herramienta más popular y recomendada, no es obligatorio. Puedes usar otras herramientas como Azure Data Studio, Visual Studio Code con extensiones, o incluso línea de comandos (sqlcmd).

---

### Pregunta 12: INT es el tipo de dato adecuado para almacenar precios con decimales
**Respuesta correcta: Falso**

**Explicación**: INT solo almacena números enteros sin decimales. Para precios con centavos, debes usar DECIMAL o NUMERIC. Ejemplo: `DECIMAL(10,2)` permite números hasta 99,999,999.99.

---

### Pregunta 13: La base de datos 'master' se puede eliminar si no la necesitas
**Respuesta correcta: Falso**

**Explicación**: ¡NUNCA elimines la base de datos 'master'! Es crítica para el funcionamiento de SQL Server. Contiene información vital del sistema. Eliminarla haría que SQL Server no funcione.

---

### Pregunta 14: NOT NULL significa que ese campo es obligatorio
**Respuesta correcta: Verdadero**

**Explicación**: NOT NULL indica que el campo no puede estar vacío. Debes proporcionar un valor al insertar o actualizar datos. Es útil para campos críticos como nombres, emails, fechas importantes.

---

## Sección 3: Código Completado

### Ejercicio 15: Crear base de datos
```sql
CREATE DATABASE Biblioteca;
```

---

### Ejercicio 16: Usar base de datos
```sql
USE MiBaseDatos;
```

---

### Ejercicio 17: Crear tabla con PRIMARY KEY IDENTITY
```sql
CREATE TABLE Libros (
    LibroID INT PRIMARY KEY IDENTITY(1,1),
    Titulo NVARCHAR(200) NOT NULL,
    Autor NVARCHAR(100)
);
```

---

### Ejercicio 18: Insertar registro
```sql
INSERT INTO Libros (Titulo, Autor)
VALUES ('Cien años de soledad', 'Gabriel García Márquez');
```

---

### Ejercicio 19: Consultar todos los libros
```sql
SELECT * FROM Libros;
```

---

## Sección 4: Errores Corregidos

### Ejercicio 20: Error en nombre de base de datos
**Código con error:**
```sql
CREATE DATABASE Mi Base Datos;
```

**Error**: Los nombres de bases de datos no pueden tener espacios sin corchetes.

**Corrección:**
```sql
CREATE DATABASE MiBaseDatos;
-- o
CREATE DATABASE [Mi Base Datos];  -- Con corchetes si quieres espacios
```

---

### Ejercicio 21: Error de coma extra
**Código con error:**
```sql
CREATE TABLE Productos (
    ProductoID INT PRIMARY KEY,
    Nombre VARCHAR(100),
);  -- Coma extra antes del paréntesis de cierre
```

**Error**: Hay una coma después del último campo. SQL Server no permite esto.

**Corrección:**
```sql
CREATE TABLE Productos (
    ProductoID INT PRIMARY KEY,
    Nombre VARCHAR(100)  -- Sin coma al final
);
```

---

### Ejercicio 22: Error de sintaxis en SELECT
**Código con error:**
```sql
SELECT Nombre Email FROM Clientes;
```

**Error**: Falta la coma entre los nombres de las columnas.

**Corrección:**
```sql
SELECT Nombre, Email FROM Clientes;
```

---

## Sección 5: Asociación de Conceptos - Respuestas

1. PRIMARY KEY → **D)** Identificador único de cada fila
2. NVARCHAR → **B)** Tipo de dato para texto con Unicode
3. IDENTITY → **E)** Auto-incrementa valores numéricos
4. NOT NULL → **G)** Campo obligatorio que no puede estar vacío
5. SSMS → **A)** Herramienta gráfica para administrar SQL Server
6. Tabla → **C)** Estructura que almacena datos en filas y columnas
7. Registro → **F)** Una fila en una tabla
8. Campo → **H)** Una columna en una tabla

---

## Sección 6: Ejercicios Prácticos - Soluciones

### Ejercicio 23: Crear Base de Datos de Tienda

```sql
-- Crear la base de datos
CREATE DATABASE MiTienda;

-- Usar la base de datos
USE MiTienda;

-- Crear la tabla Productos
CREATE TABLE Productos (
    ProductoID INT PRIMARY KEY IDENTITY(1,1),
    Nombre NVARCHAR(100) NOT NULL,
    Precio DECIMAL(10,2) NOT NULL,
    Stock INT DEFAULT 0
);
```

---

### Ejercicio 24: Insertar Productos

```sql
INSERT INTO Productos (Nombre, Precio, Stock)
VALUES ('Laptop', 899.99, 10);

INSERT INTO Productos (Nombre, Precio, Stock)
VALUES ('Mouse', 25.50, 50);

INSERT INTO Productos (Nombre, Precio, Stock)
VALUES ('Teclado', 45.00, 30);

-- También se puede hacer en una sola instrucción:
INSERT INTO Productos (Nombre, Precio, Stock)
VALUES 
    ('Laptop', 899.99, 10),
    ('Mouse', 25.50, 50),
    ('Teclado', 45.00, 30);
```

---

### Ejercicio 25: Consultas Básicas

```sql
-- Consulta 1: Ver todos los productos
SELECT * FROM Productos;

-- Consulta 2: Ver solo nombres y precios
SELECT Nombre, Precio FROM Productos;

-- Consulta 3: Ver productos ordenados por precio (menor a mayor)
SELECT * FROM Productos ORDER BY Precio ASC;
-- O simplemente:
SELECT * FROM Productos ORDER BY Precio;  -- ASC es por defecto
```

---

### Ejercicio 26: Base de Datos de Escuela

```sql
-- Crear base de datos
CREATE DATABASE Escuela;
USE Escuela;

-- Crear tabla Profesores
CREATE TABLE Profesores (
    ProfesorID INT PRIMARY KEY IDENTITY(1,1),
    Nombre NVARCHAR(100) NOT NULL,
    Especialidad NVARCHAR(100),
    Email NVARCHAR(100)
);

-- Crear tabla Cursos
CREATE TABLE Cursos (
    CursoID INT PRIMARY KEY IDENTITY(1,1),
    NombreCurso NVARCHAR(150) NOT NULL,
    Creditos INT NOT NULL,
    ProfesorID INT
);
```

---

## Sección 7: Desafío de Tipos de Datos - Respuestas

**Escenario A: Edad de una persona**
Tipo de dato: **INT** o **TINYINT** (para edades 0-255)

**Escenario B: Descripción detallada de un producto (hasta 500 caracteres)**
Tipo de dato: **NVARCHAR(500)**

**Escenario C: Precio de un artículo con centavos**
Tipo de dato: **DECIMAL(10,2)** o **MONEY**

**Escenario D: Fecha de nacimiento**
Tipo de dato: **DATE**

**Escenario E: Estado activo/inactivo (solo dos opciones)**
Tipo de dato: **BIT** (1 = activo, 0 = inactivo)

**Escenario F: Código de producto único (GUID)**
Tipo de dato: **UNIQUEIDENTIFIER**

**Escenario G: Hora de entrada de empleados**
Tipo de dato: **TIME** o **DATETIME**

---

## Sección 8: Pensamiento Crítico - Respuestas Sugeridas

### Pregunta 28: ¿Por qué es importante usar PRIMARY KEY en las tablas?

**Respuesta sugerida:**
PRIMARY KEY es importante porque:
1. **Identifica únicamente cada fila**: Garantiza que no haya registros duplicados
2. **Mejora el rendimiento**: SQL Server crea automáticamente un índice en la PRIMARY KEY, haciendo las búsquedas mucho más rápidas
3. **Permite relaciones**: Es necesaria para relacionar tablas entre sí
4. **Integridad de datos**: Asegura que siempre puedas referenciar un registro específico de forma confiable

---

### Pregunta 29: Explica con tus propias palabras qué significa que una base de datos sea "relacional"

**Respuesta sugerida:**
Una base de datos relacional significa que las tablas pueden estar conectadas o "relacionadas" entre sí mediante campos comunes. Por ejemplo, una tabla de "Clientes" se puede relacionar con una tabla de "Pedidos" usando el ClienteID. Esto evita duplicar información y mantiene los datos organizados y consistentes. Es como tener fichas de archivo conectadas por hilos invisibles.

---

### Pregunta 30: ¿Cuál es la diferencia entre VARCHAR y NVARCHAR? ¿Cuándo usarías cada uno?

**Respuesta sugerida:**
- **VARCHAR**: Almacena caracteres ASCII (inglés básico). Usa 1 byte por carácter. Ideal para emails, códigos, nombres en inglés sin acentos.
- **NVARCHAR**: Almacena Unicode (todos los idiomas). Usa 2 bytes por carácter. Necesario para español (ñ, acentos), chino, árabe, emojis.

**Cuándo usar cada uno:**
- VARCHAR: Campos en inglés sin caracteres especiales (ej: códigos de producto "PROD001")
- NVARCHAR: Campos en español o multiidioma (ej: nombres "José García")

---

### Pregunta 31: ¿En qué situaciones de la vida real se usan bases de datos SQL Server?

**Respuestas ejemplo:**

1. **Bancos**: Gestión de cuentas, transacciones, préstamos
2. **Hospitales**: Historiales médicos, citas, inventario de medicamentos
3. **Tiendas online**: Catálogo de productos, carritos de compra, pedidos
4. **Empresas**: Nómina, recursos humanos, inventarios
5. **Escuelas**: Registro de estudiantes, calificaciones, horarios
6. **Gobierno**: Registros civiles, impuestos, licencias
7. **Redes sociales**: Perfiles de usuarios, publicaciones, mensajes
8. **Aerolíneas**: Reservas de vuelos, pasajeros, rutas

---

## Sección 9: Proyecto Mini - Solución Completa

### Ejercicio 32: Biblioteca Personal

```sql
-- Crear base de datos
CREATE DATABASE MiBiblioteca;
GO

-- Usar la base de datos
USE MiBiblioteca;
GO

-- Crear tabla Libros
CREATE TABLE Libros (
    LibroID INT PRIMARY KEY IDENTITY(1,1),
    Titulo NVARCHAR(200) NOT NULL,
    Autor NVARCHAR(100) NOT NULL,
    AnioPublicacion INT,
    Genero NVARCHAR(50),
    Leido BIT DEFAULT 0,
    Calificacion INT
);
GO

-- Insertar libros (5 ejemplos)
INSERT INTO Libros (Titulo, Autor, AnioPublicacion, Genero, Leido, Calificacion)
VALUES 
    ('Cien años de soledad', 'Gabriel García Márquez', 1967, 'Realismo mágico', 1, 5),
    ('1984', 'George Orwell', 1949, 'Ciencia ficción', 1, 5),
    ('El código Da Vinci', 'Dan Brown', 2003, 'Thriller', 1, 4),
    ('Fundación', 'Isaac Asimov', 1951, 'Ciencia ficción', 0, NULL),
    ('Don Quijote de la Mancha', 'Miguel de Cervantes', 1605, 'Clásico', 1, 3);
GO

-- Consulta 1: Todos los libros que has leído
SELECT * FROM Libros WHERE Leido = 1;

-- Consulta 2: Libros ordenados por calificación (mayor a menor)
SELECT * FROM Libros 
WHERE Calificacion IS NOT NULL 
ORDER BY Calificacion DESC;

-- Consulta 3: Libros de un género específico
SELECT * FROM Libros WHERE Genero = 'Ciencia ficción';
```

---

## Sección 10: Desafío Extra - Respuestas

### Ejercicio 33: Investigación de Comandos

**ALTER TABLE**
Modifica la estructura de una tabla existente. Permite agregar, eliminar o modificar columnas sin perder los datos existentes.
```sql
ALTER TABLE Productos ADD Descripcion NVARCHAR(500);
```

**DROP TABLE**
Elimina completamente una tabla y todos sus datos. ¡Usar con precaución! No hay vuelta atrás.
```sql
DROP TABLE ProductosViejos;
```

**TRUNCATE TABLE**
Elimina todos los registros de una tabla pero mantiene la estructura. Más rápido que DELETE porque no registra cada eliminación individualmente.
```sql
TRUNCATE TABLE LogsTemporales;
```

**sp_help**
Procedimiento almacenado del sistema que muestra información detallada sobre un objeto de base de datos (tabla, vista, etc.): columnas, tipos de datos, índices.
```sql
EXEC sp_help 'Productos';
```

---

### Ejercicio 34: Práctica Avanzada - Solución

```sql
-- Crear base de datos
CREATE DATABASE GestionEmpleados;
GO

USE GestionEmpleados;
GO

-- Crear tabla Departamentos
CREATE TABLE Departamentos (
    DepartamentoID INT PRIMARY KEY IDENTITY(1,1),
    NombreDepartamento NVARCHAR(100) NOT NULL,
    Presupuesto DECIMAL(12,2)
);
GO

-- Crear tabla Empleados
CREATE TABLE Empleados (
    EmpleadoID INT PRIMARY KEY IDENTITY(1,1),
    NombreCompleto NVARCHAR(150) NOT NULL,
    Email NVARCHAR(100),
    Salario DECIMAL(10,2),
    FechaContratacion DATE,
    DepartamentoID INT,
    Activo BIT DEFAULT 1
);
GO

-- Insertar departamentos
INSERT INTO Departamentos (NombreDepartamento, Presupuesto)
VALUES 
    ('Tecnología', 500000.00),
    ('Ventas', 300000.00),
    ('Recursos Humanos', 150000.00);
GO

-- Insertar empleados
INSERT INTO Empleados (NombreCompleto, Email, Salario, FechaContratacion, DepartamentoID)
VALUES 
    ('Ana García López', 'ana.garcia@empresa.com', 45000.00, '2020-03-15', 1),
    ('Carlos Rodríguez Pérez', 'carlos.rodriguez@empresa.com', 38000.00, '2021-06-01', 2),
    ('María Fernández Silva', 'maria.fernandez@empresa.com', 42000.00, '2019-09-20', 1),
    ('Luis Martínez Gómez', 'luis.martinez@empresa.com', 35000.00, '2022-01-10', 2),
    ('Laura Sánchez Torres', 'laura.sanchez@empresa.com', 40000.00, '2020-11-05', 3);
GO

-- Consultas de verificación
SELECT * FROM Departamentos;
SELECT * FROM Empleados;
```

---

## Resumen de Conceptos Clave

### Comandos Principales Aprendidos:
- ✅ CREATE DATABASE - Crear base de datos
- ✅ USE - Seleccionar base de datos activa
- ✅ CREATE TABLE - Crear tabla
- ✅ INSERT INTO - Insertar datos
- ✅ SELECT - Consultar datos
- ✅ ORDER BY - Ordenar resultados

### Tipos de Datos Principales:
- ✅ INT - Números enteros
- ✅ NVARCHAR - Texto con Unicode
- ✅ DECIMAL - Números con decimales
- ✅ DATE - Fechas
- ✅ BIT - Verdadero/Falso

### Conceptos Importantes:
- ✅ PRIMARY KEY - Identificador único
- ✅ IDENTITY - Auto-incremento
- ✅ NOT NULL - Campo obligatorio
- ✅ DEFAULT - Valor por defecto

---

**¡Felicidades por completar el Módulo 1! Ahora tienes las bases sólidas de SQL Server. Sigue practicando y nos vemos en el Módulo 2. 🚀💾**
