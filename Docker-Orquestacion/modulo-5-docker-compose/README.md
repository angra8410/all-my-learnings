# Módulo 5: Docker Compose

## Introducción

¡Docker Compose revoluciona cómo trabajamos con aplicaciones multi-contenedor! En este módulo aprenderás:

- Sintaxis de docker-compose.yml
- Definir servicios, redes y volúmenes
- Orquestar aplicaciones completas
- Variables de entorno y configuración
- Perfiles y ambientes (dev, prod)
- Dependencias entre servicios

## ¿Por qué es importante?

Docker Compose te permite:

- **Simplicidad**: Definir stack completo en un archivo YAML
- **Reproducibilidad**: Mismo entorno en cualquier máquina
- **Productividad**: Levantar/bajar todo con un comando
- **Documentación**: El archivo YAML es la documentación
- **Desarrollo**: Ambiente local idéntico a producción

## Conceptos Principales

### 1. ¿Qué es Docker Compose?

Herramienta para definir y ejecutar aplicaciones Docker multi-contenedor usando un archivo YAML.

**Ejemplo básico - docker-compose.yml:**
```yaml
version: '3.8'

services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
  
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: secret
```

**Comandos:**
```bash
docker-compose up        # Iniciar servicios
docker-compose down      # Detener y eliminar
docker-compose ps        # Ver estado
docker-compose logs      # Ver logs
```

### 2. Estructura de docker-compose.yml

```yaml
version: '3.8'  # Versión de Compose

services:       # Definición de contenedores
  servicio1:
    # Configuración del servicio
  servicio2:
    # Configuración del servicio

networks:       # Redes personalizadas (opcional)
  mi-red:

volumes:        # Volúmenes persistentes (opcional)
  mi-volumen:
```

### 3. Definir Servicios

**Opciones principales:**

```yaml
services:
  backend:
    # Imagen a usar
    image: node:18-alpine
    
    # O construir desde Dockerfile
    build:
      context: ./backend
      dockerfile: Dockerfile
    
    # Nombre del contenedor
    container_name: mi-backend
    
    # Puertos
    ports:
      - "3000:3000"
    
    # Variables de entorno
    environment:
      NODE_ENV: production
      DB_HOST: database
    
    # Archivo de variables
    env_file:
      - .env
    
    # Volúmenes
    volumes:
      - ./backend:/app
      - node_modules:/app/node_modules
    
    # Redes
    networks:
      - app-network
    
    # Dependencias
    depends_on:
      - database
      - redis
    
    # Reinicio
    restart: unless-stopped
    
    # Comando personalizado
    command: npm start
    
    # Healthcheck
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/health"]
      interval: 30s
      timeout: 3s
      retries: 3
```

### 4. Stack Completo: App + DB + Cache

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  # Frontend
  frontend:
    build: ./frontend
    ports:
      - "80:80"
    depends_on:
      - backend
    networks:
      - frontend-network

  # Backend API
  backend:
    build:
      context: ./backend
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    environment:
      DATABASE_URL: postgresql://postgres:secret@database:5432/myapp
      REDIS_URL: redis://cache:6379
    depends_on:
      - database
      - cache
    networks:
      - frontend-network
      - backend-network
    volumes:
      - ./backend:/app
      - /app/node_modules
    restart: unless-stopped

  # Database
  database:
    image: postgres:15-alpine
    environment:
      POSTGRES_DB: myapp
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: secret
    volumes:
      - postgres-data:/var/lib/postgresql/data
    networks:
      - backend-network
    restart: unless-stopped

  # Cache
  cache:
    image: redis:7-alpine
    networks:
      - backend-network
    restart: unless-stopped

networks:
  frontend-network:
  backend-network:

volumes:
  postgres-data:
```

### 5. Variables de Entorno

**Archivo .env:**
```bash
# Database
POSTGRES_DB=myapp
POSTGRES_USER=postgres
POSTGRES_PASSWORD=supersecret

# API
API_PORT=3000
NODE_ENV=production
```

**Usar en docker-compose.yml:**
```yaml
services:
  db:
    image: postgres:15
    environment:
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
  
  api:
    build: ./api
    ports:
      - "${API_PORT}:3000"
    environment:
      NODE_ENV: ${NODE_ENV}
```

### 6. Perfiles y Ambientes

**Desarrollo vs Producción:**

```yaml
services:
  api:
    build: ./api
    # Común a todos
    ports:
      - "3000:3000"
    
  # Solo en desarrollo
  debug-tools:
    image: debug-image
    profiles:
      - development
  
  # Solo en producción
  monitoring:
    image: prometheus
    profiles:
      - production
```

**Ejecutar:**
```bash
# Desarrollo
docker-compose --profile development up

# Producción
docker-compose --profile production up
```

### 7. Healthchecks y Dependencias

```yaml
services:
  database:
    image: postgres:15
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5

  backend:
    image: node:18
    depends_on:
      database:
        condition: service_healthy
    # Backend espera a que DB esté healthy
