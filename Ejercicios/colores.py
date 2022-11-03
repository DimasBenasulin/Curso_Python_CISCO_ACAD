def construye_tabla_formatos():
    for estilo in range(8):
        for colortexto in range(30,38):
            cad_cod = ''
            for colorfondo in range(40,48): 
                fmto = ';'.join([str(estilo), 
                                 str(colortexto),
                                 str(colorfondo)]) 
                cad_cod+="\033["+fmto+"m "+fmto+" \033[0m" 
            print(cad_cod)
        print('\n')

construye_tabla_formatos()