# Módulo 4: Volúmenes y Redes

## Introducción

En este módulo dominarás la persistencia de datos y comunicación entre contenedores. Aprenderás:

- Volúmenes Docker en profundidad
- Bind mounts vs volúmenes
- Networking avanzado
- Tipos de redes Docker
- DNS y descubrimiento de servicios
- Comunicación entre contenedores

## ¿Por qué es importante?

Los volúmenes y redes son esenciales porque:

- **Persistencia**: Los datos sobreviven al contenedor
- **Compartir**: Múltiples contenedores acceden a mismos datos
- **Performance**: Volúmenes son más rápidos que bind mounts
- **Aislamiento**: Redes permiten segmentar aplicaciones
- **Escalabilidad**: Fundamento para arquitecturas distribuidas

## Conceptos Principales

### 1. Tipos de Almacenamiento

```
┌─────────────────────────────────────────┐
│         Volúmenes Docker                │
│    (Gestionados por Docker)             │
│    /var/lib/docker/volumes/             │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│         Bind Mounts                     │
│    (Carpeta específica del host)        │
│    /home/user/data → /app/data          │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│         tmpfs (en memoria)              │
│    No persiste, solo en RAM             │
└─────────────────────────────────────────┘
```

### 2. Volúmenes Docker

**Crear y gestionar:**
```bash
# Crear volumen
docker volume create mi-volumen

# Listar volúmenes
docker volume ls

# Inspeccionar
docker volume inspect mi-volumen

# Eliminar
docker volume rm mi-volumen

# Limpiar volúmenes sin usar
docker volume prune
```

**Usar volúmenes:**
```bash
# Con volumen nombrado
docker run -v mi-volumen:/app/data nginx

# Volumen anónimo
docker run -v /app/data nginx

# Solo lectura
docker run -v mi-volumen:/app/data:ro nginx
```

### 3. Bind Mounts

```bash
# Montar carpeta del host
docker run -v /ruta/host:/ruta/contenedor nginx

# Ruta relativa (pwd)
docker run -v $(pwd)/data:/app/data nginx

# Solo lectura
docker run -v $(pwd)/config:/etc/config:ro nginx
```

**Diferencias clave:**

| Característica | Volumen | Bind Mount |
|----------------|---------|------------|
| **Gestión** | Docker | Usuario |
| **Ubicación** | /var/lib/docker/volumes | Cualquier parte |
| **Performance** | Optimizado | Puede variar |
| **Portabilidad** | Alta | Baja |
| **Uso típico** | Datos de producción | Desarrollo |

### 4. Networking en Docker

**Tipos de redes:**

```bash
# Bridge (por defecto)
# Contenedores en misma red pueden comunicarse

# Host
# Contenedor usa red del host directamente

# None
# Sin networking

# Overlay
# Múltiples hosts Docker (Swarm/Kubernetes)
```

**Gestión de redes:**
```bash
# Listar redes
docker network ls

# Crear red
docker network create mi-red
docker network create --driver bridge mi-red-bridge

# Inspeccionar
docker network inspect mi-red

# Conectar contenedor
docker network connect mi-red contenedor1

# Desconectar
docker network disconnect mi-red contenedor1

# Eliminar
docker network rm mi-red
```

### 5. Comunicación entre Contenedores

**Escenario típico: App + Database**

```bash
# Crear red
docker network create app-network

# Base de datos
docker run -d \
  --name postgres-db \
  --network app-network \
  -v db-data:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=secret \
  postgres:15

# Aplicación
docker run -d \
  --name backend \
  --network app-network \
  -e DATABASE_URL=postgresql://postgres:secret@postgres-db:5432/mydb \
  -p 3000:3000 \
  mi-backend

# Backend puede acceder a postgres-db por nombre DNS
```

### 6. DNS y Descubrimiento

Docker proporciona DNS automático:

```bash
# En la red "app-network":
# - contenedor "web" puede hacer ping a "db"
# - contenedor "db" puede hacer ping a "web"

docker exec web ping db
docker exec db ping web
```

## Implementación Práctica

### Ejercicio 1: Persistencia con Volúmenes

```bash
# Crear volumen
docker volume create datos-persistentes

# Contenedor 1: Escribir datos
docker run --rm \
  -v datos-persistentes:/data \
  alpine sh -c "echo 'Hola Docker' > /data/mensaje.txt"

# Contenedor 2: Leer datos
docker run --rm \
  -v datos-persistentes:/data \
  alpine cat /data/mensaje.txt

# Output: Hola Docker ✅
```

### Ejercicio 2: Desarrollo con Bind Mounts

