#si quitamos el yin.yang = yang (asi como el print(yin.yang is yang) para que no de error), el mensaje aparece antes de la interrogacion.
#esto ocurre porque al hacer esa asignacion creamos dos variables apuntando al mismo objeto.
#entonces, al destruirlo, destruye una de las dos variables, pero no el objeto, que se destruye automaticamente al final de la ejecucion.
#otra manera de evitar esto es llamando al destructor con las dos variables antes de la interrogacion.