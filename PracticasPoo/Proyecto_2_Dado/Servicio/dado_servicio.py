from Entidad.dado_entidad import Dado
import random

class Dado_Servicio():
    
    def lanzar(sef,dado:Dado)->int:
        
        return random.randint(1,dado.cara_cantidad)