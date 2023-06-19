"""
Las funciones integradas map y filter son funciones de orden superior muy útiles que operan en listas (u objetos similares llamados iterables). El mapa de funciones toma una función y un iterable como argumentos, y devuelve un nuevo iterable con la función aplicada a cada argumento.
"""
#^ MAP
print("map en base a funcion")
def add_five(x):
    return x + 5

nums = [2, 4, 6, 8, 10]
result = list(map(add_five, nums))
print(result)


print("\nmap en base a lambda")
nums = [2, 4, 6, 8, 10]
result = list(map(lambda x: x+5, nums))
print(result)

#^ FILTER
print("\nfilter en base a funcion")
def resto_cero(x):
    return x%2==0

nums = [1, 2, 3, 4, 5]
res = list(filter(resto_cero, nums))
print(res)


print("\nfilter en base a lambda")
nums = [1, 2, 3, 4, 5]
res = list(filter(lambda x: x%2==0, nums))
print(res)