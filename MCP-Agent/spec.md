# Especificación del Agente MCP (Model Context Protocol)

## 1. Introducción

Este documento define la especificación completa del **Agente MCP** (Model Context Protocol Agent), un componente de software que actúa como intermediario entre aplicaciones cliente y modelos de lenguaje grandes (LLMs).

### 1.1 Propósito

El agente MCP tiene como objetivo:

- Proporcionar una interfaz HTTP estandarizada para interactuar con LLMs
- Abstraer la complejidad de diferentes proveedores de LLM
- Gestionar el contexto y flujo de conversaciones
- Procesar y estructurar las respuestas del LLM
- Permitir extensibilidad mediante herramientas (tools) y plugins

### 1.2 Alcance

Esta especificación cubre:

- Roles y responsabilidades del agente
- Interfaz HTTP RESTful
- Interfaz programática (Python API)
- Flujo de decisión y procesamiento
- Formatos de entrada y salida
- Ejemplos de uso

## 2. Arquitectura y Roles

### 2.1 Componentes del Sistema

```
┌─────────────┐         ┌──────────────┐         ┌─────────────┐
│   Cliente   │ ──────> │  Agente MCP  │ ──────> │     LLM     │
│  (HTTP/API) │ <────── │  (Servidor)  │ <────── │  (OpenAI,   │
└─────────────┘         └──────────────┘         │  Anthropic) │
                                │                 └─────────────┘
                                │
                                ▼
                        ┌──────────────┐
                        │  Herramientas│
                        │   (Tools)    │
                        │   Opcionales │
                        └──────────────┘
```

### 2.2 Roles del Agente MCP

El agente MCP cumple los siguientes roles:

1. **Receptor**: Recibe requests HTTP de clientes
2. **Validador**: Valida y sanitiza los inputs
3. **Procesador**: Prepara prompts y contexto para el LLM
4. **Ejecutor**: Invoca el LLM o herramientas según sea necesario
5. **Formateador**: Estructura las respuestas en formato JSON
6. **Gestor de Errores**: Maneja errores y devuelve respuestas apropiadas

## 3. Interfaz HTTP

### 3.1 Endpoint Principal: POST /prompt

**Descripción**: Procesa un prompt del usuario y devuelve la respuesta del agente/LLM.

**URL**: `http://localhost:8000/prompt`

**Método**: `POST`

**Headers**:
```
Content-Type: application/json
```

**Request Body (JSON)**:

```json
{
  "prompt": "string (requerido)",
  "context": {
    "user_id": "string (opcional)",
    "session_id": "string (opcional)",
    "metadata": {}
  },
  "options": {
    "temperature": 0.7,
    "max_tokens": 1000,
    "model": "gpt-4"
  }
}
```

**Campos**:

- `prompt` (string, requerido): El texto del prompt que el usuario quiere procesar
- `context` (object, opcional): Información contextual adicional
  - `user_id` (string): Identificador del usuario
  - `session_id` (string): Identificador de la sesión
  - `metadata` (object): Metadatos adicionales
- `options` (object, opcional): Opciones de configuración del LLM
  - `temperature` (float): Control de aleatoriedad (0.0 - 1.0)
  - `max_tokens` (integer): Máximo de tokens en la respuesta
  - `model` (string): Modelo LLM a usar

**Response Body (JSON)**:

```json
{
  "response": "string",
  "metadata": {
    "agent_version": "string",
    "processed_at": "ISO 8601 timestamp",
    "model_used": "string",
    "tokens_used": 0
  }
}
```

**Campos de Respuesta**:

- `response` (string): La respuesta procesada por el agente/LLM
- `metadata` (object): Información sobre el procesamiento
  - `agent_version` (string): Versión del agente
  - `processed_at` (string): Timestamp del procesamiento
  - `model_used` (string): Modelo LLM utilizado
  - `tokens_used` (integer): Tokens consumidos

**Códigos de Estado HTTP**:

- `200 OK`: Request procesado exitosamente
- `400 Bad Request`: Request inválido (falta prompt, JSON malformado)
- `500 Internal Server Error`: Error interno del agente o LLM

### 3.2 Endpoint de Salud: GET /health

**Descripción**: Verifica que el agente está operativo.

**URL**: `http://localhost:8000/health`

**Método**: `GET`

**Response Body (JSON)**:

```json
{
  "status": "healthy",
  "version": "1.0.0",
  "uptime_seconds": 3600
}
```

## 4. Interfaz Programática (Python)

### 4.1 Función `process_prompt`

La función principal del agente es `process_prompt()`, que puede invocarse directamente en Python:

```python
from examples.agent import process_prompt

# Procesar un prompt
result = process_prompt(
    prompt="¿Cuál es el clima hoy?",
    context={"user_id": "user123"},
    options={"temperature": 0.7}
)

print(result["response"])
# Output: "Procesado: ¿Cuál es el clima hoy?"
```

