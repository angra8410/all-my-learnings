# Módulo 5: Interactividad y Publicación

## Introducción

¡Casi llegamos! Ahora tus informes cobrarán vida con interactividad y serán compartidos con el mundo. En este módulo aprenderás:

- Crear filtros y slicers efectivos
- Implementar drill-through y drill-down
- Botones y navegación entre páginas
- Bookmarks y storytelling
- Publicar en Power BI Service
- Compartir y colaborar
- Configurar actualizaciones automáticas
- Row-Level Security (RLS)

## ¿Por qué es importante?

Un informe estático es solo una imagen. Un informe interactivo es una herramienta de exploración:

- ✅ Usuarios pueden encontrar sus propias respuestas
- ✅ Reduce solicitudes de "otro informe más"
- ✅ Facilita análisis ad-hoc
- ✅ Aumenta adopción y valor
- ✅ Democratiza el acceso a datos

## Conceptos Principales

### 1. Slicers (Segmentadores)

**¿Qué son?**
Filtros visuales que los usuarios pueden manipular interactivamente.

**Tipos de slicers:**
- **Lista**: Selección múltiple con checkboxes
- **Dropdown**: Ahorra espacio, selección única o múltiple
- **Rango numérico**: Slider para números
- **Rango de fechas**: Calendario entre dos fechas
- **Relativo**: Últimos 7 días, este mes, etc.

**Mejores prácticas:**
- ✅ Coloca slicers en ubicación consistente (típicamente arriba o izquierda)
- ✅ Agrupa slicers relacionados
- ✅ Usa dropdown para ahorrar espacio
- ✅ Sincroniza slicers entre páginas cuando sea relevante

### 2. Drill-Down y Drill-Up

**Drill-Down**: Profundizar en jerarquías
- Año → Trimestre → Mes → Día
- País → Estado → Ciudad

**Cómo habilitar:**
1. Crear jerarquía en modelo
2. Agregar a visual
3. Habilitar iconos de drill en visual

**Drill-Up**: Volver al nivel superior

### 3. Drill-Through

**¿Qué es?**
Navegar a una página de detalles manteniendo el contexto de filtro.

**Ejemplo**: 
- Página 1: Ventas por producto (vista general)
- Click derecho en "Laptop" → Drill-through
- Página 2: Detalles completos de ventas de Laptop

**Cómo configurar:**
1. Crear página de destino
2. Agregar campos a "Drill-through filters"
3. Botón "Back" aparece automáticamente

### 4. Bookmarks (Marcadores)

**¿Qué son?**
Capturan el estado de una página (filtros, visibilidad, selecciones).

**Usos comunes:**
- **Storytelling**: Crear una narrativa guiada
- **Vistas alternativas**: Cambiar entre diferentes perspectivas
- **Limpiar filtros**: Botón "Reset" que restaura estado inicial

**Ejemplo de storytelling:**
1. Bookmark 1: Vista general
2. Bookmark 2: Destaca problema
3. Bookmark 3: Muestra causa raíz
4. Bookmark 4: Presenta solución

### 5. Botones y Navegación

**Tipos de botones:**
- **Navegación**: Ir a otra página
- **Bookmark**: Aplicar un marcador
- **Back**: Regresar
- **Drill-through**: Navegar con filtro
- **Q&A**: Abrir preguntas naturales
- **Web URL**: Abrir enlace externo

**Diseño de botones:**
- ✅ Usa iconos claros
- ✅ Agrega hover effects
- ✅ Mantén estilo consistente
- ✅ Posiciónatenido común (menú superior)

### 6. Power BI Service (Publicación)

**¿Qué es Power BI Service?**
Plataforma en la nube para compartir y colaborar.

**Proceso de publicación:**
1. En Power BI Desktop: Archivo → Publicar
2. Seleccionar workspace
3. Esperar confirmación
4. Abrir en Service para configurar

**Workspaces:**
- **Mi workspace**: Personal, solo tú
- **Workspaces compartidos**: Colaboración en equipo
- **Premium workspaces**: Características empresariales

### 7. Compartir Informes

**Opciones para compartir:**

**A) Compartir directo** (Share)
- Envías link a usuarios específicos
- Requieren licencia Pro
- Control de permisos

