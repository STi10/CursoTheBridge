"""
Este script solicita al usuario los datos de una dirección (calle, número, ciudad, código postal y país)
y los almacena en un diccionario. Luego muestra cada dato por separado y finalmente los concatena en una sola línea.
"""

# Pedir todos los valores por teclado
# Se crea el diccionario 'direccion' con los datos introducidos por el usuario
direccion = {
    "calle": input("Introduce la calle: "),
    "numero": input("Introduce el número: "),
    "ciudad": input("Introduce la ciudad: "),
    "codigo_postal": input("Introduce el código postal: "),
    "pais": input("Introduce el país: ")
}

# Mostrar cada dato por separado
print(direccion["calle"])
print(direccion["numero"])
print(direccion["ciudad"])
print(direccion["codigo_postal"])
print(direccion["pais"])

# Otra forma de mostrar todos los datos concatenados
print(f"{direccion['calle']} {direccion['numero']} {direccion['ciudad']} {direccion['codigo_postal']} {direccion['pais']}")
