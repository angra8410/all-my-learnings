# Módulo 8: Docker Swarm

## Introducción

¡Tu primer orquestador! Docker Swarm es simple pero poderoso. En este módulo aprenderás:

- Inicializar un cluster Swarm
- Servicios y réplicas
- Stacks con docker-compose
- Rolling updates y rollbacks
- Secrets y configs
- Networking en Swarm
- Alta disponibilidad

## ¿Por qué es importante?

Docker Swarm te permite:

- **Simplicidad**: Fácil de aprender y usar
- **Nativo**: Incluido con Docker
- **Producción**: Listo para producción
- **Escalable**: Maneja cientos de nodos
- **Compatible**: Usa docker-compose.yml

## Conceptos Principales

### 1. Inicializar Swarm

```bash
# Convertir Docker en modo Swarm
docker swarm init

# Output:
# Swarm initialized: current node (xyz) is now a manager.
# 
# To add a worker to this swarm, run the following command:
#     docker swarm join --token SWMTKN-1-xxx... 192.168.1.100:2377
```

**Arquitectura:**
```
Manager Node (Control Plane)
    ↓
Worker Nodes (ejecutan tareas)
    - Node 1
    - Node 2
    - Node 3
```

### 2. Servicios Swarm

```bash
# Crear servicio
docker service create \
  --name web \
  --replicas 3 \
  --publish 8080:80 \
  nginx:alpine

# Listar servicios
docker service ls

# Ver réplicas
docker service ps web

# Escalar
docker service scale web=5

# Actualizar
docker service update --image nginx:1.25 web

# Eliminar
docker service rm web
```

### 3. Stacks (Multi-Servicio)

**docker-compose.yml (versión Swarm):**
```yaml
version: '3.8'

services:
  web:
    image: nginx:alpine
    ports:
      - "80:80"
    deploy:
      replicas: 3
      update_config:
        parallelism: 1
        delay: 10s
      restart_policy:
        condition: on-failure
    networks:
      - frontend

  api:
    image: node:18-alpine
    deploy:
      replicas: 5
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
    networks:
      - frontend
      - backend
    secrets:
      - db_password

  db:
    image: postgres:15-alpine
    deploy:
      replicas: 1
      placement:
        constraints:
          - node.role == manager
    volumes:
      - db-data:/var/lib/postgresql/data
    networks:
      - backend
    secrets:
      - db_password
    environment:
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password

networks:
  frontend:
  backend:

volumes:
  db-data:

secrets:
  db_password:
    external: true
```

**Desplegar stack:**
```bash
# Crear secret
echo "supersecret" | docker secret create db_password -

# Desplegar
docker stack deploy -c docker-compose.yml myapp

# Listar stacks
docker stack ls

# Ver servicios del stack
docker stack services myapp

# Ver tareas
docker stack ps myapp

# Logs
docker service logs myapp_web

# Eliminar stack
docker stack rm myapp
```

### 4. Secrets Management

```bash
# Crear secret desde archivo
docker secret create api_key api_key.txt

# Crear secret desde stdin
echo "supersecret" | docker secret create db_pass -

# Listar secrets
docker secret ls

# Usar en servicio
docker service create \
  --name api \
  --secret api_key \
  node:18

# Dentro del contenedor: /run/secrets/api_key
```

### 5. Configs

```bash
# Crear config
docker config create nginx_config nginx.conf

# Usar en servicio
docker service create \
  --name web \
  --config source=nginx_config,target=/etc/nginx/nginx.conf \
  nginx

# Actualizar config (nuevo config, rolling update)
docker config create nginx_config_v2 nginx_v2.conf
docker service update \
  --config-rm nginx_config \
  --config-add source=nginx_config_v2,target=/etc/nginx/nginx.conf \
  web
```

### 6. Rolling Updates

```bash
# Configurar estrategia de actualización
docker service update \
  --update-parallelism 2 \
  --update-delay 10s \
  --update-failure-action rollback \
  --image nginx:1.25 \
  web

# Proceso:
# 1. Detiene 2 réplicas
# 2. Inicia 2 con nueva imagen
# 3. Espera 10s
# 4. Repite con siguientes 2
# 5. Si falla → rollback automático
```

### 7. Networking en Swarm

```bash
# Overlay network (multi-host)
docker network create --driver overlay mi-red

# Servicios en misma red se comunican
docker service create --name db --network mi-red postgres
docker service create --name api --network mi-red node:18

# Routing mesh (load balancing automático)
# Cualquier nodo puede recibir tráfico
# Swarm lo rutea al contenedor correcto
```

## Implementación Práctica

### Ejercicio 1: Primer Cluster

```bash
# Inicializar Swarm
docker swarm init

# Ver nodos
docker node ls

# Información del nodo
docker node inspect self
```

### Ejercicio 2: Servicio con Réplicas

```bash
# Crear servicio web
docker service create \
  --name web \
  --replicas 3 \
  --publish 8080:80 \
  nginx:alpine

# Ver réplicas distribuidas
docker service ps web

# Probar auto-recuperación
# Encuentra un contenedor y detienlo
docker ps
docker stop <container-id>

# Swarm detecta y crea nuevo
docker service ps web
# Verás el fallido y el nuevo
```

