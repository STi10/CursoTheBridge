# Solicitar datos al usuario
distrito = input("Introduce el distrito: ")
superficie = float(input("Introduce la superficie en m2: "))

# Comprobar si es Retiro y aplicar precios según superficie
if distrito.lower() == "retiro":
    print("Distrito Retiro")
    if superficie > 100:
        print("Precio: 1000€")
    else:
        print("Precio: 500€")
else:
    print("Otro distrito")