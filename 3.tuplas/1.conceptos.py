# lo mismo que las listas pero
# las tuplas son inmutables, no podemos modificar los elementos que almacenan
# tampoco podemos quitar o añadir elementos, una vez definida esta se queda asi en todo el programa

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# la ventaja es la mayor velocidad de acceso a los elementos
elemento0 = tupla[0]
print(elemento0)

last_elemento = tupla[-1]
print(last_elemento)

subTuplaSteps = tupla[0:5:2]
# lo mismo que las listas
print(subTuplaSteps)
# recuerda que subtuplaSteps es una tupla

# subTuplaSteps[1] = 6 # esto dara error

# asignando variables de una tupla
# metodo largo
tupla2 = (1, 2, 3, 4)
uno, dos, tres, cuatro = tupla2[0], tupla2[1], tupla2[2], tupla2[3],
print(uno)
print(dos)
print(tres)
print(cuatro)

# metodo rapido
# pero esto solo funciona si la tupla solo tiene 4 elementos
# uno, dos, tres, cuatro = tupla  # esto dara error al tener mas de 4 elementos

uno, dos, tres, cuatro = tupla2
print(uno)
print(dos)
print(tres)
print(cuatro)

# pero si se quiere hacerlo se puede hacer asi
# el ultimo elemento tendra a las demas variables que no se pudieron asignar en forma de lista
uno, dos, tres, *cuatro = tupla
print(uno)
print(dos)
print(tres)
print(cuatro)
# esta es otra forma de realizarlo, ver resultado
uno, *dos, ocho, nueve = tupla
print(uno)
print(dos)
print(ocho)
print(nueve)
