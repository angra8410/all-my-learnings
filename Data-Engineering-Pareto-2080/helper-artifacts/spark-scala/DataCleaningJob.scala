/**
 * Minimal Spark Scala Job Example
 * =================================
 * 
 * Este job Spark en Scala es un template básico que muestra el 20% de patterns
 * que usarás en 80% de tus trabajos de procesamiento de datos.
 * 
 * Cubre:
 * - Lectura de datos (CSV, Parquet)
 * - Transformaciones core (select, filter, groupBy, join)
 * - Escritura particionada
 * - Manejo de errores básico
 * 
 * Uso:
 * 1. Compilar: sbt package
 * 2. Ejecutar localmente: spark-submit --class DataCleaningJob target/scala-2.12/spark-job.jar
 * 3. Ejecutar en cluster: spark-submit --master yarn --class DataCleaningJob ...
 * 
 * Autor: Data Engineering Pareto 20/80 Course
 */

package com.dataeng.pareto

import org.apache.spark.sql.{DataFrame, SparkSession}
import org.apache.spark.sql.functions._
import org.apache.spark.sql.types._

object DataCleaningJob {
  
  /**
   * Main entry point del Spark job.
   */
  def main(args: Array[String]): Unit = {
    
    // ========================================================================
    // 1. INICIALIZAR SPARK SESSION
    // ========================================================================
    val spark = SparkSession
      .builder()
      .appName("DataCleaningJob - Pareto Example")
      .config("spark.sql.shuffle.partitions", "200")  // Default partitions para aggregations
      .config("spark.sql.adaptive.enabled", "true")   // Adaptive Query Execution (Spark 3+)
      .getOrCreate()
    
    import spark.implicits._  // Para usar $"column_name" syntax
    
    try {
      
      // Parsear argumentos (ejemplo simple)
      val inputPath = if (args.length > 0) args(0) else "data/input/sales.csv"
      val outputPath = if (args.length > 1) args(1) else "data/output/sales_clean"
      
      println(s"==> Input: $inputPath")
      println(s"==> Output: $outputPath")
      
      // ======================================================================
      // 2. LECTURA DE DATOS
      // ======================================================================
      
      // Opción A: CSV con schema inferido
      val rawDF = spark.read
        .option("header", "true")
        .option("inferSchema", "true")
        .csv(inputPath)
      
      // Opción B: CSV con schema explícito (mejor para producción)
      val schema = StructType(Array(
        StructField("transaction_id", StringType, nullable = false),
        StructField("date", DateType, nullable = false),
        StructField("customer_id", StringType, nullable = false),
        StructField("product_id", StringType, nullable = false),
        StructField("quantity", IntegerType, nullable = false),
        StructField("unit_price", DoubleType, nullable = false),
        StructField("discount", DoubleType, nullable = true)
      ))
      
      // val rawDF = spark.read.schema(schema).csv(inputPath)
      
      println(s"==> Rows leídas: ${rawDF.count()}")
      rawDF.printSchema()
      
      // ======================================================================
      // 3. TRANSFORMACIONES (EL 20% CORE)
      // ======================================================================
      
      // 3.1 Limpieza básica
      val cleanDF = rawDF
        .na.drop("any", Seq("transaction_id", "customer_id"))  // Drop nulls en columnas clave
        .filter($"quantity" > 0 && $"unit_price" > 0)          // Filtrar valores inválidos
        .withColumn("discount", coalesce($"discount", lit(0.0))) // Reemplazar nulls
      
      // 3.2 Calcular columna derivada
      val enrichedDF = cleanDF
        .withColumn("total_amount", 
          round($"quantity" * $"unit_price" * (lit(1.0) - $"discount"), 2)
        )
        .withColumn("date_partition", 
          date_format($"date", "yyyy-MM-dd")  // Para particionado posterior
        )
      
      // 3.3 Deduplicación (patrón común)
      val dedupedDF = enrichedDF
        .withColumn("row_num", 
          row_number().over(
            Window.partitionBy("transaction_id").orderBy($"date".desc)
          )
        )
        .filter($"row_num" === 1)
        .drop("row_num")
      
      println(s"==> Rows después de limpieza: ${dedupedDF.count()}")
      
      // ======================================================================
      // 4. AGREGACIONES (patrón común)
      // ======================================================================
      
      val dailySalesDF = dedupedDF
        .groupBy("date_partition", "product_id")
        .agg(
          count("transaction_id").alias("num_transactions"),
          sum("quantity").alias("total_quantity"),
          sum("total_amount").alias("total_revenue"),
          avg("unit_price").alias("avg_price")
        )
        .orderBy($"date_partition".desc, $"total_revenue".desc)
      
      println("==> Muestra de agregaciones diarias:")
      dailySalesDF.show(10, truncate = false)
      
      // ======================================================================
      // 5. JOINS (ejemplo si necesitas enriquecer con otra fuente)
      // ======================================================================
      
      // Ejemplo: join con tabla de productos (placeholder)
      val productsDF = spark.createDataFrame(Seq(
        ("PROD001", "Electronics", "Laptop"),
        ("PROD002", "Clothing", "T-Shirt"),
        ("PROD003", "Home", "Chair")
      )).toDF("product_id", "category", "product_name")
      
      val enrichedSalesDF = dailySalesDF
        .join(productsDF, Seq("product_id"), "left")  // LEFT JOIN
        .select(
          $"date_partition",
          $"product_id",
          $"product_name",
          $"category",
          $"num_transactions",
          $"total_quantity",
          $"total_revenue"
        )
      
      // ======================================================================
      // 6. ESCRITURA DE DATOS (con particionado)
      // ======================================================================
      
      // Opción A: Parquet con particionado por fecha (patrón más común)
      enrichedSalesDF.write
        .mode("overwrite")  // overwrite, append, error, ignore
        .partitionBy("date_partition")  // CLAVE para performance en queries
        .parquet(outputPath)
      
      // Opción B: CSV (menos eficiente, usar solo para outputs pequeños)
      // enrichedSalesDF.write
      //   .mode("overwrite")
      //   .option("header", "true")
      //   .csv(outputPath)
      
      println(s"==> Datos escritos a: $outputPath")
      
      // ======================================================================
      // 7. DATA QUALITY CHECKS (básico)
      // ======================================================================
      
      runDataQualityChecks(enrichedSalesDF)
      
      println("==> Job completado exitosamente!")
      
    } catch {
      case e: Exception =>
        println(s"ERROR: Job falló con excepción: ${e.getMessage}")
        e.printStackTrace()
        sys.exit(1)  // Exit code 1 para indicar fallo
    } finally {
      spark.stop()
    }
  }
  
