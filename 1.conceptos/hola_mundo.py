print('hola mundo')

nombre_tutor = 'max'
print(nombre_tutor)

# constante
CONSTANTE = 'no debe cambiarse el valor'
print(CONSTANTE)
# no existen constantes en python, se pone en mayuscula para identificar a una constante

# declaramos multiples variables
valor1, valor2, valor3 = 'hola', True, 3


variable_uno = 10
variable_dos = 18

mayor = variable_uno > variable_dos
menor = variable_uno < variable_dos
mayor_igual = variable_uno >= variable_dos
menor_igual = variable_uno <= variable_dos
igual = variable_uno == variable_dos
diferente = variable_uno != variable_dos

print(mayor)
print(menor)
print(mayor_igual)
print(menor_igual)
print(igual)
print(diferente)

# operadores logicos
resultado = True and True and diferente
print(resultado)

resultado = True and True and mayor
resultado = True or True or False

resultado = not True

# comparar si dos valores enteros son iguales/
igual = variable_uno is variable_dos

# entrada por teclado
print('Cual es tu nombre')
nombre = input()
edad = int(input('Cual es tu edad\n'))
peso = float(input('Cual es tu peso\n'))
autorizado = input('estas autorizado (si/no)\n') == 'si'
print('Hola', nombre, ' de ', edad, ' años y ', peso, ' de peso')
print('autorizado: ', autorizado)
