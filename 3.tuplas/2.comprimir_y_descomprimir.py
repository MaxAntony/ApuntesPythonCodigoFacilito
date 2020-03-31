tupla = (1, 2, 3, 4, 5, 6)
lista = [10, 20, 30, 40]
# la funcion zip puede recibir n cantidad de listas y tuplas
resultado = zip(tupla, lista)
print(resultado)

# lo convertimos atupla para visualizarlo
resultado = tuple(resultado)
print(resultado)

# tambien lo podemos convertir a lista
resultado = list(resultado)
print(resultado)

tupla_dos = (100, 200, 300, 400)
resultado = zip(tupla, lista, tupla_dos)
resultado = list(resultado)
print(resultado)

# desempaquetando tuplas
tupla = (10, 20, 30, 40, 50)
# necesitamos obtener el primer, segundo y ultimo elemento

# con indices
primer = tupla[0]
segundo = tupla[1]
ultimo = tupla[-1]
# o mejor
primer, segundo, ultimo = tupla[0], tupla[1], tupla[-1]


# otra opcion usando guion bajo
primer, segundo, _, _, ultimo = tupla
# la posicion tercera y cuarta son ignoradas

# pero si tenemos una tupla mas larga
tupla = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400)

# de esta manera
primer, segundo, *_, ultimo = tupla

# La función incorporada (i.e. no necesita importarse) zip() toma como argumento dos o más objetos iterables (idealmente cada uno de ellos con la misma cantidad de elementos) y retorna un nuevo iterable cuyos elementos son tuplas que contienen un elemento de cada uno de los iteradores originales.

paises = ["China", "India", "Estados Unidos", "Indonesia"]
poblaciones = [1391, 1364, 327, 264]
# Esta función es especialmente útil en bucles for para acceder a los elementos de dos o más iterables simultáneamente:

for pais, poblacion in zip(paises, poblaciones):
    print("{}: {} millones de habitantes.".format(pais, poblacion))
