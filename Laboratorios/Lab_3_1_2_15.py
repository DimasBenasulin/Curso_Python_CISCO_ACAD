c0=int(input("Ingrese semilla distinta de cero y positiva : "))

pasos = 0

while c0 <= 0:
    print("Por favor respete lo que se le solicita")
    print("\n")
    c0 = int(input("Ingrese semilla distinta de cero y positiva"))
    
while(c0 != 1):
    if (c0 % 2) == 0:
        c0 = c0 // 2
    else:
        c0 = c0 * 3 + 1
    pasos += 1
    print(c0)

print("pasos: ", pasos)


    

