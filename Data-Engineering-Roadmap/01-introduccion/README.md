# 🚀 Módulo 01 — Introducción a Data Engineering

## 🎯 Objetivos de Aprendizaje

Al completar este módulo serás capaz de:

1. **Comprender el rol del Data Engineer** y cómo encaja en el ecosistema de datos moderno
2. **Configurar un entorno de desarrollo profesional** con Git, Docker y VSCode
3. **Entender el ciclo de vida completo de los datos** desde la ingesta hasta el consumo
4. **Identificar las herramientas clave** del stack moderno de Data Engineering
5. **Ejecutar tu primer contenedor Docker** con PostgreSQL funcionando

## 📚 Contenido Teórico

### 1. ¿Qué hace un Data Engineer?

Un Data Engineer es el arquitecto de la infraestructura de datos. Sus responsabilidades incluyen:

- **Construcción de pipelines de datos**: Diseñar y mantener sistemas que mueven datos desde fuentes (APIs, bases de datos, archivos) hacia destinos (data warehouses, data lakes)
- **Garantizar calidad y confiabilidad**: Implementar validaciones, tests y monitoreo
- **Optimización de rendimiento**: Diseñar soluciones escalables que manejen grandes volúmenes
- **Colaboración multifuncional**: Trabajar con Data Scientists, Analytics Engineers y stakeholders de negocio

**Diferencias clave con otros roles:**

| Rol | Enfoque Principal |
|-----|------------------|
| **Data Engineer** | Infraestructura, pipelines, ETL/ELT |
| **Data Scientist** | Modelos ML, análisis estadístico |
| **Analytics Engineer** | Transformaciones de datos, métricas de negocio |
| **Data Analyst** | Reportes, dashboards, insights de negocio |

### 2. Ciclo de Vida de los Datos

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐     ┌──────────┐
│  Ingesta    │ --> │Almacenamiento│ --> │ Transformación  │ --> │ Consumo  │
│             │     │              │     │                 │     │          │
│ APIs        │     │ Data Lake    │     │ dbt, Airflow    │     │ BI Tools │
│ Databases   │     │ Data Warehouse│     │ Python, SQL     │     │ ML Models│
│ Files (CSV) │     │ (Snowflake)  │     │                 │     │ APIs     │
└─────────────┘     └──────────────┘     └─────────────────┘     └──────────┘
```

**Etapas detalladas:**

1. **Ingesta**: Extracción de datos desde múltiples fuentes
   - Batch (diario, horario) vs Streaming (tiempo real)
   - Conectores, APIs, webhooks

2. **Almacenamiento**: Guardar datos raw y procesados
   - Data Lakes (S3, Azure Blob): datos crudos, schema-on-read
   - Data Warehouses (Snowflake, BigQuery): datos estructurados, optimizados para consultas

3. **Transformación**: Limpiar, enriquecer, agregar
   - ELT moderno: Extract → Load → Transform (en warehouse)
   - Herramientas: dbt, Spark, Python

4. **Consumo**: Entrega de datos a usuarios finales
   - Dashboards (Tableau, Power BI, Looker)
   - APIs de datos
   - Modelos de ML

### 3. Herramientas Clave del Curso

Este roadmap cubre el stack moderno de Data Engineering:

**Lenguajes:**
- 🐍 **Python**: Scripting, ETL, automatización
- 📊 **SQL**: Consultas, transformaciones, análisis

**Orquestación:**
- 🔀 **Apache Airflow**: Scheduling y gestión de workflows

**Transformación:**
- 🎨 **dbt (data build tool)**: Transformaciones versionadas, testing

**Almacenamiento:**
- ❄️ **Snowflake**: Data Warehouse cloud moderno
- 🐘 **PostgreSQL**: Base de datos relacional para desarrollo

**Infraestructura:**
- 🐳 **Docker**: Contenedores para desarrollo local
- ☁️ **Cloud platforms**: AWS, Azure, GCP

**Control de versiones:**
- 🌿 **Git/GitHub**: Versionado de código y colaboración

### 4. Configuración del Entorno

#### 4.1 Requisitos del Sistema

- **Sistema Operativo**: Windows 10/11, macOS, Linux
- **RAM**: Mínimo 8GB (recomendado 16GB)
- **Espacio en disco**: 20GB libres
- **Conexión a internet**: Para descargas y cloud services

#### 4.2 Instalaciones Necesarias

**A. Git**
- Windows: [Git for Windows](https://git-scm.com/download/win)
- macOS: `brew install git` o Xcode Command Line Tools
- Linux: `sudo apt-get install git`

**B. VSCode (Editor recomendado)**
- Descarga: https://code.visualstudio.com/
- Extensiones útiles:
  - Python
  - Docker
  - GitLens
  - SQL Tools
  - YAML

**C. Docker Desktop**
- Descarga: https://www.docker.com/products/docker-desktop
- Verifica instalación: `docker --version`

**D. Python 3.9+**
- Descarga: https://www.python.org/downloads/
- Verifica: `python --version`

#### 4.3 Configuración de Git

```bash
# Configurar nombre y email
git config --global user.name "Tu Nombre"
git config --global user.email "tu-email@ejemplo.com"

