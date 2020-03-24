# la varible global es accesible desde la funcion
animal = 'leon'


def mostrar_animal():
    print(animal)


mostrar_animal()

# aqui demostramos el namespace de la funcion
ave = 'pollo'


def mostrar_ave():
    # la funcion crea su propio namespace, los name spaces pueden existir
    # por lo que esta variable local ave es diferente a la variable global ave de arriba
    ave = 'aguila'
    print(ave)


mostrar_ave()
print(ave)


# para modificar una variable global dentro de una funcion
# usaremos global

insecto = 'hormiga'


def mostrar_insecto():
    global insecto
    insecto = 'cucaracha'
    print(insecto)


mostrar_insecto()
print(insecto)
