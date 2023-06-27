"""
Las Lambdas son funciones sin definir funciones
"""

# Lambda
var = (lambda x: x**2)(3)
print(f"lambda x -> {var}")

var = (lambda x,y: x*2*y)(3,4)
print(f"lambda x,y -> {var}")

# Funcion
def exponente(x):
    return x**2

var2 = exponente(3)
print(f"funcion -> {var2}")

# Funcion con Lambda
def funct(num):
    return num*4

var2 = funct((lambda x: x*2)(3))
print(f"Funcion con Lambda -> {var2}")