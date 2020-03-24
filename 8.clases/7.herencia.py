# crear clase a partir de exitentes pero con nuevas caracteristica
class Animal:
    def comer(self):
        print('comiendo')

    def dormir(self):
        print('durmiendo')


# ahora perro podra comer y dormir, la clase animal ahora es la clase padre de perro y gato


class Perro(Animal):
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print('ladrando')


class Gato(Animal):
    def ronroneo(self):
        print('ronroneo')


firulais = Perro('firulais')
firulais.dormir()

michi = Gato()
michi.comer()
michi.ronroneo()
