n=int(input("ingrese número: "))

if n < 1:
    print("Debe ingresar un número positivo")
elif n == 2:
    print("El Número: ", n, "es primo")
else:
    aux=False
    for i in range(2, n):
        if n % i == 0:
            print("El número: ", n, "No es primo")
            aux=1
            break
    if aux == False:
        print("El Número: ", n, "es primo")

