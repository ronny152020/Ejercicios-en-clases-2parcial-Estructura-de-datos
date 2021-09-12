import os
class matriz:
    def __init__(self,numfilas,numcol):
        self.matriz=[]
        self.filas=numfilas
        self.col=numcol
        
    def ingresar(self):
        self.matriz=[]
        for fila in range(self.filas):
            columna=[]
            for col in range(self.col):
                dato=int(input("FILA [{}] COLUMNA [{}]--> ".format(fila,col)))
                os.system("cls")
                columna.append(dato)
            self.matriz.append(columna)
    
    def mostrar(self):
        print("-------------------------")
        for fila in range(0,len(self.matriz)):
            for col in range(len(self.matriz[fila])):
                print("[{}]".format(self.matriz[fila][col]),end=" ")
            print()
            
    def sumarmatriz(self,matriz2):
        matrizsuma=[]
        for fila in range(self.filas):
            columna=[]
            for col in range(self.col):
                res=self.matriz[fila][col]+matriz2[fila][col]
                columna.append(res)
            matrizsuma.append(columna)
        return matrizsuma
        
    
matde=matriz(3,3)
matde.ingresar()
matde.mostrar()
matde2=matriz(3,3)
matde2.ingresar()
matde2.mostrar()
matde2.matriz=matde.sumarmatriz(matde2.matriz)
matde2.mostrar()