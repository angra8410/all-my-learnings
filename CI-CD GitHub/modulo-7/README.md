# Módulo 7: Matrix Strategies y Jobs Paralelos

## Introducción

Bienvenido al módulo sobre matrix strategies. En este módulo aprenderás:

- Strategy matrix en detalle
- Jobs paralelos eficientes
- Configuraciones dinámicas
- Fail-fast y continue-on-error
- Optimización de pipelines

## ¿Por qué es importante?

Las matrix strategies permiten probar tu código en múltiples configuraciones simultáneamente, ahorrando tiempo y asegurando compatibilidad amplia.

## Conceptos Principales

### 1. Matrix Básico

```yaml
jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        node: [16, 18, 20]
    
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: ${{ matrix.node }}
      - run: npm test
```

Esto crea **9 jobs** (3 OS × 3 versiones de Node).

### 2. Matrix con Include

Agregar configuraciones específicas:

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest]
    node: [16, 18]
    include:
      # Configuración adicional específica
      - os: ubuntu-latest
        node: 20
        experimental: true
      - os: macos-latest
        node: 18
```

### 3. Matrix con Exclude

Omitir ciertas combinaciones:

```yaml
strategy:
  matrix:
    os: [ubuntu-latest, windows-latest, macos-latest]
    node: [16, 18, 20]
    exclude:
      # No probar Node 16 en Windows
      - os: windows-latest
        node: 16
      # No probar Node 20 en macOS
      - os: macos-latest
        node: 20
```

### 4. Fail-Fast

Comportamiento cuando un job falla:

```yaml
strategy:
  # Por defecto: true (cancela todos si uno falla)
  fail-fast: false  # Continuar aunque fallen algunos
  matrix:
    version: [1, 2, 3, 4, 5]
```

**fail-fast: true** (default):
```
Job 1: ✅
Job 2: ❌ → Cancela Jobs 3, 4, 5
```

**fail-fast: false**:
```
Job 1: ✅
Job 2: ❌
Job 3: ✅
Job 4: ✅
Job 5: ❌
```

### 5. Max-Parallel

Controlar cuántos jobs se ejecutan simultáneamente:

```yaml
strategy:
  max-parallel: 2
  matrix:
    test: [1, 2, 3, 4, 5, 6]
```

Útil para:
- Limitar uso de recursos compartidos
- Respetar rate limits de APIs
- Reducir costos de runners concurrentes

### 6. Matrix Dinámico desde JSON

```yaml
jobs:
  prepare:
    runs-on: ubuntu-latest
    outputs:
      matrix: ${{ steps.set-matrix.outputs.matrix }}
    steps:
      - id: set-matrix
        run: |
          echo 'matrix={\"version\":[\"16\",\"18\",\"20\"]}' >> $GITHUB_OUTPUT
  
  test:
    needs: prepare
    strategy:
      matrix: ${{ fromJson(needs.prepare.outputs.matrix) }}
    runs-on: ubuntu-latest
    steps:
      - uses: actions/setup-node@v3
        with:
          node-version: ${{ matrix.version }}
      - run: npm test
```

### 7. Jobs Paralelos sin Matrix

Ejecutar trabajos diferentes simultáneamente:

```yaml
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - run: npm run lint
  
  test-unit:
    runs-on: ubuntu-latest
    steps:
      - run: npm run test:unit
  
  test-integration:
    runs-on: ubuntu-latest
    steps:
      - run: npm run test:integration
  
  # Todos se ejecutan en paralelo
```

## Implementación Práctica

### Ejemplo 1: Testing Multi-Plataforma

```yaml
name: Cross-Platform Tests

on: [push, pull_request]

