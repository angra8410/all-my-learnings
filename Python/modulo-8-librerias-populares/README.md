# Módulo 8: Librerías Populares de Python

## Introducción

¡Bienvenido al Módulo 8! Una de las mayores fortalezas de Python es su ecosistema de librerías. En lugar de reinventar la rueda, puedes usar herramientas creadas por la comunidad para acelerar tu desarrollo.

En este módulo aprenderás sobre:
- Requests (peticiones HTTP)
- BeautifulSoup (web scraping)
- Pandas (análisis de datos)
- NumPy (computación numérica)
- Matplotlib (visualización)
- Pillow (procesamiento de imágenes)

## ¿Por qué es importante?

Las librerías te permiten:
- Ahorrar tiempo (no programar desde cero)
- Usar código probado y optimizado
- Acceder a funcionalidades avanzadas fácilmente
- Ser más productivo

**Analogía:** Es como tener una caja de herramientas profesional en lugar de fabricar cada herramienta tú mismo.

## Conceptos Principales

### 1. Instalación de Librerías con pip

```bash
# Instalar una librería
pip install requests

# Instalar versión específica
pip install pandas==2.0.0

# Instalar desde requirements.txt
pip install -r requirements.txt

# Listar librerías instaladas
pip list

# Actualizar librería
pip install --upgrade requests
```

### 2. Requests - Peticiones HTTP

Ideal para consumir APIs y descargar contenido web:

```python
import requests

# GET request
response = requests.get("https://api.github.com/users/python")
print(response.status_code)  # 200
print(response.json())  # Parsea JSON automáticamente

# POST request
data = {"nombre": "Ana", "edad": 25}
response = requests.post("https://api.ejemplo.com/usuarios", json=data)

# Con parámetros
params = {"q": "python", "sort": "stars"}
response = requests.get("https://api.github.com/search/repositories", params=params)

# Con headers
headers = {"Authorization": "Bearer TOKEN"}
response = requests.get("https://api.ejemplo.com/data", headers=headers)

# Manejo de errores
try:
    response = requests.get("https://api.ejemplo.com/data", timeout=5)
    response.raise_for_status()  # Lanza excepción si error 4xx/5xx
    datos = response.json()
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

**Ejemplo práctico: Cliente de API del clima**
```python
import requests

def obtener_clima(ciudad):
    api_key = "TU_API_KEY"
    url = f"https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": ciudad,
        "appid": api_key,
        "units": "metric",
        "lang": "es"
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        datos = response.json()
        temp = datos["main"]["temp"]
        descripcion = datos["weather"][0]["description"]
        return f"{ciudad}: {temp}°C, {descripcion}"
    return "Ciudad no encontrada"

print(obtener_clima("Madrid"))
```

### 3. BeautifulSoup - Web Scraping

Para extraer datos de páginas HTML:

```python
from bs4 import BeautifulSoup
import requests

# Descargar página
url = "https://ejemplo.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Encontrar elementos
titulo = soup.find("h1")  # Primer h1
print(titulo.text)

# Encontrar todos
enlaces = soup.find_all("a")  # Todos los enlaces
for enlace in enlaces:
    print(enlace.get("href"))

# Buscar por clase CSS
articulos = soup.find_all("div", class_="articulo")

# Buscar por ID
cabecera = soup.find(id="header")

# CSS selectors
items = soup.select(".item > h2")
```

**Ejemplo práctico: Scraper de noticias**
```python
from bs4 import BeautifulSoup
import requests

