from Entidades.auto import Auto


list_auto = []
def crear_auto():
    while True: 
        print("Cargar nuevo auto:")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        color = input("Color: ")
        anio = input("Año: ")

        auto = Auto(marca, modelo, color, anio)
        
        list_auto.append(auto)
        while True:
            pregunta = input("Desea Ingresar otro auto? si o no ").lower().strip()
            if pregunta == "no":
                return list_auto
            elif pregunta == "si" :
                break
            else:
                print("Error Ingreso una opcion invalida")
                continue

def mostrar_autos():

    for auto in list_auto:
        print(auto)
    