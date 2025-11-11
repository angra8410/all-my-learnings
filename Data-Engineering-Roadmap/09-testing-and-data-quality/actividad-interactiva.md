# Actividad Interactiva — Testing y Calidad de Datos

🎯 Objetivo
Construir y automatizar una suite de tests para un pipeline ETL simple (ingest → transform → load) usando tests SQL y pruebas unitarias en Python. Implementar al menos 5 checks de calidad.

🧪 Ejercicio 1: Preparar entorno de tests (15 minutos)
Objetivo: Instalar pytest y Great Expectations (opcional) en el entorno.

Pasos:
```bash
pip install pytest great_expectations
```
Verificación: `pytest --version` -> _______________ ; `great_expectations --version` -> _______________

Duración: 15 minutos

✅ Ejercicio 2: Tests unitarios para funciones de transformación (30 minutos)
Objetivo: Escribir tests pytest para una función normalize/clean en Python.

Ejemplo test (tests/test_normalize.py):
```python
import pandas as pd
from my_etl import normalize

def test_normalize_basic():
    df = pd.DataFrame({'producto':[' A ', None]})
    out = normalize(df)
    assert out['producto'].iloc[0] == 'a'
    assert out['producto'].iloc[1] == ''
```
Verificación: `pytest -q` -> tests passed: __ / __

Duración: 30 minutos

🔍 Ejercicio 3: SQL checks básicos (40 minutos)
Objetivo: Implementar comprobaciones SQL que comprueben nulls, uniqueness y rangos.

SQL examples:
```sql
-- Row count
SELECT COUNT(*) FROM ventas;

-- Null check
SELECT COUNT(*) FROM ventas WHERE cliente_id IS NULL;

-- Uniqueness check (order_id)
SELECT order_id, COUNT(*) FROM ventas GROUP BY order_id HAVING COUNT(*) > 1;

-- Range check (total >= 0)
SELECT COUNT(*) FROM ventas WHERE total < 0;
```
Verificación: Copia los resultados: total_rows: __ ; null_cliente: __ ; duplicates_found: __ ; negative_totals: __

Duración: 40 minutos

📦 Ejercicio 4: Integrar Great Expectations (45 minutos)
Objetivo: Crear un suite básica de GE para la tabla `ventas`.

Pasos:
```bash
great_expectations init
great_expectations datasource new --name my_pg --type sql
# create expectation suite
great_expectations suite new
# add expectations: expect_column_values_to_not_be_null, expect_column_values_to_be_unique, etc.
```
Verificación: `great_expectations checkpoint run <checkpoint_name>` -> status: __

Duración: 45 minutos

🔁 Ejercicio 5: Añadir tests al pipeline (Airflow/CI) (40 minutos)
Objetivo: Añadir un step en Airflow DAG o GitHub Actions que corra los tests antes de promover datos.

Pasos (GitHub Actions snippet):
```yaml
- name: Run tests
  run: |
    pytest -q
    great_expectations checkpoint run my_checkpoint
```
Verificación: action logs show success -> Yes / No

Duración: 40 minutos

🧾 Mini-proyecto (2 horas)
Objetivo: Crear la suite completa que combine pytest + SQL checks + Great Expectations y añadirla a CI. Produce un informe de resultados.

Entregables:
- folder tests/ con pytest
- examples/ge_suite/
- CI snippet en .github/workflows

Duración: 2 horas

Resumen del tiempo
Ejercicio	Duración
1. Preparar entorno	15 min
2. Unit tests	30 min
3. SQL checks	40 min
4. Great Expectations	45 min
5. Integrar a CI	40 min
Mini-proyecto	120 min
TOTAL ~5.5 horas

Próximo paso: subir la carpeta tests/ y el GE suite al repo y enlazar en progreso.md.
