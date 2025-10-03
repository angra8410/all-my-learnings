# Módulo 8: GitHub Actions Marketplace y Custom Actions

## Introducción

Bienvenido al módulo sobre el Marketplace y custom actions. En este módulo aprenderás:

- Explorar el GitHub Actions Marketplace
- Usar actions de terceros
- Crear tus propias actions
- Tipos de actions (JavaScript, Docker, Composite)
- Publicar actions en el Marketplace

## ¿Por qué es importante?

El Marketplace ofrece miles de actions reutilizables que aceleran el desarrollo. Crear custom actions permite encapsular lógica común y compartirla entre proyectos.

## Conceptos Principales

### 1. GitHub Actions Marketplace

**Explorar el Marketplace:**
- https://github.com/marketplace?type=actions
- Categorías: CI, Deployment, Code Quality, etc.
- Verificar popularidad, mantenimiento y reviews

**Actions populares:**
```yaml
# Checkout código
- uses: actions/checkout@v3

# Setup lenguajes
- uses: actions/setup-node@v3
- uses: actions/setup-python@v4
- uses: actions/setup-java@v3

# Testing
- uses: codecov/codecov-action@v3
- uses: cypress-io/github-action@v5

# Deployment
- uses: aws-actions/configure-aws-credentials@v2
- uses: azure/webapps-deploy@v2

# Utilidades
- uses: actions/cache@v3
- uses: github/super-linter@v5
```

### 2. Versioning de Actions

**Formas de especificar versión:**

```yaml
# Por tag específico (recomendado)
- uses: actions/checkout@v3

# Por SHA específico (más seguro)
- uses: actions/checkout@8e5e7e5ab8b370d6c329ec480221332ada57f0ab

# Por rama (no recomendado para producción)
- uses: actions/checkout@main

# Por versión semántica exacta
- uses: actions/checkout@v3.5.2
```

### 3. Tipos de Custom Actions

**1. JavaScript Actions:**
```yaml
# action.yml
name: 'My JavaScript Action'
description: 'Does something cool'
inputs:
  who-to-greet:
    description: 'Who to greet'
    required: true
    default: 'World'
outputs:
  time:
    description: 'The time we greeted you'
runs:
  using: 'node16'
  main: 'index.js'
```

**2. Docker Container Actions:**
```yaml
# action.yml
name: 'My Docker Action'
description: 'Runs in Docker'
runs:
  using: 'docker'
  image: 'Dockerfile'
  args:
    - ${{ inputs.myInput }}
```

**3. Composite Actions:**
```yaml
# action.yml
name: 'My Composite Action'
description: 'Runs multiple steps'
runs:
  using: 'composite'
  steps:
    - run: echo "Step 1"
      shell: bash
    - run: echo "Step 2"
      shell: bash
```

### 4. Crear una JavaScript Action

**Estructura del proyecto:**
```
my-action/
├── action.yml
├── index.js
├── package.json
└── README.md
```

**action.yml:**
```yaml
name: 'Hello World'
description: 'Greet someone'
inputs:
  who-to-greet:
    description: 'Who to greet'
    required: true
    default: 'World'
outputs:
  time:
    description: 'The greeting time'
runs:
  using: 'node16'
  main: 'index.js'
```

**index.js:**
```javascript
const core = require('@actions/core');
const github = require('@actions/github');

try {
  const nameToGreet = core.getInput('who-to-greet');
  console.log(`Hello ${nameToGreet}!`);
  
  const time = (new Date()).toTimeString();
  core.setOutput('time', time);
  
  // Access the GitHub context
  const payload = JSON.stringify(github.context.payload, null, 2);
  console.log(`Event payload: ${payload}`);
} catch (error) {
  core.setFailed(error.message);
}
```

**package.json:**
```json
{
  "name": "hello-world-action",
  "version": "1.0.0",
  "main": "index.js",
  "dependencies": {
    "@actions/core": "^1.10.0",
    "@actions/github": "^5.1.1"
  }
}
```

### 5. Crear una Composite Action

