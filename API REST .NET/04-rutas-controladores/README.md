# Módulo 4: Rutas, Controladores y Modelos

## Profundizando en las APIs

Ya creaste tu primera API, pero ahora es momento de comprender a fondo cómo funcionan las rutas, cómo organizar mejor tus controladores y cómo diseñar modelos efectivos. Este módulo te convertirá en un experto en la estructura de APIs RESTful.

**Analogía del día**: Si en el módulo anterior abriste tu restaurante, ahora vas a **organizar el menú de manera profesional**, establecer rutas claras para los meseros y definir exactamente qué platos ofreces.

## Rutas en ASP.NET Core

### ¿Qué son las rutas?

Las **rutas** son los "caminos" que los clientes usan para acceder a tus endpoints. Son como las direcciones de tu casa: claras, únicas y predecibles.

**Ejemplo**:
```
GET https://miapi.com/api/productos
GET https://miapi.com/api/productos/123
POST https://miapi.com/api/productos
```

### Tipos de Rutas

#### 1. Rutas basadas en Atributos (Recomendado para APIs)

```csharp
[ApiController]
[Route("api/[controller]")]
public class ProductosController : ControllerBase
{
    // GET: api/productos
    [HttpGet]
    public ActionResult<IEnumerable<Producto>> GetAll()
    {
        // ...
    }
    
    // GET: api/productos/5
    [HttpGet("{id}")]
    public ActionResult<Producto> GetById(int id)
    {
        // ...
    }
}
```

**Desglose**:
- `[Route("api/[controller]")]`: Establece la ruta base
- `[controller]` se reemplaza automáticamente por el nombre del controlador (sin "Controller")
- `ProductosController` → ruta base: `/api/productos`

#### 2. Rutas Personalizadas

Puedes definir rutas específicas para cada acción:

```csharp
[ApiController]
public class ProductosController : ControllerBase
{
    [HttpGet("api/catalogo/productos")]
    public ActionResult<IEnumerable<Producto>> GetAll()
    {
        // GET: api/catalogo/productos
    }
    
    [HttpGet("api/catalogo/productos/{id}")]
    public ActionResult<Producto> GetById(int id)
    {
        // GET: api/catalogo/productos/5
    }
    
    [HttpGet("api/productos/destacados")]
    public ActionResult<IEnumerable<Producto>> GetDestacados()
    {
        // GET: api/productos/destacados
    }
}
```

## Parámetros de Ruta

### Parámetros Requeridos

```csharp
// GET: api/productos/5
[HttpGet("{id}")]
public ActionResult<Producto> GetById(int id)
{
    // id es obligatorio
}

// GET: api/productos/categorias/electronicos
[HttpGet("categorias/{categoria}")]
public ActionResult<IEnumerable<Producto>> GetByCategoria(string categoria)
{
    // categoria es obligatorio
}
```

### Parámetros Opcionales y Valores por Defecto

```csharp
// GET: api/productos?pagina=1&tamanio=10
[HttpGet]
public ActionResult<IEnumerable<Producto>> GetAll(
    [FromQuery] int pagina = 1,
    [FromQuery] int tamanio = 10)
{
    var productos = _productos
        .Skip((pagina - 1) * tamanio)
        .Take(tamanio);
    return Ok(productos);
}
```

### Restricciones de Rutas

Puedes especificar tipos y restricciones:

```csharp
// Solo acepta números
[HttpGet("{id:int}")]
public ActionResult<Producto> GetById(int id) { }

// id debe ser número mayor que 0
[HttpGet("{id:int:min(1)}")]
public ActionResult<Producto> GetById(int id) { }

// Acepta guid
[HttpGet("{id:guid}")]
public ActionResult<Producto> GetById(Guid id) { }

// Acepta string con longitud máxima
[HttpGet("{nombre:maxlength(50)}")]
public ActionResult<Producto> GetByNombre(string nombre) { }
```

## Verbos HTTP Completos

### GET - Obtener Recursos

```csharp
// Obtener todos
[HttpGet]
public ActionResult<IEnumerable<Producto>> GetAll()
{
    return Ok(_productos);
}

// Obtener uno específico
[HttpGet("{id}")]
public ActionResult<Producto> GetById(int id)
{
    var producto = _productos.FirstOrDefault(p => p.Id == id);
    if (producto == null)
        return NotFound();
    return Ok(producto);
}
```

### POST - Crear Recursos

```csharp
// POST: api/productos
[HttpPost]
public ActionResult<Producto> Create([FromBody] Producto producto)
{
    producto.Id = _productos.Max(p => p.Id) + 1;
    producto.FechaCreacion = DateTime.Now;
    _productos.Add(producto);
    
    return CreatedAtAction(
        nameof(GetById),
        new { id = producto.Id },
        producto
    );
}
```

**`CreatedAtAction` explicado**:
- Devuelve código 201 (Created)
- Incluye header `Location` con la URL del nuevo recurso
- Devuelve el objeto creado en el cuerpo

### PUT - Actualizar Recursos (Completo)

```csharp
// PUT: api/productos/5
[HttpPut("{id}")]
public ActionResult Update(int id, [FromBody] Producto producto)
{
    var existente = _productos.FirstOrDefault(p => p.Id == id);
    if (existente == null)
        return NotFound();
    
    existente.Nombre = producto.Nombre;
    existente.Precio = producto.Precio;
    existente.Descripcion = producto.Descripcion;
    
    return NoContent(); // 204 No Content
}
```

