# 📚 Recursos — Módulo 00: Plan & Setup

## 🔗 Documentación Oficial

### Herramientas Principales

**Git:**
- Docs oficial: https://git-scm.com/doc
- Pro Git Book (gratis): https://git-scm.com/book/en/v2
- GitHub Learning Lab: https://lab.github.com/

**Docker:**
- Docs oficial: https://docs.docker.com/
- Get Started Guide: https://docs.docker.com/get-started/
- Docker Hub: https://hub.docker.com/

**PostgreSQL:**
- Docs oficial: https://www.postgresql.org/docs/
- Tutorial interactivo: https://www.postgresqltutorial.com/
- pgAdmin (GUI client): https://www.pgadmin.org/

**Apache Airflow:**
- Docs oficial: https://airflow.apache.org/docs/
- Quickstart: https://airflow.apache.org/docs/apache-airflow/stable/start.html
- Best Practices: https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html

**Databricks:**
- Community Edition: https://community.cloud.databricks.com/
- Docs oficial: https://docs.databricks.com/
- Getting Started: https://docs.databricks.com/getting-started/index.html
- Spark Scala Guide: https://spark.apache.org/docs/latest/api/scala/org/apache/spark/index.html

**Scala:**
- Docs oficial: https://docs.scala-lang.org/
- Scala Exercises: https://www.scala-exercises.org/
- sbt Documentation: https://www.scala-sbt.org/1.x/docs/

---

## 🐳 Docker Compose para Airflow (Completo)

**Archivo:** `docker-compose.yml` (para setup avanzado)

```yaml
version: '3.8'

x-airflow-common:
  &airflow-common
  image: apache/airflow:2.7.0-python3.11
  environment:
    &airflow-common-env
    AIRFLOW__CORE__EXECUTOR: LocalExecutor
    AIRFLOW__DATABASE__SQL_ALCHEMY_CONN: postgresql+psycopg2://airflow:airflow@postgres/airflow
    AIRFLOW__CORE__FERNET_KEY: ''
    AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION: 'true'
    AIRFLOW__CORE__LOAD_EXAMPLES: 'false'
    AIRFLOW__API__AUTH_BACKENDS: 'airflow.api.auth.backend.basic_auth'
  volumes:
    - ./dags:/opt/airflow/dags
    - ./logs:/opt/airflow/logs
    - ./plugins:/opt/airflow/plugins
  user: "${AIRFLOW_UID:-50000}:0"
  depends_on:
    postgres:
      condition: service_healthy

services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_USER: airflow
      POSTGRES_PASSWORD: airflow
      POSTGRES_DB: airflow
    volumes:
      - postgres-db-volume:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD", "pg_isready", "-U", "airflow"]
      interval: 5s
      retries: 5
    ports:
      - "5433:5432"

  airflow-webserver:
    <<: *airflow-common
    command: webserver
    ports:
      - "8080:8080"
    healthcheck:
      test: ["CMD", "curl", "--fail", "http://localhost:8080/health"]
      interval: 10s
      timeout: 10s
      retries: 5
    restart: always

  airflow-scheduler:
    <<: *airflow-common
    command: scheduler
    healthcheck:
      test: ["CMD-SHELL", 'airflow jobs check --job-type SchedulerJob --hostname "$${HOSTNAME}"']
      interval: 10s
      timeout: 10s
      retries: 5
    restart: always

  airflow-init:
    <<: *airflow-common
    entrypoint: /bin/bash
    command:
      - -c
      - |
        mkdir -p /sources/logs /sources/dags /sources/plugins
        chown -R "${AIRFLOW_UID:-50000}:0" /sources/{logs,dags,plugins}
        exec /entrypoint airflow db init
        airflow users create \
          --username admin \
          --firstname Admin \
          --lastname User \
          --role Admin \
          --email admin@example.com \
          --password admin
    environment:
      <<: *airflow-common-env
      _AIRFLOW_DB_UPGRADE: 'true'
      _AIRFLOW_WWW_USER_CREATE: 'true'
      _AIRFLOW_WWW_USER_USERNAME: admin
      _AIRFLOW_WWW_USER_PASSWORD: admin
    user: "0:0"
    volumes:
      - .:/sources

volumes:
  postgres-db-volume:
```

**Uso:**
```bash
# Crear archivo docker-compose.yml con contenido anterior
cd ~/airflow-pareto

# Inicializar
docker-compose up airflow-init

# Levantar servicios
docker-compose up -d

# Ver logs
docker-compose logs -f

# Detener
docker-compose down
```

---

## 🐍 Script Python para Generar Datasets Sintéticos

