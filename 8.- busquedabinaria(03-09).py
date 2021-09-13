class busquedabi:
    def __init__(self,lista):
        self.__lista=lista
        
    @property
    def lista(self):
        if self.__lista!=None:
            return self.__lista
        else:
            print("La lista esta vacía")
        
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
        
    def busquedabinaria(self,buscar):
        self.ordenar("asc")
        ultima=len(self.__lista)-1
        primero=0
        enc=False
        while primero <=ultima and enc==False:
            medio=(primero+ultima)//2
            if self.__lista[medio]["nombre"]==buscar:
                enc=True
            elif self.__lista[medio]["nombre"]<buscar:
                primero=medio+1
            else:
                ultima=medio-1
        if enc:
            return medio
        else:
            return -1
        

elementos=[
    {"nombre":"Jorge","n1":"25","n2":"30"},
    {"nombre":"Rodrigo","n1":"28","n2":"20"},
    {"nombre":"Matias","n1":"35","n2":"30"},
    {"nombre":"Andres","n1":"25","n2":"50"},
    {"nombre":"Nicole","n1":"40","n2":"60"},
    {"nombre":"Sheyla","n1":"19","n2":"32"}
]            

buscar1=busquedabi(elementos)
print(buscar1.busquedabinaria("Andres"))
            