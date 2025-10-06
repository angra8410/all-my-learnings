# Módulo 2: Imágenes y Contenedores

## Introducción

En este módulo profundizaremos en el funcionamiento interno de las imágenes y contenedores de Docker. Aprenderás:

- Arquitectura de capas en imágenes
- Gestión avanzada de contenedores
- Optimización de imágenes
- Networking básico
- Variables de entorno y configuración

## ¿Por qué es importante?

Entender cómo funcionan internamente las imágenes y contenedores te permite:

- **Optimizar**: Crear imágenes más pequeñas y eficientes
- **Depurar**: Resolver problemas más efectivamente
- **Seguridad**: Entender superficies de ataque
- **Performance**: Mejorar tiempos de build y deploy
- **Costos**: Reducir almacenamiento y transferencia de datos

## Conceptos Principales

### 1. Arquitectura de Capas

Las imágenes Docker se construyen por capas, como una cebolla:

```
┌─────────────────────────────────────┐
│    Aplicación Python (10 MB)       │ ← Capa 3
├─────────────────────────────────────┤
│    Dependencias pip (50 MB)        │ ← Capa 2
├─────────────────────────────────────┤
│    Base Ubuntu (70 MB)             │ ← Capa 1
└─────────────────────────────────────┘
         Total: 130 MB
```

**Beneficios:**
- **Reutilización**: Capas compartidas entre imágenes
- **Caché**: Builds más rápidos
- **Eficiencia**: Solo se descarga lo que cambió

**Ejemplo:**
```bash
# Ver capas de una imagen
docker history nginx:latest

# Ver información detallada
docker inspect nginx:latest
```

### 2. Copy-on-Write (CoW)

Cuando creas un contenedor, Docker usa Copy-on-Write:

```
Imagen (solo lectura)
        ↓
┌─────────────────┐
│  Capa Original  │ ← Compartida entre contenedores
└─────────────────┘
        ↓
┌─────────────────┐
│ Capa Escritura  │ ← Única por contenedor
│  (cambios)      │
└─────────────────┘
```

**Ventajas:**
- Inicio instantáneo
- Uso eficiente de disco
- Aislamiento entre contenedores

### 3. Tags y Versionado

```bash
# Formato: repository:tag
nginx:latest          # Última versión
nginx:1.24           # Versión específica
nginx:1.24-alpine    # Variante Alpine
myapp:v1.0.0         # Tu aplicación
```

**Mejores prácticas:**
```bash
# ❌ Evitar en producción
docker pull nginx

# ✅ Usar versiones específicas
docker pull nginx:1.24
docker pull python:3.11-slim
```

### 4. Gestión de Imágenes

```bash
# Listar imágenes
docker images

# Filtrar imágenes
docker images nginx
docker images --filter "dangling=true"

# Información detallada
docker inspect nginx:latest

# Eliminar imagen
docker rmi nginx:latest

# Eliminar múltiples
docker rmi $(docker images -q)

# Limpiar imágenes sin usar
docker image prune
docker image prune -a  # Todas las sin usar
```

### 5. Contenedores: Estados y Ciclos

**Estados de un contenedor:**
```
Created → Running → Paused → Stopped → Removed
   ↓         ↓         ↓         ↓
 start     pause     stop      rm
```

**Opciones avanzadas de `docker run`:**
```bash
# Modo detached
docker run -d nginx

# Nombre personalizado
docker run --name mi-app nginx

# Mapeo de puertos
docker run -p 8080:80 nginx
docker run -p 127.0.0.1:8080:80 nginx  # Solo localhost

# Variables de entorno
docker run -e API_KEY=secret123 nginx
docker run --env-file .env nginx

# Límites de recursos
docker run -m 512m --cpus=1 nginx

# Reinicio automático
docker run --restart=always nginx
docker run --restart=on-failure nginx

# Modo interactivo
docker run -it ubuntu bash

# Eliminar al salir
docker run --rm nginx
```

### 6. Networking Básico

Docker crea redes virtuales para conectar contenedores:

```bash
# Listar redes
docker network ls

# Tipos de redes:
# - bridge: Red por defecto
# - host: Usa red del host directamente
# - none: Sin red
```

**Conectar contenedores:**
```bash
# Crear red personalizada
docker network create mi-red

# Ejecutar contenedores en la red
docker run -d --name db --network mi-red postgres
docker run -d --name app --network mi-red nginx

# Los contenedores pueden comunicarse por nombre
# app puede acceder a db usando: http://db:5432
```

### 7. Variables de Entorno

