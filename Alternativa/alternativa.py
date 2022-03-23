class Cristal:
    def __init__(self, medidas):
        self.medidas = medidas
        medidas = []


#funcion que mira la proteccion que quiere en las ventanas
def proteccion():
    print("¿Le gutaria tener proteccion en las ventanas? s/n")
    respuesta = input()
    if respuesta == "s":
        print("¿Cual es?")
        opciones = ["persiana", "estor", "cortinas", "mosquitera"]
        print(opciones)
        cual_es = input()
        if cual_es not in opciones:
            print("tiene que ser una opcion de la lista")
            proteccion()
        else:
            print("gracias. Siguiente paso")
    else:
        raise Exception("No se ha escogido ninguna proteccion")