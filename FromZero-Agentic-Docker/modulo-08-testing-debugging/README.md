# Módulo 08: Testing y Debugging

## 🎯 Objetivos

- ✅ Implementar tests con pytest
- ✅ Crear tests para la API
- ✅ Debugging en contenedores
- ✅ Analizar logs efectivamente
- ✅ Usar herramientas de debugging

## 📖 Testing con Pytest

### Test Básico

```python
# test_agent.py
import pytest
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_agent_query():
    response = client.post(
        "/agent/query",
        json={"query": "What is the weather?"}
    )
    assert response.status_code == 200
    assert "result" in response.json()
```

### Ejecutar Tests

```bash
# Instalar pytest
pip install pytest pytest-cov httpx

# Ejecutar tests
pytest tests/ -v

# Con cobertura
pytest tests/ --cov=app --cov-report=html

# Test específico
pytest tests/test_agent.py::test_health_check -v
```

## 🐛 Debugging en Docker

### Ver Logs

```bash
# Logs en tiempo real
docker logs -f <container-id>

# Últimas 100 líneas
docker logs --tail 100 <container-id>

# Con timestamps
docker logs -t <container-id>
```

### Acceder al Contenedor

```bash
# Shell interactivo
docker exec -it <container-id> bash

# Ejecutar comando
docker exec <container-id> python --version

# Ver procesos
docker top <container-id>
```

### Debugging Avanzado

```bash
# Inspeccionar contenedor
docker inspect <container-id>

# Ver estadísticas
docker stats <container-id>

# Ver eventos
docker events --filter container=<container-id>
```

## 🔍 Análisis de Logs

### Mejores Prácticas

1. **Usa niveles de log apropiados**: DEBUG, INFO, WARNING, ERROR
2. **Incluye timestamps**: Para tracking temporal
3. **Contexto suficiente**: Request ID, user ID, etc.
4. **Estructurados**: JSON para parseo fácil

### Ejemplo de Logging

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

@app.post("/agent/query")
async def query_agent(request: QueryRequest):
    logger.info(f"Received query: {request.query}")
    try:
        result = agent.process_query(request.query)
        logger.info(f"Query processed successfully")
        return result
    except Exception as e:
        logger.error(f"Error processing query: {e}", exc_info=True)
        raise
```

## ✅ Checklist

- [ ] Entiendo pytest
- [ ] He escrito tests básicos
- [ ] Sé ejecutar tests
- [ ] Puedo debuggear en contenedores
- [ ] Sé analizar logs
- [ ] Implementé logging en la app

## 🎯 Próximos Pasos

Continúa al **Módulo 09: Despliegue a Producción**
