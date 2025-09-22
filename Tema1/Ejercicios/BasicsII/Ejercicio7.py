# Programa que recoge dos inputs y compara su suma con 10

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

suma = num1 + num2

if suma == 10:
    print("La suma es igual a 10.")
if suma > 10:
    print("La suma es superior a 10.")
if suma < 10:
    print("La suma es inferior a 10.")
else:
    print("Error en la suma.")