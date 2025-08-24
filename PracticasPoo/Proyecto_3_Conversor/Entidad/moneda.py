class Moneda: 
    def __init__(self,dolar,peso,dinero):
        self.__dolar =dolar
        self.__peso = peso
        
    
    @property
    def dolar(self):
        return self.dolar
    
    @dolar.setter
    def dolar(self,valor):
        self.__dolar= valor
    
    @property
    def peso(self):
        return self.peso
    
    @peso.setter
    def peso(self,valor):
        self.__peso = valor
    
    
        
    # metodo
    def convertir(self):
        
        print("1- dolar a peso")
        print("2- peso a dolar")
        opcion = input("Ingrese una opcion: ")
        
        opcion_entero = int(opcion)
        if opcion_entero.isdigit():
            match(opcion_entero):
                case 1:
                    dinero = int(input("Ingresa el dinero para convertir: "))
                    convertir = dinero *self.dolar
                    return convertir
                case 2: 
                    convertir = d 
                    
            
    
    def __str__(self):
        return f"Candidad convertida en pesos : { self.__dolar}. Cantidad convertida en dolar { }"
    
    
    