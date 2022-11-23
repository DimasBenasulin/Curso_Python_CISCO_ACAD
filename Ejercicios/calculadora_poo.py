class calculadora:

    def __init__(self):
        self.__operando_A = 0.0
        self.__operando_B = 0.0
        self.__resultado = 0.0
    
    def ingreso_operandos(self, opA, opB):
        self.__operando_A = opA
        self.__operando_B = opB

    def sumar(self):
        self.__resultado = self.__operando_A + self.__operando_B     

    def restar(self):
        self.__resultado = self.__operando_A - self.__operando_B

    def multiplicar(self):
        self.__resultado = self.__operando_A * self.__operando_B

    def dividir(self):
        self.__resultado = self.__operando_A / self.__operando_B

    def mostrar_display(self):
        return self.__resultado

    def set_operacion(self, opcion):
        if opcion == 1:
            self.sumar()
            return self.__resultado
        elif opcion == 2:
            self.restar()
            return self.__resultado
        elif opcion == 3:
            self.multiplicar()
            return self.__resultado
        elif opcion == 4:
            self.dividir()
            return self.__resultado
        else:
            return 0


calc_tienda = calculadora()
calc_despensa = calculadora()
calc_mercado = calculadora()

print("Calculadora de la Tienda \r")
numA = float(input("Ingrese operando A"))
numB = float(input("Ingrese operando B"))
opc = int(input("Ingrese operación a realizar"))

# Llamo a la calculadora de la Tienda
calc_tienda.ingreso_operandos(numA, numB)
calc_tienda.set_operacion(opc)
print("El resultado es: ", calc_tienda.mostrar_display())

print("Calculadora de la Despensa \r")
numA = float(input("Ingrese operando A"))
numB = float(input("Ingrese operando B"))
opc = int(input("Ingrese operación a realizar"))

# Llamo a la calculadora de la Despensa
calc_despensa.ingreso_operandos(numA, numB)
calc_despensa.set_operacion(opc)
print("El resultado es: ", calc_despensa.mostrar_display())

print("Calculadora del Mercado \r")
numA = float(input("Ingrese operando A"))
numB = float(input("Ingrese operando B"))
opc = int(input("Ingrese operación a realizar"))

# Llamo a la calculadora de la Mercado
calc_mercado.ingreso_operandos(numA, numB)
calc_mercado.set_operacion(opc)
print("El resultado es: ", calc_mercado.mostrar_display())

# Mostrar Display Actuales
print("Display de la Calculadora de la Tienda : ", calc_tienda.mostrar_display())
print("Display de la Calculadora de la Despensa : ", calc_despensa.mostrar_display())
print("Display de la Calculadora del Mercado : ", calc_mercado.mostrar_display())
