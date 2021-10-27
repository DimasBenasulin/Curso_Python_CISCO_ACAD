print("--- Agenda en Python 2021 ---")
print("-----------------------------")
print("\n")
print("-----------------------------")
print("1. Añadir/Modificar          ")
print("2. Buscar                    ")
print("3. Borrar                    ")
print("4. Listar                    ")
print("5. Salir                     ")
print("-----------------------------")
print("\n")

agenda = {'Eliseo': 3513781703, 'Rodrigo': 3541653441, 'Joaquin': 3513022346, 'Horacio': 3512585678, 'Pablo': 3516580942, 'Milton': 3512436454, "Romina": 3516665318, "Milton": 3512436454, "Muriel": 3517617402, 'Exequiel': 3515577124, "Matías": 3512268934, 'Martin': 3512520687
          }

operacion = int(input("Ingrese operación a realizar: "))

resultado = 0

while (operacion != 5):

    # Añadir o Modificar
    if operacion == 1:
        nombre = input("Ingrese nuevo Nombre a la agenda: ")
        tel = input("Ingrese número de telefono: ")
        agenda[nombre] = int(tel)

        operacion = int(input("Ingrese operación a realizar: "))
        # Buscar
    elif operacion == 2:
        nombre= input("INGRESE NOMBRE:")
        print(agenda.get(nombre, 'No esta en la agenda'))
        
        operacion = int(input("Ingrese operación a realizar: "))
        # Borrar
    elif operacion == 3:
        print("Ingrese Nombre a borrar: \n")

        nombre = input("Ingrese Nombre: ")

        if agenda.get(nombre):
            if input("Desea Borrar el registro seleccionado? [S/N]") == 'S':
                del agenda[nombre]
                print("Registro borrado")
            else:
                print("No se ha borrado el registro") 
        else:
            print("No Existe el nombre ingresado")
        operacion = int(input("Ingrese operación a realizar: "))
        # Listar
    elif operacion == 4:
        for x,y in sorted(agenda.items()):
            print(x,y)

        operacion = int(input("Ingrese operación a realizar: "))
    else:
        print("Have a nice day :-)")
        operacion = 5

