# Módulo 03: Docker Básico

## 🎯 Objetivos del Módulo

Al finalizar este módulo, habrás:

- ✅ Comprendido los conceptos fundamentales de Docker
- ✅ Dominado los comandos Docker esenciales
- ✅ Creado tu primer Dockerfile
- ✅ Construido y ejecutado imágenes Docker
- ✅ Gestionado contenedores (start, stop, logs, rm)
- ✅ Entendido volúmenes y redes básicas

## 📖 Conceptos Fundamentales

### Imagen vs Contenedor

**Imagen**: Template read-only que contiene la aplicación y sus dependencias.
**Contenedor**: Instancia ejecutable de una imagen.

```
Imagen (Template)  →  docker run  →  Contenedor (Proceso)
    Dockerfile     →  docker build →  Imagen
```

### Anatomía de un Dockerfile

Un Dockerfile es un archivo de texto con instrucciones para construir una imagen.

**Instrucciones principales**:

- `FROM` - Imagen base
- `WORKDIR` - Directorio de trabajo
- `COPY` - Copiar archivos
- `RUN` - Ejecutar comandos durante build
- `EXPOSE` - Declarar puerto
- `CMD` - Comando por defecto al ejecutar

### Ejemplo de Dockerfile

Revisa el archivo en `ejemplos/Dockerfile`:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 🔧 Comandos Docker Esenciales

### Gestión de Imágenes

```bash
# Listar imágenes
docker images

# Construir imagen
docker build -t nombre:tag .

# Eliminar imagen
docker rmi <image-id>

# Descargar imagen del registry
docker pull python:3.11-slim

# Ver detalles de imagen
docker inspect <image-id>
```

### Gestión de Contenedores

```bash
# Ejecutar contenedor
docker run -p 8000:8000 nombre:tag

# Ejecutar en segundo plano
docker run -d -p 8000:8000 nombre:tag

# Ejecutar con nombre
docker run -d --name mi-app -p 8000:8000 nombre:tag

# Listar contenedores activos
docker ps

# Listar todos los contenedores
docker ps -a

# Detener contenedor
docker stop <container-id>

# Iniciar contenedor detenido
docker start <container-id>

# Ver logs
docker logs <container-id>

# Ver logs en tiempo real
docker logs -f <container-id>

# Ejecutar comando en contenedor
docker exec -it <container-id> bash

# Eliminar contenedor
docker rm <container-id>

# Eliminar contenedor forzadamente
docker rm -f <container-id>
```

### Limpieza

```bash
# Eliminar contenedores detenidos
docker container prune

# Eliminar imágenes no usadas
docker image prune

# Limpieza completa
docker system prune -a
```

## 📝 Ejercicios Prácticos

### Ejercicio 1: Construye tu Primera Imagen

```bash
# 1. Navega al directorio de ejemplos
cd modulo-03-docker-basico/ejemplos

# 2. Revisa los archivos
ls -la
cat Dockerfile

# 3. Construye la imagen
docker build -t my-first-app:v1 .

# 4. Verifica que se creó
docker images | grep my-first-app
```

### Ejercicio 2: Ejecuta tu Contenedor

```bash
# 1. Ejecuta el contenedor
docker run -d -p 8000:8000 --name test-app my-first-app:v1

# 2. Verifica que está corriendo
docker ps

# 3. Prueba la API
curl http://localhost:8000
curl http://localhost:8000/health
curl http://localhost:8000/info

# 4. Ve los logs
docker logs test-app
```

### Ejercicio 3: Interactúa con el Contenedor

```bash
# 1. Accede al contenedor
docker exec -it test-app bash

# Dentro del contenedor:
pwd
ls -la
python --version
exit

# 2. Ve los procesos
docker top test-app

# 3. Ve estadísticas de recursos
docker stats test-app --no-stream
```

### Ejercicio 4: Ciclo de Vida del Contenedor

```bash
# 1. Detener
docker stop test-app

# 2. Verificar que está detenido
docker ps -a | grep test-app

# 3. Iniciar de nuevo
docker start test-app

# 4. Reiniciar
docker restart test-app

# 5. Eliminar
docker stop test-app
docker rm test-app
```

## 🎯 Casos de Uso Comunes

### Variables de Entorno

```bash
docker run -d -p 8000:8000   -e API_KEY="secret123"   -e DEBUG="true"   --name app-with-env   my-first-app:v1
```

### Montar Volúmenes

```bash
docker run -d -p 8000:8000   -v $(pwd)/data:/app/data   --name app-with-volume   my-first-app:v1
```

### Modo Interactivo

```bash
docker run -it python:3.11-slim python
```

## 📊 Mejores Prácticas

1. **Usa imágenes oficiales** - `FROM python:3.11-slim`
2. **Minimiza capas** - Combina comandos RUN
3. **Usa .dockerignore** - Excluye archivos innecesarios
4. **No incluyas secretos** - Usa variables de entorno
5. **Etiqueta tus imágenes** - `name:version`
6. **Limpia regularmente** - `docker system prune`

## 🔍 Debugging

### Ver logs detallados

```bash
docker logs --details test-app
docker logs --tail 50 test-app
```

### Inspeccionar contenedor

```bash
docker inspect test-app
```

### Verificar redes

```bash
docker network ls
docker network inspect bridge
```

## ✅ Checklist del Módulo

- [ ] Entiendo la diferencia entre imagen y contenedor
- [ ] Sé leer un Dockerfile
- [ ] Puedo construir imágenes con `docker build`
- [ ] Puedo ejecutar contenedores con `docker run`
- [ ] Sé ver logs con `docker logs`
- [ ] Puedo detener/iniciar contenedores
- [ ] Sé acceder a un contenedor con `docker exec`
- [ ] Puedo eliminar contenedores e imágenes
- [ ] Entiendo variables de entorno en Docker
- [ ] He practicado todos los ejercicios

## 📚 Recursos Adicionales

- [Docker Official Docs](https://docs.docker.com/)
- [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)
- [Docker CLI Reference](https://docs.docker.com/engine/reference/commandline/cli/)

## 🎯 Próximos Pasos

1. Completa `actividad-interactiva.md`
2. Documenta en `retroalimentacion.md`
3. Actualiza `progreso.md`
4. Continúa al **Módulo 04: Construye la Agent Core**

---

**¡Docker básico dominado! Ahora construiremos el agente. 🚀**
