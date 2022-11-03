from random import randrange

board=[["1","2","3"],["4","5","6"], ["7","8","9"]]
board[1][1]="X"


def DisplayBoard(board):
    print(("+"+8*"-")*3+"+")
    print(("|"+8*" ")*3+"|")
    print("|"+ " "*3 +str(board[0][0])+ " "*3 +" |"+" "*3+str(board[0][1])+" "*3+" |" + " "*3+ str(board[0][2])+" "*3+" |")
    print(("|"+8*" ")*3+"|")
    print(("+"+8*"-")*3+"+")
    print(("|"+8*" ")*3+"|")
    print("|"+ " "*3 +str(board[1][0])+ " "*3 +" |"+" "*3+str(board[1][1])+" "*3+" |" + " "*3+ str(board[1][2])+" "*3+" |")
    print(("|"+8*" ")*3+"|")
    print(("+"+8*"-")*3+"+")
    print(("|"+8*" ")*3+"|")
    print("|"+ " "*3 +str(board[2][0])+ " "*3 +" |"+" "*3+str(board[2][1])+" "*3+" |" + " "*3+ str(board[2][2])+" "*3+" |")
    print(("|"+8*" ")*3+"|")
    print(("+"+8*"-")*3+"+")
#
# la función acepta un parámetro el cual contiene el estado actual del tablero
# y lo muestra en la consola
#

def EnterMove(board):
# la función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,   
# verifica la entrada y actualiza el tablero acorde a la decisión del usuario   
# aca tengo el error de que si no esta en la lista nose como hacer para que vuelva a pedir otro movimiento 
    lugares={1:(0,0) , 2: (0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}
 
    mov=int(input("INGRESA TU MOVIMIENTO "))
    lugmov=lugares.get(mov)
    lista=MakeListOfFreeFields(board)
    
    while lugmov in lista:
        if 0<mov<10:
           
           board[lugmov[0]][lugmov[1]]="O"
           indice=lista.index(lugmov)
           del(lista[indice])
           
   # else:
    #mov=int(input("INGRESA TU MOVIMIENTO "))
    #lugmov=lugares.get(mov)

    
    return DisplayBoard(board)


def MakeListOfFreeFields(board):
# la función examina el tablero y construye una lista de todos los cuadros vacío
# la lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna    
    freeX=[]
    free=[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    for i in range(3):    
        for j in range(3):
            if "X" == board[i][j]:
                freeX.append((i,j))
    
    
  
    for i in range(3):    
        for j in range(3):
            if "O" == board[i][j]:
                freeX.append((i,j))
    for k in range(len(freeX)):
        if freeX[k] in free:
            indice=free.index(freeX[k])
            del(free[indice])
               

        


    free.sort()
    return free


def VictoryFor(board, sign):
    f1=board[0]
    f2=board[1]
    f3=board[2]
    diag1=[f1[0], f2[1], f3[2]]
    diag2=[f1[2], f2[1], f3[0]]
# la función analiza el estatus del tablero para verificar si
# el jugador que utiliza las 'O's o las 'X's ha ganado el juego
    if f1[0]==f1[1]==f1[2]==sign:
        
        print("EL JUGADOR QUE USA " + sign + " HA GANADO EL JUEGO")
    elif f2[0]==f2[1]==f2[2]==sign:
        print("EL JUGADOR QUE USA " + sign + " HA GANADO EL JUEGO")
    elif f3[0]==f3[1]==f3[2]==sign:
        print("EL JUGADOR QUE USA " + sign + " HA GANADO EL JUEGO")
    elif diag1[0]==diag1[1]==diag1[2]==sign:
        print("EL JUGADOR QUE USA " + sign + " HA GANADO EL JUEGO")
    elif diag2[0]==diag2[1]==diag2[2]==sign:
        print("EL JUGADOR QUE USA " + sign + " HA GANADO EL JUEGO") 
    else:
        lista=MakeListOfFreeFields(board)
        if len(lista)==0:
            print("LOS JUGADORES HAN EMPATADO")
        else:
            print("EL JUEGO PUEDE CONTINUAR")
        
    
def DrawMove(board):
#
# la función dibuja el movimiento de la maquina y actualiza el tablero
#ACA TENGO EL ERROR DE QUE CUANDO EL MOVIMIENTO generado por randrange no esta en la lista nose como
#volverlo a actualizar para que elija otro hasta que encuentro uno que si este en la lista 
 
    lugares={1:(0,0) , 2: (0,1), 3:(0,2), 4:(1,0), 5:(1,1), 6:(1,2), 7:(2,0), 8:(2,1), 9:(2,2)}
    mov=randrange(1,9)
    lugmov=lugares.get(mov)
    lista=MakeListOfFreeFields(board)
    if lugmov in lista:
        board[lugmov[0]][lugmov[1]]="X"
        indice=lista.index(lugmov)
        del(lista[indice])
    elif lugmov not in lista:
        mov=randrange(1,9)
        lugmov=lugares.get(mov)
    DisplayBoard(board)
    return board

print("PRIMER TURNO")       
DisplayBoard(board)
EnterMove(board)
VictoryFor(board, "X")
VictoryFor(board, "O")

print("SEGUNDO TURNO")
DrawMove(board)
EnterMove(board)
VictoryFor(board, "X")
VictoryFor(board, "O")
print("tercer TURNO")
DrawMove(board)
EnterMove(board)
VictoryFor(board, "X")
VictoryFor(board, "O")
print("Cuarto1 TURNO")
DrawMove(board)
EnterMove(board)
VictoryFor(board, "X")
VictoryFor(board, "O")

    
    
    
    