# Actividad Interactiva — Observabilidad y Cost Management

🎯 Objetivo
Instrumentar un pipeline sencillo para exponer métricas básicas (success/fail, duration, rows processed), crear una alerta y visualizar en un dashboard.

🟢 Ejercicio 1: Añadir métricas simples a un job (20 minutos)  
Objetivo: Exportar métricas desde un script Python usando prometheus_client.

Ejemplo (snippet):
```python
from prometheus_client import Summary, Counter, start_http_server

REQUEST_TIME = Summary('job_duration_seconds', 'Time spent processing job')
ROWS_PROCESSED = Counter('rows_processed', 'Number of rows processed')

@REQUEST_TIME.time()
def run_job():
    # run ETL
    ROWS_PROCESSED.inc(1234)

if __name__ == '__main__':
    start_http_server(8000)
    run_job()
```

Verificación:
- `curl http://localhost:8000/metrics` -> observas `job_duration_seconds` y `rows_processed`.
- Resultado rows_processed: __

Duración: 20 minutos

📊 Ejercicio 2: Crear alerta Prometheus (25 minutos)  
Objetivo: Definir una alert rule si job fails o duration > threshold.

Ejemplo rule (prometheus_rules.yml):
```yaml
groups:
- name: dataeng.rules
  rules:
  - alert: JobDurationHigh
    expr: job_duration_seconds_count > 0 and job_duration_seconds_sum / job_duration_seconds_count > 300
    for: 5m
    labels:
      severity: warning
    annotations:
      summary: "Job duration is high"
```

Verificación:
- Cargar rule en Prometheus / simular métricas -> alert fires? Yes / No

Duración: 25 minutos

📈 Ejercicio 3: Dashboard simple en Grafana (30 minutos)  
Objetivo: Crear panel con job success rate, avg duration, rows processed.

Pasos:
1. Añadir Prometheus como datasource en Grafana.
2. Crear panel con PromQL queries:
   - Success rate: `sum(increase(job_success_total[1h])) / sum(increase(job_runs_total[1h]))`
   - Avg duration: `rate(job_duration_seconds_sum[5m]) / rate(job_duration_seconds_count[5m])`

Verificación:
- Captura del panel: __ (pegar enlace o screenshot)

Duración: 30 minutos

💸 Ejercicio 4: Cost optimization checklist (30 minutos)  
Objetivo: Revisar configuración de cluster y proponer ajustes.

Checklist (práctico):
- ¿Clusters auto-terminate configurados? Yes / No
- ¿Uso de spot/preemptible nodes posible? Yes / No
- ¿Cache / reuse data entre jobs? Yes / No
- ¿Databricks delta cache o parquet pruning habilitado? Yes / No

Verificación: responde checklist y anota 3 acciones de ahorro estimadas con %.

Duración: 30 minutos

📦 Mini-proyecto (2 horas)  
Objetivo: Instrumentar un pipeline ETL con métricas, crear un dashboard básico y una regla de alerting que notifique por Slack/Email cuando falla.

Entregables:
- script/metrics_exporter.py
- prometheus_rules.yml
- grafana_dashboard.json (o screenshot)
- runbook_observability.md (procedimiento de respuesta)

Duración: 2 horas
