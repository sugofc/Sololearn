"""
Cosas basicas de Python
"""

print("Prints".center(50))
print('test')
print(2)
print("salto \nde \nlinea") # \n saltar linea
print("\ttabulacion") # \t tabulacion

print("\n\n")
print("Formas de Prints".center(50))
name = 'Felipe'
edad = 35
dolar = 24.7
print("Tu nombre es "+name+" y tu edad es "+str(edad)+" y tienes "+str(dolar)+" dolares.")
print("Tu nombre es {:10} y tu edad es {:20} y tienes {:30} dolares.".format(name,edad,dolar))
print("Tu nombre es {n} y tu edad es {e} y tienes {d:.2f} dolares.".format(n=name,e=edad,
d=dolar))
print("Tu nombre es %s y tu edad es %d y tienes %.3f dolares." % (name, edad, dolar))
print(f"Tu nombre es {name} y tu edad es {edad} y tienes {dolar:.4f} dolares.")

print("\n\n")
print("Tipos de Datos".center(50))
n1 = 12
n2 = "14"
print(type(n1), type(n2)) # No se puede sumar un entero con un string #! class int, class str
print("la suma entre {} y {} es: {}".format(n1,int(n2),n1+int(n2))) #! 12 + 14 = 26

print("\n\n")
print("Variables".center(50))
#~ en 1 lineas
name, last = "Felipe", "Castillo"
#~ en linea separadas
apodo = "Sugo"
age = 35
print("Mi nombre es ",name," y me apellido es ",last)  #impresion de variable
print(f"Mi nombre es {name} y me apellido es {last}") # con f string

print("\n\n")
print("Booleanos".center(50))
v = True
f = False
print(v,f) #! True False

x,y = "5", 5
print(x==y) #! False

print("\n\n")
print("Operaciones Aritmeticas".center(50))
a, b = 6, 2
print(a+5) # suma #! 11
a+=2 # A la variable "a" se le asigna +2 a 6
print(a) # resultado de a+=2 #! 8
print(a/b) # 8 / 2 = #!4.0
a/=b # A la variable "a" se le asigna /2 a 8
print(a) # resultado de a/=2 #! 4.0
print(4%3) # modulo #! 1
print(a+b) # suma 2 variables a + b (4 + 2) = #! 6.0