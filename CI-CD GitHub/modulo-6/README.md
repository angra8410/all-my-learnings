# Módulo 6: Environments y Secrets

## Introducción

Bienvenido al módulo sobre environments y secrets. En este módulo aprenderás:

- Configurar environments
- Gestionar secrets de forma segura
- Variables de entorno
- Protection rules
- Scoping de secrets

## ¿Por qué es importante?

Los secrets permiten manejar información sensible (API keys, passwords) de forma segura sin exponerla en el código. Los environments organizan tus deployments y aplican reglas de seguridad.

## Conceptos Principales

### 1. GitHub Secrets

Los **secrets** almacenan información sensible de forma encriptada:

**Tipos de secrets:**
- **Repository secrets**: Disponibles para todo el repositorio
- **Environment secrets**: Solo para un environment específico
- **Organization secrets**: Compartidos entre repos de la org

**Crear un secret:**
1. Settings → Secrets and variables → Actions
2. New repository secret
3. Name: `API_KEY`, Value: `tu-api-key-secreta`

**Usar en workflow:**
```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Deploy with API key
        env:
          API_KEY: ${{ secrets.API_KEY }}
        run: |
          echo "API_KEY está disponible pero oculto"
          # El valor nunca se muestra en los logs
```

### 2. Environments

**Crear environment:**
1. Settings → Environments → New environment
2. Nombre: `production`
3. Configurar protection rules

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://myapp.com
    steps:
      - name: Deploy
        env:
          DEPLOY_TOKEN: ${{ secrets.DEPLOY_TOKEN }}
        run: ./deploy.sh
```

### 3. Protection Rules

**Configuraciones de protección:**

**Required reviewers:**
```yaml
# En Settings → Environments → production
# Agregar required reviewers
# El deployment se pausará hasta aprobación
```

**Wait timer:**
```yaml
# Esperar X minutos antes de deployment
# Útil para deployments programados
```

**Deployment branches:**
```yaml
# Solo permitir deployments desde main
# Previene deployments accidentales desde features
```

### 4. Secrets Jerárquicos

```yaml
# Repository secret (disponible en todos los environments)
${{ secrets.GLOBAL_TOKEN }}

# Environment secret (solo en ese environment)
environment: production
env:
  PROD_TOKEN: ${{ secrets.PROD_TOKEN }}  # Solo existe en production
```

**Precedencia:**
1. Environment secrets (más específico)
2. Repository secrets
3. Organization secrets

### 5. Variables vs Secrets

**Variables**: Información no sensible
```yaml
# Crear en Settings → Variables
jobs:
  build:
    runs-on: ubuntu-latest
    env:
      APP_VERSION: ${{ vars.APP_VERSION }}
      ENVIRONMENT: ${{ vars.ENVIRONMENT }}
```

**Secrets**: Información sensible (encriptada)
```yaml
env:
  DATABASE_PASSWORD: ${{ secrets.DB_PASSWORD }}
  API_KEY: ${{ secrets.API_KEY }}
```

### 6. Masked Values

Los secrets se enmascaran automáticamente en logs:

```yaml
steps:
  - name: Test secret masking
    env:
      MY_SECRET: ${{ secrets.MY_SECRET }}
    run: |
      echo "Secret value: $MY_SECRET"
      # Output: Secret value: ***
```

## Implementación Práctica

### Ejemplo: Multi-Environment Deployment

```yaml
name: Multi-Environment Deploy

