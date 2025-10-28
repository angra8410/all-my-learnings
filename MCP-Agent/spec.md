# Especificación del MCP Agent

## 1. Introducción

Este documento define la especificación técnica para el **MCP Agent** (Model Context Protocol Agent), un sistema que procesa prompts de usuario y genera respuestas utilizando el protocolo MCP. El agente actúa como intermediario entre el usuario y un modelo de lenguaje, gestionando el contexto y el flujo de la conversación.

## 2. Roles del Agente

### 2.1. Roles Principales

El MCP Agent puede operar en diferentes roles según el contexto:

- **Asistente General**: Responde preguntas y proporciona información
- **Procesador de Tareas**: Ejecuta tareas específicas basadas en prompts estructurados
- **Analizador de Contexto**: Mantiene y gestiona el contexto de conversaciones multi-turno
- **Router**: Redirige solicitudes a diferentes componentes o herramientas según el prompt

### 2.2. Responsabilidades

1. **Recibir y validar prompts** de entrada
2. **Procesar y enriquecer** el prompt con contexto relevante
3. **Invocar el modelo de lenguaje** (o mock en esta versión)
4. **Post-procesar la respuesta** del modelo
5. **Formatear y devolver** la respuesta al usuario

## 3. Interfaz de Prompts

### 3.1. Formato de Entrada

El agente acepta prompts en formato de diccionario/JSON con la siguiente estructura:

```python
{
    "prompt": str,              # El texto del prompt (REQUERIDO)
    "role": str,                # Rol del usuario: "user", "system", "assistant" (opcional, default: "user")
    "context": dict,            # Contexto adicional (opcional)
    "max_tokens": int,          # Máximo de tokens en la respuesta (opcional, default: 150)
    "temperature": float,       # Temperatura del modelo (opcional, default: 0.7)
    "metadata": dict            # Metadatos adicionales (opcional)
}
```

**Ejemplo de prompt simple**:
```python
{
    "prompt": "¿Cuál es la capital de Francia?",
    "role": "user"
}
```

**Ejemplo de prompt con contexto**:
```python
{
    "prompt": "¿Y cuál es su población?",
    "role": "user",
    "context": {
        "previous_question": "¿Cuál es la capital de Francia?",
        "previous_answer": "La capital de Francia es París."
    }
}
```

### 3.2. Formato de Salida

El agente devuelve una respuesta en formato de diccionario con la siguiente estructura:

```python
{
    "response": str,            # La respuesta generada
    "status": str,              # Estado: "success", "error", "partial"
    "metadata": {
        "model": str,           # Modelo utilizado
        "tokens_used": int,     # Tokens consumidos
        "processing_time": float, # Tiempo de procesamiento en segundos
        "timestamp": str        # Timestamp ISO 8601
    },
    "error": str                # Mensaje de error (solo si status == "error")
}
```

**Ejemplo de respuesta exitosa**:
```python
{
    "response": "La capital de Francia es París.",
    "status": "success",
    "metadata": {
        "model": "mock-llm-v1",
        "tokens_used": 8,
        "processing_time": 0.05,
        "timestamp": "2025-10-28T18:41:14.766Z"
    }
}
```

## 4. Flujo de Decisión

### 4.1. Diagrama de Flujo

```
┌─────────────────────┐
│  Recibir Prompt     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Validar Input      │
└──────────┬──────────┘
           │
           ├─── ✗ Error ──────────────┐
           │                          │
           ▼ ✓ Válido                 ▼
┌─────────────────────┐      ┌──────────────┐
│  Enriquecer         │      │ Retornar     │
│  con Contexto       │      │ Error        │
└──────────┬──────────┘      └──────────────┘
           │
           ▼
┌─────────────────────┐
│  Invocar LLM/Mock   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Post-procesar      │
│  Respuesta          │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Formatear y        │
│  Retornar           │
└─────────────────────┘
```

### 4.2. Lógica de Decisión

1. **Validación de Input**:
   - Verificar que el campo `prompt` existe y no está vacío
   - Validar tipos de datos de campos opcionales
   - Si falla: retornar error con status 400

2. **Enriquecimiento de Contexto**:
   - Si existe campo `context`, agregarlo al prompt
   - Aplicar templates de sistema según el `role`
   - Preparar prompt final para el LLM

