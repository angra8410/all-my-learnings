# Módulo 10: Best Practices, Security y Optimización

## Introducción

Bienvenido al módulo final sobre best practices y security. En este módulo aprenderás:

- Security best practices
- Optimización de workflows
- Caching strategies
- Secrets management avanzado
- Code scanning y vulnerability detection
- Performance tuning

## ¿Por qué es importante?

Workflows seguros y optimizados son esenciales para producción. Un workflow lento o inseguro puede comprometer todo tu proyecto.

## Conceptos Principales

### 1. Security Best Practices

**Principio de mínimo privilegio:**
```yaml
permissions:
  contents: read
  pull-requests: write
  issues: write
  # Solo los permisos necesarios
```

**Usar SHA en lugar de tags:**
```yaml
# Menos seguro
- uses: actions/checkout@v3

# Más seguro (inmutable)
- uses: actions/checkout@8e5e7e5ab8b370d6c329ec480221332ada57f0ab
```

**Validar inputs:**
```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Validate environment
        if: github.event.inputs.environment != 'production' && github.event.inputs.environment != 'staging'
        run: |
          echo "Invalid environment"
          exit 1
```

### 2. Dependabot para GitHub Actions

**Configurar .github/dependabot.yml:**
```yaml
version: 2
updates:
  - package-ecosystem: "github-actions"
    directory: "/"
    schedule:
      interval: "weekly"
    open-pull-requests-limit: 10
```

### 3. Code Scanning

**CodeQL Analysis:**
```yaml
name: CodeQL

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  schedule:
    - cron: '0 0 * * 1'  # Weekly

jobs:
  analyze:
    runs-on: ubuntu-latest
    permissions:
      security-events: write
      actions: read
      contents: read
    
    strategy:
      matrix:
        language: ['javascript', 'python']
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Initialize CodeQL
        uses: github/codeql-action/init@v2
        with:
          languages: ${{ matrix.language }}
      
      - name: Autobuild
        uses: github/codeql-action/autobuild@v2
      
      - name: Perform CodeQL Analysis
        uses: github/codeql-action/analyze@v2
```

### 4. Secret Scanning

**Habilitar secret scanning:**
```yaml
# En Settings → Code security and analysis
# Habilitar:
# - Secret scanning
# - Push protection
```

**Prevenir commits de secrets:**
```yaml
name: Prevent Secrets

on: [push, pull_request]

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          fetch-depth: 0
      
      - name: Gitleaks scan
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### 5. Caching para Optimización

**Cache de dependencias:**
```yaml
- name: Cache Node modules
  uses: actions/cache@v3
  with:
    path: ~/.npm
    key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
    restore-keys: |
      ${{ runner.os }}-node-
```

**Cache de build:**
```yaml
- name: Cache build
  uses: actions/cache@v3
  with:
    path: dist
    key: ${{ runner.os }}-build-${{ github.sha }}
```

**Cache multi-nivel:**
```yaml
- uses: actions/cache@v3
  with:
    path: |
      ~/.npm
      ~/.cache
      node_modules
    key: ${{ runner.os }}-${{ hashFiles('**/package-lock.json') }}
```

### 6. Optimización de Workflows

**Ejecutar jobs solo cuando sea necesario:**
```yaml
on:
  pull_request:
    paths:
      - 'src/**'
      - 'package.json'
      - '.github/workflows/**'
```

**Fail fast en tests:**
```yaml
jobs:
  test:
    strategy:
      fail-fast: true  # Detener si uno falla
      matrix:
        version: [14, 16, 18]
```

**Concurrency control:**
```yaml
concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true  # Cancelar runs previos
```

### 7. Reusable Workflows

**Workflow reutilizable:**
```yaml
# .github/workflows/reusable-deploy.yml
name: Reusable Deploy

on:
  workflow_call:
    inputs:
      environment:
        required: true
        type: string
    secrets:
      deploy-token:
        required: true

jobs:
  deploy:
    runs-on: ubuntu-latest
    environment: ${{ inputs.environment }}
    steps:
      - uses: actions/checkout@v3
      - name: Deploy
        env:
          TOKEN: ${{ secrets.deploy-token }}
        run: ./deploy.sh ${{ inputs.environment }}
```

**Llamar workflow:**
```yaml
jobs:
  deploy-staging:
    uses: ./.github/workflows/reusable-deploy.yml
    with:
      environment: staging
    secrets:
      deploy-token: ${{ secrets.STAGING_TOKEN }}
```

### 8. OIDC para Autenticación

**Usar OIDC en lugar de long-lived tokens:**
```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      id-token: write
      contents: read
    steps:
      - uses: aws-actions/configure-aws-credentials@v2
        with:
          role-to-assume: arn:aws:iam::123456789:role/GitHubActionsRole
          aws-region: us-east-1
      
      - name: Deploy to AWS
        run: aws s3 sync dist/ s3://my-bucket/
```

## Implementación Práctica

### Ejemplo 1: Workflow Seguro y Optimizado

```yaml
name: Secure Production Deploy

on:
  push:
    branches: [main]
    paths:
      - 'src/**'
      - 'package.json'

concurrency:
  group: production-deploy
  cancel-in-progress: false  # No cancelar deploys en curso

permissions:
  contents: read
  id-token: write

