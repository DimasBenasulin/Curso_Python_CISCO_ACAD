#entradas
anio=int(input("Ingrese año: "))

#salidas
print("\n Resultado: ")
print("\n")
if (anio % 400 == 0) or (anio % 4 == 0) and (anio % 100 != 0):
    print("El año ingresado fue o será bisiesto")
else:
    print("No es bisiesto")