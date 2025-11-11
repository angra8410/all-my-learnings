# Módulo 10 — Observabilidad y Cost Management (Pareto 20/80)

Objetivo general:
Conocer y aplicar lo esencial de observabilidad en pipelines de datos (logging, métricas, tracing) y prácticas de gestión de costes que maximicen ROI en producción.

Resultados de aprendizaje:
- Instrumentar métricas en jobs (Airflow, Spark, Databricks).
- Crear dashboards simples (Prometheus + Grafana o Datadog).
- Definir alertas y SLOs relevantes para pipelines.
- Aplicar estrategias de cost optimization (right-size clusters, spot instances, caching).

Duración estimada: 6–10 horas

Pareto 20/80:
- 20%: métricas clave (job success/failure, duration, data volume), logs estructurados y alerting básico.
- 80%: practicar instrumentando 3 pipelines distintos y configurar alertas + dashboard.

Estructura:
- README.md
- actividad-interactiva.md
- progreso.md
- retroalimentacion.md
- recursos.md
- examples/: prometheus alerts, grafana dashboard JSON (ejemplo), script metrics exporter