**Archivo:** `generate_synthetic_data.py`

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Dataset 1: E-commerce Sales
def generate_ecommerce_data(n_rows=10000):
    """Genera datos sintéticos de ventas e-commerce"""
    
    categories = ['Electronics', 'Clothing', 'Home', 'Sports', 'Books']
    regions = ['North', 'South', 'East', 'West']
    
    np.random.seed(42)
    
    start_date = datetime(2023, 1, 1)
    dates = [start_date + timedelta(days=random.randint(0, 365)) for _ in range(n_rows)]
    
    data = {
        'transaction_id': [f'TXN{str(i).zfill(8)}' for i in range(1, n_rows+1)],
        'date': dates,
        'customer_id': [f'CUST{random.randint(1, 5000):05d}' for _ in range(n_rows)],
        'product_id': [f'PROD{random.randint(1, 500):04d}' for _ in range(n_rows)],
        'category': [random.choice(categories) for _ in range(n_rows)],
        'region': [random.choice(regions) for _ in range(n_rows)],
        'quantity': np.random.randint(1, 10, n_rows),
        'unit_price': np.round(np.random.uniform(10, 500, n_rows), 2),
        'discount': np.round(np.random.uniform(0, 0.3, n_rows), 2)
    }
    
    df = pd.DataFrame(data)
    df['total_amount'] = np.round(df['quantity'] * df['unit_price'] * (1 - df['discount']), 2)
    
    return df

# Dataset 2: Weather Data
def generate_weather_data(n_days=365):
    """Genera datos sintéticos de clima"""
    
    cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
    
    data = []
    start_date = datetime(2023, 1, 1)
    
    for day in range(n_days):
        date = start_date + timedelta(days=day)
        for city in cities:
            # Temperatura base según ciudad
            base_temp = {'New York': 15, 'Los Angeles': 22, 'Chicago': 12, 
                        'Houston': 24, 'Phoenix': 28}[city]
            
            # Variación estacional
            seasonal = 10 * np.sin((day / 365) * 2 * np.pi)
            
            data.append({
                'date': date,
                'city': city,
                'temperature': round(base_temp + seasonal + np.random.uniform(-5, 5), 1),
                'humidity': round(np.random.uniform(30, 90), 1),
                'precipitation': round(max(0, np.random.normal(0, 5)), 1),
                'wind_speed': round(np.random.uniform(0, 30), 1)
            })
    
    return pd.DataFrame(data)

# Dataset 3: User Activity Logs
def generate_user_activity(n_rows=50000):
    """Genera logs sintéticos de actividad de usuarios"""
    
    actions = ['login', 'view_page', 'click_button', 'add_to_cart', 'purchase', 'logout']
    devices = ['mobile', 'desktop', 'tablet']
    
    np.random.seed(42)
    
    start_date = datetime(2023, 1, 1)
    
    data = {
        'event_id': [f'EVT{str(i).zfill(10)}' for i in range(1, n_rows+1)],
        'timestamp': [start_date + timedelta(seconds=random.randint(0, 31536000)) for _ in range(n_rows)],
        'user_id': [f'USER{random.randint(1, 10000):06d}' for _ in range(n_rows)],
        'session_id': [f'SESS{random.randint(1, 20000):08d}' for _ in range(n_rows)],
        'action': [random.choice(actions) for _ in range(n_rows)],
        'device': [random.choice(devices) for _ in range(n_rows)],
        'page_url': [f'/page/{random.randint(1, 100)}' for _ in range(n_rows)],
        'duration_seconds': np.random.randint(1, 600, n_rows)
    }
    
    return pd.DataFrame(data)

# Main: Generar todos los datasets
if __name__ == "__main__":
    import os
    
    # Crear directorio si no existe
    output_dir = "~/data-engineering-pareto/datasets"
    os.makedirs(os.path.expanduser(output_dir), exist_ok=True)
    
    print("Generando datasets sintéticos...")
    
    # Dataset 1
    print("1/3 - E-commerce sales data...")
    ecommerce_df = generate_ecommerce_data(10000)
    ecommerce_df.to_csv(os.path.expanduser(f"{output_dir}/ecommerce_sales.csv"), index=False)
    print(f"   ✓ {len(ecommerce_df)} filas generadas")
    
    # Dataset 2
    print("2/3 - Weather data...")
    weather_df = generate_weather_data(365)
    weather_df.to_csv(os.path.expanduser(f"{output_dir}/weather_data.csv"), index=False)
    print(f"   ✓ {len(weather_df)} filas generadas")
    
    # Dataset 3
    print("3/3 - User activity logs...")
    activity_df = generate_user_activity(50000)
    activity_df.to_csv(os.path.expanduser(f"{output_dir}/user_activity.csv"), index=False)
    print(f"   ✓ {len(activity_df)} filas generadas")
    
    print("\n✅ Todos los datasets generados exitosamente!")
    print(f"   Ubicación: {output_dir}")
```

**Ejecutar:**
```bash
python3 generate_synthetic_data.py
```

---

## 🔧 Troubleshooting Común

### Docker Desktop no inicia (Windows)

**Problema:** Error "Docker Desktop requires WSL2"

**Solución:**
```powershell
# En PowerShell como Administrator
wsl --install
wsl --set-default-version 2

# Reiniciar computadora
# Abrir Docker Desktop y verificar Settings > General > "Use WSL 2 based engine"
```

### PostgreSQL: "Connection refused"

**Problema:** No se puede conectar a localhost:5432

**Diagnóstico y solución:**
```bash
# Verificar que contenedor esté corriendo
docker ps | grep postgres

# Ver logs
docker logs postgres-pareto

