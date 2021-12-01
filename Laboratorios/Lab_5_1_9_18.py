def misplit(strng):
    lista=[]
    aux = strng.strip()
    if len(aux) == 0:
        return lista
    mi_indice = 0
    mensaje = '' 
    for ix in range(len(aux)):
        mensaje += aux[ix]
        if aux[ix] == ' ':
            mensaje = mensaje.strip()
            lista.append(mensaje)
            mensaje = ''
    lista.append(mensaje)
    return lista   