"""
Cuando una función con la declaración yield es llamada, no se ejecuta inmediatamente como una función normal. En cambio, devuelve un objeto generador que puede ser iterado para obtener los valores generados. Cada vez que se solicita un valor al generador, la función se ejecuta desde el principio hasta que alcanza una declaración yield. En ese momento, el valor después de la declaración yield se devuelve como el siguiente valor en la secuencia generada. La función se "pausa" en ese punto, y cuando se solicita el siguiente valor, se reanuda desde donde se detuvo.
"""

def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1
    
for i in countdown():
    print(i)
