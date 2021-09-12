class matriz:
    def __init__(self,matriz):
        self.matriz=matriz
        
    def mostrar(self):
        for fila in range(0,len(self.matriz)):
            #print(fila,end=" ")
            for col in range(len(self.matriz[fila])):
                print(self.matriz[fila][col],end=" ")
            print()
      
valores=[[2,4,6,8],[3,6,9,12],[4,8,12,16],[5,10,15,20]]
math=matriz(valores)
math.mostrar()