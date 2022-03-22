import El_dia_siguiente

if __name__ == "__main__":
    print("Estas son las ciudades que hay:")
    print(El_dia_siguiente.ny.nombre)
    print(El_dia_siguiente.la.nombre)
    print("Este es el nombre de la empresa:")
    print(El_dia_siguiente.yoohoo.nombre)
    print("Los edificios que tiene a su propiedad:")
    print(El_dia_siguiente.yoohoo.list_edificios.pop().get_nombre())
    print(El_dia_siguiente.yoohoo.list_edificios.pop().get_nombre())
    print(El_dia_siguiente.yoohoo.list_edificios.pop().get_nombre())
    print("Estos son los empleados que trabajan en esta empresa:")
    print(El_dia_siguiente.yoohoo.list_empleados.pop().nombre)
    print(El_dia_siguiente.yoohoo.list_empleados.pop().nombre)
    print(El_dia_siguiente.yoohoo.list_empleados.pop().nombre)
    print("Estos son los edificios que hay en Nueva York pertenecientes a Yoohoo!:")
    print(El_dia_siguiente.ny.edificios.pop().get_nombre())
    print(El_dia_siguiente.ny.edificios.pop().get_nombre())
    print("Estos son los edificios que hay en Los Angeles pertenecientes a Yoohoo!:")
    print(El_dia_siguiente.la.edificios.pop().get_nombre())


    print("¿Quiere destruir Nueva York?  s/n")
    respuesta = input()
    if respuesta == "s":
        El_dia_siguiente.ny.__del__()
        if len(El_dia_siguiente.ny.nombre) == 0:
            print("Ciudades de Nueva York restantes: " + str(len(El_dia_siguiente.ny.nombre)))
            print("La ciudad de Nueva York ya no existe, ha sido destruida")
        else:
            print("Ha habido un error al pulsar el boton rojo. No se ha podido destruir.")
        if len(El_dia_siguiente.ny.edificios) == 0:
            print("Edificios de Yoohoo restantes: " + str(len(El_dia_siguiente.ny.edificios)))
            print("Los edificios de Nueva York han sido destruidos")
        else:
            print("Ha habido un error al pulsar el boton rojo. No se ha podido destruir.")
    elif respuesta == "n":
        print("De acuerdo.")
    else:
        print("Esa no es una opcion valida")