# Módulo 3: Dockerfile y Builds

## Introducción

¡Ahora aprenderás a crear tus propias imágenes Docker! En este módulo dominarás:

- Sintaxis de Dockerfile
- Instrucciones esenciales
- Optimización de builds
- Multi-stage builds
- Best practices de construcción
- Cache de Docker

## ¿Por qué es importante?

Crear tus propias imágenes te permite:

- **Customización**: Adaptar imágenes a tus necesidades
- **Reproducibilidad**: Documentar la configuración en código
- **Automatización**: Builds consistentes y repetibles
- **Eficiencia**: Imágenes optimizadas para tu caso de uso
- **CI/CD**: Integrar en pipelines de despliegue

## Conceptos Principales

### 1. ¿Qué es un Dockerfile?

Un Dockerfile es un archivo de texto con instrucciones para construir una imagen Docker.

**Estructura básica:**
```dockerfile
# Comentario
FROM imagen-base
INSTRUCCION argumentos
INSTRUCCION argumentos
...
```

**Ejemplo simple:**
```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
EXPOSE 3000
CMD ["node", "server.js"]
```

### 2. Instrucciones Principales

#### FROM - Imagen Base
```dockerfile
# Imagen oficial
FROM node:18-alpine

# Versión específica
FROM python:3.11-slim

# Múltiples etapas (veremos más adelante)
FROM golang:1.20 AS builder
```

#### WORKDIR - Directorio de Trabajo
```dockerfile
# Establece el directorio de trabajo
WORKDIR /app

# Equivalente a: cd /app
# Todos los comandos siguientes se ejecutan ahí
```

#### COPY - Copiar Archivos
```dockerfile
# Copiar archivo específico
COPY app.py /app/

# Copiar múltiples archivos
COPY package.json package-lock.json ./

# Copiar todo
COPY . .

# Con permisos
COPY --chown=node:node . .
```

#### ADD - Similar a COPY (con extras)
```dockerfile
# Preferir COPY en general
# ADD puede descomprimir automáticamente
ADD archivo.tar.gz /destino/

# ADD puede descargar URLs
ADD https://example.com/file.txt /app/
```

#### RUN - Ejecutar Comandos
```dockerfile
# Formato shell
RUN apt-get update && apt-get install -y curl

# Formato exec
RUN ["pip", "install", "-r", "requirements.txt"]

# Múltiples comandos (mejor práctica)
RUN apt-get update && \
    apt-get install -y \
        curl \
        git \
        vim && \
    rm -rf /var/lib/apt/lists/*
```

#### ENV - Variables de Entorno
```dockerfile
# Variable simple
ENV NODE_ENV=production

# Múltiples variables
ENV API_URL=https://api.example.com \
    PORT=3000 \
    DEBUG=false
```

#### EXPOSE - Documentar Puertos
```dockerfile
# Documenta que la app usa estos puertos
EXPOSE 3000
EXPOSE 8080 8443

# No publica puertos automáticamente
# Usar -p en docker run
```

#### CMD - Comando por Defecto
```dockerfile
# Formato exec (recomendado)
CMD ["python", "app.py"]

# Formato shell
CMD python app.py

# Solo puede haber un CMD
# El último gana
```

#### ENTRYPOINT - Punto de Entrada
```dockerfile
# Hace la imagen ejecutable
ENTRYPOINT ["python"]
CMD ["app.py"]

# docker run imagen otros.py
# Ejecutará: python otros.py

# Combinación común:
ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["start"]
```

#### USER - Cambiar Usuario
```dockerfile
# Crear usuario no-root
RUN adduser -D appuser
USER appuser

# Todo después corre como appuser
```

#### VOLUME - Puntos de Montaje
```dockerfile
# Declara volúmenes
VOLUME /app/data
VOLUME ["/var/log", "/var/db"]
```

#### ARG - Argumentos de Build
```dockerfile
# Variable solo en build-time
ARG VERSION=latest
ARG BUILD_DATE

# Usar en instrucciones
FROM node:${VERSION}
LABEL build-date=${BUILD_DATE}

# Pasar en build:
# docker build --build-arg VERSION=18 .
```

### 3. Optimización de Builds

#### Orden de Capas
```dockerfile
# ❌ MAL - Reinstala dependencias en cada cambio de código
FROM node:18
WORKDIR /app
COPY . .
RUN npm install
CMD ["node", "server.js"]

# ✅ BIEN - Aprovecha caché de Docker
FROM node:18
WORKDIR /app
COPY package*.json ./      # Copiar solo dependencias primero
RUN npm install            # Esta capa se cachea
COPY . .                   # Código cambia frecuentemente
CMD ["node", "server.js"]
```

#### Minimizar Capas
```dockerfile
# ❌ Muchas capas
RUN apt-get update
RUN apt-get install -y curl
RUN apt-get install -y git
RUN rm -rf /var/lib/apt/lists/*

# ✅ Combinar comandos relacionados
RUN apt-get update && \
    apt-get install -y curl git && \
    rm -rf /var/lib/apt/lists/*
```

#### .dockerignore
```bash
# Archivo .dockerignore
node_modules
npm-debug.log
.git
.env
*.md
.vscode
.idea
__pycache__
*.pyc
.pytest_cache
dist/
build/
```

### 4. Multi-Stage Builds

Crear imágenes finales pequeñas:

