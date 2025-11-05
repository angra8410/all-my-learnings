# 🎮 Actividad Interactiva 01: Configuración y Preparación del Entorno PL-300

## 🎯 Objetivo

Configurar completamente tu entorno de desarrollo y aprendizaje para la certificación PL-300, verificando que todos los componentes estén instalados y funcionando correctamente. Al finalizar, tendrás Power BI Desktop, Power BI Service, y herramientas complementarias listas para comenzar tu preparación.

**Duración total estimada**: 90-120 minutos

---

## 📋 Ejercicio 1: Instalación de Power BI Desktop (20 minutos)

### 🎯 Objetivo
Instalar la versión más reciente de Power BI Desktop y verificar su funcionamiento.

### 📝 Pasos

1. **Descargar Power BI Desktop**
   - Navegar a: https://powerbi.microsoft.com/desktop
   - Hacer clic en "Descargar gratis" o "Download free"
   - Elegir opción de descarga (Microsoft Store recomendado para actualizaciones automáticas)

2. **Ejecutar el instalador**
   ```
   Opción A (Microsoft Store):
   - Abrir Microsoft Store
   - Buscar "Power BI Desktop"
   - Clic en "Obtener" o "Get"
   
   Opción B (Instalador .exe):
   - Ejecutar PBIDesktopSetup_x64.exe
   - Aceptar términos y condiciones
   - Seleccionar idioma de preferencia
   - Completar instalación
   ```

3. **Verificar instalación**
   - Abrir Power BI Desktop desde el menú inicio
   - Verificar que carga correctamente
   - Anotar versión instalada

### ✅ Comprobación

**Versión de Power BI Desktop instalada**: ___________________________

**Fecha de la versión**: ___________________________

**Idioma de la interfaz**: ___________________________

¿Se abrió correctamente la aplicación? ⬜ Sí ⬜ No

Si hubo problemas, describe: ___________________________

---

## 📋 Ejercicio 2: Configuración de Power BI Service (25 minutos)

### 🎯 Objetivo
Crear y configurar cuenta en Power BI Service para publicación y colaboración.

### 📝 Pasos

1. **Crear cuenta de Power BI Service**
   - Navegar a: https://app.powerbi.com
   - Clic en "Probar gratis" o "Try for free"
   - Ingresar correo electrónico corporativo o crear cuenta Microsoft personal
   - Completar el proceso de registro

2. **Explorar la interfaz**
   ```
   Elementos a identificar:
   - Panel de navegación izquierdo
   - Home / Inicio
   - Workspace / Área de trabajo
   - Botón "Create" / "Crear"
   - Configuración de perfil
   ```

3. **Crear tu primer Workspace**
   - En el panel izquierdo, clic en "Workspaces"
   - Clic en "+ New workspace" / "+ Nueva área de trabajo"
   - Nombre sugerido: "PL-300-Practica"
   - Dejar configuración por defecto
   - Crear workspace

4. **Verificar tipo de licencia**
   - Ir a Settings (ícono de engranaje) > Admin portal (si disponible) o Settings
   - Verificar tipo de licencia (Free, Pro, Premium)

### ✅ Comprobación

**Email de cuenta Power BI**: ___________________________

**Tipo de licencia**: ⬜ Free ⬜ Pro ⬜ Premium ⬜ Premium Per User

**Nombre del Workspace creado**: ___________________________

**Workspace ID** (Configuración > Details): ___________________________

¿Puedes acceder correctamente al servicio? ⬜ Sí ⬜ No

**Nota**: Si tienes licencia Free, considera upgrade a Pro Trial (60 días gratis) para funcionalidades completas.

---

## 📋 Ejercicio 3: Verificación de Requisitos del Sistema (15 minutos)

### 🎯 Objetivo
Confirmar que tu equipo cumple con los requisitos técnicos para ejecutar Power BI Desktop eficientemente.

### 📝 Pasos

1. **Verificar versión de Windows**
   ```powershell
   # Ejecutar en PowerShell
   systeminfo | findstr /C:"OS Name" /C:"OS Version"
   ```
   
   **Resultado esperado**: Windows 10 versión 14393.0 o superior, o Windows 11

2. **Verificar arquitectura del procesador**
   ```powershell
   # Ejecutar en PowerShell
   wmic cpu get Name, DataWidth, NumberOfCores
   ```
   
   **Resultado esperado**: DataWidth = 64, NumberOfCores >= 2

