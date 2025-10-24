# Módulo 09: Despliegue a Producción

## 🎯 Objetivos

- ✅ Optimizar Dockerfile para producción
- ✅ Configurar variables de entorno
- ✅ Implementar health checks
- ✅ Gestionar secretos
- ✅ Optimizar recursos
- ✅ Monitoreo básico

## 📖 Dockerfile para Producción

### Multi-stage Build

```dockerfile
# Build stage
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Production stage
FROM python:3.11-slim
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
ENV PATH=/root/.local/bin:$PATH
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
```

### Mejores Prácticas

1. **Multi-stage builds** - Reduce tamaño
2. **Non-root user** - Seguridad
3. **Health checks** - Monitoring
4. **Resource limits** - Estabilidad
5. **Logging** - Observabilidad

## 🔒 Gestión de Secretos

### Variables de Entorno

```bash
# .env file (NO commitear)
API_KEY=secret123
DATABASE_URL=postgresql://...
REDIS_URL=redis://...
```

### Docker Secrets (Docker Swarm)

```yaml
version: '3.8'
services:
  app:
    image: agentic-app:v1
    secrets:
      - api_key
      - db_password

secrets:
  api_key:
    external: true
  db_password:
    external: true
```

## 🚀 Deployment Options

### Option 1: Docker on VPS

```bash
# En servidor
git clone <repo>
cd <repo>
docker-compose up -d

# Con auto-restart
docker-compose up -d --restart=always
```

### Option 2: Docker Swarm

```bash
# Inicializar swarm
docker swarm init

# Deploy stack
docker stack deploy -c docker-compose.yml agentic-stack
```

### Option 3: Cloud Platforms

- **AWS ECS** - Elastic Container Service
- **Google Cloud Run** - Serverless containers
- **Azure Container Instances** - Managed containers
- **DigitalOcean App Platform** - PaaS

## 📊 Monitoreo

### Health Check Endpoint

```python
@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "uptime": get_uptime(),
        "version": "1.0.0"
    }
```

### Logs

```bash
# Ver logs
docker-compose logs -f

# Con filtros
docker-compose logs -f --tail=100 agent-api
```

## 🔧 Optimizaciones

### Resource Limits

```yaml
services:
  app:
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M
```

### Caching

```python
# Redis caching
import redis
r = redis.Redis(host='redis', port=6379)

def get_weather(location):
    cached = r.get(f"weather:{location}")
    if cached:
        return json.loads(cached)
    
    data = fetch_weather(location)
    r.setex(f"weather:{location}", 300, json.dumps(data))
    return data
```

## ✅ Checklist

- [ ] Dockerfile optimizado
- [ ] Variables de entorno configuradas
- [ ] Health checks implementados
- [ ] Logs configurados
- [ ] Resource limits definidos
- [ ] Plan de deployment claro

## 🎯 Próximos Pasos

Continúa al **Módulo 10: Proyecto Integrador**