jobs:
  test:
    name: Test on ${{ matrix.os }} with Node ${{ matrix.node }}
    runs-on: ${{ matrix.os }}
    
    strategy:
      fail-fast: false
      matrix:
        os: [ubuntu-latest, windows-latest, macos-latest]
        node: [16, 18, 20]
        exclude:
          # Node 16 obsoleto en Windows
          - os: windows-latest
            node: 16
        include:
          # Prueba experimental con Node 21
          - os: ubuntu-latest
            node: 21
            experimental: true
    
    continue-on-error: ${{ matrix.experimental == true }}
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js ${{ matrix.node }}
        uses: actions/setup-node@v3
        with:
          node-version: ${{ matrix.node }}
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run tests
        run: npm test
      
      - name: Upload coverage
        if: matrix.os == 'ubuntu-latest' && matrix.node == '18'
        uses: codecov/codecov-action@v3
```

### Ejemplo 2: Multi-Database Testing

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    
    strategy:
      matrix:
        database:
          - name: postgres
            version: 14
            port: 5432
          - name: postgres
            version: 15
            port: 5433
          - name: mysql
            version: 8
            port: 3306
    
    services:
      database:
        image: ${{ matrix.database.name }}:${{ matrix.database.version }}
        ports:
          - ${{ matrix.database.port }}:${{ matrix.database.port }}
    
    steps:
      - uses: actions/checkout@v3
      - run: npm ci
      - run: npm test
        env:
          DB_TYPE: ${{ matrix.database.name }}
          DB_PORT: ${{ matrix.database.port }}
```

### Ejemplo 3: Build para Múltiples Targets

```yaml
jobs:
  build:
    strategy:
      matrix:
        include:
          - target: linux-x64
            os: ubuntu-latest
            arch: x64
          - target: linux-arm64
            os: ubuntu-latest
            arch: arm64
          - target: windows-x64
            os: windows-latest
            arch: x64
          - target: darwin-x64
            os: macos-latest
            arch: x64
          - target: darwin-arm64
            os: macos-latest
            arch: arm64
    
    runs-on: ${{ matrix.os }}
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Build for ${{ matrix.target }}
        run: |
          npm run build -- --target=${{ matrix.arch }}
      
      - name: Upload artifact
        uses: actions/upload-artifact@v3
        with:
          name: build-${{ matrix.target }}
          path: dist/
```

### Ejemplo 4: Pipeline Completo con Paralelismo

```yaml
name: Optimized Pipeline

on: push

jobs:
  # Jobs rápidos en paralelo
  quick-checks:
    strategy:
      matrix:
        check: [lint, format, types]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm ci
      - run: npm run ${{ matrix.check }}
  
  # Tests en paralelo con matrix
  test:
    needs: quick-checks
    strategy:
      fail-fast: false
      max-parallel: 4
      matrix:
        shard: [1, 2, 3, 4]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm ci
      - name: Run test shard ${{ matrix.shard }}/4
        run: npm run test -- --shard=${{ matrix.shard }}/4
  
  # Build para diferentes plataformas
  build:
    needs: test
    strategy:
      matrix:
        platform: [linux, windows, macos]
    runs-on: ${{ matrix.platform }}-latest
    steps:
      - uses: actions/checkout@v3
      - run: npm ci
      - run: npm run build:${{ matrix.platform }}
  
  # Deploy solo después de todo
  deploy:
    needs: [test, build]
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - run: echo "All tests passed, deploying..."
```

## Mejores Prácticas

1. **Usa fail-fast: false para tests**: Ver todos los fallos
2. **Limita max-parallel si usas recursos compartidos**
3. **Nombra jobs descriptivamente**: Usa `name:` en matrix jobs
4. **Usa exclude para optimizar**: No pruebes combinaciones innecesarias
5. **Continue-on-error para versiones experimentales**

## Conceptos clave para recordar

- 🔑 **Matrix**: Ejecutar job con múltiples configuraciones
- 🔑 **Fail-fast**: Cancelar al primer fallo (o no)
- 🔑 **Max-parallel**: Limitar jobs concurrentes
- 🔑 **Include**: Agregar configuraciones específicas
- 🔑 **Exclude**: Omitir ciertas combinaciones
- 🔑 **Continue-on-error**: Permitir fallos sin afectar el workflow

## Próximos pasos

En el siguiente módulo explorarás el GitHub Actions Marketplace y aprenderás a usar y crear actions reutilizables.

¡Sigue aprendiendo! 🚀
