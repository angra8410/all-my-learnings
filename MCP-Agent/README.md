# MCP Agent Prompts

Este directorio contiene prompts especializados para el MCP Agent, diseñados para automatizar tareas repetitivas y correcciones en el repositorio.

## Prompts Disponibles

### 📄 htmlpreview-runner-prompt.md

**Objetivo:** Automatizar la corrección de ejercicios HTML para que funcionen correctamente con htmlpreview.github.io y jsDelivr.

**Qué hace:**
- Convierte rutas relativas de CSS/JS a URLs absolutas de jsDelivr CDN
- Inyecta fallbacks inline para Chart.js, Plotly, utils.js
- Añade fixes para canvas sin tamaño
- Asegura que todos los ejercicios HTML se puedan visualizar desde htmlpreview sin errores 404 o dependencias rotas

**Problemas que resuelve:**
- ❌ `../examples/styles.css` → ✅ `https://cdn.jsdelivr.net/gh/angra8410/all-my-learnings@main/DataViz-Storytelling/examples/styles.css`
- ❌ Chart.js no carga desde CDN → ✅ Fallback inline previene errores
- ❌ Canvas con tamaño 0x0 → ✅ Estilos forzados para tamaño visible
- ❌ utils.js relativo falla en preview → ✅ CDN + fallback inline

## Cómo Usar

### Prerrequisitos

1. Tener instalado el MCP Agent
2. Clonar el repositorio localmente
3. Tener permisos de escritura en los archivos HTML

### Ejecución Básica

```bash
# Corregir un archivo específico
mcp-agent run MCP-Agent/prompts/htmlpreview-runner-prompt.md \
  --input '{"files": ["DataViz-Storytelling/modulo-01/modulo-01-ejercicio.html"], "repository": "angra8410/all-my-learnings", "branch": "main"}'

# Corregir múltiples archivos
mcp-agent run MCP-Agent/prompts/htmlpreview-runner-prompt.md \
  --input '{"files": ["DataViz-Storytelling/modulo-01/modulo-01-ejercicio.html", "DataViz-Storytelling/modulo-02/modulo-02-ejercicio.html"], "repository": "angra8410/all-my-learnings", "branch": "main"}'

# Corregir todos los HTML de un módulo usando glob pattern
mcp-agent run MCP-Agent/prompts/htmlpreview-runner-prompt.md \
  --input '{"files": ["DataViz-Storytelling/**/*.html"], "repository": "angra8410/all-my-learnings", "branch": "main"}'
```

### Estructura de Entrada

```json
{
  "files": [
    "ruta/relativa/archivo1.html",
    "ruta/relativa/archivo2.html"
  ],
  "repository": "angra8410/all-my-learnings",
  "branch": "main"
}
```

**Parámetros:**
- `files` (array): Lista de rutas relativas de archivos HTML a corregir. Acepta glob patterns como `**/*.html`
- `repository` (string): Usuario/organización y nombre del repositorio en formato `owner/repo`
- `branch` (string): Branch del repositorio a usar en las URLs de jsDelivr (típicamente `main`)

### Salida Esperada

El MCP Agent procesará los archivos y devolverá un JSON con el resultado:

```json
{
  "status": "success",
  "files_processed": 5,
  "files_modified": 4,
  "files_skipped": 1,
  "details": [
    {
      "file": "DataViz-Storytelling/modulo-01/modulo-01-ejercicio.html",
      "changes": [
        "Patrón A: 2 rutas relativas → jsDelivr CDN",
        "Patrón B: Chart.js fallback inyectado",
        "Patrón B: canvas size fix inyectado"
      ],
      "status": "modified"
    },
    {
      "file": "DataViz-Storytelling/modulo-02/modulo-02-ejercicio.html",
      "changes": ["Ya tiene CDN jsDelivr y fallbacks"],
      "status": "skipped"
    }
  ],
  "errors": []
}
```

## Pruebas Locales

### 1. Ejecutar el MCP Agent

```bash
# Desde la raíz del repositorio
cd /ruta/a/all-my-learnings

# Crear archivo de entrada
cat > input.json << 'EOF'
{
  "files": ["DataViz-Storytelling/modulo-01/modulo-01-ejercicio.html"],
  "repository": "angra8410/all-my-learnings",
  "branch": "main"
}
EOF

# Ejecutar
mcp-agent run MCP-Agent/prompts/htmlpreview-runner-prompt.md --input-file input.json
```

### 2. Verificar los Cambios

```bash
# Ver diff de los archivos modificados
git diff DataViz-Storytelling/modulo-01/modulo-01-ejercicio.html

# Verificar que las URLs de jsDelivr están presentes
grep -n "cdn.jsdelivr.net" DataViz-Storytelling/modulo-01/modulo-01-ejercicio.html
```

