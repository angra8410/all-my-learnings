# Módulo 02: Prerrequisitos y Entorno

## 🎯 Objetivos del Módulo

Al finalizar este módulo, habrás:

- ✅ Instalado y configurado Python 3.9+
- ✅ Instalado y configurado Docker Desktop
- ✅ Configurado tu entorno de desarrollo (VS Code o similar)
- ✅ Instalado herramientas CLI esenciales
- ✅ Creado tu primer entorno virtual Python
- ✅ Verificado que todo funciona correctamente

## 📋 Prerrequisitos

### Sistema Operativo

El curso funciona en:
- ✅ Windows 10/11 (con WSL2 para Docker)
- ✅ macOS (Intel o Apple Silicon)
- ✅ Linux (Ubuntu, Debian, Fedora, etc.)

### Hardware Mínimo

- **RAM**: 8 GB (16 GB recomendado)
- **Almacenamiento**: 10 GB libres
- **Procesador**: Dual-core moderno

## 🔧 Instalaciones Necesarias

### 1. Python 3.9 o Superior

#### Verificar si ya está instalado

```bash
python --version
# o
python3 --version
```

Si ves algo como `Python 3.9.x`, `Python 3.10.x`, `Python 3.11.x`, o `Python 3.12.x`, ¡estás listo!

#### Instalación por Sistema Operativo

**Windows:**
```bash
# Opción 1: Desde python.org
# Descargar desde: https://www.python.org/downloads/
# Marcar: "Add Python to PATH" durante instalación

# Opción 2: Con winget
winget install Python.Python.3.12

# Verificar
python --version
```

**macOS:**
```bash
# Opción 1: Con Homebrew (recomendado)
brew install python@3.12

# Opción 2: Desde python.org
# Descargar desde: https://www.python.org/downloads/

# Verificar
python3 --version
```

**Linux (Ubuntu/Debian):**
```bash
# Actualizar repositorios
sudo apt update

# Instalar Python
sudo apt install python3 python3-pip python3-venv

# Verificar
python3 --version
pip3 --version
```

### 2. Docker Desktop

#### Instalación por Sistema Operativo

**Windows:**
```bash
# Prerrequisitos: WSL2
# 1. Habilitar WSL2
wsl --install

# 2. Descargar Docker Desktop
# https://www.docker.com/products/docker-desktop/

# 3. Ejecutar instalador y reiniciar

# 4. Verificar
docker --version
docker ps
```

**macOS:**
```bash
# Opción 1: Descargar desde
# https://www.docker.com/products/docker-desktop/

# Opción 2: Con Homebrew
brew install --cask docker

# Iniciar Docker Desktop desde Applications

# Verificar
docker --version
docker ps
```

**Linux (Ubuntu/Debian):**
```bash
# 1. Instalar dependencias
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg lsb-release

# 2. Añadir repositorio de Docker
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# 3. Instalar Docker Engine
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# 4. Añadir usuario al grupo docker
sudo usermod -aG docker $USER
newgrp docker

# 5. Verificar
docker --version
docker run hello-world
```

### 3. Editor de Código: VS Code

#### Instalación

**Windows:**
```bash
# Opción 1: Descargar desde
# https://code.visualstudio.com/

# Opción 2: Con winget
winget install Microsoft.VisualStudioCode
```

**macOS:**
```bash
# Opción 1: Descargar desde
# https://code.visualstudio.com/

# Opción 2: Con Homebrew
brew install --cask visual-studio-code
```

**Linux:**
```bash
# Ubuntu/Debian
sudo snap install code --classic

# O con apt
wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
sudo install -o root -g root -m 644 packages.microsoft.gpg /etc/apt/trusted.gpg.d/
echo "deb [arch=amd64] https://packages.microsoft.com/repos/code stable main" | sudo tee /etc/apt/sources.list.d/vscode.list
sudo apt update
sudo apt install code
```

#### Extensiones Recomendadas

Instala desde VS Code (Ctrl+Shift+X / Cmd+Shift+X):

1. **Python** (Microsoft)
2. **Docker** (Microsoft)
3. **Pylance** (Microsoft)
4. **Python Debugger** (Microsoft)
5. **GitLens** (opcional pero útil)

```bash
# Instalar desde línea de comandos
code --install-extension ms-python.python
code --install-extension ms-azuretools.vscode-docker
code --install-extension ms-python.vscode-pylance
```

### 4. Git (Control de Versiones)

**Windows:**
```bash
# Con winget
winget install Git.Git

# O descargar desde
# https://git-scm.com/download/win
```

**macOS:**
```bash
# Viene preinstalado, pero para actualizar:
brew install git
```

**Linux:**
```bash
sudo apt install git
```

**Verificar:**
```bash
git --version
```

**Configuración inicial:**
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

## 🛠️ Configuración del Entorno

### 1. Crear Estructura de Carpetas

```bash
# Crear carpeta principal del curso
mkdir -p ~/fromzero-agentic-docker
cd ~/fromzero-agentic-docker

# Crear estructura
mkdir -p {modulos,proyectos,tests,logs}

# Ver estructura
tree .
# o si no tienes tree:
ls -la
```

### 2. Primer Entorno Virtual Python

```bash
# Crear entorno virtual
python -m venv venv
# En algunos sistemas:
python3 -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate

# Verificar que está activo (deberías ver (venv) en tu prompt)
which python
# En Windows: where python

# Actualizar pip
pip install --upgrade pip

# Instalar dependencias básicas
pip install fastapi uvicorn pydantic pytest
```

### 3. Verificar Instalaciones

