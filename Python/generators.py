"""
Los generadores son un tipo de iterables, como listas o tuplas. A diferencia de las listas, no permiten la indexación con índices arbitrarios, pero aún se pueden iterar con bucles for. Se pueden crear usando funciones y la declaración de rendimiento.
"""

def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1
    
for i in countdown():
    print(i)