# Diccionarios en Python

## Crear un Diccionario

```python
# Diccionario vacío
diccionario_vacio = {}

# Diccionario con elementos
diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Cordoba"
}
```

## Acceder a Valores
```python
nombre = diccionario["nombre"]  # "Juan"
edad = diccionario.get("edad")  # 30
```

## Modificar Valores
```python
diccionario["edad"] = 31  # Cambia el valor de "edad" a 31
``` 

## Añadir Nuevos Pares Clave-Valor
```python
diccionario["profesion"] = "Ingeniero"
```

## Eliminar Pares Clave-Valor
```python
# Usando del
del diccionario["ciudad"]

# Usando pop
profesion = diccionario.pop("profesion")  # "Ingeniero"
``` 
## Comprobar Existencia de Clave
```python
existe_nombre = "nombre" in diccionario  # True
existe_ciudad = "ciudad" in diccionario  # False
```
## Iterar Sobre un Diccionario
```python
# Iterar sobre claves
for clave in diccionario:
    print(clave, diccionario[clave])

# Iterar sobre valores
for valor in diccionario.values():
    print(valor)

# Iterar sobre claves y valores
for clave, valor in diccionario.items():
    print(clave, valor)
```
## Métodos Comunes
```python
# Obtener todas las claves
claves = diccionario.keys()  # dict_keys(['nombre', 'edad'])

# Obtener todos los valores
valores = diccionario.values()  # dict_values(['Juan', 31])

# Obtener todos los pares clave-valor
items = diccionario.items()  # dict_items([('nombre', 'Juan'), ('edad', 31)])

# Limpiar el diccionario
diccionario.clear()  # {}

# Copiar un diccionario
diccionario_copia = diccionario.copy()
```

## Diccionarios Anidados
```python
estudiantes = {
    "Juan": {"edad": 25, "ciudad": "Madrid"},
    "Ana": {"edad": 22, "ciudad": "Barcelona"}
}

# Acceder a valores en diccionarios anidados
edad_juan = estudiantes["Juan"]["edad"]  # 25
```
## Comprensión de Diccionarios
```python
cuadrados = {x: x*x for x in range(6)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```
## Ejemplos Avanzados
### Contar Frecuencia de Elementos
```python
from collections import Counter

lista = ["a", "b", "a", "c", "a", "b"]
frecuencia = Counter(lista)  # Counter({'a': 3, 'b': 2, 'c': 1})
```
### Combinar Diccionarios
```python
dic1 = {"a": 1, "b": 2}
dic2 = {"b": 3, "c": 4}

# Usando el operador ** (Python 3.5+)
dic_combinado = {**dic1, **dic2}  # {'a': 1, 'b': 3, 'c': 4}

# Usando el método update
dic1.update(dic2)  # dic1 es ahora {'a': 1, 'b': 3, 'c': 4}
```
### Ordenar un Diccionario por Claves o Valores
```python
# Ordenar por claves
dic_ordenado_claves = dict(sorted(diccionario.items()))  # {'edad': 31, 'nombre': 'Juan'}

# Ordenar por valores
dic_ordenado_valores = dict(sorted(diccionario.items(), key=lambda item: item[1]))  # {'nombre': 'Juan', 'edad': 31}
```