Crea un archivo `verify_setup.py`:

```python
#!/usr/bin/env python3
"""Script para verificar que todo está instalado correctamente."""

import sys
import subprocess

def check_python():
    """Check Python version."""
    version = sys.version_info
    if version.major == 3 and version.minor >= 9:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - OK")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} - Necesitas Python 3.9+")
        return False

def check_pip():
    """Check pip installation."""
    try:
        result = subprocess.run(['pip', '--version'], capture_output=True, text=True)
        print(f"✅ pip installed - {result.stdout.strip()}")
        return True
    except Exception as e:
        print(f"❌ pip not found - {e}")
        return False

def check_docker():
    """Check Docker installation."""
    try:
        result = subprocess.run(['docker', '--version'], capture_output=True, text=True)
        print(f"✅ Docker installed - {result.stdout.strip()}")
        
        result = subprocess.run(['docker', 'ps'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Docker daemon is running")
            return True
        else:
            print("⚠️  Docker installed but daemon not running")
            return False
    except Exception as e:
        print(f"❌ Docker not found - {e}")
        return False

def check_git():
    """Check Git installation."""
    try:
        result = subprocess.run(['git', '--version'], capture_output=True, text=True)
        print(f"✅ Git installed - {result.stdout.strip()}")
        return True
    except Exception as e:
        print(f"❌ Git not found - {e}")
        return False

def main():
    """Run all checks."""
    print("🔍 Verificando instalaciones...\n")
    
    checks = [
        ("Python", check_python),
        ("pip", check_pip),
        ("Docker", check_docker),
        ("Git", check_git),
    ]
    
    results = []
    for name, check_func in checks:
        results.append(check_func())
        print()
    
    print("=" * 50)
    if all(results):
        print("🎉 ¡Todo está instalado correctamente!")
        print("✅ Estás listo para comenzar el curso")
    else:
        print("⚠️  Algunas herramientas faltan o tienen problemas")
        print("📝 Revisa los mensajes arriba y completa las instalaciones")
    print("=" * 50)

if __name__ == "__main__":
    main()
```

Ejecutar:

```bash
python verify_setup.py
```

## 🧪 Pruebas de Configuración

### Test 1: Python funcional

```bash
# Crear archivo test
echo 'print("Hello, Agentic World!")' > test_python.py

# Ejecutar
python test_python.py

# Resultado esperado:
# Hello, Agentic World!
```

### Test 2: Docker funcional

```bash
# Ejecutar contenedor de prueba
docker run hello-world

# Resultado esperado:
# Hello from Docker!
# (mensaje de confirmación)
```

### Test 3: FastAPI funcional

Crear `test_fastapi.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "FastAPI is working!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
```

Ejecutar:

```bash
# Instalar uvicorn si no está
pip install uvicorn

# Ejecutar servidor
uvicorn test_fastapi:app --reload

# En otra terminal, probar:
curl http://localhost:8000
curl http://localhost:8000/health
```

## 📚 Comandos Esenciales a Memorizar

### Python

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Desactivar entorno
deactivate

# Instalar paquetes
pip install <paquete>

# Ver paquetes instalados
pip list

# Guardar dependencias
pip freeze > requirements.txt

# Instalar desde requirements.txt
pip install -r requirements.txt
```

### Docker

```bash
# Ver versión
docker --version

# Ver imágenes
docker images

# Ver contenedores activos
docker ps

# Ver todos los contenedores
docker ps -a

# Construir imagen
docker build -t nombre:tag .

# Ejecutar contenedor
docker run -p 8000:8000 nombre:tag

# Ver logs
docker logs <container-id>

# Detener contenedor
docker stop <container-id>

# Eliminar contenedor
docker rm <container-id>

# Eliminar imagen
docker rmi <image-id>
```

### Git

```bash
# Estado del repositorio
git status

# Añadir archivos
git add .

# Commit
git commit -m "mensaje"

# Ver log
git log --oneline

# Ver diferencias
git diff
```

## 🎯 Checklist de Verificación Final

Antes de continuar al Módulo 03:

- [ ] Python 3.9+ instalado y funcional
- [ ] pip funcional
- [ ] Docker Desktop instalado
- [ ] Docker daemon corriendo
- [ ] VS Code instalado con extensiones
- [ ] Git instalado y configurado
- [ ] Entorno virtual creado y activado
- [ ] FastAPI y uvicorn instalados
- [ ] Todos los tests pasaron
- [ ] Estructura de carpetas creada
- [ ] Script de verificación ejecutado exitosamente

## 💡 Solución de Problemas Comunes

### Python

**Problema**: `python: command not found`
**Solución**: Usa `python3` en su lugar, o añade Python al PATH

**Problema**: `pip: command not found`
**Solución**: Usa `python -m pip` en su lugar

### Docker

**Problema**: `Cannot connect to the Docker daemon`
**Solución**: Asegúrate de que Docker Desktop está corriendo

**Problema**: `permission denied` en Linux
**Solución**: Añade tu usuario al grupo docker: `sudo usermod -aG docker $USER`

### VS Code

**Problema**: No detecta Python
**Solución**: Ctrl+Shift+P → "Python: Select Interpreter" → Selecciona tu venv

## 📝 Próximos Pasos

1. Completa todos los ejercicios en `actividad-interactiva.md`
2. Documenta tus instalaciones en `retroalimentacion.md`
3. Marca tu progreso en `progreso.md`
4. Continúa al **Módulo 03: Docker Básico**

---

**¡Entorno configurado! Ahora sí, a programar. 🚀**
