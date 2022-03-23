import alternativa

if __name__ == "__main__":
    print("¿Que superficie quiere para las ventanas?")
    print("Ventana norte:")
    v_n = input()
    print("Ventana sur:")
    v_s = input()
    print("Ventana este:")
    v_e = input()
    print("Ventana oeste:")
    v_o = input()
    print("¿Que superficie quiere para las paredes?")
    print("Pared norte:")
    p_n = input()
    print("Pared sur:")
    p_s = input()
    print("Pared este:")
    p_e = input()
    print("Pared oeste:")
    p_o = input()
    alternativa.Cristal.medidas.apeend(v_n, v_s, v_e, v_o, p_n, p_s, p_e, p_o)

    