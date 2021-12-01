def DisplayBoard(board):
	print("+-------" * 3,"+",sep="")
	for row in range(3):
		print("|       " * 3,"|",sep="")
		for col in range(3):
			print("|   " + str(board[row][col]) + "   ",end="")
		print("|")
		print("|       " * 3,"|",sep="")
		print("+-------" * 3,"+",sep="")

def EnterMove(board):
	ok = False	#  assu fake mption - Lo necesitamos para entrar en bucle
	while not ok:
		move = input("Pon tu movimiento bro: ")
		ok = len(move) == 1 and move >= '1' and move <= '9' # Es valida?
		if not ok:
			print("Jajaja mal movimiento - repite tu entrada!") # no lo es - haz la entrada nuevamente
			continue
		move = int(move) - 1 	# numero de celda de 0 a 8
		row = move // 3 	# fila de celda
		col = move % 3		# columna de celdas
		sign = board[row][col]	# verifica el cuadrado seleccionado
		ok = sign not in ['O','X']
		if not ok:	# está ocupado - a la entrada nuevamente
			print("Repite tu tiro!")
			continue
	board[row][col] = 'O' 	# poner '0' en el cuadrado seleccionado

def MakeListOfFreeFields(board):
	free = []	# la lista está vacía inicialmente
	for row in range(3): # atraves de las filas
		for col in range(3): # atraves de las columnas
			if board[row][col] not in ['O','X']: # la fila esta libre?
				free.append((row,col)) # yes, it is - agregar nueva tupla a la lista
	return free


def VictoryFor(board,sgn):
	if sgn == "X":	# Estamos buscando x?
		who = 'me'	# si es del lado dela computadora
	elif sgn == "O": # o para "O"?
		who = 'you'	# si - es de nuestro lado
	else:
		who = None	# no debemos caer aquí
	cross1 = cross2 = True  # para diagonales
	for rc in range(3):
		if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:	# check row rc
			return who
		if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn: # check column rc
			return who
		if board[rc][rc] != sgn: # checar 1ra lista diagonal
			cross1 = False
		if board[2 - rc][2 - rc] != sgn: # checar 2da diagonal
			cross2 = False
	if cross1 or cross2:
		return who
	return None

import random

def DrawMove(board):
  free = MakeListOfFreeFields(board) # crear lista de campos libres
  cnt = (len(free))
  if cnt > 0: 	# si la lista no está vacía, elija un lugar para 'X' y configurelo
    this = random.randrange(cnt)
    row, col = free[this]
    board[row][col] = 'X'

board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ] # crea un tablero vacío
board[1][1] = 'X' # establece primero 'X' en el medio
free = MakeListOfFreeFields(board)
humanturn = True # ¿qué turno es ahora?
while len(free):
	DisplayBoard(board)
	if humanturn:
		EnterMove(board)
		victor = VictoryFor(board,'O')
	else:
		DrawMove(board)
		victor = VictoryFor(board,'X')
	if victor != None:
		break
	humanturn = not humanturn
	free = MakeListOfFreeFields(board)

DisplayBoard(board)
if victor == 'you':
	print("Ganaste!")
elif victor == 'me':
	print("Gane")
else:
	print("Jajaja!")