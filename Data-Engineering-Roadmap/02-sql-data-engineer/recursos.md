# 📚 Recursos — Módulo 02: SQL para Data Engineering

## 🎯 Documentación Oficial

### PostgreSQL
- **PostgreSQL Documentation**: https://www.postgresql.org/docs/current/
- **Window Functions Guide**: https://www.postgresql.org/docs/current/tutorial-window.html
- **Performance Tips**: https://wiki.postgresql.org/wiki/Performance_Optimization
- **Indexes**: https://www.postgresql.org/docs/current/indexes.html

### SQL Estándar
- **SQL Standards**: https://www.iso.org/standard/76583.html
- **Modern SQL**: https://modern-sql.com/

---

## 🎓 Tutoriales y Cursos

### Window Functions
- **PostgreSQL Window Functions Tutorial**: https://www.postgresqltutorial.com/postgresql-window-function/
- **Window Functions Explained**: https://www.windowfunctions.com/
- **Advanced SQL - Mode Analytics**: https://mode.com/sql-tutorial/sql-window-functions/

### Optimización
- **Use The Index Luke**: https://use-the-index-luke.com/
- **SQL Performance Explained**: https://sql-performance-explained.com/
- **EXPLAIN Explained**: https://www.depesz.com/tag/explain/

### CTEs y Subconsultas
- **CTE Tutorial**: https://www.essentialsql.com/introduction-common-table-expressions-ctes/
- **PostgreSQL CTEs**: https://www.postgresqltutorial.com/postgresql-cte/

---

## 📖 Libros Recomendados

1. **"SQL Performance Explained"** - Markus Winand
   - Optimización de queries paso a paso
   - Índices explicados claramente

2. **"PostgreSQL: Up and Running"** - Regina Obe & Leo Hsu
   - Características avanzadas de PostgreSQL
   - Best practices

3. **"SQL Antipatterns"** - Bill Karwin
   - Errores comunes y cómo evitarlos

---

## 🎥 Videos

- **SQL Window Functions - Computerphile**: https://www.youtube.com/watch?v=7nJKDrGW4sw
- **Database Indexing Explained**: https://www.youtube.com/watch?v=HubezKbFL7E
- **PostgreSQL Performance Tuning**: https://www.youtube.com/watch?v=6dDPq4GlcfA

---

## 💻 Herramientas Online

### SQL Practice
- **SQLZoo**: https://sqlzoo.net/ - Ejercicios interactivos
- **HackerRank SQL**: https://www.hackerrank.com/domains/sql
- **LeetCode Database**: https://leetcode.com/problemset/database/
- **Mode SQL Tutorial**: https://mode.com/sql-tutorial/

### Query Testers
- **DB Fiddle**: https://www.db-fiddle.com/ - Probar queries online
- **SQLFiddle**: http://sqlfiddle.com/
- **PostgreSQL Online**: https://extendsclass.com/postgresql-online.html

### Visualizadores de EXPLAIN
- **Explain PostgreSQL**: https://explain.depesz.com/
- **PEV (Postgres Explain Visualizer)**: https://tatiyants.com/pev/

---

## 🎯 Datasets de Práctica

### Datasets Grandes para Performance Testing
- **NYC Taxi Data** (>100M filas): https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page
- **Stack Overflow Data**: https://www.kaggle.com/stackoverflow/stackoverflow
- **GitHub Archive**: https://www.gharchive.org/
- **IMDB Datasets**: https://www.imdb.com/interfaces/

### Datasets Medianos
- **Sakila Database** (PostgreSQL): https://github.com/jOOQ/sakila
- **Northwind Database**: https://github.com/pthom/northwind_psql
- **AdventureWorks**: https://github.com/lorint/AdventureWorks-for-Postgres

---

## 📝 Cheat Sheets

### Window Functions Cheat Sheet
```sql
-- ROW_NUMBER: Número único por fila
ROW_NUMBER() OVER (PARTITION BY column ORDER BY column)

-- RANK: Con gaps para empates
RANK() OVER (ORDER BY column DESC)

-- DENSE_RANK: Sin gaps
DENSE_RANK() OVER (ORDER BY column)

-- LAG: Valor de fila anterior
LAG(column, offset) OVER (PARTITION BY col ORDER BY col)

-- LEAD: Valor de fila siguiente
LEAD(column, offset) OVER (PARTITION BY col ORDER BY col)

-- Running total
SUM(column) OVER (ORDER BY date)

-- Moving average (3 periodos)
AVG(column) OVER (ORDER BY date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW)

-- FIRST_VALUE / LAST_VALUE
FIRST_VALUE(column) OVER (PARTITION BY col ORDER BY col)
LAST_VALUE(column) OVER (PARTITION BY col ORDER BY col 
                         ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING)
```

### Índices Cheat Sheet
```sql
-- Índice simple
CREATE INDEX idx_name ON table(column);

-- Índice compuesto (orden importa!)
CREATE INDEX idx_name ON table(col1, col2, col3);

-- Índice parcial
CREATE INDEX idx_name ON table(column) WHERE condition;

-- Índice único
CREATE UNIQUE INDEX idx_name ON table(column);

-- Índice con INCLUDE (PostgreSQL 11+)
CREATE INDEX idx_name ON table(col1) INCLUDE (col2, col3);

-- Ver índices de una tabla
\di+ table_name

-- Eliminar índice
DROP INDEX idx_name;
```

