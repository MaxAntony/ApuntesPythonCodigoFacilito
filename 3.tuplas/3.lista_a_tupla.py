lista = ['curso', 'python', 'codigoFacilito']
tupla = ('introduccion', 'basica', 'listas', 'tuplas')

# tupla a lista, la tupla no se modifica
nueva_lista = list(tupla)
print(nueva_lista)

# la lista no se modifica
nueva_tupla = tuple(lista)
print(nueva_tupla)


# los string pueden ser convertidos a listas y a tuplas
mensaje = ' este es el curso de python'
print(tuple(mensaje))
print(list(mensaje))
