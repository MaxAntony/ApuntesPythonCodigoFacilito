# crear clase a partir de exitentes pero con nuevas caracteristica
class Animal:
    def comer(self):
        print('comiendo')

    def dormir(self):
        print('durmiendo')


# como el script se lee de arriba hacia abajo las clases de donde estamos heredando deben estar arriba


class Mascota:
    def fecha_adopcion(self, fecha):
        self.fecha_de_adopcion = fecha

# ahora perro podra comer y dormir, la clase animal ahora es la clase padre de perro y gato


class Perro(Animal, Mascota):
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print('ladrando')

# sobreescribimo el motodo dormir de animal
    def dormir(self):
        print(self.nombre + ' esta durmiendo')
        # si queremos agregar mas funcionalidad es asi
        Animal.dormir(self)
        print('no molestar')


firulais = Perro('firulais')
firulais.dormir()
