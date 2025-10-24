# Módulo 02: Actividad Interactiva

## 🎯 Objetivo

Instalar, configurar y verificar todas las herramientas necesarias para el curso.

---

## 🐍 Ejercicio 1: Instala Python (15 minutos)

**Objetivo**: Tener Python 3.9+ funcionando en tu sistema.

### Pasos:

1. **Verifica si ya tienes Python**:

```bash
python --version
python3 --version
```

2. **Si necesitas instalarlo**, sigue las instrucciones del README.md para tu sistema operativo.

3. **Verifica la instalación**:

```bash
python3 --version
pip3 --version
```

**Mi versión de Python**: _______________
**Mi versión de pip**: _______________

4. **Prueba rápida**:

```bash
python3 -c "print('Python works!')"
```

**Resultado**: _______________

**Duración**: 15 minutos

---

## 🐳 Ejercicio 2: Instala Docker (20 minutos)

**Objetivo**: Tener Docker Desktop instalado y corriendo.

### Pasos:

1. **Descarga e instala Docker Desktop** para tu sistema operativo (ver README.md).

2. **Inicia Docker Desktop**.

3. **Verifica la instalación**:

```bash
docker --version
docker ps
```

**Mi versión de Docker**: _______________

4. **Ejecuta tu primer contenedor**:

```bash
docker run hello-world
```

**¿Funcionó?**:
- [ ] Sí - Vi el mensaje "Hello from Docker!"
- [ ] No - Error: _______________

**Duración**: 20 minutos

---

## 💻 Ejercicio 3: Instala VS Code (10 minutos)

**Objetivo**: Tener un editor de código configurado.

### Pasos:

1. **Instala VS Code** (ver README.md).

2. **Abre VS Code** y familiarízate con la interfaz.

3. **Instala extensiones** necesarias:

```bash
code --install-extension ms-python.python
code --install-extension ms-azuretools.vscode-docker
```

**Extensiones instaladas**:
- [ ] Python
- [ ] Docker
- [ ] Pylance

**Duración**: 10 minutos

---

## 🔧 Ejercicio 4: Crea tu Entorno Virtual (8 minutos)

**Objetivo**: Crear y activar un entorno virtual Python.

### Pasos:

```bash
# 1. Crear carpeta del curso
mkdir -p ~/fromzero-agentic-docker
cd ~/fromzero-agentic-docker

# 2. Crear entorno virtual
python3 -m venv venv

# 3. Activar entorno virtual
# macOS/Linux:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 4. Verificar
which python  # macOS/Linux
where python  # Windows

# 5. Actualizar pip
pip install --upgrade pip
```

**¿Ves (venv) en tu prompt?**:
- [ ] Sí
- [ ] No

**Ruta de Python en venv**: _______________

**Duración**: 8 minutos

---

## 📦 Ejercicio 5: Instala Dependencias Básicas (5 minutos)

**Objetivo**: Instalar las librerías principales del curso.

### Pasos:

```bash
# Con el venv activado:
pip install fastapi uvicorn pydantic pytest

# Verificar instalaciones
pip list
```

**Paquetes instalados**:
- [ ] fastapi
- [ ] uvicorn
- [ ] pydantic
- [ ] pytest

**Número total de paquetes**: _______________

**Duración**: 5 minutos

---

## ✅ Ejercicio 6: Script de Verificación (10 minutos)

**Objetivo**: Ejecutar un script que verifique todas las instalaciones.

### Pasos:

1. **Crea el archivo** `verify_setup.py` (código en README.md).

2. **Ejecuta el script**:

```bash
python verify_setup.py
```

3. **Registra los resultados**:

**Python**: [ ] ✅ - [ ] ❌
**pip**: [ ] ✅ - [ ] ❌
**Docker**: [ ] ✅ - [ ] ❌
**Git**: [ ] ✅ - [ ] ❌

**Si hay errores**, ¿cuáles?:
_______________________________________________

