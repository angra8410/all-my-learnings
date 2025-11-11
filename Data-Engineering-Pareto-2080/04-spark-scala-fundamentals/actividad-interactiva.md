# Actividad Interactiva — Spark Scala

🎯 Objetivo
Implementar un job Spark en Scala que lea ventas, limpie datos, agregue métricas y escriba un Delta/Parquet particionado por fecha.

🛠 Ejercicio 1: Preparar entorno (15 minutos)
Objetivo: Verificar si tienes sbt/Scala/Spark en local o usar Databricks.

Comandos:
```bash
scala -version
sbt sbtVersion
spark-submit --version
```
Verificación: versions -> Scala: _______________ Spark: _______________

Duración: 15 minutos

🔧 Ejercicio 2: Job Scala minimal (45 minutos)
Objetivo: Crear un job que lea CSV y escriba Parquet particionado.

Scala ejemplo (skeleton):
```scala
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._

object SalesJob {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder.appName("SalesJob").getOrCreate()
    import spark.implicits._
    val df = spark.read.option("header", "true").csv("data/sales_sample.csv")
    val clean = df.withColumn("producto", lower(trim($"producto")))
    val agreg = clean.groupBy("fecha").agg(sum($"total").alias("daily_total"))
    agreg.write.mode("overwrite").partitionBy("fecha").parquet("output/sales_daily")
    spark.stop()
  }
}
```

Verificación: `ls output/sales_daily/fecha=2024-01-01` -> _______________

Duración: 45 minutos

⚙️ Ejercicio 3: Optimización y broadcast joins (30 minutos)
Objetivo: Aplicar broadcast join cuando una tabla es pequeña.

Scala snippet:
```scala
import org.apache.spark.sql.functions.broadcast
val dim = spark.read.parquet("data/dim_customer")
val fact = spark.read.parquet("output/sales_daily")
val joined = fact.join(broadcast(dim), Seq("cliente_id"))
```
Verificación: explain plan -> buscar BroadcastHashJoin -> _______________

Duración: 30 minutos

📦 Ejercicio 4: Mini-proyecto Spark (2 horas)
Objetivo: Crear job que haga ingest, transform, partition write, y pequeña suite de QA (conteos y checks).

Entregables:
- src/main/scala/SalesJob.scala
- build.sbt
- Script de ejecución: run_spark.sh

Duración: 2 horas
