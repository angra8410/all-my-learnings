# 🎯 Módulo 01 — Introducción al Pareto 20/80

## 🎯 Objetivos de Aprendizaje

Al completar este módulo serás capaz de:

1. **Comprender el principio de Pareto 80/20** aplicado a Data Engineering
2. **Identificar el 20% de skills que generan 80% de impacto** en el trabajo real
3. **Planificar tu roadmap de aprendizaje** enfocado en proyectos
4. **Aplicar la metodología projects-first** en tu estudio
5. **Establecer un plan personalizado** basado en tu tiempo disponible

---

## 📚 Contenido Teórico

### 1. El Principio de Pareto en Data Engineering

**Definición:**
El **Principio de Pareto** (regla 80/20) establece que aproximadamente el **80% de los resultados** provienen del **20% de las causas**.

**Aplicado a Data Engineering:**
- **20% de los skills** → **80% del valor** que entregas en el trabajo
- **20% de las herramientas** → **80% de los pipelines** que construirás
- **20% de los patrones** → **80% de los casos de uso** que enfrentarás

### 2. El 20% Crítico en Data Engineering

#### 2.1 Lenguajes y Queries (20% Core)

**SQL (el skill más importante):**
```
✅ JOINs (INNER, LEFT, FULL OUTER)
✅ Window functions (ROW_NUMBER, RANK, LAG, LEAD)
✅ GROUP BY con agregaciones
✅ CTEs (WITH clauses)
✅ MERGE/UPSERT statements

❌ No necesitas (al inicio):
- SQL Server CLR functions
- Advanced PL/SQL procedures
- Database administration tasks
```

**Python para ETL:**
```
✅ pandas (read_csv, to_sql, merge, groupby)
✅ requests (API calls)
✅ psycopg2/sqlalchemy (DB connections)
✅ Error handling (try/except)

❌ No necesitas (al inicio):
- Machine learning libraries
- Web frameworks (Flask/Django)
- Advanced decorators/metaclasses
```

**Scala para Spark:**
```
✅ DataFrame API (select, filter, join, groupBy)
✅ partitionBy para escritura eficiente
✅ Functions (col, lit, when, udf)

❌ No necesitas (al inicio):
- RDD API (legacy)
- Advanced functional programming
- Scala macros
```

#### 2.2 Patrones de ETL (20% Core)

**Cargas incrementales idempotentes:**
```sql
-- Patrón MERGE (UPSERT) - usado en 80% de pipelines
MERGE INTO target_table AS t
USING source_table AS s
ON t.id = s.id
WHEN MATCHED THEN
  UPDATE SET t.value = s.value, t.updated_at = CURRENT_TIMESTAMP
WHEN NOT MATCHED THEN
  INSERT (id, value, created_at) VALUES (s.id, s.value, CURRENT_TIMESTAMP);
```

**Particionado por fecha:**
```scala
// Patrón usado en 80% de data lakes
df.write
  .mode("overwrite")
  .partitionBy("date_partition")  // Clave para performance
  .parquet("s3://bucket/table/")
```

**Deduplicación:**
```sql
-- Patrón ROW_NUMBER - elimina duplicados
WITH ranked AS (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY id ORDER BY updated_at DESC) AS rn
  FROM raw_data
)
SELECT * EXCLUDE rn FROM ranked WHERE rn = 1;
```

#### 2.3 Orquestación (20% Core)

**Diseño de DAGs en Airflow:**
```python
# Patrón básico usado en 80% de workflows
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'dataeng',
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    'etl_pipeline',
    default_args=default_args,
    schedule_interval='0 2 * * *',  # Daily at 2 AM
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:
    
    extract = PythonOperator(task_id='extract', python_callable=extract_func)
    transform = PythonOperator(task_id='transform', python_callable=transform_func)
    load = PythonOperator(task_id='load', python_callable=load_func)
    
    extract >> transform >> load
```

#### 2.4 Testing (20% Core)

**Checks esenciales que previenen 80% de problemas:**
```python
# 1. Row count
assert df.count() > 0, "Empty DataFrame"

# 2. Uniqueness
assert df.select('id').distinct().count() == df.count(), "Duplicate IDs"

# 3. Not NULL
assert df.filter(col('id').isNull()).count() == 0, "NULL IDs found"

# 4. Expected range
assert df.filter(col('amount') < 0).count() == 0, "Negative amounts"
```

---

### 3. Metodología Projects-First

**Tradicional (Theory-First):**
```
1. Leer 200 páginas de documentación
2. Ver 10 horas de videos
3. Hacer ejercicios de sintaxis
4. (Tal vez) construir un proyecto
```

**Pareto 20/80 (Projects-First):**
```
1. Proyecto mini definido (ej: "ETL de CSV a PostgreSQL")
2. Aprender SOLO lo necesario para ese proyecto
3. Construir, romper, arreglar, iterar
4. Documentar aprendizajes
5. Repetir con proyecto similar (reinforcement)
```

