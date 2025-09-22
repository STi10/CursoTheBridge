import math

# Ejercicio 1: Conversor de números a días de la semana
def conversorDiasSemana(dia_Int):
    if type(dia_Int) != int or dia_Int < 1 or dia_Int > 7:
        return "Día erroneo"
    else:
        dias_semana = {
            1: "Lunes",
            2: "Martes",
            3: "Miercoles",
            4: "Jueves",
            5: "Viernes",
            6: "Sabado",
            7: "Domingo"
        }
        return dias_semana[dia_Int]

# Ejercicio 2: Crear pirámide invertida
def creaPiramide(n_filas):
    piramide = list(range(n_filas, 0, -1))
    for i in range(1, n_filas + 1):
        print(piramide)
        piramide.pop(0)

# Ejercicio 3: Comparador de números
def comparadorNumeros(num1, num2):
    if num1 > num2:
        return f"El número {num1} es mayor que {num2}"
    elif num1 < num2:
        return f"El número {num1} es menor que {num2}"
    else:
        return f"El número {num1} es igual que {num2}"

# Ejercicio 4: Contador de letras
def contadorLetras(cadena, letraABuscar):
    contador = 0
    for caracter in cadena:
        if caracter == letraABuscar:
            contador += 1
    return contador

# Ejercicio 5: Conteo de todas las letras
def conteoletras(cadena):
    diccionario = {}
    for letra in cadena:
        if letra in diccionario:
            diccionario[letra] += 1
        else:
            diccionario[letra] = 1
    return diccionario

# Ejercicio 6: Gestor de lista
def gestorLista(lista, funcion, elemento=None):
    if funcion.lower() != "add" and funcion.lower() != "remove":
        return "Funcion incorrecta"
    if funcion.lower() == "add":
        lista.append(elemento)
    elif funcion.lower() == "remove":
        try:
            lista.remove(elemento)
        except ValueError:
            return "Elemento no encontrado en la lista"
    return lista

# Ejercicio 7: Crear frase desde palabras
def hacerFrase(lista_palabras):
    return ' '.join(lista_palabras)

# Ejercicio 8: Fibonacci recursivo
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Ejercicio 9: Cálculo de áreas
def calculoAreas(operacion):
    match operacion.lower():
        case "cuadrado":
            lado = float(input("Introduce el lado del cuadrado: "))
            return lado * lado
        case "triangulo":
            base = float(input("Introduce la base del triángulo: "))    
            altura = float(input("Introduce la altura del triángulo: "))
            return (base * altura) / 2
        case "circulo":
            radio = float(input("Introduce el radio del círculo: "))
            return math.pi * radio * radio
        case _:
            return "Operación no válida. Por favor, elige 'cuadrado', 'triangulo' o 'circulo'."
