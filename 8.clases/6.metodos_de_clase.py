# son metodos similiares que pueden ser llamados sin la necesidad de instancias
class Circulo:
    pi = 3.14159265

    @classmethod
    # cls no es palabra reservada pero por convencion hace referncia ala clase
    def area(cls, radio):
        return cls.pi * radio**2


# normalmente utilizado para trabajar con variables de clase
print(Circulo.area(10))
