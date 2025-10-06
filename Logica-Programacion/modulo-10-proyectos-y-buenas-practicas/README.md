# Módulo 10: Proyectos y Buenas Prácticas

## Introducción

¡Felicitaciones por llegar al módulo final! Aquí consolidarás todo lo aprendido en un proyecto integrador y aprenderás las mejores prácticas de la industria que te convertirán en un programador profesional.

## Conceptos Principales

### 1. Estilo de código

**Convenciones de nomenclatura:**

```
// Variables y funciones: camelCase o snake_case
nombre_usuario = "Ana"
calcular_promedio()

// Constantes: MAYÚSCULAS
PI = 3.14159
MAX_INTENTOS = 3

// Clases (conceptual): PascalCase
UsuarioPremium
GestorDeArchivos
```

**Indentación y espacios:**

```
// Bien indentado
SI condicion ENTONCES
    hacer_algo()
    SI otra_condicion ENTONCES
        hacer_otra_cosa()
    FIN SI
FIN SI

// Usa espacios alrededor de operadores
resultado = a + b * c
SI x == 10 ENTONCES
```

### 2. Documentación

**Comentarios efectivos:**

```
// Malo: Explica lo obvio
contador = contador + 1  // Incrementa contador

// Bueno: Explica el por qué
contador = contador + 1  // Necesitamos contar desde 1, no desde 0

// Excelente: Documenta funciones
FUNCION calcular_imc(peso, altura):
    /**
     * Calcula el Índice de Masa Corporal
     * 
     * Parámetros:
     *   peso: Peso en kilogramos (número positivo)
     *   altura: Altura en metros (número positivo)
     * 
     * Retorna:
     *   IMC calculado (número decimal)
     * 
     * Ejemplo:
     *   calcular_imc(70, 1.75) retorna 22.86
     */
    RETORNAR peso / (altura * altura)
FIN FUNCION
```

### 3. Testing y depuración

**Tipos de pruebas:**

**1. Pruebas unitarias** - Prueban funciones individuales:
```
FUNCION test_sumar():
    resultado = sumar(2, 3)
    SI resultado == 5 ENTONCES
        ESCRIBIR "✓ Test pasado"
    SINO
        ESCRIBIR "✗ Test fallido"
    FIN SI
FIN FUNCION
```

**2. Pruebas de integración** - Prueban componentes juntos:
```
FUNCION test_sistema_completo():
    inicializar_sistema()
    agregar_usuario("Ana")
    agregar_producto("Libro")
    resultado = procesar_compra("Ana", "Libro")
    verificar_resultado(resultado)
FIN FUNCION
```

**Técnicas de depuración:**

```
// 1. Imprimir valores
ESCRIBIR "Debug: valor de x =", x

// 2. Verificar condiciones
ESCRIBIR "Debug: condicion es", (x > 10)

// 3. Rastrear flujo
ESCRIBIR "Debug: entrando a función X"
// código
ESCRIBIR "Debug: saliendo de función X"
```

### 4. Optimización

**Principios de optimización:**

**1. Primero que funcione, luego optimiza:**
```
// Versión 1: Simple y clara
FUNCION buscar_simple(lista, elemento):
    PARA CADA item EN lista HACER
        SI item == elemento ENTONCES
            RETORNAR Verdadero
        FIN SI
    FIN PARA
    RETORNAR Falso
FIN FUNCION

// Versión 2: Optimizada (solo si es necesario)
FUNCION buscar_optimizada(lista_ordenada, elemento):
    // Usa búsqueda binaria
    RETORNAR busqueda_binaria(lista_ordenada, elemento)
FIN FUNCION
```

**2. Evita optimización prematura:**
- Optimiza solo cuando sea necesario
- Mide antes de optimizar
- Mantén la claridad

**3. Cache de resultados:**
```
// Fibonacci con cache
cache = {}

FUNCION fibonacci_optimizado(n):
    SI n EN cache ENTONCES
        RETORNAR cache[n]
    FIN SI
    
    SI n <= 1 ENTONCES
        RETORNAR n
    FIN SI
    
    resultado = fibonacci_optimizado(n-1) + fibonacci_optimizado(n-2)
    cache[n] = resultado
    RETORNAR resultado
FIN FUNCION
```

## Proyecto Final Completo

### Sistema de Gestión de Biblioteca

