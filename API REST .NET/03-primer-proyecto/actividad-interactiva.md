# Actividades Interactivas - Módulo 3: Tu Primera API en .NET

## Sección 1: Preguntas de Opción Múltiple

### Pregunta 1
**¿Qué comando se usa para crear un nuevo proyecto de API web en .NET?**

A) `dotnet create webapi`  
B) `dotnet new webapi -n NombreProyecto`(X) 
C) `dotnet init api`  
D) `dotnet start webapi`  

---

### Pregunta 2
**¿Cuál es el archivo principal que configura e inicia una aplicación .NET?**

A) `Main.cs`  
B) `Startup.cs`  
C) `Program.cs`(X)  
D) `App.cs`  

---

### Pregunta 3
**¿Qué hace el atributo `[ApiController]` en una clase?**

A) Crea la API automáticamente  
B) Marca la clase como un controlador de API(X)  
C) Define las rutas  
D) Inicia el servidor  

---

### Pregunta 4
**¿Qué clase base deben heredar los controladores de API?**

A) `Controller`  
B) `ControllerBase`(X)  
C) `ApiController`  
D) `BaseController`  

---

### Pregunta 5
**¿Para qué sirve Swagger en una API?**

A) Para compilar el código  
B) Para generar documentación automática e interfaz de pruebas(X)  
C) Para conectar a la base de datos  
D) Para crear modelos  

---

### Pregunta 6
**¿Qué indica el atributo `[HttpGet]` en un método?**

A) Que el método obtiene datos mediante GET(X)  
B) Que el método crea datos  
C) Que el método elimina datos  
D) Que el método actualiza datos  

---

### Pregunta 7
**¿Qué devuelve el método `Ok(datos)`?**

A) Error 404  
B) Código 200 con los datos(X)  
C) Código 201  
D) Error 500  

---

### Pregunta 8
**¿Qué es un modelo (Model) en una API?**

A) La base de datos  
B) Una clase que representa la estructura de los datos(X)  
C) El controlador  
D) La ruta de la API  

---

## Sección 2: Completa la Analogía

### Analogía 1
**Controlador es a API como (A) es a restaurante**

A) Cocina  
B) Mesero  
C) Cliente  
D) Plato  

---

### Analogía 2
**Modelo es a datos como (A) es a construcción**

A) Herramienta  
B) Plano o molde  
C) Trabajador  
D) Pintura  

---

### Analogía 3
**Swagger es a API como (B) es a restaurante**

A) Cocina  
B) Menú ilustrado con fotos  
C) Mesero  
D) Caja registradora  

---

### Analogía 4
**Program.cs es a aplicación como (B) es a automóvil**

A) Volante  
B) Motor de arranque  
C) Llantas  
D) Radio  

---

### Analogía 5
**ActionResult es a respuesta como (A) es a carta**

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
1 → E  
2 → G  
3 → D  
4 → A  
5 → B  
6 → C  
7 → H  
8 → F 

---

## Sección 4: Verdadero o Falso

1. **V ** El comando `dotnet new webapi` crea un proyecto de API web.

2. **F ** Swagger solo funciona en producción.

3. **V ** Un controlador puede tener múltiples métodos HTTP.

4. **F ** El atributo `[ApiController]` es opcional en controladores de API.

5. **V ** Los modelos representan la estructura de los datos.

6. **F ** `NotFound()` devuelve un código de estado 200.

7. **V ** Puedes tener múltiples controladores en una API.

8. **V ** El comando `dotnet run` compila y ejecuta la API.

---

## Sección 5: Ejercicio Práctico - Creando tu API

**Instrucciones**: Documenta tu experiencia creando la API de Tareas.

### Parte 1: Creación del Proyecto

**¿Creaste el proyecto TareasAPI exitosamente?** (Sí/No)
Sí

**¿Qué comando usaste?**
dotnet create new -n webapi Tareas

**¿En qué carpeta creaste el proyecto?**
En la carpeta local de mi máquina llamada proyectos/dotnet

**¿Qué archivos y carpetas se generaron?** (enumera al menos 4)
1. Program.cs
2. _______________________________________________
3. _______________________________________________
4. _______________________________________________

---

### Parte 2: Primer Ejecución

**¿Ejecutaste `dotnet run` exitosamente?** (Sí/No)
Sí

**¿En qué puerto se ejecutó tu API?** (ej: 7001, 5000)
- HTTPS: 5000
- HTTP: 7001

**¿Pudiste acceder a Swagger?** (Sí/No)
Sí

**URL de Swagger que usaste:**
https:localhost:5000/swagger/Tareas

---

### Parte 3: Explorando Swagger

**¿Cuántos endpoints encontraste inicialmente?**
1

**¿Qué endpoint(s) vienen por defecto?**
Weather get

