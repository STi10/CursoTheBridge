direccion ={
    "calle": "Calle Falsa",
    "numero": 123,
    "ciudad": "Springfield",
    "codigo_postal": "12345",
    "pais": "USA"
}
print(direccion["calle"])
print(direccion["numero"])
print(direccion["ciudad"])
print(direccion["codigo_postal"])
print(direccion["pais"])
## Otra forma de hacerlo concatenando todos los datos
concatenacion = (f"{direccion['calle']} {direccion['numero']} {direccion['ciudad']} {direccion['codigo_postal']} {direccion['pais']}")
print(concatenacion)