### EXPLAIN Cheat Sheet
```sql
-- Plan básico
EXPLAIN SELECT ...;

-- Con costos estimados
EXPLAIN (COSTS true) SELECT ...;

-- Con ejecución real (OJO: ejecuta la query!)
EXPLAIN ANALYZE SELECT ...;

-- Con más detalles
EXPLAIN (ANALYZE, BUFFERS, VERBOSE) SELECT ...;

-- Solo buffers
EXPLAIN (ANALYZE, BUFFERS) SELECT ...;
```

**Indicadores de problemas en EXPLAIN:**
- 🚨 **Seq Scan** en tablas grandes → Agregar índice
- 🚨 **Nested Loop** costoso → Verificar estadísticas (ANALYZE)
- 🚨 **Sort** con memoria insuficiente → Aumentar work_mem o agregar índice
- 🚨 Estimaciones muy incorrectas (rows estimado vs actual) → Ejecutar ANALYZE

---

## 🔧 Configuración de PostgreSQL

### Configuraciones para Desarrollo Local
```sql
-- Ver configuración actual
SHOW all;

-- Aumentar memoria para sorts (temporal, solo para sesión)
SET work_mem = '256MB';

-- Habilitar query timing
\timing on

-- Ver estadísticas de tablas
SELECT * FROM pg_stat_user_tables WHERE tablename = 'your_table';

-- Actualizar estadísticas
ANALYZE table_name;

-- Vacuum (limpiar espacio muerto)
VACUUM ANALYZE table_name;
```

### postgresql.conf Optimizaciones
```ini
# Para desarrollo local (ajustar según tu RAM)
shared_buffers = 2GB              # 25% de RAM
effective_cache_size = 6GB        # 50-75% de RAM
work_mem = 64MB                   # Para sorts y hash tables
maintenance_work_mem = 512MB      # Para VACUUM, CREATE INDEX
random_page_cost = 1.1            # Para SSDs (default 4.0 es para HDDs)
```

---

## 💡 Best Practices

### Escritura de Queries
1. **Usa CTEs para legibilidad** en queries complejas
2. **Evita SELECT *** - Especifica columnas necesarias
3. **WHERE antes de JOIN** cuando sea posible
4. **Usa índices en columnas de JOIN y WHERE**
5. **LIMIT** en desarrollo para pruebas rápidas

### Optimización
1. **Ejecuta EXPLAIN ANALYZE** antes de optimizar
2. **Crea índices basados en queries reales**, no por "si acaso"
3. **Índices compuestos**: Columnas más selectivas primero
4. **Evita funciones en WHERE** sobre columnas indexadas (rompe índice)
5. **Mantén estadísticas actualizadas** con ANALYZE regular

### ETL
1. **TRUNCATE** es más rápido que DELETE para vaciar tablas
2. **COPY** es más rápido que INSERT para cargas masivas
3. **Desactiva índices** antes de cargas grandes, recréalos después
4. **Usa transacciones** para atomicidad
5. **Particiona tablas grandes** por fecha/región

---

## 🌐 Comunidades

- **PostgreSQL Slack**: https://pgtreats.info/slack-invite
- **r/PostgreSQL**: https://www.reddit.com/r/PostgreSQL/
- **r/SQL**: https://www.reddit.com/r/SQL/
- **Stack Overflow - PostgreSQL**: https://stackoverflow.com/questions/tagged/postgresql
- **PostgreSQL Mailing Lists**: https://www.postgresql.org/list/

---

## 📊 Herramientas de Gestión

### GUI Clients
- **pgAdmin**: https://www.pgadmin.org/ - Cliente oficial PostgreSQL
- **DBeaver**: https://dbeaver.io/ - Universal, gratis
- **TablePlus**: https://tableplus.com/ - Modern UI (Mac/Windows)
- **DataGrip**: https://www.jetbrains.com/datagrip/ - Potente pero pago

### CLI Tools
- **psql**: Cliente de línea de comandos oficial
- **pgcli**: https://www.pgcli.com/ - psql con autocomplete
- **usql**: https://github.com/xo/usql - Universal CLI para varias DBs

---

## 🎯 Ejercicios Adicionales

### Sitios con Problemas SQL
1. **StrataScratch**: https://www.stratascratch.com/ - Real interview questions
2. **DataLemur**: https://datalemur.com/ - Data Science SQL
3. **SQL Practice**: https://www.sql-practice.com/
4. **W3Schools SQL**: https://www.w3schools.com/sql/

### Proyectos Sugeridos
1. **Análisis de logs de servidor** - Parsing, agregaciones, detección de anomalías
2. **Dashboard de métricas de e-commerce** - Sales, conversion rates, cohorts
3. **Sistema de recomendaciones** - Collaborative filtering con SQL
4. **Data quality monitoring** - Detectar nulls, duplicados, outliers

---

## 📖 Artículos Recomendados

- **Things I Wish More Developers Knew About Databases**: https://medium.com/@rakyll/things-i-wished-more-developers-knew-about-databases-2d0178464f78
- **SQL Style Guide**: https://www.sqlstyle.guide/
- **SQL Indexing and Tuning e-Book**: https://use-the-index-luke.com/

---

**Última actualización:** Noviembre 2024  
**Mantenedor:** angra8410

💡 **Tip**: SQL es una habilidad que se perfecciona con práctica constante. Dedica 30 minutos diarios a resolver problemas en HackerRank o LeetCode para mantener tu fluidez.
