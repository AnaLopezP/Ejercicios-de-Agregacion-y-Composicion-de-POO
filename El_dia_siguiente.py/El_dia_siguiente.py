
class CIUDAD:
    def __init__(self, nombre, list_edificios):
        self.nombre = nombre
        self.list_edificios = list_edificios

class EDIFICIO:
    def __init__(self, nombre_ciudad):
        self.nombre_ciudad = nombre_ciudad


class EMPRESA:
    def __init__(self, nombre, list_empleados, list_edificios):
        self.nombre = nombre
        self.list_empleados = list_empleados
        self.list_edificios = list_edificios

'''edificaciones = EDIFICIO()
los_angeles = CIUDAD("Los Angeles")
nueva_y = CIUDAD("Nueva York")
trabajo = EMPRESA()
class destrucc_NY(EMPRESA):
    def __init__(self, NY, LA, A, B, C, martin, salim, xing):
        super().__init__(NY, LA, A, B, C, martin, salim, xing)

    def __del__(self):
        ciudades.remove(self.NY)
        edificaciones.remove(self.A, self.B)'''