numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    print(numero)

diccionario = {'a': 1, 'b': 2}
# al iterar un diccionario el valor que obtenemos es la llave
for llave in diccionario:
    print(llave)

valores = ((10, 20), ['string', 'strind'], (True, False))
for valor in valores:
    print(valor)

# de esta manera obtenenemos los valores de los iterables
for valor1, valor2 in valores:
    print(valor1, valor2)
