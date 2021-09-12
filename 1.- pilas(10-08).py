class pila:
    def __init__(self,cantidadele):
        self.__pila=[]
        self.__limit=0
        self.limite=cantidadele
        
    def empty(self):
        if self.__limit==0:
            return True
        else:
            return False
        
    def push(self,valor):
        if self.__limit<self.limite:
            self.__pila+=[valor]
            self.__limit+=1
            print("Se ha agregado el elemento con exito")
        else:
            print("La Pila ya se encuentra llena")
            
    def pop(self):
        if self.__limit==0:
            print("No se puede eliminar ningun elemento, debido a que la Pila se encuentra esta vacia")
        else:
            self.__pila=self.__pila[:-1]
            self.__limit-=1
            print("Se ha eliminado con exito el último elemento de la Pila")
    
    def show(self):
        if self.__limit>0:
            for datos in range(self.__limit-1,-1,-1):
                print("[{}]".format(self.__pila[datos]))
        else:
            print("No hay elementos que presentar, porque la Pila se encuentra vacía")
            
    def longitud(self):
        return self.__limit
    
trapila = pila(6)
trapila.push(8)
trapila.push(10)
print("tamaño: {} elementos de {}".format(trapila.longitud(),trapila.limite))
trapila.pop()
trapila.show()
trapila.pop()
trapila.show()
trapila.pop()
trapila.show()
trapila.push(50)
trapila.push(25)
trapila.show()
trapila.pop()