# Retroalimentación y Soluciones - Módulo 3: Tu Primera API en .NET

## Sección 1: Respuestas a Preguntas de Opción Múltiple

### Pregunta 1: ¿Qué comando se usa para crear un nuevo proyecto de API web en .NET?
**Respuesta correcta: B) `dotnet new webapi -n NombreProyecto`**

**Explicación**: El comando `dotnet new webapi` usa la plantilla de API web, y el flag `-n` especifica el nombre del proyecto. Por ejemplo: `dotnet new webapi -n MiAPI`.

---

### Pregunta 2: ¿Cuál es el archivo principal que configura e inicia una aplicación .NET?
**Respuesta correcta: C) Program.cs**

**Explicación**: Program.cs es el punto de entrada de la aplicación. Aquí se configura el WebApplication, se registran servicios y se define el pipeline de HTTP.

---

### Pregunta 3: ¿Qué hace el atributo `[ApiController]` en una clase?
**Respuesta correcta: B) Marca la clase como un controlador de API**

**Explicación**: `[ApiController]` habilita características específicas para APIs como validación automática de modelos, inferencia de fuentes de binding y mejor manejo de errores.

---

### Pregunta 4: ¿Qué clase base deben heredar los controladores de API?
**Respuesta correcta: B) ControllerBase**

**Explicación**: Los controladores de API heredan de `ControllerBase`, que proporciona métodos útiles como `Ok()`, `NotFound()`, `BadRequest()`, etc. `Controller` se usa para MVC con vistas.

---

### Pregunta 5: ¿Para qué sirve Swagger en una API?
**Respuesta correcta: B) Para generar documentación automática e interfaz de pruebas**

**Explicación**: Swagger (OpenAPI) genera documentación interactiva de tu API y proporciona Swagger UI para probar endpoints directamente desde el navegador.

---

### Pregunta 6: ¿Qué indica el atributo `[HttpGet]` en un método?
**Respuesta correcta: A) Que el método obtiene datos mediante GET**

**Explicación**: `[HttpGet]` indica que este método responde a peticiones HTTP GET, típicamente usadas para obtener datos sin modificarlos.

---

### Pregunta 7: ¿Qué devuelve el método `Ok(datos)`?
**Respuesta correcta: B) Código 200 con los datos**

**Explicación**: `Ok(datos)` devuelve un código de estado HTTP 200 (éxito) junto con los datos en el cuerpo de la respuesta, generalmente en formato JSON.

---

### Pregunta 8: ¿Qué es un modelo (Model) en una API?
**Respuesta correcta: B) Una clase que representa la estructura de los datos**

**Explicación**: Un modelo es una clase que define la estructura y propiedades de los datos que tu API maneja, como la clase `Tarea` con sus propiedades Id, Titulo, etc.

---

## Sección 2: Respuestas a Analogías

### Analogía 1: Controlador es a API como __________ es a restaurante
**Respuesta correcta: B) Mesero**

**Explicación**: El controlador, como un mesero, recibe peticiones (pedidos), las procesa y devuelve respuestas (comida). Es el intermediario entre el cliente y la lógica de negocio.

---

### Analogía 2: Modelo es a datos como __________ es a construcción
**Respuesta correcta: B) Plano o molde**

**Explicación**: Un modelo define la estructura exacta de los datos, igual que un plano define cómo debe ser construida una casa.

---

### Analogía 3: Swagger es a API como __________ es a restaurante
**Respuesta correcta: B) Menú ilustrado con fotos**

**Explicación**: Swagger documenta visualmente qué puedes pedir (endpoints), qué necesitas enviar (parámetros) y qué recibirás (respuesta), como un menú con fotos.

---

### Analogía 4: Program.cs es a aplicación como __________ es a automóvil
**Respuesta correcta: B) Motor de arranque**

**Explicación**: Program.cs inicializa y arranca toda la aplicación, configurando todos los componentes necesarios antes de empezar a funcionar.

---

### Analogía 5: ActionResult es a respuesta como __________ es a carta
**Respuesta correcta: A) Sobre con respuesta dentro**

**Explicación**: ActionResult es un "contenedor" que incluye tanto el código de estado (el sobre) como los datos de respuesta (el contenido).

---

## Sección 3: Asociación de Términos con Definiciones

**Respuestas correctas**:
1 → B (Controller = Clase que maneja peticiones HTTP)  
2 → G (Model = Clase que representa la estructura de datos)  
3 → D (Program.cs = Punto de entrada de la aplicación)  
4 → A (Swagger = Herramienta para documentar y probar APIs)  
5 → E ([HttpGet] = Atributo que marca un método GET)  
6 → C (ActionResult = Tipo de retorno que incluye código de estado)  
7 → H (Endpoint = Ruta específica de la API)  
8 → F (localhost = Dirección IP local)  

---

## Sección 4: Verdadero o Falso

1. **V (Verdadero)** - `dotnet new webapi` crea un proyecto de API web

2. **F (Falso)** - Swagger funciona principalmente en desarrollo, se puede desactivar en producción

3. **V (Verdadero)** - Un controlador puede tener múltiples métodos con diferentes verbos HTTP

4. **F (Falso)** - Aunque es técnicamente opcional, `[ApiController]` es altamente recomendado para APIs

5. **V (Verdadero)** - Los modelos representan la estructura de los datos

6. **F (Falso)** - `NotFound()` devuelve código 404, no 200

7. **V (Verdadero)** - Puedes tener múltiples controladores en una API

