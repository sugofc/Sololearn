
# elemento - nombre / 0 = Felipe, 1 = Pedro, 2 = Daniel, 3 = Diego
nombres = ['Felipe', 'Pedro','Daniel', 'Diego']

print(nombres) # Imprime lista
print(nombres[3])

nombres.append('Ivan') # Agrega nuevo elemento
print(nombres)
nombres.sort() # ordena la lista
print(nombres) # muestra lista ordenada
nombres[3] = 'Rodri' # modifica el elemento 3, en este caso 'Ivan'
print(nombres) # muestra lista modificada