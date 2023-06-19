lista_a_string = 'asdf'
nombre_variable = [nombre for nombre, valor in locals().items() if valor is lista_a_string ][0]
cadena = "'" + nombre_variable + "'"
print(cadena)