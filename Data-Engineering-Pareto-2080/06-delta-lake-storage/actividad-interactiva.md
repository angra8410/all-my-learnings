# Actividad Interactiva — Delta Lake & Storage

🎯 Objetivo
Implementar un flujo de ingestion/transformación que use Delta Lake para soportar cargas incrementales, time travel y housekeeping.

🧩 Ejercicio 1: Preparar entorno y datos (15 minutos)  
Objetivo: Asegurarte de que tienes acceso a Spark/Databricks y que los CSV de ejemplo existen en `Data-Engineering-Roadmap/data`.

Pasos:
1. Si usas Databricks: sube `data/sales_sample.csv` al DBFS o monta el storage. Si usas local Spark, sitúa los datos en `data/`.
2. Verifica lectura:
```scala
spark.read.option("header","true").csv("data/sales_sample.csv").show(3)
```
Verificación: ¿Se muestran 3 filas de ejemplo? Sí / No. Resultado ejemplo fila1 producto: _______________

Duración: 15 minutos

🔁 Ejercicio 2: Crear tabla Delta y escribir particionado (30 minutos)  
Objetivo: Escribir los datos como tabla Delta particionada por `fecha`.

Pasos (Spark SQL / Scala):
```sql
-- Spark SQL (Databricks or spark-sql)
CREATE TABLE IF NOT EXISTS delta_ventas
USING delta
LOCATION '/mnt/delta/ventas'
AS SELECT * FROM parquet.`data/sales_sample.csv`;
```
O usando DataFrame API (Scala/PySpark):
```scala
val df = spark.read.option("header","true").csv("data/sales_sample.csv")
df.write.format("delta").mode("overwrite").partitionBy("fecha").save("/mnt/delta/ventas")
```
Verificación: lista particiones:
```bash
ls /mnt/delta/ventas
```
Particiones encontradas: _______________

Duración: 30 minutos

🔁 Ejercicio 3: Upsert / MERGE incremental (40 minutos)  
Objetivo: Aplicar MERGE para insertar/actualizar usando `data/sales_incremental.csv`.

Pasos (Spark SQL / Delta):
```sql
-- Crear tabla stage temporal con incremental
CREATE OR REPLACE TEMP VIEW ventas_stage
USING csv
OPTIONS (path 'data/sales_incremental.csv', header 'true');

MERGE INTO delta.`/mnt/delta/ventas` AS target
USING ventas_stage AS source
ON target.order_id = source.order_id
WHEN MATCHED THEN UPDATE SET *
WHEN NOT MATCHED THEN INSERT *;
```
Verificación:
- Filas nuevas: _______________
- Filas actualizadas: _______________

Duración: 40 minutos

🕰 Ejercicio 4: Time Travel y versiones (25 minutos)  
Objetivo: Listar versiones, ver estado en versión anterior y restaurar si es necesario.

Pasos:
```sql
-- Listar historial
DESCRIBE HISTORY delta.`/mnt/delta/ventas`;

-- Consultar versión n (ejemplo version 0)
SELECT * FROM delta.`/mnt/delta/ventas@v0` LIMIT 5;

-- Restaurar: copiar versión a nueva tabla o sobrescribir
VACUUM delta.`/mnt/delta/ventas` RETAIN 0 HOURS; -- uso con cuidado, sigue política de retención
```
Verificación: ¿Pudiste ver la versión 0? Sí / No. Resultado ejemplo registro en v0: _______________

Duración: 25 minutos

🧹 Ejercicio 5: Housekeeping y buenas prácticas (20 minutos)  
Objetivo: Ejecutar OPTIMIZE (Databricks) y VACUUM, entender retention.

Pasos (Databricks):
```sql
OPTIMIZE delta.`/mnt/delta/ventas` ZORDER BY (cliente_id);
VACUUM delta.`/mnt/delta/ventas` RETAIN 168 HOURS;
```
Verificación: tamaño carpeta antes: _______________ size after OPTIMIZE: _______________

Duración: 20 minutos

📦 Mini-proyecto (2 horas)
Objetivo: Automatizar una carga diaria que:
- Carga CSV incremental a staging
- Ejecuta MERGE en la tabla Delta
- Ejecuta OPTIMIZE semanalmente y VACUUM con política segura

Entregables:
- Script/Notebook: delta_upsert_job.py / delta_upsert_notebook.py
- Documento: runbook_delta.md con pasos de rollback usando Time Travel
Duración: 2 horas

📊 Resumen del Tiempo
Ejercicio	Duración
1. Preparar entorno	15 min
2. Crear tabla Delta	30 min
3. MERGE incremental	40 min
4. Time Travel	25 min
5. Housekeeping	20 min
Mini-proyecto	120 min
TOTAL	~4.5 horas

Próximo paso: subir `delta_upsert_example.sql` y `runbook_delta.md` al módulo /examples.
