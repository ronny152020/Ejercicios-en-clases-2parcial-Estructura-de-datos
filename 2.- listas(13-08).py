class lista:
    def __init__(self,dimension):
        self.lista=[]
        self.stop=0
        self.dimension=dimension
        
    def append(self,valor):
        if self.stop<self.dimension:
            self.lista+=[valor]
            self.stop+=1
            print("Agregado con exito")
        else:
            print("La lista esta llena")
            
    def obtener(self,pos):
        if pos<0 or self.stop==0:
            print("La posicion es invalida o la lista esta vacia por lo cual no se puede obtener nigun valor")
            return None
        elif pos>=self.stop:
            print("la posicion no existe porque es mayor que la longitud")
            return None
        elif pos>=0 and pos<self.stop:
            valor=self.lista[pos]
            listanew=self.lista[0:pos]
            for dato in range(pos,self.stop-1):
                listanew=listanew+[self.lista[dato+1]]
            self.stop-=1
            self.lista=listanew
            print("eliminado con exito")
            return valor
    
    def mostrar(self,alternativa):
        if self.stop==0:
            print("No hay nada que mostrar porque la lista esta vacia")
        else:
            if alternativa.lower()=="asc":
                print("Se va a presentar de forma ascendente")
                for ele in range(0,self.stop):
                    print("[{}]".format(self.lista[ele]))
            else:
                print("Se va a presentar de forma descendente")
                for ele in range(self.stop-1,-1,-1):
                    print("[{}]".format(self.lista[ele]))
                    
usolista = lista(5)
usolista.append(10)
usolista.append(20)
usolista.append(30)
usolista.append(40)
print("De la posicion dada se obtuvo el elemento: {}".format(usolista.obtener(2)))
usolista.mostrar("asc")
usolista.mostrar("dsc")