3. **Verificar RAM disponible**
   ```powershell
   # Ejecutar en PowerShell
   systeminfo | findstr /C:"Total Physical Memory"
   ```
   
   **Resultado esperado**: Mínimo 4 GB, recomendado 8 GB o más

4. **Verificar espacio en disco**
   ```powershell
   # Ejecutar en PowerShell
   Get-PSDrive C | Select-Object Used,Free
   ```
   
   **Resultado esperado**: Al menos 10 GB libres

### ✅ Comprobación

**Sistema Operativo**: ___________________________

**Versión**: ___________________________

**Arquitectura del procesador**: ___________________________

**Número de núcleos**: ___________________________

**RAM total**: ___________________________ GB

**Espacio libre en disco C:**: ___________________________ GB

¿Tu sistema cumple los requisitos mínimos? ⬜ Sí ⬜ No

---

## 📋 Ejercicio 4: Instalación de Herramientas Complementarias (30 minutos)

### 🎯 Objetivo
Instalar herramientas adicionales que facilitarán el desarrollo y optimización en Power BI.

### 📝 Pasos

1. **Instalar DAX Studio** (recomendado)
   - Descargar desde: https://daxstudio.org/
   - Ejecutar instalador DaxStudio_x_x_x_setup.exe
   - Completar instalación con opciones por defecto
   
   **Uso**: Análisis de rendimiento de DAX, query optimization

2. **Instalar Tabular Editor 2** (opcional - versión gratuita)
   - Descargar desde: https://github.com/TabularEditor/TabularEditor/releases
   - Extraer archivo .zip
   - Ejecutar TabularEditor.exe (portable, no requiere instalación)
   
   **Uso**: Edición avanzada de modelos tabulares, scripting

3. **Instalar Power BI Report Builder** (opcional)
   - Descargar desde: https://www.microsoft.com/download/details.aspx?id=58158
   - Ejecutar instalador
   - Útil para informes paginados (no cubierto en PL-300 pero útil conocer)

4. **Configurar SQL Server Management Studio** (opcional, si tienes experiencia con SQL)
   - Descargar desde: https://learn.microsoft.com/sql/ssms/download-sql-server-management-studio-ssms
   - Útil para conexiones directas a bases de datos

### ✅ Comprobación

**DAX Studio instalado**: ⬜ Sí ⬜ No (Si Sí, versión: _______________)

**Tabular Editor descargado**: ⬜ Sí ⬜ No

**Power BI Report Builder instalado**: ⬜ Sí ⬜ No

**SSMS instalado**: ⬜ Sí ⬜ No (Si Sí, versión: _______________)

---

## 📋 Ejercicio 5: Primer Reporte en Power BI Desktop (20 minutos)

### 🎯 Objetivo
Crear tu primer reporte básico para confirmar que Power BI Desktop funciona correctamente.

### 📝 Pasos

1. **Crear nuevo reporte**
   - Abrir Power BI Desktop
   - Clic en "Obtener datos" / "Get data"
   - Seleccionar "Muestra" / "Sample" > "Financial Sample"
   - Clic en "Cargar" / "Load"

2. **Crear visualización simple**
   - En el panel de visualizaciones, seleccionar "Gráfico de columnas agrupadas"
   - Arrastrar campo "Country" a Axis/Eje
   - Arrastrar campo "Sales" a Values/Valores
   - Aplicar formato básico (título, colores)

3. **Guardar reporte**
   ```
   Archivo > Guardar como
   Nombre: "PL-300_Verificacion_Entorno.pbix"
   Ubicación: Crear carpeta "PL-300-Practicas" en Documentos
   ```

4. **Publicar a Power BI Service** (si tienes licencia Pro)
   - Clic en "Publicar" / "Publish" en la cinta
   - Seleccionar workspace "PL-300-Practica" creado anteriormente
   - Esperar confirmación de publicación
   - Clic en "Abrir en Power BI" para verificar

### ✅ Comprobación

**Archivo .pbix creado**: ⬜ Sí ⬜ No

**Ruta completa del archivo**: ___________________________

**Número de visualizaciones creadas**: ___________________________