  /**
   * Ejecuta checks de calidad de datos.
   * 
   * @param df DataFrame a validar
   */
  def runDataQualityChecks(df: DataFrame): Unit = {
    println("==> Ejecutando data quality checks...")
    
    // Check 1: Row count > 0
    val rowCount = df.count()
    require(rowCount > 0, "FAILED: DataFrame está vacío!")
    println(s"  ✓ Row count: $rowCount")
    
    // Check 2: No nulls en columnas clave
    val nullCount = df.filter(
      col("product_id").isNull || col("date_partition").isNull
    ).count()
    require(nullCount == 0, s"FAILED: $nullCount rows con nulls en columnas clave!")
    println(s"  ✓ No nulls en columnas clave")
    
    // Check 3: Valores en rango esperado
    val negativeRevenue = df.filter($"total_revenue" < 0).count()
    require(negativeRevenue == 0, s"FAILED: $negativeRevenue rows con revenue negativo!")
    println(s"  ✓ No revenue negativo")
    
    println("==> Todos los checks pasaron!")
  }
  
  /**
   * Helper: Lee datos desde múltiples fuentes (pattern avanzado).
   * 
   * @param spark SparkSession
   * @param paths Lista de paths a leer
   * @return DataFrame unificado
   */
  def readMultipleSources(spark: SparkSession, paths: Seq[String]): DataFrame = {
    import spark.implicits._
    
    val dfs = paths.map(path => 
      spark.read.option("header", "true").csv(path)
    )
    
    dfs.reduce(_ union _)  // Union de todos los DataFrames
  }
  
