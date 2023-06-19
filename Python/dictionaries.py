"""
Los Diccionarios se basan en una llave y elementos.
La llave puede ser un string, un int, y los elementos pueden ser string, int, tuplas, listas u otros diccionarios
"""
ages = {
    "Dave": 24,
    "Mary": 42,
    "John": 58
}
print(ages["Mary"])

datos = {
    1:{
        'name' : "Dave",
        'age' : 24
    },
    2: 'test',
    3: ["uno","dos","tres"]
}
print(datos[1]['age'])
print(datos[2])
print(datos[3][1])

