# Dockerfile para MCP Agent
# Este Dockerfile conteneriza el agente MCP de ejemplo

FROM python:3.11-slim

# Metadata del contenedor
LABEL maintainer="MCP Agent Team"
LABEL description="MCP Agent - Minimal Implementation Example"
LABEL version="1.0.0"

# Establecer directorio de trabajo
WORKDIR /app

# Copiar el código del agente
COPY agent.py .

# Exponer el puerto del agente (por defecto 8000)
EXPOSE 8000

# Health check: verifica que el servidor responde
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD python3 -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

# Comando para ejecutar el agente
# Se puede override el puerto con: docker run -p 8080:8080 mcp-agent 8080
CMD ["python3", "agent.py", "8000"]
