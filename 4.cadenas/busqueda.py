mensaje = 'Este es un texto un poco grande en cuanto a longitud de caracteres se refiere'
# primera forma
# Contamos la cantidad de coincidencias
resultado = mensaje.count('texto')  # devuelve un entero
print(resultado)
print(mensaje.count('e'))
print(mensaje.count('z'))

# segunda forma
resultado = 'texto' in mensaje  # devuelve un booleano
print(resultado)
print('texto' not in mensaje)  # lo negamos

# tercera forma
# nos devuelve el indice de donde comienza el texto

resultado = mensaje.find('texto')
print(resultado)
# extraemos la palabra texto del string mensaje
resultado = mensaje[resultado:resultado + len('texto')]
print(resultado)

# Que pasa si el string no se encuentra
print(mensaje.find('codigo'))  # devuelve -1

# saber si una cadena comienza o termina con
# devuelve un true si comienza con 'Este'
resultado = mensaje.startswith('Este')
print(resultado)
print(mensaje.startswith('este'))  # es case sensitive

print(mensaje.endswith('ere'))  # verifcamos si el mensaje termina en ere
