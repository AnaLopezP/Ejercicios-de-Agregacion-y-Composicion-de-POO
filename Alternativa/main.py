import alternativa

if __name__ == "__main__":
    print("¿Que superficie quiere para las ventanas?")
    print("Ventana norte:")
    v_n = alternativa.Cristal(input())
    print("Ventana sur:")
    v_s = alternativa.Cristal(input())
    print("Ventana este:")
    v_e = alternativa.Cristal(input())
    print("Ventana oeste:")
    v_o = alternativa.Cristal(input())
    print("¿Que superficie quiere para las paredes?")
    print("Pared norte:")
    p_n = alternativa.Cristal(input())
    print("Pared sur:")
    p_s = alternativa.Cristal(input())
    print("Pared este:")
    p_e = alternativa.Cristal(input())
    print("Pared oeste:")
    p_o = alternativa.Cristal(input())
    alternativa.Cristal.medidas.apeend(v_n, v_s, v_e, v_o, p_n, p_s, p_e, p_o)

