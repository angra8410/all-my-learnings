# Actividades Interactivas - Módulo 3: Tu Primera API en .NET

## Sección 1: Preguntas de Opción Múltiple

### Pregunta 1
**¿Qué comando se usa para crear un nuevo proyecto de API web en .NET?**

A) `dotnet create webapi`  
B) `dotnet new webapi -n NombreProyecto`  
C) `dotnet init api`  
D) `dotnet start webapi`  

---

### Pregunta 2
**¿Cuál es el archivo principal que configura e inicia una aplicación .NET?**

A) `Main.cs`  
B) `Startup.cs`  
C) `Program.cs`  
D) `App.cs`  

---

### Pregunta 3
**¿Qué hace el atributo `[ApiController]` en una clase?**

A) Crea la API automáticamente  
B) Marca la clase como un controlador de API  
C) Define las rutas  
D) Inicia el servidor  

---

### Pregunta 4
**¿Qué clase base deben heredar los controladores de API?**

A) `Controller`  
B) `ControllerBase`  
C) `ApiController`  
D) `BaseController`  

---

### Pregunta 5
**¿Para qué sirve Swagger en una API?**

A) Para compilar el código  
B) Para generar documentación automática e interfaz de pruebas  
C) Para conectar a la base de datos  
D) Para crear modelos  

---

### Pregunta 6
**¿Qué indica el atributo `[HttpGet]` en un método?**

A) Que el método obtiene datos mediante GET  
B) Que el método crea datos  
C) Que el método elimina datos  
D) Que el método actualiza datos  

---

### Pregunta 7
**¿Qué devuelve el método `Ok(datos)`?**

A) Error 404  
B) Código 200 con los datos  
C) Código 201  
D) Error 500  

---

### Pregunta 8
**¿Qué es un modelo (Model) en una API?**

A) La base de datos  
B) Una clase que representa la estructura de los datos  
C) El controlador  
D) La ruta de la API  

---

## Sección 2: Completa la Analogía

### Analogía 1
**Controlador es a API como __________ es a restaurante**

A) Cocina  
B) Mesero  
C) Cliente  
D) Plato  

---

### Analogía 2
**Modelo es a datos como __________ es a construcción**

A) Herramienta  
B) Plano o molde  
C) Trabajador  
D) Pintura  

---

### Analogía 3
**Swagger es a API como __________ es a restaurante**

A) Cocina  
B) Menú ilustrado con fotos  
C) Mesero  
D) Caja registradora  

---

### Analogía 4
**Program.cs es a aplicación como __________ es a automóvil**

A) Volante  
B) Motor de arranque  
C) Llantas  
D) Radio  

---

### Analogía 5
**ActionResult es a respuesta como __________ es a carta**

A) Sobre con respuesta dentro  
B) Buzón  
C) Cartero  
D) Papel  

---

## Sección 3: Asocia Términos con Definiciones

**Instrucciones**: Asocia cada término de la columna izquierda con su definición correcta.

### Términos:
1. Controller
2. Model
3. Program.cs
4. Swagger
5. [HttpGet]
6. ActionResult
7. Endpoint
8. localhost

### Definiciones:
A) Herramienta para documentar y probar APIs  
B) Clase que maneja peticiones HTTP  
C) Tipo de retorno que incluye código de estado  
D) Punto de entrada de la aplicación  
E) Atributo que marca un método GET  
F) Dirección IP local (tu computadora)  
G) Clase que representa la estructura de datos  
H) Ruta específica de la API (ej: /api/tareas)  

**Tus respuestas**:
1 → ___  
2 → ___  
3 → ___  
4 → ___  
5 → ___  
6 → ___  
7 → ___  
8 → ___  

---

## Sección 4: Verdadero o Falso

1. **___** El comando `dotnet new webapi` crea un proyecto de API web.

2. **___** Swagger solo funciona en producción.

3. **___** Un controlador puede tener múltiples métodos HTTP.

4. **___** El atributo `[ApiController]` es opcional en controladores de API.

5. **___** Los modelos representan la estructura de los datos.

6. **___** `NotFound()` devuelve un código de estado 200.

7. **___** Puedes tener múltiples controladores en una API.

8. **___** El comando `dotnet run` compila y ejecuta la API.

---

## Sección 5: Ejercicio Práctico - Creando tu API

**Instrucciones**: Documenta tu experiencia creando la API de Tareas.

### Parte 1: Creación del Proyecto

**¿Creaste el proyecto TareasAPI exitosamente?** (Sí/No)
_______________________________________________

**¿Qué comando usaste?**
_______________________________________________

**¿En qué carpeta creaste el proyecto?**
_______________________________________________

**¿Qué archivos y carpetas se generaron?** (enumera al menos 4)
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________
4. _______________________________________________

---

### Parte 2: Primer Ejecución

**¿Ejecutaste `dotnet run` exitosamente?** (Sí/No)
_______________________________________________

**¿En qué puerto se ejecutó tu API?** (ej: 7001, 5000)
- HTTPS: _______________________________________________
- HTTP: _______________________________________________

**¿Pudiste acceder a Swagger?** (Sí/No)
_______________________________________________

**URL de Swagger que usaste:**
_______________________________________________

---

### Parte 3: Explorando Swagger

**¿Cuántos endpoints encontraste inicialmente?**
_______________________________________________

**¿Qué endpoint(s) vienen por defecto?**
_______________________________________________

