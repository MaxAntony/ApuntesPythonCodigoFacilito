# los comprehension nos permiten generar estructuras de datos de una menra sensilla ya sea lista tupla o diccionario
lista = []

for x in range(1, 101):
    lista.append(x)

print(lista)

# simplificando el codigo con comprehension
# despues del corchete esta el valor que queremos guardar y despues de este el ciclo for que genera los datos
# use [] para listas, ( ) para tuplas y {} para diccionarios
estructura = [x for x in range(1, 101)]
print(estructura)
# codi es el valor que queremos almacenar y despues viene el ciclo
estructura = ['codi' for x in range(1, 101)]
print(estructura)

# para una tupla
estructura = tuple((x for x in range(1, 101)))
print(estructura)

# agregando cmoplejidad para que guarde pares
estructura = tuple((x for x in range(1, 101) if x % 2 == 0))
print(estructura)

# agregando cmoplejidad para que guarde pares y que sean menores a 50
estructura = tuple((x for x in range(1, 101) if x % 2 == 0 if x < 50))
print(estructura)

# tambien podemos usar funciones dentro de las comprehension como lo vemos con range, podemos usar muchas funciones
# lo recomendable es usar comprehension de manera simple, ya sea con una o maximo 2 condicionales


# generar diccionario
diccionario = {indice: valor for indice, valor in enumerate(estructura)}
print(diccionario)