```

## Implementación Práctica

### Ejercicio 1: Stack Web Básico

**Estructura:**
```
mi-proyecto/
├── docker-compose.yml
├── frontend/
│   └── index.html
└── backend/
    └── server.js
```

**docker-compose.yml:**
```yaml
version: '3.8'

services:
  web:
    image: nginx:alpine
    ports:
      - "8080:80"
    volumes:
      - ./frontend:/usr/share/nginx/html:ro

  api:
    image: node:18-alpine
    working_dir: /app
    volumes:
      - ./backend:/app
    ports:
      - "3000:3000"
    command: node server.js
```

**Ejecutar:**
```bash
docker-compose up -d
docker-compose ps
docker-compose logs -f
docker-compose down
```

### Ejercicio 2: Stack con Base de Datos

```yaml
version: '3.8'

services:
  app:
    image: wordpress:latest
    ports:
      - "8000:80"
    environment:
      WORDPRESS_DB_HOST: db
      WORDPRESS_DB_USER: wordpress
      WORDPRESS_DB_PASSWORD: secret
      WORDPRESS_DB_NAME: wordpress
    depends_on:
      - db
    volumes:
      - wordpress-data:/var/www/html

  db:
    image: mysql:8
    environment:
      MYSQL_DATABASE: wordpress
      MYSQL_USER: wordpress
      MYSQL_PASSWORD: secret
      MYSQL_ROOT_PASSWORD: rootsecret
    volumes:
      - db-data:/var/lib/mysql

volumes:
  wordpress-data:
  db-data:
```

### Ejercicio 3: Desarrollo con Hot Reload

```yaml
version: '3.8'

services:
  frontend:
    build:
      context: ./frontend
      target: development
    ports:
      - "3000:3000"
    volumes:
      - ./frontend/src:/app/src
      - /app/node_modules
    environment:
      - CHOKIDAR_USEPOLLING=true

  backend:
    build:
      context: ./backend
    ports:
      - "3001:3001"
    volumes:
      - ./backend:/app
      - /app/node_modules
    environment:
      - NODE_ENV=development
    command: npm run dev
```

## Comandos Esenciales

```bash
# CICLO DE VIDA
docker-compose up                # Iniciar
docker-compose up -d             # Iniciar en background
docker-compose down              # Detener y eliminar
docker-compose stop              # Solo detener
docker-compose start             # Reiniciar servicios detenidos
docker-compose restart           # Reiniciar servicios

# GESTIÓN
docker-compose ps                # Estado de servicios
docker-compose logs              # Ver logs
docker-compose logs -f servicio  # Seguir logs de un servicio
docker-compose exec servicio sh  # Entrar a contenedor
docker-compose build             # Construir imágenes
docker-compose pull              # Actualizar imágenes

# ESCALA
docker-compose up -d --scale web=3  # Escalar servicio

# LIMPIEZA
docker-compose down -v           # Eliminar también volúmenes
docker-compose down --rmi all    # Eliminar también imágenes
```

## Mejores Prácticas

### 1. Usa Variables de Entorno

```yaml
# ✅ Con variables
environment:
  DB_PASSWORD: ${DB_PASSWORD}

# ❌ Hardcoded
environment:
  DB_PASSWORD: secret123
```

### 2. Separa Ambientes

```bash
# docker-compose.yml        - Base
# docker-compose.dev.yml    - Desarrollo
# docker-compose.prod.yml   - Producción

# Ejecutar:
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up
```

### 3. Nombra Recursos

```yaml
services:
  backend:
    container_name: myapp-backend
    networks:
      - myapp-network

networks:
  myapp-network:
    name: myapp-network
```

### 4. Usa Healthchecks

```yaml
services:
  db:
    healthcheck:
      test: ["CMD", "pg_isready"]
      interval: 10s
  
  app:
    depends_on:
      db:
        condition: service_healthy
```

### 5. .dockerignore

```
node_modules
.git
.env
*.log
.vscode
```

## Conceptos clave para recordar

- 🔑 **docker-compose.yml**: Define stack completo en YAML
- 🔑 **Servicios**: Cada contenedor es un servicio
- 🔑 **depends_on**: Orden de inicio de servicios
- 🔑 **Variables**: Usa .env para configuración
- 🔑 **Volúmenes**: Persisten datos
- 🔑 **Redes**: Aíslan comunicación
- 🔑 **Perfiles**: Diferentes configuraciones por ambiente

## Próximos pasos

En el Módulo 6 aprenderás sobre:
- Docker Registry (Docker Hub)
- Publicar imágenes
- Registros privados
- Tags y versionado
- CI/CD con Docker

**¿Qué necesitas saber antes de continuar?**
✅ Crear docker-compose.yml básico  
✅ Definir servicios múltiples  
✅ Usar variables de entorno  
✅ Gestionar volúmenes y redes  
✅ Comandos de docker-compose  

---

**¡Docker Compose hace el multi-contenedor súper simple! 🎉**

**¡Nos vemos en el Módulo 6!** 🐳🚀
