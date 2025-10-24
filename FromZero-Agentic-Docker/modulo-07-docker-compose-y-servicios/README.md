# Módulo 07: Docker Compose y Servicios

## 🎯 Objetivos

- ✅ Comprender docker-compose
- ✅ Orquestar múltiples servicios
- ✅ Configurar redes y volúmenes
- ✅ Gestionar servicios con docker-compose
- ✅ Implementar reverse proxy con nginx

## 📖 Docker Compose

docker-compose permite definir y ejecutar aplicaciones multi-contenedor.

Revisa `ejemplos/docker-compose.yml` que incluye:

- **agent-api** - Aplicación FastAPI
- **redis** - Cache y almacenamiento
- **nginx** - Reverse proxy
- **networks** - Red compartida
- **volumes** - Persistencia de datos

## 🚀 Comandos Docker Compose

```bash
cd modulo-07-docker-compose-y-servicios/ejemplos

# Iniciar todos los servicios
docker-compose up -d

# Ver logs
docker-compose logs -f

# Ver estado de servicios
docker-compose ps

# Detener servicios
docker-compose down

# Reconstruir servicios
docker-compose up -d --build

# Escalar servicio
docker-compose up -d --scale agent-api=3
```

## 🧪 Probar la Aplicación

```bash
# Iniciar servicios
docker-compose up -d

# Probar API directamente (puerto 8000)
curl http://localhost:8000

# Probar a través de nginx (puerto 80)
curl http://localhost

# Ver logs de todos los servicios
docker-compose logs

# Ver logs de un servicio específico
docker-compose logs agent-api
```

## ✅ Checklist

- [ ] Entiendo docker-compose.yml
- [ ] He iniciado servicios con docker-compose up
- [ ] He probado la API
- [ ] He revisado logs
- [ ] Entiendo networks y volumes
- [ ] He usado nginx como proxy

## 🎯 Próximos Pasos

Continúa al **Módulo 08: Testing y Debugging**
