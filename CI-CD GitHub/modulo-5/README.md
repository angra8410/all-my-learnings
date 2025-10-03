# Módulo 5: Artifacts y Gestión de Deployments

## Introducción

Bienvenido al módulo sobre artifacts y deployments. En este módulo aprenderás:

- Qué son los artifacts
- Subir y descargar artifacts
- Gestión de releases
- Deployment strategies
- Environments en GitHub Actions

## ¿Por qué es importante?

Los artifacts permiten compartir resultados del build entre jobs y preservar outputs importantes. Los deployments bien gestionados aseguran entregas confiables y reversibles.

## Conceptos Principales

### 1. ¿Qué son los Artifacts?

Los **artifacts** son archivos generados durante el workflow que quieres preservar:
- Builds compilados (binarios, JARs, etc.)
- Reportes de tests
- Logs
- Screenshots de tests E2E
- Documentación generada

### 2. Subir Artifacts

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Build
        run: npm run build
      
      - name: Upload build artifacts
        uses: actions/upload-artifact@v3
        with:
          name: production-files
          path: |
            dist/
            public/
          retention-days: 7
```

**Opciones importantes:**
- `name`: Nombre del artifact
- `path`: Archivos/directorios a subir
- `retention-days`: Cuántos días mantener (máx 90)
- `if-no-files-found`: error/warn/ignore

### 3. Descargar Artifacts

```yaml
jobs:
  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Download build
        uses: actions/download-artifact@v3
        with:
          name: production-files
          path: dist/
      
      - name: Deploy
        run: |
          echo "Deploying files from dist/"
          ls -la dist/
```

### 4. Environments

Los **environments** permiten configurar reglas y secretos específicos por entorno:

```yaml
jobs:
  deploy-staging:
    runs-on: ubuntu-latest
    environment:
      name: staging
      url: https://staging.example.com
    steps:
      - name: Deploy to staging
        run: echo "Deploying to staging"
  
  deploy-production:
    needs: deploy-staging
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://example.com
    steps:
      - name: Deploy to production
        run: echo "Deploying to production"
```

**Características de Environments:**
- Protection rules (aprobaciones requeridas)
- Secretos específicos por environment
- Deployment history
- URLs de deployment

### 5. Deployment Strategies

**Blue-Green Deployment:**
```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to green
        run: ./deploy.sh green
      
      - name: Run smoke tests
        run: ./smoke-tests.sh green
      
      - name: Switch traffic
        run: ./switch-traffic.sh green
      
      - name: Keep blue as backup
        run: echo "Blue environment still running as backup"
```

**Canary Deployment:**
```yaml
- name: Deploy canary (10%)
  run: ./deploy-canary.sh 10
  
- name: Monitor metrics
  run: ./monitor.sh --duration 300
  
- name: Deploy full (100%)
  if: success()
  run: ./deploy-full.sh
```

**Rolling Deployment:**
```yaml
strategy:
  matrix:
    server: [server1, server2, server3, server4]
  max-parallel: 2
steps:
  - name: Deploy to ${{ matrix.server }}
    run: ./deploy.sh ${{ matrix.server }}
```

### 6. Releases Automáticos

```yaml
name: Create Release

on:
  push:
    tags:
      - 'v*'

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Build
        run: npm run build
      
      - name: Create Release
        uses: actions/create-release@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          tag_name: ${{ github.ref }}
          release_name: Release ${{ github.ref }}
          draft: false
          prerelease: false
      
      - name: Upload Release Asset
        uses: actions/upload-release-asset@v1
        with:
          upload_url: ${{ steps.create_release.outputs.upload_url }}
          asset_path: ./dist/app.zip
          asset_name: app.zip
          asset_content_type: application/zip
```

## Implementación Práctica

### Ejemplo Completo: Build → Test → Deploy

```yaml
name: Build, Test & Deploy

on:
  push:
    branches: [main]
  pull_request:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Build
        run: npm run build
      
      - name: Upload build artifact
        uses: actions/upload-artifact@v3
        with:
          name: build-${{ github.sha }}
          path: dist/
          retention-days: 30
  
  test:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Download build
        uses: actions/download-artifact@v3
        with:
          name: build-${{ github.sha }}
          path: dist/
      
      - name: Run tests
        run: npm test
  
  deploy-staging:
    needs: test
    if: github.event_name == 'push' && github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    environment:
      name: staging
      url: https://staging.example.com
    steps:
      - name: Download build
        uses: actions/download-artifact@v3
        with:
          name: build-${{ github.sha }}
          path: dist/
      
      - name: Deploy to staging
        run: |
          echo "Deploying to staging..."
          # aws s3 sync dist/ s3://staging-bucket/
  
  deploy-production:
    needs: deploy-staging
    runs-on: ubuntu-latest
    environment:
      name: production
      url: https://example.com
    steps:
      - name: Download build
        uses: actions/download-artifact@v3
        with:
          name: build-${{ github.sha }}
          path: dist/
      
      - name: Deploy to production
        run: |
          echo "Deploying to production..."
          # aws s3 sync dist/ s3://production-bucket/
```

## Mejores Prácticas

1. **Nomina artifacts con versión/SHA**: `build-${{ github.sha }}`
2. **Define retention apropiado**: No desperdicies espacio
3. **Usa environments para proteger producción**: Requiere aprobaciones
4. **Implementa health checks**: Verifica deployment antes de continuar
5. **Ten un plan de rollback**: Siempre poder volver atrás

## Conceptos clave para recordar

- 🔑 **Artifact**: Archivo generado que quieres preservar
- 🔑 **Environment**: Configuración de deployment (staging, prod)
- 🔑 **Protection Rules**: Reglas de aprobación para environments
- 🔑 **Deployment Strategy**: Método para desplegar (blue-green, canary, rolling)
- 🔑 **Release**: Versión publicada del software
- 🔑 **Rollback**: Volver a una versión anterior

## Próximos pasos

En el siguiente módulo profundizaremos en environments y secrets, aprendiendo a manejar información sensible de forma segura.

¡Sigue aprendiendo! 🚀
