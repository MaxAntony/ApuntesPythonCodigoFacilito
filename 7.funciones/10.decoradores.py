# en caso necesitemos modificar una funcion existente sin cambiar sus lineas de codigo
# comunmente para agregar mayor funcionalidad
# para usar un decorador necesitamos por lo menos 3 funciones
# a,b,c donde a recibe como parametro b para dar como salida c
# a(b) -> c


# funcion a
def decorador(funcion):
    # esta palabra reservada la vamos a poder usar tanto en condicionales, ciclos y funciones
    # y permite especificar que nuestra condicional, ciclo o funcion no va a realizar
    # por el momento nada
    def nueva_funcion(*args, **kwargs):
        print('podemos agregar codigo antes')
        resultado = funcion(*args, *kwargs)
        print('podemos agregar codigo despues')
        return resultado

    return nueva_funcion


# funcion b


@decorador
def funcion_a_decorar():
    print('esta es una funcion a decorar')

# tambien decoramos una funcion que puede recibie n numero de parametros
@decorador
def suma(val1, val2):
    return val1 + val2


funcion_a_decorar()

print('\n')

resultado = suma(10, 20)
print(resultado)
