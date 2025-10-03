# Módulo 3: Workflows y Sintaxis YAML Avanzada

## Introducción

Bienvenido al módulo sobre workflows avanzados y YAML. En este módulo aprenderás:

- Sintaxis YAML en profundidad
- Jobs dependientes y paralelos
- Condicionales en workflows
- Expresiones y contextos
- Reutilización de workflows

## ¿Por qué es importante?

Dominar YAML y las características avanzadas de workflows te permite crear pipelines complejos, eficientes y mantenibles que se adaptan a diferentes escenarios.

## Conceptos Principales

### 1. Sintaxis YAML Avanzada

**YAML (YAML Ain't Markup Language)** es un formato de serialización de datos legible por humanos.

**Conceptos clave:**

```yaml
# Comentarios con #
name: "String con comillas"
number: 42
boolean: true
lista:
  - item1
  - item2
  - item3
  
objeto:
  clave1: valor1
  clave2: valor2

# String multi-línea
descripcion: |
  Esta es una línea
  Esta es otra línea
  
# String en una línea
oneline: >
  Todo esto
  será una
  sola línea
```

### 2. Jobs Dependientes

Los jobs se ejecutan en paralelo por defecto. Para hacerlos secuenciales, usa `needs`:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Building..."
  
  test:
    needs: build  # Espera a que build termine
    runs-on: ubuntu-latest
    steps:
      - run: echo "Testing..."
  
  deploy:
    needs: [build, test]  # Espera a ambos
    runs-on: ubuntu-latest
    steps:
      - run: echo "Deploying..."
```

**Diagrama de flujo:**
```
    build
      ↓
    test
      ↓
    deploy
```

### 3. Jobs Paralelos vs Secuenciales

**Paralelos (por defecto):**
```yaml
jobs:
  job1:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Job 1"
  
  job2:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Job 2"
```

Ambos jobs se ejecutan simultáneamente.

**Secuenciales (con needs):**
```yaml
jobs:
  job1:
    runs-on: ubuntu-latest
    steps:
      - run: echo "Job 1"
  
  job2:
    needs: job1
    runs-on: ubuntu-latest
    steps:
      - run: echo "Job 2"
```

Job2 espera a que job1 termine.

### 4. Condicionales (if)

Ejecuta steps o jobs solo bajo ciertas condiciones:

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    # Solo en la rama main
    if: github.ref == 'refs/heads/main'
    steps:
      - run: echo "Deploying to production"
  
  notify:
    runs-on: ubuntu-latest
    steps:
      - name: Notify on failure
        if: failure()
        run: echo "Build failed!"
      
      - name: Notify on success
        if: success()
        run: echo "Build succeeded!"
```

**Funciones útiles:**
- `success()` - El step anterior tuvo éxito
- `failure()` - El step anterior falló
- `always()` - Siempre ejecutar
- `cancelled()` - El workflow fue cancelado

### 5. Expresiones y Contextos

**Expresiones** usan la sintaxis `${{ }}`:

```yaml
steps:
  - name: Print branch
    run: echo "Branch: ${{ github.ref }}"
  
  - name: Conditional step
    if: ${{ github.event_name == 'push' }}
    run: echo "This was a push event"
```

**Contextos comunes:**

```yaml
# github context
${{ github.repository }}      # nombre del repo
${{ github.actor }}           # usuario que triggereó
${{ github.event_name }}      # tipo de evento
${{ github.ref }}             # referencia git
${{ github.sha }}             # commit SHA

# env context
${{ env.MY_VAR }}

# secrets context
${{ secrets.API_KEY }}

# runner context
${{ runner.os }}              # Sistema operativo
${{ runner.temp }}            # Directorio temporal
```

### 6. Variables de Entorno

**Definir variables:**

```yaml
env:
  NODE_VERSION: '18'
  DATABASE_URL: 'postgresql://localhost'

jobs:
  build:
    runs-on: ubuntu-latest
    env:
      BUILD_ENV: 'production'
    
    steps:
      - name: Use env vars
        run: |
          echo "Node version: $NODE_VERSION"
          echo "Build env: $BUILD_ENV"
      
      - name: Set step-level env
        env:
          STEP_VAR: 'value'
        run: echo $STEP_VAR
```

**Niveles de scope:**
1. Workflow level (disponible en todos los jobs)
2. Job level (disponible en todos los steps del job)
3. Step level (solo en ese step)

### 7. Outputs entre Jobs

Pasar datos de un job a otro:

```yaml
jobs:
  job1:
    runs-on: ubuntu-latest
    outputs:
      version: ${{ steps.get_version.outputs.version }}
    
    steps:
      - name: Get version
        id: get_version
        run: echo "version=1.2.3" >> $GITHUB_OUTPUT
  
  job2:
    needs: job1
    runs-on: ubuntu-latest
    steps:
      - name: Use version
        run: echo "Version is ${{ needs.job1.outputs.version }}"
```

### 8. Estrategia Matrix

Ejecutar el mismo job con diferentes configuraciones:

```yaml
jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        node: [16, 18, 20]
        include:
          - os: ubuntu-latest
            experimental: true
    
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: ${{ matrix.node }}
      - run: npm test
```

Esto crea 9 jobs (3 OS × 3 versiones de Node).

**Opciones de strategy:**
- `fail-fast: false` - Continuar si un job falla
- `max-parallel: 2` - Limitar jobs paralelos

## Implementación Práctica

### Ejemplo Completo: Pipeline de Deployment

```yaml
name: Build, Test, Deploy

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

env:
  NODE_VERSION: '18'

jobs:
  build:
    runs-on: ubuntu-latest
    outputs:
      version: ${{ steps.package.outputs.version }}
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node
        uses: actions/setup-node@v3
        with:
          node-version: ${{ env.NODE_VERSION }}
      
      - name: Install dependencies
        run: npm ci
      
      - name: Build
        run: npm run build
      
      - name: Get package version
        id: package
        run: echo "version=$(node -p "require('./package.json').version")" >> $GITHUB_OUTPUT
      
      - name: Upload build artifact
        uses: actions/upload-artifact@v3
        with:
          name: dist-${{ steps.package.outputs.version }}
          path: dist/
  
  test:
    needs: build
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
        node: [16, 18]
    
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: ${{ matrix.node }}
      - run: npm ci
      - run: npm test
  
  deploy:
    needs: [build, test]
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
      - name: Download artifact
        uses: actions/download-artifact@v3
        with:
          name: dist-${{ needs.build.outputs.version }}
      
      - name: Deploy
        run: echo "Deploying version ${{ needs.build.outputs.version }}"
```

## Mejores Prácticas

1. **Usa needs para crear dependencias claras**
2. **Aprovecha matrix para probar múltiples configuraciones**
3. **Define variables de entorno al nivel apropiado**
4. **Usa condicionales para optimizar ejecuciones**
5. **Documenta workflows complejos con comentarios**

## Conceptos clave para recordar

- 🔑 **needs**: Define dependencias entre jobs
- 🔑 **if**: Condicionales para steps y jobs
- 🔑 **strategy.matrix**: Ejecutar con múltiples configuraciones
- 🔑 **outputs**: Pasar datos entre jobs
- 🔑 **env**: Variables de entorno
- 🔑 **contexts**: Datos disponibles (${{ github }}, ${{ env }}, etc.)
- 🔑 **expressions**: Sintaxis ${{ }}

## Próximos pasos

En el siguiente módulo aprenderás sobre testing automatizado y cómo integrar diferentes frameworks de pruebas en tus workflows.

¡Sigue aprendiendo! 🚀
