# Funciones

## Definición Básica de una Función

```python
def nombre_funcion():
    # Cuerpo de la función
    print("Hola, Mundo!")
```
### Ejemplo

```python
def saludar():
    print("¡Hola a todos!")

saludar()
# Salida: ¡Hola a todos!
```

## Función con Parámetros

```python
def nombre_funcion(parametro1, parametro2):
    # Cuerpo de la función
    resultado = parametro1 + parametro2
    return resultado
```

### Ejemplo
```python
def sumar(a, b):
    return a + b

print(sumar(3, 4))
# Salida: 7
```
## Función con Valores por Defecto
```python
def nombre_funcion(parametro1, parametro2=10):
    # Cuerpo de la función
    resultado = parametro1 + parametro2
    return resultado
```
### Ejemplo
```python
def elevar_al_cuadrado(numero, exponente=2):
    return numero ** exponente

print(elevar_al_cuadrado(5))
# Salida: 25

print(elevar_al_cuadrado(5, 3))
# Salida: 125
```

## Funciones con un Número Arbitrario de Argumentos

*args (Argumentos Posicionales)

'''python
def nombre_funcion(*args):
    # Cuerpo de la función
    for arg in args:
        print(arg)
```
### Ejemplo
def imprimir_numeros(*numeros):
    for numero in numeros:
        print(numero)

imprimir_numeros(1, 2, 3, 4)
# Salida: 
# 1
# 2
# 3
# 4
``` 
**kwargs (Argumentos con Nombre)

```python
def nombre_funcion(**kwargs):
    # Cuerpo de la función
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")
```

### Ejemplo
```python
def imprimir_info(**info):
    for clave, valor in info.items():
        print(f"{clave}: {valor}")

imprimir_info(nombre="Juan", edad=30, ciudad="Madrid")
# Salida:
# nombre: Juan
# edad: 30
# ciudad: Córdoba
```


## Funciones Lambda (Funciones Anónimas)
```python
nombre_funcion = lambda parametros: expresión
```

### Ejemplo
```python
sumar = lambda a, b: a + b
print(sumar(5, 7))
# Salida: 12
```

## Funciones como Objetos de Primera Clase
Las funciones pueden ser asignadas a variables, pasadas como argumentos a otras funciones y retornadas por otras funciones.

```python
def sumar(a, b):
    return a + b

def operar(funcion, a, b):
    return funcion(a, b)

resultado = operar(sumar, 3, 4)
print(resultado)
# Salida: 7
``` 


### Ejemplo Completo

Ejemplo que reúne varios conceptos mencionados anteriormente:
```python
def calcular(operacion, *args, **kwargs):
    """
    Realiza una operación aritmética basada en los argumentos proporcionados.
    
    :param operacion: La operación a realizar ('sumar', 'restar', 'multiplicar', 'dividir').
    :param args: Valores numéricos para la operación.
    :param kwargs: Opcionales valores adicionales, como mostrar resultado intermedio.
    :return: El resultado de la operación.
    """
    resultado = 0
    if operacion == 'sumar':
        resultado = sum(args)
    elif operacion == 'restar':
        resultado = args[0]
        for num in args[1:]:
            resultado -= num
    elif operacion == 'multiplicar':
        resultado = 1
        for num in args:
            resultado *= num
    elif operacion == 'dividir':
        try:
            resultado = args[0]
            for num in args[1:]:
                resultado /= num
        except ZeroDivisionError:
            return "Error: División por cero."
    
    if kwargs.get('mostrar_intermedio', False):
        print(f"Resultado intermedio: {resultado}")
    
    return resultado

print(calcular('sumar', 1, 2, 3, 4, 5))
# Salida: 15
print(calcular('restar', 10, 5, 1))
# Salida: 4
print(calcular('multiplicar', 2, 3, 4))
# Salida: 24
print(calcular('dividir', 20, 4, 2))
# Salida: 2.5
print(calcular('dividir', 20, 0, 2))
# Salida: Error: División por cero.
'''





