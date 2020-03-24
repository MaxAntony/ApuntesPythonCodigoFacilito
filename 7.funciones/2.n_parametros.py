# valores por default de parametros
# el valor por defecto no debe tener parentesis entre el igual
# los parametros con valores por default deben ir al final


def crear_usuario(nombre, apellido, edad=10):
    return {
        'nombre': nombre,
        'apellido': apellido,
        'nombre_completo': '{} {}'.format(nombre, apellido),
        'edad': edad
    }


codi = crear_usuario('Codi', 'Facilito')
print(codi['nombre'])
print(codi['nombre_completo'])
print(codi['edad'])

# asignar argumentos mediante el nombre de los parametros
codi2 = crear_usuario(apellido='Facilito', edad=5, nombre='max')
print(codi2['nombre'])
print(codi2['nombre_completo'])
print(codi2['edad'])
