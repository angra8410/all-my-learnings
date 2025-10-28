# Especificación del MCP Agent

## Introducción

Esta especificación define el comportamiento, la arquitectura y los contratos de interfaz del **MCP Agent** (Model Context Protocol Agent). El agente está diseñado para procesar prompts estructurados, mantener contexto de conversación y generar respuestas coherentes siguiendo el protocolo MCP.

## Roles del Agente

El MCP Agent puede asumir diferentes roles dependiendo del contexto:

### 1. **Asistente General**
- Responde preguntas generales
- Proporciona información y explicaciones
- Mantiene conversaciones contextuales

### 2. **Procesador de Tareas**
- Ejecuta tareas específicas basadas en prompts estructurados
- Extrae información de los prompts
- Devuelve resultados formateados

### 3. **Analizador de Contexto**
- Analiza el contexto proporcionado en el prompt
- Identifica intenciones y entidades
- Genera respuestas contextualizadas

## Arquitectura del Sistema

```
┌─────────────────────────────────────────────────┐
│                  MCP Agent                       │
├─────────────────────────────────────────────────┤
│                                                  │
│  ┌──────────────┐      ┌──────────────┐        │
│  │   Prompt     │──────▶   Parser      │        │
│  │   Handler    │      └──────────────┘        │
│  └──────────────┘              │                │
│         │                      ▼                │
│         │              ┌──────────────┐        │
│         │              │   Context    │        │
│         │              │   Manager    │        │
│         │              └──────────────┘        │
│         │                      │                │
│         ▼                      ▼                │
│  ┌──────────────┐      ┌──────────────┐        │
│  │  LLM Mock    │◀─────│  Decision    │        │
│  │  Adapter     │      │  Engine      │        │
│  └──────────────┘      └──────────────┘        │
│         │                      │                │
│         ▼                      ▼                │
│  ┌──────────────────────────────────┐          │
│  │    Response Formatter             │          │
│  └──────────────────────────────────┘          │
│                   │                              │
└───────────────────┼──────────────────────────────┘
                    │
                    ▼
              [Response Output]
```

## Interfaz de Prompts

### Formato de Input

El agente acepta prompts en formato de texto plano o estructurado:

#### Prompt Simple (Texto Plano)
```
"¿Cuál es la capital de Francia?"
```

#### Prompt Estructurado (JSON)
```json
{
  "prompt": "¿Cuál es la capital de Francia?",
  "context": {
    "conversation_id": "conv-123",
    "user_id": "user-456",
    "role": "asistente"
  },
  "parameters": {
    "max_tokens": 100,
    "temperature": 0.7
  }
}
```

### Formato de Output

#### Respuesta Simple
```
"La capital de Francia es París."
```

#### Respuesta Estructurada
```json
{
  "response": "La capital de Francia es París.",
  "metadata": {
    "model": "mcp-mock-v1",
    "tokens_used": 15,
    "processing_time_ms": 45,
    "conversation_id": "conv-123"
  },
  "status": "success"
}
```

## Flujo de Decisión

El agente sigue este flujo de decisión para procesar prompts:

```
1. Recibir Prompt
   │
   ▼
2. Validar Formato
   │
   ├─ Válido ──────────────┐
   │                       │
   └─ Inválido → Error     │
                           ▼
3. Parsear Prompt y Extraer Contexto
   │
   ▼
4. Determinar Intención
   │
   ├─ Pregunta ──────────┐
   ├─ Tarea ─────────────┤
   └─ Conversación ──────┤
                         │
                         ▼
5. Generar Respuesta (Mock LLM)
   │
   ▼
6. Formatear Output
   │
   ▼
7. Devolver Respuesta
```

## Ejemplos de Prompts y Respuestas

### Ejemplo 1: Pregunta Simple

**Input:**
```python
prompt = "¿Qué es el Model Context Protocol?"
```

**Output:**
```
"Respuesta del agente MCP: ¿Qué es el Model Context Protocol?"
```

### Ejemplo 2: Prompt con Contexto

**Input:**
```python
prompt = {
    "prompt": "Continúa la conversación sobre Python",
    "context": {
        "previous_topic": "Programación en Python",
        "conversation_id": "conv-789"
    }
}
```

**Output:**
```json
{
  "response": "Basado en el contexto de Python, aquí está la respuesta...",
  "metadata": {
    "conversation_id": "conv-789",
    "context_used": true
  }
}
```

### Ejemplo 3: Tarea Estructurada

**Input:**
```python
prompt = {
    "action": "summarize",
    "content": "El texto largo a resumir...",
    "max_length": 50
}
```

**Output:**
```json
{
  "response": "Resumen: ...",
  "metadata": {
    "action": "summarize",
    "original_length": 500,
    "summary_length": 45
  }
}
```

## Contratos de Interfaz

### Clase MCPAgent

```python
class MCPAgent:
    """
    Agente principal del protocolo MCP.
    """
    
    def __init__(self, config: dict = None):
        """
        Inicializa el agente con configuración opcional.
        
        Args:
            config (dict): Configuración del agente
        """
        pass
    
    def process_prompt(self, prompt: str | dict) -> str | dict:
        """
        Procesa un prompt y devuelve una respuesta.
        
        Args:
            prompt (str | dict): Prompt de entrada
            
        Returns:
            str | dict: Respuesta generada
        """
        pass
    
    def set_context(self, context: dict) -> None:
        """
        Establece el contexto para la siguiente interacción.
        
        Args:
            context (dict): Diccionario con información de contexto
        """
        pass
```

## Parámetros de Configuración

| Parámetro | Tipo | Descripción | Default |
|-----------|------|-------------|---------|
| `model_name` | string | Nombre del modelo mock | "mcp-mock-v1" |
| `max_tokens` | integer | Máximo de tokens en respuesta | 500 |
| `temperature` | float | Temperatura para generación | 0.7 |
| `timeout_seconds` | integer | Timeout para procesamiento | 30 |
| `enable_context` | boolean | Habilitar gestión de contexto | true |

## Manejo de Errores

El agente define los siguientes tipos de error:

- **ValidationError**: Prompt con formato inválido
- **ProcessingError**: Error durante el procesamiento
- **TimeoutError**: El procesamiento excedió el tiempo límite
- **ContextError**: Error en la gestión de contexto

Ejemplo de respuesta de error:

```json
{
  "status": "error",
  "error": {
    "type": "ValidationError",
    "message": "El prompt debe ser un string o dict",
    "code": "INVALID_PROMPT_FORMAT"
  }
}
```

## Extensibilidad

El agente está diseñado para ser extensible:

1. **Nuevos Adaptadores LLM**: Implementar la interfaz `LLMAdapter`
2. **Procesadores Personalizados**: Extender `PromptProcessor`
3. **Formateadores de Respuesta**: Implementar `ResponseFormatter`
4. **Plugins de Contexto**: Agregar nuevos `ContextManager` plugins

## Consideraciones de Seguridad

En futuras versiones se implementarán:

- Validación y sanitización de inputs
- Rate limiting
- Autenticación de usuarios
- Encriptación de datos sensibles
- Auditoría de prompts y respuestas

## Roadmap

- **v0.1 (Actual)**: Scaffold básico con mock LLM
- **v0.2**: Integración con OpenAI API
- **v0.3**: Sistema de contexto persistente
- **v0.4**: Soporte para múltiples modelos
- **v1.0**: Producción-ready con seguridad completa

---

**Versión**: 0.1.0  
**Última Actualización**: Octubre 2025