8. **V (Verdadero)** - `dotnet run` compila y ejecuta la aplicación

---

## Sección 7: Códigos de Estado HTTP

**Respuestas correctas**:
1 → D (404 Not Found - el recurso no existe)  
2 → A (200 OK - operación exitosa con datos)  
3 → B (201 Created - recurso creado exitosamente)  
4 → C (400 Bad Request - datos inválidos del cliente)  
5 → E (500 Internal Server Error - error en el servidor)  

---

## Evaluación de tu Desempeño

### Si acertaste 90% o más: 🌟 ¡Excelente!
¡Increíble! Has comprendido perfectamente cómo crear APIs en .NET. Tu primera API está funcionando y entiendes cada componente.

**Próximos pasos**:
- Experimenta agregando más endpoints a TareasController
- Intenta crear otro controlador para un dominio diferente (ej: Productos)
- Explora Swagger UI a fondo
- Prepárate para aprender sobre rutas avanzadas y validación

---

### Si acertaste entre 70% y 89%: 💪 ¡Muy bien!
Tienes una comprensión sólida de los conceptos fundamentales. Solo necesitas reforzar algunos detalles.

**Recomendaciones**:
- Repasa la diferencia entre Controller y ControllerBase
- Practica creando diferentes tipos de endpoints
- Revisa los códigos de estado HTTP y cuándo usar cada uno
- Asegúrate de entender qué hace cada parte de Program.cs

---

### Si acertaste entre 50% y 69%: 📚 Sigue adelante
Entiendes las bases pero necesitas más práctica con los conceptos.

**Recomendaciones**:
- Vuelve a crear el proyecto desde cero siguiendo el README
- Enfócate en entender el flujo: petición → controlador → respuesta
- Practica con Swagger hasta sentirte cómodo
- No avances hasta tener tu API funcionando correctamente

---

### Si acertaste menos de 50%: 🔄 Repaso necesario
Los conceptos de APIs y .NET pueden ser abrumadores al principio.

**Recomendaciones**:
- Asegúrate de tener el módulo anterior (instalación de .NET) bien comprendido
- Sigue el README paso a paso sin saltarte nada
- Pide ayuda si tienes errores de compilación
- Ve videos tutoriales sobre "primera API en .NET"
- Dedica más tiempo a experimentar con el código

---

## Consejos Generales para Avanzar

### 💡 Para todos los niveles:

1. **Experimenta sin miedo**: No puedes "romper" nada. Si algo sale mal, simplemente recrea el proyecto.

2. **Usa el depurador**: Aprende a poner breakpoints en VS Code para ver qué hace tu código paso a paso.

3. **Lee los mensajes de error**: Los errores de compilación te dicen exactamente qué está mal y dónde.

4. **Compara con el código de ejemplo**: Si algo no funciona, compara tu código línea por línea con los ejemplos.

5. **Documenta tus hallazgos**: Usa el archivo `progreso.md` para anotar qué funciona y qué no.

---

## Soluciones a Problemas Comunes

### Problema 1: "Failed to bind to address"
**Solución**: Otro proceso está usando el puerto. Opciones:
- Detén otras instancias de tu API
- Cambia el puerto en `Properties/launchSettings.json`
- Reinicia tu computadora

### Problema 2: Controlador no aparece en Swagger
**Verificar**:
- ¿Heredade `ControllerBase`?
- ¿Tiene el atributo `[ApiController]`?
- ¿Tiene un atributo `[Route]`?
- ¿El nombre termina en "Controller"?
- ¿Está en el namespace correcto?

### Problema 3: Certificado no confiable
**Solución**:
```bash
dotnet dev-certs https --trust
```
Luego reinicia el navegador.

---

## Recursos Adicionales Recomendados

### Videos:
- "Tutorial de Web API en .NET - Para principiantes"
- "Cómo funciona Swagger en .NET"
- "Primeros pasos con controladores en .NET"

### Documentación:
- Tutorial oficial: https://docs.microsoft.com/aspnet/core/tutorials/first-web-api
- Guía de controladores: https://docs.microsoft.com/aspnet/core/web-api/
- Documentación de Swagger: https://docs.microsoft.com/aspnet/core/tutorials/web-api-help-pages-using-swagger

### Práctica:
- Crea una API de Libros con título, autor, año
- Crea una API de Contactos con nombre, email, teléfono
- Explora otras APIs de ejemplo en GitHub

---

## Preparación para el Siguiente Módulo

Antes de avanzar al Módulo 4 (Rutas, Controladores y Modelos), asegúrate de:

✅ Tener tu API TareasAPI funcionando correctamente  
✅ Poder crear un proyecto de API desde cero  
✅ Entender qué es un controlador y un modelo  
✅ Saber usar Swagger para probar endpoints  
✅ Conocer los códigos de estado HTTP básicos (200, 404, etc.)  
✅ Poder agregar métodos GET a un controlador  

---

## Lo que Aprenderás en el Siguiente Módulo

En el Módulo 4 profundizarás en:
- Rutas personalizadas y parámetros de ruta
- Métodos HTTP completos (POST, PUT, DELETE)
- DTOs (Data Transfer Objects)
- Relaciones entre modelos
- Mejores prácticas para diseñar APIs

---

¡Felicitaciones por crear tu primera API! Este es un gran paso en tu camino como desarrollador. 🚀

**¿Listo para aprender sobre rutas y controladores avanzados?** ¡Nos vemos en el Módulo 4! 💙
