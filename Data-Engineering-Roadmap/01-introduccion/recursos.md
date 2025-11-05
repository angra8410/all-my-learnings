# 📚 Recursos — Módulo 01: Introducción a Data Engineering

## 🎯 Documentación Oficial

### Git
- **Documentación oficial**: https://git-scm.com/doc
- **Pro Git Book (gratis)**: https://git-scm.com/book/es/v2
- **Git Cheat Sheet**: https://training.github.com/downloads/github-git-cheat-sheet.pdf
- **Visualizing Git**: https://git-school.github.io/visualizing-git/

### Docker
- **Get Started with Docker**: https://docs.docker.com/get-started/
- **Docker Hub**: https://hub.docker.com/
- **Docker Compose Documentation**: https://docs.docker.com/compose/
- **Best Practices**: https://docs.docker.com/develop/dev-best-practices/

### PostgreSQL
- **PostgreSQL Official Docs**: https://www.postgresql.org/docs/
- **PostgreSQL Tutorial**: https://www.postgresqltutorial.com/
- **Docker PostgreSQL Image**: https://hub.docker.com/_/postgres

### VSCode
- **VSCode Documentation**: https://code.visualstudio.com/docs
- **Python Extension**: https://marketplace.visualstudio.com/items?itemName=ms-python.python
- **Docker Extension**: https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker
- **GitLens Extension**: https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens

---

## 🎓 Tutoriales y Cursos

### Git y GitHub
- **GitHub Learning Lab**: https://lab.github.com/
- **Learn Git Branching (interactivo)**: https://learngitbranching.js.org/?locale=es_ES
- **Atlassian Git Tutorials**: https://www.atlassian.com/git/tutorials
- **freeCodeCamp Git Course**: https://www.youtube.com/watch?v=RGOj5yH7evk

### Docker
- **Docker for Beginners (freeCodeCamp)**: https://www.youtube.com/watch?v=fqMOX6JJhGo
- **Play with Docker**: https://labs.play-with-docker.com/
- **Docker Curriculum**: https://docker-curriculum.com/
- **Katacoda Docker Scenarios**: https://www.katacoda.com/courses/docker

### Data Engineering Fundamentals
- **DataTalks.Club DE Zoomcamp (gratis)**: https://github.com/DataTalksClub/data-engineering-zoomcamp
- **The Data Engineering Cookbook**: https://github.com/andkret/Cookbook
- **Seattle Data Guy YouTube**: https://www.youtube.com/@SeattleDataGuy
- **Data Engineering Podcast**: https://www.dataengineeringpodcast.com/

---

## 🛠️ Guías de Instalación

### Windows

#### Git
```bash
# Descarga el instalador desde:
https://git-scm.com/download/win

# O instala con Chocolatey:
choco install git
```

#### Docker Desktop
```bash
# Requisitos: Windows 10/11 Pro, Enterprise, o Education con WSL2
# Descarga: https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe

# Después de instalar, habilita WSL2:
wsl --install
wsl --set-default-version 2
```

#### Python
```bash
# Descarga desde: https://www.python.org/downloads/

# O con Chocolatey:
choco install python

# Verifica:
python --version
pip --version
```

### macOS

#### Git
```bash
# Incluido en Xcode Command Line Tools:
xcode-select --install

# O con Homebrew:
brew install git
```

#### Docker Desktop
```bash
# Descarga desde: https://desktop.docker.com/mac/main/amd64/Docker.dmg

# O con Homebrew:
brew install --cask docker
```

#### Python
```bash
# Con Homebrew:
brew install python@3.11

# Verifica:
python3 --version
pip3 --version
```

### Linux (Ubuntu/Debian)

#### Git
```bash
sudo apt update
sudo apt install git

# Verifica:
git --version
```

#### Docker
```bash
# Desinstalar versiones antiguas:
sudo apt remove docker docker-engine docker.io containerd runc

# Instalar dependencias:
sudo apt update
sudo apt install ca-certificates curl gnupg lsb-release

# Agregar clave GPG oficial de Docker:
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Configurar repositorio:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Instalar Docker Engine:
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Agregar usuario al grupo docker (evitar sudo):
sudo usermod -aG docker $USER
newgrp docker

# Verifica:
docker --version
docker run hello-world
```

#### Python
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Verifica:
python3 --version
pip3 --version
```

---

## 🐛 Troubleshooting Común

### Problemas con Docker

#### Error: "Cannot connect to the Docker daemon"
```bash
# Linux:
sudo systemctl start docker
sudo systemctl enable docker

