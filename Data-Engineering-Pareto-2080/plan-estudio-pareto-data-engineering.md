# 🎯 Plan de Estudio — Data Engineering Pareto 20/80 (Projects-First)

## Resumen Ejecutivo

Este curso práctico sigue el **principio de Pareto**: identifica el **20% de conocimientos** que generan el **80% del impacto** profesional en Data Engineering. Prioriza proyectos reales, ejercicios verificables y herramientas de producción: **SQL, ETL, Testing, Spark (Scala), Databricks, Airflow y GitHub**.

**Nivel:** Principiante a Intermedio  
**Duración:** 10-12 semanas (12-15 horas/semana)  
**Modalidad:** Auto-guiado, projects-first, verificable  
**Proyecto Final:** Pipeline end-to-end con orquestación Airflow

---

## 🎯 Objetivos de Aprendizaje

Al completar este roadmap dominarás el **20% crítico** que te hace job-ready:

1. **SQL avanzado**: JOINs, window functions, MERGE/UPSERT, deduplicación
2. **ETL idempotente**: cargas incrementales, particionado, manejo de errores
3. **Spark (Scala)**: transformaciones DataFrame, escritura particionada, optimización
4. **Databricks**: notebooks, jobs, cluster config, Delta Lake
5. **Airflow**: diseño de DAGs, retries, backfills, parametrización
6. **Testing**: row counts, uniqueness, null checks, smoke tests end-to-end
7. **GitHub**: versionado de código, CI/CD básico para pipelines

---

## 🧠 Principio Pareto Aplicado

### 20% de Conocimientos (High-Impact Core)

**SQL:**
- JOINs (INNER, LEFT, FULL OUTER)
- Window functions (ROW_NUMBER, RANK, LAG/LEAD)
- GROUP BY agregaciones
- MERGE/UPSERT statements
- CTEs (Common Table Expressions)

**ETL:**
- Cargas incrementales idempotentes
- Particionado por fecha/región
- Deduplicación (ROW_NUMBER, QUALIFY)
- Manejo de errores y reintentos

**Spark/Scala:**
- DataFrame transforms (select, filter, groupBy, join)
- Escritura particionada (partitionBy)
- Evitar collect(), preferir actions eficientes
- mapPartitions para transformaciones complejas

**Orquestación:**
- Diseño de DAGs con dependencias
- Retries y backfills
- Parametrización (variables, Jinja templates)
- Sensores para esperar datos

**Testing:**
- Row counts esperados
- Checks de unicidad (PRIMARY KEY)
- Validación NOT NULL
- Smoke test end-to-end

### 80% de Práctica (Projects & Repetition)

- **Repetir el mismo pipeline con 3 datasets diferentes** (reinforcement)
- **Build incrementales diarios** (misma lógica, distintas fechas)
- **Refactoring de código** (mejorar pipeline existente)
- **Debugging sessions** (arreglar pipelines rotos)
- **Code reviews** (evaluar código de ejemplo)

---

## 📚 Estructura del Curso (12 Módulos)

### **Módulo 00: Plan & Setup**
- 🎯 Configuración del entorno (Docker, Git, Databricks Community)
- 🛠️ Herramientas: Spark local, Airflow, PostgreSQL
- 📊 Datasets de práctica (CSV, API)
- ⏱️ Duración: 3-4 horas

### **Módulo 01: Introducción al Pareto 20/80**
- 🎯 Qué enfocar y cómo estudiar
- 🎯 Metodología projects-first
- 🎯 Roadmap de carrera Data Engineer
- ⏱️ Duración: 2 horas

### **Módulo 02: SQL Core**
- 🎯 JOINs, window functions, GROUP BY
- 🎯 MERGE/UPSERT, deduplicación
- 📦 **Proyecto:** Set de reporting queries sobre ventas
- ⏱️ Duración: 10-12 horas

### **Módulo 03: Python ETL Basics**
- 🎯 Ingesta desde CSV y APIs
- 🎯 pandas transformations, write to PostgreSQL
- 📦 **Proyecto:** ETL simple con validaciones
- ⏱️ Duración: 8-10 horas

### **Módulo 04: Spark Scala Fundamentals**
- 🎯 DataFrame API, transformaciones, actions
- 🎯 Particionado, escritura eficiente
- 📦 **Proyecto:** Job Spark para limpieza y particionado
- ⏱️ Duración: 12-15 horas

### **Módulo 05: Databricks Workflow**
- 🎯 Notebooks, jobs, cluster config
- 🎯 Integración con Git
- 📦 **Proyecto:** Job productivo en Databricks
- ⏱️ Duración: 8-10 horas

### **Módulo 06: Delta Lake & Storage**
- 🎯 ACID, upserts, time travel
- 🎯 Optimización (OPTIMIZE, Z-ORDER)
- 📦 **Proyecto:** Tabla Delta con SCD Type 2
- ⏱️ Duración: 8-10 horas

### **Módulo 07: DBT or Transforms**
- 🎯 Modelos SQL sobre Delta
- 🎯 Testing integrado, documentación
- 📦 **Proyecto:** Data mart dimensional con dbt
- ⏱️ Duración: 10-12 horas

### **Módulo 08: Airflow Orchestration**
- 🎯 DAGs, operators, sensores
- 🎯 Scheduling, retries, backfills
- 📦 **Proyecto:** DAG orquestando pipeline completo
- ⏱️ Duración: 12-15 horas

### **Módulo 09: Testing & Data Quality**
- 🎯 Great Expectations / SQL checks
- 🎯 Tests unitarios, integración
- 📦 **Proyecto:** Suite de tests para pipeline
- ⏱️ Duración: 8-10 horas

