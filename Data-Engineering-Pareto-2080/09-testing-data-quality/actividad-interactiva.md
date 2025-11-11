# Actividad Interactiva — Testing y Calidad de Datos

🎯 Objetivo
Construir y automatizar una suite de tests para un pipeline ETL simple (ingest → transform → load) usando tests SQL, pruebas unitarias en Python y un perfilado básico con Great Expectations. Integrar los tests en CI/airflow.

🧪 Ejercicio 1: Preparar entorno de tests (15 minutos)  
Objetivo: Instalar pytest y Great Expectations (opcional).

Pasos:
1. Activa tu venv (si no lo tienes creado, crea uno).
```bash
python3 -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
pip install --upgrade pip
```
2. Instala dependencias:
```bash
pip install pytest great_expectations sqlalchemy psycopg2-binary
```

Verificación:
- `pytest --version` -> _______________
- `great_expectations --version` -> _______________

Duración: 15 minutos

✅ Ejercicio 2: Tests unitarios para funciones de transformación (30 minutos)  
Objetivo: Escribir tests pytest para una función `normalize` (p. ej. en `my_etl.py`).

Código ejemplo (archivo: examples/tests/test_normalize.py):
```python
import pandas as pd
from my_etl import normalize

def test_normalize_trim_and_lower():
    df = pd.DataFrame({'producto': [' AbC ', None]})
    out = normalize(df)
    assert out['producto'].iloc[0] == 'abc'
    assert out['producto'].iloc[1] == ''
```

Pasos:
1. Crea `examples/tests/test_normalize.py` con el contenido anterior.
2. Ejecuta `pytest -q`.

Verificación:
- Tests passed: __ / __
- Tiempo ejecución tests: __ seconds

Duración: 30 minutos

🔍 Ejercicio 3: Checks SQL básicos (40 minutos)  
Objetivo: Implementar comprobaciones SQL que detecten nulls, duplicados, outliers y discrepancias de row counts.

Comandos/queries ejemplo (Postgres):
```sql
-- Row count
SELECT COUNT(*) AS total_rows FROM ventas;

-- Null check (cliente_id)
SELECT COUNT(*) AS null_cliente FROM ventas WHERE cliente_id IS NULL;

-- Duplicates by order_id
SELECT order_id, COUNT(*) AS cnt FROM ventas GROUP BY order_id HAVING COUNT(*) > 1;

-- Range check (total >= 0)
SELECT COUNT(*) AS negative_totals FROM ventas WHERE total < 0;
```

Verificación: Copia resultados:
- total_rows: __
- null_cliente: __
- duplicates_found: __
- negative_totals: __

Duración: 40 minutos

🧰 Ejercicio 4: Great Expectations — primer perfilado y suite (45 minutos)  
Objetivo: Inicializar GE, crear datasource y un expectation suite básico para `ventas`.

Pasos (básicos):
```bash
great_expectations init
# Añadir datasource: puede ser SQLAlchemy hacia Postgres
great_expectations datasource new --name my_pg --type sqlalchemy
# Crear expectation suite interactivo
great_expectations suite new
# Añadir expectations: expect_column_values_to_not_be_null(order_id), expect_column_values_to_be_unique(order_id), expect_column_values_to_be_between(total, min_value=0)
```

Verificación:
- Ejecutar checkpoint: `great_expectations checkpoint run <checkpoint_name>`
- Estado del run: success / failed -> __

Duración: 45 minutos

🔁 Ejercicio 5: Integrar tests en CI (GitHub Actions) (40 minutos)  
Objetivo: Crear un job en GitHub Actions que ejecute pytest + GE checkpoint en PRs.

Snippet de ejemplo para .github/workflows/ci-tests.yml:
```yaml
name: CI - Tests

on:
  pull_request:
    branches: [ main, feat/data-engineering-roadmap ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Install deps
        run: pip install -r requirements.txt
      - name: Run unit tests
        run: pytest -q
      - name: Run Great Expectations checkpoint
        run: great_expectations checkpoint run my_checkpoint || true
```

Verificación en CI: logs muestran `pytest` pass -> Yes / No

Duración: 40 minutos

📦 Mini-proyecto (2 horas)  
Objetivo: Construir suite combinada (pytest + SQL checks + GE) y configurarla en CI. Generar un reporte con métricas clave (row counts, % nulls por columna, tests passed/failed) y un runbook corto que indique acciones a tomar si un test falla (rollback, alert, retries).

Entregables:
- `examples/tests/` - pytest files
- `great_expectations/` - GE suite (o instrucciones para generarlo)
- `.github/workflows/ci-tests.yml` - CI snippet
- `reports/qa_report_YYYYMMDD.md` - ejemplo de reporte

Duración: 2 horas

📊 Resumen de Tiempo
Ejercicio	Duración
1. Preparar entorno	15 min
2. Unit tests	30 min
3. SQL checks	40 min
4. Great Expectations	45 min
5. Integrar a CI	40 min
Mini-proyecto	120 min
TOTAL ~5.5 horas

Próximo paso: añade los ejemplos en `Data-Engineering-Roadmap/examples/` y actualiza `progreso.md`.
