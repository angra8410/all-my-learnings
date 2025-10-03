# Retroalimentación y Soluciones - Módulo 5: Persistencia de Datos

## Respuestas

### Pregunta 1: ¿Qué es Entity Framework Core?
**Respuesta correcta: B) Un ORM que mapea objetos a bases de datos**

**Explicación**: EF Core es un Object-Relational Mapper que permite trabajar con bases de datos usando objetos C# en lugar de SQL.

### Pregunta 2: ¿Qué es un DbContext?
**Respuesta correcta: B) El puente entre tu aplicación y la base de datos**

**Explicación**: DbContext coordina todas las interacciones con la base de datos y gestiona las entidades.

### Pregunta 3: ¿Qué comando crea una migración?
**Respuesta correcta: B) `dotnet ef migrations add NombreMigracion`**

**Explicación**: Este comando genera archivos de migración basados en cambios en tus modelos.

### Pregunta 4: ¿Para qué sirve `SaveChangesAsync()`?
**Respuesta correcta: B) Para guardar cambios en la base de datos**

**Explicación**: Persiste todos los cambios rastreados por el DbContext en la base de datos.

### Pregunta 5: ¿Qué hace `Include()` en una consulta?
**Respuesta correcta: B) Carga relaciones (eager loading)**

**Explicación**: Include carga entidades relacionadas en la misma consulta, evitando el problema N+1.

---

## Preparación para el Siguiente Módulo

✅ Tener EF Core configurado  
✅ Haber creado y aplicado migraciones  
✅ Entender async/await  

¡Ahora tienes persistencia real! 🗄️
