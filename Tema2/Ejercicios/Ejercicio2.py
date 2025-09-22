superficie = float(input("Introduce la superficie en m²: "))
distrito = input("Introduce el distrito en el que se encuentra el domicilio: ").lower()
if((distrito == "moncloa" or distrito == "centro") and superficie < 100):
    print("El precio del domicilio es de 1000 euros.")
elif(distrito == "salamanca" and superficie < 150):
    print("El precio del domicilio es de 1500 euros.")
elif(distrito != "retiro" and superficie >= 60 and superficie <= 80):
    print("El precio del domicilio es de 600 euros.")
else:
    print("El precio del domicilio es de 0 euros.")