# Windows/Mac: Asegúrate de que Docker Desktop esté corriendo
```

#### Error: "port is already allocated"
```bash
# Ver qué proceso usa el puerto:
# Linux/Mac:
lsof -i :5432
# Windows:
netstat -ano | findstr :5432

# Cambiar el puerto en docker run:
docker run -p 5433:5432 ...  # Usa 5433 en lugar de 5432
```

#### Contenedor se detiene inmediatamente
```bash
# Ver logs para diagnóstico:
docker logs <container_name>

# Verificar que las variables de entorno son correctas
docker inspect <container_name>
```

### Problemas con PostgreSQL

#### Error: "password authentication failed"
```bash
# Verifica la contraseña en el comando docker run
# Reinicia el contenedor con las credenciales correctas:
docker rm postgres-local
docker run --name postgres-local \
  -e POSTGRES_PASSWORD=tu_password_correcto \
  ...
```

#### No se puede conectar desde host
```bash
# Verifica que el puerto está mapeado correctamente:
docker ps
# Debe mostrar: 0.0.0.0:5432->5432/tcp

# Verifica que PostgreSQL está escuchando:
docker exec postgres-local pg_isready -U dataeng
```

### Problemas con Git

#### Error: "fatal: not a git repository"
```bash
# Asegúrate de estar en el directorio correcto:
cd /path/to/all-my-learnings
git status
```

#### Error de permisos en push
```bash
# Configura credenciales:
git config --global credential.helper cache

# O usa SSH en lugar de HTTPS:
git remote set-url origin git@github.com:angra8410/all-my-learnings.git
```

---

## 📖 Libros Recomendados

### Para Principiantes
1. **"Designing Data-Intensive Applications"** - Martin Kleppmann
   - El libro fundamental para Data Engineers
   - Cubre arquitecturas, bases de datos, procesamiento distribuido

2. **"The Data Warehouse Toolkit"** - Ralph Kimball
   - Modelado dimensional explicado magistralmente
   - Casos de estudio reales

3. **"Fundamentals of Data Engineering"** - Joe Reis & Matt Housley
   - Libro moderno (2022) sobre prácticas actuales
   - Cubre todo el ciclo de vida de datos

### Para Profundizar
4. **"Database Internals"** - Alex Petrov
   - Cómo funcionan las bases de datos internamente

5. **"97 Things Every Data Engineer Should Know"** - Tobias Macey
   - Consejos prácticos de expertos de la industria

---

## 🎥 Videos y Canales de YouTube

### Canales Recomendados
- **Seattle Data Guy**: https://www.youtube.com/@SeattleDataGuy
  - Consejos de carrera, arquitecturas, entrevistas

- **DataTalks.Club**: https://www.youtube.com/@DataTalksClub
  - Cursos completos gratuitos, eventos semanales

- **Fireship**: https://www.youtube.com/@Fireship
  - Tutoriales rápidos de tecnologías (Docker, Git, etc.)

- **TechWorld with Nana**: https://www.youtube.com/@TechWorldwithNana
  - DevOps, Docker, Kubernetes

### Videos Específicos para este Módulo
- **Git and GitHub for Beginners**: https://www.youtube.com/watch?v=RGOj5yH7evk
- **Docker Tutorial for Beginners**: https://www.youtube.com/watch?v=fqMOX6JJhGo
- **What is Data Engineering?**: https://www.youtube.com/watch?v=qWru-b6m030

---

## 🌐 Comunidades y Foros

### Slack Communities
- **dbt Community**: https://www.getdbt.com/community/
- **Data Engineering Slack**: https://www.dataengineering.wiki/Community
- **Locally Optimistic**: https://locallyoptimistic.com/community/

### Reddit
- r/dataengineering: https://www.reddit.com/r/dataengineering/
- r/learnprogramming: https://www.reddit.com/r/learnprogramming/

### Otros
- **Stack Overflow**: https://stackoverflow.com/questions/tagged/data-engineering
- **Data Engineering Weekly Newsletter**: https://www.dataengineeringweekly.com/

---

## 💻 Comandos Útiles de Referencia

### Git Básico
```bash
# Inicializar repo
git init

# Clonar repo
git clone <url>

# Ver estado
git status

# Agregar archivos
git add .
git add <archivo>

# Commit
git commit -m "mensaje"

# Push
git push origin <rama>

# Pull
git pull origin <rama>

# Ver historial
git log --oneline --graph

# Crear rama
git checkout -b <nombre-rama>

# Cambiar de rama
git checkout <rama>

