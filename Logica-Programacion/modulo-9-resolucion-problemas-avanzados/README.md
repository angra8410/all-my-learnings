# Módulo 9: Resolución de Problemas Avanzados

## Introducción

¡Bienvenido al penúltimo módulo! Aquí integrarás todo lo aprendido para resolver problemas complejos del mundo real. Aprenderás estrategias y técnicas profesionales de resolución de problemas.

## Conceptos Principales

### 1. Análisis de problemas

Antes de programar, **analiza** el problema:

**Pasos del análisis:**
1. **Comprender**: ¿Qué pide el problema?
2. **Identificar entradas**: ¿Qué datos necesito?
3. **Identificar salidas**: ¿Qué debo producir?
4. **Identificar restricciones**: ¿Qué limitaciones hay?
5. **Dividir**: Descomponer en subproblemas

**Ejemplo: Sistema de biblioteca**

**Problema:** Gestionar préstamos de libros

**Análisis:**
- **Entradas**: Datos de libros, usuarios, fechas
- **Salidas**: Confirmaciones, reportes, alertas
- **Restricciones**: Un usuario máximo 3 libros, 15 días de préstamo
- **Subproblemas**:
  - Registrar libros
  - Registrar usuarios
  - Procesar préstamos
  - Procesar devoluciones
  - Calcular multas

### 2. Diseño de soluciones

**Estrategias de diseño:**

**Top-Down (De arriba hacia abajo):**
```
Sistema_Biblioteca
├── Gestión_Libros
│   ├── Agregar_Libro
│   ├── Buscar_Libro
│   └── Eliminar_Libro
├── Gestión_Usuarios
│   ├── Registrar_Usuario
│   └── Buscar_Usuario
└── Gestión_Préstamos
    ├── Procesar_Préstamo
    ├── Procesar_Devolución
    └── Calcular_Multa
```

**Bottom-Up (De abajo hacia arriba):**
- Crear funciones básicas primero
- Combinarlas para funcionalidad compleja

### 3. Optimización de algoritmos

**Técnicas de optimización:**

**1. Evita cálculos repetidos:**
```
// Malo
PARA i DESDE 0 HASTA n HACER
    SI es_primo(i) ENTONCES  // Llama es_primo cada vez
        ESCRIBIR i
    FIN SI
FIN PARA

// Mejor
primos = calcular_primos(n)  // Calcula una vez
PARA CADA primo EN primos HACER
    ESCRIBIR primo
FIN PARA
```

**2. Usa estructuras de datos apropiadas:**
```
// Para buscar frecuentemente: usa diccionario/mapa
// Para acceso secuencial: usa lista/arreglo
// Para elementos únicos: usa conjunto/set
```

**3. Sal temprano de bucles:**
```
FUNCION buscar(lista, elemento):
    PARA CADA item EN lista HACER
        SI item == elemento ENTONCES
            RETORNAR Verdadero  // Sal inmediatamente
        FIN SI
    FIN PARA
    RETORNAR Falso
FIN FUNCION
```

### 4. Complejidad temporal

**Notación Big O** - mide eficiencia de algoritmos:

- **O(1)**: Constante - excelente
  ```
  acceso = lista[5]
  ```

- **O(log n)**: Logarítmica - muy buena
  ```
  busqueda_binaria(lista, elemento)
  ```

- **O(n)**: Lineal - buena
  ```
  PARA CADA elemento EN lista
  ```

- **O(n log n)**: Lineal logarítmica - aceptable
  ```
  ordenamiento_rapido(lista)
  ```

- **O(n²)**: Cuadrática - lenta para datos grandes
  ```
  PARA i EN lista
      PARA j EN lista
  ```

- **O(2ⁿ)**: Exponencial - evitar
  ```
  fibonacci_recursivo_ingenuo(n)
  ```

## Implementación Práctica

### Ejercicio 1: Sistema de gestión

**Sistema de inventario de tienda**

```
// Estructuras de datos
productos = []
inventario = {}  // {producto_id: cantidad}

// Funciones principales
FUNCION agregar_producto(id, nombre, precio):
    producto = {
        "id": id,
        "nombre": nombre,
        "precio": precio
    }
    productos.agregar(producto)
    inventario[id] = 0
FIN FUNCION

FUNCION actualizar_stock(id, cantidad):
    SI id EN inventario ENTONCES
        inventario[id] = inventario[id] + cantidad
        ESCRIBIR "Stock actualizado"
    SINO
        ESCRIBIR "Producto no existe"
    FIN SI
FIN FUNCION

FUNCION vender_producto(id, cantidad):
    SI id EN inventario ENTONCES
        SI inventario[id] >= cantidad ENTONCES
            inventario[id] = inventario[id] - cantidad
            buscar_precio(id, cantidad)
            RETORNAR Verdadero
        SINO
            ESCRIBIR "Stock insuficiente"
            RETORNAR Falso
        FIN SI
    FIN SI
FIN FUNCION

FUNCION buscar_precio(id, cantidad):
    PARA CADA producto EN productos HACER
        SI producto["id"] == id ENTONCES
            total = producto["precio"] * cantidad
            ESCRIBIR "Total:", total
            RETORNAR total
        FIN SI
    FIN PARA
FIN FUNCION

FUNCION generar_reporte():
    ESCRIBIR "=== REPORTE DE INVENTARIO ==="
    PARA CADA producto EN productos HACER
        id = producto["id"]
        stock = inventario[id]
        ESCRIBIR producto["nombre"], "- Stock:", stock
    FIN PARA
FIN FUNCION
```

### Ejercicio 2: Análisis de datos

**Análisis de calificaciones de estudiantes**

