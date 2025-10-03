# Retroalimentación y Soluciones - Módulo 4: Rutas, Controladores y Modelos

## Sección 1: Respuestas a Preguntas de Opción Múltiple

### Pregunta 1: ¿Qué significa `[Route("api/[controller]")]`?
**Respuesta correcta: B) El [controller] se reemplaza por el nombre del controlador**

**Explicación**: ASP.NET Core reemplaza automáticamente `[controller]` por el nombre de la clase sin el sufijo "Controller". Por ejemplo, `ProductosController` se convierte en `/api/productos`.

### Pregunta 2: ¿Qué código de estado devuelve `CreatedAtAction`?
**Respuesta correcta: B) 201 Created**

**Explicación**: `CreatedAtAction` devuelve código 201 indicando que se creó un nuevo recurso, e incluye el header `Location` con la URL del nuevo recurso.

### Pregunta 3: ¿Qué es un DTO (Data Transfer Object)?**
**Respuesta correcta: B) Un objeto diseñado para transferir datos entre capas**

**Explicación**: Los DTOs son objetos que definen exactamente qué datos se transfieren, permitiendo controlar la información expuesta y usar diferentes estructuras para entrada y salida.

### Pregunta 4: ¿Cuál es la diferencia entre PUT y PATCH?**
**Respuesta correcta: B) PUT actualiza completamente, PATCH parcialmente**

**Explicación**: PUT reemplaza todo el recurso, mientras que PATCH solo modifica los campos especificados.

### Pregunta 5: ¿Qué hace `[FromBody]` en un parámetro?**
**Respuesta correcta: B) Obtiene datos del cuerpo de la petición**

**Explicación**: `[FromBody]` indica que los datos vienen en el cuerpo de la petición HTTP, típicamente en formato JSON.

### Pregunta 6: ¿Qué devuelve `NoContent()`?**
**Respuesta correcta: C) 204 No Content**

**Explicación**: `NoContent()` devuelve código 204, indicando éxito pero sin cuerpo de respuesta, común en actualizaciones y eliminaciones.

### Pregunta 7: ¿Cómo defines parámetros opcionales en query string?**
**Respuesta correcta: B) Con valores por defecto en los parámetros**

**Explicación**: Asignar un valor por defecto hace el parámetro opcional: `int pagina = 1`.

### Pregunta 8: ¿Qué hace `{id:int:min(1)}`?**
**Respuesta correcta: B) Requiere que id sea entero mayor o igual a 1**

**Explicación**: Las restricciones de ruta validan el formato y rango de parámetros directamente en la ruta.

---

## Evaluación de tu Desempeño

### Si acertaste 90% o más: 🌟 ¡Excelente!
Dominas las rutas, verbos HTTP y DTOs. Estás listo para trabajar con bases de datos.

**Próximos pasos:**
- Implementa un CRUD completo con DTOs
- Explora restricciones de ruta avanzadas
- Prepárate para Entity Framework Core

### Si acertaste entre 70% y 89%: 💪 ¡Muy bien!
Comprendes los conceptos fundamentales, solo necesitas más práctica.

**Recomendaciones:**
- Practica implementando POST, PUT y DELETE
- Crea DTOs para tus modelos
- Experimenta con diferentes rutas

### Si acertaste menos de 70%: 📚 Sigue adelante
Necesitas repasar los conceptos fundamentales.

**Recomendaciones:**
- Repasa la diferencia entre verbos HTTP
- Practica creando endpoints uno por uno
- No avances sin tener un CRUD básico funcionando

---

## Preparación para el Siguiente Módulo

Antes de avanzar al Módulo 5 (Persistencia de Datos), asegúrate de:

✅ Implementar GET, POST, PUT y DELETE  
✅ Entender qué son los DTOs  
✅ Saber usar `[FromBody]` y `[FromQuery]`  
✅ Conocer los códigos de estado correctos  

---

¡Excelente trabajo! Ahora dominas la estructura completa de una API RESTful. 🚀
