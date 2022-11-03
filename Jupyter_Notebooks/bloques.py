blocks = int (input("Ingresa la cantidad de bloques : "))

capa = 1 

while blocks >= capa:
    blocks -= capa
    if blocks > capa:
        capa += 1


print("La altura de la piramide es; ", capa)