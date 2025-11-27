# Actividades Interactivas - Módulo 2: GitHub Actions - Fundamentos

## Sección 1: Preguntas de Opción Múltiple

### Pregunta 1
**¿Qué es GitHub Actions?**

A) Un editor de código  
B) Una plataforma de CI/CD integrada en GitHub  
C) Un lenguaje de programación  
D) Una base de datos

B
---

### Pregunta 2
**¿En qué formato se definen los workflows de GitHub Actions?**

A) JSON  
B) XML  
C) YAML  
D) CSV

C
---

### Pregunta 3
**¿Qué palabra clave se usa para ejecutar comandos shell en un step?**

A) execute  
B) command  
C) run  
D) do

C
---

### Pregunta 4
**¿Qué hace la action `actions/checkout@v3`?**

A) Crea un nuevo repositorio  
B) Descarga el código del repositorio al runner  
C) Sube archivos a GitHub  
D) Elimina archivos

B
---

### Pregunta 5
**¿Qué evento trigger ejecuta el workflow en cada push?**

A) on: commit  
B) on: push  
C) on: upload  
D) on: send

B
---

## Sección 2: Completa el Código

### Ejercicio 1: Workflow Básico
**Completa este workflow básico:**

```yaml
name: Mi Primer Workflow

on: _______________
  push:

jobs:
  mi-job:
    runs-on: ubuntu-latest
    
    steps:
      - name: Saludar
        run: ech "Hola mundo desde Github Actions"
```

**Tus respuestas:**
- `on:` push
- `runs-on:` ubuntu-latest
- `run:` echo "Hola Mundo desde GitHub Actions"

---

### Ejercicio 2: Workflow con Checkout
**Completa para hacer checkout del código:**

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
        uses: Install Node.js
        with:
          node-version: 'x16, x17, x18'
```

**Tus respuestas:**
- Checkout action: actions/checkout@v3
- Setup Node action: install node.js
- Node version: x16, x17, x18

---

## Sección 3: Verdadero o Falso

1. **Un workflow puede tener múltiples jobs.**
   - [x] Verdadero
   - [ ] Falso

2. **Los workflows deben estar en la carpeta `.github/workflows/`.**
   - [x] Verdadero
   - [ ] Falso

3. **Solo puedes usar Ubuntu como sistema operativo del runner.**
   - [x] Verdadero
   - [ ] Falso

4. **Un job puede tener múltiples steps.**
   - [x] Verdadero
   - [ ] Falso

5. **GitHub Actions es gratis ilimitadamente para repositorios privados.**
   - [ ] Verdadero
   - [x] Falso

---

## Sección 4: Identificar Componentes

**Dado este workflow, identifica cada componente:**

```yaml
name: Test Suite                    # A
on: [push, pull_request]           # B
jobs:                              # C
  test:                            # D
    runs-on: ubuntu-latest         # E
    steps:                         # F
      - uses: actions/checkout@v3  # G
      - run: npm test              # H
```

**Preguntas:**

A es: Workflow's name  
B es: Trigger event  
C es: Jobs  
D es: _______________  
E es: _______________  
F es: _______________  
G es: _______________  
H es: _______________

---

## Sección 5: Corregir Errores

**Este workflow tiene errores. Encuéntralos y corrígelos:**

```yaml
name Mi Workflow

on push

jobs
  build
    runs-on: ubuntu
    
    steps:
      - name: Test
        execute: npm test
```

**Errores encontrados:**

1. _______________________________________________
2. _______________________________________________
3. _______________________________________________
4. _______________________________________________
5. _______________________________________________

**Código corregido:**
```yaml
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________
```

---

## Sección 6: Diseña tu Workflow

**Diseña un workflow para tu proyecto que:**
- Se ejecute en push a la rama main
- Haga checkout del código
- Instale dependencias
- Ejecute tests

```yaml
name: _______________________________________________

on:
  _______________________________________________

jobs:
  _______________________________________________:
    runs-on: _______________________________________________
    
    steps:
      - name: _______________________________________________
        uses: _______________________________________________
      
      - name: _______________________________________________
        run: _______________________________________________
      
      - name: _______________________________________________
        run: _______________________________________________
```

---

## Sección 7: Escenarios Prácticos

### Escenario 1
**Tu equipo quiere ejecutar tests automáticamente en cada PR.**

**¿Qué evento usarías?**
_______________________________________________

**Escribe el inicio del workflow:**
```yaml
_______________________________________________
_______________________________________________
```

---

### Escenario 2
**Necesitas un workflow que se ejecute diariamente a las 2 AM.**

**¿Qué evento/sintaxis usarías?**
_______________________________________________

**Escribe la configuración:**
```yaml
_______________________________________________
_______________________________________________
```

---

### Escenario 3
**Quieres ejecutar el workflow en push a main y develop.**

**Escribe la configuración completa del trigger:**
```yaml
_______________________________________________
_______________________________________________
_______________________________________________
_______________________________________________
```

---

## Sección 8: Asociación de Conceptos

**Relaciona cada término con su definición:**

**Términos:**
1. Workflow
2. Job
3. Step
4. Runner
5. Action
6. Event

**Definiciones:**
A. Tarea individual dentro de un job  
B. Servidor que ejecuta los workflows  
C. Trigger que inicia un workflow  
D. Proceso automatizado completo  
E. Conjunto de steps que se ejecutan juntos  
F. Comando reutilizable

**Tus respuestas:**
1 → ___  
2 → ___  
3 → ___  
4 → ___  
5 → ___  
6 → ___

---

## Sección 9: Actions Marketplace

**Investiga en GitHub Actions Marketplace y completa:**

**3 actions útiles que encontraste:**

1. **Nombre**: _______________________________________________  
   **Qué hace**: _______________________________________________

2. **Nombre**: _______________________________________________  
   **Qué hace**: _______________________________________________

3. **Nombre**: _______________________________________________  
   **Qué hace**: _______________________________________________

**¿Cómo encontrarías una action para desplegar a AWS?**
_______________________________________________

---

## Sección 10: Proyecto Práctico

**Crea un workflow completo para uno de estos proyectos:**

- [ ] Aplicación Node.js
- [ ] Script Python
- [ ] Sitio web estático
- [ ] API REST

**Mi proyecto**: _______________________________________________

**Workflow completo:**

```yaml
name: _______________________________________________

on:
  _______________________________________________

jobs:
  _______________________________________________:
    runs-on: _______________________________________________
    
    steps:
      - name: _______________________________________________
        _______________________________________________
      
      - name: _______________________________________________
        _______________________________________________
      
      - name: _______________________________________________
        _______________________________________________
      
      - name: _______________________________________________
        _______________________________________________
```

**Explicación de cada step:**

1. _______________________________________________
2. _______________________________________________
3. _______________________________________________
4. _______________________________________________

---

## Sección 11: Análisis de Logs

**Imagina que tu workflow falló. Los logs muestran:**

```
Run npm test
npm ERR! Missing script: "test"
Error: Process completed with exit code 1.
```

**Preguntas:**

1. **¿Qué causó el error?**
   _______________________________________________

2. **¿Cómo lo solucionarías?**
   _______________________________________________

3. **¿En qué step ocurrió el error?**
   _______________________________________________

---

## Reflexión Final

**¿Qué ventaja te parece más importante de GitHub Actions?**
_______________________________________________
_______________________________________________

**¿Qué workflow crearías primero para tu proyecto?**
_______________________________________________
_______________________________________________

**¿Qué dudas tienes sobre GitHub Actions?**
_______________________________________________
_______________________________________________

¡Revisa tus respuestas en `retroalimentacion.md`! 🎉
