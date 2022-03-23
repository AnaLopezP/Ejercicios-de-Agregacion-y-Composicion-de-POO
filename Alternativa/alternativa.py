


class Cristal:
    
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho
        self.superficie = int(self.alto) * int(self.ancho)

    def get_superficie(self):
        return self.alto*self.ancho
        #return self.superficie

    def get_ancho(self):
        return self.ancho

    def get_alto(self):
        return self.alto

    def set_alto(self, alto):
        self.alto = alto
        self.superficie = self.alto * self.ancho

    def set_ancho(self, ancho):
        self.ancho = ancho
        self.superficie = self.alto * self.ancho
    
    def __str__(self):
        cadena = "ancho = " + str(self.ancho) + " alto = " + str(self.alto) + " superficie = " + str(self.superficie)
        return cadena

class Ventana(Cristal):
    def __init_subclass__(self, alto, ancho):
        super().__init_subclass__(self, alto, ancho)
        
    def get_proteccion(self):
        return self.proteccion
    
        
    def set_proteccion(self, proteccion):
        self.proteccion = proteccion

    def __str__(self) -> str:
        cadena = super().__str__()  + " proteccion = " + str(self.proteccion)
        return cadena

class Pared(Cristal): 
    def __init_subclass__():
        return super().__init_subclass__()

    def get_opacidad(self):
        return self.opacidad
    
    def set_opacidad(self, opacidad):
        self.opacidad = opacidad
    
    def __str__(self) -> str:
        cadena = super().__str__() + " opacidad = " + str(self.opacidad)
        return cadena



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
    print("Eliga la opacidad de la pared")
    opciones = ["opaco", "translucido", "transparente"]
    print(opciones)
    cual_es_p = input()

    return cual_es, cual_es_p

