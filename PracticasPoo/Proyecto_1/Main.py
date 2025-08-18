from Servicio.auto_servicios import crear_auto
from Servicio.auto_servicios import mostrar_autos

from Servicio.camioneta_servicio import crear_camioneta
from Servicio.camioneta_servicio import mostrar_camioneta
if __name__ == "__main__":
    
   
    #chata = crear_camioneta()
    auto = crear_auto() 
    print (mostrar_camioneta(auto))
    
   