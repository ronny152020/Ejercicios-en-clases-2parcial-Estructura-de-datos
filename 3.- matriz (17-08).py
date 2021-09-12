
lista=[[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
acu=0
for fila in range(0,len(lista)):
    print(fila,end=" ")
    for col in range(0,len(lista[fila])):
        print("[{}]".format(lista[fila][col]),end="")
        acu=acu+lista[fila][col]
    print()
print("La suma de toda la matriz es: ",acu)