### **Módulo 10: Observability & Cost**
- 🎯 Logging estructurado, métricas
- 🎯 Monitoreo de SLAs
- 📦 **Proyecto:** Dashboard de monitoreo
- ⏱️ Duración: 6-8 horas

### **Módulo 11: Security & Governance**
- 🎯 Manejo de secretos (Vault, GitHub Secrets)
- 🎯 RLS (Row-Level Security), encriptación
- 📦 **Proyecto:** Pipeline con credenciales seguras
- ⏱️ Duración: 4-6 horas

### **Módulo 12: Final Project**
- 🎯 **End-to-end pipeline integrador:**
  - Ingesta: CSV + API → raw landing
  - Transform: Spark (Scala) → Delta tables
  - Warehouse: dbt models → analytical tables
  - Orchestration: Airflow DAG
  - Testing: Great Expectations
  - Monitoring: logs & metrics
- 📦 **Entregables:** código en GitHub, documentación, presentación
- ⏱️ Duración: 20-25 horas

---

## 📁 Formato de cada Módulo

Cada módulo contiene **5 archivos estandarizados**:

1. **README.md**: objetivos, teoría, actividades, entregables
2. **actividad-interactiva.md**: ejercicios con comandos verificables, campos para respuestas, duraciones
3. **progreso.md**: checklist de avance
4. **retroalimentacion.md**: rúbrica de evaluación con porcentajes
5. **recursos.md**: datasets, links, snippets de código

---

## 🛠️ Prerequisitos

### Conocimientos Previos
- ✅ Programación básica (Python o Java/Scala deseable)
- ✅ SQL básico (SELECT, WHERE, JOINs simples)
- ✅ Línea de comandos (bash, terminal)
- ✅ Git básico (clone, commit, push)

### Herramientas Necesarias
- 💻 Laptop con 8GB RAM mínimo (16GB recomendado)
- 🐳 Docker Desktop
- 🔧 Git + GitHub account
- 📝 VSCode (o IntelliJ IDEA para Scala)
- ☁️ Databricks Community Edition (gratis)
- 🐘 PostgreSQL (via Docker)

---

## 🚀 Cómo Usar este Roadmap

### Paso 1: Configuración Inicial
```bash
# Clonar el repositorio
git clone https://github.com/angra8410/all-my-learnings.git
cd all-my-learnings/Data-Engineering-Pareto-2080

# Crear rama de trabajo personal
git checkout -b feature/mi-progreso-pareto
```

### Paso 2: Seguir Orden Secuencial
1. Lee **README.md** del módulo
2. Completa **actividad-interactiva.md** (hands-on)
3. Marca **progreso.md**
4. Autoevalúate con **retroalimentacion.md**
5. Profundiza con **recursos.md**

### Paso 3: Ritmo Recomendado
- **Intensivo:** 2 módulos/semana (25+ horas/semana) → 6 semanas
- **Regular:** 1.5 módulos/semana (15-20 horas/semana) → 8 semanas
- **Part-time:** 1 módulo/semana (12-15 horas/semana) → 12 semanas

---

## 🎯 Acceptance Criteria (Course Complete Checklist)

### Module Structure
- [ ] 13 módulos creados (00-12)
- [ ] Cada módulo tiene los 5 archivos (README, actividad, progreso, retroalimentacion, recursos)
- [ ] Ningún archivo está vacío

### Content Quality
- [ ] Cada `actividad-interactiva.md` contiene comandos verificables
- [ ] Cada ejercicio tiene campos para respuestas (__________) y verificación
- [ ] Al menos 6 mini-proyectos + 1 proyecto final

### Helper Artifacts
- [ ] Airflow DAG skeleton (Python)
- [ ] Spark Scala job example
- [ ] SQL DDL examples (fact/dimension tables)
- [ ] SQL test examples (uniqueness, not_null)
- [ ] Databricks CLI commands

### Projects
- [ ] Module 02: SQL reporting queries
- [ ] Module 03: Python ETL pipeline
- [ ] Module 04: Spark Scala cleaning job
- [ ] Module 06: Delta Lake SCD Type 2
- [ ] Module 07: dbt data mart
- [ ] Module 08: Airflow DAG orchestration
- [ ] Module 09: Testing suite
- [ ] Module 12: End-to-end integrator

---

## 📊 Expected Outcomes

Al finalizar este curso **projects-first Pareto 20/80**, serás capaz de:

✅ **Construir pipelines de producción** con SQL, Spark (Scala), Databricks y Airflow  
✅ **Implementar cargas incrementales idempotentes** con particionado eficiente  
✅ **Escribir tests de calidad de datos** (row counts, uniqueness, null checks)  
✅ **Orquestar workflows complejos** con Airflow (retries, backfills)  
✅ **Versionar código en GitHub** con CI/CD básico  
✅ **Optimizar costos y performance** en ambientes cloud  
✅ **Debuggear pipelines rotos** con logs y métricas  
✅ **Presentar proyectos técnicos** con documentación profesional

---

## 🔐 Security Note

- **Nunca incluir credenciales reales** en código
- Usar placeholders: `<YOUR_ACCOUNT>`, `<YOUR_KEY>`, `<YOUR_TOKEN>`
- Guardar secretos en **GitHub Secrets**, **Vault**, o archivos `.env` (gitignored)
- Revisar `.gitignore` antes de cada commit

---

## 📝 Next Steps (After Course Completion)

1. **Deploy to production:** migrar proyecto final a AWS/Azure/GCP
2. **Add CI/CD:** GitHub Actions para tests automáticos
3. **Contribute to OSS:** colaborar en proyectos Airflow, dbt, Spark
4. **Build portfolio:** documentar proyectos en LinkedIn/blog técnico
5. **Apply to jobs:** usar proyectos como portfolio en entrevistas

---

**🎓 Creado con la metodología Pareto 20/80 — Maximize learning, minimize noise.**