**Publicado correctamente a Power BI Service**: ⬜ Sí ⬜ No ⬜ N/A (no tengo Pro)

**URL del reporte en servicio** (si aplica): ___________________________

---

## 📋 Ejercicio 6: Acceso a Recursos de Microsoft Learn (15 minutos)

### 🎯 Objetivo
Registrarte en Microsoft Learn y comenzar el Learning Path oficial de PL-300.

### 📝 Pasos

1. **Crear perfil en Microsoft Learn**
   - Navegar a: https://learn.microsoft.com
   - Iniciar sesión con cuenta Microsoft (la misma de Power BI Service recomendado)
   - Completar perfil básico

2. **Acceder al Learning Path de PL-300**
   - Buscar "PL-300" o "Power BI Data Analyst"
   - URL directa: https://learn.microsoft.com/training/browse/?roles=data-analyst&products=power-bi
   - Guardar en marcadores

3. **Iniciar primer módulo de Microsoft Learn**
   - Seleccionar "Get started with Microsoft data analytics"
   - Comenzar primer unit
   - Marcar como completado

4. **Explorar Practice Assessment**
   - Navegar a: https://learn.microsoft.com/certifications/exams/pl-300/practice/assessment
   - Revisar formato de preguntas (no tomar todavía)
   - Guardar enlace para uso posterior

### ✅ Comprobación

**Perfil de Microsoft Learn creado**: ⬜ Sí ⬜ No

**Nombre de usuario/Display name**: ___________________________

**Learning Path de PL-300 encontrado**: ⬜ Sí ⬜ No

**Primer módulo iniciado**: ⬜ Sí ⬜ No

**Practice Assessment accedido**: ⬜ Sí ⬜ No

---

## 📋 Ejercicio 7: Planificación Personalizada de Estudio (20 minutos)

### 🎯 Objetivo
Crear tu calendario personalizado de estudio basado en tu disponibilidad y objetivos.

### 📝 Pasos

1. **Definir fecha objetivo para el examen**
   - Considerar: 8-12 semanas desde hoy para ritmo moderado
   - Verificar disponibilidad de fechas en Pearson VUE
   
   **Fecha objetivo del examen**: _____ / _____ / _____

2. **Calcular horas disponibles por semana**
   ```
   Días laborales (L-V): ____ horas/día x ____ días = ____ horas
   Fines de semana (S-D): ____ horas/día x ____ días = ____ horas
   Total semanal: ____ horas
   ```

3. **Distribuir módulos en calendario**
   ```
   Semana 1-2: Módulo 01 + Módulo 02 (inicio)
   Semana 3-4: Módulo 02 (completar) + Módulo 03 (inicio)
   Semana 5-6: Módulo 03 (completar) + Módulo 04
   Semana 7-8: Módulo 05 + Módulo 06 (inicio)
   Semana 9-10: Módulo 06 (simulacros) + repaso
   Semana 11-12: Módulo 07 (opcional) + examen
   ```

4. **Definir horarios específicos de estudio**
   ```
   Ejemplo:
   Lunes a Viernes: 7:00 PM - 8:30 PM (1.5 hrs)
   Sábados: 10:00 AM - 1:00 PM (3 hrs)
   Domingos: 4:00 PM - 7:00 PM (3 hrs)
   ```
   
   **Tus horarios**: 
   - Días laborales: ___________________________
   - Fines de semana: ___________________________

5. **Configurar recordatorios**
   - Crear eventos recurrentes en calendario (Google Calendar, Outlook)
   - Configurar alarmas 15 minutos antes
   - Bloquear tiempo como "ocupado"

### ✅ Comprobación

**Fecha objetivo examen definida**: ⬜ Sí ⬜ No

**Horas totales disponibles por semana**: ___________________________ horas

**Calendario de estudio creado**: ⬜ Sí ⬜ No

**Recordatorios configurados**: ⬜ Sí ⬜ No

**Ritmo seleccionado**: ⬜ Intensivo (4-6 sem) ⬜ Moderado (8-10 sem) ⬜ Relajado (12-16 sem)

---

## 📋 Ejercicio 8: Familiarización con Exam Sandbox (15 minutos)

### 🎯 Objetivo
Explorar la interfaz de examen de Microsoft para reducir ansiedad el día del examen real.

### 📝 Pasos

