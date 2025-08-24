import random 
class Dado:
    def __init__(self,cara_cantidad):
        self.__cara_cantidad = cara_cantidad
    #Getter and Setter
    @property
    def cara_cantidad(self):
        return self.__cara_cantidad

    @cara_cantidad.setter
    def cara_cantidad(self,valor):
        self.__cara_cantidad = valor

    
    
    
        