# Verificar configuración
git config --list
```

### 5. Cómo Seguir el Plan de Estudio

#### Metodología de Aprendizaje

1. **Lee el README completo** del módulo antes de comenzar
2. **Completa las actividades interactivas** paso a paso
3. **Marca tu progreso** en `progreso.md` regularmente
4. **Consulta recursos adicionales** en `recursos.md` cuando necesites profundizar
5. **Autoevalúate** con los criterios de `retroalimentacion.md`

#### Estimación de Tiempo

- **Lectura de teoría**: 1-1.5 horas
- **Actividades prácticas**: 2-3 horas
- **Exploración adicional**: 1-2 horas opcionales

**Total: 4-6 horas**

#### Estrategia de Éxito

✅ **Practica activamente**: No solo leas, ejecuta cada comando  
✅ **Documenta tu aprendizaje**: Toma notas, captura errores y soluciones  
✅ **Experimenta**: Modifica comandos, prueba variaciones  
✅ **Comparte**: Explica conceptos a otros (rubber duck debugging)  
✅ **Sé paciente**: La curva de aprendizaje inicial es empinada pero vale la pena

## 🏋️ Actividades Prácticas

### Actividad 1: Clonar el Repositorio
```bash
git clone https://github.com/angra8410/all-my-learnings.git
cd all-my-learnings/Data-Engineering-Roadmap
```

### Actividad 2: Crear Rama de Trabajo Personal
```bash
git checkout -b feature/mi-progreso-data-eng
```

### Actividad 3: Ejecutar PostgreSQL en Docker
```bash
docker run --name postgres-local \
  -e POSTGRES_PASSWORD=mypassword \
  -e POSTGRES_USER=dataeng \
  -e POSTGRES_DB=learning_db \
  -p 5432:5432 \
  -d postgres:13

# Verificar que está corriendo
docker ps
```

### Actividad 4: Conectarse a PostgreSQL
```bash
docker exec -it postgres-local psql -U dataeng -d learning_db
```

### Actividad 5: Personalizar `progreso.md`
Crea tu plan personal basado en tu disponibilidad semanal.

## 📝 Entregables

Al finalizar este módulo deberías tener:

1. ✅ Entorno completo configurado (Git, Docker, VSCode)
2. ✅ Repositorio clonado y rama personal creada
3. ✅ PostgreSQL corriendo en Docker
4. ✅ Conexión exitosa a la base de datos
5. ✅ Plan personal de estudio definido

## 🎯 Criterios de Éxito

- [ ] Todos los comandos de instalación ejecutados sin errores
- [ ] `docker ps` muestra el contenedor PostgreSQL en estado "Up"
- [ ] Conexión exitosa a PostgreSQL mediante `psql`
- [ ] Commits iniciales realizados en tu rama personal
- [ ] `progreso.md` personalizado con tu plan semanal

## 📚 Recursos Adicionales

Ver archivo `recursos.md` para:
- Guías detalladas de instalación por sistema operativo
- Troubleshooting común de Docker
- Tutoriales de Git para principiantes
- Configuración avanzada de VSCode

## ⏭️ Siguiente Paso

Una vez completado este módulo, estarás listo para **Módulo 02: SQL para Data Engineering**, donde aprenderás consultas avanzadas, optimización y operaciones críticas para pipelines de datos.

---

**💡 Consejo**: Si encuentras problemas durante la configuración, revisa `recursos.md` o consulta la documentación oficial de cada herramienta. ¡La configuración inicial es la parte más desafiante, pero solo la haces una vez!