**Signatura**:

```python
def process_prompt(prompt: str, context: dict = None, options: dict = None) -> dict:
    """
    Procesa un prompt y devuelve la respuesta del agente.
    
    Args:
        prompt (str): El texto del prompt a procesar
        context (dict, opcional): Contexto adicional
        options (dict, opcional): Opciones de configuración
    
    Returns:
        dict: Diccionario con 'response' y 'metadata'
    """
```

## 5. Flujo de Decisión

El agente MCP sigue este flujo de procesamiento:

```
1. Recibir Request HTTP (POST /prompt)
         │
         ▼
2. Validar JSON y extraer 'prompt'
         │
         ▼
3. ¿Es válido el prompt? ─── No ──> Devolver error 400
         │ Sí
         ▼
4. Preparar contexto y opciones
         │
         ▼
5. Invocar LLM o Mock
         │
         ▼
6. Procesar respuesta del LLM
         │
         ▼
7. Construir response JSON
         │
         ▼
8. Devolver HTTP 200 con response
```

## 6. Ejemplos de Uso

### 6.1 Ejemplo Básico con cURL

```bash
curl -X POST http://localhost:8000/prompt \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "Explícame qué es un agente MCP"
  }'
```

**Respuesta**:

```json
{
  "response": "Procesado: Explícame qué es un agente MCP",
  "metadata": {
    "agent_version": "1.0.0",
    "processed_at": "2025-10-28T18:55:00Z"
  }
}
```

### 6.2 Ejemplo con Contexto

```bash
curl -X POST http://localhost:8000/prompt \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "¿Cuál es mi última pregunta?",
    "context": {
      "user_id": "user123",
      "session_id": "session456"
    }
  }'
```

**Respuesta**:

```json
{
  "response": "Procesado: ¿Cuál es mi última pregunta?",
  "metadata": {
    "agent_version": "1.0.0",
    "processed_at": "2025-10-28T18:55:00Z"
  }
}
```

### 6.3 Ejemplo con Python (requests)

```python
import requests
import json

url = "http://localhost:8000/prompt"
payload = {
    "prompt": "Resume este texto: El agente MCP es un intermediario...",
    "options": {
        "temperature": 0.5,
        "max_tokens": 500
    }
}

response = requests.post(url, json=payload)
data = response.json()

print(data["response"])
```

### 6.4 Ejemplo Programático (sin HTTP)

```python
from examples.agent import process_prompt

# Uso directo de la función
result = process_prompt(
    prompt="Genera un haiku sobre la IA",
    options={"temperature": 0.9}
)

print(result["response"])
```

## 7. Extensibilidad

### 7.1 Adaptadores LLM

El agente puede extenderse con adaptadores para diferentes proveedores:

```python
class LLMAdapter:
    def call(self, prompt: str, options: dict) -> str:
        raise NotImplementedError

class OpenAIAdapter(LLMAdapter):
    def call(self, prompt: str, options: dict) -> str:
        # Llamar a OpenAI API
        pass

class AnthropicAdapter(LLMAdapter):
    def call(self, prompt: str, options: dict) -> str:
        # Llamar a Anthropic API
        pass
```

### 7.2 Herramientas (Tools)

El agente puede invocar herramientas externas:

```python
class Tool:
    def execute(self, params: dict) -> str:
        raise NotImplementedError

class WebSearchTool(Tool):
    def execute(self, params: dict) -> str:
        # Ejecutar búsqueda web
        pass
```

## 8. Consideraciones de Seguridad

- **Validación de Inputs**: Todos los prompts deben validarse y sanitizarse
- **Rate Limiting**: Implementar límites de requests por usuario/IP
- **Autenticación**: Usar API keys o tokens JWT en producción
- **HTTPS**: Siempre usar HTTPS en producción
- **Secrets Management**: Nunca hardcodear API keys, usar variables de entorno
- **Logging**: Auditar todos los prompts para detectar abuso
- **Timeout**: Implementar timeouts para evitar requests bloqueantes

## 9. Implementación de Referencia

La implementación de referencia se encuentra en:

- **Código**: `examples/agent.py`
- **Dockerfile**: `examples/Dockerfile`
- **Docker Compose**: `examples/docker-compose.yml`
- **Tests**: `tests/test_agent_basic.py`

## 10. Versión del Protocolo

- **Versión actual**: 1.0.0
- **Fecha**: 2025-10-28
- **Estado**: Draft

---

**Nota**: Esta especificación es un punto de partida educativo. Para implementaciones en producción, considera usar frameworks establecidos como [LangChain](https://www.langchain.com/) o [LlamaIndex](https://www.llamaindex.ai/).
