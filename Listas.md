# Listas en Python

## Operaciones con Listas

### Creación de una lista
```python
    mi_lista = [1, 2, 3, 4, 5] 
```

### Acceso a elementos de una lista
```python
    primer_elemento = mi_lista[0] # Accede al primer elemento
    ultimo_elemento = mi_lista[-1] # Accede al último elemento
```

### Recorrer elementos de una lista mediante un `for`
```python
for idx in range(len(mi_lista)):
    print(mi_lista[idx])
```

### Concatenación de listas
```python
    otra_lista = [6, 7, 8]
    lista_concatenada = mi_lista + otra_lista
```

## Métodos de Listas

- ### Método append() : Instera un elemento al final de la lista

``` python 
    mi_lista.append(7) 
```

- ### Método insert() : Inserta un elemento en una posición especifica dentro de la lista

``` python 
    mi_lista.append(7) 
```

- ### Método sort() : Ordena una lista 
``` python
    mi_lista.sort()
```

- ### Método reverse() : invierte la ubicación de los elementos 
``` python
    mi_lista.reverse()
```

## Operadores `in` y `not in`

Los operadores `in` y `not in` son utilizados en Python para comprobar si un valor está presente o no en una lista. Estos operadores son extremadamente útiles para la búsqueda de elementos dentro de una lista.

### Operador `in`

El operador `in` devuelve `True` si un valor está presente en la lista y `False` si no lo está.

```python
# Ejemplo de uso del operador in
frutas = ["manzana", "banana", "cereza"]
print("manzana" in frutas)  # Devuelve True
print("uva" in frutas)      # Devuelve False
``` 
### Operador `not in`

El operador not in devuelve True si un valor no está presente en la lista y False si lo está.

```python
# Ejemplo de uso del operador not in
frutas = ["manzana", "banana", "cereza"]
print("uva" not in frutas)      # Devuelve True
print("manzana" not in frutas)  # Devuelve False
```
### Uso en Condiciones

Estos operadores son comúnmente utilizados en expresiones condicionales para verificar la presencia o ausencia de elementos en una lista.

```python
# Ejemplo de uso en condiciones
if "manzana" in frutas:
    print("¡La manzana está en la lista!")
else:
    print("La manzana no está en la lista.")

if "pera" not in frutas:
    print("La pera no está en la lista.")
else:
    print("¡La pera está en la lista!")
```
 
> Ventajas : Los operadores `in` y `not in` proporcionan una forma simple y legible de verificar la existencia de elementos en una lista, lo que hace que el código sea más claro y conciso.

## Comprensión de Listas en Python

La comprensión de listas es una característica poderosa en Python que permite crear listas de manera concisa y elegante utilizando una sintaxis compacta. Permite definir y construir listas utilizando una única línea de código, lo que puede hacer que tu código sea más legible y eficiente.

### Sintaxis Básica

La sintaxis básica de la comprensión de listas es:

```python
nueva_lista = [expresion for elemento in iterable]
```
Esto crea una nueva lista `nueva_lista` donde cada elemento se obtiene aplicando la expresión a cada elemento del iterable.

#### Ejemplo de Comprensión de Listas
```python
# Crear una lista de cuadrados de números del 0 al 9
cuadrados = [x ** 2 for x in range(10)]
print(cuadrados)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```
### Uso de Condiciones

También es posible agregar condiciones a la comprensión de listas para filtrar los elementos del iterable.
```python
# Crear una lista de números pares del 0 al 9
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # Output: [0, 2, 4, 6, 8]
```

### Comprensión de Listas Anidadas
La comprensión de listas también puede ser anidada, lo que significa que puedes tener una comprensión de listas dentro de otra.

```python
# Crear una matriz 3x3 inicializada con ceros
matriz = [[0 for _ in range(3)] for _ in range(3)]
print(matriz)  # Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
```

> La comprensión de listas es una técnica poderosa y elegante en Python para crear listas de manera eficiente y legible. Es una herramienta importante en el arsenal de cualquier programador de Python y puede ayudarte a escribir código más claro y conciso.

