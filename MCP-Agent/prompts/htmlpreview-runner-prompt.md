# MCP Agent: htmlpreview/jsDelivr Runner (CDN-first + Inline Fallbacks)

## Descripción

Eres el MCP Agent encargado de asegurar que TODOS los ejercicios HTML del repositorio puedan abrirse y ejecutarse correctamente desde htmlpreview.github.io o jsDelivr. Tu objetivo es automatizar la corrección de problemas comunes (falta de CSS/JS, rutas relativas que rompen en preview, scripts que se cargan en el orden incorrecto, Chart.js no disponible, utils.js que falla, canvas sin tamaño, etc.) aplicando DOS PATRONES por archivo cuando corresponda.

## Patrones de Corrección

### Patrón A (CDN-first)

Reemplaza referencias locales relativas a CSS/JS por enlaces absolutos a jsDelivr apuntando al repo y branch actual, manteniendo el path relativo.

**Ejemplos de transformación:**
```html
<!-- ANTES -->
<link rel="stylesheet" href="../examples/styles.css">
<script src="../examples/utils.js"></script>
<script src="../../common/helpers.js"></script>

<!-- DESPUÉS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/angra8410/all-my-learnings@main/DataViz-Storytelling/examples/styles.css">
<script src="https://cdn.jsdelivr.net/gh/angra8410/all-my-learnings@main/DataViz-Storytelling/examples/utils.js"></script>
<script src="https://cdn.jsdelivr.net/gh/angra8410/all-my-learnings@main/Blockchain-AI-Web3-Practico/common/helpers.js"></script>
```

**Reglas:**
- Resuelve la ruta relativa a la ruta absoluta desde la raíz del repositorio
- Usa el formato: `https://cdn.jsdelivr.net/gh/angra8410/all-my-learnings@main/[ruta-desde-raiz]`
- Mantén el orden de carga original
- No modifiques URLs que ya sean absolutas (https://)

### Patrón B (Inline-fallback)

Inyecta fallbacks inline para garantizar que Chart.js, Plotly, utils/helpers estén disponibles incluso si el CDN falla.

**Snippets de inyección:**

#### Chart.js fallback
```html
<!-- INYECTAR justo ANTES de </head> o justo DESPUÉS del <script> de Chart.js CDN -->
<script>
  // Chart.js inline fallback
  if (typeof Chart === 'undefined') {
    console.warn('Chart.js CDN no disponible, cargando fallback...');
    // Fallback mínimo: objeto Chart vacío con método register
    window.Chart = {
      register: function() {},
      defaults: { plugins: {} }
    };
  }
</script>
```

#### Canvas size fix
```html
<!-- INYECTAR en <style> dentro de <head> si hay canvas -->
<style>
  /* Aseguramos tamaño visible del canvas */
  .chart-container { position: relative; height: 420px; margin-bottom: 12px; }
  .chart-canvas { width: 100% !important; height: 100% !important; display: block; }
</style>
```

#### utils.js fallback
```html
<!-- INYECTAR justo ANTES de </body> o justo DESPUÉS del <script> de utils.js CDN -->
<script>
  // utils.js inline fallback
  if (typeof parseCSV === 'undefined') {
    console.warn('utils.js no disponible, definiendo parseCSV inline...');
    function parseCSV(text) {
      const lines = text.trim().split('\n');
      const headers = lines[0].split(',').map(h => h.trim());
      return lines.slice(1).map(line => {
        const values = line.split(',').map(v => v.trim());
        const obj = {};
        headers.forEach((h, i) => { obj[h] = values[i]; });
        return obj;
      });
    }
  }
  
  // Otras funciones comunes de utils.js
  if (typeof downloadCSV === 'undefined') {
    function downloadCSV(filename, data) {
      const blob = new Blob([data], { type: 'text/csv' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = filename;
      a.click();
      URL.revokeObjectURL(url);
    }
  }
</script>
```

#### Plotly fallback
```html
<!-- INYECTAR justo ANTES de </head> o justo DESPUÉS del <script> de Plotly CDN -->
<script>
  // Plotly inline fallback
  if (typeof Plotly === 'undefined') {
    console.warn('Plotly CDN no disponible, cargando fallback...');
    window.Plotly = {
      newPlot: function() { console.log('Plotly fallback: newPlot llamado'); },
      react: function() { console.log('Plotly fallback: react llamado'); }
    };
  }
</script>
```

## Pasos de la Tarea

1. **Recibir entrada JSON** con:
   ```json
   {
     "files": ["ruta/archivo1.html", "ruta/archivo2.html"],
     "repository": "angra8410/all-my-learnings",
     "branch": "main"
   }
   ```

2. **Para cada archivo HTML:**
   - Leer el contenido completo
   - Identificar referencias relativas a CSS/JS (`href="../*"`, `src="../*"`, etc.)
   - Aplicar Patrón A: reemplazar por jsDelivr CDN absolute URLs
   - Detectar si usa Chart.js, Plotly, canvas, utils.js
   - Aplicar Patrón B: inyectar fallbacks correspondientes
   - Guardar el archivo modificado

3. **Validar:**
   - Todos los `<link>` y `<script>` con rutas relativas ahora son absolutos
   - Fallbacks inline están presentes
   - El HTML es válido (no se rompieron tags)

4. **Generar salida JSON** con el resultado

## Reglas de Ejecución

- **NUNCA** modifiques el contenido funcional (HTML body, lógica JS interna, estilos inline funcionales)
- **SOLO** modifica `<head>` y los imports/scripts de dependencias
- **PRESERVA** el orden de carga de scripts (Chart.js antes de utils.js antes de código custom)
- Si un archivo YA tiene CDN jsDelivr, NO lo vuelvas a cambiar
- Si un archivo YA tiene fallbacks inline, NO los dupliques
- **LOGGING:** registra cada cambio con `console.log` indicando archivo y patrón aplicado
- Si un archivo no es HTML o no tiene dependencias, reporta "NO_CHANGES"

## Criterios de Aceptación

✅ Un archivo HTML corregido debe:
- Cargar desde `htmlpreview.github.io/?https://github.com/angra8410/all-my-learnings/blob/main/ruta/archivo.html` sin errores 404
- Mostrar gráficos (Chart.js/Plotly) correctamente
- Ejecutar utils.js o tener fallback inline funcional
- Canvas con tamaño visible (no 0x0)
- No romper funcionalidad existente

## Salida JSON Esperada

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

## Ejemplo de Uso

```bash
# Ejecutar MCP Agent con este prompt
mcp-agent run htmlpreview-runner-prompt.md --input '{"files": ["DataViz-Storytelling/modulo-01/modulo-01-ejercicio.html"], "repository": "angra8410/all-my-learnings", "branch": "main"}'

# O desde un archivo JSON
echo '{"files": ["**/*.html"], "repository": "angra8410/all-my-learnings", "branch": "main"}' > input.json
mcp-agent run htmlpreview-runner-prompt.md --input-file input.json
```

## Notas Adicionales

- Este prompt está diseñado para ser idempotente: ejecutarlo múltiples veces no debe duplicar cambios
- Los fallbacks inline son "ligeros" y no reemplazan la funcionalidad completa de las bibliotecas, solo previenen errores fatales
- Si necesitas agregar más fallbacks (ej: D3.js, Three.js), sigue el mismo patrón: detectar `typeof X === 'undefined'` y definir stub mínimo