```
FUNCION analizar_calificaciones(calificaciones):
    // Estadísticas básicas
    total = longitud(calificaciones)
    suma = 0
    maximo = calificaciones[0]
    minimo = calificaciones[0]
    
    PARA CADA nota EN calificaciones HACER
        suma = suma + nota
        SI nota > maximo ENTONCES
            maximo = nota
        FIN SI
        SI nota < minimo ENTONCES
            minimo = nota
        FIN SI
    FIN PARA
    
    promedio = suma / total
    
    // Distribución
    aprobados = 0
    reprobados = 0
    
    PARA CADA nota EN calificaciones HACER
        SI nota >= 60 ENTONCES
            aprobados = aprobados + 1
        SINO
            reprobados = reprobados + 1
        FIN SI
    FIN PARA
    
    // Reporte
    ESCRIBIR "=== ANÁLISIS DE CALIFICACIONES ==="
    ESCRIBIR "Total estudiantes:", total
    ESCRIBIR "Promedio:", promedio
    ESCRIBIR "Nota máxima:", maximo
    ESCRIBIR "Nota mínima:", minimo
    ESCRIBIR "Aprobados:", aprobados, "(", (aprobados*100/total), "%)"
    ESCRIBIR "Reprobados:", reprobados, "(", (reprobados*100/total), "%)"
FIN FUNCION
```

### Ejercicio 3: Proyecto integrador

**Sistema de reservas de hotel**

```
// Variables globales
habitaciones = {}  // {numero: estado}
reservas = []

FUNCION inicializar_hotel(total_habitaciones):
    PARA i DESDE 1 HASTA total_habitaciones HACER
        habitaciones[i] = "disponible"
    FIN PARA
FIN FUNCION

FUNCION mostrar_disponibles():
    ESCRIBIR "=== HABITACIONES DISPONIBLES ==="
    PARA CADA numero, estado EN habitaciones HACER
        SI estado == "disponible" ENTONCES
            ESCRIBIR "Habitación", numero
        FIN SI
    FIN PARA
FIN FUNCION

FUNCION hacer_reserva(habitacion, nombre, dias):
    SI habitacion EN habitaciones ENTONCES
        SI habitaciones[habitacion] == "disponible" ENTONCES
            habitaciones[habitacion] = "ocupada"
            reserva = {
                "habitacion": habitacion,
                "nombre": nombre,
                "dias": dias,
                "total": dias * 100  // $100 por día
            }
            reservas.agregar(reserva)
            ESCRIBIR "Reserva confirmada"
            ESCRIBIR "Total a pagar:", reserva["total"]
            RETORNAR Verdadero
        SINO
            ESCRIBIR "Habitación no disponible"
            RETORNAR Falso
        FIN SI
    SINO
        ESCRIBIR "Habitación no existe"
        RETORNAR Falso
    FIN SI
FIN FUNCION

FUNCION cancelar_reserva(habitacion):
    PARA i DESDE 0 HASTA longitud(reservas)-1 HACER
        SI reservas[i]["habitacion"] == habitacion ENTONCES
            habitaciones[habitacion] = "disponible"
            reservas.eliminar(i)
            ESCRIBIR "Reserva cancelada"
            RETORNAR Verdadero
        FIN SI
    FIN PARA
    ESCRIBIR "Reserva no encontrada"
    RETORNAR Falso
FIN FUNCION

// Programa principal
INICIO
    inicializar_hotel(10)
    
    opcion = 0
    MIENTRAS opcion != 5 HACER
        ESCRIBIR "=== SISTEMA DE RESERVAS ==="
        ESCRIBIR "1. Ver disponibles"
        ESCRIBIR "2. Hacer reserva"
        ESCRIBIR "3. Cancelar reserva"
        ESCRIBIR "4. Ver todas las reservas"
        ESCRIBIR "5. Salir"
        
        LEER opcion
        
        SI opcion == 1 ENTONCES
            mostrar_disponibles()
        SINO SI opcion == 2 ENTONCES
            LEER habitacion, nombre, dias
            hacer_reserva(habitacion, nombre, dias)
        SINO SI opcion == 3 ENTONCES
            LEER habitacion
            cancelar_reserva(habitacion)
        // ... otras opciones
        FIN SI
    FIN MIENTRAS
FIN
```

## Mejores Prácticas

### 1. Divide y Conquista
- Divide problemas grandes en subproblemas
- Resuelve cada parte por separado
- Integra las soluciones

### 2. Piensa en Escalabilidad
- ¿Funcionará con 100 datos? ¿Con 10,000?
- Elige estructuras de datos apropiadas
- Optimiza puntos críticos

### 3. Maneja Errores
- Valida todas las entradas
- Prevé casos especiales
- Proporciona mensajes claros

### 4. Documenta tu Código
- Explica el "por qué", no solo el "qué"
- Documenta casos especiales
- Mantén la documentación actualizada

### 5. Prueba Exhaustivamente
- Casos normales
- Casos extremos (mínimos, máximos)
- Casos de error
- Casos límite

## Conceptos Clave

- 🔑 **Análisis**: Entender antes de programar
- 🔑 **Diseño**: Planificar la estructura
- 🔑 **Optimización**: Mejorar eficiencia
- 🔑 **Complejidad**: Medir rendimiento
- 🔑 **Integración**: Combinar componentes

## Próximos Pasos

En el Módulo 10 (final) aprenderás:
- Proyectos completos
- Buenas prácticas profesionales
- Estilo de código
- Testing y depuración

## Motivación Final

¡Extraordinario! 🎉 Ya puedes resolver problemas complejos del mundo real. Estás a un paso de completar este viaje.

**¡Eres un solucionador de problemas! 🧩💡**