  /**
   * Helper: Escribe con reparticionamiento para optimizar archivos.
   * 
   * @param df DataFrame a escribir
   * @param path Output path
   * @param partitionCol Columna para particionar
   */
  def writeOptimized(df: DataFrame, path: String, partitionCol: String): Unit = {
    df.repartition(10, col(partitionCol))  // 10 particiones (ajustar según tamaño)
      .write
      .mode("overwrite")
      .partitionBy(partitionCol)
      .parquet(path)
  }
}

/* ============================================================================
 * PARETO 20% - Lo que DEBES saber de Spark Scala
 * ============================================================================
 * 
 * 1. SparkSession:
 *    - Entry point para Spark 2+
 *    - .config() para tuning
 *    - import spark.implicits._ para syntax sugar
 * 
 * 2. DataFrames (API principal):
 *    - Inmutables (cada transformación crea nuevo DF)
 *    - Lazy evaluation (solo se ejecutan en actions)
 *    - Schema-aware (typed)
 * 
 * 3. Transformaciones core (80% de uso):
 *    - select(): elegir columnas
 *    - filter() / where(): filtrar filas
 *    - withColumn(): añadir/modificar columna
 *    - groupBy().agg(): agregaciones
 *    - join(): combinar DataFrames
 *    - orderBy() / sort(): ordenar
 * 
 * 4. Actions (triggers de ejecución):
 *    - count(): contar filas
 *    - show(): mostrar datos (dev only)
 *    - write: escribir a disco
 *    - collect(): traer a driver (EVITAR con datos grandes!)
 * 
 * 5. Functions más usados (import org.apache.spark.sql.functions._):
 *    - col(), lit(): referencias a columnas
 *    - when(), otherwise(): condicionales
 *    - coalesce(): manejar nulls
 *    - sum(), avg(), count(), max(), min(): agregaciones
 *    - date_format(), to_date(): manejo de fechas
 *    - row_number(), rank(): window functions
 * 
 * 6. Particionado:
 *    - .partitionBy("col"): particionar al escribir (CLAVE para performance)
 *    - .repartition(n): redistribuir particiones en memoria
 *    - .coalesce(n): reducir particiones (sin shuffle)
 * 
 * 7. Best Practices:
 *    - Usar schema explícito en lectura (producción)
 *    - Evitar .collect() con datos grandes
 *    - Particionar por columnas frecuentemente filtradas (ej: date)
 *    - Usar .cache() para DataFrames reutilizados
 *    - preferir .parquet sobre .csv (10x más rápido)
 * 
 * 8. Configuraciones importantes:
 *    - spark.sql.shuffle.partitions: # de particiones en aggregations (default 200)
 *    - spark.sql.adaptive.enabled: optimizaciones automáticas (Spark 3+)
 *    - spark.executor.memory: memoria por executor
 *    - spark.executor.cores: cores por executor
 * 
 * EVITAR (anti-patterns):
 *    - collect() en DataFrames grandes
 *    - UDFs cuando existen funciones built-in
 *    - .show() en loops
 *    - Múltiples writes del mismo DF (cachear antes)
 * 
 * TROUBLESHOOTING:
 *    - Out of Memory: aumentar spark.executor.memory o reducir partitions
 *    - Shuffle too large: aumentar spark.sql.shuffle.partitions
 *    - Slow queries: verificar plan con .explain()
 *    - Skewed data: usar salting o repartition con expresión custom
 * 
 * NEXT STEPS:
 *    1. Compilar este código con sbt
 *    2. Ejecutar localmente con datos de prueba
 *    3. Ver plan de ejecución con df.explain()
 *    4. Optimizar basado en métricas de Spark UI
 * 
 * ============================================================================
 */
