# Módulo 01: Introducción

## 🎯 Objetivos del Módulo

Al finalizar este módulo, habrás:

- ✅ Comprendido qué es un agente con IA y por qué es importante
- ✅ Entendido los fundamentos de Docker y la contenedorización
- ✅ Identificado los componentes clave de un sistema agentic
- ✅ Establecido tus expectativas y objetivos personales del curso
- ✅ Familiarizado con la estructura y metodología del curso

## 📖 ¿Qué es un Agente con IA?

Un **agente con IA** es un sistema de software que puede:

1. **Percibir** su entorno (recibir inputs)
2. **Razonar** sobre la información (procesar con IA)
3. **Actuar** para lograr objetivos (ejecutar acciones)
4. **Aprender** de las interacciones (mejorar con el tiempo)

### Componentes de un Agente

```
┌─────────────────────────────────────┐
│         User Interface              │
│    (API REST, CLI, Web, etc.)       │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│          Agent Core                 │
│  • Prompt Engineering               │
│  • Reasoning & Planning             │
│  • Tool Selection                   │
└─────────────────────────────────────┘
                 ↓
┌─────────────────────────────────────┐
│           Tools Layer               │
│  • Weather API                      │
│  • Database Access                  │
│  • File System                      │
│  • External Services                │
└─────────────────────────────────────┘
```

### Ejemplos de Agentes

- **ChatGPT** - Agente conversacional
- **GitHub Copilot** - Agente de código
- **Siri/Alexa** - Agentes de voz
- **Trading Bots** - Agentes financieros
- **Tu propio agente** - ¡Lo que construirás en este curso!

## 🐳 ¿Qué es Docker?

**Docker** es una plataforma de contenedorización que permite:

1. **Empaquetar** aplicaciones con todas sus dependencias
2. **Ejecutar** aplicaciones de forma aislada y consistente
3. **Desplegar** aplicaciones en cualquier entorno
4. **Escalar** aplicaciones fácilmente

### ¿Por qué Docker para Agentes con IA?

- ✅ **Reproducibilidad** - La misma versión de Python, librerías, etc.
- ✅ **Aislamiento** - No conflictos con otras aplicaciones
- ✅ **Portabilidad** - Funciona en tu laptop, servidor, cloud
- ✅ **Escalabilidad** - Fácil de replicar y escalar
- ✅ **Simplicidad** - Un comando para ejecutar todo

### Analogía: Docker como un Contenedor de Envío

Imagina que tu aplicación es mercancía:

- **Sin Docker**: Cada mercancía necesita transporte diferente
- **Con Docker**: Todo va en contenedores estándar que cualquier barco puede transportar

```
┌────────────────────┐
│   Mi Aplicación    │
│   + Python 3.9     │
│   + FastAPI        │
│   + OpenAI SDK     │
│   + Dependencies   │
└────────────────────┘
     ↓ Docker build
┌────────────────────┐
│  Docker Image      │  ← Empaquetado
└────────────────────┘
     ↓ Docker run
┌────────────────────┐
│  Container         │  ← Ejecutando
│  (Proceso aislado) │
└────────────────────┘
```

## 🎓 Estructura del Curso

### Progresión de Aprendizaje

```
Módulo 01: Introducción (tú estás aquí)
    ↓
Módulo 02: Configurar entorno (Python, Docker, CLI)
    ↓
Módulo 03: Docker básico (comandos, Dockerfile)
    ↓
Módulo 04: Agent core (diseño e implementación)
    ↓
Módulo 05: Prompts y tools (funcionalidad del agente)
    ↓
Módulo 06: Contenedorizar app (FastAPI + Docker)
    ↓
Módulo 07: Docker Compose (orquestación)
    ↓
Módulo 08: Testing & Debugging (calidad)
    ↓
Módulo 09: Producción (deployment, optimización)
    ↓
Módulo 10: Proyecto integrador (todo junto)
```

### Metodología "Minuto Fluido" para Programación

Adaptamos la técnica de aprendizaje de idiomas al código:

1. **Ejercicio corto** (1-3 minutos)
2. **Repetición inmediata** (3-5 veces)
3. **Incremento gradual** (pequeños cambios)
4. **Registro de resultados** (documentar)

**Ejemplo aplicado:**

```bash
# Minuto fluido 1: Ejecutar comando básico (1 min)
docker --version

# Minuto fluido 2: Ver imágenes (1 min)
docker images

# Minuto fluido 3: Ver contenedores (1 min)
docker ps -a

# Repetir x3 hasta que sea automático
```

## 📊 Lo que Construirás

Al final del curso, tendrás un sistema completo:

