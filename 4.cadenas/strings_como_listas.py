lenguajes = 'Python; Java; Ruby; PHP; Swift; JavaScript; C#; C; C++'

# el separador por default de split es en espacio
resultado = lenguajes.split()
print(resultado)

resultado = lenguajes.split(';')
print(resultado)

separador = '; '
resultado = lenguajes.split(separador)
print(resultado)

# ahora a la inversa lista a string
nuevo_string = ' '.join(resultado)
print(nuevo_string)

nuevo_string = ' - '.join(resultado)
print(nuevo_string)

nuevo_string = separador.join(resultado)
print(nuevo_string)

# dividir en saltos de linea
texto = '''Este es un texto
Con multiples
saltos de linea'''

print(texto)
print(texto.splitlines())
