# desde python 3.5 se pueden usar annottations
# def saludo(nombre):
#     print('hola '+nombre)


# nombre = 'max'
# saludo(nombre)

# indicamos el tipo de dato que espera el parametro y el tipo de la funcion
# como no retorna nada es None
def saludo(nombre: str) -> None:
    print('hola '+nombre)


nombre = 'max'
saludo(nombre)


# con valor por default
# los parametros que tiene valores por default van al final

def suma(num1: int, num2: int = 100) -> int:
    return num1+num2


print(suma(1, 4))
# son anotaciones no son reglas son guias osea que aunque este int puedes pasar un string
