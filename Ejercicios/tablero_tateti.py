from importlib.abc import TraversableResources
from random import randint

tablero = [["1", "2", "3"], ["4","5","6"], ["7","8","9"]]

def dibuja_tablero(board):
    print("+---+---+---+")
    for x in range(3):
        print("|", board[x][0], 
            "|", board[x][1], 
            "|", board[x][2], "|")
        print("+---+---+---+")

dibuja_tablero(tablero)

def verifica_movimiento(posicion, jugador = 'x'):
    if posicion > 6:
        if jugador in tablero[2]:
            return True
    elif posicion > 3:
        if jugador in tablero[1]:
            return True
    else:
        if jugador in tablero[0]:
            return True  
    return False

def ingresa_movimiento(posicion, jugador = 'x'):
    global tablero
    if posicion > 6:
        indice = posicion - 6
        tablero[2][indice-1] = jugador
    elif posicion > 3:
        indice = posicion - 3
        tablero[1][indice-1] = jugador
    else:
        indice = posicion - 1
        tablero[0][indice] = jugador
    

dibuja_tablero(tablero)
movimiento_usuario = int(input("Usuario ingrese movimiento 1...9 "))
if not verifica_movimiento(movimiento_usuario, "o"):
    ingresa_movimiento(movimiento_usuario, 'o')

dibuja_tablero(tablero)

