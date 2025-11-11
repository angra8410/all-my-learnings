# Actividad Interactiva — Python ETL

🎯 Objetivo
Construir y verificar scripts ETL reproducibles que lean CSV y APIs, normalicen datos y carguen a una tabla en Postgres.

🐍 Ejercicio 1: Entorno Python y virtualenv (10 minutos)
Objetivo: Crear y activar un entorno virtual.

Pasos:
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate   # Windows
pip install --upgrade pip
```
Verificación: `python --version` -> _______________

Duración: 10 minutos

🐍 Ejercicio 2: Instala dependencias (5 minutos)
Objetivo: Instalar pandas, sqlalchemy, requests, psycopg2-binary.

Pasos:
```bash
pip install pandas sqlalchemy requests psycopg2-binary pytest
```
Verificación: `pip list | grep pandas` -> _______________

Duración: 5 minutos

📥 Ejercicio 3: Script de ingestión desde CSV (25 minutos)
Objetivo: Escribir un script `ingest_csv.py` que lea `data/sales_sample.csv`, normalice columnas (trim, lower) y escriba a Postgres.

Pasos (esqueleto):
```python
# ingest_csv.py (pseudocódigo)
import pandas as pd
from sqlalchemy import create_engine

def normalize(df):
    df['producto']=df['producto'].str.strip().str.lower()
    return df

if __name__=='__main__':
    df = pd.read_csv('data/sales_sample.csv')
    df = normalize(df)
    engine = create_engine('postgresql://postgres:pass@localhost:5432/postgres')
    df.to_sql('ventas', engine, if_exists='append', index=False)
```

Verificación: `SELECT COUNT(*) FROM ventas;` -> _______________

Duración: 25 minutos

🔁 Ejercicio 4: Consumir API pública y guardar CSV (20 minutos)
Objetivo: Consumir ejemplo de API y almacenar datos localmente.

Pasos:
```python
import requests
resp = requests.get('https://jsonplaceholder.typicode.com/posts')
resp.raise_for_status()
data = resp.json()
# transformar y guardar
```
Verificación: Number of records saved: _______________

Duración: 20 minutos

🧪 Ejercicio 5: Tests unitarios con pytest (20 minutos)
Objetivo: Crear tests para la función `normalize`.

Pasos:
```python
# test_normalize.py
from ingest_csv import normalize

def test_normalize_trim_and_lower():
    df = pd.DataFrame({'producto':[' AbC ','XYZ']})
    out = normalize(df)
    assert out['producto'].iloc[0] == 'abc'
```

Ejecuta: `pytest -q` Verificación: tests passed -> _______________

Duración: 20 minutos

📦 Ejercicio 6: Mini-proyecto ETL (2 horas)
Objetivo: Crear pipeline que cargue CSV + API, realice deduplicación y cargue a tabla `ventas_mart`.

Entregables:
- scripts/ingest_csv.py
- scripts/ingest_api.py
- tests/test_normalize.py

Duración: 2 horas

Resumen de tiempo: total estimado ~3 horas  (práctica intensiva)
