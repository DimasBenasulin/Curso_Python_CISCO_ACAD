counter = 0
c0= int(input("Ingrese un número entero:  "))
while c0 != 1:
    if c0 % 2 ==0:
        c0 = c0 // 2
        print(c0)
        counter += 1
        continue
    elif c0 % 2 ==1:
        c0 = 3 * c0 +1
        print (c0)
        counter += 1
        continue
print ("pasos:  ", counter)