# Verificar puerto
docker port postgres-pareto

# Si el puerto está ocupado, usar otro
docker run --name postgres-pareto-alt \
  -e POSTGRES_USER=dataeng \
  -e POSTGRES_PASSWORD=pareto2080 \
  -e POSTGRES_DB=learning_db \
  -p 5433:5432 \
  -d postgres:15
```

### Airflow: DAGs no aparecen

**Problema:** DAG creado pero no visible en UI

**Solución:**
```bash
# Verificar montaje de volumen
docker inspect airflow-standalone | grep -A 10 Mounts

# Verificar permisos
ls -la ~/airflow-pareto/dags

# Ver logs del scheduler
docker logs airflow-standalone 2>&1 | grep -i error

# Forzar refresh (dentro del contenedor)
docker exec -it airflow-standalone airflow dags list-import-errors
```

### Databricks: Cluster stuck en "Pending"

**Problema:** Cluster no inicia después de 10+ minutos

**Solución:**
1. Verificar que estás usando **Community Edition** (no Trial)
2. Community Edition tiene límites: 1 cluster activo
3. Terminar otros clusters activos
4. Intentar crear cluster nuevamente
5. Esperar horarios de menor demanda (evitar peak hours)

### Mac M1/M2: Imágenes Docker fallan

**Problema:** "WARNING: The requested image's platform (linux/amd64) does not match..."

**Solución:**
```bash
# Usar imágenes ARM64 cuando sea posible
docker run --platform linux/arm64 ...

# O forzar emulación (más lento)
docker run --platform linux/amd64 ...
```

---

## 📖 Tutoriales Adicionales

### Git Básico (15 minutos)
```bash
# Comandos esenciales
git status                    # Ver estado del repo
git add .                     # Añadir cambios
git commit -m "mensaje"       # Crear commit
git push origin <branch>      # Subir cambios
git pull                      # Bajar cambios
git branch                    # Ver branches
git checkout -b <new-branch>  # Crear y cambiar branch
```

### Docker Básico (20 minutos)
```bash
# Comandos esenciales
docker ps                     # Ver contenedores corriendo
docker ps -a                  # Ver todos (incluso stopped)
docker images                 # Ver imágenes descargadas
docker logs <container>       # Ver logs
docker exec -it <container> bash  # Entrar a contenedor
docker stop <container>       # Detener
docker start <container>      # Iniciar
docker rm <container>         # Eliminar
docker system prune           # Limpiar recursos no usados
```

### PostgreSQL Básico (30 minutos)
```sql
-- Conectarse
docker exec -it postgres-pareto psql -U dataeng -d learning_db

-- Comandos útiles
\l                  -- Listar databases
\c database_name    -- Conectar a database
\dt                 -- Listar tablas
\d table_name       -- Describir tabla
\q                  -- Salir

-- Queries básicas
SELECT * FROM table_name LIMIT 10;
INSERT INTO table_name (col1, col2) VALUES (val1, val2);
UPDATE table_name SET col1 = val WHERE condition;
DELETE FROM table_name WHERE condition;
```

---

## 🌐 Datasets Públicos Recomendados

**Kaggle (requiere cuenta gratuita):**
- Retail Data: https://www.kaggle.com/datasets/retailsales
- Weather: https://www.kaggle.com/datasets/weather-data
- E-commerce: https://www.kaggle.com/datasets/carrie1/ecommerce-data

**UCI ML Repository:**
- https://archive.ics.uci.edu/ml/index.php

**NYC Open Data:**
- https://opendata.cityofnewyork.us/

**AWS Public Datasets:**
- https://registry.opendata.aws/

**Google BigQuery Public Datasets:**
- https://cloud.google.com/bigquery/public-data

---

## 🎥 Videos Recomendados

**Docker:**
- Docker Tutorial for Beginners (TechWorld with Nana): ~30 min
- Docker Crash Course (Traversy Media): ~45 min

**Git:**
- Git and GitHub for Beginners (FreeCodeCamp): ~1 hora
- Git Tutorial (Corey Schafer): ~30 min

**Databricks:**
- Getting Started with Databricks (Databricks oficial): ~15 min
- Databricks Community Edition Tutorial: ~20 min

---

## 📝 Cheat Sheets

**Git:**
- https://education.github.com/git-cheat-sheet-education.pdf

**Docker:**
- https://docs.docker.com/get-started/docker_cheatsheet.pdf

**PostgreSQL:**
- https://www.postgresqltutorial.com/postgresql-cheat-sheet/

**Scala:**
- https://docs.scala-lang.org/cheatsheets/index.html

---

## 💬 Comunidades y Soporte

**Forums:**
- Stack Overflow: https://stackoverflow.com/
- Docker Community: https://forums.docker.com/
- Databricks Community: https://community.databricks.com/

**Discord/Slack:**
- Data Engineering Discord
- Apache Airflow Slack

**Reddit:**
- r/dataengineering
- r/apachespark
- r/docker

---

**📅 Última actualización:** 2024-01-01  
**✍️ Contribuciones:** Si encuentras un recurso útil, añádelo aquí!
