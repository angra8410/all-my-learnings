# 🚀 Módulo 00 — Plan & Setup

## 🎯 Objetivos de Aprendizaje

Al completar este módulo serás capaz de:

1. **Configurar un entorno completo de Data Engineering** con todas las herramientas necesarias
2. **Ejecutar Spark local, Airflow y PostgreSQL** en contenedores Docker
3. **Crear cuenta en Databricks Community Edition** (gratis)
4. **Descargar datasets de práctica** para los proyectos del curso
5. **Validar que todo funciona correctamente** antes de comenzar con el contenido técnico

---

## 📚 Contenido Teórico

### 1. Stack Tecnológico del Curso (Pareto 20/80)

Este curso se enfoca en las herramientas que **maximizan el impacto profesional**:

| Herramienta | Propósito | 20% Core Skill |
|------------|-----------|----------------|
| **SQL** | Queries, transformaciones | JOINs, window functions, MERGE |
| **Python** | ETL scripting | pandas, requests, psycopg2 |
| **Spark (Scala)** | Procesamiento distribuido | DataFrame API, particionBy |
| **Databricks** | Plataforma cloud para Spark | Notebooks, Jobs, Delta Lake |
| **Airflow** | Orquestación de workflows | DAGs, retries, scheduling |
| **PostgreSQL** | Base de datos relacional | DDL, DML, indexes |
| **Docker** | Containerización | docker run, docker-compose |
| **Git/GitHub** | Versionado | commit, push, pull, branches |

### 2. Arquitectura del Entorno de Desarrollo

```
┌─────────────────────────────────────────────────────────────┐
│                    Tu Laptop / Desktop                      │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌─────────────────┐  │
│  │   Docker     │  │  VSCode /    │  │   Git / GitHub  │  │
│  │              │  │  IntelliJ    │  │                 │  │
│  │ - PostgreSQL │  │              │  │  - Repos        │  │
│  │ - Airflow    │  │  - Scala     │  │  - CI/CD        │  │
│  │ - Spark local│  │  - Python    │  │                 │  │
│  └──────────────┘  └──────────────┘  └─────────────────┘  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
                  ┌────────────────────────┐
                  │  Databricks Community  │
                  │  (Cloud - Gratis)      │
                  │                        │
                  │  - Notebooks           │
                  │  - Clusters            │
                  │  - Delta Lake          │
                  └────────────────────────┘
```

### 3. Requisitos del Sistema

**Hardware mínimo:**
- RAM: 8GB (recomendado 16GB)
- Disco: 30GB libres
- CPU: 4 cores (recomendado)

**Sistema Operativo:**
- Windows 10/11 Pro (con WSL2 para Docker)
- macOS 11+ (Big Sur o superior)
- Linux (Ubuntu 20.04+, Debian, Fedora)

---

## 🛠️ Instalaciones Paso a Paso

### 4.1 Git

**Windows:**
```bash
# Descargar e instalar desde:
# https://git-scm.com/download/win

# Verificar instalación
git --version
```

**macOS:**
```bash
# Con Homebrew
brew install git

# O con Xcode Command Line Tools
xcode-select --install

# Verificar
git --version
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install git -y
git --version
```

**Configuración inicial:**
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu-email@ejemplo.com"
git config --global init.defaultBranch main
```

### 4.2 Docker Desktop

**Windows/Mac:**
- Descargar desde: https://www.docker.com/products/docker-desktop
- Instalar siguiendo el wizard
- **Windows:** Asegurar que WSL2 esté habilitado

**Linux:**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install docker.io docker-compose -y
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
# Cerrar sesión y volver a entrar para aplicar cambios
```

**Verificación:**
```bash
docker --version
docker ps
docker run hello-world
```

### 4.3 Python 3.9+

**Windows:**
- Descargar desde: https://www.python.org/downloads/
- ✅ Marcar "Add Python to PATH" durante instalación

**macOS:**
```bash
brew install python@3.11
python3 --version
```

**Linux:**
```bash
sudo apt install python3 python3-pip python3-venv -y
python3 --version
```

### 4.4 VSCode (Editor Recomendado)

**Descarga:** https://code.visualstudio.com/

**Extensiones esenciales:**
```
- Python (Microsoft)
- Docker (Microsoft)
- GitLens
- Scala (Metals) — si usarás Scala localmente
- YAML
- Rainbow CSV
```

**Instalación rápida de extensiones:**
```bash
code --install-extension ms-python.python
code --install-extension ms-azuretools.vscode-docker
code --install-extension eamodio.gitlens
code --install-extension scalameta.metals
code --install-extension redhat.vscode-yaml
```

### 4.5 Scala y sbt (Opcional — para desarrollo local)

**macOS:**
```bash
brew install scala sbt
```

**Linux:**
```bash
# Instalar SDKMAN
curl -s "https://get.sdkman.io" | bash
source "$HOME/.sdkman/bin/sdkman-init.sh"

# Instalar Scala y sbt
sdk install scala
sdk install sbt
```

**Windows:**
- Descargar desde: https://www.scala-lang.org/download/
- Instalar sbt desde: https://www.scala-sbt.org/download.html

---

## 🐳 Servicios Docker

### 5.1 PostgreSQL

```bash
docker run --name postgres-pareto \
  -e POSTGRES_USER=dataeng \
  -e POSTGRES_PASSWORD=pareto2080 \
  -e POSTGRES_DB=learning_db \
  -p 5432:5432 \
  -d postgres:15

# Verificar
docker ps | grep postgres
docker exec -it postgres-pareto psql -U dataeng -d learning_db -c "SELECT version();"
```

