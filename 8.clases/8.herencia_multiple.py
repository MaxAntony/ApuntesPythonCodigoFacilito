# crear clase a partir de exitentes pero con nuevas caracteristica
class Animal:
    def comer(self):
        print('comiendo')

    def dormir(self):
        print('durmiendo')

    def comun(self):
        print('este es un metodo de animal')

# como el script se lee de arriba hacia abajo las clases de donde estamos heredando deben estar arriba


class Mascota:
    def fecha_adopcion(self, fecha):
        self.fecha_de_adopcion = fecha

    def comun(self):
        print('este es un metodo de mascota')
# ahora perro podra comer y dormir, la clase animal ahora es la clase padre de perro y gato


class Perro(Animal, Mascota):
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print('ladrando')

    def comun(self):
        print('este es un metodo de perro')


class Gato(Animal):
    def ronroneo(self):
        print('ronroneo')


firulais = Perro('firulais')
firulais.dormir()

michi = Gato()
michi.comer()
michi.ronroneo()

firulais.fecha_adopcion('hoy')
print(firulais.fecha_de_adopcion)
# como el metodo se repite, primero busca en Perro, si no se encuentra va a buscar en Animal por que es la primera clase en los parentesis, si no encuentra el metodo en animal entonce buscara en Mascota
firulais.comun()
