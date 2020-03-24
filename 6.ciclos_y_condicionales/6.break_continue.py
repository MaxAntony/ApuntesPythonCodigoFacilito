titulo = 'curso de python 3'
for letra in titulo:
    if letra == 'p':
        break
    print(letra)
    # break interrumpe todo el ciclo y ya no itera

for letra in titulo:
    if letra == 'o':
        continue
    print(letra)
    # continue hace que la iteracio se corte y pase a la sgt iteracion
