def mi_funcion():
    print('un mensaje')


mi_funcion()
# si no devuelva nada, por default devuelve none
resultado = mi_funcion()
print(resultado)


# si ponemos return, la funcion termina ahi
def mi_funcion2():
    print('un mensaje')
    return 2
    print('una linea que no se ejecutara')


print(mi_funcion2())


def mi_funcion3(parametro):
    if parametro == 0:
        return 100
    print('esto se ejecutara si el parametro es difernte de cero')
    return 1


print(mi_funcion3(0))
