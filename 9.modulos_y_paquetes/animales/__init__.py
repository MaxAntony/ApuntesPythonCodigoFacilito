# si se hace esto
from .aves import Pinguino
# entonces en principal2 puede hacer esto
# from animales import Pinguino


# cuando este archivo se encuentre dentro del folder python sabra que el folder animales es un paquete
print('este es un mensaje del archivo init')

# aqui tambien podemos generar instancias
mi_pinguino = Pinguino()  # para usarlos en importacion

# esto nos da posibilidad de usar patrones de diseño por ejemplo singleton


def mi_funcion():
    print('mi funcion')
