# Actividad Interactiva — Databricks Workflow

🎯 Objetivo
Configurar y ejecutar un job básico en Databricks que ejecute un notebook de transformaciones.

🐝 Ejercicio 1: Verificar acceso y CLI (15 minutos)
Objetivo: Instalar databricks-cli y autenticar con token.

Pasos:
```bash
pip install databricks-cli
databricks configure --token
# Introduce: host (https://<YOUR-DATABRICKS-INSTANCE>), token: <YOUR_TOKEN>
```
Verificación: `databricks workspace ls /` -> _______________

Duración: 15 minutos

📓 Ejercicio 2: Crear notebook parametrizado (30 minutos)
Objetivo: Crear notebook que acepte parámetros `run_date` y `env`.

Notebook pseudocódigo (Scala/Python mix):
```python
# db_notebook.py
dbutils.widgets.text('run_date', '2024-01-01')
run_date = dbutils.widgets.get('run_date')
# resto del notebook: leer data/sales_sample.csv, transformar y escribir
```
Verificación: ejecución local del notebook con parámetros -> logs output: _______________

Duración: 30 minutos

🔁 Ejercicio 3: Crear Job en Databricks UI o vía CLI (25 minutos)
Objetivo: Programar un job que ejecute el notebook diario.

CLI ejemplo:
```bash
databricks jobs create --json '{"name": "sales-daily", "new_cluster": {"spark_version": "12.1.x-scala2.12", "node_type_id": "Standard_DS3_v2", "num_workers": 2}, "notebook_task": {"notebook_path": "/Users/me/sales_notebook"}}'
```
Verificación: job created id: _______________

Duración: 25 minutos

📦 Ejercicio 4: Exportar notebook como source y ejecutar desde repo (20 minutos)
Objetivo: Mantener notebooks versionados. Usa `databricks workspace export`.

Comando de export:
```bash
databricks workspace export /Users/me/sales_notebook ./notebooks/sales_notebook.py
```
Verificación: archivo `notebooks/sales_notebook.py` en repo -> [ ]

Duración: 20 minutos
