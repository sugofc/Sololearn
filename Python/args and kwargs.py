"""
*args 
Python le permite tener funciones con diferentes números de argumentos. El uso de *args como parámetro de función le permite pasar un número arbitrario de argumentos a esa función. Luego se puede acceder a los argumentos como la tupla args en el cuerpo de la función.
"""
print("*args")
def function(named_arg, *args):
    print(named_arg)
    print(args)

function(1, 2, 3, 4, 5)

"""
**kwargs
significa argumentos de palabra clave, le permite manejar argumentos con nombre que no ha definido de antemano. Los argumentos de palabras clave devuelven un diccionario en el que las claves son los nombres de los argumentos y los valores son los valores de los argumentos.
"""
print("\n**kwargs")
def my_func(x, y=7, *args, **kwargs):
    print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)


print("\n\n\n\n\n")
def my_min(*args):
    return min(args)

print(my_min(8, 13, 4, 42, 120, 7))