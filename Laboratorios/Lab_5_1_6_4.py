def readint(prompt, minimo, maximo):
    try:
        valor=int(prompt)
        assert valor >= -10 and valor <= 10
        return 0
    except ValueError:
        return -1
    except AssertionError:
        return -2
    except:
        return -3

estado = 1

while estado == 1:
    entrada = input("Ingrese un número entre -10 y 10")
    resultado = readint(entrada, -10, 10)
    if resultado == 0:
        print(int(entrada))
        estado = 0
    elif resultado == -3:
        print("Oh cielos, algo salio mal...")

    elif resultado == -2:
        print("Error: El valor no está dentro del rango permitido (-10...10)")

    elif resultado == -1:
        print("Error: entrada incorrecta")