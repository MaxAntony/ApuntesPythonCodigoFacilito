calificacion = 10  # con input seria
color = None
if calificacion >= 7:
    color = 'verde'
else:
    color = 'rojo'

print(calificacion, color)

# reduciendo lineas de codigo
color = 'rojo'
if calificacion >= 7:
    color = 'verde'

print(calificacion, color)

# reduciendo aun mas lineas de codigo
color = 'verde' if calificacion >= 7 else 'verde'
print(calificacion, color)
