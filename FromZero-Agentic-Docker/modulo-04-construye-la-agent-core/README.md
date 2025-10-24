# Módulo 04: Construye la Agent Core

## 🎯 Objetivos del Módulo

- ✅ Comprender la arquitectura de un agente con IA
- ✅ Implementar un agent core básico
- ✅ Crear sistema de herramientas (tools)
- ✅ Implementar selección y ejecución de tools
- ✅ Gestionar historial de conversación
- ✅ Probar el agente localmente

## 📖 Arquitectura del Agente

Un agente con IA típicamente tiene:

1. **Query Processing** - Procesa la entrada del usuario
2. **Intent Recognition** - Identifica la intención
3. **Tool Selection** - Selecciona la herramienta apropiada
4. **Tool Execution** - Ejecuta la herramienta
5. **Response Generation** - Genera respuesta natural

## 🔧 Componentes Principales

### Tool (Herramienta)

```python
@dataclass
class Tool:
    name: str
    description: str
    function: Callable
```

### Agent Core

```python
class AgentCore:
    def __init__(self, tools: List[Tool] = None)
    def add_tool(self, tool: Tool)
    def process_query(self, query: str) -> Dict[str, Any]
    def list_tools() -> List[str]
```

## 📝 Ejemplo Práctico

Revisa el archivo `ejemplos/agent.py` que incluye:

- Clase Tool para definir herramientas
- Clase AgentCore con lógica completa
- Análisis de queries
- Selección de tools
- Ejecución y respuestas
- Historial de conversación

## 🧪 Prueba el Agent Core

```bash
cd modulo-04-construye-la-agent-core/ejemplos
python agent.py
```

## ✅ Checklist del Módulo

- [ ] Entiendo arquitectura del agente
- [ ] Comprendo el sistema de Tools
- [ ] Puedo ejecutar agent.py
- [ ] Entiendo process_query
- [ ] Sé cómo añadir nuevas tools
- [ ] He modificado el agente

## 🎯 Próximos Pasos

Continúa al **Módulo 05: Prompts y Herramientas**