on:
  push:
    branches: [main, develop]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Build
        run: npm run build
      - uses: actions/upload-artifact@v3
        with:
          name: build
          path: dist/
  
  deploy-dev:
    needs: build
    if: github.ref == 'refs/heads/develop'
    runs-on: ubuntu-latest
    environment:
      name: development
      url: https://dev.example.com
    steps:
      - uses: actions/download-artifact@v3
      - name: Deploy to Dev
        env:
          AWS_ACCESS_KEY: ${{ secrets.AWS_ACCESS_KEY }}
          AWS_SECRET_KEY: ${{ secrets.AWS_SECRET_KEY }}
          BUCKET: ${{ vars.DEV_BUCKET }}
        run: |
          aws s3 sync dist/ s3://$BUCKET/
  
  deploy-staging:
    needs: build
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment:
      name: staging
      url: https://staging.example.com
    steps:
      - uses: actions/download-artifact@v3
      - name: Deploy to Staging
        env:
          AWS_ACCESS_KEY: ${{ secrets.AWS_ACCESS_KEY }}
          AWS_SECRET_KEY: ${{ secrets.AWS_SECRET_KEY }}
          BUCKET: ${{ vars.STAGING_BUCKET }}
        run: |
          aws s3 sync dist/ s3://$BUCKET/
  
  deploy-production:
    needs: deploy-staging
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://example.com
    steps:
      - uses: actions/download-artifact@v3
      
      # Production usa secrets específicos del environment
      - name: Deploy to Production
        env:
          AWS_ACCESS_KEY: ${{ secrets.PROD_AWS_KEY }}
          AWS_SECRET_KEY: ${{ secrets.PROD_AWS_SECRET }}
          BUCKET: ${{ vars.PROD_BUCKET }}
          CLOUDFRONT_ID: ${{ secrets.CLOUDFRONT_ID }}
        run: |
          aws s3 sync dist/ s3://$BUCKET/
          aws cloudfront create-invalidation --distribution-id $CLOUDFRONT_ID --paths "/*"
```

### Ejemplo: Secrets en Docker Build

```yaml
- name: Build Docker image
  env:
    DOCKER_USERNAME: ${{ secrets.DOCKER_USERNAME }}
    DOCKER_PASSWORD: ${{ secrets.DOCKER_PASSWORD }}
  run: |
    echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin
    docker build -t myapp:latest .
    docker push myapp:latest
```

### Ejemplo: Rotating Secrets

```yaml
name: Rotate API Keys

on:
  schedule:
    - cron: '0 0 1 * *'  # Primer día de cada mes

jobs:
  rotate:
    runs-on: ubuntu-latest
    steps:
      - name: Generate new key
        id: newkey
        run: |
          NEW_KEY=$(openssl rand -base64 32)
          echo "::add-mask::$NEW_KEY"
          echo "key=$NEW_KEY" >> $GITHUB_OUTPUT
      
      - name: Update service
        env:
          OLD_KEY: ${{ secrets.API_KEY }}
          NEW_KEY: ${{ steps.newkey.outputs.key }}
        run: |
          # Actualizar el servicio con la nueva key
          curl -X POST https://api.service.com/rotate \
            -H "Authorization: Bearer $OLD_KEY" \
            -d "new_key=$NEW_KEY"
      
      # Luego actualizar el secret en GitHub manualmente
      # o usar GitHub CLI con un token de admin
```

## Mejores Prácticas

1. **Nunca commits secrets en código**: Usa siempre GitHub Secrets
2. **Usa environment secrets para producción**: Mayor control y seguridad
3. **Rota secrets periódicamente**: Cambia claves regularmente
4. **Principio de mínimo privilegio**: Solo da acceso necesario
5. **Usa required reviewers en producción**: Aprobaciones obligatorias
6. **Documenta qué secrets se necesitan**: En el README del proyecto

## Conceptos clave para recordar

- 🔑 **Secret**: Valor encriptado y enmascarado en logs
- 🔑 **Variable**: Valor de configuración no sensible
- 🔑 **Environment**: Contexto de deployment con sus propios secrets
- 🔑 **Protection Rules**: Reglas que controlan deployments
- 🔑 **Required Reviewers**: Aprobación humana requerida
- 🔑 **Masking**: Ocultación automática de secrets en logs

## Próximos pasos

En el siguiente módulo aprenderás sobre matrix strategies para ejecutar jobs en múltiples configuraciones paralelas.

¡Sigue aprendiendo! 🚀
