# Actividad Interactiva — Proyecto Final (Checklist y tareas)

🎯 Objetivo
Organizar el proyecto integrador en tareas concretas y ejecutables.

Tareas recomendadas (puedes adaptar):
1. Definir alcance y datasets (1 día)
   - Documento `project/scope.md` con fuentes, volúmenes estimados y entregables.
2. Preparar entorno y datos (1–2 días)
   - Scripts para descargar/colocar datasets en `project/data/`.
3. Implementar ingest (1–2 días)
   - Scripts/notebook para cargar CSV y API a raw storage.
4. Transformaciones (3–5 días)
   - Spark job (Scala) o PySpark + dbt models para staging → marts.
5. Orquestación (1–2 días)
   - DAG Airflow que ejecute ingest → transform → tests → notify.
6. Tests y QA (1–2 días)
   - pytest, SQL checks, GE or dbt tests.
7. Observabilidad (1 día)
   - Exporter simple y alert rule.
8. Documentación y demo (1–2 días)
   - README-deploy, notebook demo, screenshots.

Verificación (hitos):
- Hito 1: `project/data/` con muestras y README -> OK / NO
- Hito 2: Ingest + landing raw reproducible -> OK / NO
- Hito 3: dbt/models or Spark transforms produce marts -> OK / NO
- Hito 4: DAG ejecuta pipeline completo -> OK / NO
- Hito 5: Tests en CI -> OK / NO

Entregables:
- `project/` (código), `project/README-deploy.md`, `project/report.md`, `project/demo.ipynb` o screenshots.