jobs:
  security-scan:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@8e5e7e5ab8b370d6c329ec480221332ada57f0ab
      
      - name: Run Trivy vulnerability scanner
        uses: aquasecurity/trivy-action@master
        with:
          scan-type: 'fs'
          scan-ref: '.'
          severity: 'CRITICAL,HIGH'
      
      - name: Scan for secrets
        uses: gitleaks/gitleaks-action@v2
  
  build:
    needs: security-scan
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@8e5e7e5ab8b370d6c329ec480221332ada57f0ab
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Cache dependencies
        uses: actions/cache@v3
        with:
          path: ~/.npm
          key: ${{ runner.os }}-node-${{ hashFiles('**/package-lock.json') }}
          restore-keys: ${{ runner.os }}-node-
      
      - name: Install dependencies
        run: npm ci
      
      - name: Build
        run: npm run build
      
      - name: Upload artifact
        uses: actions/upload-artifact@v3
        with:
          name: dist
          path: dist/
          retention-days: 7
  
  deploy:
    needs: build
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://myapp.com
    steps:
      - uses: actions/download-artifact@v3
        with:
          name: dist
      
      - name: Configure AWS credentials (OIDC)
        uses: aws-actions/configure-aws-credentials@v2
        with:
          role-to-assume: ${{ secrets.AWS_ROLE_ARN }}
          aws-region: us-east-1
      
      - name: Deploy to S3
        run: |
          aws s3 sync . s3://${{ vars.PRODUCTION_BUCKET }}/ \
            --delete \
            --cache-control "public, max-age=31536000, immutable"
      
      - name: Invalidate CloudFront
        run: |
          aws cloudfront create-invalidation \
            --distribution-id ${{ secrets.CLOUDFRONT_ID }} \
            --paths "/*"
      
      - name: Health check
        run: |
          for i in {1..30}; do
            if curl -f https://myapp.com/health; then
              echo "Health check passed"
              exit 0
            fi
            echo "Waiting for deployment..."
            sleep 10
          done
          exit 1
```

### Ejemplo 2: Monorepo Optimizado

```yaml
name: Monorepo CI

on:
  pull_request:
    paths:
      - 'packages/**'

concurrency:
  group: ${{ github.workflow }}-${{ github.ref }}
  cancel-in-progress: true

jobs:
  changes:
    runs-on: ubuntu-latest
    outputs:
      packages: ${{ steps.filter.outputs.changes }}
    steps:
      - uses: actions/checkout@v3
      
      - uses: dorny/paths-filter@v2
        id: filter
        with:
          filters: |
            package1:
              - 'packages/package1/**'
            package2:
              - 'packages/package2/**'
            package3:
              - 'packages/package3/**'
  
  test:
    needs: changes
    if: needs.changes.outputs.packages != '[]'
    runs-on: ubuntu-latest
    strategy:
      matrix:
        package: ${{ fromJson(needs.changes.outputs.packages) }}
    steps:
      - uses: actions/checkout@v3
      
      - name: Cache for ${{ matrix.package }}
        uses: actions/cache@v3
        with:
          path: packages/${{ matrix.package }}/node_modules
          key: ${{ runner.os }}-${{ matrix.package }}-${{ hashFiles('packages/${{ matrix.package }}/package-lock.json') }}
      
      - name: Test ${{ matrix.package }}
        working-directory: packages/${{ matrix.package }}
        run: |
          npm ci
          npm test
```

## Mejores Prácticas - Checklist

### Security ✅
- [ ] Usa SHA específicos para actions críticas
- [ ] Configura permisos mínimos necesarios
- [ ] Habilita Dependabot para GitHub Actions
- [ ] Implementa secret scanning
- [ ] Usa OIDC en lugar de long-lived tokens
- [ ] Nunca hagas log de secrets
- [ ] Valida todos los inputs de usuario

### Performance ✅
- [ ] Usa caching apropiadamente
- [ ] Ejecuta solo los jobs necesarios (paths filter)
- [ ] Implementa concurrency control
- [ ] Usa fail-fast cuando sea apropiado
- [ ] Paraleliza tests
- [ ] Optimiza tamaño de artifacts

### Maintainability ✅
- [ ] Usa reusable workflows
- [ ] Documenta workflows complejos
- [ ] Nombra steps descriptivamente
- [ ] Agrupa logs relacionados
- [ ] Implementa health checks
- [ ] Mantén workflows DRY

### Reliability ✅
- [ ] Implementa retry logic
- [ ] Ten plan de rollback
- [ ] Usa environments para producción
- [ ] Configura required reviewers
- [ ] Monitorea y alerta
- [ ] Mantén retention apropiado de artifacts

## Conceptos clave para recordar

- 🔑 **Security**: Permisos mínimos, SHA pins, OIDC
- 🔑 **Caching**: Acelera workflows significativamente
- 🔑 **Concurrency**: Controla ejecuciones paralelas
- 🔑 **Code Scanning**: Detecta vulnerabilidades
- 🔑 **Dependabot**: Actualiza dependencias automáticamente
- 🔑 **Reusable Workflows**: DRY principle
- 🔑 **OIDC**: Autenticación sin long-lived tokens

## Próximos pasos

¡Felicitaciones! Has completado el curso de CI/CD con GitHub Actions. Ahora estás listo para:

1. Implementar CI/CD en tus proyectos
2. Optimizar workflows existentes
3. Contribuir a la comunidad creando actions
4. Explorar casos de uso avanzados

## Recursos Adicionales

- GitHub Actions Documentation
- GitHub Security Best Practices
- Awesome GitHub Actions (curated list)
- GitHub Actions Community Forum

¡Excelente trabajo completando el curso! 🎉🚀
