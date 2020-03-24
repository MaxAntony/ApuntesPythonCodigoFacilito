# tipo especial de funcion para la generacion de datos

# funcion que retorna tabla de multiplicar de un numero


def tabla_multiplicar(numero, maximo=10):
    for posicion in range(1, maximo+1):
        yield numero * posicion


# yield retorna el resultado de la multiplicacion sin terminar la funcion, en cada iteracion la funcion retorna un valor
for resultado in tabla_multiplicar(9):
    print(resultado)


# y tambien como el return podemos devolver  multiples valores
def tabla_multiplicar(numero, maximo=10):
    for posicion in range(1, maximo+1):
        yield numero * posicion, numero, posicion


for resultado, numero, posicion in tabla_multiplicar(9):
    print(numero, '*', posicion, '=', resultado)