```bash
# Pasar variables
docker run -e DATABASE_URL=postgres://... myapp

# Desde archivo
echo "API_KEY=secret" > .env
echo "DEBUG=true" >> .env
docker run --env-file .env myapp

# Ver variables en contenedor
docker exec mi-app env
```

### 8. Volúmenes y Bind Mounts (Introducción)

```bash
# Bind mount (carpeta del host)
docker run -v /home/user/data:/app/data nginx

# Volumen nombrado (gestión Docker)
docker volume create mi-volumen
docker run -v mi-volumen:/app/data nginx

# Volumen anónimo
docker run -v /app/data nginx
```

## Implementación Práctica

### Ejercicio 1: Explorar Capas de Imágenes

```bash
# Descargar imagen
docker pull nginx:alpine

# Ver capas
docker history nginx:alpine

# Comparar tamaños
docker images nginx

# Inspeccionar capas
docker inspect nginx:alpine | grep -A 20 "Layers"
```

**Análisis:**
```bash
# Alpine vs Ubuntu
docker pull nginx:alpine      # ~24 MB
docker pull nginx:latest      # ~142 MB

# ¡6x más pequeña!
```

### Ejercicio 2: Gestión de Contenedores

```bash
# Crear contenedor sin iniciarlo
docker create --name mi-nginx nginx

# Ver estado
docker ps -a

# Iniciar
docker start mi-nginx

# Pausar
docker pause mi-nginx

# Reanudar
docker unpause mi-nginx

# Reiniciar
docker restart mi-nginx

# Renombrar
docker rename mi-nginx nginx-produccion

# Ver logs en tiempo real
docker logs -f nginx-produccion

# Detener con timeout
docker stop -t 30 nginx-produccion

# Eliminar
docker rm nginx-produccion
```

### Ejercicio 3: Networking entre Contenedores

```bash
# Crear red
docker network create app-network

# Base de datos
docker run -d \
  --name postgres-db \
  --network app-network \
  -e POSTGRES_PASSWORD=secret \
  postgres:15

# Aplicación que usa la DB
docker run -d \
  --name api-server \
  --network app-network \
  -e DB_HOST=postgres-db \
  -e DB_PORT=5432 \
  -p 3000:3000 \
  node:18

# Verificar conexión
docker exec api-server ping postgres-db
```

### Ejercicio 4: Variables de Entorno

```bash
# Crear archivo de configuración
cat > app.env << EOF
NODE_ENV=production
PORT=3000
DATABASE_URL=postgres://user:pass@db:5432/mydb
API_KEY=supersecret123
DEBUG=false
EOF

# Ejecutar con variables
docker run -d \
  --name mi-app \
  --env-file app.env \
  -p 3000:3000 \
  node:18

# Verificar variables
docker exec mi-app env | grep NODE_ENV
```

### Ejercicio 5: Límites de Recursos

```bash
# Contenedor con límites
docker run -d \
  --name limited-nginx \
  --memory=256m \
  --memory-swap=512m \
  --cpus=0.5 \
  --pids-limit=100 \
  nginx

# Monitorear recursos
docker stats limited-nginx

# Ver configuración
docker inspect limited-nginx | grep -A 10 "Memory"
```

### Ejercicio 6: Persistencia con Volúmenes

```bash
# Crear volumen
docker volume create datos-app

# Usar volumen
docker run -d \
  --name app-con-datos \
  -v datos-app:/app/data \
  nginx

# Escribir datos
docker exec app-con-datos sh -c "echo 'Hola Docker' > /app/data/archivo.txt"

# Eliminar contenedor
docker rm -f app-con-datos

# Crear nuevo contenedor con el mismo volumen
docker run -d \
  --name app-nueva \
  -v datos-app:/app/data \
  nginx

# Verificar persistencia
docker exec app-nueva cat /app/data/archivo.txt
# Output: Hola Docker ✅
```

### Ejercicio 7: Optimización de Imágenes

```bash
# Comparar tamaños base
docker pull ubuntu:22.04          # ~77 MB
docker pull alpine:3.18           # ~7 MB
docker pull python:3.11           # ~1 GB
docker pull python:3.11-slim      # ~130 MB
docker pull python:3.11-alpine    # ~50 MB

# Ver diferencias
docker images | grep -E "ubuntu|alpine|python"
```

## Mejores Prácticas

### 1. Usa Imágenes Oficiales y Pequeñas

```bash
# ❌ Imagen grande
FROM ubuntu:22.04
RUN apt-get update && apt-get install python3

# ✅ Imagen optimizada
FROM python:3.11-slim
```

