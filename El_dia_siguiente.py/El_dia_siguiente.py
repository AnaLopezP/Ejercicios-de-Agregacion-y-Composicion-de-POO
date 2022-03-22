
class Ciudad:
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.edificios = []

    def add_edif(self, edif):
        self.edificios.append(edif)
    
    def get_edifs(self):
        return self.edificios
    def __del__(self):
        self.nombre = ""
        self.edificios = []

class Edificio:
    nombre = ""
    def __init__(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre


class Empresa:
    def __init__(self, nombre, list_empleados, list_edificios):
        self.nombre = nombre
        self.list_empleados = list_empleados
        self.list_edificios = list_edificios

class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre

    
martin = Empleado("Martin")
salim = Empleado("Salim") 
xing = Empleado("Xing")
edif_a = Edificio("A")
edif_b = Edificio("B")
edif_c = Edificio("C")
list_edificios = [edif_a, edif_b, edif_c]
list_empleados = [martin, salim, xing]
yoohoo = Empresa("Yoohoo!", list_empleados, list_edificios)
ny = Ciudad("Nueva York")
la = Ciudad("Los Angeles")
ny.add_edif(edif_a)
ny.add_edif(edif_b)
la.add_edif(edif_c)

print("Estas son las ciudades que hay:")
print(ny.nombre)
print(la.nombre)
print("Este es el nombre de la empresa:")
print(yoohoo.nombre)
print("Los edificios que tiene a su propiedad:")
print(yoohoo.list_edificios.pop().get_nombre())
print(yoohoo.list_edificios.pop().get_nombre())
print(yoohoo.list_edificios.pop().get_nombre())
print("Estos son los empleados que trabajan en esta empresa:")
print(yoohoo.list_empleados.pop().nombre)
print(yoohoo.list_empleados.pop().nombre)
print(yoohoo.list_empleados.pop().nombre)
print("Estos son los edificios que hay en Nueva York pertenecientes a Yoohoo!:")
print(ny.edificios.pop().get_nombre())
print(ny.edificios.pop().get_nombre())
print("Estos son los edificios que hay en Los Angeles pertenecientes a Yoohoo!:")
print(la.edificios.pop().get_nombre())


print("¿Quiere destruir Nueva York?  s/n")
respuesta = input()
if respuesta == "s":
    ny.__del__()
    if len(ny.nombre) == 0:
        print("Ciudades de Nueva York restantes: " + str(len(ny.nombre)))
        print("La ciudad de Nueva York ya no existe, ha sido destruida")
    else:
        print("Ha habido un error al pulsar el boton rojo. No se ha podido destruir.")
    if len(ny.edificios) == 0:
        print("Edificios de Yoohoo restantes: " + str(len(ny.edificios)))
        print("Los edificios de Nueva York han sido destruidos")
    else:
        print("Ha habido un error al pulsar el boton rojo. No se ha podido destruir.")
elif respuesta == "n":
    print("De acuerdo.")
else:
    print("Esa no es una opcion valida")

