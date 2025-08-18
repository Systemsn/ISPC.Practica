from Entidad.dado_entidad import Dado


if __name__ =="__main__":

    tirar = int(input("Ingrese las cantidad de caras del dado: "))
    lanzar = Dado(tirar)
    lanzar.lanzar()
    print(lanzar.lanzar())
 