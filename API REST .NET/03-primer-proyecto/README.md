# Módulo 3: Tu Primera API en .NET

## ¡Es hora de crear tu primera API!

Llegó el momento más emocionante: vas a construir tu primera API RESTful desde cero. No te preocupes si parece complicado al principio, lo vamos a hacer paso a paso y entenderás cada parte del proceso.

**Analogía del día**: Crear una API es como **construir tu primer restaurante**. Ya aprendiste qué es un restaurante (módulo 1) y conseguiste las herramientas necesarias (módulo 2). Ahora vas a abrir las puertas y empezar a recibir clientes.

## ¿Qué vamos a construir?

Crearemos una API simple llamada **"TareasAPI"** que permite:
- Ver una lista de tareas
- Obtener una tarea específica
- Crear nuevas tareas
- Actualizar tareas existentes
- Eliminar tareas

Es un proyecto perfecto para aprender porque es simple pero incluye todas las operaciones fundamentales (CRUD).

## Creando el proyecto

### Paso 1: Preparar tu espacio de trabajo

Primero, crea una carpeta organizada para tus proyectos:

```bash
# Navega a donde quieres crear tu proyecto
cd ~/Documentos  # o C:\Users\TuNombre\Documentos en Windows

# Crea una carpeta para tus APIs
mkdir MisAPIs
cd MisAPIs
```

### Paso 2: Crear el proyecto de API

Ahora usa el comando mágico de .NET para crear una API:

```bash
dotnet new webapi -n TareasAPI
```

**¿Qué hace este comando?**
- `dotnet new`: Crea un nuevo proyecto
- `webapi`: Usa la plantilla de API web
- `-n TareasAPI`: Le da el nombre "TareasAPI"

Verás algo como:
```
The template "ASP.NET Core Web API" was created successfully.
```

### Paso 3: Explorar lo que se creó

```bash
cd TareasAPI
ls  # o 'dir' en Windows
```

.NET creó varios archivos automáticamente. Los más importantes son:

```
TareasAPI/
├── Program.cs              # Punto de entrada de la aplicación
├── TareasAPI.csproj       # Configuración del proyecto
├── appsettings.json       # Configuración de la aplicación
├── Controllers/           # Carpeta para tus controladores
│   └── WeatherForecastController.cs
├── Properties/
│   └── launchSettings.json
└── obj/                   # Archivos temporales
```

## Estructura del proyecto: Entendiendo cada parte

### Program.cs - El corazón de tu API

Este archivo es el **punto de entrada** de tu aplicación. Es como el gerente de tu restaurante que organiza todo.

Abre el archivo en VS Code:
```bash
code .  # Abre VS Code en la carpeta actual
```

Verás código similar a esto:

```csharp
var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllers();
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();
app.UseAuthorization();
app.MapControllers();

app.Run();
```

**Desglose línea por línea:**

1. **`var builder = WebApplication.CreateBuilder(args);`**
   - Crea el "constructor" de tu aplicación
   - Como preparar la cocina antes de abrir el restaurante

2. **`builder.Services.AddControllers();`**
   - Registra los controladores (los "meseros" de tu API)

3. **`builder.Services.AddSwaggerGen();`**
   - Agrega Swagger, una herramienta que genera documentación automática
   - Es como crear un menú visual de tu restaurante

4. **`var app = builder.Build();`**
   - Construye la aplicación con todo lo configurado

5. **`app.UseSwagger();` y `app.UseSwaggerUI();`**
   - Activa la interfaz visual de Swagger (solo en desarrollo)

6. **`app.MapControllers();`**
   - Conecta las rutas con los controladores

7. **`app.Run();`**
   - ¡Inicia el servidor! Abre las puertas del restaurante

### Controllers - Los meseros de tu API

Los **controladores** son clases que manejan las peticiones HTTP. Cada método en un controlador es como un platillo en el menú.

.NET ya creó un controlador de ejemplo: `WeatherForecastController.cs`

```csharp
[ApiController]
[Route("[controller]")]
public class WeatherForecastController : ControllerBase
{
    [HttpGet(Name = "GetWeatherForecast")]
    public IEnumerable<WeatherForecast> Get()
    {
        // Código que devuelve datos del clima
    }
}
```

**Componentes importantes:**
- **`[ApiController]`**: Marca esta clase como un controlador de API
- **`[Route("[controller]")]`**: Define la ruta base (será `/weatherforecast`)
- **`[HttpGet]`**: Indica que este método responde a peticiones GET
- **`ControllerBase`**: Clase base con funcionalidades útiles para APIs

## Ejecutando tu primera API

### Paso 1: Iniciar el servidor

```bash
dotnet run
```

Verás algo como:
```
info: Microsoft.Hosting.Lifetime[14]
      Now listening on: https://localhost:7001
      Now listening on: http://localhost:5000
Building...
```

¡Tu API está viva! 🎉

### Paso 2: Probar la API en el navegador

Abre tu navegador y ve a:
```
https://localhost:7001/swagger
```

Verás una página interactiva llamada **Swagger UI** que documenta tu API automáticamente.

### Paso 3: Hacer tu primera petición

En Swagger:
1. Haz clic en **GET /WeatherForecast**
2. Haz clic en **"Try it out"**
3. Haz clic en **"Execute"**

Verás una respuesta JSON con datos del clima (datos de prueba).

También puedes probarlo directamente en el navegador:
```
https://localhost:7001/weatherforecast
```

