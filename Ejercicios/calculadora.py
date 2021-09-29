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

while (operacion != 6):
    if operacion == 1:
        resultado = operando_a + operando_b
    elif operacion == 2:
        resultado = operando_a - operando_b
    elif operacion == 3:
        resultado = operando_a * operando_b
    elif operacion == 4:
        resultado = operando_a ** operando_b

    print("El resultado es: ", resultado)
    print("\n")
    if int(input("Desea realizar otra operación? [0: NO/1: SI]")) == True:
        operando_a = float(input("Ingrese operando 1: "))
        operando_b = float(input("Ingrese operando 2: "))
        operacion = int(input("Ingrese operación a realizar: "))
    else:
        print("Have a nice day :-)")
        operacion = 6 
