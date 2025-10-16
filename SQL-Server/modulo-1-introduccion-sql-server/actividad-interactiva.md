# Actividades Interactivas - Módulo 1: Introducción a SQL Server

## Sección 1: Preguntas de Opción Múltiple

### Pregunta 1
**¿Qué es SQL Server?**

A) Un lenguaje de programación  
B) Un sistema de gestión de bases de datos relacionales  
C) Un navegador web  
D) Un sistema operativo  

---

### Pregunta 2
**¿Qué significa SQL?**

A) Server Query Language  
B) Structured Question Language  
C) Structured Query Language  
D) System Quality Language  

---

### Pregunta 3
**¿Cuál es la edición de SQL Server gratuita ideal para aprender?**

A) Enterprise  
B) Express  
C) Premium  
D) Professional  

---

### Pregunta 4
**¿Qué herramienta gráfica se usa para administrar SQL Server?**

A) Visual Studio Code  
B) Excel  
C) SQL Server Management Studio (SSMS)  
D) Notepad++  

---

### Pregunta 5
**¿Qué comando SQL se usa para crear una nueva base de datos?**

A) NEW DATABASE  
B) CREATE DATABASE  
C) MAKE DATABASE  
D) BUILD DATABASE  

---

### Pregunta 6
**¿Cuál de estas NO es una base de datos del sistema en SQL Server?**

A) master  
B) tempdb  
C) usuarios  
D) msdb  

---

### Pregunta 7
**¿Qué tipo de dato usarías para almacenar un nombre con acentos y caracteres especiales?**

A) VARCHAR  
B) CHAR  
C) NVARCHAR  
D) TEXT  

---

### Pregunta 8
**¿Qué hace la palabra clave IDENTITY(1,1)?**

A) Encripta los datos  
B) Auto-incrementa valores comenzando en 1  
C) Define un valor por defecto  
D) Crea una clave foránea  

---

## Sección 2: Verdadero o Falso

### Pregunta 9
**Una tabla en SQL Server es similar a una hoja de cálculo de Excel con filas y columnas.**

- [ ] Verdadero
- [ ] Falso

---

### Pregunta 10
**PRIMARY KEY permite tener valores duplicados en una tabla.**

- [ ] Verdadero
- [ ] Falso

---

### Pregunta 11
**Es obligatorio instalar SSMS para trabajar con SQL Server.**

- [ ] Verdadero
- [ ] Falso

---

### Pregunta 12
**INT es el tipo de dato adecuado para almacenar precios con decimales.**

- [ ] Verdadero
- [ ] Falso

---

### Pregunta 13
**La base de datos 'master' se puede eliminar si no la necesitas.**

- [ ] Verdadero
- [ ] Falso

---

### Pregunta 14
**NOT NULL significa que ese campo es obligatorio.**

- [ ] Verdadero
- [ ] Falso

---

## Sección 3: Completa el Código SQL

### Ejercicio 15
Completa el código para crear una base de datos llamada "Biblioteca":

```sql
______ ________ Biblioteca;
```

---

### Ejercicio 16
Completa el código para usar una base de datos:

```sql
____ MiBaseDatos;
```

---

### Ejercicio 17
Completa el código para crear una tabla "Libros" con un ID auto-incremental:

```sql
CREATE TABLE Libros (
    LibroID INT ________ ________ IDENTITY(1,1),
    Titulo NVARCHAR(200) NOT NULL,
    Autor NVARCHAR(100)
);
```

---

### Ejercicio 18
Completa el código para insertar un registro:

```sql
______ ______ Libros (Titulo, Autor)
VALUES ('Cien años de soledad', 'Gabriel García Márquez');
```

---

### Ejercicio 19
Completa el código para consultar todos los libros:

```sql
______ * FROM Libros;
```

---

## Sección 4: Encuentra el Error

### Ejercicio 20
¿Qué está mal en este código?

```sql
CREATE DATABASE Mi Base Datos;
```

