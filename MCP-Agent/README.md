# MCP Agent - Model Context Protocol Agent

## Visión General

El **MCP Agent** es un agente de inteligencia artificial diseñado para procesar prompts estructurados siguiendo el protocolo Model Context Protocol (MCP). Este proyecto proporciona un scaffold inicial que incluye ejemplos de código, especificaciones técnicas y herramientas para ejecutar y probar el agente localmente.

## Objetivos

- **Procesamiento de Prompts**: Implementar un agente que pueda recibir y procesar prompts estructurados
- **Interfaz Estandarizada**: Seguir el protocolo MCP para garantizar interoperabilidad
- **Extensibilidad**: Diseño modular que permita agregar nuevos adaptadores y capacidades
- **Contenerización**: Soporte completo para Docker y despliegue en contenedores
- **Testing**: Suite de tests para validar el comportamiento del agente

## Estructura del Proyecto

```
MCP-Agent/
├── README.md                    # Este archivo
├── spec.md                      # Especificación técnica del agente MCP
├── run.sh                       # Script de ejecución local
├── examples/
│   ├── agent.py                 # Implementación de ejemplo del agente
│   ├── Dockerfile               # Dockerfile para contenerización
│   └── docker-compose.yml       # Orquestación con Docker Compose
└── tests/
    └── test_agent_basic.py      # Tests unitarios básicos
```

## Requisitos

### Para Ejecución Local (Python)

- Python 3.9 o superior
- pip (gestor de paquetes de Python)

### Para Ejecución con Docker

- Docker 20.10 o superior
- Docker Compose 1.29 o superior

## Cómo Probar Localmente

### Opción 1: Ejecución Directa con Python

1. **Instalar dependencias** (si es necesario):
   ```bash
   pip install -r requirements.txt  # Si se agregan dependencias en el futuro
   ```

2. **Ejecutar el agente con el script run.sh**:
   ```bash
   chmod +x run.sh
   ./run.sh
   ```

3. **Ejecutar el agente directamente**:
   ```bash
   cd examples
   python agent.py
   ```

### Opción 2: Ejecución con Docker

1. **Construir la imagen Docker**:
   ```bash
   cd examples
   docker build -t mcp-agent:latest .
   ```

2. **Ejecutar el contenedor**:
   ```bash
   docker run --rm mcp-agent:latest
   ```

3. **Usar Docker Compose** (recomendado):
   ```bash
   cd examples
   docker-compose up
   ```

### Ejecutar Tests

```bash
# Desde la raíz del proyecto MCP-Agent
python -m pytest tests/test_agent_basic.py -v
```

O desde la raíz del repositorio:
```bash
cd MCP-Agent
python -m pytest tests/ -v
```

## Ejemplos de Uso

El agente de ejemplo (`examples/agent.py`) procesa prompts simples y devuelve respuestas mock. Aquí un ejemplo de interacción:

```python
from examples.agent import MCPAgent

agent = MCPAgent()
response = agent.process_prompt("¿Cuál es el significado de la vida?")
print(response)
# Output: "Respuesta del agente MCP: ¿Cuál es el significado de la vida?"
```

## Notas Importantes

⚠️ **Estado Actual**: Este es un scaffold inicial con implementaciones mock.

- **Adaptadores LLM**: Los adaptadores para modelos de lenguaje son simulados (mock). No se conectan a modelos reales.
- **Seguridad**: No se incluyen mecanismos de autenticación ni manejo de claves API en esta versión inicial.
- **Producción**: Este código NO está listo para producción. Es solo un punto de partida para desarrollo.

## Próximos Pasos

1. Implementar adaptadores reales para LLMs (OpenAI, Anthropic, etc.)
2. Agregar sistema de configuración (variables de entorno, archivos config)
3. Implementar manejo de errores robusto
4. Agregar logging estructurado
5. Implementar autenticación y seguridad
6. Extender la suite de tests
7. Documentar APIs y endpoints

## Contribuir

Este es un proyecto de aprendizaje. Todas las mejoras y sugerencias son bienvenidas.

## Licencia

Este proyecto es parte de un repositorio de aprendizaje personal.

---

**¡Explora, aprende y construye! 🚀**