```
// ============================================
// SISTEMA DE GESTIÓN DE BIBLIOTECA
// ============================================

// --- ESTRUCTURAS DE DATOS ---

libros = []
usuarios = []
prestamos = []
siguiente_id_libro = 1
siguiente_id_usuario = 1

// --- FUNCIONES DE LIBROS ---

FUNCION agregar_libro(titulo, autor, isbn):
    /**
     * Agrega un nuevo libro a la biblioteca
     */
    libro = {
        "id": siguiente_id_libro,
        "titulo": titulo,
        "autor": autor,
        "isbn": isbn,
        "disponible": Verdadero
    }
    libros.agregar(libro)
    siguiente_id_libro = siguiente_id_libro + 1
    ESCRIBIR "✓ Libro agregado con ID:", libro["id"]
    RETORNAR libro["id"]
FIN FUNCION

FUNCION buscar_libro_por_id(id):
    PARA CADA libro EN libros HACER
        SI libro["id"] == id ENTONCES
            RETORNAR libro
        FIN SI
    FIN PARA
    RETORNAR Nulo
FIN FUNCION

FUNCION listar_libros_disponibles():
    ESCRIBIR "=== LIBROS DISPONIBLES ==="
    contador = 0
    PARA CADA libro EN libros HACER
        SI libro["disponible"] ENTONCES
            ESCRIBIR libro["id"], "-", libro["titulo"], "por", libro["autor"]
            contador = contador + 1
        FIN SI
    FIN PARA
    
    SI contador == 0 ENTONCES
        ESCRIBIR "No hay libros disponibles"
    FIN SI
FIN FUNCION

// --- FUNCIONES DE USUARIOS ---

FUNCION registrar_usuario(nombre, email):
    /**
     * Registra un nuevo usuario en el sistema
     */
    // Validar email
    SI NO validar_email(email) ENTONCES
        ESCRIBIR "✗ Email inválido"
        RETORNAR Nulo
    FIN SI
    
    usuario = {
        "id": siguiente_id_usuario,
        "nombre": nombre,
        "email": email,
        "prestamos_activos": 0
    }
    usuarios.agregar(usuario)
    siguiente_id_usuario = siguiente_id_usuario + 1
    ESCRIBIR "✓ Usuario registrado con ID:", usuario["id"]
    RETORNAR usuario["id"]
FIN FUNCION

FUNCION buscar_usuario_por_id(id):
    PARA CADA usuario EN usuarios HACER
        SI usuario["id"] == id ENTONCES
            RETORNAR usuario
        FIN SI
    FIN PARA
    RETORNAR Nulo
FIN FUNCION

// --- FUNCIONES DE PRÉSTAMOS ---

FUNCION procesar_prestamo(id_usuario, id_libro):
    /**
     * Procesa un nuevo préstamo de libro
     * Validaciones:
     * - Usuario existe
     * - Libro existe y está disponible
     * - Usuario no excede límite de préstamos (3)
     */
    
    // Buscar usuario
    usuario = buscar_usuario_por_id(id_usuario)
    SI usuario == Nulo ENTONCES
        ESCRIBIR "✗ Usuario no encontrado"
        RETORNAR Falso
    FIN SI
    
    // Verificar límite de préstamos
    SI usuario["prestamos_activos"] >= 3 ENTONCES
        ESCRIBIR "✗ Usuario ha alcanzado el límite de préstamos"
        RETORNAR Falso
    FIN SI
    
    // Buscar libro
    libro = buscar_libro_por_id(id_libro)
    SI libro == Nulo ENTONCES
        ESCRIBIR "✗ Libro no encontrado"
        RETORNAR Falso
    FIN SI
    
    // Verificar disponibilidad
    SI NO libro["disponible"] ENTONCES
        ESCRIBIR "✗ Libro no disponible"
        RETORNAR Falso
    FIN SI
    
    // Procesar préstamo
    fecha_actual = obtener_fecha_actual()
    fecha_devolucion = fecha_actual + 15  // 15 días
    
    prestamo = {
        "id_usuario": id_usuario,
        "id_libro": id_libro,
        "fecha_prestamo": fecha_actual,
        "fecha_devolucion": fecha_devolucion,
        "devuelto": Falso
    }
    
    prestamos.agregar(prestamo)
    libro["disponible"] = Falso
    usuario["prestamos_activos"] = usuario["prestamos_activos"] + 1
    
    ESCRIBIR "✓ Préstamo procesado exitosamente"
    ESCRIBIR "Fecha de devolución:", fecha_devolucion
    RETORNAR Verdadero
FIN FUNCION

FUNCION procesar_devolucion(id_usuario, id_libro):
    /**
     * Procesa la devolución de un libro
     */
    
    // Buscar préstamo activo
    prestamo_encontrado = Nulo
    PARA CADA prestamo EN prestamos HACER
        SI (prestamo["id_usuario"] == id_usuario) Y 
           (prestamo["id_libro"] == id_libro) Y
           (NO prestamo["devuelto"]) ENTONCES
            prestamo_encontrado = prestamo
            BREAK
        FIN SI
    FIN PARA
    
    SI prestamo_encontrado == Nulo ENTONCES
        ESCRIBIR "✗ Préstamo no encontrado"
        RETORNAR Falso
    FIN SI
    
    // Calcular multa si hay retraso
    fecha_actual = obtener_fecha_actual()
    SI fecha_actual > prestamo_encontrado["fecha_devolucion"] ENTONCES
        dias_retraso = fecha_actual - prestamo_encontrado["fecha_devolucion"]
        multa = dias_retraso * 1  // $1 por día
        ESCRIBIR "⚠ Devolución con retraso"
        ESCRIBIR "Días de retraso:", dias_retraso
        ESCRIBIR "Multa:", multa
    FIN SI
    
    // Procesar devolución
    prestamo_encontrado["devuelto"] = Verdadero
    libro = buscar_libro_por_id(id_libro)
    libro["disponible"] = Verdadero
    usuario = buscar_usuario_por_id(id_usuario)
    usuario["prestamos_activos"] = usuario["prestamos_activos"] - 1
    
    ESCRIBIR "✓ Devolución procesada exitosamente"
    RETORNAR Verdadero
FIN FUNCION

// --- FUNCIONES DE REPORTES ---

FUNCION generar_reporte_completo():
    ESCRIBIR "========================================"
    ESCRIBIR "   REPORTE GENERAL DE BIBLIOTECA"
    ESCRIBIR "========================================"
    ESCRIBIR ""
    
    ESCRIBIR "LIBROS:"
    ESCRIBIR "  Total:", longitud(libros)
    disponibles = contar_libros_disponibles()
    ESCRIBIR "  Disponibles:", disponibles
    ESCRIBIR "  Prestados:", longitud(libros) - disponibles
    ESCRIBIR ""
    
    ESCRIBIR "USUARIOS:"
    ESCRIBIR "  Total registrados:", longitud(usuarios)
    ESCRIBIR ""
    
    ESCRIBIR "PRÉSTAMOS:"
    activos = contar_prestamos_activos()
    ESCRIBIR "  Activos:", activos
    ESCRIBIR "  Total histórico:", longitud(prestamos)
    ESCRIBIR ""
FIN FUNCION

// --- FUNCIONES AUXILIARES ---

FUNCION validar_email(email):
    // Validación simple: debe contener @
    RETORNAR "@" EN email
FIN FUNCION

FUNCION contar_libros_disponibles():
    contador = 0
    PARA CADA libro EN libros HACER
        SI libro["disponible"] ENTONCES
            contador = contador + 1
        FIN SI
    FIN PARA
    RETORNAR contador
FIN FUNCION

FUNCION contar_prestamos_activos():
    contador = 0
    PARA CADA prestamo EN prestamos HACER
        SI NO prestamo["devuelto"] ENTONCES
            contador = contador + 1
        FIN SI
    FIN PARA
    RETORNAR contador
FIN FUNCION

FUNCION obtener_fecha_actual():
    // Simulación - en implementación real obtendría la fecha del sistema
    RETORNAR 15  // Día 15 del mes
FIN FUNCION

// --- MENÚ PRINCIPAL ---

FUNCION mostrar_menu():
    ESCRIBIR "========================================"
    ESCRIBIR "   SISTEMA DE GESTIÓN DE BIBLIOTECA"
    ESCRIBIR "========================================"
    ESCRIBIR "1. Agregar libro"
    ESCRIBIR "2. Registrar usuario"
    ESCRIBIR "3. Procesar préstamo"
    ESCRIBIR "4. Procesar devolución"
    ESCRIBIR "5. Listar libros disponibles"
    ESCRIBIR "6. Generar reporte"
    ESCRIBIR "7. Salir"
    ESCRIBIR "========================================"
    ESCRIBIR "Seleccione una opción:"
FIN FUNCION

// --- PROGRAMA PRINCIPAL ---

INICIO
    ESCRIBIR "Iniciando Sistema de Biblioteca..."
    ESCRIBIR ""
    
    // Datos de ejemplo
    agregar_libro("Cien años de soledad", "Gabriel García Márquez", "978-0307474728")
    agregar_libro("Don Quijote", "Miguel de Cervantes", "978-8424936464")
    agregar_libro("1984", "George Orwell", "978-0451524935")
    
    opcion = 0
    MIENTRAS opcion != 7 HACER
        mostrar_menu()
        LEER opcion
        ESCRIBIR ""
        
        SI opcion == 1 ENTONCES
            ESCRIBIR "Título del libro:"
            LEER titulo
            ESCRIBIR "Autor:"
            LEER autor
            ESCRIBIR "ISBN:"
            LEER isbn
            agregar_libro(titulo, autor, isbn)
            
        SINO SI opcion == 2 ENTONCES
            ESCRIBIR "Nombre del usuario:"
            LEER nombre
            ESCRIBIR "Email:"
            LEER email
            registrar_usuario(nombre, email)
            
        SINO SI opcion == 3 ENTONCES
            ESCRIBIR "ID del usuario:"
            LEER id_usuario
            ESCRIBIR "ID del libro:"
            LEER id_libro
            procesar_prestamo(id_usuario, id_libro)
            
        SINO SI opcion == 4 ENTONCES
            ESCRIBIR "ID del usuario:"
            LEER id_usuario
            ESCRIBIR "ID del libro:"
            LEER id_libro
            procesar_devolucion(id_usuario, id_libro)
            
        SINO SI opcion == 5 ENTONCES
            listar_libros_disponibles()
            
        SINO SI opcion == 6 ENTONCES
            generar_reporte_completo()
            
        SINO SI opcion == 7 ENTONCES
            ESCRIBIR "¡Gracias por usar el sistema!"
            
        SINO
            ESCRIBIR "✗ Opción inválida"
        FIN SI
        
        ESCRIBIR ""
        ESCRIBIR "Presione Enter para continuar..."
        LEER  // Pausa
    FIN MIENTRAS
FIN
```

