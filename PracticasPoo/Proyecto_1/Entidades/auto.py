class Auto:
    def __init__(self,marca,modelo,color,anio):
        self._marca = marca
        self._modelo = modelo
        self._color = color
        self._anio = anio
   
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self,valor):
        self._marca = valor
    
    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self,valor):
        self._modelo = valor
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self,valor):
        self._color = valor
    
    @property
    def anio(self):
        return self._anio
    
    @anio.setter
    def anio(self,valor):
        self._anio = valor
    
    def __str__(self):
        return f"Caracteristica del Auto : {self.marca}, {self.modelo}, {self.color}, {self.anio}"

