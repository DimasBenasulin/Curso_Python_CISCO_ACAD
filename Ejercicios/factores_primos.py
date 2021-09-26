# Programa para descomponer un número compuesto en sus factores primos
# Dimas Benasulin

n=int(input("ingrese número: "))
print("Descomposición en factores primos")
print("\n")
resultado="Fp: " + str(n) + " = "
for i in range(2, n + 1):
    while n % i == 0:
        resultado += str(i) + " . "
        n = n / i
print(resultado)            