```yaml
# action.yml
name: 'Setup Node and Install'
description: 'Setup Node.js and install dependencies'
inputs:
  node-version:
    description: 'Node version'
    required: false
    default: '18'
runs:
  using: 'composite'
  steps:
    - name: Setup Node.js
      uses: actions/setup-node@v3
      with:
        node-version: ${{ inputs.node-version }}
    
    - name: Cache dependencies
      uses: actions/cache@v3
      with:
        path: ~/.npm
        key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
    
    - name: Install dependencies
      run: npm ci
      shell: bash
    
    - name: Show versions
      run: |
        node --version
        npm --version
      shell: bash
```

**Usar la composite action:**
```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: ./path/to/my-composite-action
        with:
          node-version: '20'
      - run: npm test
```

### 6. Usar Actions de Terceros

**Ejemplo: Deploy a AWS S3**
```yaml
- name: Configure AWS credentials
  uses: aws-actions/configure-aws-credentials@v2
  with:
    aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
    aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
    aws-region: us-east-1

- name: Deploy to S3
  uses: reggionick/s3-deploy@v3
  with:
    folder: dist
    bucket: my-bucket
    bucket-region: us-east-1
```

**Ejemplo: Slack Notifications**
```yaml
- name: Notify Slack
  uses: slackapi/slack-github-action@v1
  with:
    payload: |
      {
        "text": "Build ${{ job.status }}: ${{ github.event.head_commit.message }}"
      }
  env:
    SLACK_WEBHOOK_URL: ${{ secrets.SLACK_WEBHOOK }}
```

## Implementación Práctica

### Ejemplo 1: Custom Action para Deploy

**my-deploy-action/action.yml:**
```yaml
name: 'Deploy Application'
description: 'Deploy to specified environment'
inputs:
  environment:
    description: 'Target environment'
    required: true
  build-path:
    description: 'Path to build files'
    required: true
    default: 'dist'
outputs:
  deployment-url:
    description: 'URL of deployment'
    value: ${{ steps.deploy.outputs.url }}
runs:
  using: 'composite'
  steps:
    - name: Validate inputs
      run: |
        echo "Deploying to ${{ inputs.environment }}"
        echo "From path: ${{ inputs.build-path }}"
      shell: bash
    
    - name: Deploy
      id: deploy
      run: |
        # Deploy logic here
        URL="https://${{ inputs.environment }}.example.com"
        echo "url=$URL" >> $GITHUB_OUTPUT
      shell: bash
    
    - name: Health check
      run: |
        curl -f ${{ steps.deploy.outputs.url }}/health || exit 1
      shell: bash
```

**Usar en workflow:**
```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: ./.github/actions/my-deploy-action
        with:
          environment: production
          build-path: dist
```

### Ejemplo 2: Reusable Workflows

```yaml
# .github/workflows/reusable-test.yml
name: Reusable Test Workflow

on:
  workflow_call:
    inputs:
      node-version:
        required: false
        type: string
        default: '18'
    secrets:
      npm-token:
        required: false

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: ${{ inputs.node-version }}
      - run: npm ci
      - run: npm test
```

**Llamar al reusable workflow:**
```yaml
# .github/workflows/ci.yml
name: CI

on: [push]

jobs:
  test-node-16:
    uses: ./.github/workflows/reusable-test.yml
    with:
      node-version: '16'
  
  test-node-18:
    uses: ./.github/workflows/reusable-test.yml
    with:
      node-version: '18'
```

## Mejores Prácticas

1. **Verifica la fuente de actions de terceros**: Repositorios oficiales y verificados
2. **Pin a versiones específicas**: Usa @v3, no @main
3. **Lee la documentación**: Entiende inputs/outputs
4. **Prueba actions localmente**: Con act o herramientas similares
5. **Mantén actions simples**: Una responsabilidad por action
6. **Documenta tus custom actions**: README claro

## Conceptos clave para recordar

- 🔑 **Marketplace**: Repositorio de actions reutilizables
- 🔑 **JavaScript Action**: Action escrita en Node.js
- 🔑 **Docker Action**: Action que corre en contenedor
- 🔑 **Composite Action**: Combina múltiples steps
- 🔑 **Reusable Workflow**: Workflow que puede ser llamado por otros
- 🔑 **Versioning**: Usar tags específicos (@v3)

## Próximos pasos

En el siguiente módulo aprenderás sobre monitoring, logging y debugging de workflows.

¡Sigue aprendiendo! 🚀
