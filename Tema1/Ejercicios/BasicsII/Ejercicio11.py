texto = "Lo primero de todo, cómo están los máquinas"

# Pasarlo todo a mayúsculas
print(texto.upper())

# Pasarlo todo a minúsculas
print(texto.lower())

# Pasar a mayúsculas solo las iniciales de las palabras
print(texto.title())

# Crea una lista dividiéndolo por sus espacios
print(texto.split())

# Sustituye las comas , por puntos y comas ;
print(texto.replace(',', ';'))

# Elimina las 'a' minúsculas
print(texto.replace('a', '').replace('á', ''))