diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

print(len(diccionario))
print(diccionario)

# eliminar un elemento, forma 1
del diccionario['a']
print(len(diccionario))
print(diccionario)
# forma 2
diccionario.pop('b')
print(len(diccionario))
print(diccionario)
# igual que en las listas pop devuelve el valor eliminado
valor_eliminado = diccionario.pop('c')
print(valor_eliminado)
print(len(diccionario))
print(diccionario)

# aliminar todos los elementos
diccionario = {}
print(len(diccionario))
print(diccionario)

# otra forma
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}
diccionario.clear()
print(len(diccionario))
print(diccionario)
