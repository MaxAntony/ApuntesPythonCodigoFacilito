# podemos pasar n cantidad de parametros, se agruparan en una tupla


def suma(*args):
    print(args)
    total = 0
    for valor in args:
        total += valor
    return total


print(suma(3, 4, 5, 6, 7,))

# si van a haber multiples parametros poner el asterisco al final
# la convencion es que el paramtro con * sea args


def suma2(paramtro_requerido, *args):
    print(args)
    print(paramtro_requerido)
    total = 0
    for valor in args:
        total += valor
    return total


suma2('este es un argumento requerido', 4, 5, 6, 7, 8)


# para agruparlos en en diccionario, con argumentos con nombre


def usuarios_autenticados(**kwargs):
    print(kwargs)


usuarios_autenticados(codi=True, facilito=False)


def combinacion(valor_requerido, *args, **kwargs):
    print(valor_requerido)
    print(args)
    print(kwargs)


combinacion('argumento requerido', 10, 20, 30, valor_uno=True, valor_dos=False)
