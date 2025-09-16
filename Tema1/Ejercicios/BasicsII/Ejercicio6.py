# Solicitar tres inputs al usuario
a = input("Introduce el primer valor: ")
b = input("Introduce el segundo valor: ")
c = input("Introduce el tercer valor: ")

# Comprobar si todos son iguales
if a == b == c:
    print("Todos los valores son iguales.")
else:
    print("No todos los valores son iguales.")

# Comprobar si al menos dos son iguales
if a == b or a == c or b == c:
    print("Al menos dos valores son iguales.")
else:
    print("Ningún valor es igual a otro.")