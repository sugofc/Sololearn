"""
Un for nos sirve para recorrer elementos iterables, una lista, un set, una tupla, etc...
"""
nombres = ['Felipe', 'Pedro','Daniel', 'Diego']

for x in nombres:
    print(x)

print("\n")

for x in nombres:
    if x != 'Felipe':
        print(x)

print("\n")

for x in nombres:
    if x == 'Rodrigo':
        print(x)
else:
    print("No existe")