# obtener todas las llaves del diccionario
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
resultado = diccionario.keys()  # retoran un objeto del tipo dict_keys
print(resultado)
resultado = tuple(resultado)  # tambien se puede convertir a lista
print(resultado)

# para obtener los valores del diccionario
resultado = diccionario.values()  # retoran un objeto del tipo dict_values
print(resultado)
resultado = list(resultado)  # tambien se puede convertir a tupla
print(resultado)

# obtenet los items(clave: valor)
resultado = diccionario.items()
print(resultado)  # retoran un objeto del tipo dict_items
resultado = list(resultado)
print(resultado)  # aunque sea convertido a lista los items van a ser tuplas
