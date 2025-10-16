# Módulo 1: Introducción a SQL Server

## ¿Qué es SQL Server?

Imagina que tienes una **biblioteca gigante** con millones de libros perfectamente organizados. SQL Server es como el sistema de gestión de esa biblioteca: te ayuda a guardar información de manera ordenada, encontrarla rápidamente y mantenerla segura.

**SQL Server** es un **Sistema de Gestión de Bases de Datos Relacionales (RDBMS)** creado por Microsoft. Es una herramienta poderosa que permite almacenar, organizar y recuperar información de forma eficiente y segura.

### ¿Por qué SQL Server es importante?

1. **Almacenamiento organizado**: Guarda grandes cantidades de datos de manera estructurada (tablas con filas y columnas)

2. **Rapidez**: Encuentra información entre millones de registros en milisegundos

3. **Seguridad**: Protege datos sensibles con sistemas de autenticación y permisos

4. **Confiabilidad**: Garantiza que tus datos estén seguros incluso si hay fallos de energía o hardware

5. **Usado en todas partes**: Desde pequeños negocios hasta grandes corporaciones como bancos, hospitales, tiendas online

### Ejemplo cotidiano: Tu Lista de Contactos

Piensa en la lista de contactos de tu teléfono:
- Cada contacto es una **fila** (registro)
- Nombre, teléfono, email son **columnas** (campos)
- Toda tu lista de contactos es una **tabla**
- Tu teléfono es como SQL Server: guarda, busca y actualiza contactos

Ahora imagina eso multiplicado por millones: eso es una base de datos empresarial.

## ¿Qué es una Base de Datos?

Una **base de datos** es una colección organizada de información relacionada. Es como tener varios archivadores organizados:

- **Tabla "Clientes"**: Información de tus clientes
- **Tabla "Productos"**: Catálogo de productos
- **Tabla "Pedidos"**: Registro de ventas
- **Tabla "Empleados"**: Datos del personal

### Componentes básicos:

1. **Tablas**: Donde se guarda la información (como hojas de Excel mejoradas)
2. **Filas (Registros)**: Cada elemento individual (un cliente, un producto)
3. **Columnas (Campos)**: Características de cada elemento (nombre, precio, fecha)
4. **Relaciones**: Conexiones entre tablas (qué cliente hizo qué pedido)

## ¿Qué es SQL?

**SQL** (Structured Query Language - Lenguaje de Consulta Estructurado) es el idioma que usas para "hablar" con SQL Server. Es como aprender inglés para comunicarte con alguien que solo habla inglés.

### Principales categorías de SQL:

1. **Consultas (SELECT)**: "Muéstrame información"
   ```sql
   SELECT nombre, email FROM Clientes;
   ```

2. **Inserción (INSERT)**: "Agrega algo nuevo"
   ```sql
   INSERT INTO Clientes (nombre, email) VALUES ('Juan Pérez', 'juan@email.com');
   ```

3. **Actualización (UPDATE)**: "Modifica algo existente"
   ```sql
   UPDATE Clientes SET email = 'nuevo@email.com' WHERE nombre = 'Juan Pérez';
   ```

4. **Eliminación (DELETE)**: "Borra algo"
   ```sql
   DELETE FROM Clientes WHERE nombre = 'Juan Pérez';
   ```

## Versiones y Ediciones de SQL Server

SQL Server viene en diferentes versiones y ediciones para diferentes necesidades:

### Versiones principales:
- **SQL Server 2019**: Versión estable y ampliamente usada
- **SQL Server 2022**: La más reciente con nuevas características

### Ediciones:
- **Express**: ✅ Gratuita, ideal para aprender y proyectos pequeños
- **Developer**: ✅ Gratuita, todas las características para desarrollo
- **Standard**: 💰 Para empresas medianas
- **Enterprise**: 💰💰 Para grandes corporaciones

**Para este curso usaremos SQL Server Express o Developer (ambas gratuitas).**

## Instalación de SQL Server

### Opción 1: SQL Server Express (Recomendado para principiantes)