## Creando tu propio controlador

Ahora vamos a crear un controlador personalizado para **tareas**.

### Paso 1: Crear el modelo Tarea

Primero necesitamos definir qué es una "tarea". Crea una carpeta llamada `Models`:

```bash
mkdir Models
```

Crea un archivo `Models/Tarea.cs`:

```csharp
namespace TareasAPI.Models
{
    public class Tarea
    {
        public int Id { get; set; }
        public string? Titulo { get; set; }
        public string? Descripcion { get; set; }
        public bool Completada { get; set; }
        public DateTime FechaCreacion { get; set; }
    }
}
```

**¿Qué es esto?**
- Una **clase** que representa una tarea
- Tiene propiedades: Id, Título, Descripción, etc.
- `{ get; set; }` permite leer y modificar estas propiedades
- `?` indica que puede ser null (opcional)

### Paso 2: Crear el controlador de Tareas

Crea un archivo `Controllers/TareasController.cs`:

```csharp
using Microsoft.AspNetCore.Mvc;
using TareasAPI.Models;

namespace TareasAPI.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class TareasController : ControllerBase
    {
        // Lista temporal de tareas (en memoria)
        private static List<Tarea> tareas = new List<Tarea>
        {
            new Tarea 
            { 
                Id = 1, 
                Titulo = "Aprender .NET", 
                Descripcion = "Completar el curso de APIs",
                Completada = false,
                FechaCreacion = DateTime.Now
            },
            new Tarea 
            { 
                Id = 2, 
                Titulo = "Hacer ejercicio", 
                Descripcion = "30 minutos de cardio",
                Completada = true,
                FechaCreacion = DateTime.Now.AddDays(-1)
            }
        };

        // GET: api/tareas
        [HttpGet]
        public ActionResult<IEnumerable<Tarea>> GetTareas()
        {
            return Ok(tareas);
        }

        // GET: api/tareas/1
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
    }
}
```

### Paso 3: Probar tu nuevo controlador

1. Detén el servidor (Ctrl+C en la terminal)
2. Vuelve a ejecutar: `dotnet run`
3. Ve a: `https://localhost:7001/swagger`
4. Ahora verás **TareasController** con tus endpoints
5. Prueba GET /api/tareas

También puedes ir directamente a:
```
https://localhost:7001/api/tareas
```

¡Verás tus tareas en formato JSON!

## Entendiendo las respuestas HTTP

Cuando haces una petición, tu API devuelve un **código de estado**:

| Código | Significado | Cuándo usarlo |
|--------|-------------|---------------|
| 200 OK | Todo bien | Operación exitosa |
| 201 Created | Recurso creado | Al crear algo nuevo |
| 204 No Content | Sin contenido | Al eliminar exitosamente |
| 400 Bad Request | Petición inválida | Datos incorrectos |
| 404 Not Found | No encontrado | Recurso no existe |
| 500 Internal Server Error | Error del servidor | Bug en tu código |

En nuestro código:
- **`Ok(datos)`**: Devuelve 200 con datos
- **`NotFound()`**: Devuelve 404
- **`BadRequest()`**: Devuelve 400

## Herramientas para probar APIs

### 1. Swagger (ya lo tienes)
✅ Incluido automáticamente
✅ Perfecto para desarrollo
✅ Interfaz visual

### 2. Navegador
✅ Funciona para GET simples
❌ No funciona para POST, PUT, DELETE

### 3. Postman (recomendado)
1. Descarga Postman: https://www.postman.com/downloads/
2. Crea una nueva petición
3. Elige el método (GET, POST, etc.)
4. Ingresa la URL: `https://localhost:7001/api/tareas`
5. Haz clic en "Send"

### 4. cURL (línea de comandos)
```bash
curl https://localhost:7001/api/tareas
```

## Conceptos clave para recordar

- 🔑 **WebAPI**: Plantilla de proyecto para crear APIs
- 🔑 **Program.cs**: Configura e inicia tu aplicación
- 🔑 **Controller**: Clase que maneja peticiones HTTP
- 🔑 **Model**: Clase que representa datos (como Tarea)
- 🔑 **[HttpGet], [HttpPost]**: Atributos que indican el método HTTP
- 🔑 **ActionResult**: Tipo de retorno que incluye código de estado
- 🔑 **Swagger**: Herramienta de documentación automática
- 🔑 **localhost**: Tu computadora (servidor local)
- 🔑 **Puerto**: Número que identifica tu aplicación (ej: 7001)

## Resolución de problemas comunes

### Error: "Failed to bind to address"
**Causa**: El puerto ya está en uso  
**Solución**: Cierra otras instancias de la API o cambia el puerto en `launchSettings.json`

### Error: "Certificate not trusted"
**Causa**: Certificado HTTPS no confiable  
**Solución**: 
```bash
dotnet dev-certs https --trust
```

### No aparece mi controlador en Swagger
**Causa**: Nombre incorrecto o herencia faltante  
**Solución**: Asegúrate de que herede de `ControllerBase` y tenga `[ApiController]`

## Próximos pasos

Ahora que tienes tu primera API funcionando:
- Experimenta modificando las tareas existentes
- Agrega más propiedades al modelo Tarea
- Intenta crear más endpoints
- En el próximo módulo aprenderás sobre rutas y verbos HTTP en detalle

¡Felicidades! Has creado tu primera API RESTful en .NET 🚀