# Ver diferencias
git diff
```

### Docker Básico
```bash
# Ver imágenes
docker images

# Descargar imagen
docker pull <imagen>:<tag>

# Ejecutar contenedor
docker run [opciones] <imagen>

# Listar contenedores corriendo
docker ps

# Listar todos los contenedores
docker ps -a

# Detener contenedor
docker stop <nombre_o_id>

# Iniciar contenedor
docker start <nombre_o_id>

# Eliminar contenedor
docker rm <nombre_o_id>

# Ver logs
docker logs <nombre_o_id>
docker logs -f <nombre_o_id>  # Seguir logs en tiempo real

# Ejecutar comando en contenedor
docker exec -it <nombre> <comando>

# Inspeccionar contenedor
docker inspect <nombre>

# Ver uso de recursos
docker stats
```

### PostgreSQL Básico
```sql
-- Listar bases de datos
\l

-- Conectar a base de datos
\c <nombre_db>

-- Listar tablas
\dt

-- Describir tabla
\d <nombre_tabla>

-- Salir de psql
\q

-- Ejecutar query desde terminal
psql -U usuario -d database -c "SELECT * FROM tabla;"
```

---

## 🎯 Datasets de Práctica (para módulos futuros)

- **Kaggle Datasets**: https://www.kaggle.com/datasets
- **Google Dataset Search**: https://datasetsearch.research.google.com/
- **AWS Open Data**: https://registry.opendata.aws/
- **Data.gov**: https://data.gov/
- **NYC Open Data**: https://opendata.cityofnewyork.us/

---

## 🔗 Herramientas Online Útiles

### Editores Online
- **SQLFiddle**: http://sqlfiddle.com/ - Probar SQL sin instalar nada
- **DB Fiddle**: https://www.db-fiddle.com/ - Similar a SQLFiddle
- **Replit**: https://replit.com/ - IDE online para Python

### Diagramas y Visualización
- **dbdiagram.io**: https://dbdiagram.io/ - Diseñar esquemas de DB
- **Excalidraw**: https://excalidraw.com/ - Diagramas técnicos
- **Draw.io**: https://app.diagrams.net/ - Diagramas de arquitectura

### Validadores
- **YAML Validator**: https://www.yamllint.com/
- **JSON Validator**: https://jsonlint.com/
- **SQL Formatter**: https://sqlformat.org/

---

## 📝 Plantillas Útiles

### .gitignore para proyectos de datos
```gitignore
# Python
__pycache__/
*.py[cod]
*$py.class
.Python
venv/
env/

# Jupyter
.ipynb_checkpoints

# Data files
*.csv
*.parquet
*.db
*.sqlite

# Credentials
.env
credentials.json
*.pem

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
```

### docker-compose.yml template
```yaml
version: '3.8'

services:
  postgres:
    image: postgres:13
    container_name: postgres-dev
    environment:
      POSTGRES_USER: ${DB_USER:-dataeng}
      POSTGRES_PASSWORD: ${DB_PASSWORD:-password}
      POSTGRES_DB: ${DB_NAME:-learning_db}
    ports:
      - "${DB_PORT:-5432}:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql

volumes:
  postgres_data:
```

---

## 🎓 Certificaciones Relevantes

Aunque no las necesitas ahora, estas son valiosas para el futuro:

- **AWS Certified Data Analytics - Specialty**
- **Google Cloud Professional Data Engineer**
- **Microsoft Certified: Azure Data Engineer Associate**
- **Snowflake SnowPro Core Certification**
- **dbt Analytics Engineering Certification**

---

## 📞 Obtener Ayuda

### Cuando estés bloqueado:

1. **Lee el mensaje de error completo** - Muchas veces contiene la solución
2. **Busca en Google** con el mensaje exacto entre comillas
3. **Consulta Stack Overflow** - Alguien probablemente tuvo el mismo problema
4. **Revisa documentación oficial** - Es tu mejor amigo
5. **Pregunta en comunidades** - Slack, Reddit, pero con contexto detallado
6. **Usa ChatGPT/Claude** - Excelente para explicar errores y conceptos

### Cómo hacer una buena pregunta:

1. Describe qué intentas lograr
2. Muestra qué has intentado
3. Comparte el error completo
4. Indica tu sistema operativo y versiones
5. Simplifica al mínimo caso reproducible

---

**Última actualización:** Noviembre 2024  
**Mantenedor:** angra8410  

💡 **Tip**: Guarda este archivo como referencia. Lo consultarás frecuentemente durante el curso.