### 2. Limita Recursos

```bash
# Siempre establece límites en producción
docker run -d \
  --memory=512m \
  --cpus=1 \
  --restart=unless-stopped \
  myapp
```

### 3. No Almacenes Secretos en Imágenes

```bash
# ❌ MAL - Secreto en imagen
docker build --build-arg API_KEY=secret123 .

# ✅ BIEN - Secreto en runtime
docker run -e API_KEY=secret123 myapp
```

### 4. Usa Versiones Específicas

```bash
# ❌ Evitar
FROM node
FROM python:latest

# ✅ Mejor
FROM node:18.17-alpine
FROM python:3.11-slim
```

### 5. Nombra Contenedores y Volúmenes

```bash
# ❌ IDs generados automáticamente
docker run nginx

# ✅ Nombres descriptivos
docker run --name frontend-prod nginx
docker volume create frontend-data
```

### 6. Limpieza Regular

```bash
# Rutina de limpieza semanal
docker system prune -a --volumes

# O selectivamente
docker container prune  # Contenedores detenidos
docker image prune     # Imágenes sin usar
docker volume prune    # Volúmenes sin usar
docker network prune   # Redes sin usar
```

## Comandos Esenciales - Referencia

```bash
# IMÁGENES
docker images                           # Listar
docker pull <imagen>:<tag>              # Descargar
docker rmi <imagen>                     # Eliminar
docker history <imagen>                 # Ver capas
docker inspect <imagen>                 # Detalles
docker image prune                      # Limpiar

# CONTENEDORES
docker run [opciones] <imagen>          # Crear y ejecutar
docker create <imagen>                  # Solo crear
docker start <contenedor>               # Iniciar
docker stop <contenedor>                # Detener
docker restart <contenedor>             # Reiniciar
docker pause/unpause <contenedor>       # Pausar/reanudar
docker rm <contenedor>                  # Eliminar
docker rename <viejo> <nuevo>           # Renombrar

# INSPECCIÓN
docker ps                               # Contenedores activos
docker ps -a                            # Todos
docker logs <contenedor>                # Ver logs
docker logs -f <contenedor>             # Seguir logs
docker stats                            # Recursos
docker top <contenedor>                 # Procesos
docker inspect <contenedor>             # Detalles

# NETWORKING
docker network ls                       # Listar redes
docker network create <nombre>          # Crear red
docker network inspect <red>            # Detalles
docker network connect <red> <cont>     # Conectar
docker network disconnect <red> <cont>  # Desconectar

# VOLÚMENES
docker volume ls                        # Listar
docker volume create <nombre>           # Crear
docker volume inspect <nombre>          # Detalles
docker volume rm <nombre>               # Eliminar
```

## Conceptos clave para recordar

- 🔑 **Capas**: Las imágenes se construyen por capas inmutables
- 🔑 **Tags**: Siempre usa versiones específicas en producción
- 🔑 **CoW**: Copy-on-Write permite eficiencia y rapidez
- 🔑 **Networking**: Usa redes personalizadas para conectar contenedores
- 🔑 **Variables**: Configura con variables de entorno, no hardcoding
- 🔑 **Recursos**: Limita CPU y memoria en producción
- 🔑 **Volúmenes**: Para persistir datos más allá del ciclo del contenedor

## Próximos pasos

En el Módulo 3 aprenderás sobre:
- Crear tus propias imágenes con Dockerfile
- Optimización de builds
- Multi-stage builds
- Mejores prácticas de construcción
- Automatización de builds

**¿Qué necesitas saber antes de continuar?**
✅ Entender la arquitectura de capas  
✅ Saber gestionar contenedores avanzadamente  
✅ Poder crear redes y conectar contenedores  
✅ Usar variables de entorno  
✅ Entender persistencia con volúmenes  

## Recursos Adicionales

- 📚 [Docker Images Documentation](https://docs.docker.com/engine/reference/commandline/images/)
- 📚 [Container Networking](https://docs.docker.com/network/)
- 📚 [Manage Data in Docker](https://docs.docker.com/storage/)
- 🎥 [Docker Deep Dive](https://www.youtube.com/results?search_query=docker+deep+dive)
- 💡 [Docker Image Best Practices](https://docs.docker.com/develop/dev-best-practices/)

---

**¡Excelente trabajo! Ahora entiendes cómo funcionan internamente las imágenes y contenedores. 🚀**

**¡Nos vemos en el Módulo 3 donde crearás tus propias imágenes!** 🐳
