# Crear una lista con 3 elementos numéricos
lista = [10, 20, 30]

# Añadir un cuarto elemento
lista.append(40)

# Calcular la suma de todos
suma = sum(lista)
print("Suma de todos los elementos:", suma)

# Eliminar el segundo elemento de la lista
del lista[1]

# Añadir otro elemento en la posición 3 de la lista
lista.insert(2, 50)

# Crear otra lista con 4 elementos y concatenarla a la que ya tenías
otra_lista = [60, 70, 80, 90]
lista_final = lista + otra_lista

print("Lista final:", lista_final)