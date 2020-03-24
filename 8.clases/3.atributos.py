# son funciones dentro de la clase
class Usuario:

    def __init__(self, username='', correo='', nombre=''):
        self.username = username
        self.correo = correo
        self.nombre = nombre

    def saludar(self, nombre):
        print('hola {}'.format(nombre))

    def mostrar_username(self):
        print(self.username)

    def mostrar_nombre(self):
        print(self.nombre)

    def crear_nombre(self, nombre):
        self.nombre = nombre


# para crear atributos existen 2 maneras, dentro y fuera de la clase
# instanciamos un objeto
codi = Usuario()

codi.username = 'codi'
codi.correo = 'codi@gmail.com'

codi.mostrar_username()
codi.crear_nombre('max')
codi.mostrar_nombre()

codi.saludar('max')

maxi = Usuario('maximo', 'mm@mm.com', 'lalala')
