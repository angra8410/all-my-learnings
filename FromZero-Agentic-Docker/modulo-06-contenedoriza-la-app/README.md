# Módulo 06: Contenedoriza la App

## 🎯 Objetivos

- ✅ Crear un Dockerfile para FastAPI + Agent
- ✅ Construir imagen Docker optimizada
- ✅ Ejecutar la aplicación en contenedor
- ✅ Probar la API desde Docker
- ✅ Gestionar variables de entorno

## 📖 Dockerfile para FastAPI

Revisa `ejemplos/Dockerfile` que incluye:

- Imagen base Python 3.11-slim
- Instalación de dependencias
- Configuración de la app
- Health check
- CMD para uvicorn

## 🚀 Construir y Ejecutar

```bash
cd modulo-06-contenedoriza-la-app/ejemplos

# Construir imagen
docker build -t agentic-app:v1 .

# Ejecutar contenedor
docker run -d -p 8000:8000 --name mi-agente agentic-app:v1

# Probar API
curl http://localhost:8000
curl http://localhost:8000/health
curl -X POST http://localhost:8000/agent/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is the weather?"}'

# Ver logs
docker logs mi-agente

# Acceder a docs
# http://localhost:8000/docs
```

## ✅ Checklist

- [ ] Revisado Dockerfile
- [ ] Revisado app/main.py
- [ ] Construida imagen Docker
- [ ] Ejecutado contenedor
- [ ] Probada la API
- [ ] Verificado health check
- [ ] Accedido a /docs

## 🎯 Próximos Pasos

Continúa al **Módulo 07: Docker Compose y Servicios**
