"""
Los decoradores proporcionan una forma de modificar funciones usando otras funciones. Esto es ideal cuando necesita ampliar la funcionalidad de las funciones que no desea modificar.
"""

def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("TEST DECORATORS!")

print_text = decor(print_text)

print_text()