### Ejercicio 3: Stack Completo

**Estructura:**
```
app/
├── docker-compose.yml
├── frontend/
│   └── Dockerfile
└── backend/
    └── Dockerfile
```

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  frontend:
    build: ./frontend
    image: myapp/frontend:latest
    ports:
      - "80:80"
    deploy:
      replicas: 2
      update_config:
        parallelism: 1
    networks:
      - app-network

  backend:
    build: ./backend
    image: myapp/backend:latest
    deploy:
      replicas: 3
      resources:
        limits:
          memory: 512M
    networks:
      - app-network
    secrets:
      - api_key

  redis:
    image: redis:7-alpine
    deploy:
      replicas: 1
    networks:
      - app-network

networks:
  app-network:
    driver: overlay

secrets:
  api_key:
    file: ./api_key.txt
```

**Desplegar:**
```bash
# Build local
docker-compose build

# Push imágenes (si usas registry)
docker-compose push

# Desplegar stack
docker stack deploy -c docker-compose.yml miapp

# Monitorear
watch docker stack ps miapp
```

### Ejercicio 4: Alta Disponibilidad

```bash
# Múltiples managers para HA
# Nodo 1 (ya es manager):
docker swarm init --advertise-addr 192.168.1.10

# Nodo 2 y 3 como managers:
docker swarm join-token manager
# Ejecutar comando en nodos 2 y 3

# Ahora tienes 3 managers (tolerancia a 1 fallo)
docker node ls
```

## Comandos Esenciales

```bash
# SWARM
docker swarm init                    # Inicializar
docker swarm join                    # Unir nodo
docker swarm leave                   # Salir del swarm

# NODES
docker node ls                       # Listar nodos
docker node inspect <node>           # Detalles
docker node update --availability drain <node>  # Drenar nodo
docker node promote <node>           # Promover a manager
docker node demote <node>            # Degradar a worker

# SERVICES
docker service create                # Crear servicio
docker service ls                    # Listar
docker service ps <service>          # Ver réplicas
docker service scale <service>=N     # Escalar
docker service update <service>      # Actualizar
docker service rollback <service>    # Rollback
docker service logs <service>        # Logs
docker service rm <service>          # Eliminar

# STACKS
docker stack deploy -c file.yml name # Desplegar
docker stack ls                      # Listar stacks
docker stack services <stack>        # Servicios del stack
docker stack ps <stack>              # Tareas del stack
docker stack rm <stack>              # Eliminar stack

# SECRETS
docker secret create <name> <file>   # Crear
docker secret ls                     # Listar
docker secret inspect <secret>       # Detalles
docker secret rm <secret>            # Eliminar

# CONFIGS
docker config create <name> <file>   # Crear
docker config ls                     # Listar
docker config inspect <config>       # Detalles
docker config rm <config>            # Eliminar
```

## Mejores Prácticas

### 1. Alta Disponibilidad

```bash
# Al menos 3 managers
# Tolerancia: (N-1)/2
# 3 managers → tolera 1 fallo
# 5 managers → tolera 2 fallos
# 7 managers → tolera 3 fallos
```

### 2. Recursos

```yaml
deploy:
  resources:
    limits:
      cpus: '0.5'
      memory: 512M
    reservations:
      cpus: '0.25'
      memory: 256M
```

### 3. Health Checks

```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost/health"]
  interval: 30s
  timeout: 10s
  retries: 3
  start_period: 40s
```

### 4. Update Strategy

```yaml
deploy:
  update_config:
    parallelism: 2
    delay: 10s
    failure_action: rollback
    order: start-first  # o stop-first
```

### 5. Placement

```yaml
deploy:
  placement:
    constraints:
      - node.role == worker
      - node.labels.region == us-east
    preferences:
      - spread: node.labels.zone
```

## Conceptos clave para recordar

- 🔑 **Swarm Mode**: Modo cluster de Docker
- 🔑 **Services**: Definición de aplicación orquestada
- 🔑 **Stacks**: Múltiples servicios con compose
- 🔑 **Secrets**: Gestión segura de secretos
- 🔑 **Overlay**: Red multi-host automática
- 🔑 **Rolling Update**: Actualización sin downtime
- 🔑 **Self-Healing**: Auto-recuperación automática

## Próximos pasos

En el Módulo 9 comenzarás con **Kubernetes Básico**:
- Arquitectura de Kubernetes
- Pods, Deployments, Services
- kubectl básico
- Namespaces
- Tu primera aplicación en K8s

**¿Qué necesitas saber antes de continuar?**
✅ Inicializar Swarm  
✅ Crear y escalar servicios  
✅ Desplegar stacks  
✅ Usar secrets y configs  
✅ Rolling updates  

---

**¡Docker Swarm hace la orquestación accesible! 🐝**

**¡Nos vemos en el Módulo 9 - Kubernetes!** ⚓🚀
