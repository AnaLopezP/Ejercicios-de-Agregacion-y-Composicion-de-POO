


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
    def __init_subclass__():
        return super().__init_subclass__()

    def get_estado(self):
        return self.estado
    
    def set_estado(self, estado):
        self.estado = estado
        

class Pared(Cristal): 
    def __init_subclass__():
        return super().__init_subclass__()

    def get_opacidad(self):
        return self.opacidad
    
    def set_estado(self, opacidad):
        self.opacidad = opacidad



















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

