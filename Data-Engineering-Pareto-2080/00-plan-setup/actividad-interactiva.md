# 🎯 Actividad Interactiva — Módulo 00: Plan & Setup

## Objetivo General
Configurar el entorno completo de Data Engineering con Docker, Git, Databricks y validar que todas las herramientas funcionan correctamente.

---

## 📋 Ejercicio 1: Verificación de Instalaciones Base (Duración: 15 minutos)

### 🎯 Objetivo
Confirmar que Git, Docker y Python están correctamente instalados y accesibles.

### Pasos

1. **Verificar Git**
```bash
git --version
```

**Tu salida:**
```
_______________________________________________
```

2. **Verificar Docker**
```bash
docker --version
docker ps
```

**Tu salida:**
```
_______________________________________________
_______________________________________________
```

3. **Verificar Python**
```bash
python3 --version
pip3 --version
```

**Tu salida:**
```
_______________________________________________
_______________________________________________
```

### Verificación
- ✅ Git versión 2.30 o superior
- ✅ Docker versión 20.x o superior
- ✅ Python versión 3.9 o superior
- ✅ `docker ps` ejecuta sin errores

**Duración:** 15 minutos

---

## 📋 Ejercicio 2: Configurar Git Global (Duración: 10 minutos)

### 🎯 Objetivo
Establecer tu identidad en Git para commits futuros.

### Pasos

1. **Configurar nombre y email**
```bash
git config --global user.name "Tu Nombre Completo"
git config --global user.email "tu-email@ejemplo.com"
git config --global init.defaultBranch main
```

2. **Verificar configuración**
```bash
git config --list | grep -E "user.name|user.email|init.default"
```

**Tu configuración:**
```
user.name=_______________________________________________
user.email=_______________________________________________
init.defaultBranch=_______________________________________________
```

### Verificación
- ✅ `user.name` configurado
- ✅ `user.email` configurado
- ✅ `init.defaultBranch` = main

**Duración:** 10 minutos

---

## 📋 Ejercicio 3: Levantar PostgreSQL en Docker (Duración: 20 minutos)

### 🎯 Objetivo
Ejecutar PostgreSQL en un contenedor Docker y validar conexión.

### Pasos

1. **Crear contenedor PostgreSQL**
```bash
docker run --name postgres-pareto \
  -e POSTGRES_USER=dataeng \
  -e POSTGRES_PASSWORD=pareto2080 \
  -e POSTGRES_DB=learning_db \
  -p 5432:5432 \
  -d postgres:15
```

**Tu salida (Container ID):**
```
_______________________________________________
```

2. **Verificar que el contenedor está corriendo**
```bash
docker ps | grep postgres
```

**Tu salida:**
```
_______________________________________________
```

3. **Conectarse a PostgreSQL**
```bash
docker exec -it postgres-pareto psql -U dataeng -d learning_db
```

4. **Dentro de psql, ejecutar:**
```sql
-- Verificar versión
SELECT version();

-- Crear tabla de prueba
CREATE TABLE test_setup (
  id SERIAL PRIMARY KEY,
  message TEXT,
  created_at TIMESTAMP DEFAULT NOW()
);

-- Insertar datos
INSERT INTO test_setup (message) VALUES ('Setup exitoso!');

-- Consultar
SELECT * FROM test_setup;

-- Salir
\q
```

**Cantidad de filas retornadas:**
```
_______________________________________________
```

### Verificación
- ✅ Contenedor corriendo (`docker ps` muestra postgres-pareto)
- ✅ Conexión exitosa a psql
- ✅ Tabla creada y datos insertados
- ✅ Query SELECT retorna 1 fila

**Duración:** 20 minutos

---

## 📋 Ejercicio 4: Configurar Apache Airflow (Duración: 30 minutos)

### 🎯 Objetivo
Levantar Airflow en modo standalone y acceder a la UI.

### Pasos

1. **Crear estructura de directorios**
```bash
mkdir -p ~/airflow-pareto/{dags,logs,plugins}
cd ~/airflow-pareto
```

2. **Levantar Airflow Standalone**
```bash
docker run -d \
  --name airflow-standalone \
  -p 8080:8080 \
  -v $(pwd)/dags:/opt/airflow/dags \
  -e AIRFLOW__CORE__LOAD_EXAMPLES=False \
  -e AIRFLOW__CORE__EXECUTOR=LocalExecutor \
  apache/airflow:2.7.0-python3.11 standalone
```

**Container ID:**
```
_______________________________________________
```

3. **Esperar inicialización (~2-3 minutos) y obtener credenciales**
```bash
# Ver logs para encontrar password
docker logs airflow-standalone 2>&1 | grep -A 3 "standalone_admin_password"
```

**Password generado:**
```
_______________________________________________
```

4. **Acceder a Airflow UI**
- URL: http://localhost:8080
- User: `admin`
- Password: (obtenido en paso anterior)

5. **Crear DAG de prueba**
```bash
cat > ~/airflow-pareto/dags/test_setup_dag.py << 'EOF'
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'dataeng',
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    'test_setup_dag',
    default_args=default_args,
    description='DAG de verificación de setup',
    schedule_interval=None,
    start_date=datetime(2024, 1, 1),
    catchup=False
) as dag:
    
    task1 = BashOperator(
        task_id='print_date',
        bash_command='date'
    )
    
    task2 = BashOperator(
        task_id='print_message',
        bash_command='echo "Airflow setup exitoso!"'
    )
    
    task1 >> task2
EOF
```

6. **Verificar DAG en UI**
- Refrescar navegador (puede tomar 30-60 segundos)
- Buscar `test_setup_dag` en la lista
- Activar toggle a ON
- Trigger DAG manualmente (botón "Play")

