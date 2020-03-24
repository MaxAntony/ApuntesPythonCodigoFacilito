# la funcion map nos permite aplicar una funcion sobre los items de un objeto iterable
# syntax
# map(function, objeto_iterable)

# la funcion retorna un objeto map que podemos convertie a lista o tupla


def cuadrado(numero):
    return numero * numero


lista = [1, 2, 3, 4, 5, 6]
resultado = map(cuadrado, lista)
print(resultado)

lista_resultado = list(resultado)
print(lista_resultado)

# es posible utilizar map junto con una funcion lambda, se considera la mejor opcion
resultado = map(lambda numero: numero * numero, lista)
lista_resultado = list(resultado)
print(lista_resultado)
