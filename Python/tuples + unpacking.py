
#* Tuplas
# Las tuplas no se pueden modificar
numeros = ('dos','cinco','tres','uno','cuatro')

print(f"tupla -> {numeros}")
print(f"tupla[0] -> {numeros[0]}")

#* Tuplas Unpacking
a, b, c, d, e = numeros #numeros es la tupla mas arriba
print(f"Unpacking A -> {a, b, c, d, e}")

a, *b, c = numeros # "*" Desempaqueta elementos
print(f"Unpacking B -> {a, b, c}")

*a, = numeros
print(f"Unpacking C -> {a}")

x, y = ["x","y"] # Intercambia valores
x, y = y, x
print(f"Intercambio -> {x, y}")