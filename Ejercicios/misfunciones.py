def bisiesto(anio):
    if (anio % 400 == 0) or (anio % 4 == 0 and anio % 100 != 0):
        return True 
    else:
        return False

def dias_en_el_mes(anio, mes):
    normal = [31,28,31,30,31,30,31,31,30,31,30,31]
    bisiestos = normal[:]
    bisiestos[1] = 29
    dias = 0
    if bisiesto(anio):
        for i in range(mes):
            dias += bisiestos[i]
    else:
        for i in range(mes):
            dias += normal[i]
        
    return dias
