# 🛠️ Helper Artifacts — Data Engineering Pareto 20/80

Este directorio contiene **code snippets y templates reutilizables** que puedes copiar y adaptar para tus propios proyectos.

---

## 📁 Contenido

### 1. Airflow DAG Skeleton (`airflow/`)

**Archivo:** `minimal_dag_skeleton.py`

**Qué incluye:**
- Template básico de DAG con best practices
- Ejemplos de PythonOperator, BashOperator, FileSensor
- Configuración de retries, timeouts, scheduling
- Uso de XCom para pasar datos entre tasks
- Comentarios explicativos del 20% core

**Uso:**
```bash
# Copiar a tu directorio de Airflow
cp helper-artifacts/airflow/minimal_dag_skeleton.py ~/airflow-pareto/dags/mi_pipeline_dag.py

# Editar y personalizar
# Ejecutar en Airflow
```

---

### 2. Spark Scala Job (`spark-scala/`)

**Archivo:** `DataCleaningJob.scala`

**Qué incluye:**
- Job completo de limpieza de datos
- Lectura de CSV/Parquet
- Transformaciones core (filter, select, groupBy, join)
- Deduplicación con window functions
- Escritura particionada
- Data quality checks integrados
- Best practices y anti-patterns explicados

**Compilación:**
```bash
# Asumiendo sbt configurado
sbt package

# Submit local
spark-submit \
  --class com.dataeng.pareto.DataCleaningJob \
  --master local[*] \
  target/scala-2.12/spark-job.jar \
  data/input/sales.csv \
  data/output/sales_clean
```

**Uso en Databricks:**
1. Crear notebook Scala
2. Copiar código del job
3. Ajustar paths (usar DBFS)
4. Ejecutar en cluster

---

### 3. SQL DDL Examples (`sql/`)

**Archivo:** `ddl_fact_dimension_tables.sql`

**Qué incluye:**
- Dimension tables (dim_customer, dim_product, dim_date, dim_location)
- Fact tables (fact_sales, fact_inventory)
- Slowly Changing Dimensions (SCD Type 1 y Type 2)
- Aggregate tables
- Staging tables
- Views útiles
- Indexes y constraints
- Partitioning strategies

**Uso:**
```bash
# Ejecutar en PostgreSQL
psql -U dataeng -d warehouse_db -f helper-artifacts/sql/ddl_fact_dimension_tables.sql

# O en chunks
psql -U dataeng -d warehouse_db << EOF
-- Copy paste secciones específicas
CREATE TABLE dim_customer (...);
EOF
```

---

### 4. SQL Data Quality Tests (`sql/`)

**Archivo:** `data_quality_tests.sql`

**Qué incluye:**
- Tests de Completeness (row count, nulls, missing data)
- Tests de Uniqueness (duplicates)
- Tests de Validity (ranges, formats, foreign keys)
- Tests de Consistency (calculated fields, cross-table)
- Tests de Timeliness (freshness)
- Tests de Outliers (statistical)
- Función PL/pgSQL para test suite completo

**Uso:**
```bash
# Ejecutar tests individuales
psql -U dataeng -d warehouse_db -f helper-artifacts/sql/data_quality_tests.sql

# O ejecutar suite completa
psql -U dataeng -d warehouse_db -c "SELECT * FROM run_all_data_quality_tests();"

# Integrar en Airflow
# Ver airflow/minimal_dag_skeleton.py para ejemplo de task de validación
```

---

## 🎯 Pareto 20% — Cómo Usar Estos Artifacts

### 1. No copies ciegamente
- **Entiende** cada línea antes de copiar
- **Adapta** a tus necesidades específicas
- **Simplifica** si no necesitas toda la funcionalidad

### 2. Orden de uso recomendado
1. **Primero:** SQL DDL — crea tu warehouse schema
2. **Segundo:** SQL Tests — valida tus datos
3. **Tercero:** Spark job — procesa y carga datos
4. **Cuarto:** Airflow DAG — orquesta todo el pipeline

### 3. Integración típica

```
Pipeline completo:

1. Airflow DAG trigger
   ↓
2. Extract task (Python/Bash)
   ↓
3. Spark job (limpieza y transformación)
   ↓
4. Load to warehouse (COPY/INSERT)
   ↓
5. SQL tests (data quality)
   ↓
6. Alertas si falla
   ↓
7. Success notification
```

### 4. Customización por proyecto

**Para proyecto simple (CSV → PostgreSQL):**
- Usar solo: Airflow DAG básico + SQL tests
- Skip: Spark (usar pandas en Python)

**Para proyecto medium (ETL distribuido):**
- Usar todo: Airflow + Spark + SQL DDL + Tests

**Para proyecto enterprise (data lakehouse):**
- Extender Spark job con Delta Lake
- Añadir dbt para transformaciones
- Integrar Great Expectations para tests avanzados

---

## 📚 Templates Adicionales (Futuros)

Planeados para añadir:

- [ ] `databricks/job_config.json` - Configuración de Databricks Job
- [ ] `dbt/models/` - Ejemplos de modelos dbt
- [ ] `great_expectations/` - Config de Great Expectations
- [ ] `terraform/` - IaC para desplegar infraestructura
- [ ] `docker/` - Dockerfiles para servicios locales
- [ ] `testing/pytest_examples.py` - Tests unitarios Python

---

## 🔧 Troubleshooting

### Airflow DAG no aparece en UI
```bash
# Verificar syntax
python helper-artifacts/airflow/minimal_dag_skeleton.py

# Verificar logs
docker logs airflow-standalone | grep ERROR
```

### Spark job falla con OutOfMemory
```bash
# Aumentar memoria del executor
spark-submit \
  --executor-memory 4G \
  --driver-memory 2G \
  ...
```

### SQL tests muy lentos
```sql
-- Añadir indexes en columnas usadas en WHERE
CREATE INDEX idx_fact_sales_date ON fact_sales(date_key);

-- Usar sampling para tables grandes
SELECT ... FROM fact_sales TABLESAMPLE SYSTEM (10);  -- 10% sample
```

---

## 💡 Best Practices

1. **Versionado:**
   - Guardar estos templates en tu repo Git
   - Documentar cambios que haces

2. **Reusabilidad:**
   - Crear tu propia librería de snippets
   - Estandarizar dentro de tu equipo

3. **Testing:**
   - Testear localmente antes de deploy
   - Usar datos sintéticos para dev

4. **Documentación:**
   - Comentar tus adaptaciones
   - Mantener README actualizado

---

## 🚀 Next Steps

1. **Explorar** cada archivo en detalle
2. **Ejecutar** ejemplos en tu entorno local
3. **Adaptar** para tu primer proyecto
4. **Contribuir** mejoras a este repo (pull requests bienvenidos!)

---

**📝 Nota:** Estos templates son punto de partida, no solución final. Siempre optimiza según tu caso de uso específico.

**🎓 Curso:** Data Engineering Pareto 20/80  
**📅 Última actualización:** 2024-01-01
