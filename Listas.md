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
