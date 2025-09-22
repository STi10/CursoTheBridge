"""
Una clase que representa un Perro con atributos y comportamientos básicos.

Atributos de Clase:
    Patas (int): Número de patas, por defecto es 4
    Orejas (int): Número de orejas, por defecto es 2
    Ojos (int): Número de ojos, por defecto es 2

Atributos:
    velocidad (str): Velocidad actual del perro, inicializada como "0"
    raza (str): Raza del perro
    color (str): Color del perro, inicializado como "Marron"
    dueño (bool): Indica si el perro tiene dueño, inicializado como False

Métodos:
    __init__(velocidad, raza, color, dueño): Inicializa una nueva instancia de Perro
    andar(ritmo): Hace que el perro camine a un ritmo dado
    parar(): Detiene el movimiento del perro
    ladrar(comentario): Hace que el perro ladre con un mensaje específico
"""
    Patas = 4  # Atributo de clase
    Orejas =2
    Ojos =2
    def __init__(self,velocidad, raza, color,dueño):
        self.velocidad = "0"
        self.raza = raza
        self.color = "Marron"
        self.dueño = False
    def andar (self , ritmo):
        if self.velocidad == "0":
            self.velocidad = ritmo
        else:
            self.velocidad = ritmo * self.velocidad
        return self.velocidad
    def parar (self):
        self.velocidad = "0"
        return self.velocidad
    def ladrar (self , comentario):
        return f"GUAUU, digo {comentario}"

Perro1 = Perro("0", "Labrador", "Marron", False)
print(Perro1.Patas)
print(Perro1.Orejas)
print(Perro1.Ojos)
print(Perro1.velocidad)
print(Perro1.raza)
print(Perro1.color)
print(Perro1.dueño)
print(Perro1.andar(5))
print(Perro1.velocidad)
print(Perro1.parar())
print(Perro1.velocidad)
print(Perro1.ladrar("Hola que tal"))
print(Perro1.andar(3))
print(Perro1.velocidad)