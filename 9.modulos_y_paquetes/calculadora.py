def suma(val1, val2):
    return val1+val2


def resta(val1, val2):
    return val1-val2


def multiplicacion(val1, val2):
    return val1*val2


def division(val1, val2):
    return val1/val2


# aqui main significa que este es el archivo pricipal
print(__name__)

if __name__ == '__main__':
    print('soy un mensaje de calculadora')
else:
    print('estoy siendo usado como modulo')
