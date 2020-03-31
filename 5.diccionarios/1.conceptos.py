# los diccionarios son mutables, y sus llaves pueden ser de cualquier tipo incluido otro diccionario
diccionario = {}
diccionario['nombre'] = 'max'  # agregamos una llave con su valor
valor = diccionario['nombre']  # obtenemos el valor
print(diccionario)
print(valor)
diccionario['nombre'] = 90
print(diccionario)

# print(diccionario['apellido']) # dara error por que no existe esa llave
diccionario = {'a': 1, 'b': 2, 'c': 3, 'a': 4}
# aqui vemos que no puede haber 2 llaves iguales, si son iguales se asigna el ultimo valor
print(diccionario)

# al parecer los diccionarios tienen la misma caracteristica de los objetos en js
# por que no se pasan por valor sino por referencia, y tambien los demas objetos
# Tradicionalmente:
# Los tipos simples se pasan por valor: Enteros, flotantes, cadenas, lógicos...
# Los tipos compuestos se pasan por referencia: Listas, diccionarios, conjuntos...
# https://docs.hektorprofe.net/python/programacion-de-funciones/paso-por-valor-y-referencia/

dic1 = {'1': 1, '2': 2}
dic2 = dic1
print(dic1)
print(dic2)

dic2['1'] = 3
print(dic1)
print(dic2)
