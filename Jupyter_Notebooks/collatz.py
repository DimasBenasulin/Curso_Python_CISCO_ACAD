n = int (input("Ingresa un número natural positivo : "))
contador = 0
while n > 1:
    if n % 2 == 0:                      
	    n = n // 2
        print("Instancia par :", n)
    else:                               
	    n = (n*3) + 1
        print("Instancia impar:", n)
        contador += 1
    
print("Cantidad de pasos: ", contador)