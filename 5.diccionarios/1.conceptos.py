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
