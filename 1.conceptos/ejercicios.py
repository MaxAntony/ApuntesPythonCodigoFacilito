from datetime import date
from datetime import datetime
import math

print('calcular el area de un triangulo: ')
base = float(input('ingrese la base\n'))
altura = float(input('ingrese la altura\n'))
area = (base * altura) / 2
print('el area del triangulo es: ', area)

print('\nConvertir dolares a pesos colombianos')
dolares = float(input('Ingrese la cantidad de dolares: '))
pesos_colombianos = dolares * 4120.5
print('la cantidad en pesos colombianos es: ', pesos_colombianos)

print('\nConvertir grados centigrados a fahrenheit')
centigrados = float(input('ingrese los grados centigrados: '))
fahrenheit = (centigrados * 9 / 5) + 32
print('equivale a ', fahrenheit, 'grados fahrenheit')

segundos = 60 * 60 * 24 * 365 * 5
print('\nun lustro tiene ', segundos, ' segundos')

km_sol_a_marte = 227940000
luz_km_x_seg = 300000
tiempo = km_sol_a_marte / luz_km_x_seg
print('\nEl tiempo que se demora la luz desde el sol a marte es: ', tiempo, ' segundos')

diamtro_cm = 50
circunferencia = math.pi * diamtro_cm
num_vueltas = round(1000 / (circunferencia / 100), 1)
print('\nla cantidad de vueltas que da una rueda de 50cm de diametro en 1km son: ', num_vueltas)

cateto_opuesto = 20
angulo_elevacion = 20
# http://elclubdelautodidacta.es/wp/2013/03/trigonometria-en-python/
cateto_adyacente = cateto_opuesto / math.tan(math.radians(22))
# la funcion tan espera radianes por eso se convierte los angulos a radianes
print('\nla longitud de de la sombra de un edificio de 20m')
print('cuando el angulo de los rayos del sol es 22 grados es: ', cateto_adyacente)

edad_usuario1 = input('\ningrese edad del primer usuario: ')
edad_usuario2 = input('ingrese edad del segundo usuario: ')
comparacion_edad = edad_usuario1 == edad_usuario2
print('la edad del primer usuario es la misma que del segundo?: ', comparacion_edad)

dia = int(input('\ningrese su dia de nacimiento: '))
mes = int(input('ingrese su mes de nacimiento: '))
year = int(input('ingrese su año de nacimiento: '))
hoy = datetime.now()

fecha_nacimiento = datetime(year, mes, dia)
meses = round(abs(hoy - fecha_nacimiento).days / 30, 1)
print('\nla cantida de meses transcurridos desde su nacimiento son ', meses)
print('(suponiendo que todos los meses tengan 30 dias)')

materia1 = float(input('\ningrese la nota de la materia 1: '))
materia2 = float(input('ingrese la nota de la materia 2: '))
materia3 = float(input('ingrese la nota de la materia 3: '))
materia4 = float(input('ingrese la nota de la materia 4: '))
materia5 = float(input('ingrese la nota de la materia 5: '))
promedio = (materia1 + materia2 + materia3 + materia4 + materia5) / 5
print('el promedio del alumno es: ', promedio)