```dockerfile
# Etapa 1: Build
FROM golang:1.20 AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY . .
RUN CGO_ENABLED=0 go build -o app

# Etapa 2: Runtime
FROM alpine:3.18
WORKDIR /app
COPY --from=builder /app/app .
EXPOSE 8080
CMD ["./app"]

# Imagen final: solo ~10MB en lugar de ~800MB
```

**Ejemplo Node.js:**
```dockerfile
# Build stage
FROM node:18 AS builder
WORKDIR /build
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

# Production stage
FROM node:18-alpine
WORKDIR /app
COPY --from=builder /build/node_modules ./node_modules
COPY --from=builder /build/dist ./dist
COPY package*.json ./
USER node
EXPOSE 3000
CMD ["node", "dist/server.js"]
```

## Implementación Práctica

### Ejercicio 1: Primera Imagen Python

**Crear app.py:**
```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '¡Hola desde Docker!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

**Crear requirements.txt:**
```
Flask==2.3.0
```

**Crear Dockerfile:**
```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Copiar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY app.py .

# Exponer puerto
EXPOSE 5000

# Usuario no-root
RUN useradd -m appuser
USER appuser

# Comando
CMD ["python", "app.py"]
```

**Construir y ejecutar:**
```bash
# Build
docker build -t mi-flask-app .

# Run
docker run -p 5000:5000 mi-flask-app

# Probar: http://localhost:5000
```

### Ejercicio 2: Optimizar con Multi-Stage

**Dockerfile optimizado:**
```dockerfile
# Stage 1: Dependencies
FROM python:3.11-slim AS deps
WORKDIR /deps
COPY requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-slim
WORKDIR /app

# Copiar dependencias instaladas
COPY --from=deps /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH

# Copiar aplicación
COPY app.py .

# Usuario
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 5000
CMD ["python", "app.py"]
```

### Ejercicio 3: App Node.js Completa

**Estructura del proyecto:**
```
mi-app/
├── Dockerfile
├── .dockerignore
├── package.json
├── server.js
└── public/
    └── index.html
```

**package.json:**
```json
{
  "name": "mi-app",
  "version": "1.0.0",
  "scripts": {
    "start": "node server.js"
  },
  "dependencies": {
    "express": "^4.18.2"
  }
}
```

**server.js:**
```javascript
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.static('public'));

app.get('/api/health', (req, res) => {
  res.json({ status: 'OK', timestamp: new Date() });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

**Dockerfile:**
```dockerfile
FROM node:18-alpine

WORKDIR /app

# Instalar dependencias
COPY package*.json ./
RUN npm ci --only=production

# Copiar código
COPY . .

# Usuario no-root
USER node

EXPOSE 3000

HEALTHCHECK --interval=30s --timeout=3s \
  CMD node -e "require('http').get('http://localhost:3000/api/health')"

CMD ["npm", "start"]
```

**.dockerignore:**
```
node_modules
npm-debug.log
.git
.env
README.md
.dockerignore
Dockerfile
```

**Build y run:**
```bash
docker build -t mi-node-app .
docker run -p 3000:3000 --name app mi-node-app
```

## Mejores Prácticas

### 1. Usa Imágenes Base Pequeñas
```dockerfile
# ❌ Grande
FROM ubuntu:22.04

# ✅ Pequeña
FROM alpine:3.18
FROM python:3.11-slim
FROM node:18-alpine
```

### 2. No Ejecutes como Root
```dockerfile
# Crear y usar usuario no-privilegiado
RUN adduser -D appuser
USER appuser
```

### 3. Limpia en la Misma Capa
```dockerfile
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*
```

### 4. Usa Multi-Stage para Compilados
```dockerfile
FROM golang:1.20 AS builder
# ... compilar ...

FROM alpine:3.18
COPY --from=builder /app/binary .
```

### 5. Aprovecha la Caché
```dockerfile
# Copiar archivos de dependencias primero
COPY package.json package-lock.json ./
RUN npm install

# Código después (cambia más frecuentemente)
COPY . .
```

## Comandos Esenciales

```bash
# BUILD
docker build -t nombre:tag .                 # Build básico
docker build -t nombre:tag -f Dockerfile.prod . # Dockerfile específico
docker build --no-cache -t nombre:tag .      # Sin caché
docker build --build-arg VAR=valor .         # Con argumentos

# TAGS
docker tag imagen:tag nueva:tag              # Etiquetar
docker tag imagen usuario/imagen:tag         # Para registry

# INFORMACIÓN
docker history imagen                        # Ver capas
docker inspect imagen                        # Detalles
```

## Conceptos clave para recordar

- 🔑 **Dockerfile**: Receta para construir imágenes
- 🔑 **Capas**: Cada instrucción crea una capa
- 🔑 **Caché**: Orden correcto acelera builds
- 🔑 **Multi-stage**: Imágenes finales pequeñas
- 🔑 **.dockerignore**: Excluir archivos innecesarios
- 🔑 **Usuario**: No ejecutar como root
- 🔑 **Optimización**: Combinar comandos, limpiar en misma capa

## Próximos pasos

En el Módulo 4 aprenderás sobre:
- Volúmenes persistentes en profundidad
- Networking avanzado
- Comunicación entre contenedores
- Docker networks en detalle
- Bind mounts vs volumes

**¿Qué necesitas saber antes de continuar?**
✅ Crear un Dockerfile básico  
✅ Entender instrucciones principales  
✅ Construir imágenes con docker build  
✅ Aplicar optimizaciones básicas  
✅ Usar multi-stage builds  

---

**¡Ahora puedes crear tus propias imágenes Docker! 🎉**

**¡Nos vemos en el Módulo 4!** 🐳🚀
