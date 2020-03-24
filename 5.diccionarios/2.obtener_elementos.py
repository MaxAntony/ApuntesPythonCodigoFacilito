diccionario = {'a': 1, 'b': 2, 'c': 3, 'a': 4}
print(diccionario['a'])

# para saber si una llave existe en un diccionario
existe = 'z' in diccionario
print(existe)
existe = 'a' in diccionario
print(existe)

# otra forma de evitar el error,  metodo recomendado
print(diccionario.get('a'))
print(diccionario.get('z'))  # devuelve none por que no existe la llave
# valor pordefecto en caso la llave no exista
print(diccionario.get('z', 'La llave no existe'))
print(diccionario.get('z', {}))  # el valor por defecto puede ser cualquiera

# metodo setDefault
# si existe la llave retorna el valor, si no existe
# genera una nueva llave con el valor que pasa y devuelve el valor
# en caso z no existe le ponemos un diccionario vacio en su lugar y lo devolvemos
resultado = diccionario.setdefault('z', {})
print(diccionario)
print(resultado)