1. **Acceder al Exam Sandbox**
   - Navegar a: https://aka.ms/examdemo
   - Seleccionar cualquier examen de demostración (todos tienen misma interfaz)

2. **Explorar elementos de la interfaz**
   ```
   - Temporizador en esquina superior
   - Navegación entre preguntas (Anterior/Siguiente)
   - Botón "Marcar para revisión"
   - Panel de resumen de preguntas
   - Botón "Finalizar examen"
   - Calculadora (si disponible)
   ```

3. **Practicar tipos de preguntas**
   - Responder al menos 5 preguntas de diferentes tipos
   - Practicar marcar preguntas para revisión
   - Usar el panel de resumen
   - Completar el "examen" de práctica

4. **Identificar características importantes**
   - ¿Puedes volver a preguntas anteriores? ___________
   - ¿Cuánto tiempo hay para revisar? ___________
   - ¿Hay penalización por respuestas incorrectas? ___________

### ✅ Comprobación

**Exam Sandbox accedido**: ⬜ Sí ⬜ No

**Tipos de preguntas practicados**:
- ⬜ Opción múltiple simple
- ⬜ Opción múltiple compuesta
- ⬜ Arrastrar y soltar
- ⬜ Case study
- ⬜ Simulación activa

**Nivel de comodidad con interfaz**: ⬜ Bajo ⬜ Medio ⬜ Alto

**Notas sobre la experiencia**: ___________________________

---

## 📊 Resumen de Tiempo

| Ejercicio | Duración Estimada | Duración Real |
|-----------|-------------------|---------------|
| 1. Instalación Power BI Desktop | 20 min | _______ min |
| 2. Configuración Power BI Service | 25 min | _______ min |
| 3. Verificación de Sistema | 15 min | _______ min |
| 4. Herramientas Complementarias | 30 min | _______ min |
| 5. Primer Reporte | 20 min | _______ min |
| 6. Microsoft Learn | 15 min | _______ min |
| 7. Planificación de Estudio | 20 min | _______ min |
| 8. Exam Sandbox | 15 min | _______ min |
| **TOTAL** | **160 min (2.7 hrs)** | **_______ min** |

---

## ✅ Checklist Final de Verificación

Antes de continuar al Módulo 02, confirma que has completado:

### Software y Cuentas
- [ ] Power BI Desktop instalado y funcionando
- [ ] Cuenta de Power BI Service creada
- [ ] Workspace de práctica creado en Power BI Service
- [ ] DAX Studio instalado (recomendado)
- [ ] Perfil de Microsoft Learn creado

### Verificaciones Técnicas
- [ ] Sistema cumple requisitos mínimos
- [ ] Primer reporte .pbix creado y guardado
- [ ] Reporte publicado a Power BI Service (si tienes Pro)
- [ ] Acceso verificado a recursos de Microsoft Learn

### Planificación
- [ ] Fecha objetivo de examen definida
- [ ] Calendario de estudio personalizado creado
- [ ] Recordatorios configurados
- [ ] Familiarizado con interfaz del examen (Exam Sandbox)

### Recursos Marcados
- [ ] Documentación oficial de Power BI
- [ ] Learning Path PL-300 en Microsoft Learn
- [ ] Exam Sandbox
- [ ] Practice Assessment
- [ ] Comunidades de soporte (Community, Reddit, Stack Overflow)

---

## 🎯 Criterios de Éxito

Has completado exitosamente este módulo si:

✅ Tienes Power BI Desktop y Service configurados y funcionando  
✅ Creaste y publicaste tu primer reporte básico  
✅ Tienes un plan de estudio personalizado con fechas específicas  
✅ Conoces la estructura del examen y la interfaz  
✅ Tienes acceso a todos los recursos oficiales de Microsoft  

---

## 📝 Notas y Observaciones

Espacio para tus notas personales sobre la configuración:

_______________________________________________

_______________________________________________

_______________________________________________

_______________________________________________

_______________________________________________

---

## 🚀 Siguiente Paso

¡Felicitaciones! Tu entorno está listo. Actualiza tu archivo `progreso.md` y continúa con:

**[Módulo 02: Prepare the Data →](../02-prepare-data/README.md)**

---

**Tiempo total**: 90-120 minutos  
**Dificultad**: ⭐ Básico  
**Última actualización**: Noviembre 2025
