# Módulo 1: Introducción a las APIs y REST

## ¿Qué es una API?

Imagina que estás en un restaurante. Tú eres el **cliente**, la **cocina** es el sistema que prepara la comida, y el **mesero** es quien toma tu pedido y te trae lo que ordenaste. En este ejemplo, el mesero es como una **API** (Application Programming Interface - Interfaz de Programación de Aplicaciones).

Una **API** es un intermediario que permite que dos aplicaciones se comuniquen entre sí. Es como un "contrato" que define cómo puedes pedir información o servicios a un sistema, y cómo ese sistema te responderá.

### ¿Por qué existen las APIs?

Las APIs existen para:

1. **Facilitar la comunicación**: Permiten que diferentes sistemas (aplicaciones, sitios web, dispositivos) hablen entre sí sin importar cómo estén construidos internamente.

2. **Proteger la información**: No necesitas conocer cómo funciona internamente la cocina del restaurante (el servidor, la base de datos), solo necesitas saber cómo pedirle lo que necesitas.

3. **Reutilizar funcionalidad**: En lugar de reinventar la rueda, puedes usar servicios que otros ya crearon. Por ejemplo, usar la API de Google Maps para mostrar un mapa en tu aplicación.

4. **Escalar y mantener**: Si la cocina (el backend) necesita cambiar, mientras mantenga el mismo "menú" (interfaz), tú como cliente no te enteras del cambio.

### Ejemplo cotidiano: La Carta del Restaurante

Piensa en una **carta de restaurante**:
- La carta te muestra **qué puedes pedir** (los servicios disponibles)
- Cada platillo tiene un **nombre** (endpoint o ruta)
- Puedes hacer **peticiones especiales** (parámetros)
- El mesero te trae **exactamente lo que pediste** (respuesta)
- Si pides algo que no existe, te dicen que **no está disponible** (error 404)

¡Eso es exactamente cómo funciona una API!

## ¿Qué es REST?

**REST** (Representational State Transfer) es un estilo arquitectónico para diseñar APIs. Es como un conjunto de "buenas prácticas" o reglas que hacen que las APIs sean más fáciles de entender y usar.

### Principios básicos de REST:

1. **Cliente-Servidor**: Separación clara entre quien pide (cliente) y quien responde (servidor)

2. **Sin estado (Stateless)**: Cada petición es independiente. Es como si cada vez que pides en el restaurante, el mesero no recordara tu pedido anterior.

3. **Recursos**: Todo se trata como un "recurso" identificable. Por ejemplo:
   - `/usuarios` → La lista de usuarios
   - `/usuarios/123` → El usuario con ID 123
   - `/productos` → La lista de productos

4. **Métodos HTTP estándar**:
   - **GET**: "Dame información" (como ver la carta)
   - **POST**: "Crea algo nuevo" (como hacer un pedido)
   - **PUT**: "Actualiza algo completo" (como cambiar todo un pedido)
   - **DELETE**: "Elimina algo" (como cancelar un pedido)

5. **Representaciones**: Los datos se pueden devolver en diferentes formatos (JSON, XML, etc.). El más común hoy en día es **JSON**.

### Analogía: REST como un Sistema de Biblioteca

Imagina una biblioteca moderna:
- **GET** `/libros` → "Muéstrame todos los libros disponibles"
- **GET** `/libros/123` → "Muéstrame el libro con código 123"
- **POST** `/libros` → "Registra un nuevo libro en el sistema"
- **PUT** `/libros/123` → "Actualiza toda la información del libro 123"
- **DELETE** `/libros/123` → "Elimina el libro 123 del catálogo"

Cada operación es clara, predecible y fácil de entender.

## ¿Para qué sirven las APIs RESTful?

Las APIs RESTful se usan en casi todo lo que haces en internet:

1. **Redes Sociales**: Cuando publicas una foto en Instagram, tu app usa una API para enviarla al servidor.

2. **Aplicaciones Móviles**: Tu app del clima usa una API para obtener el pronóstico.

3. **E-commerce**: Amazon, Mercado Libre, etc., usan APIs para gestionar productos, carritos de compra y pagos.

4. **Servicios de Terceros**: Iniciar sesión con Google o Facebook en otras aplicaciones.

5. **IoT (Internet de las Cosas)**: Tu termostato inteligente usa una API para comunicarse con tu teléfono.

