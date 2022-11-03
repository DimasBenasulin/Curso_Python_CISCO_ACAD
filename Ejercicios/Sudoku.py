sudoku=input("INGRESE FILA A VERIFICAR: ")
sudoku=sudoku.split()
matsudo=[]
for i in range (len(sudoku)):
    
    matsudo.append(list(sudoku[i]))
print(matsudo)
flag=True

cuadro0=[]            
for i in range(3):
    for j in range(3):
        cuadro0.append(matsudo[i][j])
print(cuadro0)

for i in range(len(cuadro0)):
    for j in range(i+1,len(cuadro0)):
        if cuadro0[i] ==cuadro0[j]:
          
            flag=False
            break

cuadro1=[]            

for i in range(3):
    for j in range(3,6):
        cuadro1.append(matsudo[i][j])
for i in range(len(cuadro1)):
    for j in range(i+1,len(cuadro1)):
        if cuadro1[i] ==cuadro1[j]:
            
        
            flag=False
            break
            
cuadro2=[]            
for i in range(3):
    for j in range(5,9):
        cuadro2.append(matsudo[i][j])
for i in range(len(cuadro2)):
    for j in range(i+1,len(cuadro2)):
        if cuadro2[i] ==cuadro2[j]:
           
            flag=False
            break
            
cuadro3=[]            
for i in range(3,6):
    for j in range(3):
        cuadro3.append(matsudo[i][j])
for i in range(len(cuadro3)):
    for j in range(i+1,len(cuadro3)):
        if cuadro3[i] ==cuadro3[j]:
           
            flag=False
            break

cuadro4=[]            
for i in range(3,6):
    for j in range(3,6):
        cuadro4.append(matsudo[i][j])

for i in range(len(cuadro4)):
    for j in range(i+1,len(cuadro4)):
        if cuadro4[i] ==cuadro4[j]:
           
            flag=False
            break
cuadro5=[]            
for i in range(3,6):
    for j in range(5,9):
        cuadro5.append(matsudo[i][j])
for i in range(len(cuadro5)):
    for j in range(i+1,len(cuadro5)):
        if cuadro5[i] ==cuadro5[j]:
           
            flag=False
            break
            
cuadro6=[]            
for i in range(6,9):
    for j in range(3):
        cuadro6.append(matsudo[i][j])
for i in range(len(cuadro6)):
    for j in range(i+1,len(cuadro6)):
        if cuadro6[i] ==cuadro6[j]:
           
            flag=False
            break
cuadro7=[]            
for i in range(6,9):
    for j in range(3,6):
        cuadro7.append(matsudo[i][j])
for i in range(len(cuadro7)):
    for j in range(i+1,len(cuadro7)):
        if cuadro7[i] ==cuadro7[j]:
           
            flag=False
            break
            
cuadro8=[]            
for i in range(6,9):
    for j in range(5,9):
        cuadro8.append(matsudo[i][j])
for i in range(len(cuadro8)):
    for j in range(i+1,len(cuadro8)):
        if cuadro8[i] ==cuadro8[j]:
           
            flag=False
            break

for fila in matsudo:
    for j in range(len(matsudo[0])):    
        for i in range(j+1, len(matsudo[0])):
            if fila[j]==fila[i]:
                
               
                flag=False
                break
for fila in matsudo:
    for i in range(9):
        for j in range(i+1, 9):
            if fila[i]==matsudo[i][j]:
               
                flag=False
                #print(i, j,fila[i],matsudo[j][i], "ACA" )
                break
            
            
    
print(flag)