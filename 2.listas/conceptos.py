# las listaS en python son una estructura

lista = [False, 1, 'hola', [True, 19.4,
                            'otra lista dentro'], 'c#', 5, 'java', 'lua']
print(lista[0])
print(lista[-1])
print(lista[-1][-1])
print(lista[-2])
# print(lista[10]) # error

# obtenemos una nueva lista, desde el primero hasta el segundo
sublista = lista[0:2]
# el indice 2 que seria la tercera posicion no aparece por que solo hasta ahi llega
# el primer valor siempre sera desde y el segundo sera hasta
print(sublista)
# si se comienza desde el primer elemento se puede omitir 0
sublista = lista[:3]
print(sublista)

# aqui decimos que desde el indice 2 hasta el final
sublista = lista[2:]
print(sublista)

# decimos que desde el 1 hasta el indice 7 saltando de 2 en 2
sublista = lista[1:7:2]
print(sublista)
# hasta el final
sublista = lista[1::2]
print(sublista)

# obtener la liste invertida
sublista = lista[::-1]
print(sublista)

# formas de crear sublistas a partir de otra
# [:] Todos los elementos.
# [start:] Todos los elementos desde el índice establecido(start).
# [:end] Todos los elementos desde el índice cero hasta el índice establecido(end).
# [start:end] Todos los elementos de un rango de índices.
# [start:end:step] Todos los elementos de un rango de índices con saltos.
# De igual forma, este listado es aplicable a las tuplas y los strings.
