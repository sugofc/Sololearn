"""
Comprime el for en una lista y lo devuelve
"""
#^ Ejemplo 1
# Ejemplo For
nombres = ['Felipe', 'Pedro','Daniel', 'Diego']

for x in nombres:
    print(x)

# Ejemplo List Comprehension
print([x for x in nombres])

print("\n")

#^ Ejemplo 2
# Ejemplo For en una Lista
numeros = [1,2]
letras = ["A","B","C"]
data = []
p = 0

for n in numeros:
    for l in letras:
        data.append([])
        data[p] = [n,l]
        p += 1
else:
    print(data)

# Ejemplo List Comprehension (que ya lo deja en lista)
print([[n,l] for n in numeros for l in letras])

print("\n")

#^ Ejemplo 3
# Ejemplo For
nombres = ['Felipe', 'Pedro','Daniel', 'Diego']

for x in nombres:
    if x == 'Diego':
        print(x)

# Ejemplo List Comprehension
print([x for x in nombres if x == 'Diego'])

print("\n")

#^ Ejemplo 4
# Ejemplo For con else
for x in nombres:
    if x == 'Rodrigo':
        print(x)
else:
    print("No existe")

# Ejemplo List Comprehension - No existe else en una comprehension, pero se puede agregar
# sin embargo arrojara la cantidad de else segun el tamaño de la lista
print([x if x == 'Rodrigo' else 'No Existe' for x in nombres])