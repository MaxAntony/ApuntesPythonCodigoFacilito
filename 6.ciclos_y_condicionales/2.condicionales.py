color_luz = 'amarillo'
# cuando una condicion se cumple ejecuta el codigo y ya no evalua mas codiciones
if color_luz == 'verde':
    print('puede pasar')
elif color_luz == 'amarillo':
    print('espere por favor')
else:
    print('alto total')
# el else es completamente optativo

# sin aperadores
variable = True
if variable:
    print('es verdadero')

variable = {}
if variable:
    print('es verdadero')
else:
    print('no es verdadero')


# en python no hay do-while ni switch
# para el switch podemos usar condiciones
# el do while se emula usando el while con el else
