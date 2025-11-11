# 🎯 Data Engineering Pareto 20/80 — Projects-First Course

> **Aprende el 20% de Data Engineering que genera el 80% del impacto profesional**

Este curso práctico sigue el **principio de Pareto**: identifica el **20% de conocimientos críticos** que generan el **80% del valor** en el trabajo real de Data Engineering. Prioriza proyectos verificables sobre teoría abstracta.

---

## 🚀 Quick Start

```bash
# 1. Clonar repositorio
git clone https://github.com/angra8410/all-my-learnings.git
cd all-my-learnings/Data-Engineering-Pareto-2080

# 2. Leer el plan de estudio
cat plan-estudio-pareto-data-engineering.md

# 3. Crear rama personal
git checkout -b feature/mi-progreso-pareto

# 4. Comenzar con Módulo 00
cd 00-plan-setup
cat README.md
```

---

## 📚 Estructura del Curso

### Plan de Estudio
📄 **[plan-estudio-pareto-data-engineering.md](plan-estudio-pareto-data-engineering.md)**  
Resumen ejecutivo del curso con objetivos, metodología Pareto, estructura de módulos y acceptance criteria.

### 13 Módulos (120+ horas)

| # | Módulo | Duración | Proyecto | Status |
|---|--------|----------|----------|--------|
| **00** | [Plan & Setup](00-plan-setup/) | 3-4h | Setup completo | ✅ |
| **01** | [Intro Pareto 20/80](01-intro-pareto/) | 2h | Roadmap personal | ✅ |
| **02** | [SQL Core](02-sql-core/) | 10-12h | Reporting queries | 📝 |
| **03** | [Python ETL Basics](03-python-etl-basics/) | 8-10h | ETL pipeline | 📝 |
| **04** | [Spark Scala Fundamentals](04-spark-scala-fundamentals/) | 12-15h | Data cleaning job | 📝 |
| **05** | [Databricks Workflow](05-databricks-workflow/) | 8-10h | Production job | 📝 |
| **06** | [Delta Lake & Storage](06-delta-lake-storage/) | 8-10h | SCD Type 2 | 📝 |
| **07** | [DBT or Transforms](07-dbt-transforms/) | 10-12h | Data mart | 📝 |
| **08** | [Airflow Orchestration](08-airflow-orchestration/) | 12-15h | DAG completo | 📝 |
| **09** | [Testing & Data Quality](09-testing-data-quality/) | 8-10h | Test suite | 📝 |
| **10** | [Observability & Cost](10-observability-cost/) | 6-8h | Monitoring dashboard | 📝 |
| **11** | [Security & Governance](11-security-governance/) | 4-6h | Secure pipeline | 📝 |
| **12** | [Final Project](12-final-project/) | 20-25h | End-to-end integrator | 📝 |

**Leyenda:**  
✅ = Contenido completo  
📝 = Estructura creada (placeholder files)

### Cada Módulo Incluye

Formato estandarizado de 5 archivos:

1. **README.md**: Objetivos, teoría, actividades prácticas
2. **actividad-interactiva.md**: Ejercicios con comandos verificables, campos para respuestas, duraciones
3. **progreso.md**: Checklist de avance personal
4. **retroalimentacion.md**: Rúbrica de evaluación con porcentajes
5. **recursos.md**: Datasets, links, código de ejemplo

---

## 🛠️ Helper Artifacts

**[helper-artifacts/](helper-artifacts/)** — Code snippets reutilizables del 20% core:

### 1. Airflow DAG Skeleton
📄 `airflow/minimal_dag_skeleton.py` (10KB)
- Template completo con best practices
- Retries, scheduling, XCom
- Comentarios explicativos

### 2. Spark Scala Job
📄 `spark-scala/DataCleaningJob.scala` (12KB)
- Job completo de limpieza de datos
- Transformaciones core
- Escritura particionada
- Data quality checks integrados

### 3. SQL DDL Examples
📄 `sql/ddl_fact_dimension_tables.sql` (16KB)
- Star schema completo
- Fact y dimension tables
- SCD Type 1 y Type 2
- Indexes, constraints, partitioning