## Mejores Prácticas Profesionales

### 1. Código Limpio
- Nombres descriptivos
- Funciones pequeñas y enfocadas
- Evitar duplicación (DRY - Don't Repeat Yourself)

### 2. Mantenibilidad
- Comentarios útiles
- Estructura clara
- Fácil de modificar

### 3. Escalabilidad
- Diseño modular
- Estructuras de datos eficientes
- Código reutilizable

### 4. Confiabilidad
- Validación de entradas
- Manejo de errores
- Pruebas exhaustivas

## Conceptos Clave

- 🔑 **Estilo de código**: Convenciones y formato
- 🔑 **Documentación**: Comentarios y explicaciones
- 🔑 **Testing**: Pruebas unitarias e integración
- 🔑 **Optimización**: Mejorar rendimiento
- 🔑 **Buenas prácticas**: Código profesional

## Motivación Final

¡FELICITACIONES! 🎉🎊 Has completado el curso de Lógica de Programación.

Ya no eres un principiante. Ahora tienes las herramientas para:
- ✨ Pensar computacionalmente
- ✨ Resolver problemas complejos
- ✨ Escribir código limpio y eficiente
- ✨ Diseñar sistemas completos
- ✨ Seguir aprendiendo por tu cuenta

## Tu Próximo Paso

Este es solo el comienzo. Ahora puedes:

1. **Aprender un lenguaje de programación específico**
   - Python, JavaScript, Java, C++, etc.
   - La lógica que aprendiste aplica a todos

2. **Especialízarte**
   - Desarrollo web
   - Ciencia de datos
   - Inteligencia artificial
   - Desarrollo móvil
   - Y mucho más...

3. **Practicar constantemente**
   - Resuelve problemas en plataformas online
   - Crea tus propios proyectos
   - Contribuye a proyectos open source

> "El viaje de mil millas comienza con un solo paso. Tú ya diste muchos pasos. Ahora, ¡sigue caminando!" - Lao Tzu

**¡Estás listo para conquistar el mundo de la programación! 🚀💻**

**¡Feliz código!** 👨‍💻👩‍💻