### PATCH - Actualizar Parcial (Opcional)

```csharp
// PATCH: api/productos/5
[HttpPatch("{id}")]
public ActionResult UpdateParcial(int id, [FromBody] JsonPatchDocument<Producto> patch)
{
    var producto = _productos.FirstOrDefault(p => p.Id == id);
    if (producto == null)
        return NotFound();
    
    patch.ApplyTo(producto);
    return NoContent();
}
```

### DELETE - Eliminar Recursos

```csharp
// DELETE: api/productos/5
[HttpDelete("{id}")]
public ActionResult Delete(int id)
{
    var producto = _productos.FirstOrDefault(p => p.Id == id);
    if (producto == null)
        return NotFound();
    
    _productos.Remove(producto);
    return NoContent(); // 204 No Content
}
```

## Modelos y DTOs

### ¿Qué son los DTOs?

**DTO** (Data Transfer Object) es un objeto diseñado específicamente para transferir datos entre capas o a través de la red.

**¿Por qué usar DTOs?**
- Controlar exactamente qué datos expones
- Evitar exponer propiedades internas
- Diferentes representaciones para entrada y salida

### Ejemplo: Producto

**Modelo de Dominio** (entidad interna):
```csharp
public class Producto
{
    public int Id { get; set; }
    public string Nombre { get; set; }
    public decimal Precio { get; set; }
    public decimal PrecioCosto { get; set; } // No queremos exponerlo
    public int Stock { get; set; }
    public DateTime FechaCreacion { get; set; }
    public DateTime? FechaModificacion { get; set; }
    public bool Activo { get; set; }
}
```

**DTO para Lectura** (lo que devuelves al cliente):
```csharp
public class ProductoDTO
{
    public int Id { get; set; }
    public string Nombre { get; set; }
    public decimal Precio { get; set; }
    public bool DisponibleEnStock => Stock > 0;
    public int Stock { get; set; }
}
```

**DTO para Creación** (lo que el cliente envía):
```csharp
public class ProductoCreateDTO
{
    [Required]
    [MaxLength(100)]
    public string Nombre { get; set; }
    
    [Required]
    [Range(0.01, 999999)]
    public decimal Precio { get; set; }
    
    [Range(0, int.MaxValue)]
    public int Stock { get; set; }
}
```

**DTO para Actualización**:
```csharp
public class ProductoUpdateDTO
{
    [MaxLength(100)]
    public string? Nombre { get; set; }
    
    [Range(0.01, 999999)]
    public decimal? Precio { get; set; }
    
    [Range(0, int.MaxValue)]
    public int? Stock { get; set; }
}
```

### Usando DTOs en Controladores

```csharp
[ApiController]
[Route("api/[controller]")]
public class ProductosController : ControllerBase
{
    private static List<Producto> _productos = new();
    
    [HttpGet]
    public ActionResult<IEnumerable<ProductoDTO>> GetAll()
    {
        var productosDTO = _productos.Select(p => new ProductoDTO
        {
            Id = p.Id,
            Nombre = p.Nombre,
            Precio = p.Precio,
            Stock = p.Stock
        });
        
        return Ok(productosDTO);
    }
    
    [HttpPost]
    public ActionResult<ProductoDTO> Create([FromBody] ProductoCreateDTO createDTO)
    {
        var producto = new Producto
        {
            Id = _productos.Any() ? _productos.Max(p => p.Id) + 1 : 1,
            Nombre = createDTO.Nombre,
            Precio = createDTO.Precio,
            Stock = createDTO.Stock,
            FechaCreacion = DateTime.Now,
            Activo = true
        };
        
        _productos.Add(producto);
        
        var productoDTO = new ProductoDTO
        {
            Id = producto.Id,
            Nombre = producto.Nombre,
            Precio = producto.Precio,
            Stock = producto.Stock
        };
        
        return CreatedAtAction(nameof(GetById), new { id = producto.Id }, productoDTO);
    }
}
```

## Organizando Controladores

### Separación por Recurso

```
Controllers/
├── ProductosController.cs
├── CategoriasController.cs
├── ClientesController.cs
└── PedidosController.cs
```

Cada controlador maneja un recurso específico.

### Controladores Anidados

Para recursos relacionados:

```csharp
// GET: api/categorias/5/productos
[HttpGet("api/categorias/{categoriaId}/productos")]
public ActionResult<IEnumerable<Producto>> GetProductosPorCategoria(int categoriaId)
{
    // Devolver productos de una categoría
}
```

## Conceptos clave para recordar

- 🔑 **Ruta**: Dirección para acceder a un endpoint
- 🔑 **[Route]**: Atributo para definir rutas
- 🔑 **Parámetros de ruta**: Valores dinámicos en la URL ({id})
- 🔑 **Query parameters**: Parámetros opcionales (?pagina=1)
- 🔑 **DTO**: Objeto para transferir datos, diferente del modelo de dominio
- 🔑 **POST**: Crear recursos (código 201)
- 🔑 **PUT**: Actualizar completamente (código 200/204)
- 🔑 **PATCH**: Actualizar parcialmente
- 🔑 **DELETE**: Eliminar recursos (código 204)
- 🔑 **CreatedAtAction**: Devuelve 201 con Location header

## Próximos pasos

En el siguiente módulo aprenderás sobre persistencia de datos con bases de datos reales usando Entity Framework Core.

¡Ahora tienes el conocimiento para diseñar APIs profesionales! 🚀
