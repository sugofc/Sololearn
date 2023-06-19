
#* Tuplas

# Las tuplas no se pueden modificar
numeros = ('dos','cinco','tres','uno','cuatro')

print(numeros)
print(numeros[0])
#numeros[0] = 'cero'


#* Tuplas Unpacking
a, b, c, d, e = numeros #numeros es la tupla mas arriba
print(a, b, c, d, e)

a, *b, c = numeros # "*" Desempaqueta elementos
print(a, b, c)

x, y = ["a","b"] # Intercambia valores
x, y = y, x
print(x, y)