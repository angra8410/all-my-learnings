# Actividades Interactivas - Módulo 1: APIs y REST

## Sección 1: Preguntas de Opción Múltiple

### Pregunta 1
**¿Qué es una API?**

A) Un lenguaje de programación  
B) Un intermediario que permite la comunicación entre aplicaciones  
C) Una base de datos  
D) Un navegador web  

---

### Pregunta 2
**En la analogía del restaurante, ¿qué representa la API?**

A) El cliente que hace el pedido  
B) La cocina que prepara la comida  
C) El mesero que toma el pedido y trae la comida  
D) La carta del menú  

---

### Pregunta 3
**¿Cuál de los siguientes NO es un método HTTP estándar de REST?**

A) GET  
B) POST  
C) FETCH  
D) DELETE  

---

### Pregunta 4
**¿Qué significa que REST sea "sin estado" (stateless)?**

A) Que la API no funciona  
B) Que cada petición es independiente y no depende de peticiones anteriores  
C) Que no se pueden guardar datos  
D) Que el servidor no tiene base de datos  

---

### Pregunta 5
**¿Qué método HTTP usarías para obtener información de un usuario?**

A) POST  
B) DELETE  
C) GET  
D) PUT  

---

### Pregunta 6
**¿Qué método HTTP usarías para crear un nuevo producto en una tienda online?**

A) GET  
B) POST  
C) DELETE  
D) READ  

---

### Pregunta 7
**¿Cuál es el formato más común para intercambiar datos en APIs REST modernas?**

A) XML  
B) CSV  
C) JSON  
D) PDF  

---

### Pregunta 8
**¿Qué representa un "recurso" en una API REST?**

A) El servidor donde corre la API  
B) Cualquier información que puede ser nombrada (usuarios, productos, etc.)  
C) La memoria RAM del servidor  
D) El código fuente de la aplicación  

---

## Sección 2: Completa la Analogía

Completa las siguientes analogías basándote en lo que aprendiste:

### Analogía 1
**API es a Aplicaciones como __________ es a Personas**

A) Teléfono  
B) Computadora  
C) Internet  
D) Teclado  

---

### Analogía 2
**Cliente es a Petición como Servidor es a __________**

A) Pregunta  
B) Respuesta  
C) Error  
D) Código  

---

### Analogía 3
**GET es a "Leer" como POST es a __________**

A) Borrar  
B) Actualizar  
C) Crear  
D) Modificar  

---

### Analogía 4
**Cajero Automático es a Banco como API es a __________**

A) Cliente  
B) Servidor/Base de Datos  
C) Internet  
D) Computadora  

---

### Analogía 5
**Menú de Restaurante es a Platillos como API es a __________**

A) Servidores  
B) Recursos/Endpoints  
C) Clientes  
D) Bases de datos  

---

## Sección 3: Asocia Términos con Definiciones

**Instrucciones**: Asocia cada término de la columna izquierda con su definición correcta de la columna derecha.

### Términos:
1. REST
2. API
3. Endpoint
4. GET
5. POST
6. JSON
7. Cliente
8. Servidor

### Definiciones:
A. Método HTTP para obtener información  
B. Formato común para intercambiar datos  
C. Estilo arquitectónico para diseñar APIs  
D. Quien hace las peticiones  
E. Interfaz que permite comunicación entre sistemas  
F. Método HTTP para crear nuevos recursos  
G. URL específica que representa un recurso  
H. Quien responde a las peticiones  

**Tu respuesta:**
- 1 → ___
- 2 → ___
- 3 → ___
- 4 → ___
- 5 → ___
- 6 → ___
- 7 → ___
- 8 → ___

---

## Sección 4: Verdadero o Falso

Indica si las siguientes afirmaciones son **Verdaderas (V)** o **Falsas (F)**:

1. ___ Una API solo puede usarse en sitios web.

2. ___ REST requiere que cada petición contenga toda la información necesaria para ser procesada.

3. ___ El método DELETE se usa para actualizar información.

4. ___ JSON es el único formato que pueden usar las APIs REST.

5. ___ Una API puede servir tanto a una aplicación web como a una aplicación móvil.

6. ___ En REST, `/usuarios/123` representa el recurso del usuario con ID 123.

7. ___ El cliente necesita conocer cómo funciona internamente el servidor para usar una API.

8. ___ PUT se usa para actualizar información existente.

---

## Sección 5: Ejercicio Práctico - Inventa una API

**Instrucciones**: Diseña una API para un sistema de la vida cotidiana. Sigue el ejemplo y luego crea el tuyo.

### Ejemplo: API del Refrigerador 🧊

**Descripción**: Una API que permite gestionar los alimentos en un refrigerador inteligente.

**Recursos y Endpoints**:

1. **Listar todos los alimentos**
   - Método: GET
   - Endpoint: `/alimentos`
   - Respuesta: Lista de todos los alimentos en el refrigerador

