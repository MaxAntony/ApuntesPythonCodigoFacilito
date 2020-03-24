# todas las clases c¿que creamos heredan de object

# amblas clases hereddan de object, solo que en la primera es implicita


class Gato():
    def __init__(self, nombre):
        self.nombre = nombre

    # sobreescribimos el methodo de object y se puede ver la la linea 23

    def __str__(self):
        return self.nombre


class Pato(object):
    # el metodo init no es el constructor de la clase
    def __init__(self, nombre):
        self.nombre = nombre


gato = Gato('BIGOTES')
pato = Pato('LUCAS')

print(gato.nombre)
print(pato.nombre)

gato.edad = 56

print(gato.__dict__)
print(pato.__dict__)