### 4. SQL Data Quality Tests
📄 `sql/data_quality_tests.sql` (15KB)
- Tests de completeness, uniqueness, validity
- Statistical outlier detection
- Test suite automatizado (PL/pgSQL)

---

## 🎯 Principio Pareto Aplicado

### 20% de Skills (High-Impact Core)

**SQL:**
```sql
-- JOINs, window functions, MERGE/UPSERT
WITH ranked AS (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY id ORDER BY date DESC) AS rn
  FROM data
)
SELECT * FROM ranked WHERE rn = 1;
```

**Spark/Scala:**
```scala
// DataFrame API, particionado
df.write
  .mode("overwrite")
  .partitionBy("date_partition")
  .parquet("s3://bucket/table/")
```

**Airflow:**
```python
# DAG design con retries
default_args = {
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}
```

**Testing:**
```python
# Checks esenciales
assert df.count() > 0  # Row count
assert df.select('id').distinct().count() == df.count()  # Uniqueness
```

### 80% de Práctica (Projects & Repetition)

- ✅ Build el mismo pipeline con 3 datasets diferentes
- ✅ Cargas incrementales diarias (misma lógica, distintas fechas)
- ✅ Refactoring de código (mejorar pipeline existente)
- ✅ Debugging sessions (arreglar pipelines rotos)

---

## 🚦 Getting Started

### Prerequisitos

**Conocimientos:**
- ✅ Programación básica (Python o Java/Scala deseable)
- ✅ SQL básico (SELECT, WHERE, JOINs simples)
- ✅ Línea de comandos (bash, terminal)
- ✅ Git básico (clone, commit, push)

**Herramientas:**
- 💻 Laptop con 8GB RAM mínimo (16GB recomendado)
- 🐳 Docker Desktop
- 🔧 Git + GitHub account
- 📝 VSCode (o IntelliJ IDEA para Scala)
- ☁️ Databricks Community Edition (gratis)
- 🐘 PostgreSQL (via Docker)

### Instalación

Ver **[Módulo 00: Plan & Setup](00-plan-setup/README.md)** para instrucciones detalladas.

```bash
# Rápido check de herramientas
git --version
docker --version
python3 --version

# Levantar PostgreSQL
docker run --name postgres-pareto \
  -e POSTGRES_USER=dataeng \
  -e POSTGRES_PASSWORD=pareto2080 \
  -e POSTGRES_DB=learning_db \
  -p 5432:5432 \
  -d postgres:15
```

### Ritmo Recomendado

| Ritmo | Horas/semana | Duración total |
|-------|--------------|----------------|
| **Intensivo** | 20-25h | 6-8 semanas |
| **Regular** | 15-20h | 8-10 semanas |
| **Part-time** | 10-15h | 12-14 semanas |

---

## 📊 Acceptance Criteria

Checklist completo para validar que el curso está listo:

### Module Structure
- [x] 13 módulos creados (00-12)
- [x] Cada módulo tiene los 5 archivos (README, actividad, progreso, retroalimentacion, recursos)
- [ ] Ningún archivo está vacío (in progress)

### Content Quality
- [x] Cada `actividad-interactiva.md` debe contener comandos verificables
- [x] Cada ejercicio debe tener campos para respuestas (`__________`) y verificación
- [ ] Al menos 6 mini-proyectos + 1 proyecto final (in progress)

### Helper Artifacts
- [x] Airflow DAG skeleton (Python)
- [x] Spark Scala job example
- [x] SQL DDL examples (fact/dimension tables)
- [x] SQL test examples (uniqueness, not_null)

### Projects
- [x] Module 02: SQL reporting queries (planned)
- [x] Module 03: Python ETL pipeline (planned)
- [x] Module 04: Spark Scala cleaning job (planned)
- [x] Module 06: Delta Lake SCD Type 2 (planned)
- [x] Module 07: dbt data mart (planned)
- [x] Module 08: Airflow DAG orchestration (planned)
- [x] Module 09: Testing suite (planned)
- [x] Module 12: End-to-end integrator (planned)

### Validation
- [x] Sanity check script created (`sanity_check.sh`)
- [ ] All modules passing sanity checks (in progress)

---

## 🔧 Sanity Check

