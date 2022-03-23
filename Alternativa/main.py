import alternativa

def obtener_medidas(tipo):
        print("alto de la " + str(tipo))
        alto = int(input())
        print("ancho de la " + str(tipo))
        ancho = int(input())
        return alto, ancho


if __name__ == "__main__":
    prot, opac = alternativa.proteccion()

    print("introduce la medida de la superficie de las ventanas")
    print("medidas de la ventana de la pared norte:")
    v_n_alto, v_n_ancho = obtener_medidas("ventana")
    print("medidas de la ventana de la pared sur:")
    v_s_alto, v_s_ancho = obtener_medidas("ventana")
    print("medidas de la ventana de la pared este:") 
    v_e_alto, v_e_ancho = obtener_medidas("ventana")
    print("medidas de la ventana de la pared oeste:")
    v_o_alto, v_o_ancho = obtener_medidas("ventana")


    ventana_n = alternativa.Ventana(v_n_alto, v_n_ancho)
    ventana_n.set_proteccion(prot)
    ventana_s = alternativa.Ventana(v_s_alto, v_s_ancho)
    ventana_s.set_proteccion(prot)
    ventana_e = alternativa.Ventana(v_e_alto, v_e_ancho)
    ventana_e.set_proteccion(prot)
    ventana_o = alternativa.Ventana(v_o_alto, v_o_ancho)
    ventana_o.set_proteccion(prot)

    print("Ventana norte:")
    print(ventana_n)
    print("Ventana sur:")
    print(ventana_s)
    print("Ventana este:")
    print(ventana_e)
    print("Ventana oeste:")
    print(ventana_o)

    print("introduce la medida de la superficie de las paredes")
    print("medidas de la pared norte:")
    p_n_alto, p_n_ancho = obtener_medidas("pared")
    print("medidas de la pared sur:")
    p_s_alto, p_s_ancho = obtener_medidas("pared")
    print("medidas de la pared este:") 
    p_e_alto, p_e_ancho = obtener_medidas("pared")
    print("medidas de la pared oeste:")
    p_o_alto, p_o_ancho = obtener_medidas("pared")

    pared_n = alternativa.Pared(p_n_alto, p_n_ancho)
    pared_n.set_opacidad(prot)
    pared_s = alternativa.Pared(p_s_alto, p_s_ancho)
    pared_s.set_opacidad(prot)
    pared_e = alternativa.Pared(p_e_alto, p_e_ancho)
    pared_e.set_opacidad(prot)
    pared_o = alternativa.Pared(p_o_alto, p_o_ancho)
    pared_o.set_opacidad(prot)

    print("Ventana norte:")
    print(ventana_n)
    print("Ventana sur:")
    print(ventana_s)
    print("Ventana este:")
    print(ventana_e)
    print("Ventana oeste:")
    print(ventana_o)

