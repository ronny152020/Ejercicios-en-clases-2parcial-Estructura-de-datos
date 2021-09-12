class busqueda:
    def __init__(self,lista):
        self.__lista=lista
        
    @property
    def lista(self):
        if self.__lista!=None:
            return self.__lista
        else:
            print("La lista esta vacía")
            
    def busquedalineal(self,buscado):
        dis=len(self.__lista)
        enc=False
        pos=0
        while pos<dis and enc==False:
            if self.__lista[pos]["nombre"]==buscado:
                enc=True
            else:
                pos+=1
        if enc:
            return pos
        else:
            return -1
    
    def ordenar(self,orden):
        if orden.lower()=="asc":
            for pos in range (0,len(self.__lista)):
                for sig in range (pos+1,len(self.__lista)):
                    if self.__lista[pos]["nombre"]>self.__lista[sig]["nombre"]:
                        aux=self.__lista[pos]
                        self.__lista[pos]=self.lista[sig]
                        self.__lista[sig]=aux
        else:
            for pos in range (0,len(self.__lista)):
                for sig in range (pos+1,len(self.__lista)):
                    if self.__lista[pos]["nombre"]<self.__lista[sig]["nombre"]:
                        aux=self.__lista[pos]
                        self.__lista[pos]=self.lista[sig]
                        self.__lista[sig]=aux
        
datos=[
    {"nombre":"Jorge","n1":"25","n2":"30"},
    {"nombre":"Rodrigo","n1":"28","n2":"20"},
    {"nombre":"Matias","n1":"35","n2":"30"},
    {"nombre":"Andres","n1":"25","n2":"50"},
    {"nombre":"Nicole","n1":"40","n2":"60"},
    {"nombre":"Sheyla","n1":"19","n2":"32"}
]        
search1=busqueda(datos)
print(search1.busquedalineal("Andres"))
# print("search1",search1.lista)
# search2=busqueda(["Jose","Gonzales","Pedro"])
# print("search2",search2.lista)
orden=str(input("De que forma desea ordenar los datos (asc/dsc): "))
search1.ordenar(orden)
print(search1.lista)
