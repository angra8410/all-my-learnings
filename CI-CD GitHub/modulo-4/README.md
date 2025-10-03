# Módulo 4: Testing Automatizado en CI/CD

## Introducción

Bienvenido al módulo sobre testing automatizado. En este módulo aprenderás:

- Tipos de tests en CI/CD
- Configurar tests unitarios
- Tests de integración
- Code coverage
- Test reporting

## ¿Por qué es importante?

Los tests automatizados son la red de seguridad de tu código. Permiten detectar errores antes de que lleguen a producción y dan confianza para hacer cambios.

## Conceptos Principales

### 1. Tipos de Tests

**Tests Unitarios**: Prueban unidades individuales de código (funciones, métodos)
```javascript
test('suma dos números', () => {
  expect(suma(2, 3)).toBe(5);
});
```

**Tests de Integración**: Prueban cómo interactúan componentes
```javascript
test('API devuelve usuarios', async () => {
  const response = await fetch('/api/users');
  expect(response.status).toBe(200);
});
```

**Tests E2E**: Prueban flujos completos de usuario
```javascript
test('usuario puede hacer login', async () => {
  await page.goto('/login');
  await page.fill('#email', 'test@example.com');
  await page.click('button[type=submit]');
  await expect(page).toHaveURL('/dashboard');
});
```

### 2. Tests en GitHub Actions

**Workflow para Node.js con Jest:**

```yaml
name: Run Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Install dependencies
        run: npm ci
      
      - name: Run unit tests
        run: npm test
      
      - name: Run integration tests
        run: npm run test:integration
```

### 3. Code Coverage

Medir qué porcentaje del código está cubierto por tests:

```yaml
- name: Run tests with coverage
  run: npm test -- --coverage
  
- name: Upload coverage to Codecov
  uses: codecov/codecov-action@v3
  with:
    file: ./coverage/coverage-final.json
    fail_ci_if_error: true
```

### 4. Tests con Múltiples Versiones

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
      - run: npm ci
      - run: npm test
```

### 5. Test Reports

Generar reportes visuales de tests:

```yaml
- name: Test Report
  uses: dorny/test-reporter@v1
  if: success() || failure()
  with:
    name: Test Results
    path: reports/jest-*.xml
    reporter: jest-junit
```

## Implementación Práctica

### Ejemplo Completo: Pipeline de Testing

```yaml
name: Comprehensive Testing

on:
  push:
    branches: [main, develop]
  pull_request:

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm ci
      - run: npm run lint
  
  unit-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
        with:
          node-version: '18'
      - run: npm ci
      - run: npm test -- --coverage
      - uses: codecov/codecov-action@v3
  
  integration-tests:
    needs: unit-tests
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:14
        env:
          POSTGRES_PASSWORD: postgres
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
    steps:
      - uses: actions/checkout@v3
      - run: npm ci
      - run: npm run test:integration
        env:
          DATABASE_URL: postgresql://postgres:postgres@localhost:5432/test
  
  e2e-tests:
    needs: integration-tests
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
      - run: npm ci
      - run: npx playwright install
      - run: npm run test:e2e
      - uses: actions/upload-artifact@v3
        if: failure()
        with:
          name: playwright-screenshots
          path: test-results/
```

## Mejores Prácticas

1. **Tests rápidos primero**: Ejecuta tests unitarios antes que E2E
2. **Falla rápido**: Si los tests unitarios fallan, no ejecutes los demás
3. **Guarda artifacts**: Screenshots, logs de tests fallidos
4. **Usa caché**: Para dependencias y datos de tests
5. **Reporta resultados**: Usa badges en el README

## Conceptos clave para recordar

- 🔑 **Tests Unitarios**: Prueban funciones individuales
- 🔑 **Tests de Integración**: Prueban interacciones entre componentes
- 🔑 **Tests E2E**: Prueban flujos completos de usuario
- 🔑 **Coverage**: Porcentaje de código cubierto por tests
- 🔑 **Services**: Contenedores auxiliares (DB, cache, etc.)
- 🔑 **Test Matrix**: Probar en múltiples versiones/plataformas

## Próximos pasos

En el siguiente módulo aprenderás sobre artifacts y gestión de deployments para manejar los resultados de tus builds.

¡Sigue aprendiendo! 🚀