**¿Probaste el endpoint de ejemplo?** (Sí/No)
Sí

**¿Qué respuesta recibiste?**
EL clima código 200
_______________________________________________

---

### Parte 4: Creando el Modelo Tarea

**¿Creaste la carpeta Models?** (Sí/No)
Sí

**¿Creaste la clase Tarea?** (Sí/No)
Sí

**¿Qué propiedades tiene tu modelo Tarea?** (enumera todas)
1. Id
2. Título
3. Descripción
4. Realizada(True, False)
5. FechaRealizacion

---

### Parte 5: Creando TareasController

**¿Creaste TareasController.cs?** (Sí/No)
_______________________________________________

**¿Qué métodos HTTP implementaste?** (marca todos)
- [x ] GET (listar todas)
- [x ] GET (obtener una específica)
- [x ] POST
- [x ] PUT
- [x ] DELETE

**¿Aparece tu controlador en Swagger?** (Sí/No)
Sí

---

### Parte 6: Probando tu API

**¿Probaste GET /api/tareas?** (Sí/No)
Sí

**¿Cuántas tareas devolvió?**
4 tareas

**¿Probaste GET /api/tareas/{id}?** (Sí/No)
Sí

**¿Qué pasó cuando pediste un ID que no existe?**
Me arrijó un error 404

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
Busca por el id especificado y si lo encuentra
devuelve el código 200 ok

### Pregunta 2
**¿Qué significa `FirstOrDefault`?**
La tarea que aparece de primero


### Pregunta 3
**¿Qué código de estado devuelve `NotFound()`?**
404

### Pregunta 4
**¿Qué código de estado devuelve `Ok(tarea)`?**
200

### Pregunta 5
**¿Por qué verificamos si `tarea == null`?**
Para lanzar el código de validación, si existe,
arroja el codigo 200, sino, el código 404

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
1 → D 
2 → A  
3 → B  
4 → C  
5 → E  

---

## Sección 8: Mini-Proyecto - Personaliza tu API

**Instrucciones**: Modifica la API de Tareas según las siguientes especificaciones.

### Tarea 1: Agregar una Propiedad
**Agrega una propiedad `Prioridad` (Alta, Media, Baja) al modelo Tarea.**

¿Lo completaste? [X] Sí [ ] No

¿Qué tipo de dato usaste?
Prioridad: Alta, Media o Baja.

---

### Tarea 2: Crear Tareas de Prueba
**Agrega al menos 3 tareas diferentes a la lista inicial.**

¿Lo completaste? [ ] Sí [ ] No

Enumera tus tareas:
1. Leer un Libro
2. Hacer burpees a las 04:00 am
3. Nadar todos los dias.

---

### Tarea 3: Probar con Diferentes Herramientas
**Prueba tu API usando al menos 2 de estas herramientas:**

- [x ] Swagger
- [x ] Navegador
- [ ] Postman
- [ ] cURL

¿Cuál te gustó más y por qué?
Insomnia, pero no está en la lista proveida.
_______________________________________________

---

## Sección 9: Solución de Problemas

**Instrucciones**: Para cada problema, describe qué harías.

### Problema 1
**Ejecutas `dotnet run` pero recibes: "Error: Failed to bind to address https://localhost:7001"**

¿Qué podría estar pasando?
Que el puerto 7001 está siendo usado por otra app. 
_______________________________________________

¿Qué solución intentarías?
habria que detener la ejecución en ese puerto. hacer la compilación nuevamente y ejecutar dotnet run
o agregar un nuevo puerto usando launchSetting.json

---

### Problema 2
**Tu controlador no aparece en Swagger.**

¿Qué verificarías?** (enumera al menos 3 cosas)
1. Verificar en el COntroller model
2. Revisar los nombres en el controlador
3. verificar la herencia

---

### Problema 3
**El navegador dice que la conexión no es segura al acceder a https://localhost:7001**

¿Qué comando podrías ejecutar para solucionarlo?
dotnet dev-certs --trust

---

## Sección 10: Reflexión y Aprendizaje

**¿Qué fue lo más emocionante de crear tu primera API?**
Tener acceso a una API creada directamente por mi.

**¿Qué concepto te resultó más difícil de entender?**
en la parte de los Controllers

**¿Qué te gustaría agregar a tu API?**
la prioridad en las tareas

**En una escala del 1 al 5, ¿qué tan cómodo te sientes con lo aprendido?**
1 (nada cómodo) - 2 - 3 - 4 - 5 (muy cómodo)
5
**¿Qué quieres aprender en el próximo módulo?**
_______________________________________________
_______________________________________________

---

¡Excelente trabajo! Una vez que completes estas actividades, revisa tus respuestas en el archivo `retroalimentacion.md`. 🎉