```bash
# Proyecto web simple
mkdir mi-web
cd mi-web
echo '<h1>¡Hola desde Docker!</h1>' > index.html

# Servidor con bind mount
docker run -d \
  --name dev-server \
  -p 8080:80 \
  -v $(pwd):/usr/share/nginx/html:ro \
  nginx

# Editar index.html en tiempo real
# Los cambios se reflejan inmediatamente
```

### Ejercicio 3: Stack Completo (App + DB + Cache)

```bash
# Crear red
docker network create stack-network

# Redis (caché)
docker run -d \
  --name redis-cache \
  --network stack-network \
  redis:7-alpine

# PostgreSQL (base de datos)
docker run -d \
  --name postgres-db \
  --network stack-network \
  -v pgdata:/var/lib/postgresql/data \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=myapp \
  postgres:15

# API Backend
docker run -d \
  --name api-backend \
  --network stack-network \
  -e DATABASE_URL=postgresql://postgres:secret@postgres-db:5432/myapp \
  -e REDIS_URL=redis://redis-cache:6379 \
  -p 3000:3000 \
  node:18-alpine sleep infinity

# Verificar conectividad
docker exec api-backend ping redis-cache
docker exec api-backend ping postgres-db
```

### Ejercicio 4: Compartir Volumen entre Contenedores

```bash
# Volumen compartido
docker volume create shared-logs

# Productor de logs
docker run -d \
  --name logger \
  -v shared-logs:/logs \
  alpine sh -c "while true; do date >> /logs/app.log; sleep 5; done"

# Consumidor de logs
docker run -d \
  --name log-viewer \
  -v shared-logs:/logs:ro \
  alpine sh -c "tail -f /logs/app.log"

# Ver logs en tiempo real
docker logs -f log-viewer
```

## Mejores Prácticas

### 1. Usa Volúmenes para Datos Persistentes

```bash
# ✅ Producción
docker run -v db-data:/var/lib/postgresql/data postgres

# ❌ Evitar en producción
docker run -v /home/user/db:/var/lib/postgresql/data postgres
```

### 2. Bind Mounts para Desarrollo

```bash
# ✅ Desarrollo
docker run -v $(pwd):/app node:18

# Permite hot-reload y edición directa
```

### 3. Redes Personalizadas

```bash
# ✅ Mejor
docker network create mi-app
docker run --network mi-app ...

# ❌ Red por defecto
docker run ...  # Usa bridge default
```

### 4. Nombra tus Recursos

```bash
# ✅ Nombres descriptivos
docker volume create postgres-production-data
docker network create app-backend-network

# ❌ IDs generados
docker volume create
docker network create
```

### 5. Backups de Volúmenes

```bash
# Backup
docker run --rm \
  -v mi-volumen:/data \
  -v $(pwd):/backup \
  alpine tar czf /backup/backup.tar.gz /data

# Restore
docker run --rm \
  -v mi-volumen:/data \
  -v $(pwd):/backup \
  alpine tar xzf /backup/backup.tar.gz -C /
```

## Comandos Esenciales

```bash
# VOLÚMENES
docker volume create <nombre>           # Crear
docker volume ls                        # Listar
docker volume inspect <nombre>          # Detalles
docker volume rm <nombre>               # Eliminar
docker volume prune                     # Limpiar sin usar

# REDES
docker network create <nombre>          # Crear
docker network ls                       # Listar
docker network inspect <nombre>         # Detalles
docker network connect <red> <cont>     # Conectar
docker network disconnect <red> <cont>  # Desconectar
docker network rm <nombre>              # Eliminar
docker network prune                    # Limpiar sin usar

# MONTAJES
-v volumen:/ruta                        # Volumen nombrado
-v /host:/contenedor                    # Bind mount
-v /ruta:ro                             # Solo lectura
--mount type=volume,src=vol,dst=/ruta   # Sintaxis mount
```

## Conceptos clave para recordar

- 🔑 **Volúmenes**: Para datos persistentes en producción
- 🔑 **Bind Mounts**: Para desarrollo y configuración
- 🔑 **Redes**: Aíslan y conectan contenedores
- 🔑 **DNS**: Contenedores se comunican por nombre
- 🔑 **Bridge**: Red por defecto para contenedores
- 🔑 **Persistencia**: Los datos sobreviven al contenedor
- 🔑 **Compartir**: Volúmenes permiten compartir datos

## Próximos pasos

En el Módulo 5 aprenderás sobre:
- Docker Compose
- Definir multi-contenedor con YAML
- Orquestar servicios
- Variables y configuración
- Perfiles y ambientes

**¿Qué necesitas saber antes de continuar?**
✅ Crear y usar volúmenes  
✅ Entender bind mounts  
✅ Crear redes personalizadas  
✅ Conectar contenedores en red  
✅ Comunicación por DNS  

---

**¡Ahora dominas volúmenes y networking en Docker! 🎉**

**¡Nos vemos en el Módulo 5!** 🐳🚀