```
┌─────────────────────────────────────────────┐
│        Weather Agent System                 │
├─────────────────────────────────────────────┤
│                                             │
│  FastAPI REST API                           │
│    ├── /health                              │
│    ├── /agent/query                         │
│    └── /docs                                │
│                                             │
│  Agent Core                                 │
│    ├── Prompt Engineering                   │
│    ├── Tool Selection                       │
│    └── Response Generation                  │
│                                             │
│  Tools                                      │
│    ├── Weather Tool (mock)                  │
│    ├── Time Tool                            │
│    └── Calculator Tool                      │
│                                             │
│  Containerized with Docker                  │
│    ├── Dockerfile                           │
│    ├── docker-compose.yml                   │
│    └── Ready for production                 │
│                                             │
│  Tested & Documented                        │
│    ├── Unit tests (pytest)                  │
│    ├── API tests                            │
│    └── Integration tests                    │
└─────────────────────────────────────────────┘
```

## 💪 Habilidades que Desarrollarás

### Técnicas

- ✅ Python async/await
- ✅ FastAPI development
- ✅ Docker & docker-compose
- ✅ Prompt engineering
- ✅ API design
- ✅ Testing con pytest
- ✅ Logging y debugging

### Conceptuales

- ✅ Arquitectura de agentes
- ✅ Contenedorización
- ✅ Microservicios
- ✅ CI/CD basics
- ✅ Production best practices

## 🚀 Expectativas y Compromiso

### Lo que HARÁS en este curso:

- ✅ Escribir código desde el primer día
- ✅ Ejecutar y probar cada ejemplo
- ✅ Modificar y experimentar
- ✅ Cometer errores y aprender de ellos
- ✅ Documentar tu progreso
- ✅ Hacer commits frecuentes

### Lo que NO harás:

- ❌ Solo leer teoría sin practicar
- ❌ Copiar sin entender
- ❌ Saltar módulos
- ❌ Ignorar los ejercicios
- ❌ Rendirte ante los errores

## 🎯 Establece tus Objetivos

Tómate 5 minutos para responder:

1. **¿Por qué quiero aprender sobre agentes con IA?**
   - _Tu respuesta: ..._

2. **¿Qué proyecto personal me gustaría construir?**
   - _Tu respuesta: ..._

3. **¿Cuánto tiempo puedo dedicar semanalmente?**
   - _Tu respuesta: ... horas/semana_

4. **¿Cuál es mi nivel actual?**
   - [ ] Principiante en Python
   - [ ] Intermedio en Python
   - [ ] Avanzado en Python
   - [ ] Nunca he usado Docker
   - [ ] He usado Docker básicamente
   - [ ] Tengo experiencia con Docker

## 📝 Conceptos Clave

### Términos que Usaremos

**Agent (Agente)**: Sistema de software que puede razonar y actuar de forma autónoma.

**Tool (Herramienta)**: Función o servicio que el agente puede usar (ej. API del clima).

**Prompt**: Instrucciones en lenguaje natural para guiar al agente.

**Container (Contenedor)**: Proceso aislado que ejecuta tu aplicación.

**Image (Imagen)**: Template para crear contenedores (como una receta).

**Dockerfile**: Archivo que define cómo construir una imagen.

**docker-compose**: Herramienta para orquestar múltiples contenedores.

**FastAPI**: Framework moderno de Python para crear APIs.

**uvicorn**: Servidor ASGI para ejecutar aplicaciones FastAPI.

## 🔄 Flujo de Trabajo Típico

```bash
# 1. Escribir código
vim agent.py

# 2. Probar localmente
python agent.py

# 3. Crear Dockerfile
vim Dockerfile

# 4. Construir imagen
docker build -t my-agent:v1 .

# 5. Ejecutar contenedor
docker run -p 8000:8000 my-agent:v1

# 6. Probar API
curl http://localhost:8000/health

# 7. Ver logs
docker logs <container-id>

# 8. Iterar y mejorar
```

## 📚 Recursos Complementarios

- [Docker Official Docs](https://docs.docker.com/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Python Official Docs](https://docs.python.org/3/)
- [OpenAI Cookbook](https://cookbook.openai.com/)

## ✅ Checklist de Preparación

Antes de continuar al Módulo 02, asegúrate de:

- [ ] Haber leído este README completo
- [ ] Entender qué es un agente con IA
- [ ] Entender qué es Docker y por qué lo usamos
- [ ] Haber establecido tus objetivos personales
- [ ] Estar motivado para comenzar a programar
- [ ] Tener tiempo dedicado para el curso

## 🎬 Próximos Pasos

1. Completa la actividad interactiva (`actividad-interactiva.md`)
2. Registra tus aprendizajes en `retroalimentacion.md`
3. Marca tu progreso en `progreso.md`
4. Continúa al **Módulo 02: Prerrequisitos y Entorno**

---

**¡Estás listo para empezar tu viaje! 🚀**

Recuerda: El mejor momento para empezar es AHORA. No esperes a tener todas las respuestas, aprendes haciendo.
