# Módulo 5: Persistencia de Datos - Introducción a Bases de Datos

## ¡Es hora de guardar datos de verdad!

Hasta ahora, tus datos se guardaban en memoria y se perdían al reiniciar la API. Es momento de aprender a **persistir datos** en una base de datos real usando **Entity Framework Core**.

**Analogía del día**: Imagina que tu restaurante hasta ahora solo tomaba pedidos en papelitos que se perdían al cerrar. Ahora vas a implementar un **sistema de registro permanente** donde todo queda guardado.

## ¿Qué es Entity Framework Core?

**Entity Framework Core** (EF Core) es un ORM (Object-Relational Mapper) que te permite:
- Trabajar con bases de datos usando objetos C#
- No escribir SQL manualmente (aunque puedes si quieres)
- Cambiar fácilmente de base de datos (SQL Server, PostgreSQL, SQLite, etc.)

**Analogía**: EF Core es como un **traductor automático** entre tu código C# y la base de datos.

## Configurando Entity Framework Core

### Paso 1: Instalar paquetes NuGet

```bash
# En la carpeta de tu proyecto
dotnet add package Microsoft.EntityFrameworkCore
dotnet add package Microsoft.EntityFrameworkCore.SqlServer
dotnet add package Microsoft.EntityFrameworkCore.Tools
dotnet add package Microsoft.EntityFrameworkCore.Design
```

**Para SQLite (más simple para aprender)**:
```bash
dotnet add package Microsoft.EntityFrameworkCore.Sqlite
```

### Paso 2: Crear el DbContext

El `DbContext` es el puente entre tu aplicación y la base de datos:

```csharp
using Microsoft.EntityFrameworkCore;

public class ApplicationDbContext : DbContext
{
    public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
        : base(options)
    {
    }

    public DbSet<Producto> Productos { get; set; }
    public DbSet<Categoria> Categorias { get; set; }
    
    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        // Configuraciones adicionales
        modelBuilder.Entity<Producto>()
            .Property(p => p.Precio)
            .HasColumnType("decimal(18,2)");
    }
}
```

### Paso 3: Configurar en Program.cs

```csharp
// Agregar el DbContext al contenedor de servicios
builder.Services.AddDbContext<ApplicationDbContext>(options =>
    options.UseSqlite("Data Source=miapi.db"));
    // o UseSqlServer para SQL Server
```

## Migraciones

Las **migraciones** son como "versiones" de tu base de datos.

### Crear una migración

```bash
dotnet ef migrations add InicialCreate
```

Esto genera archivos que describen los cambios en la base de datos.

### Aplicar migraciones

```bash
dotnet ef database update
```

Esto crea o actualiza la base de datos según las migraciones.

## Usando EF Core en Controladores

### Inyección de Dependencias

```csharp
[ApiController]
[Route("api/[controller]")]
public class ProductosController : ControllerBase
{
    private readonly ApplicationDbContext _context;
    
    public ProductosController(ApplicationDbContext context)
    {
        _context = context;
    }
    
    [HttpGet]
    public async Task<ActionResult<IEnumerable<Producto>>> GetProductos()
    {
        var productos = await _context.Productos.ToListAsync();
        return Ok(productos);
    }
    
    [HttpGet("{id}")]
    public async Task<ActionResult<Producto>> GetProducto(int id)
    {
        var producto = await _context.Productos.FindAsync(id);
        
        if (producto == null)
            return NotFound();
            
        return Ok(producto);
    }
    
    [HttpPost]
    public async Task<ActionResult<Producto>> CreateProducto(Producto producto)
    {
        _context.Productos.Add(producto);
        await _context.SaveChangesAsync();
        
        return CreatedAtAction(nameof(GetProducto), new { id = producto.Id }, producto);
    }
    
    [HttpPut("{id}")]
    public async Task<ActionResult> UpdateProducto(int id, Producto producto)
    {
        if (id != producto.Id)
            return BadRequest();
            
        _context.Entry(producto).State = EntityState.Modified;
        await _context.SaveChangesAsync();
        
        return NoContent();
    }
    
    [HttpDelete("{id}")]
    public async Task<ActionResult> DeleteProducto(int id)
    {
        var producto = await _context.Productos.FindAsync(id);
        if (producto == null)
            return NotFound();
            
        _context.Productos.Remove(producto);
        await _context.SaveChangesAsync();
        
        return NoContent();
    }
}
```

## Relaciones entre Modelos

### Uno a Muchos

```csharp
public class Categoria
{
    public int Id { get; set; }
    public string Nombre { get; set; }
    
    // Navegación
    public ICollection<Producto> Productos { get; set; }
}

public class Producto
{
    public int Id { get; set; }
    public string Nombre { get; set; }
    public decimal Precio { get; set; }
    
    // Clave foránea
    public int CategoriaId { get; set; }
    
    // Navegación
    public Categoria Categoria { get; set; }
}
```

### Consultas con Include

```csharp
var productos = await _context.Productos
    .Include(p => p.Categoria)
    .ToListAsync();
```

## Conceptos clave para recordar

- 🔑 **EF Core**: ORM para trabajar con bases de datos
- 🔑 **DbContext**: Punto de acceso a la base de datos
- 🔑 **DbSet**: Colección de entidades
- 🔑 **Migraciones**: Versionado de la base de datos
- 🔑 **async/await**: Operaciones asíncronas
- 🔑 **SaveChangesAsync**: Guarda cambios en la base de datos

## Próximos pasos

En el siguiente módulo implementarás un CRUD completo con base de datos.

¡Ahora tus datos persisten para siempre! 🗄️
