# DataViz-Storytelling: Curso Práctico de Data Visualization & Storytelling

## 🎯 Descripción del Curso

**DataViz-Storytelling** es un curso intensivo y práctico (95% hands-on) diseñado para llevarte desde cero hasta nivel avanzado en visualización de datos y storytelling, con un enfoque único: **todos los ejercicios se ejecutan directamente en el navegador** sin necesidad de Jupyter, Colab o entornos de servidor.

### Características Principales

✅ **95% Práctico**: Mínima teoría, máxima acción con ejercicios interactivos  
✅ **100% Cliente Web**: HTML + JavaScript + Chart.js/Plotly (sin backend, sin Python notebooks)  
✅ **Ejercicios Interactivos**: Cada módulo incluye ejercicios ejecutables en el navegador  
✅ **CSV de Muestra**: Datasets pequeños en texto plano para practicar  
✅ **Guardado Local**: Resultados almacenados en localStorage del navegador  
✅ **Exportación**: Descarga gráficos como PNG y datos como CSV/JSON  
✅ **Evaluación Automática**: Cuestionarios con scoring 0-100% integrados  
✅ **Sin Instalación**: Abre el HTML en tu navegador y comienza a trabajar

---

## 🚀 Cómo Usar Este Curso

### Navegador Recomendado

- **Chrome** o **Edge** (mejor compatibilidad)
- Firefox también funciona
- Safari puede tener limitaciones

### Flujo de Trabajo

1. **Explora el módulo**: Lee el `README.md` del módulo
2. **Lee la actividad**: Revisa `actividad-interactiva.md` para conocer los ejercicios
3. **Abre el HTML interactivo**: Haz doble clic en `modulo-XX-ejercicio.html`
4. **Practica**: 
   - Carga CSV desde `/examples/` o pega tus propios datos
   - Configura parámetros del gráfico
   - Visualiza resultados en tiempo real
   - Responde el cuestionario del módulo
5. **Guarda evidencias**: 
   - Descarga gráficos como PNG
   - Descarga resultados como CSV/JSON
   - Commitea los outputs a tu repositorio
6. **Registra progreso**: Actualiza `progreso.md` y `retroalimentacion.md`

### Estructura de Archivos

```
DataViz-Storytelling/
├── README.md                                    # Este archivo
├── ejercicio-evaluativo-interactivo.html        # Evaluación global del curso
├── examples/                                     # Recursos compartidos
│   ├── ventas.csv                               # Datos de ventas
│   ├── poblacion.csv                            # Datos de población
│   ├── tiempos.csv                              # Datos de tiempos de trabajo
│   ├── utils.js                                 # Utilidades JavaScript
│   └── styles.css                               # Estilos comunes
├── modulo-01-introduccion/
│   ├── README.md
│   ├── actividad-interactiva.md
│   ├── retroalimentacion.md
│   ├── progreso.md
│   └── modulo-01-ejercicio.html
├── modulo-02-principios-visualizacion/
│   └── ...
└── modulo-10-proyecto-integrador/
    └── ...
```

---

## 📚 Estructura del Curso

### Módulo 01: Introducción a Data Visualization
**Duración**: 3-4 horas  
**Contenido**: Conceptos básicos, tipos de gráficos, cuándo usar cada uno, primeros ejercicios con Chart.js

### Módulo 02: Principios de Visualización
**Duración**: 4-5 horas  
**Contenido**: Percepción visual, elección de colores, jerarquía visual, principios de diseño aplicados

### Módulo 03: Herramientas y Librerías
**Duración**: 5-6 horas  
**Contenido**: Chart.js, Plotly.js, D3.js basics, comparación de herramientas, ejercicios prácticos

### Módulo 04: Datos y Agrupación
**Duración**: 5-6 horas  
**Contenido**: Manipulación de CSV, agregación, filtrado, transformación, preparación de datos para visualización

### Módulo 05: Interacción y Dashboards
**Duración**: 6-7 horas  
**Contenido**: Gráficos interactivos, tooltips, zoom, filtros dinámicos, construcción de dashboards cliente

### Módulo 06: Storytelling y Narrativa
**Duración**: 5-6 horas  
**Contenido**: Estructura narrativa, guía al espectador, contexto y anotaciones, casos de estudio

### Módulo 07: Diseño Avanzado y Accesibilidad
**Duración**: 5-6 horas  
**Contenido**: Paletas de color accesibles, contraste, diseño responsivo, visualizaciones para daltonismo

### Módulo 08: Evaluación Crítica
**Duración**: 4-5 horas  
**Contenido**: Análisis de visualizaciones, detección de gráficos engañosos, mejora iterativa