**B) Publicar en web** (Publish to web)
- ⚠️ PÚBLICO en internet
- No requiere login
- ⚠️ Solo usar para datos no sensibles

**C) Exportar a PDF/PowerPoint**
- Snapshot estático
- No interactivo
- Útil para presentaciones

**D) Integrar (Embed)**
- En SharePoint, Teams, sitio web
- Mantiene interactividad
- Requiere permisos apropiados

**E) Aplicaciones (Apps)**
- Experiencia curada
- Para distribución masiva
- Actualización centralizada

### 8. Actualizaciones Programadas

**¿Por qué?**
Mantener datos frescos automáticamente.

**Requisitos:**
- Power BI Pro/Premium
- Gateway (para datos on-premise)
- Credenciales configuradas

**Configuración:**
1. En dataset: Settings → Scheduled refresh
2. Configurar frecuencia (hasta 8 veces/día en Pro)
3. Configurar credenciales de fuente de datos
4. Habilitar notificaciones de error

### 9. Row-Level Security (RLS)

**¿Qué es?**
Filtrar datos por usuario automáticamente.

**Ejemplo**: 
- Gerente región Norte solo ve ventas del Norte
- Gerente región Sur solo ve ventas del Sur

**Cómo implementar:**
```DAX
// En tabla Ventas
[Región] = USERNAME()

// O más sofisticado con tabla de usuarios
[Región] IN VALUES(Usuarios[Región])
```

**Pasos:**
1. Modeling → Manage Roles
2. Crear rol y DAX filter
3. Publicar
4. En Service: Asignar usuarios a roles

## Mejores Prácticas

### ✅ Interactividad
- Usa slicers para filtros frecuentes
- Implementa drill-through para detalles
- Agrega tooltips informativos
- Crea navegación intuitiva
- Incluye botón "Reset filters"

### ✅ Publicación
- Organiza en workspaces lógicos
- Usa nombres descriptivos
- Configura actualización automática
- Documenta datasets
- Implementa RLS si es necesario

### ❌ Evitar
- Demasiados slicers (sobrecarga)
- Navegación confusa
- Olvidar configurar actualizaciones
- Compartir datos sensibles públicamente
- No testear RLS antes de publicar

## Implementación Práctica

### Ejercicio 1: Diseña navegación

**Escenario**: Dashboard de 3 páginas

**Páginas:**
1. Overview (general)
2. Ventas (detalle)
3. Productos (análisis)

**Diseña la navegación:**
_______________________________________________
_______________________________________________

### Ejercicio 2: Crea historia con bookmarks

**Tema**: Análisis de caída de ventas

**Bookmark 1** (Setup): _______________________________________________
**Bookmark 2** (Problema): _______________________________________________
**Bookmark 3** (Causa): _______________________________________________
**Bookmark 4** (Solución): _______________________________________________

## Conceptos Clave

🎯 **Slicers** = Filtros interactivos para usuarios

🔍 **Drill-through** = Navegar a detalles manteniendo contexto

📖 **Bookmarks** = Capturar estados para storytelling

🔘 **Botones** = Navegación y acciones

☁️ **Power BI Service** = Plataforma de publicación y colaboración

🔄 **Actualización automática** = Datos siempre frescos

🔒 **RLS** = Seguridad a nivel de fila

## Próximos Pasos

En el **Módulo 6: Data Storytelling y Casos Prácticos**, aprenderás a:
- Contar historias efectivas con datos
- Principios de storytelling
- Casos prácticos reales
- Proyecto final integrador
- Mejores prácticas end-to-end

**Recursos:**
- 📚 Documentación Power BI Service
- 🎥 Tutoriales de publicación
- 🌐 Comunidad Power BI
- 🛠️ Power BI Gateway

## Motivación Final

> "Un dashboard compartido vale más que mil dashboards en tu computadora." - Anónimo

Has llegado muy lejos. Ya sabes modelar datos, crear medidas DAX y diseñar visualizaciones. Ahora es momento de compartir tu trabajo con el mundo.

**Publicar tu primer informe es un hito importante.** Disfrútalo.

---

**Tiempo estimado**: 4-5 horas  
**Dificultad**: Intermedio ⭐⭐⭐☆☆  
**Prerrequisitos**: Módulos 1-4, Power BI Pro (para publicar)