## Diagrama: Interacción Cliente-API-Servidor

```
┌─────────────────┐
│     CLIENTE     │
│  (Navegador,    │
│  App Móvil,     │
│  Otra App)      │
└────────┬────────┘
         │
         │ 1. Petición HTTP (Request)
         │    GET /usuarios/123
         │    Headers: Authorization, Content-Type
         │
         ▼
┌─────────────────┐
│   API REST      │
│  (Servidor)     │
│                 │
│  - Recibe       │
│    petición     │
│  - Valida       │
│  - Procesa      │
│  - Consulta BD  │
│  - Construye    │
│    respuesta    │
└────────┬────────┘
         │
         │ 2. Respuesta HTTP (Response)
         │    Status: 200 OK
         │    Body: { "id": 123, "nombre": "Juan" }
         │
         ▼
┌─────────────────┐
│     CLIENTE     │
│  Recibe datos   │
│  y los muestra  │
└─────────────────┘
```

### Flujo detallado de una petición:

1. **El cliente hace una petición**:
   ```
   GET https://api.miapp.com/usuarios/123
   Headers: {
     "Authorization": "Bearer token_secreto",
     "Content-Type": "application/json"
   }
   ```

2. **La API procesa**:
   - Verifica que la petición sea válida
   - Comprueba los permisos (autenticación)
   - Busca el usuario 123 en la base de datos
   - Formatea la respuesta

3. **El servidor responde**:
   ```
   Status: 200 OK
   Body: {
     "id": 123,
     "nombre": "Juan Pérez",
     "email": "juan@example.com",
     "edad": 28
   }
   ```

4. **El cliente usa la información**:
   - Muestra el nombre del usuario en pantalla
   - Actualiza la interfaz
   - Guarda datos en caché si es necesario

## La relación con el mundo real

Las APIs son como los **puntos de contacto** que usamos en la vida diaria:

### 1. Cajero Automático (ATM)
- **Tú** (cliente) insertas tu tarjeta y haces una petición ("quiero retirar $100")
- **El cajero** (API) recibe tu petición y la envía al banco
- **El banco** (servidor/base de datos) verifica tu saldo y autoriza
- **El cajero** te entrega el dinero (respuesta)

### 2. Control Remoto del TV
- **Tú** presionas un botón (petición)
- **El control** envía una señal (API)
- **El TV** recibe la señal y cambia de canal (servidor procesa)
- **Ves el resultado** en la pantalla (respuesta)

### 3. Servicio de Delivery
- **Tú** ordenas comida por una app (petición POST)
- **La app** envía tu pedido al restaurante (API)
- **El restaurante** prepara tu comida (servidor procesa)
- **Recibes tu comida** (respuesta con el recurso solicitado)

## ¿Por qué aprender sobre APIs REST?

1. **Demanda en el mercado**: Casi todas las empresas necesitan APIs para sus aplicaciones.

2. **Fundamento de la web moderna**: Entender APIs te abre las puertas a desarrollo web, móvil, IoT, y más.

3. **Escalabilidad**: Permite que aplicaciones grandes funcionen de manera eficiente.

4. **Flexibilidad**: Una misma API puede servir a un sitio web, una app móvil y otros servicios.

5. **Carrera profesional**: Los desarrolladores de APIs están muy bien pagados y son muy solicitados.

## Conceptos clave para recordar

- 🔑 **API**: Interfaz que permite la comunicación entre sistemas
- 🔑 **REST**: Estilo arquitectónico con buenas prácticas para diseñar APIs
- 🔑 **Cliente**: Quien hace las peticiones (navegador, app, etc.)
- 🔑 **Servidor**: Quien responde a las peticiones (tu API)
- 🔑 **Recurso**: Cualquier información que se puede nombrar (usuarios, productos, etc.)
- 🔑 **HTTP Methods**: GET, POST, PUT, DELETE - acciones sobre recursos
- 🔑 **JSON**: Formato común para intercambiar datos

## Próximos pasos

Ahora que entiendes qué son las APIs y REST, es momento de poner en práctica estos conceptos. En las siguientes secciones:
- Resolverás actividades interactivas para reforzar lo aprendido
- Verás ejemplos prácticos de APIs del mundo real
- Crearás tus propias ideas de APIs

¡Vamos a la práctica! 🚀
