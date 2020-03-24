def comenzar_play_list(lista):
    def reproducir():
        for val in lista:
            print(val)
    # la funcion reproducir solo puede ser llamada desde la funcion comenzar_play_list por su scope
    reproducir()
    print(lista)


lista = ['track1', 'track2', 'track3']
comenzar_play_list(lista)


# ejemplo del namespace de la funciones


def comenzar_play_list(lista):
    def reproducir():
        # tal como en la seccion de variables globales y locales, cada funcion tiene su propio namespace
        # es por eso que estas variables ya son diferentes
        lista = [1, 2, 3]
        for val in lista:
            print(val)
    # la funcion reproducir solo puede ser llamada desde la funcion comenzar_play_list
    reproducir()
    print(lista)


lista = ['track1', 'track2', 'track3']
comenzar_play_list(lista)


# modificar la variable local de comenzar_play_list desde reproducir
# para esto usaremos nonlocal
def comenzar_play_list(lista):
    def reproducir():
        # accedemos a la variable superior
        nonlocal lista
        lista = [1, 2, 3]
        for val in lista:
            print(val)
    # la funcion reproducir solo puede ser llamada desde la funcion comenzar_play_list
    reproducir()
    print(lista)


lista = ['track1', 'track2', 'track3']
comenzar_play_list(lista)