### 5.2 Apache Airflow (Standalone)

```bash
# Crear directorio para Airflow
mkdir -p ~/airflow-pareto/{dags,logs,plugins}
cd ~/airflow-pareto

# Crear docker-compose.yml (ver recursos.md para contenido completo)
# O usar imagen standalone simplificada:
docker run -d \
  --name airflow-standalone \
  -p 8080:8080 \
  -v $(pwd)/dags:/opt/airflow/dags \
  -e AIRFLOW__CORE__LOAD_EXAMPLES=False \
  apache/airflow:2.7.0-python3.11 standalone

# Esperar ~2 minutos para inicialización
# Acceder: http://localhost:8080
# User: admin
# Password: admin (o ver logs con `docker logs airflow-standalone`)
```

### 5.3 Spark Local (Opcional)

```bash
# Imagen con Jupyter + PySpark
docker run -d \
  --name spark-local \
  -p 8888:8888 \
  -p 4040:4040 \
  -v $(pwd)/notebooks:/home/jovyan/work \
  jupyter/pyspark-notebook

# Obtener token para Jupyter
docker logs spark-local 2>&1 | grep "127.0.0.1:8888/lab?token="
```

---

## ☁️ Databricks Community Edition

### 6.1 Crear Cuenta (Gratis)

1. Ir a: https://community.cloud.databricks.com/login.html
2. Click en **"Sign up for Community Edition"**
3. Completar formulario con email personal
4. Verificar email
5. Login y explorar interfaz

### 6.2 Crear Primer Cluster

```
1. Ir a "Compute" en sidebar
2. Click "Create Cluster"
3. Configuración:
   - Cluster Name: "learning-cluster"
   - Cluster Mode: Single Node
   - Databricks Runtime: 13.3 LTS (Scala 2.12, Spark 3.4.1)
   - Node type: (default — Community Edition usa nodos fijos)
4. Click "Create Cluster"
5. Esperar ~5-7 minutos a que inicie
```

### 6.3 Probar con Notebook

```scala
// Crear notebook nuevo (Create > Notebook)
// Lenguaje: Scala
// Cluster: learning-cluster

// Cell 1: Verificar Spark
println(s"Spark version: ${spark.version}")

// Cell 2: Crear DataFrame de prueba
val data = Seq(
  ("Alice", 28, "Engineer"),
  ("Bob", 35, "Manager"),
  ("Charlie", 42, "Director")
)
val df = data.toDF("name", "age", "role")
df.show()

// Cell 3: Transformación simple
df.filter($"age" > 30).select("name", "role").show()
```

---

## 📊 Datasets de Práctica

### 7.1 Descargar Datasets

Crear carpeta local:
```bash
mkdir -p ~/data-engineering-pareto/datasets
cd ~/data-engineering-pareto/datasets
```

**Dataset 1: E-commerce Sales**
```bash
# Descargar (simulado — usar datos propios o generar con script)
# Ver recursos.md para links a datasets públicos
# Ejemplo: Kaggle Retail Data, UCI ML Repository
```

**Dataset 2: Weather API**
```bash
# Registro en OpenWeatherMap (gratis)
# API Key: <YOUR_API_KEY>
# Endpoint: https://api.openweathermap.org/data/2.5/weather
```

**Dataset 3: Mock Transaction Data**
```python
# Script Python para generar datos sintéticos
# Ver recursos.md para script completo
```

---

## ✅ Checklist de Verificación

Antes de avanzar al Módulo 01, verifica:

- [ ] Git instalado y configurado (`git --version`)
- [ ] Docker funcionando (`docker ps` sin errores)
- [ ] PostgreSQL corriendo (`docker ps | grep postgres`)
- [ ] Conexión exitosa a PostgreSQL (`docker exec -it postgres-pareto psql -U dataeng`)
- [ ] Airflow accesible en http://localhost:8080
- [ ] Python 3.9+ instalado (`python3 --version`)
- [ ] VSCode con extensiones instaladas
- [ ] Cuenta Databricks Community creada
- [ ] Cluster Databricks iniciado y funcional
- [ ] Carpeta `~/data-engineering-pareto/datasets` creada
- [ ] Repositorio clonado y rama personal creada

---

## 🎯 Entregables

1. ✅ Screenshot de `docker ps` mostrando contenedores corriendo
2. ✅ Screenshot de Airflow UI (http://localhost:8080)
3. ✅ Screenshot de Databricks notebook ejecutando código Scala
4. ✅ Archivo `setup-verification.md` con outputs de comandos de verificación

---

## ⏱️ Duración Estimada

- **Instalaciones:** 1-2 horas
- **Configuración Docker:** 30 minutos
- **Databricks setup:** 20 minutos
- **Verificaciones:** 30 minutos

**Total: 3-4 horas**

---

## 📚 Recursos Adicionales

Ver `recursos.md` para:
- Scripts de instalación automatizada
- Troubleshooting común
- docker-compose.yml completo para Airflow
- Scripts Python para generar datasets sintéticos

---

## ⏭️ Siguiente Paso

Una vez completada la configuración, estarás listo para **Módulo 01: Introducción al Pareto 20/80**, donde aprenderás la metodología de estudio y planificarás tu roadmap personalizado.

---

**💡 Consejo Pro:** Si encuentras problemas con Docker en Windows, asegúrate de que WSL2 esté correctamente configurado y que Docker Desktop esté usando el backend WSL2. En Mac con chip M1/M2, usa imágenes ARM64 cuando sea posible para mejor performance.
