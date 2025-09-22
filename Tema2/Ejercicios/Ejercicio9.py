import random
numeroRandom = random.randint(1, 5)
n_vidas = 2
while(n_vidas >= 0):
    numero = int(input("Adivina el número entre 1 y 5: "))
    if(numero == numeroRandom):
        print("¡Has ganado!")
        break
    else:
        n_vidas = n_vidas - 1
        if(n_vidas < 0):
            print("Lo siento, has perdido. El número era", numeroRandom)
        else:
            print("Número incorrecto. Te quedan", n_vidas, "vidas.")