hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# coloca tu código aqui

t_total = hora * 60 + min
t_total = t_total + dura 

#separo en dos variables minutos y horas 
#dura_hora = dura // 60
#dura_min = dura % 60

fin_hora = t_total // 60
fin_min = t_total % 60


if fin_hora > 24:
    nota = "del día siguiente"
else:
    nota = "del día :-)"

#Arreglo de la hora
fin_hora = fin_hora % 24



#primero proceso los minutos que son quienes pueden desbordar

#min = min + dura_min

#actualizo hora de fin por desborde

#hora = hora + ((min + dura_min) // 60)

#actualizo minutos

#min = min + 


print("el Evento finalizará a las: ", fin_hora, ":", fin_min, nota)
