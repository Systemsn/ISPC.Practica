from Entidades.camioneta import Camioneta
list_camioneta = []
def crear_camioneta():
    while True:
        marca = input("Ingresa Marca:")
        modelo = input("Ingresa Modelo: ")
        color = input("Ingresa color: ")
        anio = input("Ingresa anio: ")
    
        camioneta = Camioneta(marca,modelo,color,anio)
        list_camioneta.append(camioneta)
        
        while True:
            pregunta = input("¿Desea Ingresar otra camioneta?").lower().strip()
            if pregunta == "no":
                return list_camioneta
            elif pregunta == "si":
                break
            else:
                print("Error Ingreso una opcion no valida")
                continue
    
def mostrar_camioneta(list_camioneta):
    resultado = ""
    for camioneta in list_camioneta:
        resultado += str(camioneta) + "\n"
    return resultado