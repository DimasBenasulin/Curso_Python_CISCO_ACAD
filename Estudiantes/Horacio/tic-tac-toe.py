from random import randrange

board = [[1,2,3],[4,"X",6],[7,8,9]]

def DisplayBoard(board):
    print("+"+"-------"+"+"+"-------"+"+"+"-------"+"+")
    print("|       "+"|       "+"|       "+"|       ")
    print("|   ",board[0][0]," |   ",board[0][1]," |   ",board[0][2]," |")
    print("|       "+"|       "+"|       "+"|       ")
    print("+"+"-------"+"+"+"-------"+"+"+"-------"+"+")
    print("|       "+"|       "+"|       "+"|       ")
    print("|   ",board[1][0]," |   ",board[1][1]," |   ",board[1][2]," |")
    print("|       "+"|       "+"|       "+"|       ")
    print("+"+"-------"+"+"+"-------"+"+"+"-------"+"+")
    print("|       "+"|       "+"|       "+"|       ")
    print("|   ",board[2][0]," |   ",board[2][1]," |   ",board[2][2]," |")
    print("|       "+"|       "+"|       "+"|       ")
    print("+"+"-------"+"+"+"-------"+"+"+"-------"+"+")



def EnterMove(board):
    while True:
        movimiento = int(input("Ingresa tu mopvimiento: "))
        if movimiento >= 1 and movimiento <= 9:
            for i in range(0,3):
                for j in range(0,3):
                    if board[i][j] == str(movimiento):
                        board[i][j] = "O"
                    return
        else:
            print("Selecciona otro numero")
            continue

listavacia = []
def MakeListOfFreeFields(board):
    tamaño=len(board)
    for i in range(0,tamaño):
        for j in range(0,tamaño):
            if board[i][j] == "X" or board[i][j] == "O":
                continue
            else:
                listavacia.append(([i],[j]))


DisplayBoard(board)
EnterMove(board)
DisplayBoard(board)