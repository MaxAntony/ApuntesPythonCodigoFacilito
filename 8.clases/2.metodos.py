# son funciones dentro de la clase
class Usuario:
    pass

# todos los metodos deben recibir un parameetro, por convencion ponemos la palabra self que simboliza el objeto
    def saluda(self):
        print('hola')
# todo lo visto en funcinoes es apicable

    def saluda_persona(self, nombre):
        print('hola {}'.format(nombre))


# instanciamos un objeto
codi = Usuario()
facilito = Usuario()

# saber typo de objeto
print(type(codi))

codi.saluda()
