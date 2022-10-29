try:
    valor = int(input("Ingrese un numero natural: "))
    print("El inverso es:  ", 1/valor)

except ZeroDivisionError:
    print("Ingrese un valor difernete de cero ")

except ValueError:
    print("Ingrese solo dato numerico")

except:
    print("Hay algo mal que no funciona bien ")