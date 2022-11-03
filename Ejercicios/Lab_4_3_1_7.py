from misfunciones import *

tabla_meses = {1:"enero", 
               2:"febrero",
               3:"marzo",
               4:"abril",
               5:"mayo",
               6:"junio",
               7:"julio",
               8:"agosto",
               9:"septiembre",
               10:"octubre",
               11:"noviembre",
               12:"diciembre"}

year = int(input("Ingrese año :"))
month = int(input("Ingrese mes :"))

print("La cantidad de dias hasta el mes: ", tabla_meses[month], " es de : ", dias_en_el_mes(year, month))
