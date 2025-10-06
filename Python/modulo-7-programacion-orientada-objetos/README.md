# Módulo 7: Programación Orientada a Objetos

## Introducción

¡Bienvenido al Módulo 7! Hasta ahora has usado funciones y estructuras de datos. La **Programación Orientada a Objetos (POO)** es un paradigma que te permite organizar código de forma más natural, agrupando datos y funcionalidad.

En este módulo aprenderás:
- Qué son las clases y objetos
- Atributos y métodos
- Constructor (__init__)
- Encapsulamiento
- Herencia
- Polimorfismo
- Métodos especiales

## ¿Por qué es importante?

La POO te permite:
- Modelar entidades del mundo real (Usuario, Producto, Auto)
- Reutilizar código mediante herencia
- Organizar proyectos grandes de forma mantenible
- Crear código más legible y profesional

**Analogía:** Una clase es como un molde para galletas. De un molde (clase) puedes hacer muchas galletas (objetos), todas con la misma forma pero con diferentes decoraciones (atributos).

## Conceptos Principales

### 1. Clases y Objetos

**Definir una clase:**
```python
class Persona:
    pass  # Clase vacía por ahora

# Crear objetos (instancias)
persona1 = Persona()
persona2 = Persona()
```

**Clase con atributos:**
```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

# Crear objetos
ana = Persona("Ana", 25)
carlos = Persona("Carlos", 30)

print(ana.nombre)  # Ana
print(carlos.edad)  # 30
```

**Constructor `__init__`:**
- Se ejecuta automáticamente al crear un objeto
- `self` representa la instancia actual
- Inicializa atributos del objeto

### 2. Métodos

Los métodos son funciones dentro de una clase:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        return f"Hola, soy {self.nombre}"
    
    def cumpleaños(self):
        self.edad += 1
        return f"¡Ahora tengo {self.edad} años!"

# Usar métodos
ana = Persona("Ana", 25)
print(ana.saludar())  # Hola, soy Ana
print(ana.cumpleaños())  # ¡Ahora tengo 26 años!
```

### 3. Atributos de Clase vs Instancia

```python
class Estudiante:
    # Atributo de clase (compartido por todos)
    institucion = "Universidad Python"
    
    def __init__(self, nombre, carrera):
        # Atributos de instancia (único por objeto)
        self.nombre = nombre
        self.carrera = carrera

est1 = Estudiante("Ana", "Informática")
est2 = Estudiante("Carlos", "Matemáticas")

print(est1.institucion)  # Universidad Python
print(est2.institucion)  # Universidad Python (mismo valor)
print(est1.nombre)  # Ana
print(est2.nombre)  # Carlos (diferente)
```

### 4. Encapsulamiento

Convención: atributos privados empiezan con `_`:

```python
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self._saldo = saldo_inicial  # "Privado" por convención
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad
            return True
        return False
    
    def retirar(self, cantidad):
        if 0 < cantidad <= self._saldo:
            self._saldo -= cantidad
            return True
        return False
    
    def consultar_saldo(self):
        return self._saldo

cuenta = CuentaBancaria("Ana", 1000)
cuenta.depositar(500)
print(cuenta.consultar_saldo())  # 1500
```

### 5. Herencia

Una clase puede heredar de otra:

```python
# Clase padre (base)
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hacer_sonido(self):
        pass

# Clases hijas
class Perro(Animal):
    def hacer_sonido(self):
        return "¡Guau!"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"

# Usar
perro = Perro("Rex")
gato = Gato("Michi")

print(perro.nombre)  # Rex (heredado)
print(perro.hacer_sonido())  # ¡Guau!
print(gato.hacer_sonido())  # ¡Miau!
```

**Super() para llamar al padre:**
```python
class Empleado:
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario

class Gerente(Empleado):
    def __init__(self, nombre, salario, departamento):
        super().__init__(nombre, salario)  # Llama al constructor padre
        self.departamento = departamento

gerente = Gerente("Ana", 5000, "IT")
print(gerente.nombre)  # Ana
print(gerente.departamento)  # IT
```

### 6. Polimorfismo

Diferentes clases pueden tener métodos con el mismo nombre:

```python
class Forma:
    def area(self):
        pass