### 3. Probar en htmlpreview.github.io

Abre en el navegador:
```
https://htmlpreview.github.io/?https://github.com/angra8410/all-my-learnings/blob/main/DataViz-Storytelling/modulo-01/modulo-01-ejercicio.html
```

**Checklist de validación:**
- ✅ La página carga sin errores 404 en la consola
- ✅ Los estilos CSS se aplican correctamente
- ✅ Los gráficos Chart.js/Plotly se renderizan
- ✅ Los canvas tienen tamaño visible (no 0x0)
- ✅ Las funciones de utils.js funcionan o hay fallback

### 4. Revertir si es necesario

```bash
# Revertir cambios en un archivo
git checkout DataViz-Storytelling/modulo-01/modulo-01-ejercicio.html

# Revertir todos los cambios
git checkout .
```

## Patrones Aplicados

### Patrón A: CDN-first

Convierte rutas relativas a URLs absolutas de jsDelivr:

```html
<!-- ANTES -->
<link rel="stylesheet" href="../examples/styles.css">
<script src="../examples/utils.js"></script>

<!-- DESPUÉS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/angra8410/all-my-learnings@main/DataViz-Storytelling/examples/styles.css">
<script src="https://cdn.jsdelivr.net/gh/angra8410/all-my-learnings@main/DataViz-Storytelling/examples/utils.js"></script>
```

### Patrón B: Inline-fallback

Inyecta fallbacks para dependencias críticas:

```html
<!-- Fallback de Chart.js -->
<script>
  if (typeof Chart === 'undefined') {
    console.warn('Chart.js CDN no disponible, cargando fallback...');
    window.Chart = {
      register: function() {},
      defaults: { plugins: {} }
    };
  }
</script>

<!-- Fix de tamaño de canvas -->
<style>
  .chart-container { position: relative; height: 420px; margin-bottom: 12px; }
  .chart-canvas { width: 100% !important; height: 100% !important; display: block; }
</style>
```

## Características del Prompt

- ✅ **Idempotente:** Ejecutarlo múltiples veces no duplica cambios
- ✅ **Conservador:** Solo modifica `<head>` y imports, no toca el body ni la lógica JS
- ✅ **Seguro:** Preserva el orden de carga de scripts
- ✅ **Validado:** Reporta cambios detallados por archivo
- ✅ **Eficiente:** Detecta archivos que ya están corregidos y los salta

## Troubleshooting

### Problema: MCP Agent no encuentra los archivos

**Solución:** Verifica que las rutas sean relativas desde la raíz del repositorio:
```json
{
  "files": ["DataViz-Storytelling/modulo-01/modulo-01-ejercicio.html"]
}
```

No uses rutas absolutas o que empiecen con `/`.

### Problema: Los cambios se duplican

**Solución:** El prompt es idempotente. Si esto ocurre, reporta un bug. Mientras tanto, revierte con `git checkout` y vuelve a ejecutar.

### Problema: Chart.js sigue sin funcionar en htmlpreview

**Solución:** 
1. Verifica que el CDN de Chart.js esté ANTES del fallback inline
2. Verifica que el fallback esté DENTRO de `<script>` tags, no como comentario
3. Abre la consola del navegador y verifica los mensajes de error

### Problema: El archivo no se modifica (status: "skipped")

**Solución:** El archivo ya tiene las correcciones aplicadas. Verifica con:
```bash
grep -n "cdn.jsdelivr.net" archivo.html
```

## Extensión del Prompt

Si necesitas agregar soporte para otras librerías (D3.js, Three.js, etc.), edita `htmlpreview-runner-prompt.md` y añade:

1. Un nuevo snippet de fallback en la sección "Patrón B"
2. Lógica de detección (ej: `if (typeof D3 === 'undefined')`)
3. Stub mínimo para prevenir errores fatales

Ejemplo para D3.js:
```html
<script>
  if (typeof d3 === 'undefined') {
    console.warn('D3.js CDN no disponible, cargando fallback...');
    window.d3 = {
      select: function() { return { append: function() {} }; }
    };
  }
</script>
```

## Contribuir

Para mejorar este prompt:
1. Identifica un nuevo problema recurrente en htmlpreview
2. Desarrolla el snippet de corrección
3. Prueba que sea idempotente
4. Actualiza `htmlpreview-runner-prompt.md` y este README
5. Abre un PR con ejemplos de antes/después

## Licencia

Este prompt y documentación son parte del repositorio `all-my-learnings` y están disponibles para uso interno y educativo.
