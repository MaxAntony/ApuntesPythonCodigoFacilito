numero, contador = 123456789, 0

while numero >= 1:
    contador += 1
    numero = numero/10
else:
    print('la cantidad de digitos es', contador)

print(numero, contador)