class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado ** 2

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return 3.14159 * self.radio ** 2

# Polimorfismo en acción
formas = [Cuadrado(5), Circulo(3)]
for forma in formas:
    print(f"Área: {forma.area()}")
```

### 7. Métodos Especiales (Dunder Methods)

```python
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def __str__(self):
        # Representación legible
        return f"{self.titulo} por {self.autor}"
    
    def __repr__(self):
        # Representación técnica
        return f"Libro('{self.titulo}', '{self.autor}')"
    
    def __len__(self):
        return len(self.titulo)

libro = Libro("Python 101", "Ana García")
print(libro)  # Python 101 por Ana García (__str__)
print(len(libro))  # 10 (__len__)
```

**Otros métodos especiales:**
- `__add__`: Sobrecarga del operador +
- `__eq__`: Sobrecarga del operador ==
- `__lt__`: Sobrecarga del operador <
- `__getitem__`: Permite indexación obj[key]

## Implementación Práctica

### Ejemplo 1: Sistema de Biblioteca

```python
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.prestado = False
    
    def prestar(self):
        if not self.prestado:
            self.prestado = True
            return True
        return False
    
    def devolver(self):
        self.prestado = False

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
    
    def agregar_libro(self, libro):
        self.libros.append(libro)
    
    def buscar_por_titulo(self, titulo):
        for libro in self.libros:
            if titulo.lower() in libro.titulo.lower():
                return libro
        return None
    
    def listar_disponibles(self):
        return [libro for libro in self.libros if not libro.prestado]

# Usar
biblioteca = Biblioteca("Biblioteca Central")
libro1 = Libro("Python 101", "Ana", "12345")
libro2 = Libro("Java Avanzado", "Carlos", "67890")

biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

libro1.prestar()
print(f"Libros disponibles: {len(biblioteca.listar_disponibles())}")
```

### Ejemplo 2: Juego de Rol Simple

```python
class Personaje:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
    
    def atacar(self, objetivo):
        objetivo.recibir_daño(self.ataque)
        print(f"{self.nombre} atacó a {objetivo.nombre}")
    
    def recibir_daño(self, daño):
        self.vida -= daño
        if self.vida < 0:
            self.vida = 0
    
    def esta_vivo(self):
        return self.vida > 0

class Guerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=100, ataque=20)
        self.defensa = 10

class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre, vida=70, ataque=30)
        self.mana = 100

# Batalla
guerrero = Guerrero("Arturo")
mago = Mago("Merlín")

guerrero.atacar(mago)
print(f"{mago.nombre} tiene {mago.vida} de vida")
```

## Mejores Prácticas

1. **Nombres de clases en PascalCase**
   ```python
   class MiClase:  # ✅
   class mi_clase:  # ❌
   ```

2. **Un archivo, una clase principal (para proyectos grandes)**
   ```
   persona.py → class Persona
   estudiante.py → class Estudiante(Persona)
   ```

3. **Usa propiedades para getter/setter**
   ```python
   class Persona:
       @property
       def edad(self):
           return self._edad
       
       @edad.setter
       def edad(self, valor):
           if valor >= 0:
               self._edad = valor
   ```

4. **Documenta clases y métodos**
   ```python
   class MiClase:
       """Descripción de la clase"""
       
       def mi_metodo(self):
           """Descripción del método"""
           pass
   ```

## Conceptos clave para recordar

- 🔑 **Clase**: Plantilla para crear objetos
- 🔑 **Objeto**: Instancia de una clase
- 🔑 **__init__**: Constructor, inicializa objetos
- 🔑 **self**: Referencia a la instancia actual
- 🔑 **Herencia**: Clase que extiende otra
- 🔑 **Polimorfismo**: Métodos con mismo nombre, diferente comportamiento

## Próximos pasos

En el Módulo 8 aprenderás sobre:
- Librerías populares de Python
- NumPy, Pandas, Requests
- Automatización de tareas

**¡Ya puedes crear programas con arquitectura orientada a objetos! 🎉**
