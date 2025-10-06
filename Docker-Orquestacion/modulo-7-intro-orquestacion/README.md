# Módulo 7: Introducción a Orquestación

## Introducción

¡Bienvenido al mundo de la orquestación de contenedores! En este módulo aprenderás:

- ¿Qué es la orquestación?
- ¿Por qué necesitamos orquestadores?
- Docker Swarm vs Kubernetes
- Conceptos fundamentales de orquestación
- Alta disponibilidad y escalabilidad
- Load balancing y service discovery

## ¿Por qué es importante?

La orquestación es crucial porque:

- **Escala**: Gestionar cientos/miles de contenedores
- **Alta Disponibilidad**: Tolerancia a fallos
- **Automatización**: Despliegues, actualizaciones, rollbacks
- **Eficiencia**: Uso óptimo de recursos
- **Producción**: Estándar de la industria

## Conceptos Principales

### 1. ¿Qué es Orquestación?

**Sin orquestador (manual):**
```
¿Qué pasa si un contenedor falla?  → Reinicio manual
¿Cómo escalar a 10 instancias?     → docker run x10
¿Actualizar sin downtime?          → Complejo y manual
¿Balanceo de carga?                → Configurar aparte
```

**Con orquestador (automatizado):**
```
Contenedor falla    → Auto-reinicio
Necesitas escalar   → scale replicas=10
Actualizar          → Rolling update automático
Balanceo            → Incluido y automático
```

### 2. Problemas que Resuelven los Orquestadores

**Gestión de Contenedores:**
- Iniciar/detener contenedores automáticamente
- Reiniciar contenedores fallidos
- Reemplazar contenedores no saludables

**Escalabilidad:**
- Escalar horizontalmente (más instancias)
- Distribuir carga entre instancias
- Auto-scaling basado en métricas

**Networking:**
- Service discovery automático
- Load balancing
- DNS interno
- Gestión de puertos

**Almacenamiento:**
- Persistencia de datos
- Compartir volúmenes
- Backups automáticos

**Actualizaciones:**
- Rolling updates (cero downtime)
- Rollback automático si falla
- Blue-green deployments
- Canary releases

**Seguridad:**
- Secrets management
- Network policies
- RBAC (Control de acceso)
- Certificados TLS automáticos

### 3. Arquitectura de Orquestadores

```
┌──────────────────────────────────────────┐
│           Control Plane                  │
│   (Toma decisiones, gestiona estado)     │
│                                          │
│  - API Server                            │
│  - Scheduler                             │
│  - Controller Manager                    │
│  - etcd (Estado del cluster)             │
└──────────────────────────────────────────┘
              ↓ ↓ ↓
┌──────────────────────────────────────────┐
│             Workers Nodes                │
│    (Ejecutan los contenedores)           │
│                                          │
│  Node 1    Node 2    Node 3              │
│  [Pods]    [Pods]    [Pods]              │
└──────────────────────────────────────────┘
```

### 4. Docker Swarm vs Kubernetes

| Característica | Docker Swarm | Kubernetes |
|---------------|--------------|------------|
| **Complejidad** | Simple, fácil de aprender | Complejo, curva de aprendizaje |
| **Setup** | Rápido (minutos) | Complejo (horas/días) |
| **Escalabilidad** | Buena (cientos de nodos) | Excelente (miles de nodos) |
| **Ecosistema** | Limitado | Muy amplio |
| **Popularidad** | Menor | Estándar de industria |
| **Auto-scaling** | Limitado | Avanzado |
| **Comunidad** | Pequeña | Muy grande |
| **Mejor para** | Proyectos pequeños/medianos | Empresas, producción a escala |

### 5. Conceptos Fundamentales

**Cluster:**
- Conjunto de máquinas (nodos) trabajando juntas
- Nodos manager (control plane)
- Nodos worker (ejecutan cargas)

**Service:**
- Definición de cómo ejecutar aplicación
- Número de réplicas
- Imagen a usar
- Puertos, redes, volúmenes

**Réplicas:**
- Múltiples instancias del mismo contenedor
- Alta disponibilidad
- Distribuidas entre nodos

**Load Balancing:**
- Distribuir tráfico entre réplicas
- Automático y transparente
- Health checks

**Service Discovery:**
- Servicios se encuentran por nombre
- DNS interno del cluster
- Sin configuración manual

**Rolling Updates:**
- Actualizar sin downtime
- Gradual (1 a 1, 2 a 2, etc.)
- Rollback si falla

**Self-Healing:**
- Detecta contenedores fallidos
- Reinicia automáticamente
- Reemplaza nodos caídos

### 6. Estado Deseado vs Estado Actual

