for valor in range(10):
    # se empieza a contar desde 0 po default
    print(valor)

for valor in range(1, 10):
    # el 10 no se tomara en cuenta, por que es 'hasta' 10
    print(valor)

for valor in range(-10, 11):
    # el 10 no se tomara en cuenta, por que es 'hasta' 10
    print(valor)

for valor in range(1, 51, 2):
    # imprimimos los numeros impares del 1 al 100 por que salta de 2 en 2
    print(valor)

lista = [1, 2, 3, 4, 5, 6]
for indice in range(len(lista)):
    print('indice ', indice, 'valor ', lista[indice])

# el enumerate da indice y valor de la lista a iterar
for indice, valor in enumerate(lista):
    print('indice ', indice, 'valor ', valor)

# indicar punto de partida el indice
for indice, valor in enumerate(lista, 10):
    print('indice ', indice, 'valor ', valor)
