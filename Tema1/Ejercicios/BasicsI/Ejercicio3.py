"""
Este script solicita al usuario un valor en grados Celsius,
lo convierte a grados Fahrenheit usando la fórmula:
F = C * 9/5 + 32
y muestra el resultado por pantalla.
"""

# Solicita al usuario el dato en grados Celsius
print("Introduce el dato de los grado Celsius a convertir a Fahrenheit:")
# Convierte la entrada a tipo float
grados_celsius = float(input())
# Realiza la conversión de Celsius a Fahrenheit
grados_fahrenheit = (grados_celsius * 9/5) + 32
# Muestra el resultado
print(f"{grados_celsius} grados Celsius son {grados_fahrenheit} grados Fahrenheit")