lista5 = [3, 20, 3, 47, 19, 3, 29, 45, 67, 78, 90, 3, 3]
def ejer5(lista5):
    for i in range(lista5.count(3)):
        lista5.remove(3)
    return lista5
print(ejer5(lista5))