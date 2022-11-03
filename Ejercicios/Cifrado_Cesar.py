text = input("Ingresa tu mensaje: ")
codigo = int(input("Ingrese desplazamiento: "))

cifrado = ""
aux = ""

for caracter in text:
    #Ver si el caracter esta en mayúscula
    if caracter.isupper():
        # desplazamiento a la posicion 0
        code_indx = ord(caracter) - ord('A')
        
        code_sft = (code_indx + codigo) % 26 + ord('A')

        aux = chr(code_sft)
        cifrado += aux

    #Ver si el caracter esta en minúscula        
    elif caracter.islower():

        #Restar el valor en unicode de 'a' para obtener un rango de 0 a 25
        code_indx = ord(caracter) - ord('a')

        code_sft = (code_indx + codigo) % 26 + ord('a')

        aux = chr(code_sft)
        cifrado += aux

    elif caracter.isdigit():
        code_sft = (int(caracter) + codigo) % 10
        cifrado += str(code_sft)

    else:
        cifrado += caracter

print(cifrado)