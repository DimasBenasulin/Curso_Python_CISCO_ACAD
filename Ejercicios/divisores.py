#Programa para determinar los divisores de un numero
#Elaborado en Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06)
print("introduzca el numero")

numero = int(input()) #aquí se lee el número entero
contador = 0
print("los divisores de ",numero)
for divisor in range(1,numero+1):
    if (numero % divisor) == 0 :
        print(divisor,"es divisor")
        contador += 1
print("el numero ",numero," tiene ",contador," divisores")