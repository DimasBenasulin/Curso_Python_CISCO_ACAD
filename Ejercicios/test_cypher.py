caracter = "A"
codigo = 5

code_indx = ord(caracter) - ord('A')
        
code_sft = (code_indx + codigo) % 26 + ord('A')

aux = chr(code_sft)

print(aux)