3. **Invocación del Modelo**:
   - En versión mock: generar respuesta predefinida
   - En versión producción: llamar API del LLM
   - Manejar timeouts y errores de API

4. **Post-procesamiento**:
   - Limpiar formato de la respuesta
   - Extraer metadatos (tokens, tiempo, etc.)
   - Validar longitud y contenido

5. **Formateo Final**:
   - Construir objeto de respuesta según especificación
   - Añadir timestamp y metadata
   - Retornar al cliente

## 5. Ejemplos de Prompts

### 5.1. Prompt Simple

**Input**:
```python
{
    "prompt": "Explica qué es el Model Context Protocol"
}
```

**Output**:
```python
{
    "response": "El Model Context Protocol (MCP) es un protocolo estandarizado para la comunicación entre aplicaciones y modelos de lenguaje...",
    "status": "success",
    "metadata": {
        "model": "mock-llm-v1",
        "tokens_used": 45,
        "processing_time": 0.12,
        "timestamp": "2025-10-28T18:41:14.766Z"
    }
}
```

### 5.2. Prompt con Contexto Multi-turno

**Input (turno 1)**:
```python
{
    "prompt": "¿Qué es Python?",
    "role": "user"
}
```

**Output (turno 1)**:
```python
{
    "response": "Python es un lenguaje de programación de alto nivel...",
    "status": "success",
    "metadata": {...}
}
```

**Input (turno 2)**:
```python
{
    "prompt": "Dame un ejemplo de código",
    "role": "user",
    "context": {
        "previous_question": "¿Qué es Python?",
        "previous_answer": "Python es un lenguaje de programación de alto nivel..."
    }
}
```

### 5.3. Prompt con Configuración Avanzada

**Input**:
```python
{
    "prompt": "Genera un poema corto sobre la IA",
    "role": "user",
    "max_tokens": 100,
    "temperature": 0.9,
    "metadata": {
        "user_id": "user123",
        "session_id": "sess456"
    }
}
```

## 6. Extensibilidad

### 6.1. Puntos de Extensión

El diseño del agente permite extender funcionalidad en:

- **Validadores personalizados**: Añadir lógica de validación específica
- **Procesadores de contexto**: Implementar estrategias de gestión de contexto
- **Adaptadores de LLM**: Integrar diferentes proveedores (OpenAI, Anthropic, etc.)
- **Post-procesadores**: Aplicar transformaciones a las respuestas

### 6.2. Interfaces Recomendadas

```python
class PromptProcessor:
    def validate(self, prompt: dict) -> bool:
        """Valida el formato del prompt"""
        pass
    
    def enrich_context(self, prompt: dict) -> dict:
        """Enriquece el prompt con contexto adicional"""
        pass
    
    def process(self, prompt: dict) -> dict:
        """Procesa el prompt y genera respuesta"""
        pass
```

## 7. Consideraciones de Implementación

### 7.1. Rendimiento
- Implementar caching de respuestas frecuentes
- Usar conexiones persistentes con APIs de LLM
- Implementar timeouts apropiados (< 30s)

### 7.2. Seguridad
- Sanitizar inputs para prevenir inyección de prompts
- Validar longitud máxima de prompts
- Implementar rate limiting
- No registrar contenido sensible en logs

### 7.3. Escalabilidad
- Diseño stateless para permitir escalado horizontal
- Uso de colas para procesamiento asíncrono si es necesario
- Separación de concerns (validación, procesamiento, respuesta)

## 8. Limitaciones Actuales (v0.1 - Mock)

- ✓ Respuestas simuladas (no LLM real)
- ✓ Sin persistencia de contexto entre sesiones
- ✓ Sin autenticación ni autorización
- ✓ Sin rate limiting
- ✓ Sin métricas ni observabilidad avanzada

## 9. Roadmap

### Versión 0.2
- Integración con LLM real (OpenAI API)
- Gestión de claves API mediante variables de entorno
- Logging estructurado

### Versión 0.3
- Persistencia de contexto (Redis/PostgreSQL)
- Sistema de plugins para extender funcionalidad
- Métricas y observabilidad (Prometheus)

### Versión 1.0
- Autenticación y autorización
- Rate limiting y quotas
- Múltiples backends de LLM
- API REST completa

---

**Versión**: 0.1-mock  
**Última actualización**: 2025-10-28  
**Autores**: Team MCP Agent
