class Camioneta:
    def __init__(self,marca,modelo,color,anio):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__anio = anio

    @property
    def marca(self):
        return self.__marca
    
    @marca.setter 
    def marca(self,valor):
        self.__marca = valor

    @property
    def modelo(self):
        return self.__modelo
    
    @modelo.setter
    def modelo(self,valor):
        self.__modelo = valor
    
    @property
    def color(self):
        return self.__color
    @color.setter
    def color(self,valor):
        self.__color = valor
    
    @property
    def anio(self):
        return self.__anio
    @anio.setter
    def anio(self,valor):
        self.__anio=valor
        
    def __str__(self):
        return f"La caracteristica de la camioneta: {self.__marca}, {self.__modelo}, {self.__color}, {self.__anio}"