def scrape_titulares(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    titulares = soup.find_all("h2", class_="titulo-noticia")
    
    for i, titular in enumerate(titulares[:5], 1):
        print(f"{i}. {titular.text.strip()}")

scrape_titulares("https://ejemplo-noticias.com")
```

### 4. Pandas - Análisis de Datos

Para trabajar con datos tabulares:

```python
import pandas as pd

# Crear DataFrame
datos = {
    "nombre": ["Ana", "Carlos", "Elena"],
    "edad": [25, 30, 28],
    "ciudad": ["Madrid", "Barcelona", "Valencia"]
}
df = pd.DataFrame(datos)

# Leer CSV
df = pd.read_csv("datos.csv")

# Ver primeras filas
print(df.head())

# Información del DataFrame
print(df.info())
print(df.describe())

# Acceder a columnas
print(df["nombre"])
print(df[["nombre", "edad"]])

# Filtrar
mayores_25 = df[df["edad"] > 25]
madrid = df[df["ciudad"] == "Madrid"]

# Agregar columna
df["adulto"] = df["edad"] >= 18

# Ordenar
df_ordenado = df.sort_values("edad", ascending=False)

# Agrupar
por_ciudad = df.groupby("ciudad")["edad"].mean()

# Guardar
df.to_csv("salida.csv", index=False)
```

**Ejemplo práctico: Análisis de ventas**
```python
import pandas as pd

# Cargar datos
ventas = pd.read_csv("ventas.csv")

# Estadísticas
print("Ventas totales:", ventas["monto"].sum())
print("Venta promedio:", ventas["monto"].mean())
print("Producto más vendido:", ventas["producto"].mode()[0])

# Agrupar por producto
por_producto = ventas.groupby("producto")["monto"].agg(["sum", "mean", "count"])
print(por_producto)
```

### 5. NumPy - Computación Numérica

Para operaciones matemáticas eficientes:

```python
import numpy as np

# Crear arrays
arr = np.array([1, 2, 3, 4, 5])
matriz = np.array([[1, 2], [3, 4]])

# Arrays especiales
ceros = np.zeros(5)  # [0. 0. 0. 0. 0.]
unos = np.ones((3, 3))
rango = np.arange(0, 10, 2)  # [0, 2, 4, 6, 8]
aleatorios = np.random.rand(5)

# Operaciones
print(arr * 2)  # [2, 4, 6, 8, 10]
print(arr + 10)  # [11, 12, 13, 14, 15]
print(np.sqrt(arr))  # Raíz cuadrada
print(arr.mean())  # Promedio
print(arr.sum())  # Suma

# Operaciones matriciales
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A @ B)  # Multiplicación matricial
print(A.T)  # Transpuesta
```

### 6. Matplotlib - Visualización

Para crear gráficos:

```python
import matplotlib.pyplot as plt

# Gráfico de líneas
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Gráfico de Líneas")
plt.show()

# Gráfico de barras
categorias = ["A", "B", "C", "D"]
valores = [23, 45, 56, 78]

plt.bar(categorias, valores)
plt.title("Gráfico de Barras")
plt.show()

# Histograma
datos = np.random.randn(1000)
plt.hist(datos, bins=30)
plt.title("Histograma")
plt.show()

# Gráfico de dispersión
x = np.random.rand(50)
y = np.random.rand(50)
plt.scatter(x, y)
plt.title("Dispersión")
plt.show()
```

### 7. Pillow - Procesamiento de Imágenes

```python
from PIL import Image, ImageFilter

# Abrir imagen
img = Image.open("foto.jpg")

# Información
print(img.size)  # (ancho, alto)
print(img.format)  # JPG, PNG, etc.

# Redimensionar
img_pequeña = img.resize((200, 200))

# Rotar
img_rotada = img.rotate(45)

# Aplicar filtros
img_blur = img.filter(ImageFilter.BLUR)
img_contorno = img.filter(ImageFilter.CONTOUR)

# Convertir a escala de grises
img_gris = img.convert("L")

# Guardar
img_gris.save("foto_gris.jpg")

# Crear thumbnail
img.thumbnail((150, 150))
img.save("thumbnail.jpg")
```

## Implementación Práctica

### Proyecto: Bot de Clima con Telegram

```python
import requests

def obtener_clima_ciudad(ciudad, api_key):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": ciudad, "appid": api_key, "units": "metric", "lang": "es"}
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        datos = response.json()
        return {
            "temperatura": datos["main"]["temp"],
            "descripcion": datos["weather"][0]["description"],
            "humedad": datos["main"]["humidity"]
        }
    return None

# Usar
clima = obtener_clima_ciudad("Madrid", "TU_API_KEY")
if clima:
    print(f"Temperatura: {clima['temperatura']}°C")
    print(f"Descripción: {clima['descripcion']}")
```

### Proyecto: Análisis de Dataset

```python
import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv("ventas_anuales.csv")

# Análisis
ventas_por_mes = df.groupby("mes")["ventas"].sum()

# Visualización
plt.figure(figsize=(10, 6))
ventas_por_mes.plot(kind="bar")
plt.title("Ventas por Mes")
plt.xlabel("Mes")
plt.ylabel("Ventas ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("ventas_por_mes.png")
plt.show()
```

## Mejores Prácticas

1. **Usa virtual environments**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

2. **Crea requirements.txt**
   ```bash
   pip freeze > requirements.txt
   ```

3. **Maneja errores al importar**
   ```python
   try:
       import pandas as pd
   except ImportError:
       print("Instala pandas: pip install pandas")
   ```

4. **Lee la documentación oficial**
   - Cada librería tiene docs excelentes
   - Busca ejemplos en la documentación

## Conceptos clave para recordar

- 🔑 **pip**: Gestor de paquetes de Python
- 🔑 **requests**: Peticiones HTTP/APIs
- 🔑 **BeautifulSoup**: Web scraping
- 🔑 **pandas**: Análisis de datos
- 🔑 **numpy**: Computación numérica
- 🔑 **matplotlib**: Visualización de datos

## Próximos pasos

En el Módulo 9 aprenderás sobre:
- Decoradores
- Generadores
- Context managers
- Funciones lambda avanzadas

**¡Ya puedes aprovechar el poder del ecosistema Python! 🎉**
