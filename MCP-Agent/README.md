# MCP Agent - Scaffold y Ejemplos

## Visión General

Este directorio contiene la especificación, scaffolding y ejemplos iniciales para el desarrollo de un **MCP Agent** (Model Context Protocol Agent). El objetivo es proporcionar una base sólida y reutilizable para construir agentes que procesen prompts y generen respuestas utilizando el protocolo MCP.

## Objetivos

- **Definir la especificación** del agente MCP: roles, interfaz de prompts, flujo de decisión
- **Proporcionar ejemplos funcionales** que puedan ejecutarse localmente
- **Establecer una base de tests** para validar el comportamiento del agente
- **Facilitar la contenerización** mediante Docker para despliegues consistentes
- **Documentar el proceso** para que otros desarrolladores puedan extender el agente

## Estructura del Proyecto

```
MCP-Agent/
├── README.md                      # Este archivo
├── spec.md                        # Especificación técnica del agente MCP
├── run.sh                         # Script para ejecutar el agente localmente
├── examples/
│   ├── agent.py                   # Implementación de ejemplo del agente
│   ├── Dockerfile                 # Dockerfile para contenerizar el agente
│   └── docker-compose.yml         # Orquestación de servicios
└── tests/
    └── test_agent_basic.py        # Tests unitarios básicos
```

## Requisitos

### Para ejecución local (Python)
- Python 3.9 o superior
- pip (gestor de paquetes de Python)

### Para ejecución con Docker
- Docker 20.10 o superior
- Docker Compose 2.0 o superior

## Cómo Probar Localmente

### Opción 1: Ejecución directa con Python

1. **Instalar dependencias** (si las hubiera en el futuro):
   ```bash
   cd MCP-Agent
   # pip install -r requirements.txt  # Cuando se agreguen dependencias
   ```

2. **Ejecutar el agente usando el script**:
   ```bash
   chmod +x run.sh
   ./run.sh
   ```

3. **O ejecutar directamente con Python**:
   ```bash
   python examples/agent.py
   ```

### Opción 2: Ejecución con Docker

1. **Construir la imagen Docker**:
   ```bash
   cd MCP-Agent/examples
   docker build -t mcp-agent:latest .
   ```

2. **Ejecutar el contenedor**:
   ```bash
   docker run --rm mcp-agent:latest
   ```

3. **O usar Docker Compose para orquestación completa**:
   ```bash
   cd MCP-Agent/examples
   docker-compose up
   ```

### Opción 3: Ejecutar tests unitarios

```bash
cd MCP-Agent
python -m pytest tests/test_agent_basic.py -v
```

O si no tienes pytest instalado:

```bash
python -m unittest tests.test_agent_basic
```

## Estado Actual

⚠️ **Nota**: Esta es una versión inicial de scaffolding. Los componentes actuales incluyen:

- ✅ Mock de LLM: El agente utiliza respuestas simuladas (no un LLM real)
- ✅ Estructura básica: Interfaz de prompts y procesamiento de respuestas
- ✅ Tests unitarios: Validación básica del flujo del agente
- ✅ Contenerización: Dockerfile y docker-compose funcionales

### Próximos Pasos

- Integrar un LLM real (OpenAI, Anthropic, modelos locales, etc.)
- Añadir gestión de claves API de forma segura (variables de entorno, secrets)
- Implementar logging y monitoreo
- Expandir la cobertura de tests
- Añadir ejemplos de casos de uso más complejos

## Contribuir

Para extender este agente:

1. Revisa la especificación en `spec.md`
2. Modifica `examples/agent.py` según tus necesidades
3. Añade tests en `tests/` para nuevas funcionalidades
4. Actualiza la documentación correspondiente

## Seguridad y Claves

🔒 **Importante**: Esta versión de ejemplo NO incluye manejo de claves API reales ni tokens de autenticación. Al integrar un LLM real:

- Usa variables de entorno para claves sensibles
- NO hagas commit de claves en el código
- Considera usar servicios de secrets management (AWS Secrets Manager, HashiCorp Vault, etc.)
- Implementa rate limiting y validación de entrada

## Recursos Adicionales

- [Model Context Protocol Specification](https://spec.modelcontextprotocol.io/)
- [Docker Documentation](https://docs.docker.com/)
- [Python Best Practices](https://docs.python-guide.org/)

---

**¡Comienza a experimentar con tu propio MCP Agent!** 🚀
