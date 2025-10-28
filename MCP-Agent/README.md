# MCP-Agent: Especificación y Scaffold del Agente MCP

¡Bienvenido al módulo de **MCP Agent**! Este directorio contiene la especificación completa, ejemplos y herramientas para construir y probar un agente MCP (Model Context Protocol) desde cero.

## 🎯 Visión General

Un **agente MCP** es un componente de software que actúa como intermediario entre aplicaciones cliente y modelos de lenguaje (LLMs). El agente MCP:

- **Recibe prompts** de clientes a través de una interfaz HTTP
- **Procesa el contexto** y decide qué acciones tomar
- **Interactúa con LLMs** (o mocks para desarrollo/testing)
- **Devuelve respuestas estructuradas** al cliente

Este módulo te permite aprender cómo diseñar, implementar y desplegar un agente MCP de forma práctica.

## 🎯 Objetivos

Al trabajar con este módulo, serás capaz de:

- ✅ Comprender la arquitectura y especificación del protocolo MCP
- ✅ Implementar un agente MCP básico con Python
- ✅ Exponer una API HTTP para interactuar con el agente
- ✅ Contenedorizar el agente usando Docker
- ✅ Realizar testing básico con pytest
- ✅ Ejecutar el agente localmente con scripts automatizados
- ✅ Extender el agente con adaptadores LLM reales (OpenAI, Anthropic, etc.)

## 📁 Estructura del Proyecto

```
MCP-Agent/
├── README.md                    # Este archivo - visión general
├── spec.md                      # Especificación completa del agente MCP
├── run.sh                       # Script para ejecutar el agente localmente
├── examples/
│   ├── agent.py                 # Implementación mínima del agente
│   ├── Dockerfile               # Dockerfile para contenerizar el agente
│   └── docker-compose.yml       # Orquestación del agente y dependencias
└── tests/
    └── test_agent_basic.py      # Tests unitarios básicos
```

## 🚀 Cómo Probar Localmente

### Opción 1: Ejecutar con el Script `run.sh`

El script `run.sh` automatiza la creación del entorno virtual y la ejecución del agente:

```bash
cd MCP-Agent
./run.sh
```

El agente estará disponible en `http://localhost:8000`

### Opción 2: Ejecutar Manualmente con Python

```bash
cd MCP-Agent

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Ejecutar el agente
python examples/agent.py
```

### Opción 3: Ejecutar con Docker

```bash
cd MCP-Agent/examples

# Construir la imagen
docker build -t mcp-agent:latest .

# Ejecutar el contenedor
docker run -p 8000:8000 mcp-agent:latest
```

### Opción 4: Ejecutar con Docker Compose

```bash
cd MCP-Agent/examples
docker-compose up
```

## 🧪 Testing

Para ejecutar los tests unitarios:

```bash
cd MCP-Agent

# Activar entorno virtual si no está activo
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Ejecutar pytest
pytest tests/
```

O ejecutar tests específicos:

```bash
pytest tests/test_agent_basic.py -v
```

## 📋 Requisitos

- **Python 3.8+**: Lenguaje principal para el agente
- **Docker** (opcional): Para contenedorización
- **pytest** (para testing): Se instala automáticamente con `run.sh`

**Nota**: El agente de ejemplo **NO requiere dependencias externas** para ejecutarse. Usa únicamente la biblioteca estándar de Python (`http.server`, `json`).

## 🔌 Interfaz del Agente

El agente expone un endpoint HTTP:

**POST** `/prompt`

**Request Body (JSON)**:
```json
{
  "prompt": "¿Cuál es el clima hoy?",
  "context": {
    "user_id": "user123",
    "session_id": "session456"
  }
}
```

**Response (JSON)**:
```json
{
  "response": "Procesado: ¿Cuál es el clima hoy?",
  "metadata": {
    "agent_version": "1.0.0",
    "processed_at": "2025-10-28T18:55:00Z"
  }
}
```

Para más detalles sobre la interfaz, consulta [`spec.md`](./spec.md).

## 🔒 Notas de Seguridad

⚠️ **IMPORTANTE**: Este es un scaffold educativo y de desarrollo. Para producción:

- **NO incluyas claves de API** en el código fuente
- **Usa variables de entorno** para credenciales (OpenAI API keys, etc.)
- **Implementa autenticación** en el endpoint HTTP (API keys, JWT tokens)
- **Valida y sanitiza** todos los inputs del usuario
- **Usa HTTPS** en producción, nunca HTTP plano
- **Implementa rate limiting** para evitar abuso
- **Audita los prompts** enviados al LLM para evitar prompt injection

## 🛠️ Siguientes Pasos

Este scaffold es solo el punto de partida. Algunas mejoras sugeridas:

1. **Integrar LLMs reales**: Reemplazar el mock con adaptadores para OpenAI, Anthropic, Ollama, etc.
2. **Añadir herramientas (tools)**: Permitir que el agente ejecute funciones (búsqueda web, APIs, etc.)
3. **Implementar memoria**: Guardar contexto de conversaciones (RAG, vectorstores)
4. **Añadir logging estructurado**: Integrar herramientas como `structlog` o `loguru`
5. **Optimizar prompts**: Experimentar con diferentes técnicas de prompting
6. **Mejorar testing**: Añadir tests de integración y end-to-end
7. **CI/CD**: Integrar con GitHub Actions para testing automático
8. **Monitoreo**: Implementar métricas y observabilidad (Prometheus, Grafana)

## 📚 Recursos Adicionales

- [Especificación completa del agente](./spec.md)
- [Anthropic MCP Documentation](https://modelcontextprotocol.io/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/) (para versiones avanzadas)
- [Docker Best Practices](https://docs.docker.com/develop/dev-best-practices/)

---

¡Explora, experimenta y construye tu propio agente MCP! 🚀
