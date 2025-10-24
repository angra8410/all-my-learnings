# Módulo 06: Actividad Interactiva

## Ejercicio 1: Construir Imagen (10 min)

```bash
cd modulo-06-contenedoriza-la-app/ejemplos
docker build -t agentic-app:v1 .
docker images | grep agentic-app
```

**Imagen construida**: [ ] Sí
**Tamaño**: _____ MB
**Tiempo de build**: _____ segundos

## Ejercicio 2: Ejecutar Contenedor (10 min)

```bash
docker run -d -p 8000:8000 --name test-agent agentic-app:v1
docker ps
curl http://localhost:8000
```

**Contenedor corriendo**: [ ] Sí
**Respuesta recibida**: _______________

## Ejercicio 3: Probar Endpoints (15 min)

```bash
# Health
curl http://localhost:8000/health

# Query agent
curl -X POST http://localhost:8000/agent/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is the weather?"}'

# History
curl http://localhost:8000/agent/history

# Info
curl http://localhost:8000/info
```

**Todos los endpoints funcionan**: [ ] Sí

## Ejercicio 4: Explorar Logs (5 min)

```bash
docker logs test-agent
docker logs -f test-agent
```

**Logs revisados**: [ ] Sí

## Total: 40 minutos
