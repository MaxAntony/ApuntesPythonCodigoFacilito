texto = 'curso De python 3, python basico'
print(texto.capitalize())
print(texto.swapcase())
print(texto.upper())
print(texto.lower())
print(texto.isupper())
print(texto.islower())
print(texto.lower().islower())
print(texto.title())
print(texto.replace('python', 'ruby'))
# python sera reemplazado una sola vez
print(texto.replace('python', 'ruby', 1))

texto = '    curso de python 3, python basico            '
print(texto.strip())  # quita espacion al inicio y al final

# =============0
curso = 'Python'
version = '3'
# reemplazo con respecto a la posicion
resultado = 'Curso de %s %s' % (curso, version)
print(resultado)

# con metodo format
resultado = 'curso de {} {}'.format(curso, version)
print(resultado)

resultado = 'curso de {a} {b}'.format(
    b=version, a=curso)  # reemplazo con respecto a nombres
print(resultado)
