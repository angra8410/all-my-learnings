# Módulo 2: GitHub Actions - Fundamentos

## Introducción

Bienvenido al módulo sobre GitHub Actions. En este módulo aprenderás:

- ¿Qué es GitHub Actions?
- Componentes principales
- Eventos y triggers
- Tu primer workflow
- Actions predefinidas

## ¿Por qué es importante?

GitHub Actions es la plataforma de CI/CD integrada directamente en GitHub. Permite automatizar workflows sin necesidad de servicios externos, simplificando enormemente la configuración y mantenimiento de pipelines.

## Conceptos Principales

### 1. ¿Qué es GitHub Actions?

**GitHub Actions** es una plataforma de automatización que permite ejecutar workflows directamente desde tu repositorio de GitHub. Puedes usarlo para:

- Ejecutar pruebas automáticamente
- Construir y desplegar aplicaciones
- Automatizar tareas de mantenimiento
- Gestionar issues y pull requests
- Y mucho más...

**Analogía**: Si GitHub es tu casa (repositorio), GitHub Actions son los robots domésticos que automatizan tareas como limpiar (tests), cocinar (builds), y organizar (deployment).

### 2. Componentes Principales

```
┌─────────────────────────────────────────────────────────┐
│                     WORKFLOW                             │
│  ┌───────────────────────────────────────────────────┐  │
│  │                    JOB 1                          │  │
│  │  ┌──────────┐  ┌──────────┐  ┌──────────┐       │  │
│  │  │  STEP 1  │→ │  STEP 2  │→ │  STEP 3  │       │  │
│  │  └──────────┘  └──────────┘  └──────────┘       │  │
│  └───────────────────────────────────────────────────┘  │
│                                                          │
│  ┌───────────────────────────────────────────────────┐  │
│  │                    JOB 2                          │  │
│  │  ┌──────────┐  ┌──────────┐                      │  │
│  │  │  STEP 1  │→ │  STEP 2  │                      │  │
│  │  └──────────┘  └──────────┘                      │  │
│  └───────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

**Workflow**: Proceso automatizado completo definido en un archivo YAML  
**Job**: Conjunto de steps que se ejecutan en el mismo runner  
**Step**: Tarea individual (un comando o action)  
**Action**: Comando reutilizable  
**Runner**: Servidor que ejecuta los workflows

### 3. Eventos y Triggers

Los workflows se activan con eventos. Los más comunes:

```yaml
# Se ejecuta cuando haces push
on: push

# Se ejecuta en pull requests
on: pull_request

# Se ejecuta cuando creas un release
on: release

# Múltiples eventos
on: [push, pull_request]

# Evento programado (cron)
on:
  schedule:
    - cron: '0 0 * * *'  # Diariamente a medianoche
```

### 4. Tu Primer Workflow

Creemos un workflow simple que saluda al mundo:

**Archivo**: `.github/workflows/hello-world.yml`

```yaml
name: Hello World

# Ejecutar cuando hay push a main
on:
  push:
    branches: [ main ]

jobs:
  greet:
    runs-on: ubuntu-latest
    
    steps:
      - name: Saludar
        run: echo "¡Hola, Mundo desde GitHub Actions!"
      
      - name: Mostrar fecha
        run: date
      
      - name: Listar archivos
        run: ls -la
```

**Desglose línea por línea:**

1. `name: Hello World` - Nombre del workflow que verás en GitHub
2. `on: push` - Se ejecuta cuando haces push
3. `branches: [ main ]` - Solo en la rama main
4. `jobs:` - Define los trabajos a ejecutar
5. `greet:` - Nombre del job
6. `runs-on: ubuntu-latest` - Sistema operativo del runner
7. `steps:` - Lista de pasos a ejecutar
8. `name:` - Nombre descriptivo del step
9. `run:` - Comando a ejecutar

### 5. Workflow con Checkout

Para trabajar con tu código, necesitas hacer checkout del repositorio:

```yaml
name: Build y Test

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
      # Paso 1: Obtener el código
      - name: Checkout código
        uses: actions/checkout@v3
      
      # Paso 2: Configurar Node.js
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      # Paso 3: Instalar dependencias
      - name: Instalar dependencias
        run: npm install
      
      # Paso 4: Ejecutar tests
      - name: Ejecutar tests
        run: npm test
