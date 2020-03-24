variable = [1, 2, 3, 4]
# python toma a none como valor False al igual que 0
# python toma false a None, 0, 0.0, '', [], (), {}, todos los demas valores seran tomados como true
variable = None
print(variable)

if variable:
    print('variable es true')
else:
    print('variable es false')