**Error:** _______________________________________________

---

### Ejercicio 21
¿Qué está mal aquí?

```sql
CREATE TABLE Productos (
    ProductoID INT PRIMARY KEY,
    Nombre VARCHAR(100),
);
```

**Error:** _______________________________________________

---

### Ejercicio 22
¿Qué está mal en esta consulta?

```sql
SELECT Nombre Email FROM Clientes;
```

**Error:** _______________________________________________

---

## Sección 5: Asociación de Conceptos

Relaciona cada término con su definición:

### Términos:
1. PRIMARY KEY
2. NVARCHAR
3. IDENTITY
4. NOT NULL
5. SSMS
6. Tabla
7. Registro
8. Campo

### Definiciones:
A) Herramienta gráfica para administrar SQL Server  
B) Tipo de dato para texto con Unicode  
C) Estructura que almacena datos en filas y columnas  
D) Identificador único de cada fila  
E) Auto-incrementa valores numéricos  
F) Una fila en una tabla  
G) Campo obligatorio que no puede estar vacío  
H) Una columna en una tabla  

**Tus respuestas:**
1. _____
2. _____
3. _____
4. _____
5. _____
6. _____
7. _____
8. _____

---

## Sección 6: Ejercicios Prácticos

### Ejercicio 23: Crear Base de Datos de Tienda

Crea una base de datos llamada "MiTienda" y una tabla "Productos" con:
- ProductoID (INT, PRIMARY KEY, IDENTITY)
- Nombre (NVARCHAR(100), obligatorio)
- Precio (DECIMAL(10,2), obligatorio)
- Stock (INT, valor por defecto 0)

**Tu código aquí:**
```sql







```

---

### Ejercicio 24: Insertar Productos

Usando la tabla del ejercicio anterior, inserta 3 productos diferentes:
- Laptop, $899.99, 10 unidades
- Mouse, $25.50, 50 unidades
- Teclado, $45.00, 30 unidades

**Tu código aquí:**
```sql







```

---

### Ejercicio 25: Consultas Básicas

Escribe consultas para:
1. Ver todos los productos
2. Ver solo nombres y precios
3. Ver productos ordenados por precio (menor a mayor)

**Tu código aquí:**
```sql
-- Consulta 1:


-- Consulta 2:


-- Consulta 3:


```

---

### Ejercicio 26: Base de Datos de Escuela

Crea una base de datos "Escuela" con dos tablas:

**Tabla Profesores:**
- ProfesorID (INT, PRIMARY KEY, IDENTITY)
- Nombre (NVARCHAR(100), obligatorio)
- Especialidad (NVARCHAR(100))
- Email (NVARCHAR(100))

**Tabla Cursos:**
- CursoID (INT, PRIMARY KEY, IDENTITY)
- NombreCurso (NVARCHAR(150), obligatorio)
- Creditos (INT, obligatorio)
- ProfesorID (INT)

**Tu código aquí:**
```sql













```

---

## Sección 7: Desafío de Tipos de Datos

### Ejercicio 27
Para cada escenario, indica qué tipo de dato usarías:

**Escenario A: Edad de una persona**
Tipo de dato: _______________

**Escenario B: Descripción detallada de un producto (hasta 500 caracteres)**
Tipo de dato: _______________

**Escenario C: Precio de un artículo con centavos**
Tipo de dato: _______________

**Escenario D: Fecha de nacimiento**
Tipo de dato: _______________

**Escenario E: Estado activo/inactivo (solo dos opciones)**
Tipo de dato: _______________

**Escenario F: Código de producto único (GUID)**
Tipo de dato: _______________

**Escenario G: Hora de entrada de empleados**
Tipo de dato: _______________

---

## Sección 8: Pensamiento Crítico

### Pregunta 28
**¿Por qué es importante usar PRIMARY KEY en las tablas?**

_______________________________________________
_______________________________________________
_______________________________________________

---

### Pregunta 29
**Explica con tus propias palabras qué significa que una base de datos sea "relacional".**

