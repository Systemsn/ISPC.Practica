from Entidad.dado_entidad import Dado
from Servicio.dado_servicio import Dado_Servicio 

if __name__ =="__main__":
    lados = int(input("Ingrese la cantidad de lados del dado: "))
    dado_rojo = Dado(lados)
    
    servicio = Dado_Servicio()
    print(f"Dado Lanzado... \n La cara que salio es : {servicio.lanzar(dado_rojo)}")