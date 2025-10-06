# Módulo 6: Registros y Publicación

## Introducción

Aprende a compartir y distribuir tus imágenes Docker. En este módulo dominarás:

- Docker Hub y registros públicos
- Publicar imágenes propias
- Registros privados
- Tags y versionado semántico
- Automatización con GitHub Actions
- Seguridad en imágenes

## ¿Por qué es importante?

Publicar imágenes te permite:

- **Compartir**: Distribuir aplicaciones fácilmente
- **Colaborar**: Equipos usan las mismas imágenes
- **CI/CD**: Automatizar despliegues
- **Reutilización**: Compartir componentes
- **Versioning**: Control de versiones de aplicaciones

## Conceptos Principales

### 1. Docker Hub

Docker Hub es el registro público oficial:

**Crear cuenta:**
- Visita https://hub.docker.com
- Regístrate gratuitamente
- Permite repositorios públicos ilimitados
- 1 repositorio privado gratis

**Login:**
```bash
docker login
# Ingresa usuario y password
```

### 2. Nombrado de Imágenes

```
usuario/repositorio:tag

Ejemplos:
nginx:latest
myuser/myapp:v1.0.0
company/backend:prod
myuser/api:1.2.3-alpine
```

**Reglas:**
- usuario: Tu nombre en Docker Hub
- repositorio: Nombre de la imagen
- tag: Versión (default: latest)

### 3. Publicar Imagen

**Proceso completo:**

```bash
# 1. Construir imagen
docker build -t myuser/myapp:1.0.0 .

# 2. Probar localmente
docker run myuser/myapp:1.0.0

# 3. Login a Docker Hub
docker login

# 4. Publicar
docker push myuser/myapp:1.0.0

# 5. También publicar como latest
docker tag myuser/myapp:1.0.0 myuser/myapp:latest
docker push myuser/myapp:latest
```

### 4. Versionado Semántico

```
MAJOR.MINOR.PATCH

1.0.0 → Primera versión
1.0.1 → Bug fix
1.1.0 → Nueva funcionalidad (compatible)
2.0.0 → Cambios no compatibles
```

**Estrategia de tags:**
```bash
# Versión completa
docker tag myapp myuser/myapp:1.2.3

# Versión menor
docker tag myapp myuser/myapp:1.2

# Versión mayor
docker tag myapp myuser/myapp:1

# Latest
docker tag myapp myuser/myapp:latest

# Publicar todos
docker push myuser/myapp --all-tags
```

### 5. Registros Privados

**GitHub Container Registry:**
```bash
# Login
echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin

# Tag
docker tag myapp ghcr.io/username/myapp:1.0.0

# Push
docker push ghcr.io/username/myapp:1.0.0
```

**Amazon ECR:**
```bash
# Login
aws ecr get-login-password --region region | \
  docker login --username AWS --password-stdin \
  aws_account_id.dkr.ecr.region.amazonaws.com

# Push
docker push aws_account_id.dkr.ecr.region.amazonaws.com/myapp:1.0.0
```

### 6. Automatización con GitHub Actions

**.github/workflows/docker-publish.yml:**
```yaml
name: Docker Build and Push

on:
  push:
    tags:
      - 'v*'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2
      
      - name: Login to Docker Hub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
      
      - name: Extract metadata
        id: meta
        uses: docker/metadata-action@v4
        with:
          images: username/myapp
      
      - name: Build and push
        uses: docker/build-push-action@v4
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          labels: ${{ steps.meta.outputs.labels }}
```

### 7. Seguridad y Mejores Prácticas

**Escaneo de vulnerabilidades:**
```bash
# Docker Scout (nuevo)
docker scout cves myimage:tag

# Trivy
trivy image myimage:tag
```

**Firma de imágenes:**
```bash
# Docker Content Trust
export DOCKER_CONTENT_TRUST=1
docker push myuser/myapp:1.0.0
```

## Implementación Práctica

### Ejercicio 1: Publicar Primera Imagen