```

**Conceptos nuevos:**

- `uses:` - Usa una action predefinida
- `actions/checkout@v3` - Action oficial para obtener tu código
- `with:` - Parámetros para la action
- `@v3` - Versión específica de la action

### 6. Actions Predefinidas Comunes

GitHub y la comunidad ofrecen miles de actions reutilizables:

```yaml
# Checkout del código
- uses: actions/checkout@v3

# Setup de diferentes lenguajes
- uses: actions/setup-node@v3      # Node.js
- uses: actions/setup-python@v4    # Python
- uses: actions/setup-java@v3      # Java
- uses: actions/setup-dotnet@v3    # .NET

# Subir artefactos
- uses: actions/upload-artifact@v3
  with:
    name: mi-app
    path: dist/

# Descargar artefactos
- uses: actions/download-artifact@v3
  with:
    name: mi-app
```

## Implementación Práctica

### Ejemplo: Workflow para Node.js

```yaml
name: Node.js CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    strategy:
      matrix:
        node-version: [16.x, 18.x, 20.x]
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Use Node.js ${{ matrix.node-version }}
      uses: actions/setup-node@v3
      with:
        node-version: ${{ matrix.node-version }}
    
    - name: Install dependencies
      run: npm ci
    
    - name: Run tests
      run: npm test
    
    - name: Build
      run: npm run build
```

**Este workflow:**
1. Se ejecuta en push a main/develop y en PRs a main
2. Prueba en 3 versiones de Node.js (16, 18, 20)
3. Instala dependencias
4. Ejecuta tests
5. Hace build del proyecto

### Ejemplo: Workflow para Python

```yaml
name: Python CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    
    - name: Run tests
      run: pytest
    
    - name: Lint
      run: flake8 .
```

## Mejores Prácticas

1. **Nombra tus workflows descriptivamente**: `CI`, `Deploy to Production`, `Run Tests`
2. **Usa versiones específicas de actions**: `@v3` en lugar de `@latest`
3. **Minimiza el uso de runners**: Los minutos tienen límite
4. **Usa caché cuando sea posible**: Acelera las ejecuciones
5. **Falla rápido**: Pon los tests primero para detectar errores pronto

## Estructura de Archivos

Tu repositorio debe tener esta estructura:

```
mi-proyecto/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       ├── deploy.yml
│       └── tests.yml
├── src/
│   └── ...
├── tests/
│   └── ...
└── README.md
```

## Conceptos clave para recordar

- 🔑 **Workflow**: Proceso automatizado definido en YAML
- 🔑 **Job**: Conjunto de steps que se ejecutan juntos
- 🔑 **Step**: Tarea individual en un job
- 🔑 **Action**: Comando reutilizable
- 🔑 **Runner**: Servidor que ejecuta el workflow
- 🔑 **Event**: Trigger que inicia el workflow (push, PR, etc.)
- 🔑 **uses**: Palabra clave para usar actions predefinidas
- 🔑 **run**: Palabra clave para ejecutar comandos shell

## Diagrama: Flujo de Ejecución

```
   GitHub Repository
         │
         │  Event (push/PR/etc.)
         ▼
   GitHub Actions
         │
         ├─→ Trigger Workflow
         │
         ├─→ Iniciar Runner (Ubuntu/Windows/macOS)
         │
         ├─→ Ejecutar Jobs
         │     │
         │     ├─→ Job 1: Setup + Steps
         │     │
         │     └─→ Job 2: Setup + Steps
         │
         ├─→ Reportar Resultados
         │
         └─→ Notificar (✅/❌)
```

## Próximos pasos

En el siguiente módulo profundizaremos en la sintaxis YAML y crearemos workflows más complejos con múltiples jobs, condiciones y estrategias avanzadas.

¡Sigue aprendiendo! 🚀
