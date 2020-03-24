import calculadora
# importar un paquete
from animales.aves import Pinguino

print(calculadora.suma(4, 6))
print(calculadora.__name__)

# aqui main significa que este es el archivo pricipal
print(__name__)
# __ name__ va a tener el valor de __main__ siempre que sea el archivo ejecutado


pinguino = Pinguino()
pinguino.nadar()
