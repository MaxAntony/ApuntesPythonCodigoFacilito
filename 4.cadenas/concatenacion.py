curso = 'Curso de python'
curso = 'c' + curso[1:] + ' en codigo facilito'  # Generamos otro string

print(curso)
# curso = curso + 1  # esto dara un error por que solo se deben concatenar strings
# tenemos que convertir
curso = curso + str(1)
curso = curso + str(False)
print(curso)