**¿Probaste el endpoint de ejemplo?** (Sí/No)
_______________________________________________

**¿Qué respuesta recibiste?**
_______________________________________________
_______________________________________________

---

### Parte 4: Creando el Modelo Tarea

**¿Creaste la carpeta Models?** (Sí/No)
_______________________________________________

**¿Creaste la clase Tarea?** (Sí/No)
_______________________________________________

**¿Qué propiedades tiene tu modelo Tarea?** (enumera todas)
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________
4. _______________________________________________
5. _______________________________________________

---

### Parte 5: Creando TareasController

**¿Creaste TareasController.cs?** (Sí/No)
_______________________________________________

**¿Qué métodos HTTP implementaste?** (marca todos)
- [ ] GET (listar todas)
- [ ] GET (obtener una específica)
- [ ] POST
- [ ] PUT
- [ ] DELETE

**¿Aparece tu controlador en Swagger?** (Sí/No)
_______________________________________________

---

### Parte 6: Probando tu API

**¿Probaste GET /api/tareas?** (Sí/No)
_______________________________________________

**¿Cuántas tareas devolvió?**
_______________________________________________

**¿Probaste GET /api/tareas/{id}?** (Sí/No)
_______________________________________________

**¿Qué pasó cuando pediste un ID que no existe?**
_______________________________________________
_______________________________________________

---

## Sección 6: Análisis de Código

**Instrucciones**: Lee el siguiente código y responde.

```csharp
[HttpGet("{id}")]
public ActionResult<Tarea> GetTarea(int id)
{
    var tarea = tareas.FirstOrDefault(t => t.Id == id);
    
    if (tarea == null)
    {
        return NotFound();
    }
    
    return Ok(tarea);
}
```

### Pregunta 1
**¿Qué hace `{id}` en `[HttpGet("{id}")]`?**
_______________________________________________
_______________________________________________

### Pregunta 2
**¿Qué significa `FirstOrDefault`?**
_______________________________________________
_______________________________________________

### Pregunta 3
**¿Qué código de estado devuelve `NotFound()`?**
_______________________________________________

### Pregunta 4
**¿Qué código de estado devuelve `Ok(tarea)`?**
_______________________________________________

### Pregunta 5
**¿Por qué verificamos si `tarea == null`?**
_______________________________________________
_______________________________________________

---

## Sección 7: Códigos de Estado HTTP

**Instrucciones**: Asocia cada situación con el código de estado correcto.

### Situaciones:
1. El cliente pidió la tarea con ID 99 pero no existe
2. La operación se completó exitosamente y devolvemos datos
3. Se creó una nueva tarea correctamente
4. El cliente envió datos inválidos
5. Hay un error en el código del servidor

### Códigos:
A) 200 OK  
B) 201 Created  
C) 400 Bad Request  
D) 404 Not Found  
E) 500 Internal Server Error  

**Tus respuestas**:
1 → ___  
2 → ___  
3 → ___  
4 → ___  
5 → ___  

---

## Sección 8: Mini-Proyecto - Personaliza tu API

**Instrucciones**: Modifica la API de Tareas según las siguientes especificaciones.

### Tarea 1: Agregar una Propiedad
**Agrega una propiedad `Prioridad` (Alta, Media, Baja) al modelo Tarea.**

¿Lo completaste? [ ] Sí [ ] No

¿Qué tipo de dato usaste?
_______________________________________________

---

### Tarea 2: Crear Tareas de Prueba
**Agrega al menos 3 tareas diferentes a la lista inicial.**

¿Lo completaste? [ ] Sí [ ] No

Enumera tus tareas:
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

---

### Tarea 3: Probar con Diferentes Herramientas
**Prueba tu API usando al menos 2 de estas herramientas:**

- [ ] Swagger
- [ ] Navegador
- [ ] Postman
- [ ] cURL

¿Cuál te gustó más y por qué?
_______________________________________________
_______________________________________________

---

## Sección 9: Solución de Problemas

**Instrucciones**: Para cada problema, describe qué harías.

### Problema 1
**Ejecutas `dotnet run` pero recibes: "Error: Failed to bind to address https://localhost:7001"**

¿Qué podría estar pasando?
_______________________________________________
_______________________________________________

¿Qué solución intentarías?
_______________________________________________
_______________________________________________

---

### Problema 2
**Tu controlador no aparece en Swagger.**

¿Qué verificarías?** (enumera al menos 3 cosas)
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

---

### Problema 3
**El navegador dice que la conexión no es segura al acceder a https://localhost:7001**

¿Qué comando podrías ejecutar para solucionarlo?
_______________________________________________

---

## Sección 10: Reflexión y Aprendizaje

**¿Qué fue lo más emocionante de crear tu primera API?**
_______________________________________________
_______________________________________________

**¿Qué concepto te resultó más difícil de entender?**
_______________________________________________
_______________________________________________

**¿Qué te gustaría agregar a tu API?**
_______________________________________________
_______________________________________________

**En una escala del 1 al 5, ¿qué tan cómodo te sientes con lo aprendido?**
1 (nada cómodo) - 2 - 3 - 4 - 5 (muy cómodo)

**¿Qué quieres aprender en el próximo módulo?**
_______________________________________________
_______________________________________________

---

¡Excelente trabajo! Una vez que completes estas actividades, revisa tus respuestas en el archivo `retroalimentacion.md`. 🎉