**Estado del DAG después de ejecutar:**
```
_______________________________________________
```

### Verificación
- ✅ Airflow UI accesible en http://localhost:8080
- ✅ Login exitoso
- ✅ DAG `test_setup_dag` visible en lista
- ✅ DAG ejecutado exitosamente (estado verde)

**Duración:** 30 minutos

---

## 📋 Ejercicio 5: Crear Cuenta Databricks Community (Duración: 15 minutos)

### 🎯 Objetivo
Registrarse en Databricks Community Edition y crear primer cluster.

### Pasos

1. **Registro**
- URL: https://community.cloud.databricks.com/login.html
- Click "Sign up for Community Edition"
- Completar formulario con email personal

**Email usado:**
```
_______________________________________________
```

2. **Crear Cluster**
- Sidebar > Compute > Create Cluster
- Cluster Name: `learning-cluster`
- Cluster Mode: Single Node
- Runtime: 13.3 LTS (Scala 2.12, Spark 3.4.1)
- Click "Create Cluster"

**Tiempo de inicio del cluster (minutos):**
```
_______________________________________________
```

3. **Crear Notebook de prueba**
```
- Sidebar > Create > Notebook
- Name: "Setup Verification"
- Language: Scala
- Cluster: learning-cluster
```

4. **Ejecutar código Scala**
```scala
// Cell 1
println(s"Spark version: ${spark.version}")
println(s"Scala version: ${scala.util.Properties.versionString}")

// Cell 2
val testData = Seq(
  ("Setup", "Exitoso", 1),
  ("Databricks", "Funcionando", 2)
)
val df = testData.toDF("modulo", "estado", "id")
df.show()

// Cell 3
df.filter($"id" > 0).count()
```

**Output de Cell 3 (count):**
```
_______________________________________________
```

### Verificación
- ✅ Cuenta Databricks creada
- ✅ Cluster iniciado exitosamente
- ✅ Notebook creado y código ejecutado
- ✅ Output correcto (count = 2)

**Duración:** 15 minutos

---

## 📋 Ejercicio 6: Clonar Repositorio y Crear Rama (Duración: 10 minutos)

### 🎯 Objetivo
Clonar el repo del curso y crear rama personal de trabajo.

### Pasos

1. **Clonar repositorio**
```bash
git clone https://github.com/angra8410/all-my-learnings.git
cd all-my-learnings/Data-Engineering-Pareto-2080
```

2. **Crear rama personal**
```bash
git checkout -b feature/mi-progreso-pareto-$(whoami)
```

**Nombre de tu rama:**
```
_______________________________________________
```

3. **Verificar rama actual**
```bash
git branch --show-current
```

**Salida:**
```
_______________________________________________
```

### Verificación
- ✅ Repositorio clonado
- ✅ Rama personal creada
- ✅ Branch actual es tu rama personal

**Duración:** 10 minutos

---

## 📋 Ejercicio 7: Verificación Final Completa (Duración: 10 minutos)

### 🎯 Objetivo
Crear documento consolidado con evidencia de todas las instalaciones.

### Pasos

1. **Crear archivo de verificación**
```bash
cd ~/all-my-learnings/Data-Engineering-Pareto-2080/00-plan-setup
touch setup-verification.md
```

2. **Ejecutar comandos de verificación**
```bash
cat > setup-verification.md << 'EOF'
# Verificación de Setup Completo

## Git
$(git --version)

## Docker
$(docker --version)

## Python
$(python3 --version)

## Contenedores Corriendo
$(docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}")

## PostgreSQL
$(docker exec -it postgres-pareto psql -U dataeng -d learning_db -c "SELECT 'PostgreSQL OK' as status;")

## Git Branch
$(git branch --show-current)

---
**Fecha de verificación:** $(date)
EOF
```

3. **Revisar archivo generado**
```bash
cat setup-verification.md
```

**¿Todos los servicios están OK? (Sí/No):**
```
_______________________________________________
```

### Verificación
- ✅ Archivo `setup-verification.md` creado
- ✅ Todos los checks retornan valores correctos
- ✅ PostgreSQL responde con "PostgreSQL OK"

**Duración:** 10 minutos

---

## ⏱️ Resumen del Tiempo

| Ejercicio | Duración |
|-----------|----------|
| 1. Verificación instalaciones base | 15 min |
| 2. Configurar Git global | 10 min |
| 3. PostgreSQL en Docker | 20 min |
| 4. Apache Airflow | 30 min |
| 5. Databricks Community | 15 min |
| 6. Clonar repo y crear rama | 10 min |
| 7. Verificación final | 10 min |
| **TOTAL** | **110 min (~2 horas)** |

---

## ✅ Criterios de Éxito

Al completar esta actividad:
- [ ] Git, Docker y Python verificados
- [ ] PostgreSQL corriendo y accesible
- [ ] Airflow UI funcionando en http://localhost:8080
- [ ] DAG de prueba ejecutado exitosamente
- [ ] Cuenta Databricks creada con cluster funcional
- [ ] Notebook Scala ejecutado correctamente
- [ ] Repositorio clonado con rama personal
- [ ] Archivo `setup-verification.md` completado

---

## 🎯 Próximos Pasos

Una vez completada esta actividad interactiva:
1. Marcar progreso en `progreso.md`
2. Autoevaluarte con `retroalimentacion.md`
3. Avanzar a **Módulo 01: Introducción al Pareto 20/80**

---

**💡 Tip:** Guarda screenshots de Airflow UI y Databricks notebook ejecutándose — serán útiles para tu portfolio!
