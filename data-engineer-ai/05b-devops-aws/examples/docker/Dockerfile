# Dockerfile para aplicación Python compatible con ECS Fargate
# Este Dockerfile crea una imagen ligera con un servidor HTTP simple
# que incluye un endpoint /health para health checks

# Usar imagen oficial de Python 3.11 slim (más ligera que la versión completa)
FROM python:3.11-slim

# Metadata del contenedor
LABEL maintainer="data-engineer-learning"
LABEL description="Simple Python app for ECS demonstration"
LABEL version="1.0"

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copiar archivo de requirements (si existe)
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Por ahora solo necesitamos Flask para el servidor simple
RUN pip install --no-cache-dir flask gunicorn

# Copiar código de la aplicación
COPY app.py .

# Crear usuario no-root para ejecutar la aplicación (best practice de seguridad)
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app

# Cambiar a usuario no-root
USER appuser

# Exponer el puerto 8080 (puerto estándar para aplicaciones no-privilegiadas)
EXPOSE 8080

# Health check para que ECS sepa cuando el contenedor está listo
HEALTHCHECK --interval=30s --timeout=3s --start-period=40s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

# Variable de entorno para configuración
ENV FLASK_APP=app.py
ENV PYTHONUNBUFFERED=1

# Comando para iniciar la aplicación con gunicorn (production-ready WSGI server)
# 4 workers, bind a todas las interfaces en puerto 8080, timeout de 120s
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "--workers", "4", "--timeout", "120", "app:app"]
