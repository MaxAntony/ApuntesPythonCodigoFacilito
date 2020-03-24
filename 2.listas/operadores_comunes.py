lista = [8.17, 90, 1, 5, 44, 1.32]
print(lista)
# ordenar la lista de forma ascendente
lista.sort()
print(lista)

lista.reverse()
print(lista)
# obtener el mayor valor
print(lista[0])
print(max(lista))
# obtener el menor valor
print(lista[-1])
print(min(lista))

# longitud de lista
print(len(lista))

# buscar elementos en la lista
print(8 in lista)
print(8.17 in lista)

# obtener el indice de un valor
print(lista.index(8.17))

# saber cuantas veces se encuentra un elemento en la lista, si da 0 es que no se encuentra en la lista
print(lista.count(5))
