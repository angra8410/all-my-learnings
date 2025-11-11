# Módulo 06 — Delta Lake & Storage (Pareto 20/80)

Objetivo general:
Entender y aplicar el 20% de Delta Lake y arquitecturas de almacenamiento que producen el 80% del beneficio: almacenamiento transaccional (ACID), upserts/merge, time travel, particionamiento y optimizaciones de lectura/escritura.

Resultados de aprendizaje:
- Comprender las diferencias entre Data Lake (Parquet) y Delta Lake.
- Realizar MERGE/UPSERT sobre tablas Delta.
- Usar Time Travel para inspeccionar y restaurar versiones.
- Aplicar particionamiento y optimizaciones (Z-Order / OPTIMIZE cuando aplique en Databricks).
- Estrategias de esquema y housekeeping (VACUUM / retention).

Contenido (resumen):
1. Qué es Delta Lake y por qué usarlo
2. Formatos: Parquet vs Delta
3. MERGE INTO / upsert patterns
4. Time travel y versiones
5. Particionamiento y archivos pequeños
6. Housekeeping (VACUUM / retention) y buenas prácticas

Duración estimada: 8-12 horas
Prerequisitos: Spark/Databricks básico, ejemplos de datos (CSV/Parquet) y acceso a un cluster (local/Databricks).

Pareto 20/80:
- 20% para aprender: MERGE pattern, time travel basic, partitioning, OPTIMIZE concepts.
- 80% para practicar: implementar un pipeline que escriba Delta particionado y que soporte upserts diarios, luego probar time travel y vacuum.

Estructura del módulo:
- actividad-interactiva.md (ejercicios detallados)
- progreso.md
- retroalimentacion.md
- recursos.md
- ejemplos: scripts de MERGE, comandos Spark SQL y notas para Databricks
