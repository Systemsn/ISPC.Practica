import random 
class Dado:
    def __init__(self,__cara_cantidad):
        self.__cara_cantidad = __cara_cantidad
    #Getter and Setter
    @property
    def cara_cantidad(self):
        return self.__cara_cantidad

    @cara_cantidad.setter
    def cara_cantidad(self,valor):
        self.__cara_cantidad = valor

    #Metodos 
    def lanzar(self):
        aleatorio = random.randint(1,self.__cara_cantidad)
        return f"El resultado {aleatorio}"
    
    
    
        