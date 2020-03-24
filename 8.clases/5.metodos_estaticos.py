# metodos que no necesitan una instancia para ser usados
class Triangulo:
    # metodo de clase
    # cuando usamos methodos estaticos no podemos usar variables de instancia, es una limitante
    # pero ayuda si tenemos que ejecutar esta funcion multiples veces sin tener que crear instancias
    # pero si podemos usar variables de clase
    numero = 2
    @staticmethod
    def area(base, altura):
        return (base+altura)/Triangulo.numero


# no se necesita instanciar para usar
print(Triangulo.area(10, 20))