**Ejemplo concreto:**
```
Proyecto: "Pipeline de ventas diarias"

Paso 1: Define entregables
- Input: ventas.csv (10K filas)
- Output: PostgreSQL tabla fact_ventas
- Transformación: agregación por día y categoría
- Orquestación: Airflow DAG

Paso 2: Aprende SOLO lo necesario
- pandas.read_csv()
- pandas.groupby()
- sqlalchemy.create_engine()
- df.to_sql()
- Airflow BashOperator básico

Paso 3: Construye versión 1 (2 horas)
Paso 4: Mejora con deduplicación (1 hora)
Paso 5: Añade tests (30 min)
Paso 6: Documenta (30 min)

Total: 4 horas → Pipeline funcional en portfolio
```

---

### 4. Pareto 20/80 por Módulo del Curso

| Módulo | 20% to Learn (Core Skills) | 80% to Practice (Projects) |
|--------|---------------------------|----------------------------|
| **SQL** | JOINs, window functions, MERGE | Reportes de ventas, queries analíticas |
| **Python ETL** | pandas, requests, psycopg2 | ETL CSV→DB, API→DB |
| **Spark Scala** | DataFrame API, partitionBy | Limpieza de datos, particionado |
| **Databricks** | Notebooks, Jobs, Delta Lake | Job productivo end-to-end |
| **Airflow** | DAGs, retries, scheduling | Orquestar pipeline completo |
| **Testing** | Row count, uniqueness, NULL checks | Suite de tests para pipeline |

---

### 5. Roadmap de Carrera Data Engineer

**Junior Data Engineer (0-2 años):**
```
Core skills:
✅ SQL avanzado
✅ Python para ETL
✅ Git/GitHub básico
✅ Docker básico
✅ Airflow (DAGs básicos)

Portfolio:
- 2-3 pipelines ETL documentados en GitHub
- Al menos 1 proyecto con Airflow
```

**Mid Data Engineer (2-4 años):**
```
Core skills:
✅ Spark (Scala o PySpark)
✅ Cloud platform (AWS/Azure/GCP)
✅ Delta Lake / Data Lakehouse
✅ dbt para transformaciones
✅ Testing & data quality

Portfolio:
- Pipeline end-to-end en producción (cloud)
- Contribuciones a proyectos open source
- Blog técnico con aprendizajes
```

**Senior Data Engineer (4+ años):**
```
Core skills:
✅ Arquitectura de sistemas distribuidos
✅ Optimización de costos cloud
✅ Mentoring & code reviews
✅ Diseño de data platforms
✅ CI/CD para data pipelines

Logros:
- Liderazgo de proyectos de data
- Diseño de arquitecturas escalables
- Mejoras de performance (ej: 50% reducción costos)
```

---

### 6. Cómo Estudiar Este Curso (Estrategia Pareto)

**❌ NO hagas esto:**
- Leer todos los módulos linealmente sin practicar
- Ver videos sin ejecutar código
- Copiar/pegar código sin entenderlo
- Saltarte los proyectos ("lo haré después")

**✅ SÍ haz esto:**
- **1 proyecto por módulo** (mínimo)
- **Ejecutar cada comando** en `actividad-interactiva.md`
- **Romper código intencionalmente** (aprender debuggeando)
- **Repetir patrones** en 3 datasets diferentes
- **Documentar aprendizajes** en tu rama personal

**Ritmo recomendado (Pareto-optimized):**
```
Semana 1-2: Setup + SQL Core + Proyecto SQL
Semana 3-4: Python ETL + Spark basics + Proyectos
Semana 5-6: Databricks + Delta Lake + Proyectos
Semana 7-8: Airflow + Testing + Proyecto integrador
Semana 9-10: Observability + Security + Proyecto final
Semana 11-12: Pulir proyecto final + Portfolio
```

---

## 🏋️ Actividades Prácticas

### Actividad 1: Identificar tu 20% Personal

Revisa job postings reales de Data Engineer y lista las skills más mencionadas.

### Actividad 2: Crear tu Roadmap Personal

Basado en tu tiempo disponible, planifica qué módulos completarás y en qué orden.

### Actividad 3: Configurar Sistema de Tracking

Crea un documento personal de progreso (puede ser en `progreso.md`).

---

## 📝 Entregables

Al finalizar este módulo:

1. ✅ Documento con tu 20% personal identificado
2. ✅ Roadmap personalizado (timeline)
3. ✅ Sistema de tracking configurado
4. ✅ Primer mini-proyecto definido

---

## 🎯 Criterios de Éxito

- [ ] Comprendes el principio Pareto 80/20
- [ ] Identificaste el 20% crítico en Data Engineering
- [ ] Tienes un plan de estudio personalizado
- [ ] Entiendes la metodología projects-first
- [ ] Estás motivado para comenzar con proyectos

---

## ⏱️ Duración Estimada

- **Lectura de teoría:** 45 minutos
- **Actividades prácticas:** 1 hora
- **Planificación personal:** 30 minutos

**Total: 2-2.5 horas**

---

## 📚 Recursos Adicionales

Ver `recursos.md` para:
- Job postings reales analizados
- Roadmaps de otros Data Engineers
- Artículos sobre Pareto en tech skills

---

## ⏭️ Siguiente Paso

**Módulo 02: SQL Core** — Donde aplicarás el principio Pareto para dominar el 20% de SQL que usarás en el 80% de tus pipelines.

---

**💡 Tip:** El principio Pareto no significa ignorar el 80% restante. Significa **priorizar inteligentemente** para maximizar ROI de tu tiempo de estudio.
