n = int(input("Ingresa un número natural positivo : "))
contador = 0
while n > 1:
    if n % 2 == 0:
	    n = n // 2
    else:
        n = (n*3) + 1
    contador += 1
    
print("Cantidad de pasos: ", contador, "Valor de n", n)
