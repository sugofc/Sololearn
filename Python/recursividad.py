"""
La recursividad es un concepto muy importante en la programación funcional. La parte fundamental de la recursividad es la autorreferencia: funciones que se llaman a sí mismas. Se utiliza para resolver problemas que se pueden dividir en subproblemas más fáciles del mismo tipo. Un ejemplo clásico de una función que se implementa recursivamente es la función factorial, que encuentra el producto de todos los números enteros positivos por debajo de un número específico. Por ejemplo, 5! (5 factorial) es 5 * 4 * 3 * 2 * 1 (120). Para implementar esto recursivamente, observe que 5! = 5 * 4!, 4! = 4 * 3!, 3! = 3 * 2!, y así sucesivamente. Generalmente, n! = n * (n-1)!. Además, 1! = 1. Esto se conoce como el caso base, ya que se puede calcular sin realizar más factoriales. A continuación se muestra una implementación recursiva de la función factorial.
"""

#* Factorial
def factorial(x):
    if x == 1:
        return 1
    else: 
        return x * factorial(x-1)

print(f"factorial -> {factorial(3)}")


#* PAR E IMPAR
def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)

print(f"par -> {is_odd(17)}")
print(f"impar -> {is_even(23)}")


def fib(x):
    if x == 0 or x == 1:
        return 1
    else: 
        return fib(x-1) + fib(x-2)
print(f"fib -> {fib(4)}")