**Duración**: 10 minutos

---

## 🧪 Ejercicio 7: Prueba FastAPI (12 minutos)

**Objetivo**: Ejecutar tu primera aplicación FastAPI.

### Pasos:

1. **Crea** `test_fastapi.py` (código en README.md).

2. **Ejecuta el servidor**:

```bash
uvicorn test_fastapi:app --reload
```

3. **En otra terminal, prueba la API**:

```bash
# Test endpoint raíz
curl http://localhost:8000

# Test endpoint health
curl http://localhost:8000/health

# Test documentación
# Abre en navegador: http://localhost:8000/docs
```

**Resultados**:

**Endpoint /**:
```json
_______________________________________________
```

**Endpoint /health**:
```json
_______________________________________________
```

**¿Pudiste ver /docs?**: [ ] Sí - [ ] No

**Duración**: 12 minutos

---

## 🐋 Ejercicio 8: Primer Contenedor Docker (15 minutos)

**Objetivo**: Ejecutar comandos Docker básicos.

### Pasos:

```bash
# 1. Ver imágenes actuales
docker images

# 2. Ejecutar contenedor de prueba
docker run hello-world

# 3. Ver contenedores
docker ps -a

# 4. Ejecutar contenedor interactivo
docker run -it python:3.11-slim python --version

# 5. Limpiar
docker container prune -f
```

**Minuto fluido x5 - Repite estos comandos**:

| Repetición | Comando ejecutado | Resultado |
|------------|-------------------|-----------|
| 1 | docker images | _____________ |
| 2 | docker ps | _____________ |
| 3 | docker ps -a | _____________ |
| 4 | docker run hello-world | _____________ |
| 5 | docker images | _____________ |

**Duración**: 15 minutos

---

## 📁 Ejercicio 9: Estructura de Carpetas (5 minutos)

**Objetivo**: Organizar tu espacio de trabajo.

### Pasos:

```bash
cd ~/fromzero-agentic-docker

# Crear estructura
mkdir -p modulos proyectos tests logs

# Crear .gitignore
cat > .gitignore << 'GITIGNORE'
venv/
__pycache__/
*.pyc
.env
.DS_Store
*.log
GITIGNORE

# Ver estructura
tree -L 2
# o: ls -la
```

**Mi estructura**:
```
_______________________________________________
_______________________________________________
_______________________________________________
```

**Duración**: 5 minutos

---

## 🔐 Ejercicio 10: Configurar Git (5 minutos)

**Objetivo**: Preparar Git para commits futuros.

### Pasos:

```bash
# Configurar identidad
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"

# Verificar configuración
git config --list

# Inicializar repositorio local
cd ~/fromzero-agentic-docker
git init
git add .
git commit -m "Initial setup"
```

**Git configurado**:
- [ ] user.name
- [ ] user.email
- [ ] Repositorio inicializado

**Duración**: 5 minutos

---

## 📊 Resumen del Tiempo

| Ejercicio | Duración | Completado |
|-----------|----------|------------|
| 1. Instala Python | 15 min | [ ] |
| 2. Instala Docker | 20 min | [ ] |
| 3. Instala VS Code | 10 min | [ ] |
| 4. Entorno virtual | 8 min | [ ] |
| 5. Dependencias | 5 min | [ ] |
| 6. Verificación | 10 min | [ ] |
| 7. Prueba FastAPI | 12 min | [ ] |
| 8. Primer contenedor | 15 min | [ ] |
| 9. Estructura carpetas | 5 min | [ ] |
| 10. Configurar Git | 5 min | [ ] |
| **TOTAL** | **105 min** | |

---

## 🎯 Próximos Pasos

1. Completa todos los ejercicios
2. Registra resultados en `retroalimentacion.md`
3. Actualiza `progreso.md`
4. Continúa al **Módulo 03: Docker Básico**

---

**¡Tu entorno está listo para el curso! 🚀**
