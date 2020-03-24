# importamos las librerias necesarias
from datetime import date
from datetime import datetime
from datetime import timedelta

# dia actual
today = date.today()
print(today)


# fecha actual
now = datetime.now()
print(now)


# ATRIBUTOS
print('el dia actual es {}'.format(today.day))
print('el mes actual es {}'.format(today.month))
print('el año actual es {}'.format(today.year))

print('el dia actual es {}'.format(now.day))
print('el mes actual es {}'.format(now.month))
print('el año actual es {}'.format(now.year))
print('la hora actual es {}'.format(now.hour))
print('el minuto actual es {}'.format(now.minute))
print('el segundo actual es {}'.format(now.second))
print('el microsegundo actual es {}'.format(now.microsecond))

# creando una fecha
new_date = datetime(2019, 3, 5, 15, 45, 5)

# operaciones
# sumar dos dias a la fecha actual
now = datetime.now()
new_date = now + timedelta(days=2)
print(new_date)

# comparacion
if now < new_date:
    print('la fecha actual es menor que la fecha nueva')

# FORMATO DE FECHAS
format = now.strftime(
    'Dia: %d, Mes: %m,Año: %Y,Hora: %H, Minutos: %M, Segundos: %S ')
print(format)


def current_date_format(date):
    months = ('Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
              'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre')
    day = date.day
    month = months[date.month - 1]
    year = date.year
    message = '{} de {} del {}'.format(day, month, year)

    return message


print(current_date_format(now))