_______________________________________________
_______________________________________________
_______________________________________________

---

### Pregunta 30
**¿Cuál es la diferencia entre VARCHAR y NVARCHAR? ¿Cuándo usarías cada uno?**

_______________________________________________
_______________________________________________
_______________________________________________

---

### Pregunta 31
**¿En qué situaciones de la vida real se usan bases de datos SQL Server?**

Nombra al menos 4 ejemplos:

1. _______________________________________________
2. _______________________________________________
3. _______________________________________________
4. _______________________________________________

---

## Sección 9: Proyecto Mini - Sistema de Biblioteca Personal

### Ejercicio 32: Biblioteca Personal

Crea un sistema completo para gestionar tu biblioteca personal:

**Requisitos:**

1. Base de datos llamada "MiBiblioteca"

2. Tabla "Libros" con:
   - LibroID (auto-incremental)
   - Titulo (obligatorio, hasta 200 caracteres)
   - Autor (obligatorio, hasta 100 caracteres)
   - AnioPublicacion (INT)
   - Genero (NVARCHAR(50))
   - Leido (BIT, por defecto 0/falso)
   - Calificacion (INT, del 1 al 5)

3. Inserta al menos 5 libros que conozcas o te gusten

4. Consultas:
   - Todos los libros que has leído
   - Libros ordenados por calificación (mayor a menor)
   - Libros de un género específico

**Tu código completo aquí:**
```sql
-- Crear base de datos


-- Usar la base de datos


-- Crear tabla


-- Insertar libros


-- Consulta 1: Libros leídos


-- Consulta 2: Ordenados por calificación


-- Consulta 3: Por género


```

---

## Sección 10: Desafío Extra ⭐

### Ejercicio 33: Investigación de Comandos

Investiga y explica qué hacen estos comandos (usa Google o la documentación):

**ALTER TABLE**
_______________________________________________
_______________________________________________

**DROP TABLE**
_______________________________________________
_______________________________________________

**TRUNCATE TABLE**
_______________________________________________
_______________________________________________

**sp_help**
_______________________________________________
_______________________________________________

---

### Ejercicio 34: Práctica Avanzada

Crea una base de datos "GestionEmpleados" con:

1. Tabla "Departamentos":
   - DepartamentoID (PRIMARY KEY, IDENTITY)
   - NombreDepartamento (NVARCHAR(100), obligatorio)
   - Presupuesto (DECIMAL(12,2))

2. Tabla "Empleados":
   - EmpleadoID (PRIMARY KEY, IDENTITY)
   - NombreCompleto (NVARCHAR(150), obligatorio)
   - Email (NVARCHAR(100))
   - Salario (DECIMAL(10,2))
   - FechaContratacion (DATE)
   - DepartamentoID (INT)
   - Activo (BIT, por defecto 1)

3. Inserta al menos 3 departamentos y 5 empleados

**Tu código aquí:**
```sql













```

---

## Autoevaluación

### ¿Cuántas preguntas/ejercicios completaste correctamente?

- Opción múltiple (1-8): ___ / 8
- Verdadero/Falso (9-14): ___ / 6
- Completar código (15-19): ___ / 5
- Encuentra el error (20-22): ___ / 3
- Asociación (23): ___ / 8
- Ejercicios prácticos (24-26): ___ / 3
- Tipos de datos (27): ___ / 7
- Pensamiento crítico (28-31): ___ / 4
- Proyecto mini (32): ___ / 1
- Extra (33-34): ___ / 2

**Total:** ___ / 47

### Reflexión

**Lo que mejor entendí:**
_______________________________________________
_______________________________________________

**Lo que necesito repasar:**
_______________________________________________
_______________________________________________

**Mi ejercicio favorito fue:**
_______________________________________________

---

**¡Excelente trabajo! Ahora revisa el archivo `retroalimentacion.md` para verificar tus respuestas y el archivo `progreso.md` para registrar tu avance. 🎉**
