# FromZero-Agentic-Docker: Curso Práctico From Zero to Agentic con Docker

¡Bienvenido al curso más práctico de agentes con IA y Docker! Este es un curso **90% hands-on** diseñado para llevarte desde cero hasta crear, contenedorizar y desplegar un sistema de agentes con IA completamente funcional.

## 🎯 Objetivos del Curso

Al finalizar este curso, serás capaz de:

- ✅ Comprender los fundamentos de Docker y contenedorización
- ✅ Diseñar y construir un agente con IA (agent core) desde cero
- ✅ Implementar prompts efectivos y herramientas (tools) para tu agente
- ✅ Contenedorizar aplicaciones FastAPI con Docker
- ✅ Orquestar servicios múltiples con docker-compose
- ✅ Realizar testing y debugging en entornos contenedorizados
- ✅ Desplegar tu aplicación a producción
- ✅ Integrar todos los componentes en un proyecto real

## 📚 Estructura de Módulos

Este curso está organizado en 10 módulos progresivos:

### Módulo 01: Introducción
Visión general del curso, conceptos de agentes con IA y Docker.

### Módulo 02: Prerrequisitos y Entorno
Configuración del entorno de desarrollo: Python, Docker, herramientas CLI.

### Módulo 03: Docker Básico
Comandos esenciales, Dockerfile, imágenes y contenedores.

### Módulo 04: Construye la Agent Core
Diseño e implementación del motor del agente con IA.

### Módulo 05: Prompts y Herramientas
Creación de prompts efectivos y herramientas (tools) para el agente.

### Módulo 06: Contenedoriza la App
Dockeriza tu aplicación FastAPI y el agente.

### Módulo 07: Docker Compose y Servicios
Orquestación de múltiples servicios con docker-compose.

### Módulo 08: Testing y Debugging
Estrategias de testing, pytest y debugging en contenedores.

### Módulo 09: Despliegue a Producción
Mejores prácticas para producción, optimización y monitoreo.

### Módulo 10: Proyecto Integrador
Integración completa de todos los componentes en un proyecto real.

## 🚀 Cómo Usar Este Curso

### Estructura de Cada Módulo

Cada módulo contiene 4 archivos:

1. **README.md** - Objetivos y contenido principal del módulo
2. **actividad-interactiva.md** - Ejercicios prácticos paso a paso
3. **retroalimentacion.md** - Plantillas para registrar tus resultados
4. **progreso.md** - Checklist de tareas completadas

### Flujo de Trabajo Recomendado

1. **Lee** el README.md del módulo
2. **Practica** con los ejercicios en actividad-interactiva.md
3. **Registra** tus resultados en retroalimentacion.md
4. **Marca** tu progreso en progreso.md
5. **Repite** hasta completar todos los módulos

## 💻 Requisitos Previos

- Python 3.9 o superior
- Docker Desktop instalado
- Editor de código (VS Code recomendado)
- Terminal/línea de comandos
- Git básico

## 🛠️ Instalación y Configuración

### 1. Clonar el Repositorio

```bash
git clone https://github.com/angra8410/all-my-learnings.git
cd all-my-learnings/FromZero-Agentic-Docker
```

### 2. Verificar Docker

```bash
docker --version
docker ps
```

### 3. Verificar Python

```bash
python --version
pip --version
```

## 🧪 Cómo Probar los Ejemplos

### Ejecutar Docker Básico

```bash
# Construir una imagen
docker build -t mi-app:latest .

# Ejecutar un contenedor
docker run -p 8000:8000 mi-app:latest

# Ver logs
docker logs <container-id>
```

### Ejecutar FastAPI con Uvicorn

```bash
# Instalar dependencias
pip install fastapi uvicorn

# Ejecutar la aplicación
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Acceder a la API
curl http://localhost:8000
curl http://localhost:8000/docs
```

### Ejecutar con Docker Compose

```bash
# Iniciar todos los servicios
docker-compose up -d

# Ver logs
docker-compose logs -f

# Detener servicios
docker-compose down
```

### Ejecutar Tests

```bash
# Instalar pytest
pip install pytest pytest-cov

# Ejecutar tests
pytest tests/ -v

# Con cobertura
pytest tests/ --cov=app --cov-report=html
```

## 📝 Cómo Ejecutar los Ejercicios Localmente

### Ejemplo Completo: Módulo 06

```bash
# 1. Navegar al módulo
cd modulo-06-contenedoriza-la-app/ejemplos

# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar la app localmente
uvicorn app.main:app --reload

# 5. Construir la imagen Docker
docker build -t agentic-app:v1 .

# 6. Ejecutar el contenedor
docker run -d -p 8000:8000 --name mi-agente agentic-app:v1

# 7. Probar la API
curl http://localhost:8000/health
curl -X POST http://localhost:8000/agent/query -H "Content-Type: application/json" -d '{"query": "What is the weather?"}'

# 8. Ver logs
docker logs mi-agente

# 9. Detener y limpiar
docker stop mi-agente
docker rm mi-agente
```