```bash
# Crear app simple
mkdir mi-app && cd mi-app

cat > app.py << 'EOF'
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '¡Mi primera imagen pública!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
EOF

cat > requirements.txt << 'EOF'
Flask==2.3.0
EOF

cat > Dockerfile << 'EOF'
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]
EOF

# Build
docker build -t tuusuario/mi-app:1.0.0 .

# Push
docker login
docker push tuusuario/mi-app:1.0.0
```

### Ejercicio 2: Multi-Plataforma

```bash
# Crear builder
docker buildx create --name mybuilder --use

# Build para múltiples arquitecturas
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t tuusuario/mi-app:multiarch \
  --push .
```

### Ejercicio 3: Workflow Completo

```bash
# 1. Desarrollo
git checkout -b feature/nueva-funcionalidad
# ... desarrollar ...
docker build -t mi-app:dev .

# 2. Pruebas
docker run mi-app:dev
# ... probar ...

# 3. Tag y push a staging
docker tag mi-app:dev tuusuario/mi-app:staging
docker push tuusuario/mi-app:staging

# 4. Merge y release
git checkout main
git merge feature/nueva-funcionalidad
git tag v1.2.0

# 5. Build producción
docker build -t tuusuario/mi-app:1.2.0 .
docker tag tuusuario/mi-app:1.2.0 tuusuario/mi-app:latest
docker push tuusuario/mi-app:1.2.0
docker push tuusuario/mi-app:latest
```

## Comandos Esenciales

```bash
# LOGIN/LOGOUT
docker login                          # Docker Hub
docker login ghcr.io                  # GitHub
docker logout

# TAG
docker tag imagen:tag nueva:tag
docker tag imagen usuario/imagen:tag

# PUSH/PULL
docker push usuario/imagen:tag
docker pull usuario/imagen:tag
docker push usuario/imagen --all-tags

# BÚSQUEDA
docker search python
docker search --filter stars=50 nginx

# INSPECCIÓN
docker manifest inspect usuario/imagen:tag
```

## Mejores Prácticas

### 1. Versionado Consistente

```bash
# ✅ Semántico
myapp:1.0.0
myapp:1.2.3
myapp:2.0.0-beta

# ❌ Evitar
myapp:final
myapp:new
myapp:ultimo
```

### 2. Múltiples Tags

```bash
# Versión específica
docker push myapp:1.2.3

# Compatible con
docker push myapp:1.2
docker push myapp:1
docker push myapp:latest
```

### 3. No Incluir Secretos

```bash
# ❌ NUNCA
ENV API_KEY=secret123

# ✅ En runtime
docker run -e API_KEY=secret123 myapp
```

### 4. README en Docker Hub

Documenta:
- Qué hace la imagen
- Cómo usarla
- Variables de entorno
- Puertos expuestos
- Ejemplos

### 5. Automatización

- GitHub Actions para builds automáticos
- Tags automáticos desde Git
- Escaneo de seguridad en CI/CD

## Conceptos clave para recordar

- 🔑 **Docker Hub**: Registro público principal
- 🔑 **Tags**: Versionado de imágenes
- 🔑 **Push/Pull**: Publicar y descargar
- 🔑 **Semántico**: MAJOR.MINOR.PATCH
- 🔑 **Privados**: Para código propietario
- 🔑 **Seguridad**: Escanear vulnerabilidades
- 🔑 **Automatización**: CI/CD para builds

## Próximos pasos

En el Módulo 7 comenzarás con:
- Introducción a orquestación
- ¿Por qué necesitamos orquestadores?
- Docker Swarm vs Kubernetes
- Conceptos de orquestación
- Preparación para Swarm y K8s

**¿Qué necesitas saber antes de continuar?**
✅ Publicar imagen en Docker Hub  
✅ Aplicar versionado semántico  
✅ Usar múltiples tags  
✅ Entender registros privados  
✅ Conceptos básicos de seguridad  

---

**¡Ahora puedes compartir tus imágenes con el mundo! 🌎**

**¡Nos vemos en el Módulo 7 - Orquestación!** 🐳🚀
