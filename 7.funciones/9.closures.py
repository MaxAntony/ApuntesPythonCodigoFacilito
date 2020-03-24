# esta funcion es un closure, se llaman closure cuando una funcion genere dinamicamente una funcion
# y que esta nueva funcion pueda acceder a las variables locales aun cuando la primera haya finalizado


def mostrar_mensaje(mensaje):
    # esta variable local es utilizada hasta la lina 14, cuando mostrar mensaje ya a sido ejecutado
    mensaje = mensaje.title()  # local

    def mostrar():
        print(mensaje)
    return mostrar


nueva_funcion = mostrar_mensaje('hola max')
# el uso de closures es util en programas de alto nivel por que nos permitira evitar usar variables globales
# y proporcionara consistencia en nuestros datos debido a que las variables locales no pueden
# ser modificadas fuera de la funcion
nueva_funcion()
