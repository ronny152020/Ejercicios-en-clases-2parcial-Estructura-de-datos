class matriz:
    def __init__(self,matriz):
        self.matriz=matriz
        
    def mostrar(self):
        for fila in range(0,len(self.matriz)):
            #print(fila,end=" ")
            for col in range(len(self.matriz[fila])):
                print(self.matriz[fila][col],end=" ")
            print()
            
    def buscafor(self,buscado):
        resp={}
        for fila in range(0,len(self.matriz)):
            for col in range(len(self.matriz[fila])):
                if self.matriz[fila][col]==buscado:
                    resp["fila"]=fila
                    resp["columna"]=col
                    break
            if resp:break
        return resp
    
    def buscawhile(self,buscado):
        resp={}
        fila=0
        enc=False
        while fila<len(self.matriz)and enc==False:
            col=0
            while col<len(self.matriz[fila]) and enc==False:
                if self.matriz[fila][col]==buscado:
                    resp["fila"]=fila
                    resp["columna"]=col
                    enc=True
                else:col+=1
            fila+=1
        return resp
    
valores=[[2,4,6,8],[12,14,16,18],[24,28,32,36],[45,50,55,60]]
usomat=matriz(valores)
respuesta=usomat.buscafor(32)
if respuesta:
    print(respuesta)
else:
    print("El valor no se encuentra en la matriz")
    
solu=usomat.buscawhile(45)
if solu:
    print(solu)
else:
    print("No se encuentra el valor en la matriz")