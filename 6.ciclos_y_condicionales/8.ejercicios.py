# calificaciones = {'calculo': 10, 'dibujo': 15, 'artes': 20, 'matematica': 4}

# total = 0
# mejor = 0
# for materia in calificaciones:
#     total += calificaciones[materia]
#     if calificaciones[materia] > mejor:
#         mejor = calificaciones[materia]
# print('promedio total del alumno:')
# print(total / len(calificaciones))
# print('mejor materia:')
# print(mejor)

# continuar = 10
# lista = []
# while continuar > 0:
#     entrada = int(input('ingrese un numero positivo: '))
#     if entrada > 0:
#         continuar -= 1
#         print(continuar)
#         lista.append(entrada)
#     else:
#         print('por favor ingrese un numero positivo')

# suma = 0
# for numero in lista:
#     suma += numero
# print('la suma de los numeros ingresados es: ', suma)
# print('el promedio es: ', suma / len(lista))
# print('el mayor numero de la lista es', max(lista))
# print('el menor numero de la lista es', min(lista))

# =======================
# buscar palabras palindromas
# continuar = True
# lista = []
# while continuar:
#     frase = input('ingrese una frase: ')
#     lista.append(frase)
#     seguir = input('¿continuar? si/no: ')
#     if seguir != 'si':
#         continuar = False
# todas_frases = ''
# for item in lista:
#     todas_frases += (' ' + item)
# palabras = todas_frases.split(' ')
# palindromas = []
# for palabra in palabras:
#     reverse = ''
#     for letra in reversed(palabra):
#         reverse += letra
#     if palabra == reverse and palabra != '':
#         palindromas.append(palabra)

# print('\nlas palabras palindromas son: ')
# for palindroma in palindromas:
#     print(palindroma)

# ======================0
# palabra que mas se repite
# TODO: mejorar a la hora de dividir las palabras por que no se eliminan los
# signos de puntuacion, con endWith podria ser
fragmento = '''You will rejoice to hear that no disaster has accompanied the
commencement of an enterprise which you have regarded with such
evil forebodings.  I arrived here yesterday, and my first task is
to assure my dear sister of my welfare and increasing confidence in
the success of my undertaking.

I am already far north of London, and as I walk in the streets of
Petersburgh, I feel a cold northern breeze play upon my cheeks,
which braces my nerves and fills me with delight.  Do you understand
this feeling?  This breeze, which has travelled from the regions
towards which I am advancing, gives me a foretaste of those icy climes.
Inspirited by this wind of promise, my daydreams become more fervent
and vivid.  I try in vain to be persuaded that the pole is the seat
of frost and desolation; it ever presents itself to my imagination as the
region of beauty and delight.  There, Margaret, the sun is forever visible,
its broad disk just skirting the horizon and diffusing a perpetual splendour.
There--for with your leave, my sister, I will put some trust in preceding
navigators--there snow and frost are banished; and, sailing over a calm sea,
we may be wafted to a land surpassing in wonders and in beauty every region
hitherto discovered on the habitable globe.  Its productions and features
may be without example, as the phenomena of the heavenly bodies undoubtedly
are in those undiscovered solitudes.  What may not be expected in a country
of eternal light?  I may there discover the wondrous power which attracts
the needle and may regulate a thousand celestial observations that require
only this voyage to render their seeming eccentricities consistent forever.
I shall satiate my ardent curiosity with the sight of a part of the world
never before visited, and may tread a land never before imprinted by the
foot of man.  These are my enticements, and they are sufficient to conquer
all fear of danger or death and to induce me to commence this laborious voyage
with the joy a child feels when he embarks in a little boat, with his holiday
mates, on an expedition of discovery up his native river.  But supposing all
these conjectures to be false, you cannot contest the inestimable benefit
which I shall confer on all mankind, to the last generation, by discovering
a passage near the pole to those countries, to reach which at present so many
months are requisite; or by ascertaining the secret of the magnet, which,
if at all possible, can only be effected by an undertaking such as mine.
'''
palabras = fragmento.split()
cantidades = {}
for palabra in palabras:
    numero = cantidades.setdefault(palabra, 0)
    cantidades[palabra] = numero+1
anterior = 0
mas_repetida = {}
for item in cantidades:
    print(item)

# Mostrar en pantalla la palabra que más se repita junto con la cantidad de veces que lo hace del capituló número uno de Frankenstein

# Remplazar cada letra de una frase dada por el usuario por la posición que le corresponde en el abecedario y mostrar el nuevo string en pantalla. (Los espacios no se remplazan) . Ejemplo: frase : 'Hola' salida : 815121 H(8) o(15) l(12) a(1)

# Mostrar en pantalla la cantidad de vocales que existe en una frase dada por el usuario.

# Mostrar en pantalla la frecuencia de aparición de vocales en una frase dada por el usuario.

# Ejemplo : 'Hola Mundo' salida : o=2, a=3, u=1

# Eliminar todas las vocales de una frase dado por el usuario y mostrar el nuevo string en pantalla.

# Listar todos los números pares del 0 al 100
# TODO: queda pendiente terminar estos ejercicios
