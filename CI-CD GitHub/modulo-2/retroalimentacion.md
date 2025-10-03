# Retroalimentación y Soluciones - Módulo 2: GitHub Actions - Fundamentos

## Respuestas a Preguntas de Opción Múltiple

### Pregunta 1: ¿Qué es GitHub Actions?
**Respuesta correcta: B) Una plataforma de CI/CD integrada en GitHub**

**Explicación**: GitHub Actions es la plataforma de automatización y CI/CD que viene integrada directamente en GitHub, permitiendo crear workflows sin herramientas externas.

---

### Pregunta 2: ¿En qué formato se definen los workflows?
**Respuesta correcta: C) YAML**

**Explicación**: Los workflows de GitHub Actions se definen en archivos YAML (`.yml` o `.yaml`), un formato legible para definir configuraciones.

---

### Pregunta 3: ¿Qué palabra clave se usa para ejecutar comandos shell?
**Respuesta correcta: C) run**

**Explicación**: La palabra clave `run` se usa para ejecutar comandos de shell en un step.

---

### Pregunta 4: ¿Qué hace `actions/checkout@v3`?
**Respuesta correcta: B) Descarga el código del repositorio al runner**

**Explicación**: Esta action oficial hace checkout (descarga) del código de tu repositorio al runner para que puedas trabajar con él.

---

### Pregunta 5: ¿Qué evento trigger ejecuta el workflow en cada push?
**Respuesta correcta: B) on: push**

**Explicación**: `on: push` configura el workflow para ejecutarse cada vez que se hace push al repositorio.

---

## Respuestas a Verdadero o Falso

1. **Un workflow puede tener múltiples jobs.**  
   **Verdadero** - Un workflow puede tener tantos jobs como necesites, y pueden ejecutarse en paralelo o secuencialmente.

2. **Los workflows deben estar en `.github/workflows/`.**  
   **Verdadero** - GitHub Actions busca workflows específicamente en esta carpeta.

3. **Solo puedes usar Ubuntu como sistema operativo del runner.**  
   **Falso** - Puedes usar Ubuntu, Windows y macOS como runners.

4. **Un job puede tener múltiples steps.**  
   **Verdadero** - Los jobs contienen una lista de steps que se ejecutan secuencialmente.

5. **GitHub Actions es gratis ilimitadamente para repositorios privados.**  
   **Falso** - Para repos privados hay límites mensuales de minutos. Los repos públicos tienen uso gratuito ilimitado.

---

## Solución: Completa el Código

### Ejercicio 1: Workflow Básico
```yaml
name: Mi Primer Workflow

on: push

jobs:
  mi-job:
    runs-on: ubuntu-latest
    
    steps:
      - name: Saludar
        run: echo "Hola Mundo"
```

---

### Ejercicio 2: Workflow con Checkout
```yaml
name: Build App

on: push

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout código
        uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
```

---

## Solución: Identificar Componentes

A es: **Nombre del workflow**  
B es: **Eventos que triggean el workflow**  
C es: **Sección de jobs**  
D es: **Nombre del job**  
E es: **Sistema operativo del runner**  
F es: **Lista de steps**  
G es: **Action para hacer checkout**  
H es: **Comando para ejecutar tests**

---

## Solución: Corregir Errores

**Errores encontrados:**
1. Falta `:` después de `name`
2. Falta `:` después de `on`
3. Falta `:` después de `jobs`
4. Falta `:` después de `build`
5. `ubuntu` debería ser `ubuntu-latest` o versión específica
6. `execute` debería ser `run`

**Código corregido:**
```yaml
name: Mi Workflow

on: push

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
      - name: Test
        run: npm test
```

---

## Respuestas a Asociación de Conceptos

1. Workflow → **D** (Proceso automatizado completo)
2. Job → **E** (Conjunto de steps que se ejecutan juntos)
3. Step → **A** (Tarea individual dentro de un job)
4. Runner → **B** (Servidor que ejecuta los workflows)
5. Action → **F** (Comando reutilizable)
6. Event → **C** (Trigger que inicia un workflow)

---

## Soluciones a Escenarios Prácticos

### Escenario 1: Tests en cada PR
```yaml
name: PR Tests
on: pull_request
```

---

### Escenario 2: Ejecución diaria
```yaml
on:
  schedule:
    - cron: '0 2 * * *'
```

---

### Escenario 3: Push a main y develop
```yaml
on:
  push:
    branches:
      - main
      - develop
```

---

## Análisis de Logs

**1. ¿Qué causó el error?**  
El script "test" no está definido en el `package.json`.

**2. ¿Cómo lo solucionarías?**  
Agregar el script `"test": "..."` en la sección de scripts del `package.json`.

**3. ¿En qué step ocurrió el error?**  
En el step que ejecuta `npm test`.

---

## Workflow Sugerido para Node.js

```yaml
name: Node.js CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build-and-test:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout código
        uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
      
      - name: Instalar dependencias
        run: npm ci
      
      - name: Ejecutar tests
        run: npm test
      
      - name: Build
        run: npm run build
```

---

## Evaluación de Desempeño

### Si acertaste 90% o más: 🌟 ¡Excelente!
Dominas los fundamentos de GitHub Actions. Estás listo para workflows más avanzados.

**Próximos pasos:**
- Continúa con el Módulo 3
- Experimenta creando workflows en tus repos
- Explora el Marketplace de Actions

---

### Si acertaste 70-89%: 💪 ¡Muy bien!
Comprendes los conceptos principales. Algunos detalles necesitan práctica.

**Recomendaciones:**
- Practica creando workflows simples
- Revisa la sintaxis YAML
- Experimenta con diferentes triggers

---

### Si acertaste menos de 70%: 📚 Sigue adelante
Necesitas reforzar los conceptos básicos.

**Recomendaciones:**
- Vuelve a leer el README
- Crea un workflow simple paso a paso
- Usa la documentación oficial de GitHub Actions

---

## Preparación para el Siguiente Módulo

Asegúrate de:

✅ Entender la estructura de un workflow (name, on, jobs, steps)  
✅ Saber usar `run` y `uses`  
✅ Conocer actions comunes como `checkout` y `setup-node`  
✅ Poder crear un workflow básico desde cero  
✅ Entender diferentes eventos/triggers  

---

## Recursos Adicionales

**Documentación oficial:**
- GitHub Actions documentation
- Workflow syntax reference
- Events that trigger workflows

**Actions útiles para explorar:**
- `actions/checkout@v3` - Checkout code
- `actions/setup-node@v3` - Setup Node.js
- `actions/setup-python@v4` - Setup Python
- `actions/upload-artifact@v3` - Upload artifacts
- `actions/cache@v3` - Cache dependencies

¡Excelente trabajo! Ahora dominas los fundamentos de GitHub Actions! 🎉
