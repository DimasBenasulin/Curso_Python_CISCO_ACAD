bloques = int(input("Ingrese el número de bloques:"))

altura = 0
capa = 1

while (bloques >= capa):
    if bloques >= capa:
        bloques -= capa
        capa += 1
    else:
        bloques = 0
    altura += 1  

print("La altura de la pirámide:", altura)