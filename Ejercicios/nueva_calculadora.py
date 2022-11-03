print("Programa de cálculo en Python")
print("-----------------------------")
print("\n")
print("-----------------------------")
print("1. Suma                      ")
print("2. Resta                     ")
print("3. Multiplicación            ")
print("4. División                  ")
print("5. Potencia                  ")
print("6. Salir                     ")
print("-----------------------------")
print("\n")
operando_a = float(input("Ingrese operando 1: "))
operando_b = float(input("Ingrese operando 2: "))
operacion = int(input("Ingrese operación a realizar: "))

resultado = 0
opcion = 1

while opcion != 0:
    if operacion == 1:
        resultado = operando_a + operando_b
    elif operacion == 2:
        resultado = operando_a - operando_b
    elif operacion == 3:
        resultado = operando_a * operando_b
    elif operacion == 4:
        resultado = operando_a / operando_b
    elif operacion == 5:
        resultado = operando_a ** operando_b
            
    print("El resultado es: ", resultado)
    
    opcion = int(input("Desea realizar otra operación: 1 - Si / 0 - No :"))
    
    if opcion == 1:
        operando_a = float(input("Ingrese operando 1: "))
        operando_b = float(input("Ingrese operando 2: "))
        operacion = int(input("Ingrese operación a realizar: "))
    else:
        print("Que tenga un buen día")