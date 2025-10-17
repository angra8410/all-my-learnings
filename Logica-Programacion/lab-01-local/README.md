# Lab 01: Laboratorio Local de Lógica y Programación

## 🎯 Objetivos del Laboratorio

Este laboratorio te permite practicar conceptos fundamentales de lógica y programación con un sistema de auto-calificación automatizado:

- Implementar algoritmos básicos en Python
- Practicar funciones: suma, factorial, ordenamiento y búsqueda
- Validar soluciones con tests automáticos
- Obtener retroalimentación instantánea con calificaciones
- Trabajar en un entorno Docker reproducible

## 🏗️ Estructura del Lab

```
lab-01-local/
├── docker-compose.yml          # Configuración de servicios Docker
├── Makefile                    # Comandos automatizados
├── README.md                   # Esta guía
├── revision.md                 # Calificación y resultados (generado)
├── ejercicios/                 # Tus soluciones
│   ├── suma.py
│   ├── factorial.py
│   ├── ordenamiento.py
│   └── busqueda.py
└── tests/                      # Scripts de prueba
    └── check_ejercicios.sh     # Script de calificación
```

## 📋 Prerrequisitos

### Opción 1: Usar DevContainer (Recomendado)

Si usas VS Code con Remote - Containers, todas las herramientas ya están instaladas:

- Visual Studio Code
- Docker Desktop
- Extensión Remote - Containers

### Opción 2: Instalación Local

- **Docker** >= 20.10 y **Docker Compose** >= 2.0
- **Make** (instalado en Linux/Mac por defecto, en Windows usar WSL o Git Bash)

Verificar instalación:
```bash
docker --version
docker compose version
make --version
```

## 🚀 Inicio Rápido

### 1. Navegar al Directorio del Lab

```bash
cd Logica-Programacion/lab-01-local
```

### 2. Ver Comandos Disponibles

```bash
make help
```

### 3. Iniciar el Laboratorio

```bash
# Levantar el servicio Python
make up
```

Este comando:
- Inicia un contenedor Python 3.11
- Monta los directorios de ejercicios y tests
- Instala pytest automáticamente
- Deja el contenedor listo para ejecutar tests

### 4. Ejecutar Tests y Generar Calificación

```bash
make check
```

Este comando:
- Ejecuta todos los tests de los ejercicios
- Calcula el puntaje total (0-100%)
- Genera/actualiza el archivo `revision.md` con:
  - Resultados detallados por ejercicio
  - Errores encontrados
  - Porcentaje de calificación
  - Fecha y hora de la revisión

### 5. Consultar la Calificación

```bash
cat revision.md
```

O abre el archivo `revision.md` en tu editor para ver:
- ✅ Ejercicios completados correctamente
- ⚠️ Ejercicios con errores
- Detalles de cada error encontrado
- Porcentaje total obtenido

### 6. Detener el Laboratorio

```bash
# Detener servicios
make down

# Detener y limpiar todo
make clean
```

## 📝 Ejercicios Incluidos

### 1. suma.py
**Objetivo:** Implementar una función que sume dos números.

```python
def suma(a, b):
    # Tu código aquí
    pass
```

**Tests:**
- suma(2, 3) → 5
- suma(0, 0) → 0
- suma(-1, 1) → 0
- suma(10, -5) → 5

### 2. factorial.py
**Objetivo:** Calcular el factorial de un número.

```python
def factorial(n):
    # Tu código aquí
    pass
```

**Tests:**
- factorial(0) → 1
- factorial(1) → 1
- factorial(5) → 120
- factorial(10) → 3628800

### 3. ordenamiento.py
**Objetivo:** Ordenar una lista de números de menor a mayor.

```python
def ordenamiento(lista):
    # Tu código aquí
    pass
```

**Tests:**
- ordenamiento([3, 1, 4, 1, 5]) → [1, 1, 3, 4, 5]
- ordenamiento([5, 4, 3, 2, 1]) → [1, 2, 3, 4, 5]
- ordenamiento([]) → []

### 4. busqueda.py
**Objetivo:** Buscar un elemento en una lista y retornar su índice.

```python
def busqueda(lista, elemento):
    # Tu código aquí
    pass
```

**Tests:**
- busqueda([1, 2, 3, 4, 5], 3) → 2
- busqueda([1, 2, 3, 4, 5], 6) → -1
- busqueda([], 1) → -1

## 🔄 Flujo de Trabajo

1. **Iniciar el lab:** `make up`
2. **Editar ejercicios:** Modifica los archivos en `ejercicios/`
3. **Ejecutar tests:** `make check`
4. **Ver resultados:** Consulta `revision.md`
5. **Corregir errores:** Vuelve al paso 2
6. **Detener el lab:** `make down`

## 📊 Comandos del Makefile

| Comando | Descripción |
|---------|-------------|
| `make help` | Muestra todos los comandos disponibles |
| `make up` | Inicia el laboratorio |
| `make down` | Detiene el laboratorio |
| `make check` | Ejecuta tests y genera calificación |
| `make logs` | Muestra logs del contenedor |
| `make status` | Muestra estado del servicio |
| `make clean` | Limpia todo (contenedores y volúmenes) |
| `make shell` | Abre un shell interactivo en el contenedor |
| `make info` | Muestra información del laboratorio |

## 🔍 Solución de Problemas

### El contenedor no inicia

```bash
# Ver logs para identificar el problema
make logs

# Reconstruir desde cero
make clean
make up
```

