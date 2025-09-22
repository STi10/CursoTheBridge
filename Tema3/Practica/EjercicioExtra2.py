# Crear tablero 10x10 con espacios
tablero = [[" " for _ in range(10)] for _ in range(10)]
global count_barcos
count_barcos = 7
# Insertar barco horizontal de 4 casillas
for j in range(4):
    tablero[1][j] = "B"

# Insertar barco vertical de 3 casillas
for i in range(3, 6):
    tablero[i][3] = "B"

def imprimir_tablero(tab):
    for fila in tab:
        print("|", end=" ")
        for celda in fila:
            print(celda, end=" | ")
        print()

def solicitar_coordenada(letra):
    while True:
        try:
            coord = int(input(f"Introduce coordenada {letra} (0-9): "))
            if 0 <= coord <= 9:
                return coord
            print("Por favor, introduce un número entre 0 y 9")
        except ValueError:
            print("Por favor, introduce un número válido")

def disparar(tab, i, j):
    global count_barcos
    if tab[i][j] == "B":
        tab[i][j] = "X"
        print(f"¡Tocado en posición {i},{j}! te quedan {count_barcos - 1} aciertos.")
        count_barcos -= 1
        if count_barcos == 0:
            print("¡Has hundido todos los barcos!")
            return True
        return True
    elif tab[i][j] == " ":
        tab[i][j] = "O"
        print("¡Agua!")
        return False
    else:
        print("Esta posición ya ha sido disparada")
        return False

# Bucle principal del juego
print("¡Bienvenido a Hundir la Flota!")
print("Tablero inicial:")
imprimir_tablero(tablero)

while True:
    i = solicitar_coordenada("i")
    j = solicitar_coordenada("j")
    
    acierto = disparar(tablero, i, j)
    imprimir_tablero(tablero)
    
    if count_barcos == 0:
        print("¡Felicidades! Has ganado el juego.")
        break

    if not acierto:
        continuar = input("¿Quieres hacer otro disparo? (s/n): ")
        if continuar.lower() != 's':
            break
    