2. **Obtener información de un alimento específico**
   - Método: GET
   - Endpoint: `/alimentos/123`
   - Respuesta: Detalles del alimento (nombre, fecha de vencimiento, cantidad)

3. **Agregar un nuevo alimento**
   - Método: POST
   - Endpoint: `/alimentos`
   - Datos a enviar: { "nombre": "Leche", "cantidad": 1, "vencimiento": "2024-12-31" }

4. **Actualizar un alimento existente**
   - Método: PUT
   - Endpoint: `/alimentos/123`
   - Datos a enviar: { "cantidad": 2 }

5. **Eliminar un alimento**
   - Método: DELETE
   - Endpoint: `/alimentos/123`

**Ejemplo de uso práctico**:
- Cuando sacas la leche del refrigerador, la app hace un DELETE
- Cuando compras nuevos alimentos, la app hace un POST
- Cuando quieres ver qué hay, la app hace un GET

---

### Tu turno: Crea tu propia API

**Elige uno de estos sistemas (o inventa el tuyo)**:
- Sistema de biblioteca personal (libros en tu casa)
- Sistema de lista de tareas
- Sistema de playlist de música
- Sistema de mascotas
- Sistema de plantas de tu jardín
- Tu propia idea: _______________

**Completa la siguiente plantilla**:

**Nombre de tu API**: _______________

**Descripción**: _______________

**Recursos y Endpoints** (completa al menos 4):

1. **Operación**: Listar todos los _______________
   - Método: ______
   - Endpoint: ______
   - Qué hace: _______________

2. **Operación**: Obtener uno específico
   - Método: ______
   - Endpoint: ______
   - Qué hace: _______________

3. **Operación**: Crear/Agregar nuevo(a) _______________
   - Método: ______
   - Endpoint: ______
   - Datos que necesita: _______________

4. **Operación**: Actualizar un(a) _______________
   - Método: ______
   - Endpoint: ______
   - Datos que necesita: _______________

5. **Operación**: Eliminar un(a) _______________
   - Método: ______
   - Endpoint: ______
   - Qué hace: _______________

**Caso de uso práctico** (escribe un ejemplo de cómo se usaría tu API):
_______________________________________________
_______________________________________________

---

## Sección 6: Pensamiento Crítico

### Pregunta 1
**Piensa en una aplicación que uses frecuentemente (Instagram, WhatsApp, Netflix, etc.). Describe 3 operaciones que crees que esa aplicación hace usando APIs.**

Tu respuesta:
1. _______________________________________________
2. _______________________________________________
3. _______________________________________________

---

### Pregunta 2
**¿Por qué crees que es importante que una API sea "sin estado" (stateless)?**

Tu respuesta:
_______________________________________________
_______________________________________________
_______________________________________________

---

### Pregunta 3
**¿Qué ventajas tiene usar JSON en lugar de enviar los datos en texto plano?**

Tu respuesta:
_______________________________________________
_______________________________________________
_______________________________________________

---

## Sección 7: Diagrama - Completa el Flujo

**Instrucciones**: Completa el siguiente diagrama con las palabras faltantes.

```
1. El __________ envía una petición HTTP
        ↓
2. La __________ recibe la petición
        ↓
3. La API __________ la petición
        ↓
4. La API consulta la __________
        ↓
5. La API construye una __________
        ↓
6. El cliente __________ la respuesta
```

**Banco de palabras**: API, Cliente, Base de Datos, Respuesta, Valida/Procesa, Recibe

---

## Sección 8: Caso Práctico - Tienda Online

Imagina que estás diseñando la API para una tienda online simple.

### Escenario 1: Un cliente quiere ver todos los productos disponibles
- ¿Qué método HTTP usarías? _______________
- ¿Cuál sería el endpoint? _______________
- ¿Qué tipo de respuesta esperarías? _______________

### Escenario 2: Un cliente quiere agregar un producto al carrito
- ¿Qué método HTTP usarías? _______________
- ¿Cuál sería el endpoint? _______________
- ¿Qué datos necesitarías enviar? _______________

### Escenario 3: Un cliente quiere actualizar la cantidad de un producto en su carrito
- ¿Qué método HTTP usarías? _______________
- ¿Cuál sería el endpoint? _______________
- ¿Qué datos necesitarías enviar? _______________

### Escenario 4: Un cliente quiere eliminar un producto de su carrito
- ¿Qué método HTTP usarías? _______________
- ¿Cuál sería el endpoint? _______________

---

## Reflexión Final

**¿Qué fue lo más interesante que aprendiste en este módulo?**
_______________________________________________
_______________________________________________

**¿Qué concepto te gustaría explorar más a fondo?**
_______________________________________________
_______________________________________________

**¿Cómo aplicarías lo aprendido en un proyecto personal?**
_______________________________________________
_______________________________________________

---

¡Excelente trabajo! Una vez que completes estas actividades, revisa tus respuestas en el archivo `retroalimentacion.md`. 🎉