### Los tests no se ejecutan

```bash
# Verificar que el contenedor está corriendo
docker ps | grep logica

# Abrir shell en el contenedor
make shell

# Dentro del contenedor, ejecutar manualmente
python tests/check_ejercicios.sh
```

### Error al importar módulos

Los ejercicios deben estar en la carpeta `ejercicios/` y seguir la estructura:

```python
def nombre_funcion(parametros):
    # código
    return resultado
```

### Permisos en Linux

Si hay problemas de permisos con el archivo `revision.md`:

```bash
# Dar permisos de escritura
chmod 666 revision.md
```

## 🌍 Transferencia a Otros Lenguajes

Los mismos algoritmos pueden implementarse en otros lenguajes:

### JavaScript (Node.js)

```javascript
// suma.js
function suma(a, b) {
    return a + b;
}

// factorial.js
function factorial(n) {
    if (n === 0 || n === 1) return 1;
    let result = 1;
    for (let i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

// ordenamiento.js
function ordenamiento(lista) {
    return lista.slice().sort((a, b) => a - b);
}

// busqueda.js
function busqueda(lista, elemento) {
    return lista.indexOf(elemento);
}
```

### Java

```java
// Suma.java
public class Suma {
    public static int suma(int a, int b) {
        return a + b;
    }
}

// Factorial.java
public class Factorial {
    public static long factorial(int n) {
        if (n == 0 || n == 1) return 1;
        long result = 1;
        for (int i = 2; i <= n; i++) {
            result *= i;
        }
        return result;
    }
}

// Ordenamiento.java
import java.util.Arrays;
public class Ordenamiento {
    public static int[] ordenamiento(int[] lista) {
        int[] resultado = lista.clone();
        Arrays.sort(resultado);
        return resultado;
    }
}

// Busqueda.java
public class Busqueda {
    public static int busqueda(int[] lista, int elemento) {
        for (int i = 0; i < lista.length; i++) {
            if (lista[i] == elemento) return i;
        }
        return -1;
    }
}
```

### C++

```cpp
// suma.cpp
int suma(int a, int b) {
    return a + b;
}

// factorial.cpp
long long factorial(int n) {
    if (n == 0 || n == 1) return 1;
    long long result = 1;
    for (int i = 2; i <= n; i++) {
        result *= i;
    }
    return result;
}

// ordenamiento.cpp
#include <algorithm>
#include <vector>
std::vector<int> ordenamiento(std::vector<int> lista) {
    std::sort(lista.begin(), lista.end());
    return lista;
}

// busqueda.cpp
#include <vector>
int busqueda(std::vector<int> lista, int elemento) {
    auto it = std::find(lista.begin(), lista.end(), elemento);
    if (it != lista.end()) {
        return std::distance(lista.begin(), it);
    }
    return -1;
}
```

## 🎓 Conceptos Aprendidos

Al completar este laboratorio, habrás practicado:

✅ **Funciones básicas:** Crear y usar funciones con parámetros y retornos  
✅ **Operaciones matemáticas:** Suma y factorial  
✅ **Algoritmos de ordenamiento:** Bubble sort y métodos nativos  
✅ **Búsqueda lineal:** Encontrar elementos en estructuras de datos  
✅ **Testing automatizado:** Validar código con tests  
✅ **Docker:** Trabajar en entornos containerizados  
✅ **Automatización:** Usar Makefiles para tareas repetitivas  

## 🚀 Siguientes Pasos

1. **Completa todos los ejercicios** hasta obtener 100% en la calificación
2. **Optimiza las soluciones:** Busca formas más eficientes
3. **Implementa en otros lenguajes:** Practica la transferencia de lógica
4. **Añade más tests:** Prueba casos extremos
5. **Explora algoritmos avanzados:** Binary search, quicksort, etc.

## 🔗 Compatibilidad con VS Code Remote - Containers

Este laboratorio es totalmente compatible con VS Code Dev Containers:

1. Abre la carpeta del lab en VS Code
2. Usa la extensión Remote - Containers
3. El contenedor Python 3.11 está listo para usar
4. Los ejercicios y tests están montados automáticamente

### Configuración para Dev Container (Opcional)

Si quieres crear una configuración específica, crea `.devcontainer/devcontainer.json`:

```json
{
  "name": "Logica Programacion Lab",
  "dockerComposeFile": "../docker-compose.yml",
  "service": "app",
  "workspaceFolder": "/app",
  "customizations": {
    "vscode": {
      "extensions": [
        "ms-python.python",
        "ms-python.vscode-pylance"
      ]
    }
  }
}
```

## 📚 Recursos Adicionales

- **Python Official Docs:** https://docs.python.org/3/
- **Algoritmos y Estructuras de Datos:** https://www.geeksforgeeks.org/
- **Docker Documentation:** https://docs.docker.com/
- **Pytest Documentation:** https://docs.pytest.org/

## ⚠️ Notas Importantes

- El archivo `revision.md` se sobrescribe cada vez que ejecutas `make check`
- Guarda una copia si necesitas mantener resultados históricos
- Los ejercicios incluidos son soluciones mínimas de ejemplo
- Puedes modificarlos y probar diferentes implementaciones
- El sistema de calificación valida resultados, no el código en sí

## 🤝 Contribuciones

Si encuentras errores o tienes sugerencias de mejora para este laboratorio, abre un issue o PR en el repositorio.

---

**¡Disfruta aprendiendo lógica y programación con auto-calificación instantánea!** 🚀💡

