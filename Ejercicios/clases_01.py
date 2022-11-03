class televisor:
    
    def __init__(self, color = 'Blanco'):
        self.colorin = color
        #print("Hola soy un televisor")
        #print(color)
    
    def ver_color(self):
        print(self.colorin)
        

    def cambiar_color(self, nuevo_color = 'Blanco'):
        self.colorin = nuevo_color


tele_habitacion = televisor('Rojo')
tele_cocina = televisor('Verde')
tele_baño = televisor('Amarillo')

print(tele_baño.ver_color())
tele_baño.cambiar_color('Naranja')
print(tele_baño.ver_color())
print(tele_habitacion.ver_color())