## 📂 Estructura del Proyecto

```
FromZero-Agentic-Docker/
├── README.md
├── modulo-01-introduccion/
│   ├── README.md
│   ├── actividad-interactiva.md
│   ├── retroalimentacion.md
│   └── progreso.md
├── modulo-02-prerrequisitos-y-entorno/
│   ├── README.md
│   ├── actividad-interactiva.md
│   ├── retroalimentacion.md
│   └── progreso.md
├── modulo-03-docker-basico/
│   ├── README.md
│   ├── actividad-interactiva.md
│   ├── retroalimentacion.md
│   ├── progreso.md
│   └── ejemplos/
│       └── Dockerfile
├── modulo-04-construye-la-agent-core/
│   ├── README.md
│   ├── actividad-interactiva.md
│   ├── retroalimentacion.md
│   ├── progreso.md
│   └── ejemplos/
│       └── agent.py
├── modulo-05-prompts-y-herramientas/
│   ├── README.md
│   ├── actividad-interactiva.md
│   ├── retroalimentacion.md
│   ├── progreso.md
│   └── ejemplos/
│       └── weather_tool.py
├── modulo-06-contenedoriza-la-app/
│   ├── README.md
│   ├── actividad-interactiva.md
│   ├── retroalimentacion.md
│   ├── progreso.md
│   └── ejemplos/
│       ├── Dockerfile
│       ├── requirements.txt
│       └── app/
│           └── main.py
├── modulo-07-docker-compose-y-servicios/
│   ├── README.md
│   ├── actividad-interactiva.md
│   ├── retroalimentacion.md
│   ├── progreso.md
│   └── ejemplos/
│       └── docker-compose.yml
├── modulo-08-testing-debugging/
│   ├── README.md
│   ├── actividad-interactiva.md
│   ├── retroalimentacion.md
│   └── progreso.md
├── modulo-09-despliegue-produccion/
│   ├── README.md
│   ├── actividad-interactiva.md
│   ├── retroalimentacion.md
│   └── progreso.md
└── modulo-10-proyecto-integrador/
    ├── README.md
    ├── actividad-interactiva.md
    ├── retroalimentacion.md
    └── progreso.md
```

## 🔍 Guardar Resultados

### Commits Regulares

```bash
git add .
git commit -m "Completado módulo 03: Docker Básico"
git push origin feature/fromzero-agentic-docker
```

### Guardar Requests y Tests

Crea un archivo `tests/requests.json` para guardar ejemplos de requests:

```json
{
  "health_check": {
    "method": "GET",
    "url": "http://localhost:8000/health",
    "response": {"status": "healthy"}
  },
  "agent_query": {
    "method": "POST",
    "url": "http://localhost:8000/agent/query",
    "body": {"query": "What is the weather in Madrid?"},
    "response": {"result": "The weather in Madrid is sunny, 25°C"}
  }
}
```

### Capturar Logs

```bash
# Logs del contenedor
docker logs mi-agente > logs/container-output.log

# Logs de la aplicación
docker exec mi-agente cat /app/logs/app.log > logs/app.log
```

## 🎓 Metodología de Aprendizaje

Este curso sigue la metodología **"Minuto Fluido"** adaptada a programación:

- **Repetición enfocada**: Ejercicios cortos y repetitivos (1-3 minutos)
- **Práctica inmediata**: Copiar, pegar, ejecutar, modificar
- **Incremento progresivo**: Cada ejercicio aumenta ligeramente la dificultad
- **Registro constante**: Documentar resultados y aprendizajes

## 💡 Consejos de Uso

1. **No saltes módulos** - Cada módulo construye sobre el anterior
2. **Practica cada comando** - No solo leas, ejecuta
3. **Modifica los ejemplos** - Experimenta con cambios
4. **Documenta tus errores** - Aprende de ellos
5. **Completa los checklists** - Te mantienen enfocado
6. **Haz commits frecuentes** - Guarda tu progreso

## 🌟 Características Especiales

- ✨ **100% Cliente-Local** - No requiere servicios externos
- ✨ **Ejemplos Copy-Paste** - Listos para usar inmediatamente
- ✨ **Instrucciones en Español** - Fácil de seguir
- ✨ **Código en Inglés** - Siguiendo best practices
- ✨ **Progresión Clara** - Del concepto a la práctica
- ✨ **Proyecto Real** - Construyes algo tangible

## 📞 Soporte

Si tienes dudas o encuentras errores:

1. Revisa el archivo `retroalimentacion.md` del módulo
2. Consulta los ejemplos en la carpeta `ejemplos/`
3. Verifica los logs con `docker logs`
4. Revisa la documentación oficial de Docker y FastAPI

## 🚦 Próximos Pasos

1. **Empieza con el Módulo 01** - Introducción
2. **Configura tu entorno** - Módulo 02
3. **Sigue la secuencia** - Módulos 03-10
4. **Completa el proyecto integrador** - Módulo 10

---

**¡Manos a la obra! Let's build something amazing! 🚀**