1. **Descargar**: Ve a [microsoft.com/sql-server/sql-server-downloads](https://www.microsoft.com/sql-server/sql-server-downloads)

2. **Instalar**: 
   - Descarga "Express Edition"
   - Ejecuta el instalador
   - Selecciona "Basic" para instalación rápida
   - Anota el nombre de tu servidor (ej: `localhost\SQLEXPRESS`)

3. **Verificar instalación**:
   - Abre SQL Server Management Studio (SSMS)
   - Conéctate al servidor
   - ¡Listo!

### SQL Server Management Studio (SSMS)

**SSMS** es la herramienta gráfica para trabajar con SQL Server. Es como tu "tablero de control":
- Escribes y ejecutas consultas
- Ves y editas datos
- Administras bases de datos
- Creas tablas, vistas, procedimientos

**Instalación de SSMS**:
1. Descarga desde [docs.microsoft.com/sql/ssms/download](https://docs.microsoft.com/sql/ssms/download-sql-server-management-studio-ssms)
2. Instala (proceso simple)
3. Abre y conecta a tu servidor SQL

## Conceptos Fundamentales

### 1. Servidor y Cliente

```
┌─────────────────┐
│    CLIENTE      │
│  (SSMS, App)    │
└────────┬────────┘
         │ 
         │ Envía comandos SQL
         │
         ▼
┌─────────────────┐
│  SQL SERVER     │
│  (Servidor BD)  │
│  - Ejecuta SQL  │
│  - Guarda datos │
│  - Devuelve     │
│    resultados   │
└─────────────────┘
```

### 2. Bases de Datos del Sistema

Cuando instalas SQL Server, vienen bases de datos predefinidas:
- **master**: Información del servidor (¡no tocar!)
- **model**: Plantilla para nuevas bases de datos
- **msdb**: Para tareas programadas
- **tempdb**: Para datos temporales

### 3. Tu Primera Base de Datos

```sql
-- Crear una base de datos
CREATE DATABASE MiPrimeraBaseDatos;

-- Usar la base de datos
USE MiPrimeraBaseDatos;

-- Ver todas las bases de datos
SELECT name FROM sys.databases;
```

## Primeros Pasos Prácticos

### Ejercicio 1: Conectarte al Servidor

1. Abre SQL Server Management Studio (SSMS)
2. En "Server name" escribe tu servidor (ej: `localhost\SQLEXPRESS`)
3. Autenticación: "Windows Authentication"
4. Click en "Connect"

¡Listo! Ya estás dentro.

### Ejercicio 2: Crear tu Primera Base de Datos

```sql
-- Crear base de datos para práctica
CREATE DATABASE EscuelaPractica;

-- Cambiar a esa base de datos
USE EscuelaPractica;

-- Verificar que estás en la base correcta
SELECT DB_NAME() AS BaseDatosActual;
```

### Ejercicio 3: Crear tu Primera Tabla

```sql
-- Crear tabla de Estudiantes
CREATE TABLE Estudiantes (
    EstudianteID INT PRIMARY KEY IDENTITY(1,1),
    Nombre NVARCHAR(100) NOT NULL,
    Email NVARCHAR(100),
    FechaNacimiento DATE,
    Activo BIT DEFAULT 1
);

-- Ver estructura de la tabla
EXEC sp_help 'Estudiantes';
```

### Ejercicio 4: Insertar Datos

```sql
-- Agregar estudiantes
INSERT INTO Estudiantes (Nombre, Email, FechaNacimiento)
VALUES ('Ana García', 'ana@email.com', '2000-05-15');

INSERT INTO Estudiantes (Nombre, Email, FechaNacimiento)
VALUES ('Carlos López', 'carlos@email.com', '1999-08-22');

INSERT INTO Estudiantes (Nombre, Email, FechaNacimiento)
VALUES ('María Rodríguez', 'maria@email.com', '2001-03-10');
```

### Ejercicio 5: Consultar Datos

```sql
-- Ver todos los estudiantes
SELECT * FROM Estudiantes;

-- Ver solo nombres y emails
SELECT Nombre, Email FROM Estudiantes;

-- Ver estudiantes ordenados por nombre
SELECT * FROM Estudiantes ORDER BY Nombre;
```

## Tipos de Datos Básicos

### Numéricos:
- **INT**: Números enteros (-2,147,483,648 a 2,147,483,647)
- **BIGINT**: Números enteros grandes
- **DECIMAL(p,s)**: Números con decimales fijos (ej: `DECIMAL(10,2)` para precios)
- **FLOAT**: Números con decimales variables

### Texto:
- **VARCHAR(n)**: Texto de longitud variable (ASCII)
- **NVARCHAR(n)**: Texto de longitud variable (Unicode - soporta ñ, acentos)
- **CHAR(n)**: Texto de longitud fija
- **TEXT**: Texto largo (obsoleto, usar VARCHAR(MAX))

### Fecha y Hora:
- **DATE**: Solo fecha (2024-01-15)
- **TIME**: Solo hora (14:30:00)
- **DATETIME**: Fecha y hora completas
- **DATETIME2**: Versión mejorada de DATETIME

### Otros:
- **BIT**: Verdadero/Falso (1/0)
- **UNIQUEIDENTIFIER**: GUID/UUID únicos
- **VARBINARY**: Datos binarios (imágenes, archivos)

## Mejores Prácticas

### 1. Nomenclatura clara
```sql
✅ BIEN:
CREATE TABLE Clientes (
    ClienteID INT,
    NombreCompleto NVARCHAR(100),
    FechaRegistro DATE
);

❌ MAL:
CREATE TABLE tbl1 (
    id INT,
    nm NVARCHAR(100),
    dt DATE
);
```

### 2. Usa PRIMARY KEY siempre
```sql
-- Toda tabla debe tener una clave primaria
CREATE TABLE Productos (
    ProductoID INT PRIMARY KEY IDENTITY(1,1),
    NombreProducto NVARCHAR(100)
);
```

### 3. Define NOT NULL cuando sea necesario
```sql
CREATE TABLE Empleados (
    EmpleadoID INT PRIMARY KEY,
    Nombre NVARCHAR(100) NOT NULL,  -- Obligatorio
    Telefono NVARCHAR(20)           -- Opcional
);
```

### 4. Usa IDENTITY para IDs auto-incrementales
```sql
CREATE TABLE Pedidos (
    PedidoID INT PRIMARY KEY IDENTITY(1,1),  -- Auto-incrementa: 1, 2, 3...
    ClienteID INT,
    FechaPedido DATE
);
```

### 5. Comenta tu código
```sql
-- Crear tabla para almacenar información de productos
CREATE TABLE Productos (
    ProductoID INT PRIMARY KEY IDENTITY(1,1),  -- ID único auto-incremental
    Nombre NVARCHAR(100) NOT NULL,             -- Nombre del producto
    Precio DECIMAL(10,2) NOT NULL,             -- Precio con 2 decimales
    Stock INT DEFAULT 0                         -- Cantidad en inventario
);
```

## Navegando en SSMS

### Panel de Objetos (Object Explorer):
```
Databases
  ├── System Databases
  │   ├── master
  │   ├── model
  │   ├── msdb
  │   └── tempdb
  └── (Tus bases de datos)
      ├── EscuelaPractica
      │   ├── Tables
      │   │   └── dbo.Estudiantes
      │   ├── Views
      │   ├── Stored Procedures
      │   └── Functions
```

### Atajos útiles:
- **Ctrl + N**: Nueva consulta
- **F5 o Ctrl + E**: Ejecutar consulta
- **Ctrl + R**: Mostrar/Ocultar panel de resultados
- **Ctrl + Shift + R**: Actualizar IntelliSense

## Glosario de Términos

| Término | Definición | Ejemplo |
|---------|------------|---------|
| **RDBMS** | Sistema de Gestión de Bases de Datos Relacionales | SQL Server, MySQL, PostgreSQL |
| **Tabla** | Estructura que almacena datos en filas y columnas | Tabla "Clientes" |
| **Fila (Registro)** | Una entrada individual en una tabla | Un cliente específico |
| **Columna (Campo)** | Una característica de los registros | Nombre, Email, Edad |
| **Primary Key** | Identificador único de cada fila | ClienteID |
| **Query** | Consulta SQL para obtener o modificar datos | SELECT * FROM Clientes |
| **SSMS** | SQL Server Management Studio | Herramienta gráfica de administración |

## Conceptos Clave para Recordar

- 🔑 **SQL Server**: Sistema de gestión de bases de datos de Microsoft
- 🔑 **Base de Datos**: Colección organizada de tablas relacionadas
- 🔑 **Tabla**: Estructura con filas y columnas que almacena datos
- 🔑 **SQL**: Lenguaje para comunicarse con la base de datos
- 🔑 **SSMS**: Herramienta visual para trabajar con SQL Server
- 🔑 **Primary Key**: Identificador único de cada registro
- 🔑 **IDENTITY**: Auto-incrementa valores numéricos

## Próximos Pasos

En el **Módulo 2** aprenderás:
- SELECT con filtros (WHERE)
- Ordenar resultados (ORDER BY)
- Agrupar datos (GROUP BY)
- Funciones agregadas (COUNT, SUM, AVG)
- Operadores lógicos (AND, OR, NOT)

### ¿Qué necesitas saber antes de continuar?

✅ Cómo conectarte a SQL Server  
✅ Cómo crear una base de datos  
✅ Cómo crear una tabla básica  
✅ Cómo insertar y consultar datos  
✅ Tipos de datos principales  

## Motivación Final

> "La información es el petróleo del siglo XXI, y las bases de datos son los pozos." - Anónimo

Has dado tu primer paso en el mundo de las bases de datos. SQL Server es usado por millones de empresas en todo el mundo. Cada vez que compras en línea, reservas un vuelo, o usas una app, hay bases de datos trabajando detrás.

**Recuerda:**
- No necesitas memorizar toda la sintaxis
- Los errores son oportunidades de aprendizaje
- La práctica constante es clave
- Google y la documentación son tus aliados
- La comunidad SQL siempre está dispuesta a ayudar

**Tu desafío:**
Crea una base de datos llamada "MiNegocio" con una tabla "Productos" que tenga: ID, Nombre, Precio y Stock. Inserta 5 productos y consulta todos los datos.

¡Nos vemos en el Módulo 2! 🚀💾
