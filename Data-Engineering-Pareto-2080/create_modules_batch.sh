#!/bin/bash

# This script creates template files for all remaining modules
# We'll populate them with actual content afterwards

MODULES=(
  "01-intro-pareto:Introducción al Pareto 20/80"
  "02-sql-core:SQL Core"
  "03-python-etl-basics:Python ETL Basics"
  "04-spark-scala-fundamentals:Spark Scala Fundamentals"
  "05-databricks-workflow:Databricks Workflow"
  "06-delta-lake-storage:Delta Lake & Storage"
  "07-dbt-transforms:DBT or Transforms"
  "08-airflow-orchestration:Airflow Orchestration"
  "09-testing-data-quality:Testing & Data Quality"
  "10-observability-cost:Observability & Cost"
  "11-security-governance:Security & Governance"
  "12-final-project:Final Project"
)

for module_info in "${MODULES[@]}"; do
  IFS=':' read -r module_dir module_name <<< "$module_info"
  echo "Creating placeholders for $module_dir..."
  
  # Create directory if needed
  mkdir -p "$module_dir"
  
  # Create placeholder files if they don't exist
  for file in README.md actividad-interactiva.md progreso.md retroalimentacion.md recursos.md; do
    if [ ! -f "$module_dir/$file" ]; then
      echo "# $module_name - $file" > "$module_dir/$file"
      echo "" >> "$module_dir/$file"
      echo "Contenido en desarrollo..." >> "$module_dir/$file"
    fi
  done
done

echo "Placeholder files created!"
