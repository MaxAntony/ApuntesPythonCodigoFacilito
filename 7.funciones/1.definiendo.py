def crear_mensaje(nombre):
    return 'hola {}, bienvenido al curso'.format(nombre)


# si dejamos sin argumentos dara un error
nuevo_mensaje = crear_mensaje('max')
print(nuevo_mensaje)


def suma(val1, val2, val3):
    return val1+val2+val3


print(suma(10, 20, 30))

# retornando multiples valores


def obtener_curso():
    return 'curso de python', 'basico', 3.6


print(obtener_curso())
curso, nivel, version = obtener_curso()
print(curso, nivel, version)