Ejecutar script de validación:

```bash
./sanity_check.sh
```

Este script verifica:
- ✅ Todos los módulos existen
- ✅ Cada módulo tiene los 5 archivos requeridos
- ✅ Archivos no están vacíos
- ✅ Helper artifacts existen
- ✅ Conteo de proyectos >= 6

---

## 🎓 Expected Outcomes

Al finalizar este curso serás capaz de:

✅ **Construir pipelines de producción** con SQL, Spark (Scala), Databricks y Airflow  
✅ **Implementar cargas incrementales idempotentes** con particionado eficiente  
✅ **Escribir tests de calidad de datos** (row counts, uniqueness, null checks)  
✅ **Orquestar workflows complejos** con Airflow (retries, backfills)  
✅ **Versionar código en GitHub** con CI/CD básico  
✅ **Optimizar costos y performance** en ambientes cloud  
✅ **Debuggear pipelines rotos** con logs y métricas  
✅ **Presentar proyectos técnicos** con documentación profesional

---

## 📝 Portfolio Projects

Al completar el curso tendrás **8+ proyectos** en GitHub:

1. **SQL Reporting Queries** — análisis de ventas con window functions
2. **Python ETL Pipeline** — CSV → PostgreSQL con validaciones
3. **Spark Scala Data Cleaning** — procesamiento distribuido con particionado
4. **Databricks Production Job** — notebook productivizado
5. **Delta Lake SCD Type 2** — historización de dimensiones
6. **dbt Data Mart** — transformaciones SQL versionadas
7. **Airflow DAG Orchestration** — pipeline completo orquestado
8. **End-to-End Integration** — CSV/API → Spark → Delta → dbt → Tests → Airflow

---

## 🔐 Security Note

- **Nunca incluir credenciales reales** en código
- Usar placeholders: `<YOUR_ACCOUNT>`, `<YOUR_KEY>`, `<YOUR_TOKEN>`
- Guardar secretos en **GitHub Secrets**, **Vault**, o archivos `.env` (gitignored)

---

## 📚 Additional Resources

**Documentación Oficial:**
- [Apache Spark](https://spark.apache.org/docs/latest/)
- [Apache Airflow](https://airflow.apache.org/docs/)
- [Databricks](https://docs.databricks.com/)
- [PostgreSQL](https://www.postgresql.org/docs/)
- [dbt](https://docs.getdbt.com/)

**Comunidades:**
- Reddit: [r/dataengineering](https://www.reddit.com/r/dataengineering/)
- Discord: Data Engineering Community
- Slack: dbt Community, Airflow Community

---

## 🤝 Contributing

Mejoras y contribuciones son bienvenidas!

1. Fork el repositorio
2. Crea rama feature (`git checkout -b feature/mejora-modulo-x`)
3. Commit cambios (`git commit -m 'Add: mejora en módulo X'`)
4. Push a la rama (`git push origin feature/mejora-modulo-x`)
5. Abre Pull Request

---

## 📅 Roadmap

**v1.0 (Actual):**
- ✅ Course blueprint
- ✅ Módulos 00-01 completos
- ✅ Helper artifacts
- ✅ Sanity check script

**v1.1 (Próximo):**
- [ ] Módulos 02, 04, 08, 12 con contenido completo
- [ ] Datasets de ejemplo descargables
- [ ] Videos complementarios (opcional)

**v2.0 (Futuro):**
- [ ] Todos los módulos completos
- [ ] CI/CD examples con GitHub Actions
- [ ] Terraform templates
- [ ] Great Expectations integration

---

## 📄 License

Este curso es de código abierto para fines educativos.

---

## ✍️ Autor

**Data Engineering Pareto 20/80 Course**  
Creado con la metodología Pareto: Maximize learning, minimize noise.

📅 **Última actualización:** 2024-01-01  
🎓 **Versión:** 1.0 (MVP)

---

**💡 Recuerda:** El principio Pareto no significa ignorar el 80% restante. Significa **priorizar inteligentemente** para maximizar el ROI de tu tiempo de estudio.

**🚀 ¡Comienza ahora!** → [Módulo 00: Plan & Setup](00-plan-setup/README.md)
