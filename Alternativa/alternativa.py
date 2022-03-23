


class Cristal:
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho
        self.superficie = alto * ancho
    
    def __init__(self):
        self.alto = 0
        self.ancho = 0
        self.superficie = 0

    def get_superficie(self):
        return self.superficie
    
    def get_ancho(self):
        return self.ancho

    def get_alto(self):
        return self.alto

    def set_alto(self, alto):
        self.alto = alto

    def set_ancho(self, ancho):
        self.ancho = ancho

class Ventana(Cristal):
    def __init__(self, medidas):
        self.medidas = medidas
        

class Pared(Cristal): pass




















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