### Módulo 09: Datasets Reales y Proyectos
**Duración**: 6-7 horas  
**Contenido**: Trabajar con datos reales, limpieza, análisis exploratorio, visualizaciones complejas

### Módulo 10: Proyecto Integrador
**Duración**: 8-10 horas  
**Contenido**: Proyecto completo desde datos crudos hasta dashboard interactivo con storytelling

---

## 🎨 Herramientas Utilizadas

- **Chart.js** (CDN): Librería de gráficos simple y versátil
- **Plotly.js** (CDN): Gráficos interactivos avanzados
- **FileReader API**: Carga de archivos CSV desde el cliente
- **localStorage**: Guardado persistente de resultados
- **Blob API**: Descarga de archivos generados

---

## 💾 Guardado de Evidencias

### Recomendación de Carpeta `outputs/`

Crea una carpeta `outputs/` para guardar tus resultados:

```bash
mkdir -p DataViz-Storytelling/outputs
```

### Tipos de Archivos a Guardar

1. **Gráficos PNG**: Descargados desde los ejercicios interactivos
2. **Resultados CSV/JSON**: Datos procesados y resultados de cuestionarios
3. **Screenshots**: Capturas de pantalla de tus visualizaciones

### Commits Recomendados

```bash
# Después de completar un módulo
git add DataViz-Storytelling/outputs/modulo-01-*
git commit -m "Complete módulo 01: Introducción a Data Visualization"
git push
```

---

## 🧪 Ejercicio Evaluativo Global

El archivo `ejercicio-evaluativo-interactivo.html` en la raíz contiene:

- **40-50 preguntas** cubriendo todos los módulos
- **Scoring automático** 0-100%
- **Guardado en localStorage**
- **Exportación de resultados**

Úsalo al finalizar el curso para evaluar tu aprendizaje global.

---

## 📖 Datasets de Muestra

En `/examples/` encontrarás tres CSV listos para usar:

### `ventas.csv`
Datos de ventas mensuales por producto (Mes, Producto, Ventas, Ingresos)

### `poblacion.csv`
Datos de población y crecimiento por país (Año, País, Población, Crecimiento)

### `tiempos.csv`
Datos de duración de tareas por empleado (Fecha, Tarea, Duración, Empleado)

Puedes usar estos datasets en cualquier ejercicio, o traer tus propios datos en formato CSV.

---

## 🔒 Privacidad y Seguridad

- ✅ **Todo local**: No se envía ningún dato a servidores externos
- ✅ **Sin tracking**: No hay analytics ni cookies de terceros
- ✅ **Código abierto**: Todo el código JavaScript es visible e inspectable
- ✅ **localStorage**: Los datos se quedan en tu navegador

---

## 🎓 Metodología de Aprendizaje

### Antes de Empezar un Módulo
1. Lee el `README.md` del módulo
2. Revisa los objetivos de aprendizaje
3. Prepara tu entorno (navegador abierto, CSV descargados)

### Durante el Módulo
1. Sigue las actividades en `actividad-interactiva.md`
2. Ejecuta el `modulo-XX-ejercicio.html`
3. Experimenta con diferentes configuraciones
4. Responde el cuestionario integrado

### Después del Módulo
1. Descarga tus gráficos y resultados
2. Actualiza `progreso.md` con lo aprendido
3. Escribe retroalimentación en `retroalimentacion.md`
4. Commitea tus evidencias

---

## 📊 Ejemplo Rápido

```html
<!-- Ejemplo mínimo de visualización -->
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>
<body>
    <canvas id="myChart"></canvas>
    <script>
        const ctx = document.getElementById('myChart');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Enero', 'Febrero', 'Marzo'],
                datasets: [{
                    label: 'Ventas',
                    data: [150, 180, 200],
                    backgroundColor: 'rgba(102, 126, 234, 0.8)'
                }]
            }
        });
    </script>
</body>
</html>
```

---

## 🚧 Roadmap del Curso

- [x] Estructura de 10 módulos
- [x] Ejercicios HTML interactivos por módulo
- [x] CSV de muestra
- [x] Utilidades JavaScript compartidas
- [ ] Videos tutoriales (futuro)
- [ ] Más datasets de ejemplo (futuro)
- [ ] Integración con GitHub Actions para CI (futuro)

---

## 🤝 Contribuciones

Este es un curso en evolución. Si encuentras errores o tienes sugerencias:

1. Abre un issue en el repositorio
2. Propone mejoras vía PR
3. Comparte tus visualizaciones creadas con el curso

---

## 📝 Licencia

Este material educativo es de uso libre para aprendizaje personal.

---

**¡Comienza tu viaje en Data Visualization & Storytelling!** 🚀📊

Abre el `modulo-01-introduccion/README.md` para empezar.
