# en python podemos asignar funciones a variables
def centigrados_a_fahremheit(grados):
    return grados * 1.8 + 32


funcion_variable = centigrados_a_fahremheit
print(funcion_variable(32))

# las funciones lambda tambien son conocidas como funciones anonimas
# son expresada comunmente en una linea de codigo


# mi_funcion2 = lambda grados=0 : grados +1.8 + 32


# print(mi_funcion2)

# por el formateo de autoPEP8 esta funcion lambda se convertira automticamente a una funcion normal
# al guardar, buscar 'pycodestyle code E731' para mas info

# Algunas formas de crear expresiones lambdas mas complejas

# sin_parametros = lambda : True

# con_valores = lambda val, val1=10, val2=10 : val + val1 + val2

# con_asterisco = lambda *args : args[0]

# con_doble_asterisco = lambda **kwargs : kwargs[0]

# con_asteriscos = lambda *args , **kwargs : kwargs.get('key', False)
