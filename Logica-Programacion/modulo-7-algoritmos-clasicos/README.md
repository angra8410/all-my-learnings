# Módulo 7: Algoritmos Clásicos

## Introducción

Los algoritmos clásicos son soluciones probadas y optimizadas para problemas comunes. Aprender estos algoritmos te ayudará a resolver problemas de manera eficiente y comprender mejor la programación.

## Conceptos Principales

### 1. Búsqueda lineal

La **búsqueda lineal** recorre cada elemento hasta encontrar el buscado.

```
FUNCION busqueda_lineal(lista, elemento):
    PARA i DESDE 0 HASTA longitud(lista)-1 HACER
        SI lista[i] == elemento ENTONCES
            RETORNAR i  // Retorna la posición
        FIN SI
    FIN PARA
    RETORNAR -1  // No encontrado
FIN FUNCION
```

**Complejidad:** O(n) - puede revisar todos los elementos

### 2. Búsqueda binaria

La **búsqueda binaria** busca en listas ordenadas dividiendo el espacio de búsqueda a la mitad.

```
FUNCION busqueda_binaria(lista_ordenada, elemento):
    inicio = 0
    fin = longitud(lista_ordenada) - 1
    
    MIENTRAS inicio <= fin HACER
        medio = (inicio + fin) / 2
        
        SI lista_ordenada[medio] == elemento ENTONCES
            RETORNAR medio
        SINO SI lista_ordenada[medio] < elemento ENTONCES
            inicio = medio + 1
        SINO
            fin = medio - 1
        FIN SI
    FIN MIENTRAS
    
    RETORNAR -1
FIN FUNCION
```

**Complejidad:** O(log n) - mucho más rápida que lineal

### 3. Ordenamiento burbuja

**Bubble sort** compara elementos adyacentes y los intercambia si están en el orden incorrecto.

```
FUNCION ordenamiento_burbuja(lista):
    n = longitud(lista)
    
    PARA i DESDE 0 HASTA n-1 HACER
        PARA j DESDE 0 HASTA n-i-2 HACER
            SI lista[j] > lista[j+1] ENTONCES
                // Intercambiar
                temp = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = temp
            FIN SI
        FIN PARA
    FIN PARA
FIN FUNCION
```

### 4. Ordenamiento por selección

**Selection sort** encuentra el mínimo y lo coloca en su posición correcta.

```
FUNCION ordenamiento_seleccion(lista):
    n = longitud(lista)
    
    PARA i DESDE 0 HASTA n-2 HACER
        min_indice = i
        
        PARA j DESDE i+1 HASTA n-1 HACER
            SI lista[j] < lista[min_indice] ENTONCES
                min_indice = j
            FIN SI
        FIN PARA
        
        // Intercambiar
        temp = lista[i]
        lista[i] = lista[min_indice]
        lista[min_indice] = temp
    FIN PARA
FIN FUNCION
```

## Implementación Práctica

### Ejercicio 1: Buscar elemento en lista

```
numeros = [5, 2, 8, 1, 9, 3]
LEER elemento_buscar

posicion = busqueda_lineal(numeros, elemento_buscar)

SI posicion != -1 ENTONCES
    ESCRIBIR "Encontrado en posición:", posicion
SINO
    ESCRIBIR "No encontrado"
FIN SI
```

### Ejercicio 2: Ordenar números

```
numeros = [64, 34, 25, 12, 22, 11, 90]

ESCRIBIR "Lista original:", numeros
ordenamiento_burbuja(numeros)
ESCRIBIR "Lista ordenada:", numeros
```

### Ejercicio 3: Encontrar máximo y mínimo

```
FUNCION encontrar_maximo(lista):
    maximo = lista[0]
    PARA CADA elemento EN lista HACER
        SI elemento > maximo ENTONCES
            maximo = elemento
        FIN SI
    FIN PARA
    RETORNAR maximo
FIN FUNCION

FUNCION encontrar_minimo(lista):
    minimo = lista[0]
    PARA CADA elemento EN lista HACER
        SI elemento < minimo ENTONCES
            minimo = elemento
        FIN SI
    FIN PARA
    RETORNAR minimo
FIN FUNCION
```

## Mejores Prácticas

1. **Elige el algoritmo correcto**: Considera el tamaño de los datos
2. **Comprende la complejidad**: Algunos algoritmos son más rápidos que otros
3. **Optimiza cuando sea necesario**: No siempre necesitas el más rápido
4. **Prueba con diferentes casos**: Listas vacías, ordenadas, inversas

## Conceptos Clave

- 🔑 **Búsqueda lineal**: O(n), simple pero lenta
- 🔑 **Búsqueda binaria**: O(log n), rápida pero requiere lista ordenada
- 🔑 **Ordenamiento burbuja**: O(n²), simple pero ineficiente
- 🔑 **Ordenamiento selección**: O(n²), intuitivo

## Motivación Final

¡Extraordinario! 🎉 Conoces algoritmos que son la base de la informática moderna.

**¡Ahora piensas como un científico de la computación! 🧠🔬**
