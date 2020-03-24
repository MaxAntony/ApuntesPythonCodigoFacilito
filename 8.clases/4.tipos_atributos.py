class Circulo:
    pi = 3.1415  # variable de clase

    def __init__(self, radio):
        self.radio = radio  # variable de isntancia


circulo_a = Circulo(10)
circulo_b = Circulo(20)

print(circulo_a.radio)
print(circulo_b.radio)
# aqui modificmos a la varibale de instancia, solo es de cada instancia
circulo_b.radio = 100
print(circulo_a.radio)
print(circulo_b.radio)

print(circulo_a.pi)
print(circulo_b.pi)
# las variables de clase se pueden usar sin necesidad de crear una instancia
print(Circulo.pi)
