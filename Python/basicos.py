"""
Cosas basicas de Python
"""

#^ Prints
print('test')
print(2)
print("salto \nde \nlinea") # \n saltar linea
print("\ttabulacion") # \t tabulacion

#^ Tipos de Datos
n1 = 12
n2 = "14"
print(type(n1), type(n2)) # No se puede sumar un entero con un string #! class int, class str
print("la suma entre {} y {} es: {}".format(n1,int(n2),n1+int(n2))) #! 12 + 14 = 26

#^ Variables
#~ en 1 lineas
name, last = "Felipe", "Castillo"
#~ en linea separadas
apodo = "Sugo"
age = 35
print("Mi nombre es ",name," y me apellido es ",last)  #impresion de variable
print(f"Mi nombre es {name} y me apellido es {last}") # con f string

#^ Booleanos
v = True
f = False
print(v,f) #! True False

x,y = "5", 5
print(x==y) #! False

#^ Operaciones Aritmeticas
a, b = 6, 2
print(a+5) # suma #! 11
a+=2 # A la variable "a" se le asigna +2 a 6
print(a) # resultado de a+=2 #! 8
print(a/b) # 8 / 2 = #!4.0
a/=b # A la variable "a" se le asigna /2 a 8
print(a) # resultado de a/=2 #! 4.0
print(4%3) # modulo #! 1
print(a+b) # suma 2 variables a + b (4 + 2) = #! 6.0