```
Estado Deseado (lo que quieres):
- 3 réplicas de nginx
- Versión 1.24
- Puerto 80 expuesto

                ↓

Orquestador trabaja constantemente
para mantener estado actual = estado deseado

                ↓

Estado Actual (lo que hay):
- 3 réplicas corriendo
- Todas versión 1.24
- Todas healthy
```

**Si algo cambia:**
```
Un contenedor falla
    ↓
Estado actual ≠ Estado deseado
    ↓
Orquestador detecta
    ↓
Inicia nuevo contenedor
    ↓
Estado actual = Estado deseado ✅
```

### 7. Casos de Uso

**Startup pequeña → Docker Compose**
- 1-5 servicios
- 1 servidor
- Tráfico moderado

**Empresa mediana → Docker Swarm**
- 10-50 servicios
- 3-20 servidores
- Alta disponibilidad básica

**Empresa grande → Kubernetes**
- 100+ servicios
- Decenas/cientos de servidores
- Multi-región
- Auto-scaling complejo
- Múltiples equipos

## Implementación Práctica

### Ejercicio 1: Simular Orquestación Manual

**Sin orquestador:**
```bash
# Iniciar 3 réplicas manualmente
docker run -d --name web1 -p 8081:80 nginx
docker run -d --name web2 -p 8082:80 nginx
docker run -d --name web3 -p 8083:80 nginx

# ¿Qué pasa si web2 falla?
docker stop web2
# ... tienes que darte cuenta y reiniciar manualmente
docker start web2

# Actualizar a nueva versión
docker stop web1
docker rm web1
docker run -d --name web1 -p 8081:80 nginx:1.25
# ... repetir para web2, web3
# ¿Downtime? ¡Sí!
```

### Ejercicio 2: Concepto de Service Discovery

```bash
# Crear red
docker network create app-net

# Servicio 1 (database)
docker run -d --name db --network app-net postgres

# Servicio 2 (backend)
docker run -d --name api --network app-net \
  -e DB_HOST=db \
  node:18

# API puede conectarse a "db" por nombre
# DNS interno de Docker resuelve
docker exec api ping db  # ✅ Funciona
```

### Ejercicio 3: Simular Load Balancing

```bash
# Nginx como load balancer
cat > nginx.conf << 'EOF'
upstream backend {
    server backend1:3000;
    server backend2:3000;
    server backend3:3000;
}

server {
    listen 80;
    location / {
        proxy_pass http://backend;
    }
}
EOF

# Iniciar backends
docker run -d --name backend1 -p 3001:3000 node-app
docker run -d --name backend2 -p 3002:3000 node-app
docker run -d --name backend3 -p 3003:3000 node-app

# Nginx distribuye tráfico
docker run -d -p 80:80 -v $(pwd)/nginx.conf:/etc/nginx/nginx.conf nginx
```

## Preparación para Swarm y Kubernetes

### Requisitos Previos

**Conceptual:**
✅ Entender contenedores  
✅ Conocer redes Docker  
✅ Saber usar volúmenes  
✅ Experiencia con docker-compose  

**Técnico:**
✅ Linux básico  
✅ Línea de comandos  
✅ YAML  
✅ Networking básico  

### Próximos Pasos

**Módulo 8: Docker Swarm**
- Inicializar cluster
- Servicios y stacks
- Rolling updates
- Secrets y configs

**Módulos 9-10: Kubernetes**
- Pods, Deployments, Services
- ConfigMaps y Secrets
- Ingress y persistent volumes
- Escalado y monitoreo

## Conceptos clave para recordar

- 🔑 **Orquestación**: Gestión automatizada de contenedores
- 🔑 **Cluster**: Conjunto de nodos trabajando juntos
- 🔑 **Service**: Definición de aplicación
- 🔑 **Réplicas**: Múltiples instancias para HA
- 🔑 **Self-Healing**: Auto-recuperación de fallos
- 🔑 **Rolling Update**: Actualización sin downtime
- 🔑 **Estado Deseado**: Orquestador mantiene lo configurado

## Próximos pasos

En el Módulo 8 comenzarás con **Docker Swarm**:
- Tu primer cluster
- Desplegar servicios
- Escalar aplicaciones
- Alta disponibilidad
- Gestión de secrets

**¿Qué necesitas saber antes de continuar?**
✅ Por qué necesitamos orquestación  
✅ Conceptos básicos de clusters  
✅ Diferencia Swarm vs Kubernetes  
✅ Service discovery y load balancing  
✅ Auto-scaling y self-healing  

---

**¡Ahora entiendes por qué la orquestación es el futuro! 🚀**

**¡Nos vemos en el Módulo 8 - Docker Swarm!** 🐳⚙️
